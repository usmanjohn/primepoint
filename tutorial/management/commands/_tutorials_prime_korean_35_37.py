# -*- coding: utf-8 -*-
"""Prime Korean — Block C oxiri + Block D boshi, darslar 35–37.

35. 아/어서 — sabab va bogʻliq ketma-ketlik
36. (으)면 — shart va faraz
37. 보다 / 제일 · 가장 — taqqoslash

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_35_37.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_35_37.py --author=prime
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
        "title": "PK-35: 아/어서 — sabab va vaqt ketma-ketligi",
        "category": "korean",
        "order": 35,
        "summary": (
            "“…gani uchun” va bogʻliq “…ib”. Koreys tilidagi eng koʻp ishlatiladigan "
            "sabab qolipi, uning ikki qatʼiy taqiqi va 고 dan farqi."
        ),
        "stories": ["배가 아파서 학교에 못 갔어요"],
        "content": """
<h2>PK-35: 아/어서 — sabab va vaqt ketma-ketligi</h2>

<p>Oʻtgan darsda siz ikki gapni <b>고</b> bilan qoʻshdingiz. Lekin “Qornim ogʻridi
<em>shuning uchun</em> shifoxonaga bordim” degan gapni 고 koʻtara olmaydi — u
shunchaki sanaydi, sabab koʻrsatmaydi. Kerakli qolip — <b>아/어서</b>. Bu koreys
tilidagi eng koʻp ishlatiladigan bogʻlovchi qoʻshimcha, va uning ikkita qatʼiy
taqiqi bor: ularni bilmasangiz, gap darrov notabiiy boʻlib qoladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>아/어서</b> bilan sabab koʻrsatishni oʻrganasiz</li>
    <li>Uning ikkinchi vazifasini — <em>bogʻliq</em> ketma-ketlikni — koʻrasiz</li>
    <li>Ikkita qatʼiy taqiqni yod olasiz: zamon yoʻq, buyruq yoʻq</li>
    <li><b>고</b> bilan <b>아/어서</b> ni ishonch bilan ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">A oʻzak</span>
  <span class="pe-chip pe-chip--v">아/어서</span>
  <span class="pe-chip pe-chip--opt">+</span>
  <span class="pe-chip pe-chip--s">B natija</span>
</div>

<h3>1. Yasalishi — bu siz bilgan 아/어 shakli</h3>

<p>Yangi narsa yoʻq: PK-18 dagi <b>아/어요</b> shaklidan 요 ni olib tashlang va
oʻrniga <b>서</b> qoʻying.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>아/어요</th><th>아/어서</th><th>Maʼnosi</th></tr>
  <tr><td>가다</td><td class="pk-stem">가요</td><td class="pk-res">가서</td>
      <td class="pk-uz">borib / borgani uchun</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹어요</td><td class="pk-res">먹어서</td>
      <td class="pk-uz">yeb / yegani uchun</td></tr>
  <tr><td>하다</td><td class="pk-stem">해요</td><td class="pk-res">해서</td>
      <td class="pk-uz">qilib / qilgani uchun</td></tr>
  <tr><td>마시다</td><td class="pk-stem">마셔요</td><td class="pk-res">마셔서</td>
      <td class="pk-uz">ichib</td></tr>
  <tr><td>없다</td><td class="pk-stem">없어요</td><td class="pk-res">없어서</td>
      <td class="pk-uz">yoʻqligi uchun</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
아/어서 <b>unli</b> bilan boshlanadi — demak PK-32 dagi notoʻgʻri feʼllar bu yerda
<em>ishga tushadi</em>: 덥다 → <b>더워서</b>, 듣다 → <b>들어서</b>, 바쁘다 →
<b>바빠서</b>. Solishtiring: 고 va 지만 da ular tinch turgan edi
(덥고, 덥지만). Qoida oʻsha bitta — uchrashuv joyida unli bormi?</div>

<h3>2. Birinchi vazifa: sabab</h3>

<p>Oldingi qism — <b>sabab</b>, keyingi qism — <b>natija</b>. Oʻzbekchada bu
“…gani uchun”, “…gani sababli”.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">배가 <span class="pe-hl pe-hl--v">아파서</span> 병원에
     갔어요.</p>
  <p class="pe-ex__uz">Qornim ogʻrigani uchun shifoxonaga bordim.</p>
  <p class="pe-ex__why">아프다 → 아파서 (PK-32: 으 tushdi).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시간이 <span class="pe-hl pe-hl--v">없어서</span> 숙제를
     못 했어요.</p>
  <p class="pe-ex__uz">Vaqtim boʻlmagani uchun uy vazifasini qila olmadim.</p>
  <p class="pe-ex__why">Inkor ham sabab boʻlaveradi: 없어서, 안 가서, 못 봐서.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">날씨가 <span class="pe-hl pe-hl--v">더워서</span> 물을 많이
     마셔요.</p>
  <p class="pe-ex__uz">Havo issiq boʻlgani uchun koʻp suv ichaman.</p>
  <p class="pe-ex__why">덥다 → 더워서. ㅂ 우 ga aylandi.</p>
</div>

<h3>3. Ikkinchi vazifa: <em>bogʻliq</em> ketma-ketlik</h3>

