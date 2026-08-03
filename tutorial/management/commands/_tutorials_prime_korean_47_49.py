# -*- coding: utf-8 -*-
"""Prime Korean — Block D, darslar 47–49.

47. Notoʻgʻri feʼllar 2: 르, ㅅ, ㅎ tuslanishi
48. (으)니까 — subyektiv sabab va kashfiyot
49. 기 때문에 / 명사 + 때문에 — obyektiv sabab

PK-35 (아/어서) uch marta “buni PK-48 da oʻrganasiz” deb vaʼda bergan —
PK-48 shu vaʼdani ochiq bajaradi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_47_49.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_47_49.py --author=prime
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
        "title": "PK-47: Notoʻgʻri feʼllar 2: 르, ㅅ, ㅎ tuslanishi",
        "category": "korean",
        "order": 47,
        "summary": (
            "몰라요, 지어요, 그래요 — qolgan uchta notoʻgʻri guruh. PK-32 dagi "
            "qoidaning oʻzi, faqat yangi aʼzolar bilan. 어떤 va 그런 ning siri ham "
            "shu yerda ochiladi."
        ),
        "stories": ["빨간 우산이 어디에 있어요?"],
        "content": """
<h2>PK-47: Notoʻgʻri feʼllar 2: 르, ㅅ, ㅎ tuslanishi</h2>

<p>PK-32 da siz uchta notoʻgʻri guruhni — <b>ㅂ, ㄷ, 으</b> — oʻrgandingiz va bitta
qoidani yod oldingiz: <em>oʻzgarish faqat unli bilan boshlanadigan qoʻshimcha
oldida sodir boʻladi</em>. Bugun qolgan uchta guruhni olamiz. Yaxshi xabar shuki,
qoida <b>oʻzgarmaydi</b> — faqat yangi aʼzolar qoʻshiladi. Va oxirida siz allaqachon
ishlatib yurgan ikkita soʻzning — <b>어떤</b> va <b>그런</b> ning — qayerdan
kelgani ochiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>르</b> guruhini oʻrganasiz — 모르다 → 몰라요</li>
    <li><b>ㅅ</b> guruhini — 짓다 → 지어요 — va uning “soxta” aʼzolarini</li>
    <li><b>ㅎ</b> guruhini — 그렇다 → 그래요, 빨갛다 → 빨간</li>
    <li>Notoʻgʻri feʼllarning butun tizimini bitta jadvalda koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Asosiy qoida</span>
  <span class="pe-chip pe-chip--s">Unli qoʻshimcha</span>
  <span class="pe-chip pe-chip--v">→ oʻzgaradi</span>
  <span class="pe-chip pe-chip--opt">·</span>
  <span class="pe-chip pe-chip--s">Undosh qoʻshimcha</span>
  <span class="pe-chip pe-chip--neg">→ oʻzgarmaydi</span>
</div>

<h3>1. 르 guruhi — ㄹ ikkilanadi</h3>

<p>Oʻzagi <b>르</b> bilan tugagan feʼllar 아/어 oldida oʻzgaradi: <b>으</b> tushadi
va oʻrniga bitta qoʻshimcha <b>ㄹ</b> paydo boʻladi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Maʼnosi</th><th>아/어요</th><th>Oʻtgan</th></tr>
  <tr><td>모르다</td><td class="pk-uz">bilmaslik</td>
      <td class="pk-res">몰라요</td><td class="pk-res">몰랐어요</td></tr>
  <tr><td>다르다</td><td class="pk-uz">boshqacha</td>
      <td class="pk-res">달라요</td><td class="pk-res">달랐어요</td></tr>
  <tr><td>빠르다</td><td class="pk-uz">tez</td>
      <td class="pk-res">빨라요</td><td class="pk-res">빨랐어요</td></tr>
  <tr><td>부르다</td><td class="pk-uz">chaqirmoq; kuylamoq</td>
      <td class="pk-res">불러요</td><td class="pk-res">불렀어요</td></tr>
  <tr><td>고르다</td><td class="pk-uz">tanlamoq</td>
      <td class="pk-res">골라요</td><td class="pk-res">골랐어요</td></tr>
  <tr><td>자르다</td><td class="pk-uz">kesmoq</td>
      <td class="pk-res">잘라요</td><td class="pk-res">잘랐어요</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>라 yoki 러?</b> Bu 르 dan <em>oldingi</em> unliga bogʻliq — PK-18 dagi
  아/어 tanlash qoidasining oʻzi. Oldingi unli <b>ㅏ</b> yoki <b>ㅗ</b> boʻlsa →
  <b>라</b>: 다<b>르</b>다 → 달<b>라</b>요, 모<b>르</b>다 → 몰<b>라</b>요.
  Boshqa har qanday unli boʻlsa → <b>러</b>: 부<b>르</b>다 → 불<b>러</b>요,
  기<b>르</b>다 → 길<b>러</b>요.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 그 사람을 <span class="pe-hl pe-hl--v">몰라요</span>.</p>
  <p class="pe-ex__uz">Men u odamni tanimayman.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>모르다 — alohida soʻz, inkor emas.</b> Oʻzbekchada “bilmayman” — bu
  “bilaman” ning inkori. Koreyschada esa <s>안 알아요</s> deyilmaydi: “bilmaslik”
  uchun butunlay boshqa feʼl bor — <b>모르다</b>. Yaʼni 알다 va 모르다 juftlik
  boʻlib yuradi, xuddi 있다/없다 kabi (PK-13). Bu — kundalik nutqda eng koʻp
  kerak boʻladigan juftliklardan biri, shuning uchun uni birinchi boʻlib yod oling.</p>
</div>

