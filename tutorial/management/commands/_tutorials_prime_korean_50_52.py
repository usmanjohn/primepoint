# -*- coding: utf-8 -*-
"""Prime Korean — Block D oxiri, darslar 50–52.

50. 아/어야 하다 / 되다 — majburiyat va zarurat
51. 아/어도 되다 va (으)면 안 되다 — ruxsat va taqiq
52. (으)ㄴ/는/(으)ㄹ 것 같다 — taxmin

PK-50 va PK-51 bitta tizim: kerak · mumkin · mumkin emas · shart emas.
PK-52 esa PK-43…PK-46 dagi aniqlovchi + 것 mashinasini yana ishlatadi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_50_52.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_50_52.py --author=prime
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
        "title": "PK-50: 아/어야 하다 / 되다 — majburiyat va zarurat",
        "category": "korean",
        "order": 50,
        "summary": (
            "“Borishim kerak.” Majburiyatni aytishning asosiy qolipi, uning ichidagi "
            "mantiq va 하다 bilan 되다 orasidagi farq."
        ),
        "stories": ["내일까지 숙제를 내야 해요"],
        "content": """
<h2>PK-50: 아/어야 하다 / 되다 — majburiyat va zarurat</h2>

<p>Kunning yarmi “kerak” degan soʻz bilan oʻtadi: “darsga borishim <b>kerak</b>”,
“dori ichishim <b>kerak</b>”, “ertagacha topshirishim <b>kerak</b>”. Koreys tilida
buning bitta asosiy qolipi bor — <b>아/어야 하다</b>. Va uning ichida chiroyli
mantiq yashiringan: <em>“faqat shunday qilsam, boʻladi”</em>. Shu mantiqni bir
marta koʻrsangiz, qolipni umuman yodlashning hojati qolmaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>아/어야 하다</b> bilan “…ishim kerak” deysiz</li>
    <li><b>하다</b> va <b>되다</b> orasidagi farqni bilib olasiz</li>
    <li>Oʻtgan zamonda “…ishim kerak edi” deysiz</li>
    <li>Qolipning ichidagi mantiqni koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Oʻzak</span>
  <span class="pe-chip pe-chip--v">아/어야</span>
  <span class="pe-chip pe-chip--v">하다 / 되다</span>
  <span class="pe-chip pe-chip--adv">= …ishim kerak</span>
</div>

<h3>1. Yasalishi — yana 아/어요 shaklidan</h3>

<p>Tanish yoʻl: <b>아/어요</b> shaklini oling, <b>요</b> ni olib tashlang,
oʻrniga <b>야 하다</b> qoʻying.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>아/어요</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>가다</td><td class="pk-stem">가요</td>
      <td class="pk-res">가야 해요</td><td class="pk-uz">borishim kerak</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹어요</td>
      <td class="pk-res">먹어야 해요</td><td class="pk-uz">yeyishim kerak</td></tr>
  <tr><td>하다</td><td class="pk-stem">해요</td>
      <td class="pk-res">해야 해요</td><td class="pk-uz">qilishim kerak</td></tr>
  <tr><td>듣다</td><td class="pk-stem">들어요</td>
      <td class="pk-res">들어야 해요</td><td class="pk-uz">tinglashim kerak</td></tr>
  <tr><td>돕다</td><td class="pk-stem">도와요</td>
      <td class="pk-res">도와야 해요</td><td class="pk-uz">yordam berishim kerak</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Oxirgi ikki qatorga eʼtibor bering: 아/어 unli bilan boshlanadi, shuning
  uchun PK-32 va PK-47 dagi notoʻgʻri feʼllar bu yerda <b>ishlaydi</b>:
  듣다 → 들어야, 돕다 → 도와야, 부르다 → <b>불러야</b>, 짓다 → <b>지어야</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 내일 <span class="pe-hl pe-hl--v">일찍 일어나야
     해요</span>.</p>
  <p class="pe-ex__uz">Men ertaga erta turishim kerak.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">약을 <span class="pe-hl pe-hl--v">먹어야 해요</span>.</p>
  <p class="pe-ex__uz">Dori ichishim kerak.</p>
</div>

<h3>2. Qolipning ichidagi mantiq</h3>

<p>Nega aynan <b>야</b>? Bu — “faqat, aynan” degan qoʻshimcha. Yaʼni
가<b>야</b> 해요 soʻzma-soʻz “<em>faqat borsam — boʻladi</em>” degani. Boshqa
yoʻl yoʻq, demak borish kerak.</p>

