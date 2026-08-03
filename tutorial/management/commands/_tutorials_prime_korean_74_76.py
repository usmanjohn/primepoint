# -*- coding: utf-8 -*-
"""Prime Korean — Block F, darslar 74–76.

74. 자마자, 기가 무섭게 — darhol ketma-ketlik
75. 는 길에, 는 김에 — yoʻl-yoʻlakay va fursatdan foydalanib
76. 고 나서, (으)ㄴ 채로 — tugagach va shu holicha

Uchtasi ham VAQT haqida: ikki ish bir-biriga qanday joylashadi.
  74 — B, A tugashi bilan darhol boshlanadi
  75 — B, A davom etayotganda ichiga qoʻshiladi
  76 — B, A butunlay tugagach (고 나서) yoki A holati saqlanib turganda (채로)

Oʻzbekcha kalitlar:
  자마자        = "…ishi BILANOQ"  (borar-bormas)
  기가 무섭게    = "…ishga ULGURMAY" (kuchli, yozma)
  는 길에        = "…ga ketayotib, YOʻL-YOʻLAKAY"
  는 김에        = "…gan ekan, BIR YOʻLA / fursatdan foydalanib"
  고 나서        = "…ib BOʻLGACH" (tugallik)
  (으)ㄴ 채로     = "…gan HOLICHA / …GANCHA"

PK-74 ning oxirida QOʻSHIMCHA boʻlim bor: **문어체 (한다체)** — yozma
uslub. Oʻqish matnlari shu darsdan boshlab 한다체 da yoziladi, va
TOPIK II 쓰기 51–54 ham shu uslubni talab qiladi. Pupil buni allaqachon
yarim biladi: PK-60 dagi 간다고 했어요 ichida aynan 간다 turibdi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_74_76.py --author=prime
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
    # PK-74
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-74: 자마자, 기가 무섭게 — darhol ketma-ketlik",
        "category": "korean",
        "order": 74,
        "summary": (
            "“Uydan chiqishi bilanoq yomgʻir boshlandi” — ikki ishning "
            "orasida bir soniya ham yoʻq. Va darsning oxirida yozma "
            "uslub — 한다체."
        ),
        "stories": ["빨리빨리, 한국"],
        "content": """
<h2>PK-74: 자마자, 기가 무섭게 — darhol ketma-ketlik</h2>

<p>Avtobusdan tushdingiz. Va <em>oʻsha zahoti</em> yomgʻir quya
boshladi. Ikki ish orasida vaqt yoʻq — biri tugadi, ikkinchisi allaqachon
boshlangan. Oʻzbekchada buni “tush<b>ishim bilanoq</b>” yoki hatto
“tush<b>ar-tushmas</b>” deb aytamiz. Koreys tilida buning aniq qolipi
bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>자마자</b> bilan “…ishi bilanoq” deysiz</li>
    <li>Nega uning oldida <b>hech qachon</b> oʻtgan zamon boʻlmasligini bilib olasiz</li>
    <li>Uni PK-33 dagi <b>고</b> va PK-35 dagi <b>아/어서</b> dan ajratasiz</li>
    <li>Kuchliroq va yozma <b>기가 무섭게</b> ni oʻrganasiz</li>
    <li>Va qoʻshimcha sifatida — <b>문어체 (한다체)</b>, kitob tili</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qolip</span>
  <span class="pe-chip pe-chip--v">feʼl oʻzagi + 자마자</span>
  <span class="pe-chip pe-chip--aux">feʼl oʻzagi + 기가 무섭게</span>
  <span class="pe-chip pe-chip--adv">= …ishi bilanoq</span>
</div>

<h3>1. 자마자 — “…ishi bilanoq”</h3>

<p>Bu darsda sizni bir yaxshi xabar kutmoqda: <b>자마자</b> da 받침
farqi <b>yoʻq</b>. 받침 bormi, yoʻqmi — baribir. Feʼl oʻzagiga toʻgʻridan
toʻgʻri yopishadi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Oʻzak</th><th>Natija</th></tr>
  <tr><td class="pk-stem">가다</td><td class="pk-end">가</td>
      <td class="pk-res">가자마자</td></tr>
  <tr><td class="pk-stem">먹다</td><td class="pk-end">먹</td>
      <td class="pk-res">먹자마자</td></tr>
  <tr><td class="pk-stem">듣다</td><td class="pk-end">듣</td>
      <td class="pk-res">듣자마자</td></tr>
  <tr><td class="pk-stem">일어나다</td><td class="pk-end">일어나</td>
      <td class="pk-res">일어나자마자</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>ㄷ, ㅂ, 르 kabi <b>notoʻgʻri feʼllar ham oʻzgarmaydi</b>:
  듣다 → <b>듣자마자</b> (❌ 들자마자), 돕다 → <b>돕자마자</b>.
  Chunki 자마자 unli bilan boshlanmaydi — undosh bilan. Notoʻgʻri
  tuslanish esa faqat unli oldida ishlaydi (PK-32, PK-47).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">집에 <span class="pe-hl pe-hl--v">도착하자마자</span>
     비가 오기 시작했어요.</p>
  <p class="pe-ex__uz">Uyga yetib kelishim bilanoq yomgʻir boshlandi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 소식을 <span class="pe-hl pe-hl--v">듣자마자</span>
     아프소나 씨한테 전화했어요.</p>
  <p class="pe-ex__uz">Bu xabarni eshitishim bilanoq Afsonaga qoʻngʻiroq
  qildim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">수업이 <span class="pe-hl pe-hl--v">끝나자마자</span>
     학생들이 교실을 나갔어요.</p>
  <p class="pe-ex__uz">Dars tugashi bilanoq oʻquvchilar sinfdan chiqib
  ketishdi.</p>
  <p class="pe-ex__why">Ikki gapning egasi <b>har xil</b> boʻlishi mumkin:
  dars tugadi, <em>oʻquvchilar</em> chiqdi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ikkita mos shakl beradi.</b> Birinchisi —
  “kel<b>ishi bilanoq</b>”. Ikkinchisi esa ancha qiziq:
  “kel<b>ar-kelmas</b>”, “chiq<b>ar-chiqmas</b>”, “yot<b>ar-yotmas</b>”
  — bir feʼlni ikki marta, biri boʻlishli, biri boʻlishsiz qilib
  takrorlaymiz. Maʼnosi aynan 자마자: hali toʻliq tugamasidan
  ikkinchisi boshlanib boʻldi. Koreys tilida bunday takror yoʻq,
  lekin oʻzbek quloq uchun 자마자 ni eslab qolishning eng oson yoʻli
  shu: <em>가자마자 = borar-bormas</em>.</p>