<p>Bu qism oʻzbek oʻquvchi uchun eng qiyini, chunki oʻzbekchada 고 ham, 아/어서 ham
bir xil — <b>“-ib”</b> boʻlib tarjima qilinadi. Farqi maʼnoda:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">고 — alohida ishlar</p>
    <p><b>빵을 사고 집에 갔어요.</b></p>
    <p>Non sotib olib uyga ketdim.</p>
    <p>Non uyga ketishga <em>aloqasiz</em>. Shunchaki tartib.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">아/어서 — bogʻliq ishlar</p>
    <p><b>빵을 사서 먹었어요.</b></p>
    <p>Non sotib olib (uni) yedim.</p>
    <p>Yeyilgan non — <em>aynan oʻsha</em> non. Ikki ish bogʻlangan.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
아/어서 da birinchi qismdagi <b>narsa yoki joy ikkinchi qismga koʻchadi</b>.
학교에 <b>가서</b> 공부해요 — oʻqiladigan joy oʻsha maktab. 친구를 <b>만나서</b>
영화를 봤어요 — kinoni oʻsha doʻst bilan koʻrdim. Agar bunday bogʻliqlik boʻlmasa,
<b>고</b> ishlatiladi.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">도서관에 <span class="pe-hl pe-hl--v">가서</span> 책을
     읽었어요.</p>
  <p class="pe-ex__uz">Kutubxonaga borib kitob oʻqidim.</p>
  <p class="pe-ex__why">Kitob oʻsha kutubxonada oʻqilgan — joy koʻchdi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada bitta qoʻshimcha — <b>“-ib”</b> — ikkala vazifani ham bajaradi:
<br>• “Non sotib ol<b>ib</b> uyga ketdim” (aloqasiz) — koreyscha <b>고</b>
<br>• “Non sotib ol<b>ib</b> yedim” (bogʻliq) — koreyscha <b>아/어서</b>
<br>Yaʼni koreys tili sizning tilingiz birlashtirgan narsani <em>ikkiga
ajratadi</em>. Shuning uchun oʻzbekchadan tarjima qilmang — <b>savol bering</b>:
birinchi ishning natijasi ikkinchisida ishlatilyaptimi? Ha boʻlsa — 아/어서.</div>

<h3>4. Birinchi taqiq: zamon qoʻyilmaydi</h3>

<p>아/어서 dan oldin <b>았/었 hech qachon qoʻyilmaydi</b>. Gap oʻtgan zamonda boʻlsa
ham, zamon faqat oxirgi feʼlda turadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Xato</th><th>Toʻgʻri</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-uz"><s>아팠어서 병원에 갔어요</s></td>
      <td class="pk-res">아파서 병원에 갔어요</td>
      <td class="pk-uz">Ogʻrigani uchun bordim</td></tr>
  <tr><td class="pk-uz"><s>비가 왔어서 집에 있었어요</s></td>
      <td class="pk-res">비가 와서 집에 있었어요</td>
      <td class="pk-uz">Yomgʻir yoqqani uchun uyda edim</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Bu 지만 dan farqi. <b>지만</b> da zamon oldin turardi (갔<b>지만</b>), <b>아/어서</b>
da esa <em>hech qachon</em>. Uchta bogʻlovchini yonma-yon koʻring:
<br>• 고 — zamon oxirida (ketma-ketlikda)
<br>• 지만 — zamon oldin ham boʻladi
<br>• 아/어서 — zamon <b>faqat</b> oxirida</div>

<h3>5. Ikkinchi taqiq: buyruq va taklif kelmaydi</h3>

<p>아/어서 dan keyin <b>(으)세요</b> yoki taklif kelmaydi. Sabab shunchaki
tushuntiriladi, undan buyruq chiqarilmaydi:</p>

<div class="pe-fix">
  <p class="pe-bad">배가 아파서 <s>병원에 가세요</s>.</p>
  <p class="pe-good">아/어서 dan keyin buyruq boʻlmaydi. Bu maʼnoni berishning
     boshqa yoʻli bor va uni <b>PK-48</b> da oʻrganasiz.</p>
</div>

<p>Lekin darak va savolda hech qanday muammo yoʻq:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 왜 안 왔어요?<br>나: 너무 <span class="pe-hl pe-hl--v">바빠서</span>
     못 왔어요.</p>
  <p class="pe-ex__uz">A: Nega kelmadingiz?<br>B: Juda band boʻlganim uchun kela
     olmadim.</p>
  <p class="pe-ex__why">왜 (nega) savoliga javob — 아/어서 ning eng tabiiy
     oʻrni.</p>
</div>

<h3>6. Ot bilan va tayyor iboralar</h3>

<p>이다 ga qoʻshilganda 받침 ga qarab tanlanadi:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">명사 + <span class="pk-par">이어서</span></p>
    <p>학생<b>이어서</b> · 방학<b>이어서</b></p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">명사 + <span class="pk-par">여서</span></p>
    <p>친구<b>여서</b> · 의사<b>여서</b></p>
  </div>
</div>