<div class="pe-call pe-rule">
  <p><b>가야 해요</b> = “faqat borish — ish boʻladi” → “borishim kerak”.<br>
  Shuning uchun bu qolip <em>yagona yoʻl</em>ni koʻrsatadi. Boshqa variantlar
  yopiq boʻlgani uchun majburiyat kelib chiqadi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham “kerak” alohida soʻz.</b> “Bor<em>ishim</em>
  <b>kerak</b>” — bu ikki boʻlak: feʼlning ot shakli va “kerak”. Koreyschada
  ham shunday: 가<b>야</b> + <b>해요</b>. Ingliz tilida esa bitta soʻz bilan
  chiqadi (“must”), shuning uchun ingliz tilidan oʻrganayotgan odam koreyscha
  qolipning ikki qismli ekanini gʻalati deb topadi. Siz uchun esa bu tabiiy —
  ona tilingizda ham xuddi shunday.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu qolipning oʻz inkori yoʻq — va bu muhim.</b> Oʻzbekchada “borishim
  kerak” ning inkori “borishim <em>shart emas</em>” yoki “borishim
  <em>mumkin emas</em>” boʻladi — ikki xil maʼno, ikki xil ibora. Koreys tili
  ham xuddi shunday ishlaydi: <s>안 가야 해요</s> deb inkor qilinmaydi, buning
  oʻrniga butunlay boshqa qoliplar ishlatiladi. Ularni <b>keyingi darsda</b>
  olasiz. Hozircha shuni bilib qoʻying: 아/어야 하다 faqat <em>ijobiy</em>
  majburiyat uchun.</p>
</div>

<h3>3. 하다 yoki 되다?</h3>

<p>Ikkalasi ham toʻgʻri va deyarli har doim oʻrin almasha oladi:
가야 <b>해요</b> = 가야 <b>돼요</b>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">아/어야 하다</p>
    <p>Biroz <b>rasmiyroq</b>, yozma nutqda koʻproq.</p>
    <p>Koʻproq <em>shaxsiy burch</em> tuygʻusi.</p>
    <p><small>매일 공부해야 합니다.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">아/어야 되다</p>
    <p>Biroz <b>ogʻzakiroq</b>, kundalik suhbatda koʻproq.</p>
    <p>Koʻproq <em>vaziyat talab qilyapti</em> tuygʻusi.</p>
    <p><small>지금 가야 돼요.</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p>Boshlangʻich darajada bu farqni oʻylab oʻtirmang — qaysi biri esingizga
  kelsa, oʻshani ishlating. TOPIK da ikkalasi ham toʻgʻri hisoblanadi.</p>
</div>

<h3>4. Oʻtgan zamon: “…ishim kerak edi”</h3>

<p>Zamon oxirdagi <b>하다 / 되다</b> ga qoʻyiladi — 야 ga emas:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 병원에 <span class="pe-hl pe-hl--v">가야
     했어요</span>.</p>
  <p class="pe-ex__uz">Kecha shifoxonaga borishim kerak edi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>어제 갔어야 해요.</s></p>
  <p class="pe-good">어제 <b>가야 했어요</b>.</p>
  <p><small>Zamon 하다 da turadi. Bu — butun kurs boʻyicha takrorlanayotgan
  qoida: zamon gapning oxirida.</small></p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada “boʻlishi” soʻzi qoʻshiladi — koreyschada esa yoʻq.</b>
  “Xona toza <em>boʻlishi</em> kerak” — biz sifatga alohida feʼl qoʻshamiz.
  Koreyschada esa sifatning oʻzi tuslanadi: 깨끗하다 → 깨끗해<b>야</b> 해요.
  Yaʼni koreys tilida sifat ham feʼlga oʻxshab ishlaydi — bu PK-45 dan beri
  koʻrib kelayotgan narsangiz. Shuning uchun “boʻlishi” ni qoʻshishga urinmang,
  shunchaki sifatni 아/어요 shakliga qoʻying.</p>
</div>

<h3>5. Sifatlar bilan ham ishlaydi</h3>

<p>Bu qolip faqat feʼllar bilan cheklanmagan — sifat bilan ham keladi va
“shunday boʻlishi kerak” degan maʼno beradi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">방이 <span class="pe-hl pe-hl--adv">깨끗해야 해요</span>.</p>
  <p class="pe-ex__uz">Xona toza boʻlishi kerak.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시험 문제가 <span class="pe-hl pe-hl--adv">쉬워야
     해요</span>.</p>
  <p class="pe-ex__uz">Imtihon savollari oson boʻlishi kerak.</p>
  <p class="pe-ex__why">쉽다 → 쉬워 (ㅂ notoʻgʻri sifati) → 쉬워야 해요.</p>
</div>

<h3>6. Ot bilan: 이어야 / 여야 하다</h3>

<p>Ot bilan kelganda <b>이다</b> tuslanadi: 받침 bor → <b>이어야</b>,
받침 yoʻq → <b>여야</b>.</p>

<ul>
  <li>학생<b>이어야</b> 해요 — talaba boʻlishi kerak</li>
  <li>친구<b>여야</b> 해요 — doʻst boʻlishi kerak</li>
