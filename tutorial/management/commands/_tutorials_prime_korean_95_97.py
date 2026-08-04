# -*- coding: utf-8 -*-
"""Prime Korean — Block G, darslar 95–97.

95. (이)랍시고, (으)ㄴ/는답시고 — kinoya va taʼna
96. 기 짝이 없다 — oʻta darajani urgʻulash
97. (으)로 말미암아, (으)로 인해 — rasmiy yozma sabab

Oʻzbekcha kalitlar:
  -(느)ㄴ답시고 = "…yaman deb (goʻyo)"   (kinoya — natija yomon)
  (이)랍시고    = "… emish deb"          (ot bilan, shu kinoya)
  기 짝이 없다  = "…ning tengi yoʻq"      (oʻta daraja, yozma)
  (으)로 인해   = "… tufayli"            (rasmiy yozma sabab)
  (으)로 말미암아 = "… oqibatida"          (undan ham rasmiyroq)

PK-95 — koʻchirma gap oilasining OXIRGI aʼzosi. PK-60/92/93 bilan
bir xil qisqarish: -다고 하 + ㅂ시고 → -답시고. Yaʼni oʻquvchi
92-93-95 ni bitta oila sifatida koʻradi: xabar → tekshirish →
hayrat → KINOYA.

PK-96 yana (으)ㅁ/기 ipiga tegadi (PK-46): 기 + 짝(juft) + 없다.
Bu darsda "짝이 없다" ni soʻzma-soʻz ochish shart — "tengi yoʻq"
degan oʻzbekcha ibora bilan bir xil tasvir.

PK-97 sabab zinapoyasini yopadi. Kursda sabab uch marta berilgan:
  아/어서 (35) → (으)니까 (48) → 기 때문에 (49) → 로 인해 (97).
Shuning uchun 97 da jadval bilan butun zinapoyani koʻrsatamiz.
Eng muhim chegara: 때문에 GAP ni ham oladi, 로 인해 faqat OT ni.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_95_97.py --author=prime
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
    # PK-95
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-95: (이)랍시고, (으)ㄴ/는답시고 — kinoya va taʼna",
        "category": "korean",
        "order": 95,
        "summary": (
            "“Oʻqiyman deb xonasiga kirib, faqat oʻyin oʻynaydi” — "
            "birovning bahonasini ishonmasdan keltirish. Koʻchirma "
            "gap oilasining eng oʻtkir aʼzosi."
        ),
        "stories": ["형이 고쳐 준 자전거"],
        "content": """
<h2>PK-95: (이)랍시고, (으)ㄴ/는답시고 — kinoya va taʼna</h2>

<p>Ukangiz “oʻqiyman” deb xonasiga kirdi. Bir soatdan keyin
qarasangiz — oʻyin oʻynayapti. Buni siz qanday aytasiz?
Oʻzbekchada javob tayyor: <em>“Oʻqiyman <b>deb</b> kirdi-yu,
oʻyin oʻynayapti”</em> yoki <em>“goʻyo oʻqirmish”</em>.</p>

<p>Diqqat qiling: siz uning gapini keltiryapsiz, lekin unga
<b>ishonmayapsiz</b>. Koreys tilida bu maʼnoning aniq qolipi bor —
va u kechagi ikki darsning ukasi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>-(느)ㄴ답시고</b> bilan birovning bahonasini kinoya bilan
      keltirasiz</li>
    <li>Ot bilan <b>(이)랍시고</b> shaklini ishlatasiz</li>
    <li>Koʻchirma gap oilasini yakunlaysiz: xabar → tekshirish →
      hayrat → kinoya</li>
    <li>Buni PK-69 dagi <b>느라고</b> dan ajratasiz</li>
    <li>Bu qolipni qachon <em>ishlatmaslik</em> kerakligini bilib
      olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">koʻchirma shakl</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--neg">ㅂ시고</span>
  <span class="pe-chip pe-chip--adv">= …yaman deb (goʻyo)</span>
</div>

<h3>1. Yana oʻsha qisqarish</h3>

<p>PK-92 va PK-93 dagi bilan bir xil hodisa: koʻchirma gap +
qoʻshimcha, oʻrtadagi <b>하</b> tushadi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Toʻliq shakl</th><th>Qisqarishi</th><th>Natija</th></tr>
  <tr><td class="pk-stem">공부한다고 하ㅂ시고</td><td class="pk-end">하 tushadi</td>
      <td class="pk-res">공부한답시고</td></tr>
  <tr><td class="pk-stem">돕는다고 하ㅂ시고</td><td class="pk-end">하 tushadi</td>
      <td class="pk-res">돕는답시고</td></tr>
  <tr><td class="pk-stem">요리라고 하ㅂ시고</td><td class="pk-end">하 tushadi</td>
      <td class="pk-res">요리랍시고</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Koʻchirma gap oilasi — toʻrt dars, bitta ildiz:</b><br>
  <b>-다고 하다</b> (PK-60) → xabar beraman<br>
  <b>-다면서요?</b> (PK-92) → tekshiraman<br>
  <b>-다니!</b> (PK-93) → hayron qolaman<br>
  <b>-답시고</b> (PK-95) → <em>ishonmayman, kinoya qilaman</em><br>
  Bittasini oʻrgansangiz, qolgan uchtasi shakl jihatdan bepul
  keladi. Faqat maʼnosini eslab qolish qoladi.</p>
