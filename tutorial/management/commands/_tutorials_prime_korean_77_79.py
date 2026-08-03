# -*- coding: utf-8 -*-
"""Prime Korean — Block F, darslar 77–79.

77. 다가, 다가 보면, 다가 보니 — harakat oʻrtasida va yangi natija
78. 았/었더라면 — oʻtmishga oid teskari faraz
79. 다가는 — salbiy natijadan ogohlantirish

Uchtasi bir oilaga tegishli: hammasining ichida **다가** bor.
  77 — 다가 (ish oʻrtasida uzilish) + 보면 (davom etsang, natija)
       + 보니 (davom etdim va kashf qildim)
  78 — 았/었더라면 (oʻtmish boshqacha boʻlganida edi…)
  79 — 다가는 (shunday davom etsang — YOMON natija)

Oʻzbekcha kalitlar:
  다가        = "…ayotib" (toʻxtatib, uzib)
  았/었다가    = "…ib boʻlib, keyin orqaga"
  다가 보면    = "…yaversang, (bir kun) …"
  다가 보니    = "…yaverib, qarasam …"
  았/었더라면  = "…gan boʻlganimda edi, … boʻlardi"
  다가는      = "shunday qilaversang, …"  (doim salbiy)

77 va 79 ni yonma-yon qoʻyish shart: 다가 보면 — betaraf yoki
ijobiy, 다가는 — faqat ogohlantirish. Ikkalasi PK-73 dagi
기 십상이다 bilan uchlik hosil qiladi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_77_79.py --author=prime
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
    # PK-77
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-77: 다가, 다가 보면, 다가 보니 — harakat oʻrtasida va yangi natija",
        "category": "korean",
        "order": 77,
        "summary": (
            "“Ketayotib toʻxtadim”, “qilaversang oʻrganasan”, "
            "“qilaverib, qarasam boʻlib qolibdi” — bitta 다가 dan uchta qolip."
        ),
        "stories": ["매일 십 분"],
        "content": """
<h2>PK-77: 다가, 다가 보면, 다가 보니 — harakat oʻrtasida va yangi natija</h2>

<p>Maktabga ketayotgan edingiz — yoʻlda toʻxtab, doʻstingiz bilan
gaplashib qoldingiz. Har kuni oz-ozdan koreyscha oʻqiyapsiz — bir kun
kelib tushunib ketasiz. Va bir kuni orqaga qarab, hayron qolasiz:
<em>qachon shuncha oʻrganib qoldim?</em> Uchta vaziyat — va uchalasining
ham ichida bitta soʻz turadi: <b>다가</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>다가</b> bilan ishni oʻrtasida uzasiz</li>
    <li><b>았/었다가</b> bilan “qilib boʻlib, keyin orqaga” deysiz</li>
    <li><b>다가 보면</b> bilan kelajakdagi natijani aytasiz</li>
    <li><b>다가 보니</b> bilan oʻzingiz kashf qilgan narsani aytasiz</li>
    <li>Va PK-75 dagi <b>는 길에</b> bilan farqini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta ildiz, uchta qolip</span>
  <span class="pe-chip pe-chip--v">다가</span>
  <span class="pe-chip pe-chip--aux">다가 보면</span>
  <span class="pe-chip pe-chip--aux">다가 보니</span>
</div>

<h3>1. 다가 — ishni oʻrtasida uzish</h3>

<p><b>다가</b> shuni aytadi: A ni qilayotgan edim, uni <em>toʻxtatdim</em>
va B ga oʻtdim. Feʼl oʻzagiga toʻgʻridan toʻgʻri qoʻshiladi —
받침 farqi yoʻq.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">학교에 <span class="pe-hl pe-hl--v">가다가</span>
     자수르 씨를 만났어요.</p>
  <p class="pe-ex__uz">Maktabga ketayotib Jasurni uchratdim
  <em>(va toʻxtadim)</em>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">밥을 <span class="pe-hl pe-hl--v">먹다가</span>
     전화를 받았어요.</p>
  <p class="pe-ex__uz">Ovqat yeyayotib telefonga javob berdim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">책을 <span class="pe-hl pe-hl--v">읽다가</span>
     잠이 들었어요.</p>
  <p class="pe-ex__uz">Kitob oʻqiyotib uxlab qoldim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada 다가 ning izi “-a turib / -ayotib” da.</b>
  “Ket<b>ayotib</b> toʻxtadim”, “yoz<b>a turib</b> charchadim”.
  Lekin bizda bu shakl <em>uzilishni</em> alohida koʻrsatmaydi —
  koreyschada esa <b>다가</b> ning butun vazifasi shu: <em>birinchi ish
  tugamadi, u yarim yoʻlda qoldi</em>. Shuning uchun
  밥을 먹<b>다가</b> 나갔어요 degan odam ovqatini
  <em>tugatmagan</em>.</p>
