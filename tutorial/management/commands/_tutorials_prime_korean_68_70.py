# -*- coding: utf-8 -*-
"""Prime Korean — Block E oxiri + Block F boshi, darslar 68–70.

68. (으)ㄴ/는 데다가 — vaziyatning ogʻirlashuvi
69. 는 바람에, (으)ㄴ/는 탓에, 느라고 — salbiy sabab va bahona
70. (으)ㄹ걸 (그랬다), 았/었어야 했다 — afsus va pushaymonlik

Uchtasi bitta hikoyaning uch bosqichi: muammolar USTMA-UST tushadi (68),
keyin AYB qidiriladi (69), oxirida esa PUSHAYMON boʻlinadi (70).
Shu tartib matnlarda ham saqlangan.

Oʻzbekcha kalitlar:
  (으)ㄴ/는 데다가 = "ustiga ustak", "…yetmagandek"
  느라고           = "…ga OVORA BOʻLIB"
  탓에 / 덕분에    = "AYBI bilan" / "SHAROFATI bilan"
  (으)ㄹ걸 그랬다   = "…sam boʻlardi"
  았/었어야 했다   = "…shim KERAK EDI"

68 dagi 데 — oltinchi aniqlovchi + ot: 것 · 줄 · 뻔 · 테 · 뿐 · 데.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_68_70.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_68_70.py --author=prime
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
        "title": "PK-68: (으)ㄴ/는 데다가 — vaziyatning ogʻirlashuvi",
        "category": "korean",
        "order": 68,
        "summary": (
            "“Yomgʻir yogʻayotgani yetmagandek, shamol ham esdi” — ikkinchi "
            "narsa birinchisining ustiga tushadi. Koreyschada 오는 데다가."
        ),
        "stories": ["산속 호텔 후기 — 별 두 개"],
        "content": """
<h2>PK-68: (으)ㄴ/는 데다가 — vaziyatning ogʻirlashuvi</h2>

<p>Ertalab kech uygʻondingiz. Bu yomon. Tashqariga chiqsangiz — yomgʻir.
Bu yanada yomon. Endi buni qanday aytasiz? “Kech uygʻonganim
<b>yetmagandek</b>, yomgʻir ham yogʻyapti” yoki “<b>ustiga ustak</b>
yomgʻir yogʻyapti”. Ikkinchi narsa birinchisining <em>ustiga</em>
tushadi va vaziyatni ogʻirlashtiradi. Koreys tilida bu —
<b>(으)ㄴ/는 데다가</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄴ/는 데다가</b> bilan ikkinchi holatni ustiga qoʻyasiz</li>
    <li>Feʼl, sifat va ot uchun uchta shaklni ajratasiz</li>
    <li>Uni PK-67 dagi <b>뿐만 아니라</b> dan farqlaysiz</li>
    <li>Uchta qatʼiy shartini bilib olasiz</li>
    <li>Oltinchi <b>aniqlovchi + ot</b> qolipini tanib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Aniqlovchi shakl</span>
  <span class="pe-chip pe-chip--v">데다가</span>
  <span class="pe-chip pe-chip--adv">= …, ustiga ustak …</span>
</div>

<h3>1. 데 — “joy, holat” degan ot</h3>

<p><b>데</b> — “joy” yoki “holat” degan ot. Unga <b>다가</b>
(“ustiga qoʻshib”) qoʻshiladi. Yaʼni 비가 오는 데다가 soʻzma-soʻz
“yomgʻir yogʻayotgan <em>holatning ustiga</em>”.</p>