</ul>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>학교에 가야 있어요.</s></p>
  <p class="pe-good">학교에 <b>가야 해요</b>.</p>
  <p><small>야 dan keyin 하다 yoki 되다 keladi — 있다 emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음악을 듣어야 해요.</s></p>
  <p class="pe-good">음악을 <b>들어야</b> 해요.</p>
  <p><small>듣다 — ㄷ notoʻgʻri feʼli, 아/어 unli bilan boshlanadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>어제 갔어야 했어요 (“kecha borishim kerak edi”
  maʼnosida)</s></p>
  <p class="pe-good">어제 <b>가야 했어요</b>.</p>
  <p><small>Zamon ikki marta qoʻyilmaydi — faqat 하다 da.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>방이 깨끗하야 해요.</s></p>
  <p class="pe-good">방이 <b>깨끗해야</b> 해요.</p>
  <p><small>하다 → 해요 → 해야. 하야 degan shakl yoʻq.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 내일 일찍
  <span class="pe-blank"></span> (일어나다) 해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>일어나야</b> — 일어나요 → 요 oʻrniga 야: 일어나야 해요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 이 노래를
  <span class="pe-blank"></span> (듣다) 해요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>들어야</b> — 듣다 → 들어요 → <b>들어야 해요</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Xatoni toping:
  <s>어제 약을 먹었어야 해요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>어제 약을 먹어야 했어요.</b> Zamon oxirdagi 하다 ga
    qoʻyiladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 가야 해요 va 가야 돼요 — farqi bormi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Deyarli yoʻq. <b>하다</b> biroz rasmiyroq, <b>되다</b> biroz
    ogʻzakiroq. Ikkalasi ham toʻgʻri va oʻrin almasha oladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Xona toza
  boʻlishi kerak.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>방이 깨끗해야 해요.</b> 깨끗하다 → 깨끗해요 → 깨끗해야 해요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> 가야 해요 dagi <b>야</b> nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>야</b> — “faqat, aynan”. Yaʼni “faqat borsam — boʻladi”, boshqa yoʻl
    yoʻq. Shundan majburiyat maʼnosi kelib chiqadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아/어야 하다 / 되다</b> — …ishi kerak</li>
  <li><b>일어나다</b> — turmoq, uygʻonmoq</li>
  <li><b>약</b> — dori</li>
  <li><b>일찍</b> — erta</li>
  <li><b>깨끗하다</b> — toza</li>
  <li><b>방</b> — xona</li>
  <li><b>내다</b> — topshirmoq, berib qoʻymoq</li>
  <li><b>까지</b> — …gacha</li>
  <li><b>문제</b> — masala, savol</li>
  <li><b>병원</b> — shifoxona</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>아/어야 하다 / 되다</b> = “…ishi kerak”. 아/어요 shaklidan yasaladi.</li>
    <li>아/어 unli, shuning uchun notoʻgʻri feʼllar ishlaydi: 들어야, 도와야,
      불러야.</li>
    <li><b>하다</b> — rasmiyroq · <b>되다</b> — ogʻzakiroq. Ikkalasi toʻgʻri.</li>
    <li>Zamon oxirdagi 하다/되다 ga qoʻyiladi: 가야 <b>했어요</b>.</li>
    <li>Sifat bilan ham keladi: 깨끗해야 해요.</li>
    <li>Ot bilan: 학생<b>이어야</b> 해요 · 친구<b>여야</b> 해요.</li>
    <li>Ichidagi mantiq: <b>야</b> = “faqat” → “faqat shunday qilsam, boʻladi”.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-51: 아/어도 되다 va (으)면 안 되다 — ruxsat va taqiq",
        "category": "korean",
        "order": 51,
        "summary": (
            "“Mumkinmi?” va “mumkin emas”. Ruxsat soʻrash, ruxsat berish, taqiqlash — "
            "va kursning eng koʻp chalkashtiriladigan juftligi: “shart emas” va "
            "“mumkin emas”."
        ),
        "stories": ["여기에서 사진을 찍어도 돼요?"],
        "content": """
<h2>PK-51: 아/어도 되다 va (으)면 안 되다 — ruxsat va taqiq</h2>

<p>Muzeyga kirdingiz va suratga olmoqchisiz. Qanday soʻraysiz? Yoki avtobusda
ovqat yeyayotgan edingiz va kimdir sizni toʻxtatdi — u nima dedi? Oʻtgan darsda
siz “kerak” ni oʻrgandingiz; bugun uning ikki qoʻshnisi keladi:
<b>mumkin</b> va <b>mumkin emas</b>. Va darsning oxirida kursdagi eng koʻp
chalkashtiriladigan juftlikni ajratasiz — “<em>shart emas</em>” va
“<em>mumkin emas</em>”.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>아/어도 되다</b> bilan ruxsat soʻraysiz va berasiz</li>
    <li><b>(으)면 안 되다</b> bilan taqiqlaysiz</li>
    <li><b>아/어도</b> — “…sa ham” — qolipini oʻrganasiz</li>
    <li>“Shart emas” va “mumkin emas” ni bir umrga ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ruxsat</span>
  <span class="pe-chip pe-chip--s">Oʻzak</span>
  <span class="pe-chip pe-chip--v">아/어도 되다</span>
  <span class="pe-chip pe-chip--adv">= …sa ham boʻladi</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Taqiq</span>
  <span class="pe-chip pe-chip--s">Oʻzak</span>
  <span class="pe-chip pe-chip--neg">(으)면 안 되다</span>
  <span class="pe-chip pe-chip--adv">= …sa boʻlmaydi</span>
</div>

<h3>1. Avval bir gʻisht: 아/어도 = “…sa ham”</h3>

<p>Ikkala qolipni tushunish uchun avval <b>아/어도</b> ni bilish kerak. U
“…sa ham” degani — yaʼni birinchi qism ikkinchisiga <em>toʻsqinlik
qilmaydi</em>:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">비가 <span class="pe-hl pe-hl--adv">와도</span>
     학교에 가요.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻsa ham maktabga boraman.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu — oʻzbekcha bilan toʻliq moslik.</b> 아/어도 = “-<em>sa ham</em>”.
  비가 와도 = “yomgʻir yogʻ<b>sa ham</b>”, 어려워도 = “qiyin boʻl<b>sa
  ham</b>”. Soʻz tartibi ham, mantigʻi ham bir xil. Va endi qarang:
  <b>아/어도 되다</b> soʻzma-soʻz “…<em>sa ham boʻladi</em>” degani — bu
  oʻzbekchada aynan shunday aytiladigan ibora! Yaʼni bu qolipni yodlamang,
  shunchaki oʻzbekcha oʻylang.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ruxsat soʻrash iborasini eslang:</b> “bor<em>sam</em>
  <b>maylimi</b>?”, “oʻqi<em>sa</em> <b>boʻladimi</b>?”. Biz ham feʼlni shart
  shakliga qoʻyib, keyin “boʻladimi” deymiz. Koreyschada aynan shu:
  가<b>도</b> <b>돼요?</b> — “borsa ham boʻladimi?”. Ikki tilda bir xil
  mantiq, faqat qoʻshimchalar boshqa. Shuning uchun bu darsni yodlash emas,
  <em>moslashtirish</em> deb qarang.</p>
</div>

<h3>2. 아/어도 되다 — ruxsat</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">여기에서 사진을 <span class="pe-hl pe-hl--v">찍어도
     돼요</span>?</p>
  <p class="pe-ex__uz">Bu yerda surat olsam boʻladimi?</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">네, <span class="pe-hl pe-hl--v">찍어도 돼요</span>.</p>
  <p class="pe-ex__uz">Ha, olsangiz boʻladi.</p>
</div>

<p><b>되다</b> oʻrniga <b>괜찮다</b> yoki <b>좋다</b> ham ishlatiladi — maʼnosi
bir xil:</p>

<ul>
  <li>먹어도 <b>돼요</b> — yesangiz boʻladi</li>
  <li>먹어도 <b>괜찮아요</b> — yesangiz ham hech gap emas</li>
  <li>먹어도 <b>좋아요</b> — yesangiz ham yaxshi</li>
</ul>

<h3>3. (으)면 안 되다 — taqiq</h3>

<p>Taqiq esa <b>(으)면</b> (PK-36) ustiga qurilgan: “…sa — boʻlmaydi”.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">면 안 되다</span></p>
    <p>가다 → 가면 안 돼요</p>
    <p>하다 → 하면 안 돼요</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">으면 안 되다</span></p>
    <p>먹다 → 먹으면 안 돼요</p>
    <p>앉다 → 앉으면 안 돼요</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">여기에서 <span class="pe-hl pe-hl--neg">사진을 찍으면
     안 돼요</span>.</p>
  <p class="pe-ex__uz">Bu yerda surat olsangiz boʻlmaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">수업 시간에 <span class="pe-hl pe-hl--neg">전화하면
     안 돼요</span>.</p>
  <p class="pe-ex__uz">Dars vaqtida telefon qilsangiz boʻlmaydi.</p>
</div>

<h3>4. Savol va javob</h3>

<p>Ruxsat soʻralganda javoblar shunday boʻladi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">Savol</p>
    <p>들어가도 돼요?<br><small>Kirsam boʻladimi?</small></p></div>
  <div class="pe-card"><p class="pe-card__h">Ha</p>
    <p>네, 들어가도 돼요.<br><small>Ha, kirsangiz boʻladi.</small></p></div>
  <div class="pe-card"><p class="pe-card__h">Yoʻq</p>
    <p>아니요, 들어가면 안 돼요.<br><small>Yoʻq, kirsangiz boʻlmaydi.</small></p></div>
</div>

<div class="pe-call pe-tip">
  <p>Diqqat: savol <b>아/어도</b> bilan, rad javobi esa <b>(으)면</b> bilan
  tuziladi. Yaʼni “yoʻq” deyish uchun qolipni <em>almashtirish</em> kerak —
  <s>안 들어가도 돼요</s> deb javob bersangiz, butunlay boshqa maʼno chiqadi.
  Buni keyingi boʻlimda koʻramiz.</p>
</div>

<h3>5. Kursning eng koʻp chalkashtiriladigan juftligi</h3>

<p>Mana shu ikki gapni yonma-yon qoʻying va farqni yaxshilab koʻring:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">안 가도 돼요</p>
    <p><b>Shart emas.</b></p>
    <p>Borish majburiy emas — xohlasangiz boring, xohlamasangiz yoʻq.</p>
    <p><small>Oʻzbekcha: “bormasangiz ham boʻladi”.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">가면 안 돼요</p>
    <p><b>Mumkin emas.</b></p>
    <p>Borish taqiqlangan — bormasligingiz kerak.</p>
    <p><small>Oʻzbekcha: “borsangiz boʻlmaydi”.</small></p>
  </div>
</div>

<div class="pe-call pe-warn">
  <p><b>Bu ikkisi bir-biriga umuman yaqin emas</b>, lekin shakli oʻxshash
  boʻlgani uchun juda koʻp aralashtiriladi. Farqni ushlash uchun
  <b>inkor qayerda turganiga</b> qarang: <b>안 가도</b> 돼요 da inkor
  <em>birinchi</em> feʼlda (bormaslik — mumkin), <b>가면 안</b> 돼요 da esa
  inkor <em>oxirida</em> (borish — boʻlmaydi).</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Yaxshi xabar: toʻrtta tushuncha sizda allaqachon bor.</b> Oʻzbek
  tilida ham “kerak”, “mumkin”, “mumkin emas” va “shart emas” — toʻrt xil
  alohida ibora, va siz ularni hech qachon aralashtirmaysiz. Demak bu darsda
  yangi <em>fikr</em> emas, yangi <em>shakl</em> oʻrganyapsiz. Toʻrtta oʻzbekcha
  iborani yozib qoʻying va yoniga koreyschasini qoʻying — shu jadval yetadi.</p>
</div>

<h3>6. Toʻrtta qolip — bitta jadval</h3>

<p>Oʻtgan dars bilan birga endi sizda toʻliq tizim bor:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Maʼnosi</th><th>Qolip</th><th>Misol</th></tr>
  <tr><td class="pk-uz">kerak</td><td class="pk-res">아/어야 하다</td>
      <td>가야 해요</td></tr>
  <tr><td class="pk-uz">mumkin</td><td class="pk-res">아/어도 되다</td>
      <td>가도 돼요</td></tr>
  <tr><td class="pk-uz">mumkin emas</td><td class="pk-res">(으)면 안 되다</td>
      <td>가면 안 돼요</td></tr>
  <tr><td class="pk-uz">shart emas</td><td class="pk-res">안 …아/어도 되다</td>
      <td>안 가도 돼요</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>여기에서 담배를 피우도 돼요?</s></p>
  <p class="pe-good">여기에서 담배를 <b>피워도</b> 돼요?</p>
  <p><small>아/어요 shaklidan yasaladi: 피우다 → 피워요 → 피워도.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>여기에서 먹면 안 돼요.</s></p>
  <p class="pe-good">여기에서 <b>먹으면</b> 안 돼요.</p>
  <p><small>먹 da 받침 bor → 으면.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad">— 들어가도 돼요? — <s>아니요, 안 들어가도 돼요.</s></p>
  <p class="pe-good">— 들어가도 돼요? — 아니요, <b>들어가면 안 돼요</b>.</p>
  <p><small>안 들어가도 돼요 — “kirmasangiz ham boʻladi”, yaʼni ruxsat
  bermayotgani emas, majburiy emasligini aytyapti.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음악을 듣어도 돼요?</s></p>
  <p class="pe-good">음악을 <b>들어도</b> 돼요?</p>
  <p><small>듣다 — ㄷ notoʻgʻri feʼli, 아/어 unli bilan boshlanadi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 여기에 <span class="pe-blank"></span>
  (앉다) 돼요?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>앉아도</b> — 앉아요 → 앉아도 돼요? (“Bu yerga oʻtirsam boʻladimi?”)</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 도서관에서 <span class="pe-blank"></span>
  (먹다) 안 돼요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>먹으면</b> — 먹 da 받침 bor → 먹으면 안 돼요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Farqini ayting: 안 와도 돼요 va
  오면 안 돼요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>안 와도 돼요</b> — “kelmasangiz ham boʻladi” (shart emas).
    <b>오면 안 돼요</b> — “kelsangiz boʻlmaydi” (taqiq). Inkorning oʻrniga
    qarang.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> “들어가도 돼요?” savoliga <em>rad</em>
  javobi qanday boʻladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>아니요, 들어가면 안 돼요.</b> Rad javobida qolip almashadi:
    아/어도 → (으)면 안 되다.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Yomgʻir yogʻsa
  ham maktabga boraman.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>비가 와도 학교에 가요.</b> 아/어도 — “…sa ham”. Bu — bugungi ikkala
    qolipning asosi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Toʻrtta qolipni ayting: kerak · mumkin ·
  mumkin emas · shart emas (가다 bilan).</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>가야 해요</b> (kerak) · <b>가도 돼요</b> (mumkin) ·
    <b>가면 안 돼요</b> (mumkin emas) · <b>안 가도 돼요</b> (shart emas).</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아/어도</b> — …sa ham</li>
  <li><b>아/어도 되다</b> — …sa ham boʻladi (ruxsat)</li>
  <li><b>(으)면 안 되다</b> — …sa boʻlmaydi (taqiq)</li>
  <li><b>사진을 찍다</b> — surat olmoq</li>
  <li><b>들어가다</b> — kirmoq</li>
  <li><b>담배를 피우다</b> — chekmoq</li>
  <li><b>수업 시간</b> — dars vaqti</li>
  <li><b>괜찮다</b> — yaxshi, hech gap emas</li>
  <li><b>박물관</b> — muzey</li>
  <li><b>조용히</b> — jimgina</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>아/어도</b> = “…sa ham” — ikkala qolipning asosi.</li>
    <li><b>아/어도 되다</b> — ruxsat: 가도 돼요. 괜찮다, 좋다 ham ishlaydi.</li>
    <li><b>(으)면 안 되다</b> — taqiq: 가면 안 돼요.</li>
    <li>Ruxsat savoliga <b>rad</b> javobi qolipni almashtiradi:
      아니요, …(으)면 안 돼요.</li>
    <li><b>안 가도 돼요</b> (shart emas) va <b>가면 안 돼요</b> (mumkin emas) —
      aralashtirmang. Inkorning oʻrniga qarang.</li>
    <li>Toʻliq tizim: 가야 해요 · 가도 돼요 · 가면 안 돼요 · 안 가도 돼요.</li>
    <li>아/어 unli, shuning uchun notoʻgʻri feʼllar ishlaydi: 들어도 돼요.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-52: (으)ㄴ/는/(으)ㄹ 것 같다 — taxmin",
        "category": "korean",
        "order": 52,
        "summary": (
            "“…ga oʻxshaydi”, “shekilli”. Aniqlovchi + 것 mashinasi yana ishlaydi — "
            "va koreyslar nega bilgan narsasini ham shu qolip bilan aytadi."
        ),
        "stories": ["비가 올 것 같아요"],
        "content": """