</div>

<h3>2. 았/었다가 — qilib boʻlib, keyin orqaga</h3>

<p>Agar birinchi ish <b>toʻliq tugagan</b> boʻlsa va keyin
<em>teskarisi</em> boʻlsa — oldiga oʻtgan zamon qoʻyiladi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">학교에 <b>가다가</b> 왔어요.</p>
    <p>Maktabga <b>yetmadim</b> — yoʻldan qaytdim.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">학교에 <b>갔다가</b> 왔어요.</p>
    <p>Maktabga <b>bordim</b> — va qaytdim.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">창문을 <span class="pe-hl pe-hl--v">열었다가</span>
     추워서 닫았어요.</p>
  <p class="pe-ex__uz">Derazani ochdim-u, sovuq boʻlgani uchun yopdim.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>다가 ning uch qoidasi:</b><br>
  1. Ikkala gapning <b>egasi bir xil</b> boʻlishi kerak.<br>
  2. Faqat <b>feʼl</b> bilan.<br>
  3. <b>다가</b> = ish yarim qoldi · <b>았/었다가</b> = ish tugadi,
  keyin teskarisi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>PK-75 dagi 는 길에 bilan solishtiring:</b><br>
  학교에 <b>가는 길에</b> 친구를 만났어요 — uchratdim, lekin
  <em>ketaverdim</em>. Yoʻl davom etdi.<br>
  학교에 <b>가다가</b> 친구를 만났어요 — uchratdim va
  <em>toʻxtadim</em>. Yurish uzildi.<br>
  Ikkalasining tarjimasi bir xil, lekin koreyslar uchun farq
  aniq.</p>
</div>

<h3>3. 다가 보면 — “…yaversang, bir kun …”</h3>

<p>Endi <b>다가</b> ga PK-41 dagi <b>보다</b> qoʻshiladi. Uning
maʼnosi “sinab koʻrmoq” edi — bu yerda esa “<em>davom
ettiraversang</em>”. <b>다가 보면</b> kelajakka qaraydi: hozir
qiynalyapsiz, lekin davom etsangiz natija keladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어를 매일 <span class="pe-hl pe-hl--aux">공부하다가
     보면</span> 실력이 늘 거예요.</p>
  <p class="pe-ex__uz">Har kuni koreyscha oʻqiyversangiz, saviyangiz
  oʻsadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국에서 <span class="pe-hl pe-hl--aux">살다가
     보면</span> 이 문화를 이해하게 될 거예요.</p>
  <p class="pe-ex__uz">Koreyada yashayversangiz, bu madaniyatni tushunib
  qolasiz.</p>
</div>

<div class="pe-call pe-tip">
  <p>Ogʻzaki tilda <b>다가</b> koʻpincha qisqaradi:
  <b>공부하다 보면</b>, <b>살다 보면</b>. Ikkalasi ham toʻgʻri —
  yozma matnda toʻliq shakl koʻproq uchraydi.</p>
</div>

<h3>4. 다가 보니 — “…yaverib, qarasam …”</h3>

