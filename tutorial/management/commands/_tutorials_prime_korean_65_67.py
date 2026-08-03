# -*- coding: utf-8 -*-
"""Prime Korean — Block E oxiri, darslar 65–67.

65. (으)ㄹ수록 — "…gan sari"
66. (으)ㄴ/는 반면에 — qarama-qarshi tomon
67. (으)ㄹ 뿐만 아니라 — "faqat emas, balki"

Uchalasi ham bogʻlovchi qoliplar, va uchalasining ham oʻzbekcha aynan
juftligi bor — bu batchning kuchli tomoni shu:
  (으)ㄹ수록      = "…gan SARI"        (oʻqigan sari qiziq boʻladi)
  (으)ㄴ/는 반면에 = "…, … ESA …"       (grammatikasi oson, talaffuzi esa qiyin)
  (으)ㄹ 뿐만 아니라 = "FAQAT … EMAS, BALKI … HAM"

67 dagi 뿐 — yana bitta aniqlovchi + ot: 것 · 줄 · 뻔 · 테 · 뿐.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_65_67.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_65_67.py --author=prime
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
        "title": "PK-65: (으)ㄹ수록 — “…gan sari”",
        "category": "korean",
        "order": 65,
        "summary": (
            "“Oʻrgangan sari qiziq boʻladi” — bir narsa ortgan sari ikkinchisi "
            "ham ortadi. Koreyschada 배울수록 재미있어요."
        ),
        "stories": ["산을 오르는 나무꾼"],
        "content": """
<h2>PK-65: (으)ㄹ수록 — “…gan sari”</h2>

<p>Koreys tilini boshlaganingizda Hangul chalkash koʻringan edi. Bir
hafta oʻqidingiz — biroz osonlashdi. Bir oy oʻqidingiz — yana
osonlashdi. Yaʼni <em>bir narsa ortgan sari</em> ikkinchisi <em>ham
oʻzgaryapti</em>. Oʻzbekchada buni bitta soʻz bilan aytamiz:
“oʻqi<b>gan sari</b> oson boʻlyapti”. Koreys tilida esa —
<b>(으)ㄹ수록</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ수록</b> bilan “…gan sari” deysiz</li>
    <li>Uning kuchli shakli <b>(으)면 …(으)ㄹ수록</b> ni oʻrganasiz</li>
    <li>Nega u <b>아/어지다</b> bilan juftlik boʻlishini koʻrasiz</li>
    <li><b>갈수록</b> degan tayyor ravishni bilib olasiz</li>
    <li>Qaysi gaplarda bu qolip <b>ishlamasligini</b> tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Oʻzak</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ수록</span>
  <span class="pe-chip pe-chip--adv">= …gan sari</span>
</div>

<h3>1. Yasalishi — tanish 받침 ayrisi</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄹ수록</span></p>
    <p>배우다 → 배울수록</p>
    <p>가다 → 갈수록</p>
    <p>보다 → 볼수록</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">을수록</span></p>
    <p>먹다 → 먹을수록</p>
    <p>많다 → 많을수록</p>
    <p>좋다 → 좋을수록</p>
  </div>
</div>

<p>Feʼl bilan ham, sifat bilan ham ishlaydi — bu qolipda ular
ajratilmaydi. <b>ㄹ</b> oʻzak bitta ㄹ boʻlib qoladi: 만들다 →
<b>만들수록</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어는 <span class="pe-hl pe-hl--v">배울수록</span>
     재미있어요.</p>
  <p class="pe-ex__uz">Koreys tili oʻrgangan sari qiziq boʻladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">사람이 <span class="pe-hl pe-hl--adv">많을수록</span>
     좋아요.</p>
  <p class="pe-ex__uz">Odam koʻp boʻlgan sari yaxshi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu dars siz uchun deyarli bepul.</b> Oʻzbek tilida aynan shu
  maʼno uchun tayyor qurilma bor: <b>“…gan sari”</b> va <b>“…gani
  sayin”</b>. “Kitob oʻqi<b>gan sari</b> aqlli boʻladi.” “Kun
  oʻt<b>gani sayin</b> sovuq boʻlyapti.” Ingliz tilida esa butun gap
  qayta quriladi (“the more… the more…”) — ikkita “the” bilan, gʻalati
  tartibda. Sizga bu kerak emas: fikr allaqachon oʻzbekcha bosh
  miyangizda tayyor, faqat <b>(으)ㄹ수록</b> qoʻshimchasini
  yodlang.</p>
</div>