<p>Muhim: oʻzgarish <b>faqat 아/어</b> oldida. Boshqa qoʻshimchalar bilan oʻzak
tinch turadi:</p>

<ul>
  <li>모르<b>면</b> · 모르<b>고</b> · 모르<b>는</b> 사람 — oʻzgarish yoʻq</li>
  <li>몰<b>라</b>요 · 몰<b>랐</b>어요 · 몰<b>라</b>서 — oʻzgargan</li>
</ul>

<h3>2. ㅅ guruhi — ㅅ yoʻqoladi, 으 qoladi</h3>

<p>Bu guruhning oʻziga xosligi shunda: ㅅ 받침 tushib ketadi, lekin <b>으
qisqarmaydi</b> — ikki unli yonma-yon turaveradi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>Maʼnosi</th><th>아/어요</th><th>(으)면</th><th>(으)ㄴ</th></tr>
  <tr><td>짓다</td><td class="pk-uz">qurmoq</td>
      <td class="pk-res">지어요</td><td class="pk-res">지으면</td>
      <td class="pk-res">지은</td></tr>
  <tr><td>낫다</td><td class="pk-uz">tuzalmoq; yaxshiroq</td>
      <td class="pk-res">나아요</td><td class="pk-res">나으면</td>
      <td class="pk-res">나은</td></tr>
  <tr><td>붓다</td><td class="pk-uz">quymoq</td>
      <td class="pk-res">부어요</td><td class="pk-res">부으면</td>
      <td class="pk-res">부은</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Diqqat — hamma ㅅ notoʻgʻri emas!</b> Quyidagilar butunlay <b>toʻgʻri</b>
  feʼllar va ㅅ ni yoʻqotmaydi:<br>
  웃다 → <b>웃어요</b> (kulmoq) · 씻다 → <b>씻어요</b> (yuvmoq) ·
  벗다 → <b>벗어요</b> (yechmoq).<br>
  Yaʼni oʻzak ㅅ bilan tugagani hali hech nimani anglatmaydi — har bir soʻzni
  alohida bilish kerak. Yaxshiyamki notoʻgʻrilari kam.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아버지가 시골에 집을 <span class="pe-hl pe-hl--v">지어요</span>.</p>
  <p class="pe-ex__uz">Otam qishloqda uy qurmoqda.</p>
  <p class="pe-ex__why">짓 + 어요 → ㅅ tushdi, lekin unlilar qisqarmadi: 지어요.</p>
</div>

<h3>3. ㅎ guruhi — sifatlar va ranglar</h3>

<p>Bu guruh deyarli butunlay <b>sifatlar</b>dan iborat, va ular ikki xil
oʻzgaradi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Sifat</th><th>Maʼnosi</th><th>아/어요 <small>(ㅎ → ㅐ)</small></th>
      <th>(으)ㄴ <small>(ㅎ tushadi)</small></th></tr>
  <tr><td>그렇다</td><td class="pk-uz">shunday</td>
      <td class="pk-res">그래요</td><td class="pk-res">그런</td></tr>
  <tr><td>어떻다</td><td class="pk-uz">qanday</td>
      <td class="pk-res">어때요</td><td class="pk-res">어떤</td></tr>
  <tr><td>이렇다</td><td class="pk-uz">bunday</td>
      <td class="pk-res">이래요</td><td class="pk-res">이런</td></tr>
  <tr><td>빨갛다</td><td class="pk-uz">qizil</td>
      <td class="pk-res">빨개요</td><td class="pk-res">빨간</td></tr>
  <tr><td>파랗다</td><td class="pk-uz">koʻk</td>
      <td class="pk-res">파래요</td><td class="pk-res">파란</td></tr>
  <tr><td>하얗다</td><td class="pk-uz">oq</td>
      <td class="pk-res">하얘요</td><td class="pk-res">하얀</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Mana nihoyat javob.</b> PK-45 da siz <b>어떤</b> soʻzini ishlatdingiz, lekin
  u qayerdan kelgani aytilmagan edi. Endi koʻrinib turibdi: 어떤 = <b>어떻다 +
  (으)ㄴ</b>, yaʼni oddiy sifat aniqlovchisi. Xuddi shunday 그런 = 그렇다 + (으)ㄴ,
  이런 = 이렇다 + (으)ㄴ. Va suhbatda tez-tez eshitiladigan <b>그래요?</b> — bu
  그렇다 ning 아/어요 shakli.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>좋다 — bu guruhga kirmaydi!</b> U ㅎ bilan tugasa ham, butunlay toʻgʻri
  feʼl: 좋<b>아</b>요, 좋<b>은</b> 사람. Aynan shu sabab uni alohida eslab qolish
  kerak — bu eng koʻp ishlatiladigan sifat.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Ranglar koreyschada sifat, oʻzbekchada ham sifat — lekin shakli ikkita.</b>
  Oʻzbekchada “qizil” soʻzi hamma joyda bir xil: “qizil olma”, “olma qizil”.
  Koreyschada esa ikki xil shakl kerak: <b>빨간</b> 사과 (aniqlovchi) va
  사과가 <b>빨개요</b> (kesim). Shuning uchun har bir rangni <b>juft holda</b>
  yodlang — 빨간/빨개요, 파란/파래요, 하얀/하얘요. Bitta shaklni bilish yetmaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">하얀</span> 눈이 왔어요.
     밖이 정말 <span class="pe-hl pe-hl--v">하얘요</span>.</p>
  <p class="pe-ex__uz">Oq qor yogʻdi. Tashqarisi rostdan ham oppoq.</p>
  <p class="pe-ex__why">Bitta soʻz, ikki shakl: 하얀 (aniqlovchi) va 하얘요 (kesim).</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu darsda siz yangi soʻz emas, tanish soʻzning ichini oʻrganyapsiz.</b>
  <b>그래요</b>, <b>어떤</b>, <b>그런</b> — bularni siz allaqachon ishlatgansiz,
  faqat ular qayerdan kelganini bilmagansiz. Til oʻrganishning eng tez usuli
  aynan shu: yodlab olgan narsangizni keyin <em>ochib koʻrish</em>. Oʻzbek
  tilida ham biz “nimaga” soʻzini ishlatamiz, lekin uning ichida “nima + ga”
  turganini har doim ham oʻylab koʻrmaymiz. Koreyschada bunday “ochiladigan”
  soʻzlar juda koʻp, va har bittasi ochilganda yodlash yuki kamayadi.</p>
