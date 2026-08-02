# -*- coding: utf-8 -*-
"""Prime Korean — Block C, darslar 32–34 (notoʻgʻri feʼllar, 고, 지만).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_32_34.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_32_34.py --author=prime
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
        "title": "PK-32: Notoʻgʻri feʼllar 1: ㅂ, ㄷ, 으 tuslanishi",
        "category": "korean",
        "order": 32,
        "summary": (
            "Nega 덥다 → 더워요, 듣다 → 들어요, 바쁘다 → 바빠요. Uchta eng koʻp "
            "uchraydigan notoʻgʻri tuslanish va ular qachon ishga tushishi."
        ),
        "stories": ["날씨가 더워요"],
        "content": """
<h2>PK-32: Notoʻgʻri feʼllar 1: ㅂ, ㄷ, 으 tuslanishi</h2>

<p>Afsona yozda Seulga bordi. Havo issiq edi va u bilgan qoidasi bilan gap tuzdi:
<s>오늘 덥어요</s>. Koreys doʻsti jilmayib tuzatdi: <b>오늘 더워요</b>. Afsona hech
qanday xato qilmagan edi — u qoidani toʻgʻri ishlatgan. Muammo shundaki, 덥다
<em>oddiy</em> feʼl emas. Koreys tilida bir nechta feʼl guruhi bor: ular qoʻshimcha
qoʻshilganda oʻzagini <em>oʻzgartiradi</em>. Bu darsda ulardan eng koʻp uchraydigan
uchtasini oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>ㅂ</b> tuslanishini oʻrganasiz: 덥다 → 더워요</li>
    <li><b>ㄷ</b> tuslanishini oʻrganasiz: 듣다 → 들어요</li>
    <li><b>으</b> tuslanishini oʻrganasiz: 바쁘다 → 바빠요</li>
    <li>Eng muhimi: bu oʻzgarish <em>qachon</em> boʻlishini va qachon boʻlmasligini
        bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-chip pe-chip--opt">+</span>
  <span class="pe-chip pe-chip--v">unli bilan boshlanuvchi qoʻshimcha</span>
  <span class="pe-chip pe-chip--neg">= oʻzak oʻzgaradi</span>
</div>

<h3>1. Avval eng muhim narsani tushunib oling</h3>

<p>“Notoʻgʻri feʼl” degani — feʼl <em>har doim</em> oʻzgaradi degani emas. Oʻzgarish
faqat bitta sharoitda boʻladi: <b>qoʻshimcha unli bilan boshlansa</b>. Qoʻshimcha
undosh bilan boshlansa, feʼl mutlaqo oddiy feʼldek tuslanadi.</p>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Notoʻgʻri tuslanish — bu <b>oʻzak bilan qoʻshimcha uchrashadigan joydagi</b>
oʻzgarish. Uchrashuv joyida unli boʻlsa — oʻzgaradi. Undosh boʻlsa — hech narsa
boʻlmaydi. Shuning uchun har doim shu savolni bering: <em>“Qoʻshimcha nima bilan
boshlanyapti?”</em></div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>아/어요 <small>(unli)</small></th>
      <th>(으)세요 <small>(으 unli)</small></th><th>습니다 <small>(undosh)</small></th></tr>
  <tr><td>덥다</td><td class="pk-res">더워요</td><td class="pk-res">더우세요</td>
      <td class="pk-uz">덥습니다</td></tr>
  <tr><td>듣다</td><td class="pk-res">들어요</td><td class="pk-res">들으세요</td>
      <td class="pk-uz">듣습니다</td></tr>
  <tr><td>바쁘다</td><td class="pk-res">바빠요</td><td class="pk-uz">바쁘세요</td>
      <td class="pk-uz">바쁩니다</td></tr>
</table></div>

<p>Oxirgi ustunga qarang — u yerda hech narsa oʻzgarmagan. Yod olish kerak boʻlgan
narsa shu: oʻzgarish qoidasi emas, <em>oʻzgarish shartlari</em>.</p>

<h3>2. ㅂ tuslanishi — 받침 ㅂ, 우 boʻladi</h3>

<p>Oʻzak <b>ㅂ</b> bilan tugasa, unli oldida ㅂ <b>우</b> ga aylanadi. Soʻng 우 + 어요
qoʻshilib <b>워요</b> boʻladi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>ㅂ → 우</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>덥다</td><td class="pk-stem">덥</td><td>더우</td>
      <td class="pk-res">더워요</td><td class="pk-uz">issiq</td></tr>
  <tr><td>춥다</td><td class="pk-stem">춥</td><td>추우</td>
      <td class="pk-res">추워요</td><td class="pk-uz">sovuq</td></tr>
  <tr><td>맵다</td><td class="pk-stem">맵</td><td>매우</td>
      <td class="pk-res">매워요</td><td class="pk-uz">achchiq</td></tr>
  <tr><td>어렵다</td><td class="pk-stem">어렵</td><td>어려우</td>
      <td class="pk-res">어려워요</td><td class="pk-uz">qiyin</td></tr>
  <tr><td>쉽다</td><td class="pk-stem">쉽</td><td>쉬우</td>
      <td class="pk-res">쉬워요</td><td class="pk-uz">oson</td></tr>
  <tr><td>무겁다</td><td class="pk-stem">무겁</td><td>무거우</td>
      <td class="pk-res">무거워요</td><td class="pk-uz">ogʻir</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">오늘 날씨가 <span class="pe-hl pe-hl--v">더워요</span>.
     그리고 김치가 아주 <span class="pe-hl pe-hl--v">매워요</span>.</p>
  <p class="pe-ex__uz">Bugun havo issiq. Va kimchi juda achchiq.</p>
  <p class="pe-ex__why">덥다 → 더워요, 맵다 → 매워요. Ikkalasida ham ㅂ yoʻqoldi.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ikkita istisno</span>
<b>돕다</b> (yordam bermoq) va <b>곱다</b> (goʻzal) 워요 emas, <b>와요</b> beradi:
돕다 → <b>도와요</b>, 곱다 → <b>고와요</b>. Boshqa hech bir ㅂ feʼl bunday
qilmaydi — shu ikkitasini alohida yod oling.</div>