</div>

<h3>2. Shakllar</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima bilan</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td class="pk-stem">feʼl, 받침 yoʻq</td><td class="pk-end">ㄴ답시고</td>
      <td class="pk-res">공부<b>한답시고</b></td></tr>
  <tr><td class="pk-stem">feʼl, 받침 bor</td><td class="pk-end">는답시고</td>
      <td class="pk-res">돕<b>는답시고</b></td></tr>
  <tr><td class="pk-stem">ot, 받침 yoʻq</td><td class="pk-end">랍시고</td>
      <td class="pk-res">요리<b>랍시고</b></td></tr>
  <tr><td class="pk-stem">ot, 받침 bor</td><td class="pk-end">이랍시고</td>
      <td class="pk-res">선물<b>이랍시고</b></td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">동생은 <span class="pe-hl pe-hl--neg">공부한답시고</span>
     방에 들어가서 게임만 한다.</p>
  <p class="pe-ex__uz">Ukam oʻqiyman deb xonasiga kirib, faqat oʻyin
  oʻynaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">형은 자전거를 <span class="pe-hl pe-hl--neg">고쳐 준답시고</span>
     더 망가뜨렸다.</p>
  <p class="pe-ex__uz">Akam velosipedni tuzataman deb, battar buzib
  qoʻydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--neg">선물이랍시고</span>
     이런 걸 주다니.</p>
  <p class="pe-ex__uz">Sovgʻa emish deb shunaqa narsa beribdi-ya.</p>
  <p class="pe-ex__why">Oxirida PK-93 dagi <b>다니</b> ham bor —
  kinoya + hayrat birga kelsa, gap yanada oʻtkir chiqadi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu — “goʻyo” va “-mish”.</b>
  “<b>Goʻyo</b> oʻqiyotgan emish”, “yordam beraman <b>deb</b>
  aralashdi”. Oʻzbekchada kinoyani biz <em>alohida soʻz</em> bilan
  (goʻyo, emish) yoki ohang bilan beramiz. Koreys tili esa uni
  <b>feʼlning qoʻshimchasiga</b> yashirgan — gap ichida hech qanday
  “goʻyo” koʻrinmaydi, lekin <b>ㅂ시고</b> ni koʻrgan koreys darhol
  tushunadi. Shuning uchun bu qolipni tarjima qilganda oʻzbekchaga
  <em>“goʻyo”</em> ni qoʻshib qoʻying — maʼno toʻliq chiqadi.</p>
</div>

<h3>3. Uchta shart — qolip qachon ishlaydi</h3>

<div class="pe-steps">
  <p><b>1. Bahona boshqa odamniki.</b> Men uning gapini
  keltiryapman.</p>
  <p><b>2. Men unga ishonmayman.</b> Yoki u aytgan ish
  bajarilmagan.</p>
  <p><b>3. Natija yomon.</b> Qolipdan keyin deyarli doim salbiy
  yoki kulgili natija keladi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Uchinchi shart majburiy.</b> Agar natija yaxshi boʻlsa,
  qolip ishlamaydi: <s>공부한답시고 시험을 잘 봤다</s> — notoʻgʻri.
  Kinoya bor joyda natija ham koʻngildagidek chiqmaydi. Yaxshi
  natija uchun oddiy <b>느라고</b> yoki <b>아/어서</b>
  ishlatiladi.</p>
</div>

<h3>4. 느라고 bilan farqi</h3>

<p>PK-69 da <b>느라고</b> ni oʻrgangansiz: “…ish bilan band
boʻlganim uchun”. Ikkalasi ham “bir ish qilib turib, ikkinchisi
buzildi” deydi. Farq — <b>ohangda</b>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">느라고 <small>PK-69</small></p>
    <p><b>Neytral.</b> Sabab rost, men unga ishonaman.</p>
    <p>Oʻzim haqimda ham ishlatiladi.</p>
    <p><small>공부하<b>느라고</b> 전화를 못 받았어요.</small></p>
    <p><small>Oʻqib oʻtirganim uchun telefonni ololmadim.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">답시고 <small>PK-95</small></p>
    <p><b>Kinoya.</b> Sabab — bahona, men ishonmayman.</p>
    <p>Deyarli doim boshqa odam haqida.</p>
    <p><small>공부<b>한답시고</b> 게임만 한다.</small></p>
    <p><small>Goʻyo oʻqiyman deb, faqat oʻyin oʻynaydi.</small></p>
  </div>
</div>

<h3>5. Kimga qarata ishlatmaslik kerak</h3>

<p>Bu qolip — <b>hukm</b>. U gapning egasini past koʻrsatadi.
Shuning uchun:</p>