<p>Va siz allaqachon bilgan bitta ibora aslida shu qolipda yasalgan:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">만나서 반갑습니다.</p>
  <p class="pe-ex__uz">Uchrashganimizdan xursandman.</p>
  <p class="pe-ex__why">만나다 → 만나서. PK-9 dagi tanishuv iborasi — endi uning
     ichini koʻrdingiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">어제 <s>아팠어서</s> 학교에 못 갔어요.</p>
  <p class="pe-good">아/어서 dan oldin zamon qoʻyilmaydi: <b>아파서</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">시간이 없어서 <s>일찍 오세요</s>.</p>
  <p class="pe-good">아/어서 dan keyin buyruq kelmaydi. Bu qolipni PK-48 da
     oʻrganasiz.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">빵을 <s>사고</s> 먹었어요 (“nonni sotib olib yedim”).</p>
  <p class="pe-good">Yeyilgan non — oʻsha non, demak bogʻliq: <b>사서 먹었어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">날씨가 <s>덥어서</s> 힘들어요.</p>
  <p class="pe-good">아/어서 unli bilan boshlanadi → ㅂ oʻzgaradi:
     <b>더워서</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">자수르 씨는 <s>학생어서</s> 바빠요.</p>
  <p class="pe-good">Ot bilan: 받침 bor → <b>학생이어서</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>바쁘다</b> ni 아/어서 shakliga oʻtkazing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>바빠서</strong>. Avval 아/어요 shaklini
    toping — 바빠요 (으 tushdi), keyin 요 oʻrniga 서.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Nega <s>어제 아팠어서 못 갔어요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>아/어서 dan oldin <b>았/었 qoʻyilmaydi</b>.
    Toʻgʻrisi: <strong>어제 아파서 못 갔어요</strong>. Oʻtgan zamon oxirgi
    feʼlda — 갔어요 — va bu butun gapni oʻtmishga oladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Qaysi biri toʻgʻri? 친구를 <span class="pe-blank">?</span> 영화를 봤어요
     (“Doʻstim bilan uchrashib kino koʻrdim”) — 만나고 / 만나서</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>만나서</strong>. Kinoni <em>oʻsha
    doʻst bilan</em> koʻrgansiz — ikki ish bogʻlangan. 만나고 deyilsa, doʻstni
    uchratganingiz kinoga aloqasiz boʻlib qolardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>듣다</b> ni 아/어서 shakliga oʻtkazing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>들어서</strong>. 아/어서 unli bilan
    boshlanadi, shuning uchun ㄷ → ㄹ (PK-32). Solishtiring: 듣<b>고</b>,
    듣<b>지만</b> — u yerda oʻzgarmagan edi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     “Vaqtim yoʻq, shuning uchun bora olmayman” — koreyscha ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>시간이 없어서 못 가요</strong>. 없다 →
    없어서. Inkor ham sabab boʻlaveradi, va natija qismida 못 bemalol
    ishlatiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">6</span>
     Nega <s>배가 아파서 병원에 가세요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>아/어서 dan keyin <b>buyruq kelmaydi</b>. Bu
    qolip sababni shunchaki tushuntiradi. Buyruq bilan ishlatiladigan sabab
    qolipini PK-48 da oʻrganasiz.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>아/어서</b><span>…gani uchun; …ib (bogʻliq)</span></li>
  <li><b>이어서 / 여서</b><span>…boʻlgani uchun (ot bilan)</span></li>
  <li><b>왜</b><span>nega</span></li>
  <li><b>배가 아프다</b><span>qorni ogʻrimoq</span></li>
  <li><b>병원</b><span>shifoxona</span></li>
  <li><b>비가 오다</b><span>yomgʻir yogʻmoq</span></li>
  <li><b>도서관</b><span>kutubxona</span></li>
  <li><b>일찍</b><span>erta</span></li>
  <li><b>너무</b><span>juda, haddan tashqari</span></li>
  <li><b>만나서 반갑습니다</b><span>tanishganimdan xursandman</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>아/어요 dan 요 ni olib <b>서</b> qoʻying — qolip shu.</li>
    <li>Ikki vazifasi: <b>sabab</b> va <b>bogʻliq ketma-ketlik</b>.</li>
    <li>고 — aloqasiz ishlar; 아/어서 — <b>bogʻliq</b> ishlar.</li>
    <li>Taqiq 1: 아/어서 dan oldin <b>zamon yoʻq</b> — 아팠어서 emas, 아파서.</li>
    <li>Taqiq 2: undan keyin <b>buyruq yoʻq</b>.</li>
    <li>Unli bilan boshlangani uchun notoʻgʻri feʼllar <b>oʻzgaradi</b>:
        더워서, 들어서, 바빠서.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-36: (으)면 — shart va faraz",
        "category": "korean",
        "order": 36,
        "summary": (
            "“Agar …sa”. Shart qolipining yasalishi, 받침 ayrisi va nega u — "
            "아/어서 dan farqli oʻlaroq — buyruq bilan bemalol ishlatilishi."
        ),
        "stories": ["시간이 있으면 같이 가요"],
        "content": """
<h2>PK-36: (으)면 — shart va faraz</h2>

<p>Oʻtgan darsda siz sababni aytishni oʻrgandingiz: <em>bu boʻldi, shuning uchun
u boʻldi</em>. Endi hali boʻlmagan narsa haqida gapiramiz: <em>agar bu boʻlsa, u
boʻladi</em>. Yomgʻir yogʻsa — uyda qolamiz. Vaqtingiz boʻlsa — keling. Bu
koreys tilida bitta qoʻshimcha bilan beriladi: <b>(으)면</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)면</b> ni 받침 ayrisi bilan toʻgʻri yasashni oʻrganasiz</li>
    <li>Shart va umumiy qoida maʼnolarini ajratasiz</li>
    <li>Nega undan keyin <em>buyruq kelishi mumkin</em>ligini bilib olasiz</li>
    <li><b>만약</b> bilan shartni kuchaytirishni oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">A oʻzak</span>
  <span class="pe-chip pe-chip--v">(으)면</span>
  <span class="pe-chip pe-chip--opt">+</span>
  <span class="pe-chip pe-chip--s">B natija</span>
</div>

<h3>1. 받침 ayrisi</h3>

<p>Tanish manzara: oʻzak undosh bilan tugasa <b>으</b> qoʻshiladi, unli bilan
tugasa yoʻq.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">면</span></p>
    <p>가<b>면</b> · 오<b>면</b> · 공부하<b>면</b> · 바쁘<b>면</b></p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">으면</span></p>
    <p>먹<b>으면</b> · 읽<b>으면</b> · 있<b>으면</b> · 없<b>으면</b></p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>가다</td><td class="pk-stem">가</td><td class="pk-res">가면</td>
      <td class="pk-uz">borsa</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td><td class="pk-res">먹으면</td>
      <td class="pk-uz">yesa</td></tr>
  <tr><td>있다</td><td class="pk-stem">있</td><td class="pk-res">있으면</td>
      <td class="pk-uz">boʻlsa, bor boʻlsa</td></tr>
  <tr><td>만들다</td><td class="pk-stem">만들</td><td class="pk-res">만들면</td>
      <td class="pk-uz">tayyorlasa</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Oxirgi qatorga eʼtibor bering: <b>ㄹ</b> oʻzak bu yerda ㄹ ni <em>tashlamaydi</em>
va 으 ham olmaydi — shunchaki <b>만들면</b>. PK-29 da ㄹ tushib qolgan edi
(만드세요), chunki u yerda 세 kelayotgan edi. ㄹ faqat <b>ㄴ, ㅂ, ㅅ</b> oldida
tushadi; 면 esa ㅁ bilan boshlanadi.</div>

<p>Notoʻgʻri feʼllar bilan — (으)면 <b>으</b> bilan, yaʼni unli bilan boshlanishi
mumkin, shuning uchun 받침 bor oʻzaklarda oʻzgarish boʻladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Natija</th><th>Nega</th></tr>
  <tr><td>덥다</td><td class="pk-res">더우면</td>
      <td class="pk-uz">ㅂ → 우 (unli 으 keldi)</td></tr>
  <tr><td>듣다</td><td class="pk-res">들으면</td>
      <td class="pk-uz">ㄷ → ㄹ (unli 으 keldi)</td></tr>
  <tr><td>바쁘다</td><td class="pk-res">바쁘면</td>
      <td class="pk-uz">받침 yoʻq → 으 ham yoʻq, oʻzak tinch</td></tr>
</table></div>

<h3>2. Birinchi maʼno: shart</h3>

<p>Hali boʻlmagan, lekin boʻlishi mumkin boʻlgan narsa. Oʻzbekchada — <b>“-sa”</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">비가 <span class="pe-hl pe-hl--v">오면</span> 집에
     있을 거예요.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻsa uyda boʻlaman.</p>
  <p class="pe-ex__why">Natija qismida kelasi zamon (PK-27) juda tabiiy —
     shart hali bajarilmagan.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시간이 <span class="pe-hl pe-hl--v">있으면</span> 같이
     영화를 봐요.</p>
  <p class="pe-ex__uz">Vaqtingiz boʻlsa birga kino koʻramiz.</p>
  <p class="pe-ex__why">있다 → 있으면. Taklif qilishning eng xushmuomala
     yoʻli.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu dars oʻzbek oʻquvchi uchun sovgʻa. Oʻzbekchada shart <b>“-sa”</b> qoʻshimchasi
bilan beriladi va u ham feʼlga yopishadi, shart ham gap boshida turadi:
<br>• “Vaqting bo‘l<b>sa</b> kel” → 시간이 <b>있으면</b> 오세요
<br>• “Yomg‘ir yog‘<b>sa</b> uyda qolaman” → 비가 <b>오면</b> 집에 있을 거예요
<br>Soʻz tartibi ham, mantiq ham bir xil. Yagona yangi narsa — <b>받침</b>
ayrisi. Boshqa hech narsani qayta oʻrganish shart emas.</div>

<h3>3. Ikkinchi maʼno: umumiy qoida</h3>

<p>Har doim takrorlanadigan haqiqat. Bu yerda “agar” emas, “…ganda” maʼnosi
chiqadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">봄이 <span class="pe-hl pe-hl--v">오면</span> 꽃이 펴요.</p>
  <p class="pe-ex__uz">Bahor kelganda gullar ochiladi.</p>
  <p class="pe-ex__why">Bu shart emas — har yili shunday boʻladi. Shakl esa
     oʻsha.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">김치를 많이 <span class="pe-hl pe-hl--v">먹으면</span>
     매워요.</p>
  <p class="pe-ex__uz">Kimchini koʻp yesangiz achchiq boʻladi.</p>
  <p class="pe-ex__why">Umumiy tajriba — kimga aytilsa ham toʻgʻri.</p>
</div>

<h3>4. Buyruq bemalol keladi — bu 아/어서 dan katta farq</h3>

<p>PK-35 da 아/어서 dan keyin buyruq qoʻya olmagan edingiz. <b>(으)면</b> da esa
hech qanday taqiq yoʻq — aksincha, buyruq va taklif uning eng tabiiy
sherigi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Gap</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">시간이 있으면 오세요.</td>
      <td class="pk-uz">Vaqtingiz boʻlsa keling.</td></tr>
  <tr><td class="pk-res">한국에 가면 김치를 드세요.</td>
      <td class="pk-uz">Koreyaga borsangiz kimchi yeng.</td></tr>
  <tr><td class="pk-res">머리가 아프면 약을 드세요.</td>
      <td class="pk-uz">Boshingiz ogʻrisa dori iching.</td></tr>
  <tr><td class="pk-res">모르면 저한테 물어 보세요.</td>
      <td class="pk-uz">Bilmasangiz mendan soʻrang.</td></tr>
</table></div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">아/어서 — sabab</p>
    <p><b>배가 아파서 병원에 갔어요.</b></p>
    <p>Boʻlib boʻlgan ish. Buyruq <b>mumkin emas</b>.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)면 — shart</p>
    <p><b>배가 아프면 병원에 가세요.</b></p>
    <p>Hali boʻlmagan ish. Buyruq <b>mumkin</b>.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Ikkisini ajratish oson: <b>allaqachon boʻlgan</b> narsa sabab (아/어서),
<b>hali boʻlmagan</b> narsa shart ((으)면). Shuning uchun maslahat berayotganingizda
deyarli har doim (으)면 kerak boʻladi.</div>

<h3>5. 만약 bilan kuchaytirish</h3>

<p>Shartni ochiq belgilash uchun gap boshiga <b>만약</b> (yoki <b>만일</b>)
qoʻyiladi. U (으)면 ning oʻrnini bosmaydi — ikkalasi birga ishlaydi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">만약</span> 내일 비가
     <span class="pe-hl pe-hl--v">오면</span> 안 갈 거예요.</p>
  <p class="pe-ex__uz">Agar ertaga yomgʻir yogʻsa, bormayman.</p>
  <p class="pe-ex__why">만약 — “agar”. U bor boʻlsa ham (으)면 baribir
     kerak.</p>
</div>

<h3>6. Ot va inkor bilan</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">ot + 이면 / 면</td><td class="pk-res">학생이면 · 친구면</td>
      <td class="pk-uz">talaba boʻlsa · doʻst boʻlsa</td></tr>
  <tr><td class="pk-stem">안 + feʼl</td><td class="pk-res">안 가면</td>
      <td class="pk-uz">bormasa</td></tr>
  <tr><td class="pk-stem">못 + feʼl</td><td class="pk-res">못 오면</td>
      <td class="pk-uz">kela olmasa</td></tr>
  <tr><td class="pk-stem">없다</td><td class="pk-res">시간이 없으면</td>
      <td class="pk-uz">vaqti boʻlmasa</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">학생이면 이 책을 살 수 있어요.</p>
  <p class="pe-ex__uz">Talaba boʻlsangiz bu kitobni sotib ololasiz.</p>
  <p class="pe-ex__why">학생 da 받침 bor → <b>이면</b>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">시간이 <s>있면</s> 오세요.</p>
  <p class="pe-good">받침 bor → <b>있으면</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">비가 <s>오으면</s> 집에 있어요.</p>
  <p class="pe-good">오 — 받침 yoʻq, demak 으 kerak emas: <b>오면</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">머리가 <s>아파서</s> 약을 드세요.</p>
  <p class="pe-good">Maslahat berayapsiz — hali boʻlmagan ish:
     <b>아프면 약을 드세요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">날씨가 <s>덥으면</s> 창문을 여세요.</p>
  <p class="pe-good">ㅂ tuslanishi: <b>더우면</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>만약</s> 시간이 있어요 <s>가요</s>.</p>
  <p class="pe-good">만약 oʻzi shart yasamaydi — qoʻshimcha baribir kerak:
     <b>만약 시간이 있으면 가요</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>먹다</b> ni (으)면 shakliga oʻtkazing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>먹으면</strong>. Oʻzak 먹 — 받침 bor,
    shuning uchun <b>으면</b>. <s>먹면</s> notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga nima tushadi? 시간이 <span class="pe-blank">?</span> 오세요.
     (“Vaqtingiz boʻlsa keling.”) — 있다</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>있으면</strong>. Eʼtibor bering: undan
    keyin <b>buyruq</b> turibdi va bu mutlaqo toʻgʻri. 아/어서 da bunday qilib
    boʻlmasdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>만들다</b> ni (으)면 shakliga oʻtkazing. ㄹ tushadimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>만들면</strong> — ㄹ <em>tushmaydi</em>
    va 으 ham qoʻshilmaydi. ㄹ faqat ㄴ, ㅂ, ㅅ oldida tushadi (만드세요,
    만듭니다). 면 esa ㅁ bilan boshlanadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Qaysi biri toʻgʻri? 머리가 <span class="pe-blank">?</span> 약을 드세요.
     — 아파서 / 아프면</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>아프면</strong>. Ikki sabab: bosh hali
    ogʻrimayapti (bu maslahat), va 아/어서 dan keyin <b>buyruq kelmaydi</b>.
    Shart esa buyruq bilan bemalol ishlaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     <b>덥다</b> ni (으)면 shakliga oʻtkazing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>더우면</strong>. 받침 bor → 으 keladi,
    yaʼni unli — shuning uchun ㅂ tuslanishi ishga tushadi (PK-32):
    덥 → 더우. Solishtiring: 덥<b>고</b>, 덥<b>지만</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">6</span>
     “Agar ertaga vaqtingiz boʻlsa, birga kutubxonaga boramiz” — tuzing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>만약 내일 시간이 있으면 같이 도서관에
    갈 거예요</strong>. 만약 ixtiyoriy, lekin shartni aniq belgilaydi;
    (으)면 esa majburiy.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)면</b><span>agar …sa; …ganda</span></li>
  <li><b>이면 / 면</b><span>…boʻlsa (ot bilan)</span></li>
  <li><b>만약 / 만일</b><span>agar (kuchaytiruvchi soʻz)</span></li>
  <li><b>비가 오다</b><span>yomgʻir yogʻmoq</span></li>
  <li><b>봄</b><span>bahor</span></li>
  <li><b>꽃이 피다</b><span>gul ochilmoq</span></li>
  <li><b>약</b><span>dori</span></li>
  <li><b>창문</b><span>deraza</span></li>
  <li><b>열다</b><span>ochmoq</span></li>
  <li><b>모르다</b><span>bilmaslik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>받침 yoʻq → <b>면</b>, 받침 bor → <b>으면</b>.</li>
    <li>ㄹ oʻzak: ㄹ <b>tushmaydi</b>, 으 ham qoʻshilmaydi — 만들면.</li>
    <li>Ikki maʼnosi: <b>shart</b> (agar …sa) va <b>umumiy qoida</b> (…ganda).</li>
    <li>Undan keyin <b>buyruq bemalol keladi</b> — 아/어서 dan asosiy farqi.</li>
    <li>Boʻlgan ish → 아/어서; hali boʻlmagan ish → <b>(으)면</b>.</li>
    <li><b>만약</b> shartni kuchaytiradi, lekin (으)면 ni almashtirmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-37: 보다 (더/덜) va 제일 / 가장 — taqqoslash",
        "category": "korean",
        "order": 37,
        "summary": (
            "Ikki narsani solishtirish va eng zoʻrini aytish. 보다, 더, 덜, "
            "제일, 가장 va 중에서 — oʻzbekcha “-dan” va “eng” bilan bir xil mantiq."
        ),
        "stories": ["우리 반에서 누가 제일 커요?"],
        "content": """