<h3>2. Kuchli shakli: (으)면 + (으)ㄹ수록</h3>

<p>Koreyslar koʻpincha feʼlni <b>ikki marta</b> aytadi: avval
<b>(으)면</b> (PK-36) bilan, keyin <b>(으)ㄹ수록</b> bilan. Bu maʼnoni
kuchaytiradi — “qilaversang, qilaversang…”:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>(으)면</th><th>(으)ㄹ수록</th><th>Natija</th></tr>
  <tr><td>하다</td><td class="pk-stem">하면</td><td class="pk-end">할수록</td>
      <td class="pk-res">하면 할수록</td></tr>
  <tr><td>보다</td><td class="pk-stem">보면</td><td class="pk-end">볼수록</td>
      <td class="pk-res">보면 볼수록</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹으면</td><td class="pk-end">먹을수록</td>
      <td class="pk-res">먹으면 먹을수록</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 노래는 <span class="pe-hl pe-hl--v">들으면
     들을수록</span> 좋아요.</p>
  <p class="pe-ex__uz">Bu qoʻshiq eshitgan sari yoqadi.</p>
  <p class="pe-ex__why">듣다 — ㄷ notoʻgʻri feʼli (PK-32): 들으면,
  들을수록.</p>
</div>

<div class="pe-call pe-tip">
  <p>Ikkilangan shakl <b>majburiy emas</b> — 배울수록 ham toʻgʻri,
  배우면 배울수록 ham toʻgʻri. Ikkinchisi kuchliroq va ogʻzaki nutqda
  koʻproq eshitiladi.</p>
</div>

<h3>3. Nega 아/어지다 bilan juftlik</h3>

<p>Bu qolip <b>oʻzgarish</b> haqida. Shuning uchun keyingi gapda
koʻpincha PK-56 dagi <b>아/어지다</b> (“…lashib bormoq”) turadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">시간이 <span class="pe-hl pe-hl--v">지날수록</span>
     실력이 <span class="pe-hl pe-hl--v">좋아져요</span>.</p>
  <p class="pe-ex__uz">Vaqt oʻtgan sari malaka yaxshilanib boradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어는 <span class="pe-hl pe-hl--v">공부할수록</span>
     <span class="pe-hl pe-hl--v">쉬워져요</span>.</p>
  <p class="pe-ex__uz">Koreys tili oʻqigan sari osonlashib boradi.</p>
</div>

<h3>4. 갈수록 — tayyor ravish</h3>

<p><b>갈수록</b> soʻzma-soʻz “borgan sari”, lekin u alohida soʻzga
aylanib ketgan: <em>“tobora, kundan-kunga”</em>. Uni feʼlsiz ham
ishlatish mumkin:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">갈수록</span> 날씨가
     추워져요.</p>
  <p class="pe-ex__uz">Kundan-kunga havo sovib boryapti.</p>
</div>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">보면 볼수록</p>
    <p>koʻrgan sari</p></div>
  <div class="pe-card"><p class="pe-card__h">알면 알수록</p>
    <p>bilgan sari</p></div>
  <div class="pe-card"><p class="pe-card__h">시간이 지날수록</p>
    <p>vaqt oʻtgan sari</p></div>
  <div class="pe-card"><p class="pe-card__h">갈수록</p>
    <p>tobora, kundan-kunga</p></div>
</div>

<h3>5. Qachon bu qolip ishlamaydi</h3>

<div class="pe-call pe-warn">
  <p>(으)ㄹ수록 — <b>asta-sekin oʻzgarish</b> haqida. Bir marta boʻlib
  oʻtgan hodisa uchun ishlatilmaydi:<br>
  <s>어제 학교에 갈수록 친구를 만났어요</s> ✗<br>
  “Kecha maktabga bordim” — bu bir martalik hodisa, unga PK-35 dagi
  <b>아/어서</b> kerak.</p>
</div>