</div>

<h3>4. Butun tizim — bitta jadvalda</h3>

<p>Endi oltita guruhning hammasi sizda bor. Ularni birga koʻrish eng foydali:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Guruh</th><th>Misol</th><th>아/어요</th><th>(으)면</th><th>고</th></tr>
  <tr><td>ㅂ</td><td>덥다</td><td class="pk-res">더워요</td>
      <td class="pk-res">더우면</td><td class="pk-uz">덥고</td></tr>
  <tr><td>ㄷ</td><td>듣다</td><td class="pk-res">들어요</td>
      <td class="pk-res">들으면</td><td class="pk-uz">듣고</td></tr>
  <tr><td>으</td><td>바쁘다</td><td class="pk-res">바빠요</td>
      <td class="pk-uz">바쁘면</td><td class="pk-uz">바쁘고</td></tr>
  <tr><td>르</td><td>모르다</td><td class="pk-res">몰라요</td>
      <td class="pk-uz">모르면</td><td class="pk-uz">모르고</td></tr>
  <tr><td>ㅅ</td><td>짓다</td><td class="pk-res">지어요</td>
      <td class="pk-res">지으면</td><td class="pk-uz">짓고</td></tr>
  <tr><td>ㅎ</td><td>그렇다</td><td class="pk-res">그래요</td>
      <td class="pk-res">그러면</td><td class="pk-uz">그렇고</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Oxirgi ustunga qarang — <b>고</b> qoʻshimchasi bilan hech qaysi guruh
  oʻzgarmaydi. Chunki 고 undosh. Bu qoida PK-32 dan beri oʻzgarmadi va
  bundan keyin ham oʻzgarmaydi. <b>르</b> va <b>으</b> guruhlari esa hatto (으)면
  oldida ham tinch turadi — ular faqat 아/어 oldida oʻzgaradi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>저는 그 사람을 안 알아요.</s></p>
  <p class="pe-good">저는 그 사람을 <b>몰라요</b>.</p>
  <p><small>“Bilmaslik” uchun alohida feʼl bor — 모르다. 안 알다 deyilmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>노래를 부러요.</s></p>
  <p class="pe-good">노래를 <b>불러요</b>.</p>
  <p><small>르 guruhida ㄹ <b>ikkilanadi</b>: 부르 → 불러. Bitta ㄹ yetmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>손을 시어요.</s></p>
  <p class="pe-good">손을 <b>씻어요</b>.</p>
  <p><small>씻다 — toʻgʻri feʼl, ㅅ tushmaydi. Faqat 짓다, 낫다, 붓다 kabilar
  notoʻgʻri.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>사과가 빨갛아요.</s></p>
  <p class="pe-good">사과가 <b>빨개요</b>.</p>
  <p><small>ㅎ guruhida 아/어 oldida ㅎ tushadi va unli <b>ㅐ</b> ga
  aylanadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>날씨가 조아요.</s></p>
  <p class="pe-good">날씨가 <b>좋아요</b>.</p>
  <p><small>좋다 bu guruhga kirmaydi — u toʻliq toʻgʻri feʼl. (Talaffuzi
  [조아요], lekin yozilishi 좋아요.)</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 저는 그 노래를
  <span class="pe-blank"></span> (모르다).</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>몰라요</b> — 모르 dagi oldingi unli ㅗ, shuning uchun 라: 몰라요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 지영 씨가 노래를
  <span class="pe-blank"></span> (부르다).</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>불러요</b> — 부르 dagi oldingi unli ㅜ (ㅏ ham, ㅗ ham emas),
    shuning uchun 러: 불러요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Qaysi biri notoʻgʻri feʼl —
  씻다 yoki 짓다?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>짓다</b> notoʻgʻri: 지어요, 지으면. <b>씻다</b> esa toʻgʻri:
    씻어요, 씻으면. Oʻzak ㅅ bilan tugagani hali hech nimani anglatmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 어떤 soʻzi qanday yasalgan?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>어떻다 + (으)ㄴ = 어떤.</b> Yaʼni bu oddiy sifat aniqlovchisi, faqat
    ㅎ tushib ketgan. Xuddi shunday 그런, 이런, 저런.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Toʻldiring: 이 사과는
  <span class="pe-blank"></span> (빨갛다). Va: <span class="pe-blank"></span>
  (빨갛다) 사과를 샀어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>빨개요</b> (kesim) va <b>빨간</b> (aniqlovchi). Ranglarni doim juft
    holda yodlang.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Nega 모르고 va 모르면 da hech nima
  oʻzgarmaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>르 guruhi <b>faqat 아/어</b> oldida oʻzgaradi. 고 — undosh, (으)면 esa
    르 ni buzmaydi. Shuning uchun 모르고, 모르면, 모르는 — hammasi
    oʻzgarishsiz.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>모르다 → 몰라요</b> — bilmaslik, tanimaslik</li>
  <li><b>다르다 → 달라요</b> — boshqacha boʻlmoq</li>
  <li><b>빠르다 → 빨라요</b> — tez boʻlmoq</li>
  <li><b>부르다 → 불러요</b> — chaqirmoq; kuylamoq</li>
  <li><b>고르다 → 골라요</b> — tanlamoq</li>
  <li><b>짓다 → 지어요</b> — qurmoq</li>
  <li><b>낫다 → 나아요</b> — tuzalmoq; yaxshiroq boʻlmoq</li>
  <li><b>그렇다 → 그래요 / 그런</b> — shunday</li>
  <li><b>빨갛다 / 파랗다 / 하얗다</b> — qizil / koʻk / oq</li>
  <li><b>우산</b> — soyabon</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>르</b>: 아/어 oldida 으 tushadi va ㄹ ikkilanadi — 모르다 → 몰라요.
      라/러 tanlovi oldingi unliga bogʻliq.</li>
    <li><b>ㅅ</b>: ㅅ tushadi, lekin 으 qoladi — 짓다 → 지어요, 지으면.</li>
    <li>씻다, 웃다, 벗다 — <b>toʻgʻri</b> feʼllar, ㅅ ni yoʻqotmaydi.</li>
    <li><b>ㅎ</b>: 아/어 oldida ㅎ tushadi va unli ㅐ boʻladi — 빨갛다 → 빨개요.
      (으)ㄴ oldida esa faqat ㅎ tushadi — 빨간.</li>
    <li><b>좋다</b> ㅎ guruhiga kirmaydi — u toʻliq toʻgʻri.</li>
    <li><b>어떤</b> = 어떻다 + (으)ㄴ · <b>그런</b> = 그렇다 + (으)ㄴ.</li>
    <li>Butun tizimda qoida bitta: unli qoʻshimcha → oʻzgarish, undosh → yoʻq.</li>
    <li>르 va 으 guruhlari faqat <b>아/어</b> oldida oʻzgaradi, (으)면 oldida emas.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-48: (으)니까 — subyektiv sabab va kashfiyot",
        "category": "korean",
        "order": 48,
        "summary": (
            "PK-35 da vaʼda qilingan dars. Sabab koʻrsatib, keyin BUYRUQ bera "
            "oladigan qolip — va uning ikkinchi vazifasi: bir ish qilib, nimadir "
            "bilib olish."
        ),
        "stories": ["비가 오니까 우산을 가져가세요"],
        "content": """
<h2>PK-48: (으)니까 — subyektiv sabab va kashfiyot</h2>

<p>PK-35 da siz <b>아/어서</b> ni oʻrgandingiz va u yerda uch marta shunday
yozilgan edi: “<em>Bu maʼnoni berishning boshqa yoʻli bor va uni PK-48 da
oʻrganasiz.</em>” Mana shu dars keldi. Muammo esa quyidagicha edi:
“Yomgʻir yogʻyapti, <b>shuning uchun soyabon oling</b>” degan gapni 아/어서
koʻtara olmaydi — undan keyin buyruq kelmaydi. Kerakli qolip —
<b>(으)니까</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)니까</b> bilan sabab koʻrsatib, keyin buyruq bera olasiz</li>
    <li>Uning ikkinchi vazifasini — <em>kashfiyot</em>ni — oʻrganasiz</li>
    <li><b>아/어서</b> va <b>(으)니까</b> ni ishonch bilan ajratasiz</li>
    <li>Uzr soʻraganda qaysi birini ishlatish kerakligini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">Sabab</span>
  <span class="pe-chip pe-chip--v">(으)니까</span>
  <span class="pe-chip pe-chip--o">Natija / buyruq / taklif</span>
</div>

<h3>1. Yasalishi</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">니까</span></p>
    <p>가다 → 가니까 · 바쁘다 → 바쁘니까</p>
    <p>하다 → 하니까 · 오다 → 오니까</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">으니까</span></p>
    <p>먹다 → 먹으니까 · 있다 → 있으니까</p>
    <p>좋다 → 좋으니까 · 없다 → 없으니까</p>
  </div>
</div>

<p><b>ㄹ</b> oʻzaklar ㄴ oldida ㄹ ni yoʻqotadi — tanish qoida:
살다 → <b>사니까</b>, 만들다 → <b>만드니까</b>, 알다 → <b>아니까</b>.</p>

<p>Notoʻgʻri feʼllar ham ishlaydi, chunki (으) unli:
듣다 → <b>들으니까</b>, 덥다 → <b>더우니까</b>, 짓다 → <b>지으니까</b>.</p>

<h3>2. Asosiy vazifasi: sabab + buyruq</h3>

<p>Mana bu — butun darsning sababi. <b>(으)니까</b> dan keyin buyruq, taklif,
maslahat — hammasi mumkin:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">비가 <span class="pe-hl pe-hl--v">오니까</span> 우산을
     <span class="pe-hl pe-hl--adv">가져가세요</span>.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻyapti, shuning uchun soyabon olib keting.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시간이 <span class="pe-hl pe-hl--v">없으니까</span>
     <span class="pe-hl pe-hl--adv">빨리 가요</span>.</p>
  <p class="pe-ex__uz">Vaqt yoʻq, shuning uchun tez yuraylik.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">배가 <span class="pe-hl pe-hl--v">아프니까</span>
     병원에 <span class="pe-hl pe-hl--adv">가세요</span>.</p>
  <p class="pe-ex__uz">Qorningiz ogʻriyapti, shuning uchun shifoxonaga boring.</p>
  <p class="pe-ex__why">PK-35 da aynan shu gap <s>아파서 가세요</s> shaklida
  <b>notoʻgʻri</b> edi. Endi toʻgʻrisi qoʻlingizda.</p>
</div>

<h3>3. Zamon (으)니까 dan oldin qoʻyilishi MUMKIN</h3>

<p>Bu ham 아/어서 dan farq qiladi. (으)니까 oldida oʻtgan zamon bemalol turadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 비가 <span class="pe-hl pe-hl--v">왔으니까</span>
     오늘은 길이 안 좋아요.</p>
  <p class="pe-ex__uz">Kecha yomgʻir yoqqani uchun bugun yoʻl yaxshi emas.</p>
</div>

<div class="pe-call pe-tip">
  <p>Yodda tuting: <b>아/어서</b> — zamon yoʻq, buyruq yoʻq.
  <b>(으)니까</b> — zamon ham, buyruq ham bor. Ikkinchisi erkinroq.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tili bu yerda sizga yordam bermaydi — va buni bilish muhim.</b>
  “Vaqt yoʻq, <em>shuning uchun</em> tez yur” va “Kech qoldim, <em>shuning
  uchun</em> uzr” — oʻzbekchada ikkalasi ham bir xil bogʻlovchi bilan chiqadi.
  Koreyschada esa birinchisi <b>(으)니까</b>, ikkinchisi <b>아/어서</b> boʻlishi
  shart. Yaʼni ona tilingiz sizga qaysi birini tanlashni aytmaydi. Shuning
  uchun tarjimaga emas, bitta savolga tayaning: <em>keyingi qismda buyruq
  yoki taklif bormi?</em> Bor boʻlsa — (으)니까, yoʻq boʻlsa — 아/어서.</p>
</div>

<h3>4. Ikkinchi vazifasi: kashfiyot</h3>

<p><b>(으)니까</b> ning yana bir ishi bor, va u sababdan butunlay boshqa:
“bir ish qildim — <em>va shunda</em> nimadir bilib qoldim”. Bu maʼnoda
birinchi qism doim <b>harakat</b>, ikkinchisi esa <b>oʻtgan zamon</b>da boʻladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">창문을 <span class="pe-hl pe-hl--v">여니까</span>
     비가 왔어요.</p>
  <p class="pe-ex__uz">Derazani ochsam, yomgʻir yogʻayotgan ekan.</p>
  <p class="pe-ex__why">“Deraza ochgani uchun yomgʻir yogʻdi” <b>emas</b> —
  bu sabab emas, kashfiyot.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">집에 <span class="pe-hl pe-hl--v">가니까</span>
     아무도 없었어요.</p>
  <p class="pe-ex__uz">Uyga borsam, hech kim yoʻq ekan.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu maʼnoning aniq juftligi bor: “-sam … ekan”.</b>
  “Derazani och<em>sam</em>, yomgʻir yogʻayotgan <em>ekan</em>”. Diqqat qiling —
  oʻzbekchada ham bu <b>shart</b> emas; “-sam” bu yerda “agar” degani emas,
  balki “qilgan edim va koʻrdim” degani. Koreyschada ham xuddi shunday: (으)니까
  bu maʼnoda (으)면 (shart) bilan aralashmaydi. Tarjima qilayotganda oʻzingizga
  savol bering: <em>bu haqiqatan sodir boʻldimi?</em> Boʻlgan boʻlsa — kashfiyot,
  hali boʻlmagan boʻlsa — shart, yaʼni (으)면.</p>
</div>

<h3>5. 아/어서 va (으)니까 — toʻliq taqqoslash</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th></th><th>아/어서 (PK-35)</th><th>(으)니까</th></tr>
  <tr><td>Keyin buyruq</td><td class="pk-uz">✗ boʻlmaydi</td>
      <td class="pk-res">✓ boʻladi</td></tr>
  <tr><td>Oldin zamon</td><td class="pk-uz">✗ qoʻyilmaydi</td>
      <td class="pk-res">✓ qoʻyiladi</td></tr>
  <tr><td>Sababning turi</td><td class="pk-uz">obyektiv, umumiy</td>
      <td class="pk-res">subyektiv, soʻzlovchining fikri</td></tr>
  <tr><td>Uzr va rahmat</td><td class="pk-res">✓ faqat shu</td>
      <td class="pk-uz">✗ ishlatilmaydi</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Nega uzrda (으)니까 qoʻpol eshitiladi?</b> Chunki (으)니까 —
  <em>subyektiv</em> sabab, yaʼni “men shunday deb hisoblayman”. Uzr
  soʻrayotganda esa sababni oʻzingiz himoya qilmasligingiz kerak. Oʻzbekchada
  ham shu tuygʻu bor: “kech qol<em>ganim uchun</em> uzr” — bu oddiy uzr, ammo
  “kech qoldim-da, <em>chunki</em>…” deyish allaqachon bahonaga oʻxshaydi.
  Koreys tili shu farqni grammatikaga kiritgan, xolos.</p>
</div>

<h3>6. Uzr soʻraganda faqat 아/어서</h3>

<p>Bu — TOPIK da ham, hayotda ham koʻp uchraydigan nuqta. Rahmat aytganda va
uzr soʻraganda <b>doim 아/어서</b> ishlatiladi:</p>

<div class="pe-fix">
  <p class="pe-bad"><s>늦으니까 죄송합니다.</s></p>
  <p class="pe-good">늦<b>어서</b> 죄송합니다.</p>
  <p><small>“Kechikkanim uchun uzr”. (으)니까 bu yerda qoʻpol eshitiladi —
  goʻyo sababni <em>bahona</em> qilayotgandek.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>도와주니까 고맙습니다.</s></p>
  <p class="pe-good">도와<b>줘서</b> 고맙습니다.</p>
  <p><small>“Yordam berganingiz uchun rahmat”. Yana 아/어서.</small></p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>배가 아파서 병원에 가세요.</s></p>
  <p class="pe-good">배가 <b>아프니까</b> 병원에 가세요.</p>
  <p><small>Keyin buyruq bor → (으)니까 kerak.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>밥을 먹니까 배가 안 고파요.</s></p>
  <p class="pe-good">밥을 <b>먹으니까</b> 배가 안 고파요.</p>
  <p><small>먹 da 받침 bor → 으니까.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>서울에 살니까 자주 가요.</s></p>
  <p class="pe-good">서울에 <b>사니까</b> 자주 가요.</p>
  <p><small>ㄹ oʻzak ㄴ oldida ㄹ ni yoʻqotadi: 살 + 니까 → 사니까.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>늦어서 죄송하니까…</s></p>
  <p class="pe-good">늦<b>어서</b> 죄송합니다.</p>
  <p><small>Uzr va rahmatda faqat 아/어서.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 시간이
  <span class="pe-blank"></span> (없다) 빨리 가세요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>없으니까</b> — 없 da 받침 bor → 으니까. Keyin buyruq bor, shuning
    uchun 아/어서 boʻlmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 음악을
  <span class="pe-blank"></span> (듣다) 기분이 좋아요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>들으니까</b> — 듣다 ㄷ notoʻgʻri feʼli, (으) unli bilan boshlanadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 아/어서 yoki (으)니까?
  “Kechikkanim uchun uzr.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>늦어서 죄송합니다.</b> Uzr va rahmatda doim 아/어서.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Bu gap nima degani?
  창문을 여니까 눈이 왔어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Derazani ochsam, qor yogʻayotgan ekan.</b> Bu sabab emas —
    <b>kashfiyot</b>: bir ish qilib, nimadir bilib qolindi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>서울에 살니까 지하철을 자주 타요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>서울에 사니까 지하철을 자주 타요.</b> ㄹ oʻzak ㄴ oldida
    ㄹ ni yoʻqotadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Koreyschaga oʻgiring: “Yomgʻir yogʻyapti,
  shuning uchun soyabon oling.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>비가 오니까 우산을 가져가세요.</b> Keyin buyruq bor → (으)니까.
    오 da 받침 yoʻq → 니까.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)니까</b> — …gani uchun (buyruq bilan); …sam, … ekan</li>
  <li><b>가져가다</b> — olib ketmoq</li>
  <li><b>우산</b> — soyabon</li>
  <li><b>창문</b> — deraza</li>
  <li><b>열다</b> — ochmoq</li>
  <li><b>아무도</b> — hech kim</li>
  <li><b>죄송하다</b> — uzr soʻramoq (rasmiy)</li>
  <li><b>늦다</b> — kechikmoq</li>
  <li><b>기분</b> — kayfiyat</li>
  <li><b>지하철</b> — metro</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)니까</b> — sabab, va undan keyin <b>buyruq mumkin</b>.</li>
    <li>받침 yoʻq → 니까 · 받침 bor → 으니까 · ㄹ oʻzak → 사니까.</li>
    <li>(으) unli, shuning uchun notoʻgʻri feʼllar ishlaydi: 들으니까, 더우니까.</li>
    <li>Zamon (으)니까 dan <b>oldin qoʻyilishi mumkin</b>: 왔으니까.</li>
    <li>Ikkinchi maʼnosi — <b>kashfiyot</b>: 창문을 여니까 비가 왔어요.</li>
    <li>Oʻzbekcha juftligi: “-sam … ekan”.</li>
    <li>Uzr va rahmatda <b>faqat 아/어서</b>: 늦어서 죄송합니다.</li>
    <li>아/어서 — obyektiv, buyruqsiz · (으)니까 — subyektiv, buyruq bilan.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-49: 기 때문에 / 명사 + 때문에 — obyektiv sabab",
        "category": "korean",
        "order": 49,
        "summary": (
            "Yozma va rasmiy sabab. 기 때문에 feʼl bilan, 때문에 ot bilan — "
            "TOPIK yozish qismida eng koʻp kerak boʻladigan qolip."
        ),
        "stories": ["시험 때문에 바빠요"],
        "content": """