</div>

<h3>2. Uchta qatʼiy qoida</h3>

<div class="pe-call pe-rule">
  <p><b>1-qoida. Birinchi gapda ZAMON boʻlmaydi.</b><br>
  ❌ <s>도착했자마자</s> · ❌ <s>도착할자마자</s> · ✅ <b>도착하자마자</b><br>
  Zamon faqat <em>oxirgi</em> feʼlda koʻrsatiladi. 자마자 ning oʻzagi
  hamisha yalangʻoch.</p>
  <p><b>2-qoida. Faqat FEʼL bilan.</b><br>
  ❌ <s>바쁘자마자</s> (sifat) · ❌ <s>학생이자마자</s> (ot).</p>
  <p><b>3-qoida. Ikkinchi gapda hamma narsa mumkin</b> — oʻtgan zamon,
  kelasi zamon, buyruq, hatto taqiq:<br>
  집에 도착하자마자 <b>전화하세요</b>. (Uyga yetib borishingiz bilanoq
  qoʻngʻiroq qiling.)</p>
</div>

<h3>3. 자마자 · 고 · 아/어서 — uchovi ham “keyin”, lekin…</h3>

<p>Sizda endi ketma-ketlik uchun uchta vosita bor. Farq —
<b>ikki ish orasidagi masofa</b> va <b>bogʻliqlik</b>.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Oralaridagi vaqt</th><th>Bogʻliqlik</th><th>Misol</th></tr>
  <tr><td class="pk-stem">고 <small>PK-33</small></td>
      <td>muhim emas</td><td>yoʻq — shunchaki tartib</td>
      <td>밥을 먹고 잤어요.</td></tr>
  <tr><td class="pk-stem">아/어서 <small>PK-35</small></td>
      <td>ketma-ket</td><td>bor — ikkinchisi birinchisi bilan bogʻliq</td>
      <td>친구를 만나서 영화를 봤어요.</td></tr>
  <tr><td class="pk-stem">자마자</td>
      <td><b>deyarli nol</b></td><td>tezlikning oʻzi urgʻuda</td>
      <td>밥을 먹자마자 잤어요.</td></tr>
</table></div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">밥을 먹<b>고</b> 잤어요.</p>
    <p>Ovqat yedim, keyin uxladim. Orada bir soat ham boʻlishi
    mumkin — hech kim soʻramaydi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">밥을 먹<b>자마자</b> 잤어요.</p>
    <p>Ovqatni yeb boʻlishim bilanoq uxlab qoldim.
    <b>Tezlik — gapning butun mazmuni.</b></p>
  </div>
</div>

<h3>4. 기가 무섭게 — “…ishga ulgurmay”</h3>

<p>Endi kuchliroq shakl. <b>기가 무섭게</b> soʻzma-soʻz
“…ish<em>dan qoʻrqqandek</em>” degani — yaʼni ish tugashini kutishga
ham <em>qoʻrqib</em>, shu qadar tez. Bu <b>boʻrttirma</b>: “men buni
kutmagandim, shunchalik tez boʻldi”.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">feʼl oʻzagi</span>
  <span class="pe-chip pe-chip--aux">기가 무섭게</span>
  <span class="pe-chip pe-chip--adv">= …ishga ulgurmay</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">새 휴대폰이 <span class="pe-hl pe-hl--aux">나오기가
     무섭게</span> 다 팔렸어요.</p>
  <p class="pe-ex__uz">Yangi telefon chiqishga ulgurmay hammasi sotilib
  ketdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">음식이 <span class="pe-hl pe-hl--aux">나오기가
     무섭게</span> 아이들이 먹기 시작했어요.</p>
  <p class="pe-ex__uz">Ovqat kelishga ulgurmay bolalar yeya boshlashdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">제가 말을 <span class="pe-hl pe-hl--aux">끝내기가
     무섭게</span> 베크조드 씨가 반대했어요.</p>
  <p class="pe-ex__uz">Gapimni tugatishga ulgurmay Bekzod eʼtiroz
  bildirdi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>기가 무섭게 ning ikkita cheklovi bor.</b><br>
  1. Ikkinchi gap odatda <b>boʻlib oʻtgan voqea</b> — oʻtgan zamon.
  Oʻz rejangiz yoki buyruq uchun ishlatilmaydi:
  ❌ <s>도착하기가 무섭게 전화하세요</s> → bu yerda <b>도착하자마자</b>.<br>
  2. U <b>hayrat</b> bildiradi. Oddiy, kutilgan ketma-ketlikka
  ishlatsangiz gʻalati eshitiladi: 아침에 일어나기가 무섭게 세수했어요 —
  bunda hayratlanadigan narsa yoʻq.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">자마자</p>
    <p><b>Betaraf.</b> Ogʻzaki ham, yozma ham. Har qanday gapda.</p>
    <p><small>수업이 끝나자마자 집에 갔어요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">기가 무섭게</p>
    <p><b>Boʻrttirma.</b> Koʻproq <em>yozma</em> — maqola, hikoya,
    TOPIK matni. Hayrat bor.</p>
    <p><small>수업이 끝나기가 무섭게 학생들이 뛰어나갔어요.</small></p>
  </div>