<div class="pe-steps">
  <p><b>Boʻladi</b> — uka, doʻst, tanish, oʻzim (hazil bilan).</p>
  <p><b>Boʻlmaydi</b> — ustoz, ota-ona, boshliq, yoshi katta odam.
  Ular haqida bu qolipni ishlatish qoʻpollik.</p>
  <p><b>Ehtiyot</b> — gapning egasi yoningizda boʻlsa, buni aytmang.
  Bu — orqadan aytiladigan gap.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Oʻzim haqimda ishlatish mumkin — lekin faqat hazil
  bilan.</b> <b>나는 요리랍시고 뭘 만들었는지 모르겠다</b> —
  “Oshpazlik qilaman deb nima yasadim oʻzim ham bilmayman”. Bu —
  oʻzini past qoʻyish, koreys muloqotida juda oddiy va yoqimli
  narsa. TOPIK yozma ishida esa bu qolipni ishlatmaslik xavfsizroq
  — u <em>hissiy baho</em> beradi, rasmiy tahlil esa buni
  yoqtirmaydi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>동생은 공부하답시고 게임만 한다.</s></p>
  <p class="pe-good">동생은 공부<b>한답시고</b> 게임만 한다.</p>
  <p><small>Feʼl hozirgi zamonda <b>ㄴ다/는다</b> oladi — koʻchirma
  gapning oʻsha tanish qoidasi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>선물랍시고 이런 걸 주다니.</s></p>
  <p class="pe-good">선물<b>이랍시고</b> 이런 걸 주다니.</p>
  <p><small>선물 da 받침 bor → <b>이랍시고</b>. 받침 yoʻq boʻlsa:
  요리<b>랍시고</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>공부한답시고 시험을 잘 봤다.</s></p>
  <p class="pe-good">공부<b>하느라고</b> 시험을 잘 봤다.</p>
  <p><small>Natija yaxshi boʻlsa kinoya oʻrinsiz. 답시고 dan keyin
  faqat <b>yomon</b> natija keladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>선생님은 도와준답시고 오셨다.</s></p>
  <p class="pe-good">선생님은 도와주<b>러</b> 오셨다. / 도와주<b>려고</b>
  오셨다.</p>
  <p><small>Ustoz haqida bu qolip qoʻpol. Hurmat qilinadigan odam
  uchun neytral shakl ishlating.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 동생은
  <span class="pe-blank"></span> 방에 들어가서 게임만 한다. (공부하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>공부한답시고</b> — feʼl, 받침 yoʻq → ㄴ답시고.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring:
  <span class="pe-blank"></span> 이런 걸 주다니. (선물)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>선물이랍시고</b> — ot, 받침 bor → 이랍시고.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring: 형은 자전거를
  <span class="pe-blank"></span> 더 망가뜨렸다. (고쳐 주다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>고쳐 준답시고</b> — 주다 → 준다 → 준답시고.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Bu qolip qaysi oilaga
  kiradi va u oilada nechanchi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Koʻchirma gap</b> oilasi: 다고 하다 (60) → 다면서요 (92)
    → 다니 (93) → <b>답시고 (95)</b>. Toʻrtinchisi va eng
    oʻtkiri.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Nega
  <s>공부한답시고 시험을 잘 봤다</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Qolipdan keyin <b>yomon</b> natija kelishi kerak. Yaxshi
    natija bilan kinoya oʻrinsiz.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> 느라고 va 답시고 farqi
  nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>느라고</b> — neytral, sabab rost. <b>답시고</b> —
    kinoya, sabab bahona.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Ustozingiz haqida bu
  qolipni ishlatsa boʻladimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Yoʻq. Qolip gapning egasini past koʻrsatadi — hurmat
    qilinadigan odamga qarata ishlatilmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">8</span> Koreyschaga oʻgiring
  (한다체): “Akam velosipedni tuzataman deb, battar buzib
  qoʻydi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>형은 자전거를 고쳐 준답시고 더 망가뜨렸다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>-(느)ㄴ답시고</b> — …yaman deb (goʻyo)</li>
  <li><b>(이)랍시고</b> — … emish deb</li>
  <li><b>망가뜨리다</b> — buzib qoʻymoq</li>
  <li><b>고치다</b> — tuzatmoq</li>
  <li><b>핑계</b> — bahona</li>
  <li><b>비꼬다</b> — kinoya qilmoq</li>
  <li><b>참견하다</b> — aralashmoq</li>
  <li><b>부품</b> — ehtiyot qism</li>
  <li><b>용돈</b> — choʻntak puli</li>
  <li><b>자전거</b> — velosiped</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>-(느)ㄴ답시고 / (이)랍시고</b> = birovning bahonasini
      <em>ishonmasdan</em> keltirish.</li>
    <li>Kelib chiqishi: <b>-다고 하 + ㅂ시고</b> → <b>-답시고</b>.</li>
    <li>Feʼl → <b>ㄴ답시고/는답시고</b> · ot → <b>(이)랍시고</b>.</li>
    <li>Uch shart: bahona boshqaniki · men ishonmayman ·
      <b>natija yomon</b>.</li>
    <li><b>느라고</b> neytral · <b>답시고</b> kinoya.</li>
    <li>Hurmat qilinadigan odam haqida ishlatilmaydi.</li>
    <li>Oʻzim haqimda — faqat hazil bilan.</li>
    <li>Oʻzbekcha juftligi: “<b>goʻyo … deb</b>”, “<b>-mish</b>”.</li>
    <li>Koʻchirma gap oilasi shu dars bilan yopiladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-96
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-96: 기 짝이 없다 — oʻta darajani urgʻulash",
        "category": "korean",
        "order": 96,
        "summary": (
            "“Xavfliligining tengi yoʻq” — sifatni eng yuqori "
            "chegaraga koʻtaradigan yozma qolip. Va nega u deyarli "
            "doim salbiy his bilan yuradi."
        ),
        "stories": ["빛을 마시던 시대"],
        "content": """
<h2>PK-96: 기 짝이 없다 — oʻta darajani urgʻulash</h2>

<p>Oʻzbek tilida biror narsani eng yuqori darajada baholamoqchi
boʻlsak, ajoyib ibora ishlatamiz: <em>“Uyatning <b>tengi
yoʻq</b>”</em>, <em>“beadablikning <b>cheki yoʻq</b>”</em>.
Yaʼni bu narsaga <em>juft</em> topilmaydi — u yolgʻiz, eng
chekkada turibdi.</p>

<p>Koreys tilida xuddi shu tasvir bor. Va u xuddi shu soʻz bilan
tuzilgan.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>기 짝이 없다</b> bilan “…ning tengi yoʻq” deysiz</li>
    <li><b>짝</b> soʻzining maʼnosini bilib olasiz</li>
    <li>Nega bu qolip <em>faqat sifat</em> bilan ishlashini
      koʻrasiz</li>
    <li>PK-82 dagi <b>(으)ㄹ 정도로</b> dan farqini oʻrganasiz</li>
    <li>Qaysi uslubga tegishli ekanini — va qachon ishlatmaslik
      kerakligini — bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--adv">형용사 oʻzagi</span>
  <span class="pe-chip pe-chip--o">기</span>
  <span class="pe-chip pe-chip--v">짝이 없다</span>
  <span class="pe-chip pe-chip--s">= …ning tengi yoʻq</span>
</div>

<h3>1. Soʻzma-soʻz ochamiz</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qism</th><th>Maʼnosi</th><th>Qayerdan</th></tr>
  <tr><td class="pk-stem">기</td><td>otlashtirish</td>
      <td class="pk-uz">PK-46</td></tr>
  <tr><td class="pk-stem">짝</td><td><b>juft, teng</b></td>
      <td class="pk-uz">mustaqil ot</td></tr>
  <tr><td class="pk-stem">없다</td><td>yoʻq</td>
      <td class="pk-uz">PK-13</td></tr>
</table></div>

<p>Yaʼni <b>부끄럽기 짝이 없다</b> = “uyatli boʻlish<em>ning</em>
<b>jufti yoʻq</b>” → “uyatning tengi yoʻq”, “oʻta uyatli”.</p>

<div class="pe-call pe-uz">
  <p><b>Ikki tilda bir xil tasvir.</b> Oʻzbekcha “<b>teng</b>i
  yoʻq”, koreyscha “<b>짝</b>이 없다” — ikkalasi ham
  <em>juftlik</em> orqali oʻlchaydi. Bu tasodif emas: koʻp tillarda
  eng yuqori daraja “oʻxshashi topilmaydi” degan fikr bilan
  beriladi. Shuning uchun bu qolipni yodlash shart emas — uni
  oʻzbekcha iborangiz bilan bogʻlab qoʻying, yetadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그때의 방법은 지금 보면
     <span class="pe-hl pe-hl--adv">위험하기 짝이 없다</span>.</p>
  <p class="pe-ex__uz">Oʻsha paytdagi usul hozir qarasangiz —
  xavfliligining tengi yoʻq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 일을 생각하면
     <span class="pe-hl pe-hl--adv">부끄럽기 짝이 없다</span>.</p>
  <p class="pe-ex__uz">Oʻsha ishni oʻylasam, uyatning tengi yoʻq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아무 준비도 없이 시작한 것은
     <span class="pe-hl pe-hl--adv">어리석기 짝이 없었다</span>.</p>
  <p class="pe-ex__uz">Hech qanday tayyorgarliksiz boshlash —
  ahmoqlikning tengi yoʻq edi.</p>
</div>

<h3>2. Faqat sifat bilan</h3>

<p>Bu — qolipning eng qatʼiy qoidasi. <b>기 짝이 없다</b> holatni
<em>baholaydi</em>, harakatni emas. Shuning uchun oldida faqat
<b>형용사</b> turadi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Sifat</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">위험하다</td><td class="pk-res">위험하기 짝이 없다</td>
      <td class="pk-uz">oʻta xavfli</td></tr>
  <tr><td class="pk-stem">부끄럽다</td><td class="pk-res">부끄럽기 짝이 없다</td>
      <td class="pk-uz">oʻta uyatli</td></tr>
  <tr><td class="pk-stem">어리석다</td><td class="pk-res">어리석기 짝이 없다</td>
      <td class="pk-uz">oʻta ahmoqona</td></tr>
  <tr><td class="pk-stem">안타깝다</td><td class="pk-res">안타깝기 짝이 없다</td>
      <td class="pk-uz">oʻta achinarli</td></tr>
  <tr><td class="pk-stem">황당하다</td><td class="pk-res">황당하기 짝이 없다</td>
      <td class="pk-uz">oʻta gʻalati, aql bovar qilmas</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Feʼl bilan ishlamaydi.</b> <s>가기 짝이 없다</s>,
  <s>먹기 짝이 없다</s> — bunday gap yoʻq. Feʼlni baholamoqchi
  boʻlsangiz, avval uni sifatga aylantiring yoki butun ishni ot
  qilib oling: <b>그렇게 행동한 것은 어리석기 짝이 없다</b>.</p>
</div>

<h3>3. Deyarli doim salbiy</h3>

<p>Qolip bilan yuradigan sifatlarga qarang: 위험하다, 부끄럽다,
어리석다, 안타깝다, 황당하다, 어이없다, 지루하다. Hammasi —
<em>yoqimsiz</em>.</p>

<div class="pe-call pe-rule">
  <p><b>Sabab mantiqiy.</b> “Tengi yoʻq” degan baho — kuchli
  hukm. Kuchli hukmni odam koʻpincha <em>norozi</em> boʻlganda
  chiqaradi. Ijobiy sifat bilan ham uchraydi
  (<b>기쁘기 짝이 없다</b> — “xursandchilikning tengi yoʻq”), lekin
  bu juda rasmiy, kitobiy va kamdan-kam. Yozayotganda salbiy
  sifatni tanlang — xato qilmaysiz.</p>
</div>

<h3>4. Uslubi: bu — yozma til</h3>

<div class="pk-level">
  <div class="pk-level__row pk-level__row--1">
    <span class="pk-level__name">kundalik</span>
    <span class="pk-level__ko">진짜 위험해</span>
    <span class="pk-level__who">doʻstlar orasida</span>
  </div>
  <div class="pk-level__row pk-level__row--3">
    <span class="pk-level__name">해요체</span>
    <span class="pk-level__ko">아주 위험해요</span>
    <span class="pk-level__who">kundalik hurmat</span>
  </div>
  <div class="pk-level__row pk-level__row--5">
    <span class="pk-level__name">문어체</span>
    <span class="pk-level__ko">위험하기 짝이 없다</span>
    <span class="pk-level__who">maqola, insho, TOPIK 쓰기</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Qayerda ishlatasiz:</b> gazeta maqolasi, insho, tanqidiy
  matn, tarixiy voqeaga baho, TOPIK 쓰기 54. Qayerda
  ishlatmaysiz: doʻstingiz bilan yozishuv, ogʻzaki suhbat.
  Kundalik gapda bu qolip <em>kitobdan koʻchirilgandek</em>
  eshitiladi.</p>
</div>

<h3>5. (으)ㄹ 정도로 bilan farqi</h3>

<p>PK-82 da darajani <em>oʻlchash</em> ni oʻrgangansiz. Ikkalasi
ham kuchaytiradi, lekin boshqa yoʻl bilan.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)ㄹ 정도로 <small>PK-82</small></p>
    <p><b>Oʻlchov beradi.</b> “Shu darajadaki, …”</p>
    <p>Ketidan <em>misol</em> keladi.</p>
    <p><small>손이 <b>떨릴 정도로</b> 추웠다.</small></p>
    <p><small>Qoʻl titraydigan darajada sovuq edi.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">기 짝이 없다 <small>PK-96</small></p>
    <p><b>Hukm chiqaradi.</b> “Bunga teng narsa yoʻq.”</p>
    <p>Ketidan hech narsa kelmaydi — gap tugaydi.</p>
    <p><small>그 방법은 <b>위험하기 짝이 없다</b>.</small></p>
    <p><small>U usul xavfliligining tengi yoʻq.</small></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">지금 보면 <span class="pe-hl pe-hl--adv">위험하기
     짝이 없는</span> 방법이었다.</p>
  <p class="pe-ex__uz">Hozir qarasangiz — xavfliligining tengi
  yoʻq usul edi.</p>
  <p class="pe-ex__why">Otni aniqlash uchun <b>없는</b> shakli
  ishlatiladi (PK-45): 짝이 <b>없는</b> + 방법.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>그 사람은 가기 짝이 없다.</s></p>
  <p class="pe-good">그 사람의 행동은 <b>어리석기 짝이 없다</b>.</p>
  <p><small>Qolip <b>faqat sifat</b> bilan. Feʼlni baholamoqchi
  boʻlsangiz, holatni bildiruvchi sifat toping.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>위험한 짝이 없다.</s></p>
  <p class="pe-good">위험하<b>기</b> 짝이 없다.</p>
  <p><small>Aniqlovchi shakl emas, <b>기</b> otlashtirishi kerak
  (PK-46).</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>야, 이거 맛없기 짝이 없어!</s></p>
  <p class="pe-good">야, 이거 진짜 맛없어!</p>
  <p><small>Bu — yozma qolip. Doʻstlar orasidagi gapda u
  gʻalati eshitiladi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>위험하기 짝이 없다 방법이었다.</s></p>
  <p class="pe-good">위험하기 짝이 <b>없는</b> 방법이었다.</p>
  <p><small>Otni aniqlaganda 없다 → <b>없는</b> (PK-45).</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> <b>짝</b> soʻzi nimani
  anglatadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Juft, teng</b>. Shuning uchun 짝이 없다 = “tengi
    yoʻq”.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 그때의 방법은
  <span class="pe-blank"></span>. (위험하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>위험하기 짝이 없다</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring: 그 일을
  생각하면 <span class="pe-blank"></span>. (부끄럽다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>부끄럽기 짝이 없다</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Nega
  <s>가기 짝이 없다</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Qolip <b>faqat sifat</b> bilan ishlaydi. 가다 — feʼl.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Otni aniqlaganda shakl
  qanday oʻzgaradi? (위험하기 짝이 없다 + 방법)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>위험하기 짝이 없는 방법</b> — 없다 → 없는 (PK-45).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bu qolip qaysi uslubga
  tegishli?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>문어체</b> — yozma til: maqola, insho, TOPIK 쓰기.
    Ogʻzaki suhbatda ishlatilmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> 기 짝이 없다 va (으)ㄹ
  정도로 farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>정도로</b> — oʻlchov beradi, ketidan misol keladi.
    <b>짝이 없다</b> — hukm chiqaradi, gap shu yerda tugaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">8</span> Koreyschaga oʻgiring
  (한다체): “Hech qanday tayyorgarliksiz boshlash — ahmoqlikning
  tengi yoʻq edi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>아무 준비도 없이 시작한 것은 어리석기 짝이 없었다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>짝</b> — juft, teng</li>
  <li><b>기 짝이 없다</b> — …ning tengi yoʻq</li>
  <li><b>위험하다</b> — xavfli</li>
  <li><b>부끄럽다</b> — uyatli</li>
  <li><b>어리석다</b> — ahmoqona</li>
  <li><b>안타깝다</b> — achinarli</li>
  <li><b>황당하다</b> — aql bovar qilmas</li>
  <li><b>어이없다</b> — hayron qoldiruvchi, bemaʼni</li>
  <li><b>유행하다</b> — moda boʻlmoq</li>
  <li><b>피해</b> — zarar</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>기 짝이 없다</b> = “…ning tengi yoʻq”, oʻta yuqori
      daraja.</li>
    <li>Tuzilishi: <b>기</b> (PK-46) + <b>짝</b> (juft) +
      <b>없다</b>.</li>
    <li><b>Faqat sifat</b> bilan. ❌ 가기 짝이 없다.</li>
    <li>Deyarli doim <b>salbiy</b> sifat bilan.</li>
    <li>Uslubi — <b>문어체</b>: maqola, insho, TOPIK 쓰기.</li>
    <li>Otni aniqlaganda: <b>짝이 없는</b> + ot.</li>
    <li><b>정도로</b> oʻlchaydi · <b>짝이 없다</b> hukm
      chiqaradi.</li>
    <li>Oʻzbekcha juftligi: “<b>tengi yoʻq</b>, <b>cheki
      yoʻq</b>”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-97
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-97: (으)로 말미암아, (으)로 인해 — rasmiy yozma sabab",
        "category": "korean",
        "order": 97,
        "summary": (
            "“Yomgʻir tufayli”, “aholi kamayishi oqibatida” — sabab "
            "bildirishning eng rasmiy shakli. Va nima uchun u faqat "
            "ot bilan ishlaydi."
        ),
        "stories": ["마지막 졸업생"],
        "content": """
<h2>PK-97: (으)로 말미암아, (으)로 인해 — rasmiy yozma sabab</h2>

<p>“Yomgʻir yoqqani uchun oʻyin boʻlmadi” — buni siz PK-49 dan beri
ayta olasiz: <b>비가 왔기 때문에</b>. Endi shu gapni gazetada
koʻring: <em>“Kuchli yomgʻir <b>tufayli</b> oʻyin bekor
qilindi.”</em></p>

<p>Maʼno bir xil. Uslub — butunlay boshqa. Bugun sabab
zinapoyasining eng yuqori pogʻonasini oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)로 인해</b> bilan rasmiy sabab bildirasiz</li>
    <li><b>(으)로 말미암아</b> shaklini va uning oʻrnini bilib
      olasiz</li>
    <li><b>(으)로 인한 + ot</b> aniqlovchi shaklini oʻrganasiz</li>
    <li>Nega bu qolip <em>faqat ot</em> olishini koʻrasiz</li>
    <li>Butun sabab zinapoyasini bir jadvalda yigʻasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">명사</span>
  <span class="pe-chip pe-chip--o">(으)로</span>
  <span class="pe-chip pe-chip--v">인해 / 말미암아</span>
  <span class="pe-chip pe-chip--adv">= … tufayli, … oqibatida</span>
</div>

<h3>1. Shakli</h3>

<p>Asosi — PK-14 dagi <b>(으)로</b> qoʻshimchasi. Unga <b>인하다</b>
(“sabab boʻlmoq”) yoki eski koreyscha <b>말미암다</b> (“kelib
chiqmoq”) feʼli qoʻshiladi.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">명사 + <span class="pk-par">으로 인해</span></p>
    <p>지진<b>으로</b> · 사건<b>으로</b> · 감염<b>으로</b></p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ (yoki ㄹ)</p>
    <p class="pk-batchim__form">명사 + <span class="pk-par">로 인해</span></p>
    <p>사고<b>로</b> · 폭우<b>로</b> · 화재<b>로</b></p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>Uslubi</th><th>Misol</th></tr>
  <tr><td class="pk-stem">(으)로 인해</td><td class="pk-uz">rasmiy yozma</td>
      <td class="pk-res">폭우로 인해 경기가 취소되었다.</td></tr>
  <tr><td class="pk-stem">(으)로 인하여</td><td class="pk-uz">yanada rasmiy</td>
      <td class="pk-res">폭우로 인하여 피해가 커졌다.</td></tr>
  <tr><td class="pk-stem">(으)로 인한 + ot</td><td class="pk-uz">aniqlovchi</td>
      <td class="pk-res">폭우로 인한 피해</td></tr>
  <tr><td class="pk-stem">(으)로 말미암아</td><td class="pk-uz">adabiy, eng rasmiy</td>
      <td class="pk-res">그 결정으로 말미암아 모든 것이 바뀌었다.</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--o">폭우로 인해</span>
     경기가 취소되었다.</p>
  <p class="pe-ex__uz">Kuchli yomgʻir tufayli oʻyin bekor qilindi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--o">인구 감소로 인해</span>
     시골 학교가 문을 닫았다.</p>
  <p class="pe-ex__uz">Aholi kamayishi tufayli qishloq maktabi
  yopildi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 <span class="pe-hl pe-hl--o">결정으로 말미암아</span>
     한 사람의 인생이 바뀌었다.</p>
  <p class="pe-ex__uz">Oʻsha qaror oqibatida bir odamning hayoti
  oʻzgardi.</p>
  <p class="pe-ex__why">말미암아 — ogʻirroq, adabiyroq. U koʻpincha
  <em>katta, qaytarib boʻlmas</em> natija haqida keladi.</p>
</div>

<h3>2. Eng muhim chegara: faqat OT</h3>

<p>Bu qolipning oldida <b>faqat ot</b> tura oladi. <b>기 때문에</b>
esa butun gapni ham, otni ham oladi — mana shu ikkalasining asosiy
farqi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Aytmoqchi boʻlgan gap</th><th>기 때문에</th>
      <th>(으)로 인해</th></tr>
  <tr><td class="pk-stem">Kech qolganim uchun</td>
      <td class="pk-end">늦었<b>기 때문에</b> ✓</td>
      <td class="pk-res">늦었<b>로 인해</b> ✗</td></tr>
  <tr><td class="pk-stem">Kechikish tufayli</td>
      <td class="pk-end">지각 <b>때문에</b> ✓</td>
      <td class="pk-res">지각<b>으로 인해</b> ✓</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Demak qadam oddiy:</b> agar sabab feʼl bilan aytilgan
  boʻlsa, uni avval <b>otga aylantiring</b>, keyin 로 인해 qoʻying.
  <br>늦다 → <b>지각</b> · 비가 오다 → <b>폭우 / 강우</b> ·
  인구가 줄다 → <b>인구 감소</b> · 사람이 다치다 → <b>부상</b>.
  <br>Bu — TOPIK 쓰기 ning asosiy koʻnikmasi: <em>gapni otga
  siqish</em>. Shuning uchun 로 인해 ni oʻrganish sizga faqat
  qolip emas, <b>yozish uslubi</b> beradi.</p>
</div>

<h3>3. Sabab zinapoyasi — butun kurs bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Dars</th><th>Uslub</th><th>Nima oladi</th>
      <th>Misol</th></tr>
  <tr><td class="pk-stem">아/어서</td><td class="pk-end">PK-35</td>
      <td class="pk-uz">kundalik</td><td>gap</td>
      <td class="pk-res">비가 와서 안 갔어요.</td></tr>
  <tr><td class="pk-stem">(으)니까</td><td class="pk-end">PK-48</td>
      <td class="pk-uz">kundalik, subyektiv</td><td>gap</td>
      <td class="pk-res">비가 오니까 안 가요.</td></tr>
  <tr><td class="pk-stem">기 때문에</td><td class="pk-end">PK-49</td>
      <td class="pk-uz">neytral, obyektiv</td><td>gap + ot</td>
      <td class="pk-res">비가 왔기 때문에…</td></tr>
  <tr><td class="pk-stem">는 바람에</td><td class="pk-end">PK-69</td>
      <td class="pk-uz">kutilmagan, salbiy</td><td>gap</td>
      <td class="pk-res">비가 오는 바람에…</td></tr>
  <tr><td class="pk-stem">(으)로 인해</td><td class="pk-end">PK-97</td>
      <td class="pk-uz"><b>rasmiy yozma</b></td><td><b>faqat ot</b></td>
      <td class="pk-res">폭우로 인해…</td></tr>
  <tr><td class="pk-stem">(으)로 말미암아</td><td class="pk-end">PK-97</td>
      <td class="pk-uz">adabiy, eng ogʻir</td><td><b>faqat ot</b></td>
      <td class="pk-res">폭우로 말미암아…</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham xuddi shunday zinapoya bor.</b><br>
  “yomgʻir yogʻ<b>gani uchun</b>” — kundalik (아/어서, 기 때문에)<br>
  “yomgʻir <b>tufayli</b>” — rasmiy (로 인해)<br>
  “yomgʻir <b>oqibatida</b>” — rasmiy yozma (로 말미암아)<br>
  Eʼtibor bering: oʻzbekchada ham “tufayli” va “oqibatida”
  <em>otdan keyin</em> keladi, “-gani uchun” esa <em>feʼldan
  keyin</em>. Yaʼni ikkala tilda ham rasmiy sabab OT talab qiladi.
  Bu — bejiz emas: rasmiy uslub voqeani <em>nomlashni</em> yaxshi
  koʻradi.</p>
</div>

<h3>4. Aniqlovchi shakl: (으)로 인한</h3>

<p>Sababni otga bogʻlamoqchi boʻlsangiz, <b>인해</b> emas,
<b>인한</b> ishlatiladi. Bu — gazeta sarlavhalarining tili.</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--o">폭우로 인한</span>
     피해가 컸다.</p>
  <p class="pe-ex__uz">Kuchli yomgʻir tufayli koʻrilgan zarar katta
  boʻldi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--o">인구 감소로 인한</span>
     문제는 시골에서 먼저 나타난다.</p>
  <p class="pe-ex__uz">Aholi kamayishi tufayli yuzaga kelgan
  muammo avval qishloqda koʻrinadi.</p>
</div>

<h3>5. Qanday sabab bilan yuradi?</h3>

<div class="pe-call pe-warn">
  <p><b>Bu qolip kichik, shaxsiy sabablar uchun emas.</b>
  <s>배가 고픔으로 인해 밥을 먹었다</s> — kulgili chiqadi.
  <b>(으)로 인해</b> odatda <em>katta, tashqi, koʻpchilikka
  taʼsir qiladigan</em> sabab bilan keladi: 폭우, 지진, 화재, 사고,
  감염, 인구 감소, 경기 침체, 기술 발전. Shaxsiy sabab uchun
  <b>아/어서</b> yoki <b>기 때문에</b> yetarli.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>비가 왔기로 인해 경기가 취소되었다.</s></p>
  <p class="pe-good"><b>폭우로 인해</b> 경기가 취소되었다.</p>
  <p><small>Qolip <b>faqat ot</b> oladi. Feʼlli gapni avval otga
  siqing: 비가 오다 → <b>폭우</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>지진로 인해 피해가 컸다.</s></p>
  <p class="pe-good">지진<b>으로</b> 인해 피해가 컸다.</p>
  <p><small>지진 da 받침 (ㄴ) bor → <b>으로</b>. 받침 yoʻq boʻlsa
  yoki ㄹ boʻlsa → 로.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>폭우로 인해 피해가 컸다는 기사</s> →
  <s>폭우로 인해 피해</s></p>
  <p class="pe-good">폭우로 <b>인한</b> 피해</p>
  <p><small>Otni aniqlaganda <b>인한</b> boʻladi, 인해 emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>배가 고픔으로 인해 밥을 먹었다.</s></p>
  <p class="pe-good">배가 고<b>파서</b> 밥을 먹었다.</p>
  <p><small>Kichik, shaxsiy sabab uchun bu qolip ogʻirlik qiladi.
  Kundalik sabab — <b>아/어서</b> (PK-35).</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring:
  <span class="pe-blank"></span> 경기가 취소되었다. (폭우)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>폭우로 인해</b> — 받침 yoʻq → 로.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring:
  <span class="pe-blank"></span> 피해가 컸다. (지진)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>지진으로 인해</b> — 받침 bor → 으로.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Otni aniqlash uchun shakl
  qanday oʻzgaradi? (폭우로 인해 + 피해)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>폭우로 인한 피해</b> — 인해 → <b>인한</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> “Kech qolganim uchun” —
  buni 로 인해 bilan ayta olasizmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻridan-toʻgʻri yoʻq. Avval otga aylantiring:
    <b>지각으로 인해</b>. Yoki oddiy <b>늦었기 때문에</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> 로 인해 va 로 말미암아
  farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Maʼno bir xil. <b>말미암아</b> ogʻirroq, adabiyroq va
    koʻpincha katta, qaytarib boʻlmas natija haqida.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Nega
  <s>배가 고픔으로 인해 밥을 먹었다</s> gʻalati?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Qolip <b>katta, tashqi</b> sabab uchun. Kichik shaxsiy
    sabab — <b>아/어서</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu feʼlli gaplarni otga
  siqing: 비가 오다 · 인구가 줄다 · 사람이 다치다</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>폭우 · 인구 감소 · 부상</b>. Bu koʻnikma TOPIK 쓰기 da
    eng koʻp kerak boʻladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">8</span> Koreyschaga oʻgiring
  (한다체): “Aholi kamayishi tufayli qishloq maktabi yopildi.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>인구 감소로 인해 시골 학교가 문을 닫았다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)로 인해</b> — … tufayli</li>
  <li><b>(으)로 말미암아</b> — … oqibatida</li>
  <li><b>인하다</b> — sabab boʻlmoq</li>
  <li><b>폭우</b> — jala, kuchli yomgʻir</li>
  <li><b>지진</b> — zilzila</li>
  <li><b>피해</b> — zarar</li>
  <li><b>인구 감소</b> — aholi kamayishi</li>
  <li><b>지각</b> — kechikish</li>
  <li><b>취소되다</b> — bekor qilinmoq</li>
  <li><b>문을 닫다</b> — yopilmoq (muassasa)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)로 인해</b> = “… tufayli”, rasmiy yozma sabab.</li>
    <li>받침 bor → <b>으로</b> · yoʻq yoki ㄹ → <b>로</b>.</li>
    <li><b>Faqat ot</b> oladi. Feʼlli gapni avval otga siqing:
      비가 오다 → 폭우.</li>
    <li>Aniqlovchi shakli: <b>(으)로 인한</b> + ot.</li>
    <li><b>말미암아</b> — undan ham rasmiy, adabiy, katta natija
      uchun.</li>
    <li>Katta, tashqi sabab uchun. Shaxsiy sabab — <b>아/어서</b>.</li>
    <li>Sabab zinapoyasi: 아/어서 → (으)니까 → 기 때문에 →
      는 바람에 → <b>(으)로 인해</b> → <b>말미암아</b>.</li>
    <li>Oʻzbekcha juftligi: “<b>tufayli</b>, <b>oqibatida</b>”.</li>
  </ul>
</div>
""",
    },
]