<h2>PK-37: 보다 (더/덜) va 제일 / 가장 — taqqoslash</h2>

<p>Afsona doʻstiga aytmoqchi: “Koreys tili ingliz tilidan qiyinroq”. U hamma
soʻzni biladi — 한국어, 영어, 어렵다 — lekin “…dan” ni qanday aytishni bilmaydi.
Bu darsda oʻsha bitta soʻzni oʻrganamiz: <b>보다</b>. Va u bilan birga
“eng” ni — <b>제일</b> va <b>가장</b> ni.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>보다</b> bilan ikki narsani solishtirasiz</li>
    <li><b>더</b> (koʻproq) va <b>덜</b> (kamroq) ni ishlatasiz</li>
    <li><b>제일 / 가장</b> bilan “eng” ni aytasiz</li>
    <li><b>중에서</b> bilan “…lar orasida” degan doirani belgilaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">A</span>
  <span class="pe-chip pe-chip--o">B보다</span>
  <span class="pe-chip pe-chip--adv">(더/덜)</span>
  <span class="pe-chip pe-chip--v">sifat</span>
</div>

<h3>1. 보다 — “…dan”</h3>

<p>Solishtiriladigan narsaga <b>보다</b> yopishadi. 받침 ayrisi <em>yoʻq</em> —
har qanday otga bir xil qoʻshiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 <span class="pe-hl pe-hl--o">동생보다</span>
     <span class="pe-hl pe-hl--v">커요</span>.</p>
  <p class="pe-ex__uz">Men ukamdan kattaman (boʻyliroqman).</p>
  <p class="pe-ex__why">크다 → 커요 (PK-32: 으 tushdi, oldingi boʻgʻin yoʻq →
     어).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어가 <span class="pe-hl pe-hl--o">영어보다</span>
     어려워요.</p>
  <p class="pe-ex__uz">Koreys tili ingliz tilidan qiyinroq.</p>
  <p class="pe-ex__why">어렵다 → 어려워요 (ㅂ tuslanishi).</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu dars ham sizga deyarli tayyor keladi. Oʻzbekchada solishtiriladigan narsa