<h3>3. Hamma ㅂ feʼl ham notoʻgʻri emas</h3>

<p>Bu eng koʻp adashtiradigan joy. Oʻzagi ㅂ bilan tugagan bir nechta feʼl butunlay
<em>oddiy</em> tuslanadi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Notoʻgʻri (ㅂ → 우)</p>
    <p>덥다 → <b>더워요</b></p>
    <p>어렵다 → <b>어려워요</b></p>
    <p>가깝다 → <b>가까워요</b></p>
    <p>Koʻpchiligi <em>sifat</em>.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Toʻgʻri (ㅂ qoladi)</p>
    <p>입다 → <b>입어요</b></p>
    <p>잡다 → <b>잡아요</b></p>
    <p>좁다 → <b>좁아요</b></p>
    <p>Koʻpchiligi <em>feʼl</em>.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Qoidasi yoʻq, lekin juda ishonchli belgi bor: <b>ㅂ bilan tugagan sifatlarning deyarli
hammasi notoʻgʻri</b>, harakat feʼllari esa koʻpincha toʻgʻri. 입다 (kiymoq), 잡다
(ushlamoq), 씹다 (chaynamoq) — hammasi harakat, hammasi toʻgʻri. Yangi soʻz
uchratganingizda lugʻatda “ㅂ불규칙” belgisini qidiring.</div>

<h3>4. ㄷ tuslanishi — 받침 ㄷ, ㄹ boʻladi</h3>

<p>Oʻzak <b>ㄷ</b> bilan tugasa, unli oldida ㄷ <b>ㄹ</b> ga aylanadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>ㄷ → ㄹ</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>듣다</td><td class="pk-stem">듣</td><td>들</td>
      <td class="pk-res">들어요</td><td class="pk-uz">eshitmoq</td></tr>
  <tr><td>걷다</td><td class="pk-stem">걷</td><td>걸</td>
      <td class="pk-res">걸어요</td><td class="pk-uz">yurmoq</td></tr>
  <tr><td>묻다</td><td class="pk-stem">묻</td><td>물</td>
      <td class="pk-res">물어요</td><td class="pk-uz">soʻramoq</td></tr>
  <tr><td>싣다</td><td class="pk-stem">싣</td><td>실</td>
      <td class="pk-res">실어요</td><td class="pk-uz">yuklamoq</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 매일 음악을 <span class="pe-hl pe-hl--v">들어요</span>.
     그리고 공원에서 한 시간 <span class="pe-hl pe-hl--v">걸어요</span>.</p>
  <p class="pe-ex__uz">Men har kuni musiqa tinglayman. Va bogʻda bir soat yuraman.</p>
  <p class="pe-ex__why">듣다 → 들어요, 걷다 → 걸어요. 받침 ㄷ ikkalasida ham ㄹ boʻldi.</p>
</div>

<p>Bu yerda ham toʻgʻri tuslanadiganlari bor, va ular juda koʻp ishlatiladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>받다</td><td class="pk-res">받아요</td><td class="pk-uz">olmoq</td></tr>
  <tr><td>닫다</td><td class="pk-res">닫아요</td><td class="pk-uz">yopmoq</td></tr>
  <tr><td>믿다</td><td class="pk-res">믿어요</td><td class="pk-uz">ishonmoq</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Bitta soʻz — ikki maʼno</span>
<b>묻다</b> ikki xil feʼl: “soʻramoq” maʼnosida <em>notoʻgʻri</em> —
물어요; “koʻmmoq” maʼnosida esa <em>toʻgʻri</em> — 묻어요. Ular yozilishi bir xil,
tuslanishi boshqa. Kontekst hal qiladi: 선생님한테 <b>물어요</b> — ustozdan
soʻrayman.</div>

<h3>5. 으 tuslanishi — 으 shunchaki yoʻqoladi</h3>

<p>Oʻzak <b>으</b> bilan tugasa, 아/어 oldida bu 으 <em>tushib qoladi</em>. Bu
guruhning eng yaxshi tomoni — <b>istisnosi yoʻq</b>. Barcha 으 oʻzaklar shunday
qiladi.</p>

<p>Savol faqat bitta: 으 tushgandan keyin <b>아</b> qoʻshiladimi yoki <b>어</b>?
Buni undan <em>oldingi</em> boʻgʻin hal qiladi:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">Oldingi unli ㅏ yoki ㅗ</p>
    <p class="pk-batchim__form">→ <span class="pk-par">아</span></p>
    <p>바쁘다 → 바<b>빠</b>요<br>아프다 → 아<b>파</b>요<br>배고프다 → 배고<b>파</b>요</p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">Boshqa har qanday unli</p>
    <p class="pk-batchim__form">→ <span class="pk-par">어</span></p>
    <p>예쁘다 → 예<b>뻐</b>요<br>슬프다 → 슬<b>퍼</b>요<br>기쁘다 → 기<b>뻐</b>요</p>
  </div>
</div>

<p>Agar oʻzak bitta boʻgʻindan iborat boʻlsa — qaraydigan “oldingi boʻgʻin” yoʻq.
Bunday paytda har doim <b>어</b>:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>쓰다</td><td class="pk-res">써요</td><td class="pk-uz">yozmoq, ishlatmoq</td></tr>
  <tr><td>크다</td><td class="pk-res">커요</td><td class="pk-uz">katta</td></tr>
  <tr><td>끄다</td><td class="pk-res">꺼요</td><td class="pk-uz">oʻchirmoq</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">오늘 아주 <span class="pe-hl pe-hl--v">바빠요</span>.
     머리도 <span class="pe-hl pe-hl--v">아파요</span>. 그래서 편지를
     못 <span class="pe-hl pe-hl--v">써요</span>.</p>
  <p class="pe-ex__uz">Bugun juda bandman. Boshim ham ogʻriyapti. Shuning uchun
     xat yoza olmayapman.</p>
  <p class="pe-ex__why">바쁘 → 바빠 (oldida ㅏ), 아프 → 아파 (oldida ㅏ),
     쓰 → 써 (oldingi boʻgʻin yoʻq).</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbek tilida ham xuddi shunday hodisa bor va siz uni sezmay ishlatasiz:
<br>• ogʻiz + im → <b>ogʻzim</b> (i tushdi) · burun + i → <b>burni</b> ·
oʻgʻil + i → <b>oʻgʻli</b>
<br>Unli qoʻshimcha kelganda oʻzakdagi unli tushib qoladi. Koreyscha 으 tuslanishi
xuddi shu mantiq: <b>바쁘 + 아요 → 바빠요</b>. Demak bu siz uchun yangi fikr emas —
faqat boshqa tilda. Shuning uchun 으 guruhini oʻzbek oʻquvchi eng tez oʻzlashtiradi.</div>

<h3>6. Hammasini bir joyga yigʻamiz</h3>

<p>Uchta guruh, bitta savol. Qoʻshimcha unli bilan boshlanadimi?</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Guruh</th><th>Nima boʻladi</th><th>Misol</th><th>Undosh oldida</th></tr>
  <tr><td class="pk-stem">ㅂ</td><td>ㅂ → 우</td>
      <td class="pk-res">춥다 → 추워요</td><td class="pk-uz">춥습니다 (oʻzgarmaydi)</td></tr>
  <tr><td class="pk-stem">ㄷ</td><td>ㄷ → ㄹ</td>
      <td class="pk-res">걷다 → 걸어요</td><td class="pk-uz">걷습니다 (oʻzgarmaydi)</td></tr>
  <tr><td class="pk-stem">으</td><td>으 tushadi</td>
      <td class="pk-res">예쁘다 → 예뻐요</td><td class="pk-uz">예쁩니다 (oʻzgarmaydi)</td></tr>
</table></div>

<p>Oʻrganganlaringiz bilan birga ishlatib koʻring — oʻtgan zamon (PK-20) ham 아/어
shakliga tayanadi, shuning uchun u ham oʻzgaradi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Hozirgi</th><th>Oʻtgan</th><th>Imkon (PK-30)</th></tr>
  <tr><td>덥다</td><td class="pk-res">더워요</td><td class="pk-res">더웠어요</td>
      <td class="pk-uz">—</td></tr>
  <tr><td>듣다</td><td class="pk-res">들어요</td><td class="pk-res">들었어요</td>
      <td class="pk-res">들을 수 있어요</td></tr>
  <tr><td>걷다</td><td class="pk-res">걸어요</td><td class="pk-res">걸었어요</td>
      <td class="pk-res">걸을 수 있어요</td></tr>
  <tr><td>바쁘다</td><td class="pk-res">바빠요</td><td class="pk-res">바빴어요</td>
      <td class="pk-uz">—</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>(으)ㄹ 수 있다</b> va <b>(으)세요</b> da ham oʻzgarish boʻladi, chunki ular ham
