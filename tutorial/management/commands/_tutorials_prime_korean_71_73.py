# -*- coding: utf-8 -*-
"""Prime Korean — Block F, darslar 71–73.

71. (으)ㄹ 겸, 고자 — maqsad va niyatning kuchli shakli
72. 기 마련이다, (으)ㄴ/는 법이다 — tabiiy va muqarrar natija
73. (으)ㄹ지도 모르다, 기 십상이다 — kuchli taxmin va ehtimol

Bu yerdan boshlab USLUB koʻtariladi: 고자, 법이다, 십상이다 — yozma
matn va TOPIK II ning tili. Har bir darsda ogʻzaki jufti bilan
solishtirib koʻrsatiladi ((으)려고 · 기 마련이다 · 것 같다).

Oʻzbekcha kalitlar:
  (으)ㄹ 겸        = "BIR YOʻLA … ham, … ham"
  고자            = "…MAQSADIDA" (rasmiy)
  기 마련이다      = "…ishi TABIIY"
  (으)ㄴ/는 법이다 = "dunyoning QONUNI shu"   (법 = qonun!)
  (으)ㄹ지도 모르다 = "…shi MUMKIN, balki"
  기 십상이다      = "…ib qoʻyishi TURGAN GAP" (doim salbiy)

Yangi aniqlovchi + ot aʼzolari: 겸 (71) va 법 (72) —
roʻyxat: 것 · 줄 · 뻔 · 테 · 뿐 · 데 · 겸 · 법.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_71_73.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_71_73.py --author=prime
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
        "title": "PK-71: (으)ㄹ 겸, 고자 — maqsad va niyatning kuchli shakli",
        "category": "korean",
        "order": 71,
        "summary": (
            "“Bir yoʻla sport ham qilay, doʻstim bilan ham koʻrishay” va "
            "“…maqsadida” — bitta ogʻzaki, bitta rasmiy maqsad qolipi."
        ),
        "stories": ["한국 교환학생 지원서"],
        "content": """
<h2>PK-71: (으)ㄹ 겸, 고자 — maqsad va niyatning kuchli shakli</h2>

<p>Uydan chiqdingiz. Nega? Bitta sabab emas — <em>ikkita</em>: havo
olay ham, non ham olay. Oʻzbekchada buni bir soʻz bilan aytamiz:
“<b>bir yoʻla</b>”. Va boshqa vaziyat: ariza yozyapsiz. U yerda
“bormoqchiman” deyilmaydi, “<b>borish maqsadida</b>” deyiladi. Bugun
shu ikki qolip — biri ogʻzaki, biri rasmiy.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ 겸</b> bilan ikki maqsadni bitta ishga sigʻdirasiz</li>
    <li>Uni ot bilan ham ishlatasiz (<b>아침 겸 점심</b>)</li>
    <li><b>고자</b> bilan rasmiy maqsad aytasiz</li>
    <li>Uni PK-40 dagi <b>(으)려고</b> dan farqlaysiz</li>
    <li>Yettinchi <b>aniqlovchi + ot</b> ni tanib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qolip</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ 겸</span>
  <span class="pe-chip pe-chip--s">고자</span>
  <span class="pe-chip pe-chip--adv">= bir yoʻla … / …maqsadida</span>
</div>

<h3>1. (으)ㄹ 겸 — bitta ish, ikkita maqsad</h3>

<p><b>겸</b> — “qoʻshib, birga” degan ot. Shuning uchun oldida
aniqlovchi (으)ㄹ turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">운동도 <span class="pe-hl pe-hl--v">할 겸</span>
     친구도 <span class="pe-hl pe-hl--v">만날 겸</span> 공원에 갔어요.</p>
  <p class="pe-ex__uz">Bir yoʻla sport ham qilay, doʻstim bilan ham
  koʻrishay deb parkka bordim.</p>
  <p class="pe-ex__why">Ikki marta takrorlanishi — eng koʻp
  uchraydigan shakli.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">바람도 <span class="pe-hl pe-hl--v">쐴 겸</span>
     밖에 나갔어요.</p>
  <p class="pe-ex__uz">Bir oz havo ham olay deb tashqariga chiqdim.</p>
  <p class="pe-ex__why">Bitta 겸 ham boʻladi — u holda “asosiy
  sababdan tashqari yana bu ham bor” degani.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchadagi “bir yoʻla” — aynan shu.</b> “Bir yoʻla bozorga
  ham kiraman, ukamni ham olib kelaman.” Diqqat qiling: oʻzbekchada
  ham ikkala maqsad <em>bitta safarga</em> sigʻadi — alohida ikki ish
  emas. Koreyschada ham xuddi shunday: 겸 ikki maqsadni bitta
  harakatning ichiga soladi. Shuning uchun oxirgi feʼl deyarli har
  doim bitta boʻladi: <b>갔어요</b>, <b>나갔어요</b>, <b>했어요</b>.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Yettinchisi.</b> 것 (52) · 줄 (53) · 뻔 (63) · 테 (64) ·
  뿐 (67) · 데 (68) — bugun <b>겸</b>. Yana oʻsha
  <em>aniqlovchi + ot</em>. Keyingi darsda sakkizinchisi keladi.</p>