<h2>PK-49: 기 때문에 / 명사 + 때문에 — obyektiv sabab</h2>

<p>Sizda endi sababning ikkita yoʻli bor: <b>아/어서</b> (PK-35) va
<b>(으)니까</b> (PK-48). Uchinchisi — <b>때문에</b> — ikkalasidan ham
<em>ogʻirroq</em> va <em>rasmiyroq</em>. Uni suhbatda kam eshitasiz, lekin
gazetada, insho matnida va TOPIK yozish qismida deyarli har paragrafda
uchratasiz. Shuning uchun bu dars ayniqsa imtihonga tayyorlanayotganlar
uchun muhim.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>기 때문에</b> bilan feʼldan sabab yasaysiz</li>
    <li><b>명사 + 때문에</b> bilan otdan sabab yasaysiz</li>
    <li>Uchta sabab qolipini bitta jadvalda taqqoslaysiz</li>
    <li>Gap boshidagi <b>그래서 · 그러니까 · 그렇기 때문에</b> ni ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Feʼl bilan</span>
  <span class="pe-chip pe-chip--s">Oʻzak</span>
  <span class="pe-chip pe-chip--v">기 때문에</span>
  <span class="pe-chip pe-chip--o">Natija</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ot bilan</span>
  <span class="pe-chip pe-chip--s">Ot</span>
  <span class="pe-chip pe-chip--v">때문에</span>
  <span class="pe-chip pe-chip--o">Natija</span>