아니라 <b>으</b> — yaʼni unli — bilan boshlanadi: 듣다 → <b>들을</b> 수 있어요,
<b>들으세요</b>. Lekin 으 guruhi bu yerda tinch turadi: 바쁘 oʻzagida 받침 yoʻq,
shuning uchun oddiygina <b>바쁘세요</b>.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">오늘 날씨가 <s>덥어요</s>.</p>
  <p class="pe-good">ㅂ tuslanishi: <b>더워요</b>. Oʻzakdagi ㅂ 우 ga aylanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">음악을 <s>듣어요</s>.</p>
  <p class="pe-good">ㄷ tuslanishi: <b>들어요</b>. 받침 ㄷ unli oldida ㄹ boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>바쁘어요</s>.</p>
  <p class="pe-good">으 tushadi va 아 qoʻshiladi: <b>바빠요</b> (oldingi unli ㅏ).</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">옷을 <s>이워요</s>.</p>
  <p class="pe-good">입다 — <em>toʻgʻri</em> feʼl: <b>입어요</b>. Hamma ㅂ feʼl
     notoʻgʻri emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">문을 <s>달아요</s>.</p>
  <p class="pe-good">닫다 — <em>toʻgʻri</em> feʼl: <b>닫아요</b>. 걷다 bilan
     adashtirmang.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>더웁니다</s></p>
  <p class="pe-good">Qoʻshimcha undosh bilan boshlangan — hech narsa oʻzgarmaydi:
     <b>덥습니다</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>춥다</b> ni 아/어요 shakliga oʻtkazing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>추워요</strong>. ㅂ tuslanishi: 춥 → 추우,
    keyin 우 + 어요 = <b>워요</b>. <s>춥어요</s> notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga nima tushadi? 저는 라디오를 <span class="pe-blank">?</span> — 듣다</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>들어요</strong>. ㄷ → ㄹ, chunki 어요 unli
    bilan boshlanadi. Solishtiring: 듣<b>습니다</b> da hech narsa
    oʻzgarmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega <s>예쁘아요</s> emas, <b>예뻐요</b>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>으 tushgandan keyin 아 yoki 어 tanlanadi, tanlovni
    <em>oldingi</em> boʻgʻin qiladi. 예 dagi unli — ㅖ, u ㅏ ham, ㅗ ham emas.
    Shuning uchun <strong>어</strong>: 예뻐요. Solishtiring: 아프다 da oldingi unli
    ㅏ, shuning uchun 아파요.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu ikkitasining qaysi biri notoʻgʻri feʼl: <b>입다</b> yoki <b>맵다</b>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>맵다</strong> notoʻgʻri — 매워요. 입다 esa
    oddiy feʼl — 입어요. Belgi: 맵다 sifat, 입다 harakat feʼli. ㅂ bilan tugagan
    sifatlarning deyarli hammasi notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     <b>걷다</b> dan “yura olaman” degan gap tuzing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>걸을 수 있어요</strong>. (으)ㄹ 수 있다
    ham <b>으</b> — unli — bilan boshlanadi, shuning uchun ㄷ → ㄹ oʻzgarishi bu
    yerda ham ishlaydi. <s>걷을 수 있어요</s> notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">6</span>
     Jasur kecha juda band edi. Koreyscha ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>자수르 씨는 어제 아주 바빴어요</strong>.
    Oʻtgan zamon ham 아/어 shakliga qurilgani uchun 으 baribir tushadi:
    바쁘 + 았어요 → <b>바빴어요</b>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>덥다</b><span>issiq (havo)</span></li>
  <li><b>춥다</b><span>sovuq (havo)</span></li>
  <li><b>맵다</b><span>achchiq</span></li>
  <li><b>어렵다 / 쉽다</b><span>qiyin / oson</span></li>
  <li><b>무겁다</b><span>ogʻir</span></li>
  <li><b>돕다</b><span>yordam bermoq (→ 도와요)</span></li>
  <li><b>듣다</b><span>eshitmoq, tinglamoq</span></li>
  <li><b>걷다</b><span>yurmoq, piyoda yurmoq</span></li>
  <li><b>묻다</b><span>soʻramoq</span></li>
  <li><b>바쁘다</b><span>band</span></li>
  <li><b>아프다</b><span>ogʻrimoq, kasal boʻlmoq</span></li>
  <li><b>쓰다</b><span>yozmoq; ishlatmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>Oʻzgarish faqat <b>unli bilan boshlanuvchi qoʻshimcha</b> oldida boʻladi.</li>
    <li><b>ㅂ → 우</b>: 덥다 → 더워요. Istisno: 돕다 → 도와요, 곱다 → 고와요.</li>
    <li><b>ㄷ → ㄹ</b>: 듣다 → 들어요, 걷다 → 걸어요.</li>
    <li><b>으 tushadi</b>: oldingi unli ㅏ/ㅗ boʻlsa 아, boshqa boʻlsa 어.</li>
    <li>Hamma ㅂ va ㄷ feʼl notoʻgʻri emas: 입다, 잡다, 받다, 닫다, 믿다 — oddiy.</li>
    <li>습니다 oldida hech narsa oʻzgarmaydi: <b>덥습니다, 듣습니다, 바쁩니다</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-33: 고 — sanash va ketma-ketlik",
        "category": "korean",
        "order": 33,
        "summary": (
            "Ikki gapni bitta qilib bogʻlaydigan eng oddiy qoʻshimcha. 고 ikki "
            "vazifada: sanash (“va”) va ketma-ketlik (“…ib”)."
        ),
        "stories": ["밥을 먹고 학교에 가요"],
        "content": """
<h2>PK-33: 고 — sanash va ketma-ketlik</h2>

<p>Hozirgacha siz yozgan gaplar qisqa edi: <em>“Nonushta qilaman.”</em>
<em>“Maktabga boraman.”</em> Lekin hech kim shunday gapirmaydi. Odam
<em>“Nonushta qilib maktabga boraman”</em> deydi. Ikki gapni bitta qiladigan eng
oddiy va eng koʻp ishlatiladigan vosita — <b>고</b>. Bu darsdan keyin
gaplaringiz birdan uzunroq va tabiiyroq boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>고</b> bilan ikki gapni bogʻlashni oʻrganasiz</li>
    <li>Uning ikki maʼnosini — <em>sanash</em> va <em>ketma-ketlik</em> — ajratasiz</li>
    <li>Zamon qoʻshimchasi qayerga qoʻyilishini bilib olasiz</li>
    <li>Sifatlar va 이다 bilan ham ishlatishni oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">A oʻzak</span>
  <span class="pe-chip pe-chip--v">고</span>
  <span class="pe-chip pe-chip--opt">+</span>
  <span class="pe-chip pe-chip--s">B gap</span>
</div>

<h3>1. Yasalishi — bu darsning eng oson qismi</h3>

<p>고 <b>받침 ayrisi yoʻq</b>. Oʻzakni oling va toʻgʻridan-toʻgʻri 고 qoʻshing.
Hech qanday 으, hech qanday 아/어 tanlovi yoʻq.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th></tr>
  <tr><td>가다</td><td class="pk-stem">가</td><td class="pk-end">고</td>
      <td class="pk-res">가고</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td><td class="pk-end">고</td>
      <td class="pk-res">먹고</td></tr>
  <tr><td>읽다</td><td class="pk-stem">읽</td><td class="pk-end">고</td>
      <td class="pk-res">읽고</td></tr>
  <tr><td>공부하다</td><td class="pk-stem">공부하</td><td class="pk-end">고</td>
      <td class="pk-res">공부하고</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Oʻtgan darsdagi notoʻgʻri feʼllar ham bu yerda <b>tinch turadi</b>, chunki 고 undosh
bilan boshlanadi: 덥다 → <b>덥고</b>, 듣다 → <b>듣고</b>, 바쁘다 → <b>바쁘고</b>.
PK-32 ning asosiy qoidasi shu yerda darhol ishlayapti.</div>

<h3>2. Birinchi vazifa: sanash (나열)</h3>

<p>Ikki mustaqil fakt — ular bir vaqtda ham, boshqa-boshqa odam haqida ham boʻlishi
mumkin. Oʻzbekchada bu <b>“va”</b>:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">김치는 <span class="pe-hl pe-hl--v">맵고</span> 불고기는
     <span class="pe-hl pe-hl--v">달아요</span>.</p>
  <p class="pe-ex__uz">Kimchi achchiq va bulgogi shirin.</p>
  <p class="pe-ex__why">Ikki alohida fakt. Ega ham har xil — 김치 va 불고기.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아프소나 씨는 학생이<span class="pe-hl pe-hl--v">고</span>
     자수르 씨는 선생님이에요.</p>
  <p class="pe-ex__uz">Afsona talaba, Jasur esa oʻqituvchi.</p>
  <p class="pe-ex__why">이다 bilan ham ishlaydi: 받침 bor → <b>이고</b>,
     받침 yoʻq → <b>고</b> (친구고).</p>
</div>

<h3>3. Ikkinchi vazifa: ketma-ketlik (순서)</h3>

<p>Bir ish tugaydi, keyin ikkinchisi boshlanadi. Oʻzbekchada bu <b>“-ib”</b>:
<em>“yeb”, “qilib”, “koʻrib”</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 아침에 밥을 <span class="pe-hl pe-hl--v">먹고</span>
     학교에 <span class="pe-hl pe-hl--v">가요</span>.</p>
  <p class="pe-ex__uz">Men ertalab ovqat yeb maktabga boraman.</p>
  <p class="pe-ex__why">Avval ovqat, keyin maktab. Tartib muhim — almashtirsangiz
     maʼno oʻzgaradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">숙제를 <span class="pe-hl pe-hl--v">하고</span> 친구를
     만났어요.</p>
  <p class="pe-ex__uz">Uy vazifasini qilib doʻstimni uchratdim.</p>
  <p class="pe-ex__why">Ketma-ketlikda odatda <b>ega bitta</b> boʻladi.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Qaysi maʼno ekanini <b>kontekst</b> hal qiladi, shakl emas. Ikkala gapning egasi
bir xil va ishlar tabiiy tartibda boʻlsa — ketma-ketlik. Aks holda — sanash.
Koreyslar bu ikkisini ajratib oʻtirmaydi, chunki farqi gapdan koʻrinib turadi.</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Sanash</p>
    <p><b>이 옷은 싸고 예뻐요.</b></p>
    <p>Bu kiyim arzon va chiroyli.</p>
    <p>Ikki xususiyat, bir vaqtda.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Ketma-ketlik</p>
    <p><b>옷을 사고 집에 갔어요.</b></p>
    <p>Kiyim sotib olib uyga ketdim.</p>
    <p>Avval biri, keyin ikkinchisi.</p>
  </div>
</div>

<h3>4. Zamon qayerga qoʻyiladi?</h3>

<p>Bu darsning eng muhim qoidasi va oʻzbek oʻquvchi eng koʻp adashadigan joy.
<b>Ketma-ketlik</b> maʼnosida zamon faqat <em>oxirgi</em> feʼlga qoʻyiladi. Birinchi
feʼl zamonsiz qoladi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Xato</th><th>Toʻgʻri</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-uz"><s>밥을 먹었고 잤어요</s></td>
      <td class="pk-res">밥을 먹고 잤어요</td>
      <td class="pk-uz">Ovqat yeb uxladim</td></tr>
  <tr><td class="pk-uz"><s>숙제를 했고 놀았어요</s></td>
      <td class="pk-res">숙제를 하고 놀았어요</td>
      <td class="pk-uz">Vazifani qilib oʻynadim</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbek tilida ham xuddi shunday! “Ovqat <b>yeb</b> uxla<b>dim</b>” deysiz —
“yeb” da oʻtgan zamon belgisi yoʻq, u faqat oxirgi feʼlda. <s>“Yedim va
uxladim”</s> ham toʻgʻri, lekin “yeb uxladim” tabiiyroq. Koreys tili shu
tabiiyroq yoʻlni <b>majburiy</b> qilgan. Yaʼni sizga yangi fikr oʻrganish shart
emas — faqat oʻz tilingizdagi odatga ishoning.</div>

<p>Lekin <b>sanash</b> maʼnosida ikkala tomon ham oʻz zamonini olishi mumkin,
chunki ular haqiqatan ham ikki alohida fakt:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">어제는 <span class="pe-hl pe-hl--v">추웠고</span> 오늘은
     <span class="pe-hl pe-hl--v">더워요</span>.</p>
  <p class="pe-ex__uz">Kecha sovuq edi, bugun esa issiq.</p>
  <p class="pe-ex__why">Ikki har xil vaqt haqida — shuning uchun har biri oʻz
     zamonini oladi. 춥다 → 추웠고 (PK-32: ㅂ → 우).</p>
</div>

<h3>5. Inkor va boshqa qoliplar bilan</h3>

<p>고 dan oldingi qism ham inkor boʻlishi mumkin. Inkor odatdagidek yasaladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Gap</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">아침을 안 먹고 학교에 가요.</td>
      <td class="pk-uz">Nonushta qilmay maktabga boraman.</td></tr>
  <tr><td class="pk-res">저는 커피를 못 마시고 물만 마셔요.</td>
      <td class="pk-uz">Men qahva icholmayman, faqat suv ichaman.</td></tr>
  <tr><td class="pk-res">손을 씻고 밥을 드세요.</td>
      <td class="pk-uz">Qoʻlingizni yuvib ovqatlaning.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Oxirgi misolga eʼtibor bering: buyruq, xohish yoki kelasi zamon — hammasi
<em>oxirgi</em> feʼlda turadi, 고 dan oldingi qism esa har doim sof oʻzak +
고 boʻlib qolaveradi. Shuning uchun 고 ni ishlatish oson: butun ogʻirlik gapning
oxiriga tushadi.</div>

<h3>6. Uchtadan koʻp ish</h3>

<p>고 ni ketma-ket qoʻyish mumkin — ammo ikki-uchtadan koʻp boʻlsa gap
zerikarli boʻladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 아침에 <span class="pe-hl pe-hl--v">일어나고</span>
     세수를 <span class="pe-hl pe-hl--v">하고</span> 학교에 가요.</p>
  <p class="pe-ex__uz">Men ertalab turib, yuzimni yuvib, maktabga boraman.</p>
  <p class="pe-ex__why">Uchta ish — bitta gap. Kundalik tartibni aytishning
     eng oddiy yoʻli.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">밥을 <s>먹었고</s> 잤어요.</p>
  <p class="pe-good">Ketma-ketlikda zamon faqat oxirida: <b>밥을 먹고 잤어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>먹으고</s> · <s>읽으고</s></p>
  <p class="pe-good">고 da <b>으 yoʻq</b>: <b>먹고</b>, <b>읽고</b>. 받침 ayrisi
     boʻlmagan qoʻshimcha.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">아프소나 씨는 <s>학생고</s> 자수르 씨는 선생님이에요.</p>
  <p class="pe-good">받침 bor otdan keyin 이 kerak: <b>학생이고</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">숙제를 하고 <s>놀아요</s>, 어제.</p>
  <p class="pe-good">Koreys gapida vaqt soʻzi boshda turadi:
     <b>어제 숙제를 하고 놀았어요</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Ikki gapni 고 bilan bogʻlang: 밥을 먹어요 + 학교에 가요.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>밥을 먹고 학교에 가요</strong>. Birinchi
    feʼl oʻzak + 고 boʻlib qoladi, zamon esa oxirgi feʼlda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Nega <s>어제 밥을 먹었고 잤어요</s> gʻalati eshitiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki bu <b>ketma-ketlik</b> — bir odam ketma-ket
    ikki ish qilgan. Bunday paytda zamon faqat oxirgi feʼlga qoʻyiladi:
    <strong>어제 밥을 먹고 잤어요</strong>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga nima tushadi? 이 식당은 <span class="pe-blank">?</span> 맛있어요.
     (“Bu oshxona arzon va mazali.”) — 싸다</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>싸고</strong>. Sifatlar ham 고 oladi va
    받침 ayrisi yoʻq: 싸 + 고. Bu <em>sanash</em> maʼnosi — ikki xususiyat bir
    vaqtda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>덥다</b> ni 고 bilan qoʻshing. Oʻzak oʻzgaradimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>덥고</strong> — oʻzgarmaydi. PK-32 dagi
    qoida: notoʻgʻri tuslanish faqat <b>unli</b> bilan boshlanuvchi qoʻshimcha
    oldida boʻladi. 고 esa undosh bilan boshlanadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     “Sherbek talaba, Dilnoza esa oʻqituvchi” — koreyscha ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>셰르벡 씨는 학생이고 딜노자 씨는
    선생님이에요</strong>. 학생 da 받침 bor → <b>이고</b>. Bu sanash: ikki
    alohida fakt, ikki xil ega.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">6</span>
     “Qoʻlingizni yuvib ovqatlaning” gapini tuzing (씻다 + 드세요).</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>손을 씻고 드세요</strong>. Buyruq shakli
    faqat <em>oxirgi</em> feʼlda turadi — <s>씻으세요 그리고 드세요</s> deyish
    shart emas, 고 ikkalasini bitta qiladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>고</b><span>va; …ib (bogʻlovchi qoʻshimcha)</span></li>
  <li><b>이고</b><span>…dir va (ot + 이다 shakli)</span></li>
  <li><b>일어나다</b><span>turmoq, uygʻonmoq</span></li>
  <li><b>세수하다</b><span>yuz yuvmoq</span></li>
  <li><b>씻다</b><span>yuvmoq</span></li>
  <li><b>싸다 / 비싸다</b><span>arzon / qimmat</span></li>
  <li><b>맛있다</b><span>mazali</span></li>
  <li><b>달다</b><span>shirin</span></li>
  <li><b>놀다</b><span>oʻynamoq, dam olmoq</span></li>
  <li><b>식당</b><span>oshxona, restoran</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>고 oʻzakka <b>toʻgʻridan-toʻgʻri</b> qoʻshiladi — 받침 ayrisi yoʻq.</li>
    <li>Ikki maʼnosi bor: <b>sanash</b> (“va”) va <b>ketma-ketlik</b> (“…ib”).</li>
    <li>Ketma-ketlikda zamon <b>faqat oxirgi feʼlda</b>: 먹고 잤어요.</li>
    <li>Sanashda ikkala tomon ham oʻz zamonini olishi mumkin: 추웠고 … 더워요.</li>
    <li>Ot bilan: 받침 bor → <b>이고</b>, yoʻq → <b>고</b>.</li>
    <li>고 undosh bilan boshlanadi, shuning uchun notoʻgʻri feʼllar oʻzgarmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-34: 지만 — qarama-qarshilik",
        "category": "korean",
        "order": 34,
        "summary": (
            "“Lekin” maʼnosini bitta gap ichida berish. 지만 ning yasalishi, "
            "zamon bilan ishlashi va 하지만 dan farqi."
        ),
        "stories": ["한국어는 어렵지만 재미있어요"],
        "content": """