<h2>PK-52: (으)ㄴ/는/(으)ㄹ 것 같다 — taxmin</h2>

<p>Osmonga qaraysiz — bulut qora. “Yomgʻir <b>yogʻadiganga oʻxshaydi</b>”, deysiz.
Aniq bilmaysiz, lekin taxminingiz bor. Koreys tilida bu <b>것 같다</b> bilan
aytiladi, va yaxshi xabar shuki, siz uning hamma qismini allaqachon bilasiz:
<b>aniqlovchi</b> (PK-43, 44, 45) + <b>것</b> (PK-46). Bugun faqat ularni
birlashtiramiz — va oxirida bir madaniy sirni ochamiz: koreyslar <em>bilgan</em>
narsasini ham koʻpincha shu qolip bilan aytadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uch zamonda taxmin qilishni oʻrganasiz</li>
    <li>Feʼl va sifat orasidagi tuzoqni koʻrasiz</li>
    <li><b>거 같아요</b> qisqargan shaklini tanib olasiz</li>
    <li>Nega koreyslar bu qolipni shunchalik koʻp ishlatishini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Aniqlovchi</span>
  <span class="pe-chip pe-chip--o">것</span>
  <span class="pe-chip pe-chip--v">같다</span>
  <span class="pe-chip pe-chip--adv">= …ga oʻxshaydi</span>