</div>

<h3>1. Ot + 때문에 — eng oson yoʻl</h3>

<p>Otdan keyin <b>때문에</b> shundoq qoʻshiladi. Hech qanday ayri yoʻq.</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">비 때문에</span>
     학교에 늦었어요.</p>
  <p class="pe-ex__uz">Yomgʻir sababli maktabga kechikdim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--adv">시험 때문에</span>
     요즘 바빠요.</p>
  <p class="pe-ex__uz">Imtihon tufayli shu kunlarda bandman.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu — oʻzbekcha bilan mukammal moslik.</b> “Yomgʻir <em>sababli</em>”,
  “imtihon <em>tufayli</em>” — oʻzbekchada ham ot turadi, keyin koʻmakchi
  keladi. 비 <b>때문에</b>, 시험 <b>때문에</b> — soʻz tartibi ham, tuzilishi ham
  aynan bir xil. Ingliz tilida esa predlog <em>oldinda</em> turadi (“because of
  the rain”). Shuning uchun bu qolipni oʻzbekchadan toʻgʻridan toʻgʻri
  koʻchiring.</p>
</div>

<p>Ot <b>이다</b> bilan kelsa, <b>이기 때문에</b> boʻladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 <span class="pe-hl pe-hl--v">학생이기 때문에</span>
     시간이 없어요.</p>
  <p class="pe-ex__uz">Men talaba boʻlganim uchun vaqtim yoʻq.</p>