<b>“-dan”</b> qoʻshimchasini oladi va u ham otga yopishadi:
<br>• “Men ukam<b>dan</b> kattaman” → 저는 동생<b>보다</b> 커요
<br>• “Bugun kecha<b>dan</b> issiqroq” → 오늘이 어제<b>보다</b> 더워요
<br>Ikkala tilda ham: <em>solishtirilayotgan narsa → belgi qoʻshimchasi → sifat,
sifat esa gap oxirida</em>. Farqi bittagina — oʻzbekchada sifatga ham “-roq”
qoʻshiladi (“katta<b>roq</b>”), koreyschada esa sifat oʻzgarmaydi, kerak boʻlsa
oldiga <b>더</b> qoʻyiladi.</div>

<h3>2. 더 va 덜</h3>

<p><b>더</b> = “koʻproq”, <b>덜</b> = “kamroq”. Ular sifatdan <em>oldin</em>
turadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Gap</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">오늘이 어제보다 더 더워요.</td>
      <td class="pk-uz">Bugun kechadan koʻra issiqroq.</td></tr>
  <tr><td class="pk-res">이 옷이 저 옷보다 덜 비싸요.</td>
      <td class="pk-uz">Bu kiyim u kiyimdan kamroq qimmat.</td></tr>
  <tr><td class="pk-res">지영 씨가 저보다 더 빨리 걸어요.</td>
      <td class="pk-uz">Jiyong mendan tezroq yuradi.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>더</b> ixtiyoriy. 보다 oʻzi allaqachon “…dan” maʼnosini beradi, shuning uchun