<p>Yana bitta muhim narsa: <b>수록 dan oldin zamon qoʻshimchasi
qoʻyilmaydi</b>. Gap qaysi zamonda ekanini <em>oxirgi</em> feʼl
aytadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어는 배울수록 재미<span class="pe-hl pe-hl--v">있었어요</span>.</p>
  <p class="pe-ex__uz">Koreys tili oʻrgangan sari qiziq boʻlgan edi.</p>
  <p class="pe-ex__why">Zamon oxirida — 배웠을수록 emas.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>한국어는 배우을수록 재미있어요.</s></p>
  <p class="pe-good">한국어는 <b>배울수록</b> 재미있어요.</p>
  <p><small>배우 da 받침 yoʻq → <b>ㄹ수록</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>사람이 많를수록 좋아요.</s></p>
  <p class="pe-good">사람이 <b>많을수록</b> 좋아요.</p>
  <p><small>많 da 받침 bor → <b>을수록</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>시간이 지났을수록 실력이 좋아졌어요.</s></p>
  <p class="pe-good">시간이 <b>지날수록</b> 실력이 좋아졌어요.</p>
  <p><small>수록 dan oldin zamon qoʻshimchasi qoʻyilmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>어제 학교에 갈수록 친구를 만났어요.</s></p>
  <p class="pe-good">어제 학교에 <b>가서</b> 친구를 만났어요.</p>
  <p><small>Bir martalik hodisa uchun (으)ㄹ수록 ishlatilmaydi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 한국어는
  <span class="pe-blank"></span> 재미있어요. (배우다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>배울수록</b> — 배우 da 받침 yoʻq → ㄹ수록.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 사람이
  <span class="pe-blank"></span> 좋아요. (많다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>많을수록</b> — 많 da 받침 bor → 을수록.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Ikkilangan shaklga aylantiring:
  이 노래는 들을수록 좋아요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>이 노래는 들으면 들을수록 좋아요.</b> (으)면 + (으)ㄹ수록 —
    maʼnoni kuchaytiradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> <b>갈수록</b> nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>“Tobora, kundan-kunga.”</b> Soʻzma-soʻz “borgan sari”, lekin
    alohida ravishga aylangan: 갈수록 추워져요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>시간이 지났을수록 실력이 좋아졌어요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>시간이 지날수록 실력이 좋아졌어요.</b> Zamon
    faqat oxirgi feʼlda boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Nega
  <s>어제 학교에 갈수록 친구를 만났어요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>(으)ㄹ수록 — <b>asta-sekin oʻzgarish</b> haqida. “Kecha
    maktabga borish” bir martalik hodisa, unga <b>가서</b> kerak.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ수록</b> — …gan sari</li>
  <li><b>(으)면 …(으)ㄹ수록</b> — kuchaytirilgan shakli</li>
  <li><b>갈수록</b> — tobora, kundan-kunga</li>
  <li><b>지나다</b> — oʻtmoq (vaqt)</li>
  <li><b>실력</b> — malaka, bilim darajasi</li>
  <li><b>노래</b> — qoʻshiq</li>
  <li><b>깊다</b> — chuqur</li>
  <li><b>어두워지다</b> — qorongʻilashmoq</li>
  <li><b>나무꾼</b> — oʻtinchi</li>
  <li><b>욕심</b> — ochkoʻzlik, tama</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ수록</b> = “…gan sari” — bir narsa ortgan sari
      ikkinchisi oʻzgaradi.</li>
    <li>받침 yoʻq → <b>ㄹ수록</b> · 받침 bor → <b>을수록</b>.
      Feʼl ham, sifat ham.</li>
    <li>Kuchli shakli: <b>(으)면 + (으)ㄹ수록</b> (하면 할수록).</li>
    <li>Koʻpincha <b>아/어지다</b> bilan juftlik: 배울수록
      쉬워져요.</li>
    <li><b>갈수록</b> — alohida ravish: “tobora”.</li>
    <li>수록 dan oldin <b>zamon qoʻshimchasi yoʻq</b> — zamon
      oxirgi feʼlda.</li>
    <li>Bir martalik hodisa uchun <b>ishlatilmaydi</b>.</li>
    <li>Oʻzbekcha juftligi: “oʻqi<b>gan sari</b>”, “oʻt<b>gani
      sayin</b>”.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-66: (으)ㄴ/는 반면에 — qarama-qarshi tomon",
        "category": "korean",
        "order": 66,
        "summary": (
            "“Grammatikasi oson, talaffuzi esa qiyin” — oʻzbekchadagi “esa” "
            "ning koreyscha juftligi. Bir narsaning ikki tomonini qiyoslash."
        ),
        "stories": ["딜노자의 블로그: 서울과 타슈켄트"],
        "content": """
<h2>PK-66: (으)ㄴ/는 반면에 — qarama-qarshi tomon</h2>

<p>Doʻstingiz soʻradi: “Koreys tili qiyinmi?”. Javob bitta soʻz emas.
“Grammatikasi oson, <b>talaffuzi esa</b> qiyin” deysiz — chunki bitta
narsaning <em>ikki tomoni</em> bor. PK-34 dagi <b>지만</b> shunchaki
“lekin” degani edi. Bugungi qolip esa ikki tomonni <em>tarozining
ikki pallasiga</em> qoʻyadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄴ/는 반면에</b> bilan ikki tomonni qiyoslaysiz</li>
    <li>Feʼl, sifat va ot uchun uchta shaklni ajratasiz</li>
    <li>Uni <b>지만</b> dan farqlaysiz</li>
    <li>Qisqargan <b>반면</b> shaklini koʻrasiz</li>
    <li>TOPIK yozma ishida qanday ishlatishni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Aniqlovchi shakl</span>
  <span class="pe-chip pe-chip--v">반면에</span>
  <span class="pe-chip pe-chip--adv">= …, … esa …</span>
</div>

<h3>1. Oʻzbekchadagi “esa”</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어는 문법이 <span class="pe-hl pe-hl--v">쉬운
     반면에</span> 발음이 어려워요.</p>
  <p class="pe-ex__uz">Koreys tilining grammatikasi oson, talaffuzi
  <b>esa</b> qiyin.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu ish uchun alohida yuklama bor: “esa”.</b>
  “Akam tinch, ukam <b>esa</b> shoʻx.” “Yozi issiq, qishi <b>esa</b>
  sovuq.” Diqqat qiling — bu “lekin” emas. “Lekin” <em>kutilmagan</em>
  narsani qoʻshadi, “esa” esa <em>ikkinchi tomonni</em> qoʻyadi.
  <b>반면에</b> ham xuddi shunday ishlaydi: u qarshi turmaydi,
  <em>muvozanat</em> qiladi. Shuning uchun 반면에 gaplari deyarli
  har doim <b>bitta mavzuning ikki tomoni</b> haqida boʻladi.</p>
</div>

<h3>2. Uchta shakl</h3>

<p>반면에 dan oldin <b>aniqlovchi shakli</b> turadi (PK-43…45).
Shuning uchun feʼl, sifat va ot uchta boshqa yoʻl tutadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima</th><th>Shakl</th><th>Misol</th><th>Natija</th></tr>
  <tr><td><b>Feʼl</b> (hozirgi)</td><td class="pk-end">는 반면에</td>
      <td class="pk-stem">좋아하다</td><td class="pk-res">좋아하는 반면에</td></tr>
  <tr><td><b>Sifat</b>, 받침 yoʻq</td><td class="pk-end">ㄴ 반면에</td>
      <td class="pk-stem">비싸다</td><td class="pk-res">비싼 반면에</td></tr>
  <tr><td><b>Sifat</b>, 받침 bor</td><td class="pk-end">은 반면에</td>
      <td class="pk-stem">좋다</td><td class="pk-res">좋은 반면에</td></tr>
  <tr><td><b>Ot</b> (이다)</td><td class="pk-end">인 반면에</td>
      <td class="pk-stem">학생이다</td><td class="pk-res">학생인 반면에</td></tr>
  <tr><td><b>Oʻtgan zamon</b></td><td class="pk-end">(으)ㄴ 반면에</td>
      <td class="pk-stem">갔다</td><td class="pk-res">간 반면에</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Eng koʻp adashiladigan joy — feʼl va sifat.</b> Feʼl
  <b>는</b> oladi, sifat esa <b>(으)ㄴ</b>. Bu PK-43 va PK-45 dagi
  qoidaning oʻzi:<br>
  좋아하다 (feʼl) → 좋아하<b>는</b> 반면에<br>
  좋다 (sifat) → 좋<b>은</b> 반면에</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 운동을 <span class="pe-hl pe-hl--v">좋아하는
     반면에</span> 동생은 책을 좋아해요.</p>
  <p class="pe-ex__uz">Men sportni yaxshi koʻraman, ukam esa kitobni.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">서울은 <span class="pe-hl pe-hl--adv">편리한
     반면에</span> 집값이 비싸요.</p>
  <p class="pe-ex__uz">Seul qulay, uy narxi esa qimmat.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">하나 씨는 <span class="pe-hl pe-hl--s">학생인
     반면에</span> 언니는 가수예요.</p>
  <p class="pe-ex__uz">Hana talaba, opasi esa qoʻshiqchi.</p>
  <p class="pe-ex__why">Ot + 이다 → <b>인 반면에</b>.</p>
</div>

<h3>3. 지만 (PK-34) bilan farqi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">지만</p>
    <p><b>Oddiy qarama-qarshilik</b> — “lekin”. Ikki gap bogʻliq
    boʻlmasa ham boʻladi.</p>
    <p><small>비가 오지만 학교에 가요. — Yomgʻir yogʻyapti, lekin
    maktabga boraman.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)ㄴ/는 반면에</p>
    <p><b>Ikki tomonni qiyoslash</b> — “esa”. Bitta mavzuning ikki
    yuzi.</p>
    <p><small>이 카페는 커피가 맛있는 반면에 자리가 좁아요.</small></p>
  </div>
</div>

<div class="pe-call pe-warn">
  <p>Yuqoridagi yomgʻir gapini 반면에 bilan aytib boʻlmaydi:
  <s>비가 오는 반면에 학교에 가요</s> ✗ — “yomgʻir” va “maktabga
  borish” bitta narsaning ikki tomoni emas. 반면에 uchun ikkala gap
  ham <b>bir xil mavzu</b> haqida boʻlishi kerak.</p>
</div>

<h3>4. 반면 — qisqargan va rasmiyroq</h3>

<p>Yozma matnda va TOPIK 쓰기 da <b>에</b> koʻpincha tushiriladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">도시는 편리한 <span class="pe-hl pe-hl--v">반면</span>
     공기가 나빠요.</p>
  <p class="pe-ex__uz">Shahar qulay, havosi esa yomon.</p>
</div>

<div class="pe-call pe-tip">
  <p>Bu qolip <b>TOPIK yozma ishida oltin</b>. Grafik yoki jadval
  tasvirlaganda (쓰기 53-savol) ikki tomonni koʻrsatish kerak boʻladi:
  “남자는 … 반면에 여자는 …”. Bitta jumlada butun taqqoslashni
  bera oladi.</p>
</div>

<h3>5. Ikki gapning egalari</h3>

<p>Odatda ikkala gapning <b>egasi boshqa</b> boʻladi, va ular
<b>은/는</b> bilan belgilanadi — chunki 은/는 (PK-12) aynan
qiyoslash uchun:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">형은</span> 조용한
     반면에 <span class="pe-hl pe-hl--s">동생은</span> 활발해요.</p>
  <p class="pe-ex__uz">Akam tinch, ukam esa shoʻx.</p>
  <p class="pe-ex__why">Ikkala tomonda ham 은 — bu tasodif emas.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>이 카페는 커피가 좋는 반면에 자리가 좁아요.</s></p>
  <p class="pe-good">커피가 <b>좋은</b> 반면에 자리가 좁아요.</p>
  <p><small>좋다 — sifat, shuning uchun <b>(으)ㄴ</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>저는 운동을 좋아한 반면에 동생은 책을 좋아해요.</s></p>
  <p class="pe-good">운동을 <b>좋아하는</b> 반면에…</p>
  <p><small>좋아하다 — feʼl, hozirgi zamonda <b>는</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>하나 씨는 학생이는 반면에…</s></p>
  <p class="pe-good">하나 씨는 <b>학생인</b> 반면에…</p>
  <p><small>Ot + 이다 → <b>인</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>비가 오는 반면에 학교에 가요.</s></p>
  <p class="pe-good">비가 <b>오지만</b> 학교에 가요.</p>
  <p><small>Bogʻliq boʻlmagan ikki gap uchun 반면에 emas,
  <b>지만</b>.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 서울은
  <span class="pe-blank"></span> 반면에 집값이 비싸요. (편리하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>편리한</b> — 편리하다 sifat, 받침 yoʻq → ㄴ 반면에.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 저는 운동을
  <span class="pe-blank"></span> 반면에 동생은 책을 좋아해요. (좋아하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>좋아하는</b> — 좋아하다 feʼl → <b>는</b> 반면에.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring: 하나 씨는
  <span class="pe-blank"></span> 반면에 언니는 가수예요. (학생이다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>학생인</b> — ot + 이다 → 인 반면에.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Qaysi biri toʻgʻri va nega?
  비가 오지만 학교에 가요 / 비가 오는 반면에 학교에 가요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>비가 오지만 학교에 가요.</b> 반면에 uchun ikkala gap bitta
    mavzuning ikki tomoni boʻlishi kerak — yomgʻir va maktabga
    borish esa boshqa-boshqa narsalar.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>커피가 좋는 반면에 자리가 좁아요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>커피가 좋은 반면에</b>. Sifat (으)ㄴ oladi,
    는 emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Akam tinch, ukam esa shoʻx” —
  koreyschada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>형은 조용한 반면에 동생은 활발해요.</b> Ikkala egada ham
    <b>은</b> — qiyoslash yuklamasi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄴ/는 반면에</b> — …, … esa …</li>
  <li><b>반면</b> — qisqargan, rasmiyroq shakli</li>
  <li><b>편리하다</b> — qulay</li>
  <li><b>집값</b> — uy narxi</li>
  <li><b>공기</b> — havo</li>
  <li><b>조용하다</b> — tinch, jim</li>
  <li><b>활발하다</b> — shoʻx, faol</li>
  <li><b>자리</b> — joy, oʻrindiq</li>
  <li><b>좁다</b> — tor · <b>넓다</b> — keng</li>
  <li><b>발음</b> — talaffuz · <b>문법</b> — grammatika</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄴ/는 반면에</b> = bitta mavzuning <b>ikki tomoni</b>.</li>
    <li>Feʼl → <b>는 반면에</b> · Sifat → <b>(으)ㄴ 반면에</b> ·
      Ot → <b>인 반면에</b>.</li>
    <li><b>지만</b> = oddiy “lekin”; <b>반면에</b> = “esa”,
      muvozanat.</li>
    <li>Ikkala gap ham <b>bir xil mavzu</b> haqida boʻlishi kerak.</li>
    <li>Egalar odatda <b>은/는</b> oladi — qiyoslash yuklamasi.</li>
    <li>Yozma matnda <b>반면</b> (에 tushadi) — TOPIK 쓰기 uchun
      juda foydali.</li>
    <li>Oʻzbekcha juftligi: “…, … <b>esa</b> …”.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-67: (으)ㄹ 뿐만 아니라 — “faqat emas, balki”",
        "category": "korean",
        "order": 67,
        "summary": (
            "“Faqat mazali emas, balki arzon ham” — bitta narsaga ikkinchi "
            "dalilni qoʻshish. Koreyschada 맛있을 뿐만 아니라 값도 싸요."
        ),
        "stories": ["누가 도와줬어요?"],
        "content": """
<h2>PK-67: (으)ㄹ 뿐만 아니라 — “faqat emas, balki”</h2>

<p>Yangi kafeni doʻstingizga maqtayapsiz. “Kofesi mazali” — yaxshi.
Lekin siz yana bir narsa qoʻshmoqchisiz: “<b>faqat</b> mazali
<b>emas</b>, narxi <b>ham</b> arzon”. Ikkinchi dalil birinchisini
kuchaytiradi. Oʻzbek tilida bu qurilma tayyor turibdi, va koreys
tilida ham bor: <b>(으)ㄹ 뿐만 아니라</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ 뿐만 아니라</b> bilan ikkinchi dalil qoʻshasiz</li>
    <li>Ot bilan qanday ishlashini koʻrasiz (뿐만 아니라, qoʻshimchasiz)</li>
    <li>Nega ikkinchi gapda <b>도</b> turishini bilib olasiz</li>
    <li>Uni jumla boshida bogʻlovchi sifatida ishlatasiz</li>
    <li>Yana bir <b>aniqlovchi + ot</b> mashinasini tanib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Oʻzak</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ 뿐만 아니라</span>
  <span class="pe-chip pe-chip--o">… 도</span>
  <span class="pe-chip pe-chip--adv">= faqat … emas, … ham</span>
</div>

<h3>1. 뿐 — “faqat” degan ot</h3>

<p><b>뿐</b> “faqat, xolos” degan ot. Yaʼni 맛있을 뿐 soʻzma-soʻz
“mazali boʻlish<em>gina</em>”. Unga <b>만</b> (faqat) va <b>아니라</b>
(emas) qoʻshilsa: “mazali boʻlishi<em>gina</em> emas…”.</p>

<div class="pe-call pe-rule">
  <p><b>Yana oʻsha mashina.</b> PK-52 da 것, PK-53 da 줄, PK-63 da 뻔,
  PK-64 da 테 — bugun <b>뿐</b>. Beshtasi ham <em>aniqlovchi +
  ot</em>. Shuning uchun oldida (으)ㄹ turadi va shuning uchun ularning
  hammasi bir xil his beradi. Yangi qolip koʻrsangiz, avval uni shu
  uchga ajrating: <b>aniqlovchi · ot · feʼl</b>.</p>
</div>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄹ 뿐만 아니라</span></p>
    <p>싸다 → 쌀 뿐만 아니라</p>
    <p>공부하다 → 공부할 뿐만 아니라</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">을 뿐만 아니라</span></p>
    <p>맛있다 → 맛있을 뿐만 아니라</p>
    <p>좋다 → 좋을 뿐만 아니라</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 식당은 음식이 <span class="pe-hl pe-hl--v">맛있을
     뿐만 아니라</span> 값<span class="pk-par">도</span> 싸요.</p>
  <p class="pe-ex__uz">U oshxonaning ovqati faqat mazali emas, narxi
  ham arzon.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha qurilma bir-bir mos tushadi:</b><br>
  <b>faqat</b> … <b>emas</b>, … <b>ham</b><br>
  <b>뿐만</b> … <b>아니라</b>, … <b>도</b><br>
  Uchta boʻlak, uchtasi ham oʻz oʻrnida. Hatto ohangi ham bir xil:
  birinchi dalil aytiladi, keyin “bu hammasi emas” degan pauza, keyin
  ikkinchi dalil. Shuning uchun bu qolipni oʻzbekchadan koreyschaga
  <em>soʻzma-soʻz</em> koʻchirsangiz ham toʻgʻri chiqadi — kam
  uchraydigan omad.</p>
</div>

<h3>2. Ot bilan: qoʻshimchasiz</h3>

<p>Ot bilan ishlatilsa, <b>을/를 yoki 이/가 qoʻyilmaydi</b> — 뿐만
아니라 toʻgʻridan-toʻgʻri otga yopishadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--o">한국어뿐만 아니라</span>
     한국 문화<span class="pk-par">도</span> 배워요.</p>
  <p class="pe-ex__uz">Faqat koreys tilini emas, koreys madaniyatini
  ham oʻrganamiz.</p>
  <p class="pe-ex__why">한국어<s>를</s> 뿐만 아니라 emas — qoʻshimcha
  tushadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">하나 씨는 <span class="pe-hl pe-hl--s">학생일 뿐만
     아니라</span> 유명한 가수예요.</p>
  <p class="pe-ex__uz">Hana faqat talaba emas, balki mashhur qoʻshiqchi.</p>
  <p class="pe-ex__why">이다 bilan — <b>일 뿐만 아니라</b>.</p>
</div>

<h3>3. Ikkinchi gapda 도 turadi</h3>

<p>Bu deyarli qoida. <b>도</b> (“ham”, PK-16) qoʻshilmasa, gap
tugallanmagandek eshitiladi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">값도 싸요</p>
    <p>narxi ham arzon</p></div>
  <div class="pe-card"><p class="pe-card__h">노래도 잘해요</p>
    <p>qoʻshiqni ham yaxshi aytadi</p></div>
  <div class="pe-card"><p class="pe-card__h">바람도 불어요</p>
    <p>shamol ham esyapti</p></div>
  <div class="pe-card"><p class="pe-card__h">친구도 많아요</p>
    <p>doʻstlari ham koʻp</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">어제는 비가 <span class="pe-hl pe-hl--v">올 뿐만
     아니라</span> 바람<span class="pk-par">도</span> 불었어요.</p>
  <p class="pe-ex__uz">Kecha faqat yomgʻir yogʻmadi, shamol ham esdi.</p>
  <p class="pe-ex__why">Zamon <b>oxirgi</b> feʼlda: 올 뿐만 아니라 …
  불었어요.</p>
</div>

<h3>4. Jumla boshida bogʻlovchi sifatida</h3>

<p><b>뿐만 아니라</b> ni yangi jumlaning boshida ham ishlatish
mumkin — u holda “bundan tashqari” degani:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그 카페는 커피가 맛있어요.
     <span class="pe-hl pe-hl--adv">뿐만 아니라</span> 자리도 넓어요.</p>
  <p class="pe-ex__uz">U kafening kofesi mazali. Bundan tashqari,
  joyi ham keng.</p>
</div>

<div class="pe-call pe-tip">
  <p>Bu shakl TOPIK 쓰기 ishida va rasmiy matnda juda foydali —
  ikkinchi dalilni qoʻshish uchun tayyor bogʻlovchi. Yozma ishda
  <b>또한</b> (“shuningdek”) bilan almashtirsa ham boʻladi.</p>
</div>

<h3>5. Ikkala dalil bir tomonga qarashi kerak</h3>

<div class="pe-call pe-warn">
  <p>Bu qolip ikkita <b>bir xil yoʻnalishdagi</b> dalilni qoʻshadi —
  ikkalasi ham ijobiy yoki ikkalasi ham salbiy:<br>
  <s>음식이 맛있을 뿐만 아니라 값이 비싸요</s> ✗ — biri maqtov, biri
  ayb.<br>
  Bunday holatda PK-66 dagi <b>반면에</b> kerak: 음식이 맛있는
  <b>반면에</b> 값이 비싸요.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>한국어를 뿐만 아니라 한국 문화도 배워요.</s></p>
  <p class="pe-good"><b>한국어뿐만</b> 아니라 한국 문화도 배워요.</p>
  <p><small>Ot bilan 을/를 tushadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음식이 맛있는 뿐만 아니라 값도 싸요.</s></p>
  <p class="pe-good">음식이 <b>맛있을</b> 뿐만 아니라 값도 싸요.</p>
  <p><small>뿐 dan oldin <b>(으)ㄹ</b> keladi, 는 emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>비가 왔을 뿐만 아니라 바람도 불었어요.</s>
    <small>(kundalik nutqda)</small></p>
  <p class="pe-good">비가 <b>올</b> 뿐만 아니라 바람도 불었어요.</p>
  <p><small>Zamonni oxirgi feʼl koʻtaradi — oldida (으)ㄹ
  yetadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>음식이 맛있을 뿐만 아니라 값이 비싸요.</s></p>
  <p class="pe-good">음식이 맛있는 <b>반면에</b> 값이 비싸요.</p>
  <p><small>Ikki dalil <b>qarama-qarshi</b> boʻlsa, 뿐만 아니라 emas,
  PK-66 dagi 반면에.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 그 식당은 음식이
  <span class="pe-blank"></span> 뿐만 아니라 값도 싸요. (맛있다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>맛있을</b> — 맛있 da 받침 bor → 을 뿐만 아니라.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring:
  <span class="pe-blank"></span> 뿐만 아니라 한국 문화도 배워요. (한국어)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>한국어</b> — ot bilan qoʻshimcha qoʻyilmaydi:
    한국어뿐만 아니라.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Ikkinchi gapda odatda qaysi
  qoʻshimcha turadi va nega?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>도</b> (“ham”). Chunki qolipning maʼnosi “faqat … emas,
    … <em>ham</em>” — oʻzbekchadagi “ham” ning oʻrni.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Nega
  <s>음식이 맛있을 뿐만 아니라 값이 비싸요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Ikkala dalil <b>bir tomonga</b> qarashi kerak. Bu yerda biri
    maqtov, biri ayb — demak <b>반면에</b> kerak:
    맛있는 반면에 값이 비싸요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>음식이 맛있는 뿐만 아니라 값도 싸요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>맛있을 뿐만 아니라</b>. 뿐 dan oldin
    <b>(으)ㄹ</b> turadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Beshta “aniqlovchi + ot”
  qolipini sanang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>것</b> (PK-52) · <b>줄</b> (PK-53) · <b>뻔</b> (PK-63) ·
    <b>테</b> (PK-64) · <b>뿐</b> (PK-67). Beshtasida ham oldida
    aniqlovchi shakli turadi.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 뿐만 아니라</b> — faqat … emas, … ham</li>
  <li><b>뿐</b> — faqat, xolos</li>
  <li><b>또한</b> — shuningdek, bundan tashqari</li>
  <li><b>값</b> — narx · <b>싸다</b> — arzon</li>
  <li><b>식당</b> — oshxona</li>
  <li><b>문화</b> — madaniyat</li>
  <li><b>가수</b> — qoʻshiqchi</li>
  <li><b>불다</b> — esmoq (shamol)</li>
  <li><b>넓다</b> — keng</li>
  <li><b>도와주다</b> — yordam bermoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ 뿐만 아니라</b> = “faqat … emas, … ham”.</li>
    <li>받침 yoʻq → <b>ㄹ 뿐만 아니라</b> · 받침 bor →
      <b>을 뿐만 아니라</b>.</li>
    <li>Ot bilan — <b>qoʻshimchasiz</b>: 한국어뿐만 아니라.</li>
    <li>이다 bilan — <b>일 뿐만 아니라</b>.</li>
    <li>Ikkinchi gapda deyarli har doim <b>도</b> turadi.</li>
    <li>Zamon <b>oxirgi feʼlda</b> — 뿐 dan oldin (으)ㄹ yetadi.</li>
    <li>Ikkala dalil <b>bir tomonga</b> qarashi kerak; qarama-qarshi
      boʻlsa — <b>반면에</b> (PK-66).</li>
    <li><b>뿐</b> — beshinchi aniqlovchi + ot: 것 · 줄 · 뻔 · 테 ·
      뿐.</li>
  </ul>
</div>
""",
    },
]