</div>

<h3>2. Feʼl / sifat + 기 때문에</h3>

<p>Bu yerda PK-46 dagi <b>기</b> yana ishga tushadi. Oʻzakka 기 qoʻshiladi,
keyin 때문에. 받침 ayrisi yoʻq — 기 undosh bilan boshlanadi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Soʻz</th><th>Oʻzak</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>바쁘다</td><td class="pk-stem">바쁘</td>
      <td class="pk-res">바쁘기 때문에</td><td class="pk-uz">band boʻlgani uchun</td></tr>
  <tr><td>먹다</td><td class="pk-stem">먹</td>
      <td class="pk-res">먹기 때문에</td><td class="pk-uz">yegani uchun</td></tr>
  <tr><td>듣다</td><td class="pk-stem">듣</td>
      <td class="pk-res">듣기 때문에</td><td class="pk-uz">tinglagani uchun</td></tr>
  <tr><td>어렵다</td><td class="pk-stem">어렵</td>
      <td class="pk-res">어렵기 때문에</td><td class="pk-uz">qiyin boʻlgani uchun</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Uchinchi va toʻrtinchi qatorga qarang: <b>듣기</b>, <b>어렵기</b> —
  oʻzgarish yoʻq. 기 undosh, demak notoʻgʻri feʼllar tinch turadi. Bu qoida
  PK-32 dan beri hech oʻzgarmadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어가 <span class="pe-hl pe-hl--v">어렵기 때문에</span>
     매일 공부해요.</p>
  <p class="pe-ex__uz">Koreys tili qiyin boʻlgani uchun har kuni oʻqiyman.</p>