</div>

<h3>1. Feʼllar bilan — uch zamon</h3>

<p>Aniqlovchining qaysi shaklini tanlasangiz, taxminingiz oʻsha zamonga tegishli
boʻladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>Zamoni</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">(으)ㄴ 것 같다</td><td class="pk-uz">oʻtgan</td>
      <td>비가 <b>온</b> 것 같아요</td><td>yomgʻir yoqqanga oʻxshaydi</td></tr>
  <tr><td class="pk-res">는 것 같다</td><td class="pk-uz">hozirgi</td>
      <td>비가 <b>오는</b> 것 같아요</td><td>yomgʻir yogʻayotganga oʻxshaydi</td></tr>
  <tr><td class="pk-res">(으)ㄹ 것 같다</td><td class="pk-uz">kelasi</td>
      <td>비가 <b>올</b> 것 같아요</td><td>yomgʻir yogʻadiganga oʻxshaydi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">지영 씨가 지금 <span class="pe-hl pe-hl--v">공부하는 것
     같아요</span>.</p>
  <p class="pe-ex__uz">Chiyong hozir dars qilayotganga oʻxshaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">밖에 눈이 <span class="pe-hl pe-hl--v">올 것 같아요</span>.</p>
  <p class="pe-ex__uz">Tashqarida qor yogʻadiganga oʻxshaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada buning bir nechta juftligi bor</b> va hammasi ishlaydi:
  “…ga <em>oʻxshaydi</em>”, “<em>shekilli</em>”, “…<em>ga oʻxshab turibdi</em>”,
  “-<em>dir</em>”. 비가 올 것 같아요 = “yomgʻir yogʻ<b>sa kerak</b>” yoki
  “yogʻadigan<b>ga oʻxshaydi</b>”. Muhimi shundaki, oʻzbekchada ham bu iboralar
  <b>gap oxirida</b> turadi — koreyschadagidek. Shuning uchun tarjima
  qilganda soʻz tartibini oʻzgartirish kerak emas.</p>