<b>저는 동생보다 커요</b> ham, <b>저는 동생보다 더 커요</b> ham toʻgʻri —
ikkinchisi biroz kuchliroq eshitiladi. <b>덜</b> esa ixtiyoriy emas: uni
qoʻymasangiz, maʼno teskarisiga aylanadi.</div>

<h3>3. Soʻz tartibi erkin</h3>

<p>보다 li boʻlak gapda joyini oʻzgartirishi mumkin — maʼno oʻzgarmaydi, faqat
urgʻu koʻchadi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Odatdagi tartib</p>
    <p><b>저는 동생보다 커요.</b></p>
    <p>Gap men haqimda.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Oldinga chiqarilgan</p>
    <p><b>동생보다 제가 커요.</b></p>
    <p>“Ukamdan koʻra <em>men</em>” — urgʻu menda.</p>
  </div>
</div>

<h3>4. 제일 va 가장 — “eng”</h3>

<p>Ikkalasi ham “eng” degani va <b>bir xil maʼno beradi</b>. Ular ham sifatdan
oldin turadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Soʻz</th><th>Qayerda koʻproq</th><th>Misol</th></tr>
  <tr><td class="pk-stem">제일</td><td class="pk-uz">ogʻzaki nutq, kundalik gap</td>
      <td class="pk-res">이게 제일 맛있어요.</td></tr>
  <tr><td class="pk-stem">가장</td><td class="pk-uz">yozma nutq, rasmiy uslub</td>
      <td class="pk-res">이것이 가장 중요해요.</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">우리 반에서 셰르벡 씨가 <span class="pe-hl pe-hl--adv">제일</span>
     커요.</p>
  <p class="pe-ex__uz">Bizning sinfda Sherbek eng katta (boʻyi eng baland).</p>
  <p class="pe-ex__why">Doira <b>에서</b> bilan berilgan: “sinfda”.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>제일</b> va <b>가장</b> ni birga ishlatmang: <s>제일 가장 커요</s> — bu “eng