<div class="pe-call pe-rule">
  <p><b>Oltinchisi.</b> PK-52 da 것, PK-53 da 줄, PK-63 da 뻔, PK-64
  da 테, PK-67 da 뿐 — bugun <b>데</b>. Oltitasi ham <em>aniqlovchi +
  ot</em>. Endi bu mashinani koʻrsangiz darrov tanishingiz kerak:
  yangi qolipning yarmi allaqachon tanish boʻladi.</p>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima</th><th>Shakl</th><th>Misol</th><th>Natija</th></tr>
  <tr><td><b>Feʼl</b> (hozirgi)</td><td class="pk-end">는 데다가</td>
      <td class="pk-stem">오다</td><td class="pk-res">오는 데다가</td></tr>
  <tr><td><b>Sifat</b>, 받침 yoʻq</td><td class="pk-end">ㄴ 데다가</td>
      <td class="pk-stem">비싸다</td><td class="pk-res">비싼 데다가</td></tr>
  <tr><td><b>Sifat</b>, 받침 bor</td><td class="pk-end">은 데다가</td>
      <td class="pk-stem">좋다</td><td class="pk-res">좋은 데다가</td></tr>
  <tr><td><b>Ot</b> (이다)</td><td class="pk-end">인 데다가</td>
      <td class="pk-stem">학생이다</td><td class="pk-res">학생인 데다가</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">비가 <span class="pe-hl pe-hl--v">오는 데다가</span>
     바람도 세게 불어요.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻyapti, ustiga ustak shamol ham
  kuchli esyapti.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 식당은 음식이 <span class="pe-hl pe-hl--adv">맛있는
     데다가</span> 값도 싸요.</p>
  <p class="pe-ex__uz">U oshxonaning ovqati mazali, ustiga narxi ham
  arzon.</p>
  <p class="pe-ex__why">Ikkala tomon ham ijobiy — bu ham toʻgʻri.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu maʼno uchun bir nechta tayyor ibora bor:</b>
  “<b>ustiga ustak</b>”, “buning <b>ustiga</b>”, “…gani
  <b>yetmagandek</b>”. Uchalasi ham bitta ishni qiladi: birinchi
  holatni aytadi, keyin ikkinchisini <em>uning ustiga qoʻyadi</em>.
  Diqqat qiling — bu shunchaki “va” emas. “Sovuq va shamol bor”
  ikkita alohida fakt. “Sovuq, <b>ustiga ustak</b> shamol ham bor”
  esa <em>toʻplanib boradigan</em> ogʻirlik. 데다가 aynan
  shu ikkinchisini bildiradi.</p>
</div>

<h3>2. Uchta qatʼiy shart</h3>

<div class="pe-steps">
  <div class="pe-step">
    <p><b>1. Bir xil yoʻnalish.</b> Ikkala holat ham yomon boʻlishi
    yoki ikkalasi ham yaxshi boʻlishi kerak.<br>
    <s>예쁜 데다가 성격이 나빠요</s> ✗ — biri maqtov, biri ayb.</p>
  </div>
  <div class="pe-step">
    <p><b>2. Bir xil mavzu.</b> Ikkala gap ham <em>bitta narsa yoki
    odam</em> haqida boʻladi.<br>
    그 식당은 음식이 맛있는 데다가 <span class="pk-par">값도</span>
    싸요 — ikkalasi ham oʻsha oshxona haqida.</p>
  </div>
  <div class="pe-step">
    <p><b>3. Koʻpincha natija keladi.</b> Toʻplangan ogʻirlik biror
    narsaga olib keladi.<br>
    길이 막히는 데다가 비까지 와서 <span class="pe-hl pe-hl--v">늦었어요</span>.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어제는 몸이 <span class="pe-hl pe-hl--adv">아픈
     데다가</span> 일<span class="pk-par">도</span> 많아서 정말
     힘들었어요.</p>
  <p class="pe-ex__uz">Kecha kasal edim, ustiga ish ham koʻp edi —
  juda qiynaldim.</p>
</div>

<div class="pe-call pe-tip">
  <p>Ikkinchi gapda koʻpincha <b>도</b> (“ham”) yoki <b>까지</b>
  (“hatto…gacha”) turadi. <b>까지</b> ohangni yanada kuchaytiradi:
  비<b>까지</b> 왔어요 — “yomgʻir <em>ham</em> yogʻdi-ya!”.</p>
</div>

<h3>3. 뿐만 아니라 (PK-67) bilan farqi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)ㄹ 뿐만 아니라</p>
    <p><b>Roʻyxat.</b> Ikkinchi dalilni qoʻshadi — sanaydi.</p>
    <p><small>한국어뿐만 아니라 문화도 배워요.</small></p>
    <p><small>Ega boshqa-boshqa boʻlsa ham boʻladi.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)ㄴ/는 데다가</p>
    <p><b>Toʻplanish.</b> Ikkinchisi birinchisining ustiga tushadi.</p>
    <p><small>길이 막히는 데다가 비까지 와서 늦었어요.</small></p>
    <p><small>Bir xil mavzu, koʻpincha natija bilan.</small></p>
  </div>
</div>

<div class="pe-call pe-warn">
  <p>Koʻp holatda <b>ikkalasi ham toʻgʻri</b> boʻladi — 맛있을 뿐만
  아니라 값도 싸요 ham, 맛있는 데다가 값도 싸요 ham. Farq juda nozik:
  <b>뿐만 아니라</b> sanaydi, <b>데다가</b> esa <em>ustiga
  qoʻyadi</em>. Lekin qarama-qarshi tomonlar uchun ikkalasi ham
  ishlamaydi — u yerda PK-66 dagi <b>반면에</b> kerak.</p>