</div>

<h3>3. Zamon 때문에 dan oldin qoʻyiladi</h3>

<p><b>(으)니까</b> dagidek, bu yerda ham oʻtgan zamon bemalol turadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 늦게 <span class="pe-hl pe-hl--v">잤기 때문에</span>
     오늘 피곤해요.</p>
  <p class="pe-ex__uz">Kecha kech yotganim uchun bugun charchaganman.</p>
</div>

<h3>4. Muhim cheklov: keyin buyruq boʻlmaydi</h3>

<div class="pe-call pe-warn">
  <p><b>기 때문에 dan keyin buyruq, taklif va maslahat kelmaydi</b> — xuddi
  아/어서 dagidek. Buyruq berish kerak boʻlsa, <b>(으)니까</b> ni tanlang.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>비가 오기 때문에 우산을 가져가세요.</s></p>
  <p class="pe-good">비가 <b>오니까</b> 우산을 가져가세요.</p>
  <p><small>Keyin buyruq bor → faqat (으)니까.</small></p>
</div>

<h3>5. Uchta sabab qolipi — bitta jadval</h3>

<p>Endi uchalasi ham sizda bor. Bu jadval — PK-35, PK-48 va bugungi darsning
xulosasi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th></th><th>아/어서</th><th>(으)니까</th><th>기 때문에</th></tr>
  <tr><td>Uslubi</td><td class="pk-uz">kundalik</td>
      <td class="pk-uz">kundalik</td><td class="pk-res">rasmiy, yozma</td></tr>
  <tr><td>Keyin buyruq</td><td class="pk-uz">✗</td>
      <td class="pk-res">✓</td><td class="pk-uz">✗</td></tr>
  <tr><td>Oldin zamon</td><td class="pk-uz">✗</td>
      <td class="pk-res">✓</td><td class="pk-res">✓</td></tr>
  <tr><td>Uzr / rahmat</td><td class="pk-res">✓</td>
      <td class="pk-uz">✗</td><td class="pk-uz">✗</td></tr>
  <tr><td>Ot bilan</td><td class="pk-uz">이라서</td>
      <td class="pk-uz">이니까</td><td class="pk-res">Ot + 때문에</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Nega oʻzbek oʻquvchiga bu jadval kerak?</b> Chunki oʻzbek tilida
  uchalasi ham koʻpincha bitta soʻz bilan chiqadi — “<em>uchun</em>”:
  “kech qolganim uchun”, “vaqt yoʻqligi uchun”, “yomgʻir sababli”. Yaʼni ona
  tilingiz sizga qaysi birini tanlashni <b>aytmaydi</b>. Shuning uchun
  tarjimaga emas, ikkita savolga tayaning: <em>keyin buyruq bormi?</em>
  (bor → 니까) va <em>bu yozma matnmi?</em> (ha → 기 때문에).</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham yozma va ogʻzaki uslub boshqa.</b> Doʻstingizga
  “yomgʻir yogʻdi, <em>shuning uchun</em> kech qoldim” deysiz; inshoda esa
  “yomgʻir <em>sababli</em> kechikdim” deb yozasiz. Ikkalasi bir maʼnoni
  beradi, lekin bir joyda ishlatilmaydi. Koreyschada <b>아/어서</b> va
  <b>(으)니까</b> — birinchisi, <b>기 때문에</b> — ikkinchisi. TOPIK yozish
  qismida tekshiruvchi aynan shu farqni koʻradi, shuning uchun inshoda
  때문에 ni tanlang.</p>