eng” degani. Bittasini tanlang.</div>

<h3>5. 중에서 — doirani belgilash</h3>

<p>“Nimalar orasida?” degan savolga javob beradigan boʻlak. <b>명사 + 중에서</b>:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">과일 <span class="pe-hl pe-hl--o">중에서</span> 사과를
     <span class="pe-hl pe-hl--adv">제일</span> 좋아해요.</p>
  <p class="pe-ex__uz">Mevalar orasida olmani eng koʻp yoqtiraman.</p>
  <p class="pe-ex__why">중에서 doirani, 제일 esa eng zoʻrini koʻrsatadi.
     Ikkalasi juft boʻlib yuradi.</p>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Doira turi</th><th>Qoʻshimcha</th><th>Misol</th></tr>
  <tr><td class="pk-stem">narsalar guruhi</td><td class="pk-end">중에서</td>
      <td class="pk-res">음식 중에서 김치가 제일 매워요.</td></tr>
  <tr><td class="pk-stem">joy</td><td class="pk-end">에서</td>
      <td class="pk-res">한국에서 서울이 제일 커요.</td></tr>
</table></div>

<h3>6. Savol qilish</h3>

<p>Taqqoslash savollarida <b>누가</b>, <b>뭐가</b>, <b>어느 것이</b> ishlatiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 우리 반에서 누가 제일 커요?<br>나: 셰르벡 씨가 제일
     커요.</p>
  <p class="pe-ex__uz">A: Sinfimizda kim eng baland boʻyli?<br>B: Sherbek eng
     baland.</p>
  <p class="pe-ex__why">Javobda ega <b>이/가</b> oladi — “aynan u” degani
     (PK-12).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 한국어하고 영어 중에서 뭐가 더 어려워요?<br>나: 저는
     한국어가 더 어려워요.</p>
  <p class="pe-ex__uz">A: Koreys tili bilan ingliz tili orasida qaysi biri
     qiyinroq?<br>B: Menga koreys tili qiyinroq.</p>
  <p class="pe-ex__why">Ikkitani solishtirganda ham 중에서 ishlatiladi —
     “ikkovi orasida”.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>동생을 보다</s> 커요.</p>
  <p class="pe-good">보다 — qoʻshimcha, otga toʻgʻridan-toʻgʻri yopishadi:
     <b>동생보다</b>. 을/를 kerak emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">이게 <s>제일 가장</s> 맛있어요.</p>
  <p class="pe-good">Bittasini tanlang: <b>제일 맛있어요</b> yoki
     <b>가장 맛있어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">과일 <s>중에서 사과가 좋아해요</s>.</p>
  <p class="pe-good">좋아하다 — oʻtimli feʼl, toʻldiruvchi oladi:
     <b>사과를 제일 좋아해요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">오늘이 어제보다 <s>덥어요</s>.</p>
  <p class="pe-good">ㅂ tuslanishi: <b>더워요</b>. Taqqoslash sifatning
     shaklini oʻzgartirmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">이 옷이 저 옷보다 <s>안 비싸요</s> (“kamroq qimmat”).</p>
  <p class="pe-good">“Kamroq” — <b>덜</b>: <b>덜 비싸요</b>. 안 비싸요 esa
     shunchaki “qimmat emas”.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     “Men ukamdan kattaman” — koreyscha ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>저는 동생보다 커요</strong>. 보다 otga
    toʻgʻridan-toʻgʻri yopishadi — 받침 ayrisi yoʻq. 크다 → 커요.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>덜</b> nima maʼno beradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Kamroq</strong>. 더 ning teskarisi:
    이 옷이 저 옷보다 <b>덜</b> 비싸요 — “bu kiyim u kiyimdan kamroq qimmat”.
    Uni tushirib qoldirsangiz maʼno teskarisiga aylanadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga nima tushadi? 과일 <span class="pe-blank">?</span> 사과를 제일
     좋아해요.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>중에서</strong>. “Mevalar orasida” —
    doirani belgilaydi. Joy haqida gapirilsa <b>에서</b> boʻlardi:
    한국<b>에서</b> 서울이 제일 커요.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega <s>저는 동생을 보다 커요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <b>보다</b> — mustaqil feʼl emas,
    <b>qoʻshimcha</b>. U otga toʻgʻridan-toʻgʻri yopishadi va oldidan 을/를
    olmaydi: <strong>동생보다</strong>. (Alohida 보다 feʼli ham bor — u
    “koʻrmoq” degani, butunlay boshqa soʻz.)</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     “Bugun kechadan issiqroq” — tuzing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>오늘이 어제보다 더 더워요</strong>.
    더 ixtiyoriy — <b>오늘이 어제보다 더워요</b> ham toʻgʻri. 덥다 → 더워요
    (PK-32).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">6</span>
     제일 va 가장 orasida qanday farq bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Maʼnosida <b>farq yoʻq</b> — ikkalasi ham
    “eng”. Faqat uslubi boshqa: <strong>제일</strong> kundalik ogʻzaki nutqda,
    <strong>가장</strong> yozma va rasmiy nutqda koʻproq uchraydi. Birga
    ishlatilmaydi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>보다</b><span>…dan (taqqoslash qoʻshimchasi)</span></li>
  <li><b>더</b><span>koʻproq, …roq</span></li>
  <li><b>덜</b><span>kamroq</span></li>
  <li><b>제일</b><span>eng (ogʻzaki)</span></li>
  <li><b>가장</b><span>eng (yozma, rasmiy)</span></li>
  <li><b>중에서</b><span>…lar orasida</span></li>
  <li><b>크다</b><span>katta, baland boʻyli</span></li>
  <li><b>빨리</b><span>tez</span></li>
  <li><b>과일</b><span>meva</span></li>
  <li><b>중요하다</b><span>muhim</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>A는 B보다 sifat</b> — 보다 otga yopishadi, 받침 ayrisi yoʻq.</li>
    <li><b>더</b> = koʻproq (ixtiyoriy), <b>덜</b> = kamroq (majburiy).</li>
    <li><b>제일 = 가장</b> — maʼnosi bir xil, uslubi boshqa. Birga ishlatilmaydi.</li>
    <li>Doira: narsalar guruhi → <b>중에서</b>, joy → <b>에서</b>.</li>
    <li>보다 oldidan <b>을/를 qoʻyilmaydi</b>: 동생보다, 동생을 보다 emas.</li>
    <li>Taqqoslash sifatning shaklini oʻzgartirmaydi — 어렵다 baribir 어려워요.</li>
  </ul>
</div>
""",
    },
]