<h2>PK-34: 지만 — qarama-qarshilik</h2>

<p>Afsonadan soʻrashdi: “Koreys tili qanday?” U aytmoqchi boʻlgan fikr bitta emas,
ikkita: <em>qiyin</em> — lekin <em>qiziqarli</em>. Oʻtgan darsdagi 고 bu yerda
ishlamaydi, chunki 고 shunchaki sanaydi, ikki fikrni <b>qarshi qoʻymaydi</b>.
Kerakli qoʻshimcha — <b>지만</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>지만</b> bilan ikki qarama-qarshi fikrni bogʻlashni oʻrganasiz</li>
    <li>Zamonni 지만 dan <em>oldin</em> qoʻyishni oʻrganasiz</li>
    <li><b>하지만</b> va <b>지만</b> ning farqini bilib olasiz</li>
    <li>고 bilan 지만 ni ishonch bilan ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">A oʻzak</span>
  <span class="pe-chip pe-chip--neg">지만</span>
  <span class="pe-chip pe-chip--opt">+</span>
  <span class="pe-chip pe-chip--s">B gap</span>
</div>

<h3>1. Yasalishi</h3>

<p>고 kabi, 지만 ham oʻzakka <b>toʻgʻridan-toʻgʻri</b> yopishadi. 받침 ayrisi yoʻq,
으 yoʻq, 아/어 tanlovi yoʻq:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl / sifat</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th></tr>
  <tr><td>가다</td><td class="pk-stem">가</td><td class="pk-end">지만</td>
      <td class="pk-res">가지만</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td><td class="pk-end">지만</td>
      <td class="pk-res">먹지만</td></tr>
  <tr><td>어렵다</td><td class="pk-stem">어렵</td><td class="pk-end">지만</td>
      <td class="pk-res">어렵지만</td></tr>
  <tr><td>바쁘다</td><td class="pk-stem">바쁘</td><td class="pk-end">지만</td>
      <td class="pk-res">바쁘지만</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Oxirgi ikki qatorga qarang: <b>어렵지만</b>, <b>바쁘지만</b> — notoʻgʻri feʼllar