</div>

<h3>2. Ot bilan: 명사 + 겸 + 명사</h3>

<p>Ikki vazifani bajaradigan narsa haqida:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">아침 겸 점심</p>
    <p>nonushta ham, tushlik ham</p></div>
  <div class="pe-card"><p class="pe-card__h">거실 겸 서재</p>
    <p>mehmonxona ham, ish xonasi ham</p></div>
  <div class="pe-card"><p class="pe-card__h">가수 겸 배우</p>
    <p>qoʻshiqchi ham, aktyor ham</p></div>
  <div class="pe-card"><p class="pe-card__h">선생님 겸 통역사</p>
    <p>oʻqituvchi ham, tarjimon ham</p></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">늦게 일어나서 <span class="pe-hl pe-hl--o">아침 겸
     점심</span>을 먹었어요.</p>
  <p class="pe-ex__uz">Kech turganim uchun nonushta ham, tushlik ham
  boʻladigan ovqat yedim.</p>
</div>

<h3>3. 고자 — rasmiy maqsad</h3>

<p><b>고자</b> — yozma matnning soʻzi. Arizada, maqolada, rasmiy
nutqda ishlatiladi. Kundalik gapda deyarli eshitilmaydi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 한국어를 <span class="pe-hl pe-hl--v">배우고자</span>
     한국에 왔습니다.</p>
  <p class="pe-ex__uz">Men koreys tilini oʻrganish maqsadida
  Koreyaga keldim.</p>
  <p class="pe-ex__why">Uslub ham rasmiy — <b>습니다</b> (PK-19)
  bilan yuradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">이 문제를 <span class="pe-hl pe-hl--v">해결하고자</span>
     많이 노력했습니다.</p>
  <p class="pe-ex__uz">Bu muammoni hal qilish maqsadida koʻp
  harakat qildim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 의사가 <span class="pe-hl pe-hl--v">되고자
     합니다</span>.</p>
  <p class="pe-ex__uz">Men shifokor boʻlish niyatidaman.</p>
  <p class="pe-ex__why"><b>고자 하다</b> — “…moqchiman” ning rasmiy
  shakli.</p>
</div>

<h3>4. 고자 va (으)려고 (PK-40)</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">(으)려고</p>
    <p><b>Kundalik.</b> Gapda ham, yozuvda ham.</p>
    <p><small>한국어를 배우려고 한국에 왔어요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">고자</p>
    <p><b>Rasmiy va yozma.</b> Ariza, maqola, nutq.</p>
    <p><small>한국어를 배우고자 한국에 왔습니다.</small></p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>고자 ning uchta sharti:</b><br>
  1. Ikkala gapning <b>egasi bir xil</b>.<br>
  2. Faqat <b>feʼl</b> bilan, <b>zamon qoʻshimchasi yoʻq</b>
  (<s>배웠고자</s> ✗).<br>
  3. Keyingi gapda <b>buyruq va taklif kelmaydi</b>
  (<s>배우고자 오세요</s> ✗).</p>
</div>