</div>

<h3>5. Qoʻshimcha: 문어체 — kitob tili (한다체)</h3>

<p>Shu darsdan boshlab oʻqish matnlari boshqacha koʻrinadi. Sabab bor:
<b>고자</b> (PK-71), <b>법이다</b> (PK-72), <b>기 십상이다</b> (PK-73),
<b>기가 무섭게</b> — bularning hammasi <em>yozma</em> grammatika.
Ularni 해요체 gap ichiga tiqish — kostyum kiyib shippak kiyish bilan
barobar.</p>

<p>Kitob, gazeta, maqola, roman va <b>TOPIK II 쓰기 51–54</b> —
hammasi <b>문어체</b>, yaʼni <b>한다체</b> da yoziladi. Bu sizga
begona emas: PK-60 da <b>간다고 했어요</b> deganingizda ichida aynan
<b>간다</b> turgan edi. Endi uni gapning oxirida ham ishlatasiz.</p>

<div class="pk-level">
  <div class="pk-level__row pk-level__row--4">
    <span class="pk-level__name">한다체 (문어체)</span>
    <span class="pk-level__ko">먹는다 / 간다</span>
    <span class="pk-level__who">kitob, gazeta, insho, TOPIK 쓰기 — <b>odamga emas, qogʻozga</b></span>
  </div>
  <div class="pk-level__row pk-level__row--3">
    <span class="pk-level__name">합니다체</span>
    <span class="pk-level__ko">먹습니다</span>
    <span class="pk-level__who">rasmiy nutq: taqdimot, xabarlar, mijoz</span>
  </div>
  <div class="pk-level__row pk-level__row--1">
    <span class="pk-level__name">해요체</span>
    <span class="pk-level__ko">먹어요</span>
    <span class="pk-level__who">kundalik hurmatli suhbat</span>
  </div>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima</th><th>Qoida</th><th>해요체</th><th>한다체</th></tr>
  <tr><td class="pk-stem">Feʼl, 받침 yoʻq</td><td class="pk-end">oʻzak + ㄴ다</td>
      <td>가요</td><td class="pk-res">간다</td></tr>
  <tr><td class="pk-stem">Feʼl, 받침 bor</td><td class="pk-end">oʻzak + 는다</td>
      <td>먹어요</td><td class="pk-res">먹는다</td></tr>
  <tr><td class="pk-stem">Sifat</td><td class="pk-end">lugʻat shakli</td>
      <td>좋아요</td><td class="pk-res">좋다</td></tr>
  <tr><td class="pk-stem">있다 / 없다</td><td class="pk-end">oʻzgarmaydi</td>
      <td>있어요</td><td class="pk-res">있다</td></tr>
  <tr><td class="pk-stem">Oʻtgan zamon</td><td class="pk-end">았/었다</td>
      <td>갔어요</td><td class="pk-res">갔다</td></tr>
  <tr><td class="pk-stem">Ot (이다)</td><td class="pk-end">이다 / 다</td>
      <td>학생이에요</td><td class="pk-res">학생이다 · 가수다</td></tr>
  <tr><td class="pk-stem">Kelasi / taxmin</td><td class="pk-end">(으)ㄹ 것이다</td>
      <td>갈 거예요</td><td class="pk-res">갈 것이다</td></tr>
  <tr><td class="pk-stem">Inkor</td><td class="pk-end">지 않는다 / 지 않다</td>
      <td>가지 않아요</td><td class="pk-res">가지 않는다</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Eng koʻp uchraydigan xato:</b> 있다 va 없다 ni feʼl deb
  hisoblab <s>있는다</s> yozish. Ular <b>있다 · 없다</b> boʻlib qoladi.
  Shuningdek sifat ham hech qachon 는다 olmaydi:
  ❌ <s>좋는다</s> → ✅ <b>좋다</b>.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>한다체 — qogʻoz uchun, odam uchun emas.</b> Uni doskaga
  yozasiz, insho yozasiz, hikoya yozasiz. Lekin oʻqituvchingizga
  <s>안녕하다</s> demaysiz. <b>Qoʻshtirnoq ichidagi gap</b> esa oʻz
  uslubini saqlaydi: hikoya 한다체 da boʻlsa ham, ichidagi odamlar
  baribir 해요체 da gaplashadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">지영은 문을 <span class="pe-hl pe-hl--v">열자마자</span>
     소리를 <span class="pe-hl pe-hl--v">질렀다</span>.
     “여기 뭐예요?”</p>
  <p class="pe-ex__uz">Jiyon eshikni ochishi bilanoq qichqirib yubordi.
  “Bu nima?”</p>
  <p class="pe-ex__why">Hikoya — <b>한다체</b> (질렀다). Qoʻshtirnoq
  ichi — <b>해요체</b> (뭐예요). Aynan shu tartib.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>집에 도착했자마자 비가 왔어요.</s></p>
  <p class="pe-good">집에 <b>도착하자마자</b> 비가 왔어요.</p>
  <p><small>자마자 oldida zamon <b>boʻlmaydi</b>. Oʻtgan zamon
  oxirgi feʼlda — 왔어요.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그 소식을 들자마자 전화했어요.</s></p>
  <p class="pe-good">그 소식을 <b>듣자마자</b> 전화했어요.</p>
  <p><small>듣다 ning ㄷ → ㄹ oʻzgarishi faqat <b>unli</b> oldida
  boʻladi. 자마자 undosh bilan boshlanadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>날씨가 춥자마자 사람들이 집에 갔어요.</s></p>
  <p class="pe-good">날씨가 <b>추워져서</b> 사람들이 집에 갔어요.</p>
  <p><small>춥다 — <b>sifat</b>. 자마자 faqat feʼl bilan.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>도착하기가 무섭게 저한테 전화하세요.</s></p>
  <p class="pe-good">도착<b>하자마자</b> 저한테 전화하세요.</p>
  <p><small>기가 무섭게 — boʻlib oʻtgan hayratli voqea uchun.
  Buyruqqa <b>자마자</b> kerak.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>교실에 학생이 많이 있는다.</s></p>
  <p class="pe-good">교실에 학생이 많이 <b>있다</b>.</p>
  <p><small>있다/없다 한다체 da oʻzgarmaydi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 집에
  <span class="pe-blank"></span> 손을 씻었어요. (오다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>오자마자</b> — oʻzak 오 + 자마자, 받침 farqi yoʻq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Nega
  <s>수업이 끝났자마자</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>자마자 oldida <b>zamon boʻlmaydi</b>. Toʻgʻrisi —
    <b>끝나자마자</b>, oʻtgan zamon esa gapning oxirida.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Qaysi biri toʻgʻri:
  듣자마자 / 들자마자?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>듣자마자</b>. ㄷ notoʻgʻri feʼli faqat unli oldida
    ㄹ ga aylanadi (들어요), 자마자 esa undosh.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Qaysi jumlada
  <b>기가 무섭게</b> mos keladi?<br>
  (a) 아침에 일어나기가 무섭게 세수했어요.<br>
  (b) 표가 나오기가 무섭게 다 팔렸어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>(b)</b>. 기가 무섭게 hayratlanarli tezlikni bildiradi.
    Ertalab yuvinish — kutilgan, oddiy ish.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> 한다체 ga oʻgiring:
  학생들이 교실에서 책을 읽어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>학생들이 교실에서 책을 읽는다.</b> 읽 da 받침 bor →
    <b>는다</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> 한다체 ga oʻgiring:
  날씨가 좋아요. 그래서 밖에 나갔어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>날씨가 좋다. 그래서 밖에 나갔다.</b> 좋다 — sifat,
    lugʻat shaklida qoladi; oʻtgan zamon 았/었다.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> “Dars tugashi bilanoq
  uyga qaytdim” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>수업이 끝나자마자 집에 돌아왔어요.</b> (한다체 da:
    돌아왔다.)</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>자마자</b> — …ishi bilanoq</li>
  <li><b>기가 무섭게</b> — …ishga ulgurmay (kuchli, yozma)</li>
  <li><b>한다체 / 문어체</b> — kitob tili, yozma uslub</li>
  <li><b>도착하다</b> — yetib kelmoq</li>
  <li><b>소식</b> — xabar</li>
  <li><b>팔리다</b> — sotilmoq</li>
  <li><b>반대하다</b> — eʼtiroz bildirmoq</li>
  <li><b>소리를 지르다</b> — qichqirmoq</li>
  <li><b>돌아오다</b> — qaytib kelmoq</li>
  <li><b>씻다</b> — yuvmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>자마자</b> = “…ishi bilanoq”. Feʼl oʻzagiga toʻgʻridan
      toʻgʻri, <b>받침 farqi yoʻq</b>.</li>
    <li>Oldida <b>hech qachon zamon yoʻq</b>: 도착하자마자, ❌ 도착했자마자.</li>
    <li>Faqat <b>feʼl</b> bilan — sifat va ot bilan emas.</li>
    <li>고 = shunchaki tartib · 아/어서 = bogʻliq ketma-ketlik ·
      <b>자마자 = nol masofa</b>.</li>
    <li><b>기가 무섭게</b> = boʻrttirma, hayratli tezlik. Koʻproq yozma,
      odatda oʻtgan voqea haqida.</li>
    <li>Oʻzbekcha juftlari: “<b>…ishi bilanoq</b>” va
      “<b>borar-bormas</b>”.</li>
    <li><b>한다체</b>: 간다 · 먹는다 · 좋다 · 있다 · 갔다 · 학생이다 ·
      갈 것이다 · 가지 않는다.</li>
    <li>Hikoya 한다체 da, lekin <b>qoʻshtirnoq ichi</b> oʻz uslubida
      qoladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-75
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-75: 는 길에, 는 김에 — yoʻl-yoʻlakay va fursatdan foydalanib",
        "category": "korean",
        "order": 75,
        "summary": (
            "“Ishdan qaytayotib doʻkonga kirdim” va “chiqqan ekanman, "
            "bir yoʻla nonni ham olay” — bitta yurishda ikkinchi ish."
        ),
        "stories": ["문 닫은 서점"],
        "content": """
<h2>PK-75: 는 길에, 는 김에 — yoʻl-yoʻlakay va fursatdan foydalanib</h2>

<p>Ishdan qaytyapsiz. Yoʻlda doʻkon koʻrinadi — kirib sut olasiz.
Doʻkonga <em>maxsus</em> chiqmagansiz: shundoq ham oʻsha yoʻldan
ketayotgan edingiz. Oʻzbekcha bunga bitta ajoyib soʻz bor:
<b>yoʻl-yoʻlakay</b>. Koreys tilida esa <em>ikkita</em> qolip bor, va
ular orasidagi farq — bugungi darsning butun mazmuni.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>는 길에</b> bilan “…ga ketayotib” deysiz</li>
    <li>Nega u faqat <b>yurish feʼllari</b> bilan ishlashini bilib olasiz</li>
    <li><b>는 김에</b> bilan “bir yoʻla, fursatdan foydalanib” deysiz</li>
    <li>Ikkalasini yonma-yon qoʻyib farqni koʻrasiz</li>
    <li>PK-71 dagi <b>(으)ㄹ 겸</b> bilan solishtirasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qolip</span>
  <span class="pe-chip pe-chip--v">가다/오다 + 는 길에</span>
  <span class="pe-chip pe-chip--aux">feʼl + 는/(으)ㄴ 김에</span>
  <span class="pe-chip pe-chip--adv">= yoʻlda / bir yoʻla</span>
</div>

<h3>1. 는 길에 — “…ga ketayotib”</h3>

<p><b>길</b> — “yoʻl”. Demak 는 길에 soʻzma-soʻz “…ayotgan yoʻlda”.
Bu <em>haqiqiy</em> yoʻl: siz A dan B ga borayapsiz va oʻrtada nimadir
qilasiz.</p>

<div class="pe-call pe-rule">
  <p><b>Eng muhim cheklov:</b> 는 길에 faqat <b>harakat feʼllari</b>
  bilan ishlaydi — <b>가다, 오다</b> va ular bilan tuzilganlar:
  출근하다, 퇴근하다, 등교하다, 돌아가다, 나가다.<br>
  ❌ <s>밥을 먹는 길에</s> · ❌ <s>공부하는 길에</s> — bular yoʻl emas.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">학교에 <span class="pe-hl pe-hl--v">가는 길에</span>
     자수르 씨를 만났어요.</p>
  <p class="pe-ex__uz">Maktabga ketayotib Jasurni uchratdim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">퇴근하는 길에 <span class="pe-hl pe-hl--o">약국</span>에
     들렀어요.</p>
  <p class="pe-ex__uz">Ishdan qaytayotib dorixonaga kirdim.</p>
  <p class="pe-ex__why"><b>들르다</b> — “yoʻl-yoʻlakay kirmoq”.
  는 길에 ning eng sodiq sherigi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">집에 <span class="pe-hl pe-hl--v">오는 길에</span>
     비를 맞았어요.</p>
  <p class="pe-ex__uz">Uyga kelayotib yomgʻirda qoldim.</p>
</div>

<div class="pe-call pe-tip">
  <p>Oʻtgan zamonda ham <b>는</b> qoladi: 어제 학교에 <b>가는 길에</b>
  만났어요. Chunki “ketayotgan” — oʻsha paytdagi holat. Zamon
  oxirgi feʼlda koʻrsatiladi (PK-43 dagi aniqlovchi qoidasi).</p>
</div>

<h3>2. 는 김에 — “bir yoʻla, mayli, shu bahonada”</h3>

<p><b>김</b> — bu yerda “qulay payt, fursat” degani. 는 김에 esa
shunday deydi: <em>“Men baribir A ni qilyapman — shu bahonada B ni
ham qilib qoʻyaman.”</em> B — <b>rejalashtirilmagan qoʻshimcha</b>.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">Hozir qilinayotgan ish</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">는 김에</span></p>
    <p>가다 → 가는 김에</p>
    <p>청소하다 → 청소하는 김에</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">Allaqachon qilingan ish</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">(으)ㄴ 김에</span></p>
    <p>오다 → 온 김에</p>
    <p>시작하다 → 시작한 김에</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시장에 <span class="pe-hl pe-hl--aux">가는 김에</span>
     빵도 좀 사 주세요.</p>
  <p class="pe-ex__uz">Bozorga borayotgan ekansiz, bir yoʻla non ham
  olib bering.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">여기까지 <span class="pe-hl pe-hl--aux">온 김에</span>
     차 한잔 마시고 가요.</p>
  <p class="pe-ex__uz">Shu yergacha kelgan ekansiz, bir piyola choy
  ichib keting.</p>
  <p class="pe-ex__why">Kelish <b>tugagan</b> — shuning uchun
  <b>온 김에</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">방을 <span class="pe-hl pe-hl--aux">청소하는 김에</span>
     창문도 닦았어요.</p>
  <p class="pe-ex__uz">Xonani tozalayotgan ekanman, derazani ham
  artib qoʻydim.</p>
  <p class="pe-ex__why">Bu yerda hech qanday <b>yoʻl yoʻq</b> —
  demak 길에 emas, faqat <b>김에</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida 김에 uchun tayyor qolip bor:</b>
  “bor<b>gan ekansiz</b>, …”, “chiq<b>qan ekanman</b>, …”,
  “<b>shu bahonada</b>”, “<b>bir yoʻla</b>”. Eʼtibor bering — bizda
  ham bu qolip <em>oʻtgan zamon</em> shaklida (“kelgan ekansiz”)
  boʻlishi mumkin, xuddi 온 김에 kabi. Ikkala tilda ham mantiq bir xil:
  <em>bu ish allaqachon boʻlyapti, uni yana bir foyda uchun
  ishlataylik</em>.</p>
</div>

<h3>3. 길에 va 김에 — yonma-yon</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">는 길에 — JOY</p>
    <p>Siz <b>yoʻldasiz</b>. Ikkinchi ish shu yoʻlning ustida
    sodir boʻladi.</p>
    <p>Faqat <b>가다 / 오다</b> guruhi.</p>
    <p><small>학교에 가는 길에 친구를 만났어요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">는 김에 — FURSAT</p>
    <p>Siz <b>bir ish qilyapsiz</b>. Shu bahonada ikkinchisini
    ham qilib qoʻyasiz.</p>
    <p><b>Har qanday</b> feʼl bilan.</p>
    <p><small>청소하는 김에 창문도 닦았어요.</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Tekshirish usuli:</b> gapda haqiqiy <em>yurish</em> bormi?
  Agar bor boʻlsa — ikkalasi ham mumkin, lekin maʼno oʻzgaradi:<br>
  시장에 <b>가는 길에</b> 친구를 만났어요. → Bozorga ketayotib
  <em>tasodifan</em> uchratdim.<br>
  시장에 <b>가는 김에</b> 빵도 샀어요. → Bozorga borayotgan ekanman,
  <em>ataylab</em> nonni ham oldim.<br>
  Yaʼni: <b>길에 = tasodif, 김에 = qoʻshimcha qaror</b>.</p>
</div>

<h3>4. 김에 va PK-71 dagi 겸</h3>

<p>Ikkalasi ham “bir yoʻla” deb tarjima qilinadi. Farq —
<b>qachon qaror qilinganida</b>.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Qachon oʻylangan</th><th>Misol</th></tr>
  <tr><td class="pk-stem">(으)ㄹ 겸 <small>PK-71</small></td>
      <td><b>oldindan</b> — ikkala maqsad ham rejada</td>
      <td>운동도 할 겸 친구도 만날 겸 공원에 갔어요.</td></tr>
  <tr><td class="pk-stem">는 김에</td>
      <td><b>joyida</b> — birinchi ish boshlangach oʻylab qolindi</td>
      <td>공원에 간 김에 운동도 했어요.</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>겸</b> — ikkita maqsad bilan yoʻlga chiqasiz.<br>
  <b>김에</b> — bitta maqsad bilan chiqasiz, ikkinchisi
  <em>yoʻlda paydo boʻladi</em>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>밥을 먹는 길에 친구를 만났어요.</s></p>
  <p class="pe-good">밥을 <b>먹는 김에</b> 친구도 만났어요.</p>
  <p><small>Ovqat yeyish — yoʻl emas. 길에 faqat 가다/오다 bilan.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>여기까지 오는 김에 차 한잔 마셔요.</s></p>
  <p class="pe-good">여기까지 <b>온 김에</b> 차 한잔 마셔요.</p>
  <p><small>Kelish <b>tugagan</b> — oʻtgan aniqlovchi
  <b>(으)ㄴ</b> kerak.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>학교에 갔는 길에 친구를 만났어요.</s></p>
  <p class="pe-good">학교에 <b>가는 길에</b> 친구를 만났어요.</p>
  <p><small>길에 oldida hamisha <b>는</b> — zamon oxirgi
  feʼlda.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>도서관에 가는 김에 책을 빌리려고 갔어요.</s></p>
  <p class="pe-good">책을 <b>빌릴 겸</b> 도서관에 갔어요.</p>
  <p><small>Kitob olish <b>asosiy maqsad</b> boʻlsa, u
  “qoʻshimcha” emas. Reja boʻlsa — <b>겸</b>.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> 길에 yoki 김에?
  회사에 가는 <span class="pe-blank"></span> 커피를 샀어요.
  (koʻzim tushdi, yoʻlda edim)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Ikkalasi ham mumkin! <b>가는 길에</b> = yoʻlda edim;
    <b>가는 김에</b> = borayotgan ekanman, atay oldim.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring:
  방을 <span class="pe-blank"></span> 김에 책상도 정리했어요. (청소하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>청소하는</b> — ish davom etayotgan edi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Nega
  <s>공부하는 길에 음악을 들었어요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>공부하다 — harakat feʼli emas. Toʻgʻrisi
    <b>공부하는 김에</b>, yoki bir vaqtda boʻlsa
    <b>공부하면서</b> (PK-39).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 겸 yoki 김에?
  “Sport ham qilay, doʻstimni ham koʻray deb parkka bordim.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>겸</b> — ikkala maqsad ham <em>oldindan</em> bor edi:
    운동도 할 <b>겸</b> 친구도 만날 <b>겸</b> 공원에 갔어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> “Shu yergacha kelgan ekansiz,
  ovqatlanib keting” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>여기까지 온 김에 식사하고 가세요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bu gapni 한다체 ga oʻgiring
  (PK-74): 퇴근하는 길에 약국에 들렀어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>퇴근하는 길에 약국에 들렀다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>는 길에</b> — …ga ketayotib, yoʻl-yoʻlakay</li>
  <li><b>는/(으)ㄴ 김에</b> — bir yoʻla, shu bahonada</li>
  <li><b>들르다</b> — yoʻlda kirib oʻtmoq</li>
  <li><b>퇴근하다</b> — ishdan qaytmoq</li>
  <li><b>출근하다</b> — ishga bormoq</li>
  <li><b>약국</b> — dorixona</li>
  <li><b>닦다</b> — artmoq, tozalamoq</li>
  <li><b>정리하다</b> — tartibga solmoq</li>
  <li><b>빌리다</b> — qarzga olmoq, ijaraga olmoq</li>
  <li><b>비를 맞다</b> — yomgʻirda qolmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>는 길에</b> = “…ga ketayotib”. <b>길</b> = yoʻl.</li>
    <li>Faqat <b>가다 / 오다</b> guruhidagi feʼllar bilan.</li>
    <li>Oldida hamisha <b>는</b> — ❌ 갔는 길에.</li>
    <li><b>는 김에</b> = “bir yoʻla, shu bahonada”. Har qanday feʼl
      bilan.</li>
    <li>Ish davom etsa <b>는 김에</b>, tugagan boʻlsa
      <b>(으)ㄴ 김에</b>.</li>
    <li>길에 = <b>tasodif</b> · 김에 = <b>qoʻshimcha qaror</b>.</li>
    <li><b>겸</b> (PK-71) = ikki maqsad oldindan rejada ·
      <b>김에</b> = ikkinchisi yoʻlda paydo boʻldi.</li>
    <li>Oʻzbekcha juftlari: “<b>yoʻl-yoʻlakay</b>” va
      “<b>…gan ekansiz, bir yoʻla</b>”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-76
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-76: 고 나서, (으)ㄴ 채로 — tugagach va shu holicha",
        "category": "korean",
        "order": 76,
        "summary": (
            "“Ovqatni yeb boʻlgach chiqdim” va “poyabzalini yechmagan "
            "holicha kirdi” — tugallangan ish va saqlanib turgan holat."
        ),
        "stories": ["잠을 방해하는 다섯 가지 습관"],
        "content": """
<h2>PK-76: 고 나서, (으)ㄴ 채로 — tugagach va shu holicha</h2>

<p>Chiroqni oʻchirmagan <em>holicha</em> uxlab qoldingiz. Ertalab
uygʻonib, yuvinib <em>boʻlgach</em>, ishga chiqdingiz. Ikki xil vaqt
munosabati: birida bir ish <b>butunlay tugaydi</b>, ikkinchisida bir
holat <b>saqlanib turadi</b>. Bugun ikkalasi ham.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>고 나서</b> bilan “…ib boʻlgach” deysiz</li>
    <li>Uni PK-33 dagi oddiy <b>고</b> dan ajratasiz</li>
    <li><b>(으)ㄴ 채로</b> bilan “…gan holicha” deysiz</li>
    <li>채로 ni PK-39 dagi <b>(으)면서</b> dan farqlaysiz</li>
    <li>Nega 채로 koʻpincha <b>gʻalati holat</b> haqida ekanini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qolip</span>
  <span class="pe-chip pe-chip--v">feʼl + 고 나서</span>
  <span class="pe-chip pe-chip--s">feʼl + (으)ㄴ 채로</span>
  <span class="pe-chip pe-chip--adv">= boʻlgach / holicha</span>
</div>

<h3>1. 고 나서 — “…ib boʻlgach”</h3>

<p><b>나다</b> — “tugamoq, chiqmoq”. 고 나서 esa shuni aytadi:
birinchi ish <b>toʻliq tugadi</b>, keyin ikkinchisi boshlandi.
Urgʻu — <em>tugallikda</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">숙제를 <span class="pe-hl pe-hl--v">하고 나서</span>
     텔레비전을 봤어요.</p>
  <p class="pe-ex__uz">Uy vazifasini bajarib boʻlgach televizor
  koʻrdim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 책을 <span class="pe-hl pe-hl--v">읽고 나서</span>
     생각이 바뀌었어요.</p>
  <p class="pe-ex__uz">Bu kitobni oʻqib boʻlgach fikrim oʻzgardi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">운동을 <span class="pe-hl pe-hl--v">하고 나서</span>
     샤워를 해요.</p>
  <p class="pe-ex__uz">Sport bilan shugʻullanib boʻlgach dush qabul
  qilaman.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha “-ib boʻlmoq” — aynan 나서 ning oʻzi.</b>
  “yozib <b>boʻldim</b>”, “yeb <b>boʻlgach</b>”, “oʻqib
  <b>boʻlgandan keyin</b>”. Bizda ham <em>boʻlmoq</em> yordamchi
  feʼli tugallikni koʻrsatadi, xuddi koreyscha <b>나다</b> kabi.
  Shuning uchun 고 나서 ni eslash oson: <em>고 = -ib, 나서 =
  boʻlgach</em>.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">고 <small>PK-33</small></p>
    <p>Shunchaki tartib. Birinchi ish tugadimi — aytilmagan.</p>
    <p><small>밥을 먹고 나갔어요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">고 나서</p>
    <p><b>Tugallik urgʻulanadi.</b> Yeb <em>boʻldim</em>, keyin
    chiqdim.</p>
    <p><small>밥을 먹고 나서 나갔어요.</small></p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>고 나서 ning uch qoidasi:</b><br>
  1. Faqat <b>feʼl</b> bilan (❌ <s>바쁘고 나서</s>).<br>
  2. Ikkala gapning egasi <b>bir xil</b> boʻlishi kerak —
  ❌ <s>비가 오고 나서 저는 나갔어요</s> → bunda
  <b>비가 온 후에</b> (PK-38).<br>
  3. Oldida zamon <b>yoʻq</b>: ❌ <s>했고 나서</s> → ✅ <b>하고 나서</b>.</p>
</div>

<h3>2. (으)ㄴ 채로 — “…gan holicha”</h3>

<p><b>채</b> — “holat, koʻrinish” degan ot. <b>(으)ㄴ 채로</b> shuni
aytadi: bir ish qilingan va uning <em>natijasi hamon saqlanib
turibdi</em> — aynan shu holatda ikkinchi ish boʻlyapti.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄴ 채로</span></p>
    <p>켜다 → 켠 채로</p>
    <p>타다 → 탄 채로</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">은 채로</span></p>
    <p>신다 → 신은 채로</p>
    <p>입다 → 입은 채로</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">신발을 <span class="pe-hl pe-hl--s">신은 채로</span>
     방에 들어갔어요.</p>
  <p class="pe-ex__uz">Poyabzalini yechmagan holicha xonaga kirdi.</p>
  <p class="pe-ex__why">Koreyada bu <b>qoʻpol xato</b> — 채로 ning eng
  mashhur misoli aynan shu.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">불을 <span class="pe-hl pe-hl--s">켠 채로</span>
     잠이 들었어요.</p>
  <p class="pe-ex__uz">Chiroqni yoqqan koʻyi uxlab qoldim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">창문을 <span class="pe-hl pe-hl--s">열어 놓은 채로</span>
     외출했어요.</p>
  <p class="pe-ex__uz">Derazani ochiq qoldirgan holicha tashqariga
  chiqdim.</p>
  <p class="pe-ex__why">PK-59 dagi <b>아/어 놓다</b> bilan birga —
  “ochib qoʻyilgan holat”.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bunga ikkita toʻliq mos shakl bor:</b>
  “-<b>gan holicha</b>” va “-<b>gancha</b>” (kitobiy tilda
  “-gan koʻyi”). “Kiy<b>gancha</b> yotdi”, “och<b>gan holicha</b>
  ketdi”, “yoq<b>qan koʻyi</b> uxlab qoldi”. Uchalasi ham aynan bir
  narsani bildiradi: <em>ish tugagan, lekin uning izi turibdi</em>.
  Koreyscha 채로 — shu izning nomi.</p>
</div>

<h3>3. 채로 va (으)면서 — eng koʻp adashiladigan juftlik</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)면서 <small>PK-39</small></p>
    <p><b>Ikki HARAKAT</b> bir vaqtda davom etadi. Ikkalasi ham
    “bajarilyapti”.</p>
    <p><small>음악을 들으면서 공부해요.</small><br>
    <small>(quloq eshitmoqda, koʻz oʻqimoqda — ikkovi ham ish)</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)ㄴ 채로</p>
    <p><b>Bir HOLAT</b> + bitta harakat. Birinchisi allaqachon
    tugagan, faqat natijasi turibdi.</p>
    <p><small>신발을 신은 채로 들어갔어요.</small><br>
    <small>(kiyish tugagan — endi faqat “kiyilgan” holat)</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Oson tekshiruv:</b> birinchi feʼlni “hozir qilyapman”
  deb ayta olasizmi?<br>
  “Musiqa <em>tinglayapman</em>” — ha → <b>면서</b>.<br>
  “Poyabzal <em>kiyayapman</em>”? Yoʻq — kiyib boʻlgansiz, endi
  shunchaki kiyimda turibsiz → <b>채로</b>.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>채로 deyarli har doim gʻalati, notoʻgʻri yoki kutilmagan
  holat haqida.</b> Chiroq yoniq uxlash, poyabzalda kirish, koʻzoynak
  taqqan holda yuvinish. Oddiy, tabiiy holat uchun koreyslar 채로 emas,
  <b>아/어 있다</b> (PK-42) yoki <b>고 있다</b> ni tanlaydi.
  Shuning uchun 채로 gapga bir tomchi <em>tanqid</em> yoki
  <em>ajablanish</em> qoʻshadi.</p>