bu yerda ham tinch. Sabab oʻsha: 지만 undosh bilan boshlanadi. PK-32, PK-33 va
PK-34 — uchalasi bitta qoidaga tayanadi.</div>

<h3>2. Maʼnosi: “…lekin…”</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어는 <span class="pe-hl pe-hl--v">어렵지만</span>
     아주 <span class="pe-hl pe-hl--v">재미있어요</span>.</p>
  <p class="pe-ex__uz">Koreys tili qiyin, lekin juda qiziqarli.</p>
  <p class="pe-ex__why">Kutilgan xulosa: qiyin boʻlsa — yoqmaydi. Gap esa
     teskarisini aytadi. Aynan shu 지만 ning ishi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 옷은 <span class="pe-hl pe-hl--v">예쁘지만</span>
     너무 <span class="pe-hl pe-hl--v">비싸요</span>.</p>
  <p class="pe-ex__uz">Bu kiyim chiroyli, lekin juda qimmat.</p>
  <p class="pe-ex__why">Yaxshi tomon → yomon tomon. Eng koʻp uchraydigan
     ishlatilishi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 김치를 <span class="pe-hl pe-hl--v">좋아하지만</span>
     동생은 <span class="pe-hl pe-hl--neg">안 좋아해요</span>.</p>
  <p class="pe-ex__uz">Men kimchini yoqtiraman, lekin ukam yoqtirmaydi.</p>
  <p class="pe-ex__why">Ikki ega har xil — 지만 uchun bu mutlaqo normal.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