</div>

<h3>4. Qisqargan shakli: 데다</h3>

<p>Ogʻzaki nutqda <b>가</b> koʻpincha tushiriladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">방이 <span class="pe-hl pe-hl--adv">좁은 데다</span>
     창문도 없어요.</p>
  <p class="pe-ex__uz">Xona tor, ustiga derazasi ham yoʻq.</p>
</div>

<h3>5. Ot bilan</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">그 사람은 <span class="pe-hl pe-hl--s">학생인
     데다가</span> 아르바이트도 해요.</p>
  <p class="pe-ex__uz">U odam talaba, ustiga qoʻshimcha ishda ham
  ishlaydi.</p>
  <p class="pe-ex__why">Ot + 이다 → <b>인 데다가</b>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>그 식당은 음식이 맛있는 데다가 값이 비싸요.</s></p>
  <p class="pe-good">음식이 맛있는 <b>반면에</b> 값이 비싸요.</p>
  <p><small>Ikkala tomon <b>bir yoʻnalishda</b> boʻlishi kerak.
  Qarama-qarshi boʻlsa — 반면에 (PK-66).</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>방이 좁는 데다가 창문도 없어요.</s></p>
  <p class="pe-good">방이 <b>좁은</b> 데다가 창문도 없어요.</p>
  <p><small>좁다 — sifat, shuning uchun <b>(으)ㄴ</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>비가 온 데다가 바람도 불어요.</s>
    <small>(hozir yogʻayotgan boʻlsa)</small></p>
  <p class="pe-good">비가 <b>오는</b> 데다가 바람도 불어요.</p>
  <p><small>Feʼl hozirgi zamonda <b>는</b> oladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그 사람은 학생이는 데다가 아르바이트도 해요.</s></p>
  <p class="pe-good">그 사람은 <b>학생인</b> 데다가 아르바이트도 해요.</p>
  <p><small>Ot + 이다 → <b>인</b>.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 비가
  <span class="pe-blank"></span> 데다가 바람도 세게 불어요. (오다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>오는</b> — feʼl, hozirgi zamon → <b>는 데다가</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 방이
  <span class="pe-blank"></span> 데다가 창문도 없어요. (좁다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>좁은</b> — sifat, 받침 bor → <b>은 데다가</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Nima uchun
  <s>예쁜 데다가 성격이 나빠요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Ikkala tomon <b>bir yoʻnalishda</b> boʻlishi kerak. Bu yerda
    biri maqtov, biri ayb — demak <b>반면에</b> kerak:
    예쁜 반면에 성격이 나빠요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 뿐만 아니라 va 데다가 farqi
  nimada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>뿐만 아니라</b> — sanaydi (“faqat … emas, … ham”).
    <b>데다가</b> — ustiga qoʻyadi, ogʻirlik toʻplanadi va koʻpincha
    natija keladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>그 사람은 학생이는 데다가 아르바이트도 해요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>학생인 데다가</b>. Ot + 이다 → 인.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Oltita “aniqlovchi + ot”
  qolipini sanang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>것</b> (52) · <b>줄</b> (53) · <b>뻔</b> (63) ·
    <b>테</b> (64) · <b>뿐</b> (67) · <b>데</b> (68).</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄴ/는 데다가</b> — …, ustiga ustak …</li>
  <li><b>데다</b> — qisqargan shakli</li>
  <li><b>까지</b> — hatto …gacha (kuchaytiruvchi)</li>
  <li><b>세게</b> — kuchli</li>
  <li><b>불다</b> — esmoq</li>
  <li><b>좁다</b> — tor</li>
  <li><b>아르바이트</b> — qoʻshimcha ish</li>
  <li><b>성격</b> — xarakter</li>
  <li><b>후기</b> — sharh, taassurot</li>
  <li><b>최악</b> — eng yomon</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄴ/는 데다가</b> = ikkinchi holat birinchisining
      <b>ustiga</b> tushadi.</li>
    <li>Feʼl → <b>는 데다가</b> · Sifat → <b>(으)ㄴ 데다가</b> ·
      Ot → <b>인 데다가</b>.</li>
    <li>Uch shart: <b>bir yoʻnalish</b> · <b>bir mavzu</b> ·
      koʻpincha <b>natija</b>.</li>
    <li>Ikkinchi gapda <b>도</b> yoki <b>까지</b> turadi.</li>
    <li>Qarama-qarshi tomonlar uchun — <b>반면에</b> (PK-66).</li>
    <li>Ogʻzaki nutqda <b>데다</b> boʻlib qisqaradi.</li>
    <li><b>데</b> — oltinchi aniqlovchi + ot: 것 · 줄 · 뻔 · 테 ·
      뿐 · 데.</li>
    <li>Oʻzbekcha juftligi: “<b>ustiga ustak</b>”, “…gani
      <b>yetmagandek</b>”.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-69: 는 바람에, (으)ㄴ/는 탓에, 느라고 — salbiy sabab va bahona",
        "category": "korean",
        "order": 69,
        "summary": (
            "“Avtobus toʻxtab qolgani tufayli”, “dangasaligim aybi bilan”, "
            "“uy vazifasiga ovora boʻlib” — ish yurishmaganda aytiladigan uchta qolip."
        ),
        "stories": ["지각 대장 베크조드"],
        "content": """
<h2>PK-69: 는 바람에, (으)ㄴ/는 탓에, 느라고 — salbiy sabab va bahona</h2>

<p>Darsga kechikdingiz. Oʻqituvchi soʻraydi: “Nega?”. Endi sizga
<em>sabab</em> kerak — lekin oddiy sabab emas. Ish <b>yurishmadi</b>,
va buni tushuntirish kerak. PK-48 dagi (으)니까 va PK-49 dagi 기 때문에
buni ayta oladi, lekin ohangsiz. Koreys tilida <em>ish
buzilganda</em> ishlatiladigan uchta alohida qolip bor — va uchalasi
uch xil ohangda.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>는 바람에</b> bilan kutilmagan xalaqitni aytasiz</li>
    <li><b>(으)ㄴ/는 탓에</b> bilan aybni koʻrsatasiz</li>
    <li><b>느라고</b> bilan bahona keltirasiz</li>
    <li><b>덕분에</b> — ularning ijobiy juftini bilib olasiz</li>
    <li>Qaysi biri qayerda ishlashini ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchta qolip</span>
  <span class="pe-chip pe-chip--v">는 바람에</span>
  <span class="pe-chip pe-chip--neg">(으)ㄴ/는 탓에</span>
  <span class="pe-chip pe-chip--adv">느라고</span>
</div>

<h3>1. 는 바람에 — kutilmagan xalaqit</h3>

<p><b>바람</b> — “shamol”. Bu tasodif emas: qolipning ohangi aynan
shunday — <em>toʻsatdan bir narsa esib keldi va rejani buzdi</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">비가 <span class="pe-hl pe-hl--v">오는 바람에</span>
     소풍을 못 갔어요.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻib qolgani tufayli sayrga bora
  olmadik.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">버스가 갑자기 <span class="pe-hl pe-hl--v">서는
     바람에</span> 넘어질 뻔했어요.</p>
  <p class="pe-ex__uz">Avtobus toʻsatdan toʻxtab qolgani uchun
  yiqilayozdim.</p>
  <p class="pe-ex__why">PK-63 dagi 뻔하다 bilan juda tabiiy
  juftlik.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Uchta qoidasi:</b><br>
  1. Faqat <b>feʼl</b> bilan, va faqat <b>는</b> shaklida — zamon
  boʻlmaydi (<s>온 바람에</s> ✗).<br>
  2. Natija <b>oʻtgan zamonda</b> va <b>kutilmagan</b> boʻladi.<br>
  3. Natija deyarli har doim <b>salbiy</b>.</p>
</div>

<h3>2. (으)ㄴ/는 탓에 — ayb koʻrsatish</h3>

<p><b>탓</b> — “ayb, gunoh” degan ot. Demak bu qolip shunchaki sabab
emas, <em>ayblov</em> beradi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td>Feʼl (hozirgi)</td><td class="pk-end">는 탓에</td>
      <td class="pk-res">비가 오는 탓에</td></tr>
  <tr><td>Feʼl (oʻtgan)</td><td class="pk-end">(으)ㄴ 탓에</td>
      <td class="pk-res">늦게 잔 탓에</td></tr>
  <tr><td>Sifat</td><td class="pk-end">(으)ㄴ 탓에</td>
      <td class="pk-res">게으른 탓에</td></tr>
  <tr><td>Ot</td><td class="pk-end">탓에</td>
      <td class="pk-res">날씨 탓에</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--neg">게으른 탓에</span>
     시험을 잘 못 봤어요.</p>
  <p class="pe-ex__uz">Dangasaligim aybi bilan imtihonni yaxshi
  topshira olmadim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--neg">날씨 탓에</span>
     비행기가 취소됐어요.</p>
  <p class="pe-ex__uz">Ob-havo tufayli samolyot bekor qilindi.</p>
  <p class="pe-ex__why">Ot bilan — qoʻshimchasiz: 날씨 <b>탓에</b>.</p>
</div>

<h3>3. 덕분에 — ijobiy jufti</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">탓에 — ayb</p>
    <p>Yomon natija. “…ning aybi bilan”.</p>
    <p><small>제 탓에 늦었어요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">덕분에 — sharofat</p>
    <p>Yaxshi natija. “…ning sharofati bilan”.</p>
    <p><small>선생님 덕분에 합격했어요.</small></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham aynan shu juftlik bor:</b> “…ning
  <b>ayb</b>i bilan” va “…ning <b>sharofat</b>i bilan”. Ikkala tilda
  ham bu <em>otlar</em> — “ayb” va “sharofat” — sabab bildirish
  uchun ishlatiladi. Shuning uchun 탓 va 덕분 ni qoʻshimcha deb emas,
  <b>soʻz</b> deb yodlang: shunda ular oʻzbekcha juftlari bilan
  birga esda qoladi.</p>
</div>

<h3>4. 느라고 — bahona</h3>

<p>Eng koʻp ishlatiladigani, chunki bu <em>oʻzingizni oqlash</em>
qolipi: “men <b>u ishga ovora boʻlib</b>, bu ishni qila olmadim”.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">숙제를 <span class="pe-hl pe-hl--adv">하느라고</span>
     잠을 못 잤어요.</p>
  <p class="pe-ex__uz">Uy vazifasiga ovora boʻlib uxlay olmadim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">게임을 <span class="pe-hl pe-hl--adv">하느라고</span>
     전화를 못 받았어요.</p>
  <p class="pe-ex__uz">Oʻyin oʻynashga ovora boʻlib telefonni ololmadim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu — “…ga ovora boʻlib”.</b> “Ovqat pishirishga
  ovora boʻlib, telefonni eshitmadim.” Diqqat qiling: oʻzbekchada ham
  <em>ikkala ishni ham bitta odam</em> qiladi, va ikkinchisi
  <em>bajarilmay qoladi</em>. Koreyschadagi 느라고 ning sharti ham
  aynan shu.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>느라고 ning uchta sharti:</b><br>
  1. Ikkala gapning <b>egasi bir xil</b>.<br>
  2. Faqat <b>feʼl</b> bilan, zamon qoʻshimchasi yoʻq
  (<s>했느라고</s> ✗).<br>
  3. Ikkinchi gap <b>salbiy</b> — koʻpincha 못 yoki 안 bilan.</p>
</div>

<h3>5. Uchtasini yonma-yon</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Ohangi</th><th>Sabab kim/nima</th><th>Misol</th></tr>
  <tr><td class="pk-stem">는 바람에</td><td>kutilmagan xalaqit</td>
      <td>tashqi hodisa</td>
      <td class="pk-res">비가 오는 바람에 못 갔어요</td></tr>
  <tr><td class="pk-stem">(으)ㄴ/는 탓에</td><td>ayblov</td>
      <td>kimningdir aybi</td>
      <td class="pk-res">게으른 탓에 떨어졌어요</td></tr>
  <tr><td class="pk-stem">느라고</td><td>bahona</td>
      <td>oʻzimning boshqa ishim</td>
      <td class="pk-res">숙제하느라고 못 잤어요</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>비가 온 바람에 소풍을 못 갔어요.</s></p>
  <p class="pe-good">비가 <b>오는</b> 바람에 소풍을 못 갔어요.</p>
  <p><small>바람에 dan oldin faqat <b>는</b> — zamon
  qoʻyilmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>숙제를 했느라고 잠을 못 잤어요.</s></p>
  <p class="pe-good">숙제를 <b>하느라고</b> 잠을 못 잤어요.</p>
  <p><small>느라고 dan oldin ham zamon boʻlmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>동생이 게임하느라고 저는 공부를 못 했어요.</s></p>
  <p class="pe-good">동생이 게임하는 <b>바람에</b> 저는 공부를 못
    했어요.</p>
  <p><small>느라고 da <b>egasi bir xil</b> boʻlishi shart. Boshqa
  odam xalaqit bergan boʻlsa — 바람에.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>선생님 탓에 합격했어요.</s></p>
  <p class="pe-good">선생님 <b>덕분에</b> 합격했어요.</p>
  <p><small>Natija yaxshi boʻlsa — <b>덕분에</b>. 탓에 ayb
  koʻrsatadi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 비가
  <span class="pe-blank"></span> 바람에 소풍을 못 갔어요. (오다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>오는</b> — 바람에 dan oldin faqat 는 shakli.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 숙제를
  <span class="pe-blank"></span> 잠을 못 잤어요. (하다 + 느라고)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>하느라고</b> — zamon qoʻshimchasi qoʻyilmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 탓에 va 덕분에 farqi nimada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>탓에</b> — yomon natija, “aybi bilan”.
    <b>덕분에</b> — yaxshi natija, “sharofati bilan”.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Nima uchun
  <s>동생이 게임하느라고 저는 공부를 못 했어요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>느라고 da <b>ikkala gapning egasi bir xil</b> boʻlishi kerak.
    Bu yerda ukam va men — boshqa odamlar. Toʻgʻrisi:
    <b>동생이 게임하는 바람에</b> 저는 공부를 못 했어요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Qaysi qolip “kutilmagan
  xalaqit” ohangini beradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>는 바람에.</b> 바람 (“shamol”) soʻzining oʻzi shuni aytib
    turibdi — toʻsatdan esib keldi va rejani buzdi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Ob-havo tufayli samolyot bekor
  qilindi” — koreyschada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>날씨 탓에 비행기가 취소됐어요.</b> Ot bilan 탓에
    qoʻshimchasiz keladi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>는 바람에</b> — …boʻlib qolgani tufayli (kutilmagan)</li>
  <li><b>(으)ㄴ/는 탓에</b> — …ning aybi bilan</li>
  <li><b>느라고</b> — …ga ovora boʻlib</li>
  <li><b>덕분에</b> — …ning sharofati bilan</li>
  <li><b>소풍</b> — sayr, piknik</li>
  <li><b>게으르다</b> — dangasa</li>
  <li><b>취소되다</b> — bekor qilinmoq</li>
  <li><b>합격하다</b> — imtihondan oʻtmoq</li>
  <li><b>지각하다</b> — darsga kechikmoq</li>
  <li><b>변명</b> — bahona</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>는 바람에</b> = kutilmagan xalaqit. Faqat feʼl, faqat
      <b>는</b>, natija oʻtgan zamon va salbiy.</li>
    <li><b>(으)ㄴ/는 탓에</b> = ayb koʻrsatish. 탓 — “ayb” degan ot;
      ot bilan qoʻshimchasiz keladi (날씨 탓에).</li>
    <li><b>덕분에</b> = uning ijobiy jufti — “sharofati bilan”.</li>
    <li><b>느라고</b> = bahona. Egasi <b>bir xil</b>, zamon yoʻq,
      ikkinchi gap salbiy.</li>
    <li>Boshqa odam xalaqit bersa — 느라고 emas, <b>바람에</b>.</li>
    <li>Oʻzbekcha juftliklari: “…ga <b>ovora boʻlib</b>”,
      “…ning <b>aybi</b> bilan”, “…ning <b>sharofati</b> bilan”.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-70: (으)ㄹ걸 (그랬다), 았/었어야 했다 — afsus va pushaymonlik",
        "category": "korean",
        "order": 70,
        "summary": (
            "“Erta uxlasam boʻlardi”, “erta kelishim kerak edi” — qilmagan "
            "ishingizdan afsuslanish. Koreyschada 일찍 잘걸 그랬어요."
        ),
        "stories": ["후배들에게 — 졸업생의 조언"],
        "content": """
<h2>PK-70: (으)ㄹ걸 (그랬다), 았/었어야 했다 — afsus va pushaymonlik</h2>

<p>Imtihon tugadi. Yaxshi topshirmadingiz. Uyga qaytayotib nima
oʻylaysiz? “<b>Koʻproq oʻqisam boʻlardi</b>” yoki “<b>Koʻproq
oʻqishim kerak edi</b>”. Ish oʻtib ketgan, oʻzgartirib boʻlmaydi —
lekin odam baribir shuni aytadi. Koreys tilida buning uchun ikkita
qolip bor, va ular bir-biridan ohang bilan farq qiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ걸 그랬다</b> bilan “…sam boʻlardi” deysiz</li>
    <li>Inkor shakli <b>지 말걸 그랬다</b> ni oʻrganasiz</li>
    <li><b>았/었어야 했다</b> bilan “…shim kerak edi” deysiz</li>
    <li>Ikkalasining ohangdagi farqini bilib olasiz</li>
    <li>Qisqargan ogʻzaki shakl <b>…(으)ㄹ걸</b> ni koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qolip</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ걸 그랬다</span>
  <span class="pe-chip pe-chip--neg">았/었어야 했다</span>
  <span class="pe-chip pe-chip--adv">= …sam boʻlardi / …shim kerak edi</span>
</div>

<h3>1. (으)ㄹ걸 그랬다 — “…sam boʻlardi”</h3>

<p><b>걸</b> — bu <b>것을</b> ning qisqargani. Yaʼni yana oʻsha
mashina: 갈 <b>것을</b> 그랬다 → 갈<b>걸</b> 그랬어요. 그랬다 esa
“shunday qilgan edim” degani.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄹ걸 그랬다</span></p>
    <p>자다 → 잘걸 그랬어요</p>
    <p>가다 → 갈걸 그랬어요</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">을걸 그랬다</span></p>
    <p>먹다 → 먹을걸 그랬어요</p>
    <p>읽다 → 읽을걸 그랬어요</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 일찍 <span class="pe-hl pe-hl--v">잘걸
     그랬어요</span>.</p>
  <p class="pe-ex__uz">Kecha erta uxlasam boʻlardi.</p>
  <p class="pe-ex__why">Demak erta uxlamadim — va hozir afsusdaman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">더 열심히 <span class="pe-hl pe-hl--v">공부할걸
     그랬어요</span>.</p>
  <p class="pe-ex__uz">Koʻproq tirishib oʻqisam boʻlardi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu — “…sam boʻlardi”.</b> “Erta chiq<b>sam
  boʻlardi</b>.” “Aytmasam boʻlardi.” Bu shakl bizda ham
  <em>faqat oʻzimiz haqimizda</em> ishlatiladi va <em>ichki afsus</em>
  bildiradi — hech kim sizni ayblamayapti, siz oʻzingizni
  aytyapsiz. Koreyschadagi <b>(으)ㄹ걸 그랬다</b> ning ohangi ham
  xuddi shunday.</p>
</div>

<h3>2. Inkori: 지 말걸 그랬다</h3>

<p>“Qilmasam boʻlardi” degani — yaʼni qilib qoʻydingiz va afsusdasiz:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그 말을 <span class="pe-hl pe-hl--neg">하지 말걸
     그랬어요</span>.</p>
  <p class="pe-ex__uz">U gapni aytmasam boʻlardi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 커피를 <span class="pe-hl pe-hl--neg">마시지
     말걸 그랬어요</span>. 잠이 안 왔어요.</p>
  <p class="pe-ex__uz">Kecha kofe ichmasam boʻlardi. Uyqum
  kelmadi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>말걸</b>, <s>마걸</s> emas — 말다 ning oʻzagi <b>말</b>.
  Bu PK-61 dagi 말라고 bilan bir xil mantiq.</p>
</div>

<h3>3. Qisqargan ogʻzaki shakl</h3>

<p>Kundalik nutqda <b>그랬어요</b> tushib qoladi va faqat
<b>(으)ㄹ걸</b> qoladi. Ohangi pasayadi — bu oʻz-oʻziga aytilgan
gap:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">아… 일찍 <span class="pe-hl pe-hl--v">올걸</span>.</p>
  <p class="pe-ex__uz">Eh… erta kelsam boʻlardi.</p>
</div>

<h3>4. 았/었어야 했다 — “…shim kerak edi”</h3>

<p>Bu qolip PK-50 dagi <b>아/어야 하다</b> (majburiyat) ning oʻtgan
zamoni. Yaʼni: majburiyat bor edi, lekin bajarilmadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">일찍 <span class="pe-hl pe-hl--v">왔어야
     했어요</span>.</p>
  <p class="pe-ex__uz">Erta kelishim kerak edi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">우산을 <span class="pe-hl pe-hl--v">가져왔어야
     했어요</span>.</p>
  <p class="pe-ex__uz">Soyabon olib kelishim kerak edi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그때 <span class="pe-hl pe-hl--v">사과했어야
     했어요</span>.</p>
  <p class="pe-ex__uz">Oʻshanda kechirim soʻrashim kerak edi.</p>
</div>

<h3>5. Ikkalasining farqi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)ㄹ걸 그랬다</p>
    <p><b>Shaxsiy, hissiy afsus.</b> Ogʻzaki nutq.</p>
    <p>Faqat <b>oʻzim</b> haqimda.</p>
    <p><small>일찍 잘걸 그랬어요. — Erta uxlasam boʻlardi.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">았/었어야 했다</p>
    <p><b>Obyektiv majburiyat</b> bajarilmagan. Kuchliroq, rasmiyroq.</p>
    <p>Boshqa odam haqida ham aytiladi.</p>
    <p><small>일찍 왔어야 했어요. — Erta kelishi kerak edi.</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p>Shuning uchun boshqa odamni <em>tanqid qilish</em> uchun
  <b>았/었어야 했다</b> ishlatiladi: 자스루르 씨가 미리
  <b>말했어야 했어요</b> (“Jasur oldindan aytishi kerak edi”).
  <s>말할걸 그랬어요</s> deb boshqa odam haqida aytib boʻlmaydi —
  u faqat oʻzingizga.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>어제 일찍 잤을걸 그랬어요.</s></p>
  <p class="pe-good">어제 일찍 <b>잘걸</b> 그랬어요.</p>
  <p><small>걸 dan oldin zamon qoʻshimchasi qoʻyilmaydi — faqat
  <b>(으)ㄹ</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그 말을 하지 마걸 그랬어요.</s></p>
  <p class="pe-good">그 말을 하지 <b>말걸</b> 그랬어요.</p>
  <p><small>말다 ning oʻzagi <b>말</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>자스루르 씨가 미리 말할걸 그랬어요.</s></p>
  <p class="pe-good">자스루르 씨가 미리 <b>말했어야 했어요</b>.</p>
  <p><small>(으)ㄹ걸 그랬다 faqat <b>oʻzingiz</b> haqingizda.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>일찍 와야 했어요.</s>
    <small>(“erta kelishim kerak edi, lekin kelmadim” maʼnosida)</small></p>
  <p class="pe-good">일찍 <b>왔어야</b> 했어요.</p>
  <p><small>Bajarilmagan majburiyat uchun <b>았/었</b> kerak.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 어제 일찍
  <span class="pe-blank"></span> 그랬어요. (자다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>잘걸</b> — 자 da 받침 yoʻq → ㄹ걸.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 더 열심히
  <span class="pe-blank"></span> 그랬어요. (공부하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>공부할걸</b> — 하 da 받침 yoʻq → ㄹ걸.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> “U gapni aytmasam boʻlardi” —
  koreyschada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>그 말을 하지 말걸 그랬어요.</b> Inkori — 지 말걸.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Ikkalasining farqi nimada?
  일찍 잘걸 그랬어요 / 일찍 잤어야 했어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Birinchisi — <b>shaxsiy, hissiy afsus</b> (“eh, uxlasam
    boʻlardi”). Ikkinchisi — <b>obyektiv majburiyat</b> bajarilmagan
    (“uxlashim kerak edi”), kuchliroq va boshqa odam haqida ham
    aytiladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>어제 일찍 잤을걸 그랬어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>일찍 잘걸 그랬어요.</b> 걸 dan oldin faqat
    (으)ㄹ, zamon qoʻshimchasi emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Doʻstingizni tanqid qilmoqchisiz:
  “oldindan aytishi kerak edi”. Qaysi qolip?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>미리 말했어야 했어요.</b> Boshqa odam haqida faqat
    <b>았/었어야 했다</b> ishlatiladi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ걸 그랬다</b> — …sam boʻlardi</li>
  <li><b>지 말걸 그랬다</b> — …masam boʻlardi</li>
  <li><b>았/었어야 했다</b> — …shim kerak edi</li>
  <li><b>후회하다</b> — pushaymon boʻlmoq</li>
  <li><b>사과하다</b> — kechirim soʻramoq</li>
  <li><b>미리</b> — oldindan</li>
  <li><b>후배</b> — kichik kursdosh · <b>선배</b> — katta kursdosh</li>
  <li><b>졸업하다</b> — bitirmoq</li>
  <li><b>조언</b> — maslahat</li>
  <li><b>기회</b> — imkoniyat</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ걸 그랬다</b> = “…sam boʻlardi” — shaxsiy, hissiy
      afsus, faqat <b>oʻzim</b> haqimda.</li>
    <li>받침 yoʻq → <b>ㄹ걸</b> · 받침 bor → <b>을걸</b>.
      걸 dan oldin <b>zamon yoʻq</b>.</li>
    <li>Inkori: <b>지 말걸 그랬다</b> (마걸 emas).</li>
    <li>Ogʻzaki nutqda 그랬어요 tushadi: <b>일찍 올걸…</b></li>
    <li><b>았/었어야 했다</b> = “…shim kerak edi” — bajarilmagan
      majburiyat, kuchliroq, <b>boshqa odam haqida ham</b>.</li>
    <li><b>걸</b> ← 것을 — yana oʻsha 것 oilasi.</li>
    <li>Oʻzbekcha juftliklari: “…<b>sam boʻlardi</b>” va
      “…<b>shim kerak edi</b>”.</li>
  </ul>
</div>
""",
    },
]