</div>

<h3>4. Uchtasi bir qatorda</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Birinchi ish</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pk-stem">고 나서</td><td>butunlay <b>tugadi</b>, izi qolmadi</td>
      <td class="pk-uz">…ib boʻlgach</td></tr>
  <tr><td class="pk-stem">(으)ㄴ 채로</td><td>tugadi, lekin <b>holati turibdi</b></td>
      <td class="pk-uz">…gan holicha</td></tr>
  <tr><td class="pk-stem">(으)면서 <small>PK-39</small></td>
      <td>hali ham <b>davom etyapti</b></td>
      <td class="pk-uz">…a turib</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>숙제를 했고 나서 잤어요.</s></p>
  <p class="pe-good">숙제를 <b>하고 나서</b> 잤어요.</p>
  <p><small>고 나서 oldida zamon <b>boʻlmaydi</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>비가 오고 나서 저는 우산을 샀어요.</s></p>
  <p class="pe-good">비가 <b>온 후에</b> 저는 우산을 샀어요.</p>
  <p><small>고 나서 da <b>ega bir xil</b> boʻlishi shart. Har xil
  ega uchun — PK-38 dagi <b>(으)ㄴ 후에</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>신발을 신는 채로 들어갔어요.</s></p>
  <p class="pe-good">신발을 <b>신은 채로</b> 들어갔어요.</p>
  <p><small>채로 oldida hamisha <b>oʻtgan aniqlovchi (으)ㄴ</b> —
  holat allaqachon vujudga kelgan.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음악을 들은 채로 공부했어요.</s></p>
  <p class="pe-good">음악을 <b>들으면서</b> 공부했어요.</p>
  <p><small>Tinglash — davom etayotgan <b>harakat</b>, holat emas.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 밥을
  <span class="pe-blank"></span> 나서 약을 먹어요. (먹다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>먹고</b> — 고 나서 da oʻzak + 고.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 안경을
  <span class="pe-blank"></span> 채로 잤어요. (쓰다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>쓴</b> — 쓰 da 받침 yoʻq → <b>ㄴ 채로</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 면서 yoki 채로?
  “Televizor koʻra turib ovqat yedim.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>면서</b> — koʻrish davom etayotgan harakat:
    텔레비전을 <b>보면서</b> 밥을 먹었어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 면서 yoki 채로?
  “Paltosini yechmagan holicha oʻtirdi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>채로</b> — kiyish tugagan, faqat holat qolgan:
    코트를 <b>입은 채로</b> 앉았어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Nega
  <s>비가 오고 나서 친구가 왔어요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Egalar har xil (yomgʻir / doʻst). 고 나서 bitta ega talab
    qiladi. Toʻgʻrisi — <b>비가 온 후에</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Chiroqni yoqqan koʻyi uxlab
  qoldi” — koreyschada, 한다체 da (PK-74).</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>불을 켠 채로 잠이 들었다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>고 나서</b> — …ib boʻlgach</li>
  <li><b>(으)ㄴ 채로</b> — …gan holicha, …gancha</li>
  <li><b>잠이 들다</b> — uyquga ketmoq</li>
  <li><b>안경을 쓰다</b> — koʻzoynak taqmoq</li>
  <li><b>외출하다</b> — tashqariga chiqmoq</li>
  <li><b>바뀌다</b> — oʻzgarmoq</li>
  <li><b>습관</b> — odat</li>
  <li><b>방해하다</b> — xalaqit bermoq</li>
  <li><b>켜다 / 끄다</b> — yoqmoq / oʻchirmoq</li>
  <li><b>벗다</b> — yechmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>고 나서</b> = “…ib boʻlgach”. <b>나다</b> = tugamoq.</li>
    <li>Faqat feʼl, <b>bitta ega</b>, oldida zamon yoʻq.</li>
    <li>고 = shunchaki tartib · <b>고 나서 = tugallik urgʻusi</b>.</li>
    <li><b>(으)ㄴ 채로</b> = “…gan holicha”. <b>채</b> = holat.</li>
    <li>받침 yoʻq → <b>ㄴ 채로</b> · 받침 bor → <b>은 채로</b>.
      Hamisha oʻtgan aniqlovchi.</li>
    <li>면서 = ikki <b>harakat</b> · 채로 = bir <b>holat</b> +
      bir harakat.</li>
    <li>채로 koʻpincha <b>gʻalati yoki notoʻgʻri</b> holat haqida —
      shuning uchun ohangida tanqid bor.</li>
    <li>Oʻzbekcha juftlari: “<b>…ib boʻlgach</b>” va
      “<b>…gancha / …gan holicha</b>”.</li>
  </ul>
</div>
""",
    },
]