지만 <b>ikkinchi qismga urgʻu beradi</b>. “Qiyin, lekin qiziqarli” degan odam
oxir-oqibat <em>qiziqarli</em> deyapti. Tartibni almashtiring — fikr ham
oʻzgaradi: 재미있지만 어려워요 = “qiziqarli, lekin qiyin”, yaʼni endi shikoyat.</div>

<h3>3. Zamon 지만 dan OLDIN turadi</h3>

<p>Bu 고 dan eng muhim farqi. 고 da (ketma-ketlik maʼnosida) zamon faqat oxirida
edi. 지만 da esa <b>har bir tomon oʻz zamonini oladi</b>, chunki ikki tomon ikki
mustaqil fikr:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Gap</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">어제는 바빴지만 오늘은 안 바빠요.</td>
      <td class="pk-uz">Kecha band edim, lekin bugun band emasman.</td></tr>
  <tr><td class="pk-res">한국에 갔지만 친구를 못 만났어요.</td>
      <td class="pk-uz">Koreyaga bordim, lekin doʻstimni uchrata olmadim.</td></tr>
  <tr><td class="pk-res">공부했지만 시험이 어려웠어요.</td>
      <td class="pk-uz">Oʻqidim, lekin imtihon qiyin edi.</td></tr>
</table></div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">고 — ketma-ketlik</p>
    <p><b>밥을 먹고 잤어요.</b></p>
    <p><s>먹었고</s> — zamon faqat oxirida.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">지만 — qarama-qarshilik</p>
    <p><b>밥을 먹었지만 배고파요.</b></p>
    <p><b>먹었</b>지만 — zamon oldida ham boʻladi.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada ham xuddi shu farq bor, faqat siz uni oʻylab oʻtirmaysiz:
<br>• “Ovqat <b>yeb</b> uxladim” — birinchi feʼl zamonsiz (bu — 고).
<br>• “Ovqat <b>yedim</b>, lekin hali ochman” — birinchi feʼl toʻliq zamonli
(bu — 지만).
<br>Yaʼni koreyscha qoida sizning tilingizdagi qoida bilan bir xil. Agar
oʻzbekcha gapda “-dim” deyayotgan boʻlsangiz, koreyschada ham 았/었 qoʻying.</div>

<h3>4. Ot bilan: 이지만</h3>

<p>이다 ga qoʻshilganda 받침 ga qarab tanlanadi — bu qoidani PK-10 dan bilasiz:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">명사 + <span class="pk-par">이지만</span></p>
    <p>학생<b>이지만</b> · 선생님<b>이지만</b></p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">명사 + <span class="pk-par">지만</span></p>
    <p>친구<b>지만</b> · 의사<b>지만</b></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">자수르 씨는 <span class="pe-hl pe-hl--v">학생이지만</span>
     한국어를 아주 잘해요.</p>
  <p class="pe-ex__uz">Jasur talaba, lekin koreys tilini juda yaxshi biladi.</p>
  <p class="pe-ex__why">받침 bor (학생) → <b>이지만</b>.</p>
</div>

<h3>5. 하지만 va 지만 — bir xil emas</h3>

<p>Ikkalasi ham “lekin” degani, lekin ular <b>bir xil oʻrinda turmaydi</b>:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th></th><th>지만</th><th>하지만</th></tr>
  <tr><td class="pk-stem">Nima?</td><td class="pk-uz">qoʻshimcha</td>
      <td class="pk-uz">mustaqil soʻz</td></tr>
  <tr><td class="pk-stem">Qayerda?</td><td class="pk-uz">feʼl oʻzagiga yopishadi</td>
      <td class="pk-uz">yangi gap boshida turadi</td></tr>
  <tr><td class="pk-stem">Misol</td><td class="pk-res">비싸지만 샀어요.</td>
      <td class="pk-res">비싸요. 하지만 샀어요.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Ikkalasini birga ishlatmang: <s>비싸지만 하지만 샀어요</s> — bu “lekin lekin”
degani. Bittasini tanlang.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시험이 어려웠어요. <span class="pe-hl pe-hl--adv">하지만</span>
     저는 열심히 공부했어요.</p>
  <p class="pe-ex__uz">Imtihon qiyin edi. Lekin men tirishib oʻqigandim.</p>
  <p class="pe-ex__why">Bu yerda nuqta bor — ikki alohida gap. Shuning uchun
     하지만.</p>