</div>

<h3>2. Sifatlar bilan — va bu yerda tuzoq bor</h3>

<p>Sifat bilan <b>(으)ㄴ 것 같다</b> ishlatiladi, lekin u <em>oʻtgan zamon
emas</em> — hozirgi zamon:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">이 음식이 <span class="pe-hl pe-hl--adv">매운 것
     같아요</span>.</p>
  <p class="pe-ex__uz">Bu taom achchiqqa oʻxshaydi.</p>
  <p class="pe-ex__why">맵다 — sifat, shuning uchun 매운 것 같다 “hozir achchiq”
  degani.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>PK-45 dagi tuzoq yana qaytdi.</b> <b>(으)ㄴ 것 같다</b> feʼl bilan
  <em>oʻtgan zamon</em>, sifat bilan <em>hozirgi zamon</em> bildiradi:<br>
  먹<b>은</b> 것 같아요 — “yeganga oʻxshaydi” (feʼl → oʻtgan)<br>
  매<b>운</b> 것 같아요 — “achchiqqa oʻxshaydi” (sifat → hozirgi)<br>
  Shakl bir xil, maʼnoni <b>soʻzning turi</b> hal qiladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Tuzoqdan chiqishning oʻzbekcha yoʻli.</b> 먹은 것 같아요 va
  매운 것 같아요 shakli bir xil, lekin oʻzbekchaga oʻgirsangiz farq darrov
  koʻrinadi: “ye<em>gan</em>ga oʻxshaydi” (ish, tugagan) va “achchiq<em>qa</em>
  oʻxshaydi” (xususiyat, hozir). Yaʼni oʻzbek tili bu ikkisini ikki xil
  soʻz turkumiga ajratadi va sizga bepul javob beradi. Koreyscha shaklga emas,
  <b>soʻzning maʼnosiga</b> qarang: harakatmi yoki xususiyatmi?</p>