</div>

<h3>6. Gap boshida: 그래서 · 그러니까 · 그렇기 때문에</h3>

<p>Uchala qolipning ham gap boshida turadigan shakli bor. Ular oldingi gapni
sabab qilib koʻrsatadi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">그래서</p>
    <p>“shuning uchun” — eng koʻp ishlatiladigan, kundalik</p></div>
  <div class="pe-card"><p class="pe-card__h">그러니까</p>
    <p>“shunday ekan” — keyin buyruq kelishi mumkin</p></div>
  <div class="pe-card"><p class="pe-card__h">그렇기 때문에</p>
    <p>“aynan shu sababdan” — rasmiy, yozma</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">비가 와요. <span class="pe-hl pe-hl--adv">그러니까</span>
     우산을 가져가세요.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻyapti. Shunday ekan, soyabon olib keting.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>비가 때문에 늦었어요.</s></p>
  <p class="pe-good"><b>비 때문에</b> 늦었어요.</p>
  <p><small>때문에 oldidagi otga <b>이/가</b> qoʻshilmaydi — u shundoq
  turadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>바쁘 때문에 못 갔어요.</s></p>
  <p class="pe-good"><b>바쁘기 때문에</b> 못 갔어요.</p>
  <p><small>Feʼl yoki sifat boʻlsa, oʻrtaga <b>기</b> kerak.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>도와줬기 때문에 고맙습니다.</s></p>
  <p class="pe-good">도와<b>줘서</b> 고맙습니다.</p>
  <p><small>Rahmat va uzrda faqat 아/어서 (PK-48).</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>학생 때문에 시간이 없어요 (“talaba boʻlganim uchun”
  maʼnosida)</s></p>
  <p class="pe-good"><b>학생이기 때문에</b> 시간이 없어요.</p>
  <p><small>학생 때문에 “talaba <em>tufayli</em>” degani — boshqa odam haqida.
  Oʻzingiz haqingizda aytmoqchi boʻlsangiz, 이기 때문에 kerak.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: <span class="pe-blank"></span>
  때문에 오늘 학교에 못 갔어요. (“qor”)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>눈</b> — 눈 때문에. Ot 때문에 oldida qoʻshimchasiz turadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 시험이
  <span class="pe-blank"></span> (어렵다) 때문에 많이 공부했어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>어렵기</b> — sifat + 기 때문에. 기 undosh, shuning uchun 어렵
    oʻzgarmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Xatoni toping:
  <s>비가 오기 때문에 우산을 가져가세요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>기 때문에 dan keyin buyruq kelmaydi. Toʻgʻrisi — <b>비가 오니까
    우산을 가져가세요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Qaysi qolipni tanlaysiz?
  “Kechikkanim uchun uzr.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>늦어서 죄송합니다.</b> Uzr va rahmatda faqat 아/어서 — na (으)니까,
    na 기 때문에.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Koreyschaga oʻgiring: “Imtihon tufayli
  shu kunlarda bandman.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>시험 때문에 요즘 바빠요.</b> 시험 — ot, shuning uchun 기 kerak emas.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> 학생 때문에 va 학생이기 때문에 —
  farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>학생 때문에</b> — “talaba <em>tufayli</em>”, yaʼni sabab boshqa
    odam. <b>학생이기 때문에</b> — “talaba <em>boʻlganim</em> uchun”, yaʼni
    oʻzim talabaman.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>기 때문에</b> — …gani uchun (rasmiy, yozma)</li>
  <li><b>명사 + 때문에</b> — … sababli, … tufayli</li>
  <li><b>이기 때문에</b> — … boʻlgani uchun</li>
  <li><b>그래서</b> — shuning uchun</li>
  <li><b>그러니까</b> — shunday ekan</li>
  <li><b>요즘</b> — shu kunlarda</li>
  <li><b>눈</b> — qor; koʻz</li>
  <li><b>늦게</b> — kech</li>
  <li><b>피곤하다</b> — charchagan</li>
  <li><b>시험</b> — imtihon</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>Ot + 때문에</b> — “… sababli”. Ot qoʻshimchasiz turadi:
      비 때문에.</li>
    <li><b>Feʼl/sifat + 기 때문에</b> — oʻzakka 기, keyin 때문에.</li>
    <li><b>이기 때문에</b> — ot + 이다 shakli: 학생이기 때문에.</li>
    <li>기 undosh, shuning uchun notoʻgʻri feʼllar oʻzgarmaydi: 듣기 때문에.</li>
    <li>Zamon oldin qoʻyilishi mumkin: 잤기 때문에.</li>
    <li><b>Keyin buyruq kelmaydi</b> — buyruq uchun (으)니까.</li>
    <li>Uslubi rasmiy va yozma — TOPIK yozish qismida eng kerakli sabab qolipi.</li>
    <li>Gap boshida: 그래서 (kundalik) · 그러니까 (buyruq bilan) ·
      그렇기 때문에 (rasmiy).</li>
  </ul>
</div>
""",
    },
]