<div class="pe-call pe-tip">
  <p><b>TOPIK 쓰기 uchun:</b> 54-savolda (uzun insho) “maqsad”
  bildirish kerak boʻlganda <b>고자</b> ishlatsangiz, uslubingiz
  darrov koʻtariladi. Lekin 듣기 va ogʻzaki nutqda uni kutmang —
  u yerda <b>(으)려고</b> eshitiladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>운동도 하 겸 친구도 만나 겸 공원에 갔어요.</s></p>
  <p class="pe-good">운동도 <b>할 겸</b> 친구도 <b>만날 겸</b> 공원에
    갔어요.</p>
  <p><small>겸 — ot, oldida <b>(으)ㄹ</b> aniqlovchisi turadi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>한국어를 배웠고자 한국에 왔습니다.</s></p>
  <p class="pe-good">한국어를 <b>배우고자</b> 한국에 왔습니다.</p>
  <p><small>고자 dan oldin zamon qoʻshimchasi qoʻyilmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>한국어를 배우고자 한국에 가세요.</s></p>
  <p class="pe-good">한국어를 <b>배우려고</b> 하면 한국에 가세요.</p>
  <p><small>고자 dan keyin <b>buyruq</b> kelmaydi.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>친구를 만날 겸 친구가 공원에 왔어요.</s></p>
  <p class="pe-good">친구를 만날 겸 <b>제가</b> 공원에 갔어요.</p>
  <p><small>Maqsad kimniki boʻlsa, harakatni ham <b>oʻsha odam</b>
  qiladi.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 운동도
  <span class="pe-blank"></span> 겸 친구도 만날 겸 공원에 갔어요. (하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>할</b> — 겸 ot, oldida (으)ㄹ turadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> <b>아침 겸 점심</b> nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Nonushta ham, tushlik ham boʻladigan ovqat. Ot bilan
    <b>겸</b> ikki vazifani bildiradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Rasmiy arizada “koreys tilini
  oʻrganish maqsadida keldim” — qanday yoziladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>한국어를 배우고자 한국에 왔습니다.</b> 고자 — yozma va
    rasmiy, shuning uchun 습니다 bilan yuradi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> 고자 va (으)려고 farqi nimada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Maʼnosi bir xil — farq <b>uslubda</b>. (으)려고 kundalik,
    <b>고자</b> rasmiy va yozma.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>한국어를 배웠고자 한국에 왔습니다.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>배우고자</b>. 고자 dan oldin zamon
    qoʻshimchasi qoʻyilmaydi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Yettita “aniqlovchi + ot”
  qolipini sanang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>것</b> (52) · <b>줄</b> (53) · <b>뻔</b> (63) ·
    <b>테</b> (64) · <b>뿐</b> (67) · <b>데</b> (68) ·
    <b>겸</b> (71).</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 겸</b> — bir yoʻla …, … ham</li>
  <li><b>명사 겸 명사</b> — … ham, … ham (ikki vazifa)</li>
  <li><b>고자</b> — …maqsadida (rasmiy)</li>
  <li><b>고자 하다</b> — …moqchi boʻlmoq (rasmiy)</li>
  <li><b>바람을 쐬다</b> — havo olmoq</li>
  <li><b>해결하다</b> — hal qilmoq</li>
  <li><b>노력하다</b> — harakat qilmoq</li>
  <li><b>지원하다</b> — ariza bermoq</li>
  <li><b>교환학생</b> — almashuv talabasi</li>
  <li><b>통역사</b> — tarjimon</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ 겸</b> = bitta ish, ikkita maqsad. Koʻpincha ikki
      marta takrorlanadi.</li>
    <li>Ot bilan: <b>아침 겸 점심</b>, <b>가수 겸 배우</b>.</li>
    <li><b>고자</b> = “…maqsadida” — <b>rasmiy va yozma</b>,
      습니다 bilan yuradi.</li>
    <li>고자 ning sharti: <b>bir xil ega</b> · <b>zamon yoʻq</b> ·
      keyin <b>buyruq yoʻq</b>.</li>
    <li>Kundalik nutqda <b>(으)려고</b> (PK-40), yozma matnda
      <b>고자</b>.</li>
    <li><b>겸</b> — yettinchi aniqlovchi + ot.</li>
    <li>Oʻzbekcha juftliklari: “<b>bir yoʻla</b>” va
      “<b>…maqsadida</b>”.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-72: 기 마련이다, (으)ㄴ/는 법이다 — tabiiy va muqarrar natija",
        "category": "korean",
        "order": 72,
        "summary": (
            "“Odam xato qilishi tabiiy”, “dunyoning qonuni shu” — hayotning "
            "oʻzgarmas qoidalarini aytadigan ikki qolip."
        ),
        "stories": ["할머니의 세 가지 말"],
        "content": """
<h2>PK-72: 기 마련이다, (으)ㄴ/는 법이다 — tabiiy va muqarrar natija</h2>

<p>Nabirasi imtihondan yiqildi va yigʻlayapti. Buvisi nima deydi?
Uni ovutmaydi, dalil ham keltirmaydi — u <em>hayotning qoidasini</em>
aytadi: “Odam <b>xato qiladi-da</b>”, “Vaqt oʻtsa <b>unutiladi</b>”.
Bunday gaplar dalilga muhtoj emas, chunki ular <em>hamma
biladigan haqiqat</em>. Koreys tilida buning uchun ikkita qolip
bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>기 마련이다</b> bilan “…ishi tabiiy” deysiz</li>
    <li><b>(으)ㄴ/는 법이다</b> bilan “qoida shunday” deysiz</li>
    <li>Ikkalasining ohangdagi farqini bilib olasiz</li>
    <li>Nega ular maqollarda koʻp uchrashini koʻrasiz</li>
    <li>Sakkizinchi <b>aniqlovchi + ot</b> ni tanib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qolip</span>
  <span class="pe-chip pe-chip--v">기 마련이다</span>
  <span class="pe-chip pe-chip--s">(으)ㄴ/는 법이다</span>
  <span class="pe-chip pe-chip--adv">= …ishi tabiiy / qoida shunday</span>
</div>

<h3>1. 기 마련이다 — “…ishi tabiiy”</h3>

<p><b>마련</b> — “tayyorgarlik, tabiiy holat” degan ot. Qolip juda
oddiy yasaladi: feʼl yoki sifat oʻzagiga <b>기</b> (PK-46 dagi
otlashtiruvchi) qoʻshiladi, keyin <b>마련이다</b>.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl/sifat</th><th>기</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>실수하다</td><td class="pk-stem">실수하기</td>
      <td class="pk-res">실수하기 마련이다</td>
      <td class="pk-uz">xato qilishi tabiiy</td></tr>
  <tr><td>잊다</td><td class="pk-stem">잊기</td>
      <td class="pk-res">잊기 마련이다</td>
      <td class="pk-uz">unutilishi tabiiy</td></tr>
  <tr><td>어렵다</td><td class="pk-stem">어렵기</td>
      <td class="pk-res">어렵기 마련이다</td>
      <td class="pk-uz">qiyin boʻlishi tabiiy</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">사람은 누구나 <span class="pe-hl pe-hl--v">실수하기
     마련이에요</span>.</p>
  <p class="pe-ex__uz">Har qanday odam xato qilishi tabiiy.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시간이 지나면 <span class="pe-hl pe-hl--v">잊기
     마련이에요</span>.</p>
  <p class="pe-ex__uz">Vaqt oʻtsa, unutilishi tabiiy.</p>
  <p class="pe-ex__why">Koʻpincha <b>(으)면</b> (PK-36) bilan
  juftlik: shart + tabiiy natija.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">처음에는 <span class="pe-hl pe-hl--adv">어렵기
     마련이에요</span>. 걱정하지 마세요.</p>
  <p class="pe-ex__uz">Boshida qiyin boʻlishi tabiiy. Xavotir
  olmang.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>게 마련이다</b> ham bor va maʼnosi bir xil: 실수하게
  마련이에요. Ikkalasi ham toʻgʻri — 기 shakli biroz koʻproq
  uchraydi.</p>
</div>

<h3>2. (으)ㄴ/는 법이다 — “qoida shunday”</h3>

<p><b>법</b> — <em>“qonun”</em> degan ot. Shuning uchun bu qolip
kuchliroq eshitiladi: bu shunchaki kuzatuv emas, <b>hayotning
qonuni</b>.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td>Feʼl</td><td class="pk-end">는 법이다</td>
      <td class="pk-res">성공하는 법이에요</td></tr>
  <tr><td>Sifat, 받침 yoʻq</td><td class="pk-end">ㄴ 법이다</td>
      <td class="pk-res">바쁜 법이에요</td></tr>
  <tr><td>Sifat, 받침 bor</td><td class="pk-end">은 법이다</td>
      <td class="pk-res">좋은 법이에요</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">노력하면 <span class="pe-hl pe-hl--v">성공하는
     법이에요</span>.</p>
  <p class="pe-ex__uz">Harakat qilsa, muvaffaqiyat keladi — qoida
  shunday.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">좋은 일에는 시간이 <span class="pe-hl pe-hl--v">걸리는
     법이에요</span>.</p>
  <p class="pe-ex__uz">Yaxshi ishga vaqt ketadi — dunyoning qonuni shu.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>법 = qonun.</b> Bu soʻzning oʻzi darsning kaliti. Oʻzbekchada
  ham biz aynan shu soʻzni ishlatamiz: “dunyoning <b>qonuni</b> shu”,
  “hayotning <b>qoidasi</b> shunday”. Yaʼni ikkala tilda ham bu
  gaplar <em>huquqiy</em> soʻz bilan aytiladi — chunki ohangi ham
  shunday: bahs qilib boʻlmaydigan haqiqat. Kichikroq ohang uchun esa
  oʻzbekchada “…adi-<b>da</b>” deymiz — “odam xato qiladi-da”. Bu
  <b>기 마련이다</b> ga toʻgʻri keladi.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Sakkizinchisi.</b> 것 · 줄 · 뻔 · 테 · 뿐 · 데 · 겸 —
  bugun <b>법</b>. Oldida aniqlovchi turishi bejiz emas.</p>
</div>

<h3>3. Ikkalasining farqi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">기 마련이다</p>
    <p><b>Yumshoq kuzatuv.</b> “Shunday boʻladi-da.”</p>
    <p>Koʻpincha <em>tasalli</em> berish uchun.</p>
    <p><small>처음에는 어렵기 마련이에요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">(으)ㄴ/는 법이다</p>
    <p><b>Qatʼiy haqiqat.</b> “Qonun shunday.”</p>
    <p>Koʻpincha <em>oʻgit</em> berish uchun.</p>
    <p><small>노력하면 성공하는 법이에요.</small></p>
  </div>
</div>

<div class="pe-call pe-warn">
  <p><b>법이다</b> ni tengdoshingizga koʻp ishlatmang — ohangi
  “men bilaman, sen bilmaysan” degandek chiqadi. U koʻproq
  <em>kattalar</em>, maqollar va yozma matnning tili. Doʻstga
  <b>기 마련이다</b> yumshoqroq.</p>
</div>

<h3>4. Nega bu qoliplar maqollarda koʻp</h3>

<p>Maqol — bu hammaga tegishli, vaqtdan tashqari haqiqat. Aynan shu
sababdan ikkala qolip ham maqol tilida yashaydi. TOPIK II oʻqishida
ular tez-tez uchraydi — matnning <b>xulosa</b> jumlasida.</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h">실수하기 마련이다</p>
    <p>xato qilishi tabiiy</p></div>
  <div class="pe-card"><p class="pe-card__h">시간이 걸리는 법이다</p>
    <p>vaqt ketishi — qonun</p></div>
  <div class="pe-card"><p class="pe-card__h">지나면 잊기 마련이다</p>
    <p>oʻtsa unutiladi</p></div>
  <div class="pe-card"><p class="pe-card__h">노력하면 되는 법이다</p>
    <p>harakat qilsa boʻladi</p></div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>사람은 누구나 실수할 마련이에요.</s></p>
  <p class="pe-good">사람은 누구나 <b>실수하기</b> 마련이에요.</p>
  <p><small>마련 dan oldin <b>기</b> keladi, (으)ㄹ emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>노력하면 성공하기 법이에요.</s></p>
  <p class="pe-good">노력하면 <b>성공하는</b> 법이에요.</p>
  <p><small>법 dan oldin <b>aniqlovchi</b> keladi: feʼl → 는.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>처음에는 어려운 마련이에요.</s></p>
  <p class="pe-good">처음에는 <b>어렵기</b> 마련이에요.</p>
  <p><small>마련 — <b>기</b> bilan, aniqlovchi bilan emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>시간이 지났기 마련이에요.</s></p>
  <p class="pe-good">시간이 지나면 <b>잊기 마련이에요</b>.</p>
  <p><small>Bu qolip <b>umumiy haqiqat</b> haqida — oʻtgan zamondagi
  bitta hodisa haqida emas.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 사람은 누구나
  <span class="pe-blank"></span> 마련이에요. (실수하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>실수하기</b> — 마련 dan oldin <b>기</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 노력하면
  <span class="pe-blank"></span> 법이에요. (성공하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>성공하는</b> — 법 dan oldin aniqlovchi; feʼl 는 oladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> <b>법</b> soʻzi nima degani va
  bu qolipning ohangiga qanday taʼsir qiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>“Qonun.”</b> Shuning uchun 법이다 qatʼiy eshitiladi —
    bahs qilib boʻlmaydigan haqiqat. Oʻzbekchada “dunyoning
    qonuni shu”.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Doʻstingiz imtihondan yiqildi.
  Qaysi qolip yumshoqroq?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>기 마련이에요</b> — “처음에는 어렵기 마련이에요”. 법이에요
    tengdoshga “men bilaman, sen bilmaysan” degandek chiqadi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Xatoni toping:
  <s>처음에는 어려운 마련이에요.</s></p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Toʻgʻrisi — <b>어렵기 마련이에요</b>. 마련 aniqlovchi emas,
    <b>기</b> oladi.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> Sakkizta “aniqlovchi + ot”
  qolipini sanang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>것 · 줄 · 뻔 · 테 · 뿐 · 데 · 겸 · 법.</b></p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>기 마련이다</b> — …ishi tabiiy</li>
  <li><b>(으)ㄴ/는 법이다</b> — qoida shunday</li>
  <li><b>법</b> — qonun · <b>마련</b> — tabiiy holat</li>
  <li><b>누구나</b> — har qanday odam</li>
  <li><b>실수하다</b> — xato qilmoq</li>
  <li><b>잊다</b> — unutmoq</li>
  <li><b>성공하다</b> — muvaffaqiyat qozonmoq</li>
  <li><b>속담</b> — maqol</li>
  <li><b>지혜</b> — donolik</li>
  <li><b>참다</b> — sabr qilmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>기 마련이다</b> = “…ishi tabiiy” — yumshoq kuzatuv,
      koʻpincha tasalli.</li>
    <li><b>(으)ㄴ/는 법이다</b> = “qoida shunday” — qatʼiy,
      koʻpincha oʻgit.</li>
    <li>마련 dan oldin <b>기</b>, 법 dan oldin <b>aniqlovchi</b>.</li>
    <li>Feʼl → <b>는 법이다</b> · Sifat → <b>(으)ㄴ 법이다</b>.</li>
    <li>Koʻpincha <b>(으)면</b> bilan juftlik: shart + tabiiy
      natija.</li>
    <li>Ikkalasi ham <b>umumiy haqiqat</b> haqida — bitta hodisa
      haqida emas.</li>
    <li>Maqol va TOPIK II matnlarining xulosa jumlasida koʻp
      uchraydi.</li>
    <li><b>법</b> — sakkizinchi aniqlovchi + ot.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-73: (으)ㄹ지도 모르다, 기 십상이다 — kuchli taxmin va ehtimol",
        "category": "korean",
        "order": 73,
        "summary": (
            "“Yomgʻir yogʻishi mumkin” va “shoshsang xato qilib qoʻyishing "
            "turgan gap” — ehtimol va ogohlantirish."
        ),
        "stories": ["한국 여행 팁 여섯 가지"],
        "content": """
<h2>PK-73: (으)ㄹ지도 모르다, 기 십상이다 — kuchli taxmin va ehtimol</h2>

<p>Ertaga sayrga chiqasiz. Osmon biroz bulut. Yomgʻir yogʻadimi?
Bilmaysiz — lekin <em>ehtimoli bor</em>. Va yana bir narsani
bilasiz: soyabonsiz chiqsangiz, <em>albatta</em> ivib qolasiz. Mana
bugungi ikki qolip: biri <b>ehtimol</b>, biri <b>ogohlantirish</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>(으)ㄹ지도 모르다</b> bilan “…shi mumkin” deysiz</li>
    <li>Uni PK-52 dagi <b>것 같다</b> bilan solishtirasiz</li>
    <li><b>기 십상이다</b> bilan ogohlantirasiz</li>
    <li>Nega 십상 doim yomon natija haqida ekanini bilib olasiz</li>
    <li>Ishonch darajalarini bir qatorga tizasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qolip</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ지도 모르다</span>
  <span class="pe-chip pe-chip--neg">기 십상이다</span>
  <span class="pe-chip pe-chip--adv">= …shi mumkin / …ib qoʻyishi turgan gap</span>
</div>

<h3>1. (으)ㄹ지도 모르다 — “…shi mumkin”</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">ㄹ지도 모르다</span></p>
    <p>오다 → 올지도 몰라요</p>
    <p>바쁘다 → 바쁠지도 몰라요</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-par">을지도 모르다</span></p>
    <p>먹다 → 먹을지도 몰라요</p>
    <p>어렵다 → 어려울지도 몰라요</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">내일 비가 <span class="pe-hl pe-hl--v">올지도
     몰라요</span>. 우산을 가져가세요.</p>
  <p class="pe-ex__uz">Ertaga yomgʻir yogʻishi mumkin. Soyabon olib
  boring.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">자스루르 씨가 벌써 <span class="pe-hl pe-hl--v">갔을지도
     몰라요</span>.</p>
  <p class="pe-ex__uz">Jasur allaqachon ketgan boʻlishi mumkin.</p>
  <p class="pe-ex__why">Oʻtgan zamon: <b>았/었을지도 모르다</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">그 사람이 새 선생님<span class="pe-hl pe-hl--s">일지도
     몰라요</span>.</p>
  <p class="pe-ex__uz">U odam yangi oʻqituvchi boʻlishi mumkin.</p>
  <p class="pe-ex__why">Ot + 이다 → <b>일지도 모르다</b>.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>모르다</b> bu yerda “bilmayman” degani emas.
  <b>(으)ㄹ지도 모르다</b> — bitta qolip, va u <em>“…shi
  mumkin”</em> degan maʼno beradi. Uni boʻlaklarga ajratib tarjima
  qilmang.</p>
</div>

<h3>2. Ishonch darajalari</h3>

<p>Endi sizda taxmin uchun bir nechta qolip bor. Ularni ishonch
darajasi boʻyicha tizib qoʻying:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Qolip</th><th>Ishonch</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pk-stem">(으)ㄹ 거예요 <small>PK-27</small></td>
      <td>yuqori</td><td class="pk-uz">…adi</td></tr>
  <tr><td class="pk-stem">(으)ㄹ 테니까 <small>PK-64</small></td>
      <td>yuqori (sabab sifatida)</td><td class="pk-uz">…sa kerak</td></tr>
  <tr><td class="pk-stem">(으)ㄹ 것 같다 <small>PK-52</small></td>
      <td>oʻrtacha</td><td class="pk-uz">…ga oʻxshaydi</td></tr>
  <tr><td class="pk-stem">(으)ㄹ지도 모르다</td>
      <td>past — faqat ehtimol</td><td class="pk-uz">…shi mumkin, balki</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham xuddi shunday zinapoya bor:</b>
  “yogʻ<b>adi</b>” → “yogʻ<b>sa kerak</b>” → “yogʻadi<b>ganga
  oʻxshaydi</b>” → “<b>balki</b> yogʻ<b>ar</b>”. Toʻrtta pogʻona,
  yuqoridan pastga. Koreys tilida ham aynan toʻrtta. Yangi gap
  eshitganingizda oʻzingizdan soʻrang: <em>soʻzlovchi qanchalik
  ishonch bilan aytyapti?</em> — javob qaysi qolip kerakligini
  aytadi.</p>
</div>

<h3>3. 기 십상이다 — ogohlantirish</h3>

<p><b>십상</b> — hanzuviy soʻz: <b>十常</b>, yaʼni “oʻn martadan
oʻni”. Demak “deyarli har doim shunday boʻladi”. Lekin bitta muhim
sharti bor: natija <b>doim yomon</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">서두르면 <span class="pe-hl pe-hl--neg">실수하기
     십상이에요</span>.</p>
  <p class="pe-ex__uz">Shoshsangiz, xato qilib qoʻyishingiz turgan gap.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">밤에 커피를 마시면 <span class="pe-hl pe-hl--neg">잠을
     못 자기 십상이에요</span>.</p>
  <p class="pe-ex__uz">Kechasi kofe ichsangiz, uxlay olmay qolishingiz
  turgan gap.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">지도 없이 가면 길을 <span class="pe-hl pe-hl--neg">잃기
     십상이에요</span>.</p>
  <p class="pe-ex__uz">Xaritasiz borsangiz, adashib qolishingiz turgan
  gap.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>기 십상이다 ning uch qoidasi:</b><br>
  1. Faqat <b>feʼl</b> bilan.<br>
  2. Natija <b>albatta salbiy</b> — <s>성공하기 십상이에요</s> ✗.<br>
  3. Koʻpincha <b>(으)면</b> bilan yuradi: shart + ogohlantirish.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">기 마련이다 <small>PK-72</small></p>
    <p><b>Tabiiy</b> — yaxshi ham, yomon ham.</p>
    <p><small>처음에는 어렵기 마련이에요.</small></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">기 십상이다</p>
    <p><b>Ogohlantirish</b> — faqat yomon.</p>
    <p><small>서두르면 실수하기 십상이에요.</small></p>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>내일 비가 오지도 몰라요.</s></p>
  <p class="pe-good">내일 비가 <b>올지도</b> 몰라요.</p>
  <p><small>지도 emas — <b>(으)ㄹ지도</b>. Aniqlovchi shakli
  shart.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>자스루르 씨가 벌써 갈지도 몰랐어요.</s>
    <small>(“ketgan boʻlishi mumkin” maʼnosida)</small></p>
  <p class="pe-good">자스루르 씨가 벌써 <b>갔을지도 몰라요</b>.</p>
  <p><small>Oʻtgan zamon <b>았/었을지도</b> ichida — 모르다 da
  emas.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>열심히 하면 성공하기 십상이에요.</s></p>
  <p class="pe-good">열심히 하면 <b>성공하는 법이에요</b>.</p>
  <p><small>십상 faqat <b>yomon</b> natija uchun. Yaxshi natija —
  PK-72 dagi 법이다 yoki 마련이다.</small></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>서두르면 실수할 십상이에요.</s></p>
  <p class="pe-good">서두르면 <b>실수하기</b> 십상이에요.</p>
  <p><small>십상 dan oldin <b>기</b> keladi, (으)ㄹ emas.</small></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">1</span> Toʻldiring: 내일 비가
  <span class="pe-blank"></span> 몰라요. (오다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>올지도</b> — 오 da 받침 yoʻq → ㄹ지도.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">2</span> Toʻldiring: 시험이
  <span class="pe-blank"></span> 몰라요. (어렵다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>어려울지도</b> — 어렵다 ㅂ notoʻgʻri sifati: 어려우 + ㄹ지도.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">3</span> Toʻldiring: 서두르면
  <span class="pe-blank"></span> 십상이에요. (실수하다)</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>실수하기</b> — 십상 dan oldin <b>기</b>.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">4</span> Nega
  <s>열심히 하면 성공하기 십상이에요</s> notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>십상 natijasi <b>doim salbiy</b>. “Muvaffaqiyat” yaxshi
    natija — unga <b>성공하는 법이에요</b> yoki
    <b>성공하기 마련이에요</b> kerak.</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">5</span> Bu toʻrttasini ishonch boʻyicha
  tizing: 올 것 같아요 · 올 거예요 · 올지도 몰라요.</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p>Eng ishonchli — <b>올 거예요</b>, keyin <b>올 것 같아요</b>,
    eng past — <b>올지도 몰라요</b> (faqat ehtimol).</p>
  </details>
</div>

<div class="pe-quiz">
  <p><span class="pe-quiz__n">6</span> “Jasur allaqachon ketgan
  boʻlishi mumkin” — koreyschada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
    <p><b>자스루르 씨가 벌써 갔을지도 몰라요.</b> Oʻtgan zamon
    았/었을지도 ichida.</p>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ지도 모르다</b> — …shi mumkin, balki</li>
  <li><b>았/었을지도 모르다</b> — …gan boʻlishi mumkin</li>
  <li><b>기 십상이다</b> — …ib qoʻyishi turgan gap (salbiy)</li>
  <li><b>서두르다</b> — shoshmoq</li>
  <li><b>길을 잃다</b> — adashmoq</li>
  <li><b>지도</b> — xarita</li>
  <li><b>없이</b> — …siz</li>
  <li><b>미리</b> — oldindan</li>
  <li><b>붐비다</b> — gavjum boʻlmoq</li>
  <li><b>주의하다</b> — ehtiyot boʻlmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Darsning xulosasi</p>
  <ul>
    <li><b>(으)ㄹ지도 모르다</b> = “…shi mumkin” — eng past ishonch
      darajasi.</li>
    <li>받침 yoʻq → <b>ㄹ지도</b> · 받침 bor → <b>을지도</b> ·
      ot → <b>일지도</b>.</li>
    <li>Oʻtgan zamon <b>았/었을지도</b> ichida, 모르다 da emas.</li>
    <li>Zinapoya: <b>거예요 → 테니까 → 것 같다 → 을지도 모르다</b>.</li>
    <li><b>기 십상이다</b> = ogohlantirish, natija <b>doim
      salbiy</b>.</li>
    <li>십상 (十常) — “oʻn martadan oʻni”. Oldida <b>기</b>
      keladi.</li>
    <li>Yaxshi natija uchun 십상 emas — <b>마련이다 / 법이다</b>
      (PK-72).</li>
    <li>Oʻzbekcha juftliklari: “<b>balki …ar</b>” va
      “<b>…ib qoʻyishi turgan gap</b>”.</li>
  </ul>
</div>
""",
    },
]