</div>

<h3>3. Ot bilan: 인 것 같다</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">저분은 <span class="pe-hl pe-hl--s">선생님인 것
     같아요</span>.</p>
  <p class="pe-ex__uz">Anavi kishi oʻqituvchiga oʻxshaydi.</p>
  <p class="pe-ex__why">이다 + (으)ㄴ → <b>인</b>.</p>
</div>

<h3>4. Qisqargan shakl: 거 같아요</h3>

<p>PK-46 dagi qoida bu yerda ham ishlaydi — ogʻzaki nutqda <b>것</b> qisqaradi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">Yozma</p>
    <p>올 <b>것</b> 같아요</p></div>
  <div class="pe-card"><p class="pe-card__h">Ogʻzaki</p>
    <p>올 <b>거</b> 같아요</p></div>
</div>

<p>Koreyslar deyarli har doim <b>거 같아요</b> deb gapiradi. Yozma matnda esa
<b>것 같아요</b> yoziladi — TOPIK da ham shunday.</p>

<h3>5. Nega koreyslar buni shunchalik koʻp ishlatadi?</h3>

<p>Endi eng qiziq qismi. Koreyslar <b>것 같다</b> ni faqat taxmin qilish uchun
emas, <b>fikrini yumshatish</b> uchun ham ishlatadi. Masalan, taomni yeb
turib:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">맛있어요</p>
    <p>“Mazali.” — qatʼiy hukm.</p>
    <p>Toʻgʻri, lekin biroz keskin eshitiladi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">맛있는 것 같아요</p>
    <p>“Mazaliga oʻxshaydi.” — yumshoq fikr.</p>
    <p>Odam taomni yeb turibdi va mazasini biladi — lekin baribir shunday
    deydi.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham bu odat bor.</b> Biz ham “menimcha”, “shekilli”,
  “nazarimda” deb fikrni yumshatamiz — hatto ishonchimiz komil boʻlsa ham.
  Koreys madaniyatida esa bu yanada kuchliroq: oʻz fikrini qatʼiy aytish
  bir oz manmanlik deb qabul qilinadi. Shuning uchun 것 같아요 ni koʻp
  eshitasiz — va agar siz ham ishlatsangiz, koreyscha nutqingiz darrov
  tabiiyroq boʻlib qoladi. Bu — grammatikadan koʻra <b>madaniyat</b> darsi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>비가 오는 것 같았어요 (“yomgʻir yogʻadiganga oʻxshaydi”
  maʼnosida)</s></p>
  <p class="pe-good">비가 <b>올</b> 것 같아요.</p>
  <p><small>Hali boʻlmagan ish → (으)ㄹ. Zamonni aniqlovchi bildiradi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>이 음식이 매웠는 것 같아요.</s></p>
  <p class="pe-good">이 음식이 <b>매운</b> 것 같아요.</p>
  <p><small>맵다 — sifat, (으)ㄴ oladi. Sifat 는 olmaydi (PK-45).</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>저분은 선생님 것 같아요.</s></p>
  <p class="pe-good">저분은 <b>선생님인</b> 것 같아요.</p>
  <p><small>Ot bilan 이다 tuslanadi: 선생님 + 인.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>지금 공부한 것 같아요 (“hozir oʻqiyaptiga oʻxshaydi”
  maʼnosida)</s></p>
  <p class="pe-good">지금 <b>공부하는</b> 것 같아요.</p>
  <p><small>Hozirgi zamon → 는. 공부한 것 같아요 “oʻqiganga oʻxshaydi”
  degani.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 밖에 비가
  <span class="pe-blank"></span> (오다) 것 같아요. (“yogʻadiganga oʻxshaydi”)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>올</b> — hali boʻlmagan ish → (으)ㄹ: 올 것 같아요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 이 문제가
  <span class="pe-blank"></span> (어렵다) 것 같아요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>어려운</b> — 어렵다 sifat, ㅂ → 우: 어려운 것 같아요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Farqini ayting: 먹은 것 같아요 va
  매운 것 같아요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>먹은 것 같아요</b> — “yeganga oʻxshaydi” (먹다 feʼl → oʻtgan zamon).
    <b>매운 것 같아요</b> — “achchiqqa oʻxshaydi” (맵다 sifat → hozirgi zamon).
    PK-45 dagi tuzoqning oʻzi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Xatoni toping:
  <s>저분은 의사 것 같아요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>저분은 의사인 것 같아요.</b> Ot bilan 이다 tuslanadi:
    의사 + 인.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Chiyong hozir dars
  qilayotganga oʻxshaydi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>지영 씨가 지금 공부하는 것 같아요.</b> Hozirgi zamon → 는.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Nega koreys odam taomni yeb turib
  “맛있어요” emas, “맛있는 것 같아요” deydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Fikrini <b>yumshatish</b> uchun. Koreys madaniyatida oʻz fikrini qatʼiy
    aytish biroz keskin eshitiladi, shuning uchun bilgan narsani ham
    것 같아요 bilan aytish odat.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄴ/는/(으)ㄹ 것 같다</b> — …ga oʻxshaydi, shekilli</li>
  <li><b>거 같아요</b> — 것 같아요 ning ogʻzaki shakli</li>
  <li><b>인 것 같다</b> — … boʻlsa kerak (ot bilan)</li>
  <li><b>같다</b> — oʻxshamoq, bir xil boʻlmoq</li>
  <li><b>저분</b> — anavi kishi (hurmat bilan)</li>
  <li><b>밖</b> — tashqari</li>
  <li><b>구름</b> — bulut</li>
  <li><b>의사</b> — shifokor</li>
  <li><b>하늘</b> — osmon</li>
  <li><b>우산</b> — soyabon</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>Aniqlovchi + 것 + 같다</b> — hammasi tanish qismlardan yigʻilgan.</li>
    <li>Feʼl: (으)ㄴ (oʻtgan) · 는 (hozirgi) · (으)ㄹ (kelasi).</li>
    <li>Sifat: <b>(으)ㄴ</b> — lekin bu <em>hozirgi</em> zamon: 매운 것 같아요.</li>
    <li>Ot: <b>인 것 같다</b> — 선생님인 것 같아요.</li>
    <li>Ogʻzaki nutqda 것 → <b>거</b>: 올 거 같아요.</li>
    <li>Zamonni aniqlovchi bildiradi — 같다 ga qoʻyilmaydi.</li>
    <li>Koreyslar buni fikrni <b>yumshatish</b> uchun ham ishlatadi: bilgan
      narsasini ham 것 같아요 bilan aytadi.</li>
  </ul>
</div>
""",
    },
]