</div>

<h3>6. 고 mi, 지만 mi?</h3>

<p>Bitta savol bering: <em>ikkinchi qism birinchisidan kutilgan narsanimi?</em></p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Fikr</th><th>Qaysi</th><th>Gap</th></tr>
  <tr><td class="pk-uz">arzon + mazali (ikkalasi ham yaxshi)</td>
      <td class="pk-stem">고</td><td class="pk-res">싸고 맛있어요.</td></tr>
  <tr><td class="pk-uz">arzon, lekin mazasiz (kutilmagan)</td>
      <td class="pk-stem">지만</td><td class="pk-res">싸지만 맛없어요.</td></tr>
  <tr><td class="pk-uz">yedim, keyin uxladim (tartib)</td>
      <td class="pk-stem">고</td><td class="pk-res">밥을 먹고 잤어요.</td></tr>
  <tr><td class="pk-uz">yedim, lekin hali ochman (kutilmagan)</td>
      <td class="pk-stem">지만</td><td class="pk-res">밥을 먹었지만 배고파요.</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">한국어는 <s>어렵으지만</s> 재미있어요.</p>
  <p class="pe-good">지만 da <b>으 yoʻq</b>: <b>어렵지만</b>. 받침 ayrisi
     boʻlmagan qoʻshimcha.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">비싸지만 <s>하지만</s> 샀어요.</p>
  <p class="pe-good">Bittasi yetadi: <b>비싸지만 샀어요</b> yoki
     <b>비싸요. 하지만 샀어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">어제 한국에 <s>가지만</s> 친구를 못 만났어요.</p>
  <p class="pe-good">Oʻtgan zamon 지만 dan oldin qoʻyiladi:
     <b>갔지만</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">자수르 씨는 <s>학생지만</s> 한국어를 잘해요.</p>
  <p class="pe-good">받침 bor otdan keyin 이 kerak: <b>학생이지만</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">이 옷은 <s>예쁘지만 그리고</s> 비싸요.</p>
  <p class="pe-good">지만 oʻzi bogʻlaydi, yana bogʻlovchi kerak emas:
     <b>예쁘지만 비싸요</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Ikki fikrni 지만 bilan bogʻlang: 한국어는 어려워요 + 재미있어요.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>한국어는 어렵지만 재미있어요</strong>.
    Oʻzak <b>어렵</b> + 지만. Diqqat: bu yerda ㅂ oʻzgarmaydi, chunki 지만 undosh
    bilan boshlanadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga nima tushadi? 어제 한국에 <span class="pe-blank">?</span>
     친구를 못 만났어요. — 가다</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>갔지만</strong>. Ish oʻtmishda boʻlgani
    uchun zamon <em>지만 dan oldin</em> turadi. <s>가지만</s> — zamonsiz, notoʻgʻri.
    Bu 고 dan eng muhim farq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Qaysi biri toʻgʻri: <b>이 식당은 싸고 맛없어요</b> yoki
     <b>이 식당은 싸지만 맛없어요</b>?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>싸지만 맛없어요</strong>. Arzon
    boʻlgani — yaxshi xabar, mazasiz boʻlgani — yomon. Ular
    <b>qarama-qarshi</b>, shuning uchun 지만. 고 ishlatilsa, ikkalasi bir xil
    tomonga qaragan boʻlishi kerak edi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     “Dilnoza oʻquvchi, lekin koreyscha juda yaxshi gapiradi” — tuzing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>딜노자 씨는 학생이지만 한국어를 아주
    잘해요</strong>. 학생 da 받침 bor → <b>이지만</b>. 받침 yoʻq boʻlsa
    (친구) — oddiy <b>지만</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Nega <s>비싸요 지만 샀어요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>지만 — <b>qoʻshimcha</b>, mustaqil soʻz emas. U
    oʻzakka yopishishi kerak: <strong>비싸지만 샀어요</strong>. Agar ikki alohida
    gap qilmoqchi boʻlsangiz, mustaqil soʻz ishlating:
    <strong>비싸요. 하지만 샀어요</strong>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">6</span>
     Kecha sovuq edi, bugun issiq. 지만 bilan ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>어제는 추웠지만 오늘은 더워요</strong>.
    춥다 → 추웠 (PK-32: ㅂ → 우, oʻtgan zamon), keyin 지만. 덥다 → 더워요.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>지만</b><span>…lekin (qoʻshimcha)</span></li>
  <li><b>이지만</b><span>…dir, lekin (ot bilan)</span></li>
  <li><b>하지만</b><span>Lekin… (gap boshida)</span></li>
  <li><b>재미있다 / 재미없다</b><span>qiziqarli / zerikarli</span></li>
  <li><b>맛없다</b><span>mazasiz</span></li>
  <li><b>비싸다</b><span>qimmat</span></li>
  <li><b>좋아하다</b><span>yoqtirmoq</span></li>
  <li><b>잘하다</b><span>yaxshi eplamoq, ustalik bilan qilmoq</span></li>
  <li><b>열심히</b><span>tirishib, astoydil</span></li>
  <li><b>시험</b><span>imtihon</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>지만 oʻzakka <b>toʻgʻridan-toʻgʻri</b> qoʻshiladi — 으 yoʻq.</li>
    <li>Maʼnosi: ikkinchi qism birinchisidan <b>kutilmagan</b> narsa.</li>
    <li>Zamon <b>지만 dan oldin</b> turadi: 갔지만, 바빴지만. Bu 고 dan farqi.</li>
    <li>Ot bilan: 받침 bor → <b>이지만</b>, yoʻq → <b>지만</b>.</li>
    <li><b>하지만</b> — mustaqil soʻz, yangi gap boshida. Ikkalasini birga
        ishlatmang.</li>
    <li>Urgʻu <b>ikkinchi</b> qismda: 어렵지만 재미있어요 = oxir-oqibat qiziqarli.</li>
  </ul>
</div>
""",
    },
]