<p>Bir xil qolip, boshqa vaqt. <b>다가 보니</b> — <em>oʻtmish</em>:
davom ettirdim va bir kuni <b>oʻzim ham kutmagan narsani kashf
qildim</b>. Ikkinchi gap hamisha oʻtgan zamonda.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">한국 드라마를 <span class="pe-hl pe-hl--aux">보다가
     보니</span> 한국어가 늘었어요.</p>
  <p class="pe-ex__uz">Koreys seriallarini koʻraverib, koreyscham
  oʻsib qolibdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">매일 조금씩 <span class="pe-hl pe-hl--aux">걷다가
     보니</span> 오 킬로그램이 빠졌어요.</p>
  <p class="pe-ex__uz">Har kuni ozgina yuraverib, besh kilo tashlabman.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu ikkisi ham bor, va ikkalasi ham
  “-avermoq” bilan yasaladi:</b> “qil<b>aversang</b>, boʻladi”
  (kelajak — 다가 보면) va “qil<b>averib</b>, qarabsizki boʻlib
  qolibdi” (oʻtmish — 다가 보니). Ikkinchisida bizda
  <em>-(i)bdi</em> qoʻshimchasi bor — “oʻsib qol<b>ibdi</b>”,
  “tashlab<b>man</b>” — u ham xuddi 보니 kabi <em>oʻzim sezmay
  qolibman</em> degan hayratni bildiradi. Ikki tilda bir xil
  fikr.</p>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Vaqti</th><th>Kim aytadi</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pk-stem">다가</td><td>oʻtmish</td>
      <td>ish uzildi</td><td class="pk-uz">…ayotib</td></tr>
  <tr><td class="pk-stem">다가 보면</td><td>kelajak</td>
      <td>maslahat, dalda</td><td class="pk-uz">…yaversang</td></tr>
  <tr><td class="pk-stem">다가 보니</td><td>oʻtmish</td>
      <td>kashfiyot, hayrat</td><td class="pk-uz">…yaverib, qarabsizki</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>학교에 갔다가 친구를 만나서 멈췄어요.</s>
    <small>(“yoʻlda toʻxtadim” maʼnosida)</small></p>
  <p class="pe-good">학교에 <b>가다가</b> 친구를 만났어요.</p>
  <p><small>갔다가 = maktabga <b>yetib bordim</b>. Yoʻlda uzilish
  boʻlsa — zamonsiz <b>가다가</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>제가 밥을 먹다가 동생이 나갔어요.</s></p>
  <p class="pe-good">제가 밥을 <b>먹다가</b> 전화를 받았어요.</p>
  <p><small>다가 da <b>ega bitta</b> boʻlishi shart. Har xil ega
  uchun boshqa qolip kerak — masalan PK-38 dagi
  <b>(으)ㄴ 후에</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>한국어를 공부하다가 보니 실력이 늘 거예요.</s></p>
  <p class="pe-good">한국어를 공부하다가 <b>보면</b> 실력이 늘 거예요.</p>
  <p><small><b>보니</b> — oʻtmishdagi kashfiyot. Kelajak natija uchun
  <b>보면</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>드라마를 보다가 보면 한국어가 늘었어요.</s></p>
  <p class="pe-good">드라마를 보다가 <b>보니</b> 한국어가 늘었어요.</p>
  <p><small>Natija <b>allaqachon</b> boʻlgan — demak
  <b>보니</b>.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 책을
  <span class="pe-blank"></span> 잠이 들었어요. (읽다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>읽다가</b> — oʻzak + 다가, 받침 farqi yoʻq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Farqni ayting:
  학교에 <b>가다가</b> 왔어요 / 학교에 <b>갔다가</b> 왔어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Birinchisi — maktabga <b>yetmadim</b>, yoʻldan qaytdim.
    Ikkinchisi — maktabga <b>bordim</b> va qaytdim.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 보면 yoki 보니?
  한국어를 계속 배우다가 <span class="pe-blank"></span>
  잘하게 될 거예요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>보면</b> — natija <b>kelajakda</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 보면 yoki 보니?
  매일 걷다가 <span class="pe-blank"></span> 살이 빠졌어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>보니</b> — natija <b>allaqachon</b> yuz bergan.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Nega
  <s>제가 밥을 먹다가 동생이 나갔어요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>다가 da ikkala gapning egasi <b>bir xil</b> boʻlishi kerak.
    Bu yerda “men” va “ukam” — ikki xil.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Derazani ochdim-u, keyin
  yopdim” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>창문을 열었다가 닫았어요.</b> Ochish tugagan → 았다가.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu gapni 한다체 ga oʻgiring
  (PK-74): 매일 걷다가 보니 살이 빠졌어요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>매일 걷다가 보니 살이 빠졌다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>다가</b> — …ayotib (uzilish bilan)</li>
  <li><b>았/었다가</b> — …ib boʻlib, keyin orqaga</li>
  <li><b>다가 보면</b> — …yaversang, bir kun …</li>
  <li><b>다가 보니</b> — …yaverib, qarabsizki …</li>
  <li><b>실력</b> — saviya, mahorat</li>
  <li><b>늘다</b> — oʻsmoq, koʻpaymoq</li>
  <li><b>살이 빠지다</b> — ozmoq</li>
  <li><b>조금씩</b> — oz-ozdan</li>
  <li><b>멈추다</b> — toʻxtamoq</li>
  <li><b>계속</b> — davomli, toʻxtovsiz</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>다가</b> = ish yarim yoʻlda uzildi. Oʻzakka toʻgʻridan
      toʻgʻri.</li>
    <li><b>았/었다가</b> = ish tugadi, keyin teskarisi boʻldi.</li>
    <li>가다가 왔어요 (yetmadim) ↔ 갔다가 왔어요 (bordim va qaytdim).</li>
    <li>Ikkala gapning <b>egasi bitta</b>, faqat feʼl bilan.</li>
    <li><b>다가 보면</b> = kelajak natija — dalda va maslahat.</li>
    <li><b>다가 보니</b> = oʻtmishdagi kashfiyot — hayrat.</li>
    <li>Ogʻzaki tilda qisqaradi: 하다 보면 · 하다 보니.</li>
    <li>는 길에 = yoʻl davom etdi · <b>다가 = yoʻl uzildi</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-78
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-78: 았/었더라면 — oʻtmishga oid teskari faraz",
        "category": "korean",
        "order": 78,
        "summary": (
            "“Erta chiqqanimda edi, poyezdga ulgurardim” — boʻlmagan "
            "oʻtmishni tasavvur qilish: afsus ham, shukr ham."
        ),
        "stories": ["한글이 없었더라면"],
        "content": """
<h2>PK-78: 았/었더라면 — oʻtmishga oid teskari faraz</h2>

<p>Poyezdga kechikdingiz. Endi peronda turib oʻylaysiz: <em>“Oʻn daqiqa
erta chiqqanimda edi…”</em> Lekin chiqmadingiz. Oʻtmishni oʻzgartirib
boʻlmaydi — faqat <b>tasavvur</b> qilish mumkin. Koreys tilida shu
tasavvurning oʻz qolipi bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>았/었더라면</b> bilan boʻlmagan oʻtmishni tasavvur qilasiz</li>
    <li>Uni PK-36 dagi oddiy <b>(으)면</b> dan ajratasiz</li>
    <li>Ikkinchi gapda nima kelishini bilib olasiz</li>
    <li>Faqat afsus emas, <b>shukr</b> ham bildirishni oʻrganasiz</li>
    <li>PK-70 dagi <b>(으)ㄹ걸 그랬다</b> bilan solishtirasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">oʻzak + 았/었더라면</span>
  <span class="pe-chip pe-chip--aux">…았/었을 것이다</span>
  <span class="pe-chip pe-chip--adv">= …gan boʻlganimda edi, … boʻlardi</span>
</div>

<h3>1. Shakli</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">ㅏ, ㅗ unlisi</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">았더라면</span></p>
    <p>가다 → 갔더라면</p>
    <p>오다 → 왔더라면</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">boshqa unlilar</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">었더라면</span></p>
    <p>먹다 → 먹었더라면</p>
    <p>있다 → 있었더라면</p>
  </div>
</div>

<p>Ichidagi <b>더</b> — “oʻsha paytga qaytib qarash” belgisi. Shuning
uchun 았/었더라면 sizni <em>oʻtmishning ichiga</em> olib kiradi:
oʻsha kunga qaytib, boshqacha yoʻlni tasavvur qilasiz.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">조금 더 일찍 <span class="pe-hl pe-hl--v">출발했더라면</span>
     기차를 탔을 것이다.</p>
  <p class="pe-ex__uz">Sal erta yoʻlga chiqqanimda edi, poyezdga
  ulgurardim.</p>
  <p class="pe-ex__why">Lekin chiqmadim — va poyezdga ham
  ulgurmadim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그때 한국어를 <span class="pe-hl pe-hl--v">배웠더라면</span>
     지금 많이 편했을 거예요.</p>
  <p class="pe-ex__uz">Oʻshanda koreyscha oʻrganganimda edi, hozir
  ancha qulay boʻlardi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">돈이 <span class="pe-hl pe-hl--v">있었더라면</span>
     그 집을 샀을 거예요.</p>
  <p class="pe-ex__uz">Pulim boʻlganida edi, oʻsha uyni sotib olardim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu qolip oʻzbek tiliga hayratlanarli darajada aniq
  tushadi.</b> “Chiq<b>qanimda edi</b>, ulgur<b>ardim</b>” —
  bizda ham ikki qism bor: birinchisida <em>-gan(imda) edi</em>,
  ikkinchisida <em>-ardim / boʻlardi</em>. Koreyschada ham
  aynan shunday: <b>았/었더라면</b> + <b>았/었을 것이다</b>.
  Ikkala tilda ham ikkinchi qism <em>“shunday boʻlardi, lekin
  boʻlmadi”</em> degan maʼnoni oʻz ichida olib yuradi. Yodlash
  kerak emas — oʻzbekcha jumlani ikkiga boʻlsangiz, koreyschasi
  chiqadi.</p>
</div>

<h3>2. Ikkinchi gapda nima keladi?</h3>

<p>Birinchi qism boʻlmagan narsa boʻlgani uchun, ikkinchi qism ham
boʻlmagan natija. Shuning uchun u <b>taxmin shaklida</b> turadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Ikkinchi gap</th><th>Maʼno</th><th>Misol</th></tr>
  <tr><td class="pk-stem">았/었을 것이다</td><td>eng koʻp uchraydi</td>
      <td class="pk-res">기차를 탔을 것이다</td></tr>
  <tr><td class="pk-stem">았/었을 거예요</td><td>ogʻzaki shakli</td>
      <td class="pk-res">기차를 탔을 거예요</td></tr>
  <tr><td class="pk-stem">(으)ㄹ 뻔했다 <small>PK-63</small></td>
      <td>“sal boʻlmasa …”</td>
      <td class="pk-res">큰일 날 뻔했다</td></tr>
  <tr><td class="pk-stem">았/었을지도 모른다 <small>PK-73</small></td>
      <td>ehtimol</td>
      <td class="pk-res">늦었을지도 모른다</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Ikkinchi gapda hozirgi zamon ham, buyruq ham
  boʻlmaydi:</b><br>
  ❌ <s>일찍 출발했더라면 기차를 타요.</s><br>
  ❌ <s>일찍 출발했더라면 기차를 타세요.</s><br>
  Chunki bu <em>boʻlgan</em> narsa emas — faqat tasavvur.</p>
</div>

<h3>3. (으)면 va 았/었더라면</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)면 <small>PK-36</small></p>
    <p><b>Haqiqiy shart.</b> Hali boʻlishi mumkin.</p>
    <p><small>일찍 출발하면 기차를 탈 거예요.</small></p>
    <p><small>Erta chiqsam, poyezdga ulguraman. — <em>hali
    imkon bor</em></small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">았/었더라면</p>
    <p><b>Teskari faraz.</b> Boʻlmagan va endi boʻlmaydi.</p>
    <p><small>일찍 출발했더라면 기차를 탔을 것이다.</small></p>
    <p><small>Erta chiqqanimda edi… — <em>lekin
    chiqmadim</em></small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p>Koʻpincha oldiga <b>만약</b> yoki <b>만일</b> (“agar”) qoʻyiladi:
  <b>만약</b> 그때 그 사람을 만나지 않았더라면 제 인생은 완전히
  달랐을 거예요. Bu ham xuddi oʻzbekchadagi “<b>agar</b>” kabi —
  gapning boshidayoq “bu faraz” deb ogohlantiradi.</p>
</div>

<h3>4. Faqat afsus emas — shukr ham</h3>

<p>Koʻp oʻquvchi 았/었더라면 ni faqat pushaymonlik deb oʻylaydi.
Aslida u <b>yomon narsadan qutulganda</b> ham ishlatiladi — inkor
bilan.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그때 <span class="pe-hl pe-hl--neg">조심하지
     않았더라면</span> 크게 다쳤을 것이다.</p>
  <p class="pe-ex__uz">Oʻshanda ehtiyot boʻlmaganimda edi, qattiq
  jarohat olardim.</p>
  <p class="pe-ex__why">Afsus emas — <b>shukr</b>. “Yaxshiyamki
  ehtiyot boʻlibman.”</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">친구가 <span class="pe-hl pe-hl--neg">도와주지
     않았더라면</span> 저는 포기했을 거예요.</p>
  <p class="pe-ex__uz">Doʻstim yordam bermaganida edi, men tashlab
  qoʻyardim.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)ㄹ걸 그랬다 <small>PK-70</small></p>
    <p><b>Qisqa afsus</b> — faqat oʻz ishim haqida.</p>
    <p><small>일찍 출발할걸 그랬어요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">았/었더라면</p>
    <p><b>Toʻliq tasavvur</b> — boshqa yoʻl <em>va</em> uning
    natijasi. Boshqa odam haqida ham boʻladi.</p>
    <p><small>일찍 출발했더라면 기차를 탔을 것이다.</small></p>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>일찍 출발하더라면 기차를 탔을 거예요.</s></p>
  <p class="pe-good">일찍 <b>출발했더라면</b> 기차를 탔을 거예요.</p>
  <p><small>Oʻtmish farazi — oldida <b>았/었</b> shart.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>돈이 있었더라면 그 집을 사요.</s></p>
  <p class="pe-good">돈이 있었더라면 그 집을 <b>샀을 거예요</b>.</p>
  <p><small>Ikkinchi gap ham boʻlmagan natija —
  <b>았/었을 것이다</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>내일 비가 왔더라면 안 갈 거예요.</s></p>
  <p class="pe-good">내일 비가 <b>오면</b> 안 갈 거예요.</p>
  <p><small>Ertaga — <b>kelajak</b>. Teskari faraz emas, oddiy
  shart: <b>(으)면</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그때 조심했더라면 크게 다쳤을 거예요.</s>
    <small>(“yaxshiyamki ehtiyot boʻldim” maʼnosida)</small></p>
  <p class="pe-good">그때 <b>조심하지 않았더라면</b> 크게 다쳤을 거예요.</p>
  <p><small>Shukr maʼnosi uchun birinchi gap <b>inkor</b>
  boʻladi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 조금 더 일찍
  <span class="pe-blank"></span> 기차를 탔을 거예요. (출발하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>출발했더라면</b> — oʻtmish farazi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 돈이
  <span class="pe-blank"></span> 그 집을 샀을 거예요. (있다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>있었더라면</b> — 있다 ning oʻzagi 있 → 있었더라면.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> 면 yoki 았/었더라면?
  “Ertaga yomgʻir yogʻsa, bormayman.”</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>(으)면</b> — kelajakdagi haqiqiy shart:
    내일 비가 <b>오면</b> 안 갈 거예요.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Nega
  <s>돈이 있었더라면 그 집을 사요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Ikkinchi gap ham boʻlmagan natija boʻlishi kerak:
    <b>샀을 거예요</b>. Hozirgi zamon mos kelmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Bu gap afsusmi yoki shukr?
  그때 조심하지 않았더라면 크게 다쳤을 거예요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>Shukr.</b> “Ehtiyot boʻlmaganimda edi jarohat olardim” —
    demak ehtiyot boʻlganman va omon qolganman.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Doʻstim yordam bermaganida
  edi, tashlab qoʻyardim” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>친구가 도와주지 않았더라면 저는 포기했을 거예요.</b></p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu gapni 한다체 ga oʻgiring
  (PK-74): 일찍 출발했더라면 기차를 탔을 거예요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>일찍 출발했더라면 기차를 탔을 것이다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>았/었더라면</b> — …gan boʻlganimda edi</li>
  <li><b>만약 / 만일</b> — agar</li>
  <li><b>출발하다</b> — yoʻlga chiqmoq</li>
  <li><b>놓치다</b> — qoʻldan boy bermoq, kechikib qolmoq</li>
  <li><b>다치다</b> — jarohat olmoq</li>
  <li><b>포기하다</b> — voz kechmoq</li>
  <li><b>완전히</b> — butunlay</li>
  <li><b>다르다</b> — boshqacha boʻlmoq</li>
  <li><b>후회하다</b> — pushaymon boʻlmoq</li>
  <li><b>다행이다</b> — yaxshiyamki</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>았/었더라면</b> = boʻlmagan oʻtmishni tasavvur qilish.</li>
    <li>Ichidagi <b>더</b> — oʻsha paytga qaytib qarash belgisi.</li>
    <li>Ikkinchi gap: <b>았/었을 것이다 / 거예요</b>. Hozirgi zamon
      va buyruq boʻlmaydi.</li>
    <li><b>(으)면</b> = haqiqiy shart · <b>았/었더라면</b> = endi
      boʻlmaydigan faraz.</li>
    <li>Koʻpincha oldida <b>만약 / 만일</b> turadi.</li>
    <li>Inkor bilan — <b>afsus emas, shukr</b>:
      조심하지 않았더라면 다쳤을 것이다.</li>
    <li>(으)ㄹ걸 그랬다 = qisqa afsus · 았/었더라면 = toʻliq
      tasavvur.</li>
    <li>Oʻzbekcha juftligi: “<b>…gan(imda) edi, …ardim</b>”.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-79
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-79: 다가는 — salbiy natijadan ogohlantirish",
        "category": "korean",
        "order": 79,
        "summary": (
            "“Shunday oʻynayversang, imtihondan yiqilasan” — hozir "
            "davom etayotgan ishning yomon oxirini aytish."
        ),
        "stories": ["코치의 마지막 말"],
        "content": """
<h2>PK-79: 다가는 — salbiy natijadan ogohlantirish</h2>

<p>Doʻstingiz uch kundan beri darsga kelmayapti. Telefonda oʻyin
oʻynaydi, tunda uxlamaydi. Siz nima deysiz? Oʻzbekchada bitta jumla:
<em>“Shunday qilaversang, imtihondan yiqilasan.”</em> Diqqat qiling —
gap kelajak haqida emas. Gap <b>hozir boʻlayotgan ish</b> haqida va
uning oxiri haqida. Koreys tilida buning aniq qolipi bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>다가는</b> bilan ogohlantirasiz</li>
    <li>Nega natija <b>doim yomon</b> ekanini bilib olasiz</li>
    <li>Nega u <b>hozir davom etayotgan</b> ish haqida ekanini koʻrasiz</li>
    <li>Uni PK-77 dagi <b>다가 보면</b> dan ajratasiz</li>
    <li>PK-73 dagi <b>기 십상이다</b> bilan birga ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">feʼl oʻzagi + 다가는</span>
  <span class="pe-chip pe-chip--neg">yomon natija</span>
  <span class="pe-chip pe-chip--adv">= shunday qilaversang, …</span>
</div>

<h3>1. Shakli va maʼnosi</h3>

<p>PK-77 dagi <b>다가</b> ga <b>는</b> qoʻshildi — va u
mavzu koʻrsatkichi (PK-12). Yaʼni: “<em>ana shu davom etayotgan
ish bor-ku</em> — uning oxiri mana bu”. Shuning uchun 다가는
hamisha <b>allaqachon boshlangan</b> ish haqida.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">그렇게 <span class="pe-hl pe-hl--neg">놀다가는</span>
     시험에 떨어질 거예요.</p>
  <p class="pe-ex__uz">Shunday oʻynayversangiz, imtihondan yiqilasiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이렇게 계속 <span class="pe-hl pe-hl--neg">먹다가는</span>
     살이 찔 거예요.</p>
  <p class="pe-ex__uz">Shunday yeyaversangiz, semirib ketasiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">밤늦게까지 <span class="pe-hl pe-hl--neg">일하다가는</span>
     건강을 잃기 십상이에요.</p>
  <p class="pe-ex__uz">Tungacha ishlayversangiz, sogʻligingizni yoʻqotib
  qoʻyishingiz turgan gap.</p>
  <p class="pe-ex__why">PK-73 dagi <b>기 십상이다</b> — 다가는 ning
  eng tabiiy sherigi.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>다가는 ning uch sharti:</b><br>
  1. Natija <b>albatta yomon</b> — ❌ <s>열심히 하다가는 성공할
  거예요</s>.<br>
  2. Birinchi ish <b>hozir davom etyapti</b> — shuning uchun
  oldida koʻpincha <b>이렇게 / 그렇게 / 계속</b> turadi.<br>
  3. Ikkinchi gap — <b>kelajak yoki taxmin</b>:
  (으)ㄹ 거예요 · 기 십상이다 · (으)ㄹ지도 몰라요.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bunga tayyor qolip bor va u ham
  “-avermoq” bilan yasaladi:</b> “ishla<b>versang</b>,
  charchaysan”, “bunday ket<b>aversa</b>, yomon boʻladi”,
  “shunday qil<b>averasan-u</b>, keyin pushaymon boʻlasan”.
  Eʼtibor bering — bizda ham bu qolip <em>hozir boʻlayotgan</em>
  ish haqida va <em>ogohlantirish</em> ohangida. Ikkala tilda ham
  “shunday” / “bunday” soʻzi deyarli har doim yonida turadi:
  <b>그렇게 놀다가는</b> = <em>shunday</em> oʻynayversang.</p>
</div>

<h3>2. 다가 보면 va 다가는 — bir ildiz, ikki yoʻl</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">다가 보면 <small>PK-77</small></p>
    <p><b>Dalda.</b> Natija yaxshi yoki betaraf.</p>
    <p><small>공부하다가 보면 실력이 늘 거예요.</small></p>
    <p><small>“Oʻqiyversang, oʻsasan.”</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">다가는</p>
    <p><b>Ogohlantirish.</b> Natija faqat yomon.</p>
    <p><small>그렇게 놀다가는 시험에 떨어질 거예요.</small></p>
    <p><small>“Oʻynayversang, yiqilasan.”</small></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p>Ikkalasining ichida ham <b>다가</b> bor, chunki ikkalasi ham
  <em>davom etayotgan ish</em> haqida. Farq — oxirida:
  <b>보면</b> (“qarab koʻrsang”) yoʻlni ochadi,
  <b>는</b> esa yoʻlni koʻrsatib, uning oxiridagi jarni
  koʻrsatadi.</p>
</div>

<h3>3. Uchta ogohlantirish qolipi</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Nima haqida</th><th>Ohangi</th></tr>
  <tr><td class="pk-stem">(으)면 <small>PK-36</small></td>
      <td>har qanday shart</td>
      <td class="pk-uz">betaraf: “…sangiz, …”</td></tr>
  <tr><td class="pk-stem">기 십상이다 <small>PK-73</small></td>
      <td>umumiy xavf</td>
      <td class="pk-uz">“…ib qoʻyishi turgan gap”</td></tr>
  <tr><td class="pk-stem">다가는</td>
      <td><b>hozir qilinayotgan</b> ish</td>
      <td class="pk-uz">shaxsiy ogohlantirish: “toʻxtat”</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">서두르면 실수하기 십상이에요.</p>
  <p class="pe-ex__uz">Shoshsangiz, xato qilib qoʻyasiz.
  <em>(umumiy haqiqat)</em></p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그렇게 <span class="pe-hl pe-hl--neg">서두르다가는</span>
     실수할 거예요.</p>
  <p class="pe-ex__uz">Shunday shoshaversangiz, xato qilasiz.
  <em>(sizga — hozir)</em></p>
</div>

<div class="pe-call pe-warn">
  <p><b>다가는 — kuchli gap.</b> U ohangida “men sizni
  ogohlantiryapman” degan maʼno bor. Shuning uchun uni
  <b>oʻzingizdan katta</b> odamga aytmaslik maʼqul. Ustozga yoki
  boshliqqa gap qaytarayotgandek eshitiladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>열심히 공부하다가는 시험에 붙을 거예요.</s></p>
  <p class="pe-good">열심히 공부<b>하다가 보면</b> 시험에 붙을 거예요.</p>
  <p><small>Natija <b>yaxshi</b> — demak 다가는 emas,
  <b>다가 보면</b>.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>그렇게 놀았다가는 시험에 떨어질 거예요.</s></p>
  <p class="pe-good">그렇게 <b>놀다가는</b> 시험에 떨어질 거예요.</p>
  <p><small>다가는 oldida <b>zamon boʻlmaydi</b> — ish hozir
  davom etyapti.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>이렇게 먹다가는 살이 쪘어요.</s></p>
  <p class="pe-good">이렇게 먹다가는 살이 <b>찔 거예요</b>.</p>
  <p><small>Ikkinchi gap — hali <b>boʻlmagan</b> natija. Oʻtgan
  zamon mos kelmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>날씨가 춥다가는 감기에 걸릴 거예요.</s></p>
  <p class="pe-good">이렇게 얇게 <b>입다가는</b> 감기에 걸릴 거예요.</p>
  <p><small>다가는 faqat <b>feʼl</b> bilan, va ish <b>odamning
  oʻzi</b> qilayotgan boʻlishi kerak.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 그렇게
  <span class="pe-blank"></span> 시험에 떨어질 거예요. (놀다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>놀다가는</b> — oʻzak + 다가는, zamon yoʻq.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> 다가는 yoki 다가 보면?
  열심히 연습하다가 <span class="pe-blank"></span> 잘하게 될 거예요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>보면</b> — natija yaxshi. 다가는 faqat yomon natija
    uchun.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Nega
  <s>이렇게 먹다가는 살이 쪘어요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>다가는 <b>hali boʻlmagan</b> natijani aytadi. Toʻgʻrisi —
    <b>살이 찔 거예요</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Nega 다가는 oldida
  koʻpincha 이렇게 / 그렇게 turadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Chunki 다가는 <b>hozir davom etayotgan</b> ish haqida —
    “<em>ana shunday</em> qilishda davom etsang”. Shuning uchun
    koʻrsatuvchi soʻz tabiiy.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> “Tungacha ishlayversangiz,
  sogʻligingizni yoʻqotasiz” — koreyschada.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>밤늦게까지 일하다가는 건강을 잃을 거예요.</b>
    (yoki <b>잃기 십상이에요</b> — PK-73.)</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Bu ikki gapning farqi nima?
  서두르면 실수하기 십상이에요 / 그렇게 서두르다가는 실수할 거예요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Birinchisi — <b>umumiy haqiqat</b> (kim shoshsa ham).
    Ikkinchisi — <b>aynan sizga</b>, hozir shoshayotganingiz
    uchun.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">7</span> Bu gapni 한다체 ga oʻgiring
  (PK-74): 그렇게 놀다가는 시험에 떨어질 거예요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>그렇게 놀다가는 시험에 떨어질 것이다.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>다가는</b> — shunday qilaversang, … (ogohlantirish)</li>
  <li><b>떨어지다</b> — yiqilmoq, imtihondan oʻtmaslik</li>
  <li><b>붙다</b> — imtihondan oʻtmoq</li>
  <li><b>살이 찌다</b> — semirmoq</li>
  <li><b>건강을 잃다</b> — sogʻlikni yoʻqotmoq</li>
  <li><b>감기에 걸리다</b> — shamollamoq</li>
  <li><b>연습하다</b> — mashq qilmoq</li>
  <li><b>얇게 입다</b> — yupqa kiyinmoq</li>
  <li><b>충고하다</b> — nasihat qilmoq</li>
  <li><b>결국</b> — oxir-oqibat</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>다가는</b> = “shunday qilaversang, …”. Ogohlantirish
      qolipi.</li>
    <li>Natija <b>doim yomon</b> — yaxshi natija uchun
      <b>다가 보면</b> (PK-77).</li>
    <li>Birinchi ish <b>hozir davom etyapti</b> — oldida zamon
      yoʻq.</li>
    <li>Koʻpincha yonida <b>이렇게 / 그렇게 / 계속</b> turadi.</li>
    <li>Ikkinchi gap — kelajak yoki taxmin:
      <b>(으)ㄹ 거예요 · 기 십상이다 · (으)ㄹ지도 몰라요</b>.</li>
    <li>Faqat <b>feʼl</b> bilan, va ish odamning oʻzi
      qilayotgan boʻlishi kerak.</li>
    <li>Kuchli ohang — <b>oʻzidan kattaga aytilmaydi</b>.</li>
    <li>Oʻzbekcha juftligi: “<b>shunday qilaversang, …</b>”.</li>
  </ul>
</div>
""",
    },
]
