# -*- coding: utf-8 -*-
"""Prime Korean — Block C, darslar 26–28 (soʻroq, kelasi zamon, xohish).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_26_28.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_26_28.py --author=prime
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
        "title": "PK-26: Soʻroq soʻzlari: 누구, 뭐, 어디, 언제, 왜, 어떻게",
        "category": "korean",
        "order": 26,
        "summary": (
            "Koreys soʻroq soʻzlari gapda oʻz oʻrnida qoladi — hech qayerga "
            "koʻchmaydi. Oʻzbekchada ham xuddi shunday, ingliz tilida esa yoʻq."
        ),
        "stories": ["언제 만나요?"],
        "content": """
<h2>PK-26: Soʻroq soʻzlari: 누구, 뭐, 어디, 언제, 왜, 어떻게</h2>

<p>Siz allaqachon bir nechta soʻroq soʻzini koʻrgansiz: <b>누가</b> (PK-12),
<b>어디</b> (PK-14), <b>무엇</b> (PK-15), <b>몇</b> (PK-23). Bugun ularni bir joyga
yigʻamiz va eng muhim qoidani oʻrganamiz — koreys soʻroq soʻzi <b>gapda oʻz oʻrnida
qoladi</b>. Bu sizga tabiiy tuyuladi, chunki oʻzbekchada ham shunday.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Oltita asosiy soʻroq soʻzini oʻrganasiz</li>
    <li>Ular gapda qayerda turishini bilib olasiz</li>
    <li>누구 + 가 = 누가 qisqarishini eslab qolasiz</li>
    <li>무슨, 어느, 얼마 ni ham tanib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Asosiy oltilik</span>
  <span class="pe-chip pe-chip--s">누구</span>
  <span class="pe-chip pe-chip--o">뭐</span>
  <span class="pe-chip pe-chip--adv">어디</span>
  <span class="pe-chip pe-chip--adv">언제</span>
  <span class="pe-chip pe-chip--neg">왜</span>
  <span class="pe-chip pe-chip--aux">어떻게</span>
</div>

<h3>1. Oltita soʻz</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Soʻz</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pk-stem">누구</td><td class="pk-uz">kim</td>
      <td class="pk-res">저 사람은 누구예요?</td></tr>
  <tr><td class="pk-stem">뭐 / 무엇</td><td class="pk-uz">nima</td>
      <td class="pk-res">뭐 해요?</td></tr>
  <tr><td class="pk-stem">어디</td><td class="pk-uz">qayer</td>
      <td class="pk-res">어디에 가요?</td></tr>
  <tr><td class="pk-stem">언제</td><td class="pk-uz">qachon</td>
      <td class="pk-res">언제 만나요?</td></tr>
  <tr><td class="pk-stem">왜</td><td class="pk-uz">nega</td>
      <td class="pk-res">왜 안 가요?</td></tr>
  <tr><td class="pk-stem">어떻게</td><td class="pk-uz">qanday</td>
      <td class="pk-res">어떻게 공부해요?</td></tr>
</table></div>

<h3>2. Eng muhim qoida: soʻz oʻz oʻrnida qoladi</h3>

<p>Koreys tilida savol yasash uchun <b>soʻzlarni koʻchirish kerak emas</b>. Soʻroq soʻzi
javob turadigan joyga qoʻyiladi, xolos:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Darak</p>
    <p>저는 <b>학교에</b> 가요.</p>
    <p>Men maktabga boraman.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Savol</p>
    <p>저는 <b>어디에</b> 가요?</p>
    <p>Men qayerga boraman?</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu sizda allaqachon shunday ishlaydi:
<br>• Men <b>maktabga</b> boraman → Men <b>qayerga</b> boraman?
<br>• Siz <b>nonni</b> yeysiz → Siz <b>nimani</b> yeysiz?
<br>Soʻroq soʻzi javob turadigan joyda qoladi. Ingliz tilida esa u <em>gap boshiga
koʻchadi</em> va yordamchi feʼl qoʻshiladi (<em>What do you eat?</em>). Shuning uchun
ingliz tilidan oʻrganuvchi bu yerda qiynaladi — siz esa oʻzbekcha gapni deyarli
soʻzma-soʻz koʻchirasiz.</div>

<h3>3. Soʻroq soʻzlari ham qoʻshimcha oladi</h3>

<p>Ular oddiy ot kabi ishlaydi — demak ega, toʻldiruvchi yoki joy boʻlishi mumkin:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Vazifa</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td class="pk-res">Ega</td><td class="pk-stem">누가</td>
      <td class="pk-uz">누가 왔어요? — Kim keldi?</td></tr>
  <tr><td class="pk-res">Toʻldiruvchi</td><td class="pk-stem">누구를</td>
      <td class="pk-uz">누구를 만나요? — Kimni uchratasiz?</td></tr>
  <tr><td class="pk-res">Egalik</td><td class="pk-stem">누구의</td>
      <td class="pk-uz">누구의 책이에요? — Kimning kitobi?</td></tr>
  <tr><td class="pk-res">Joy</td><td class="pk-stem">어디에 / 어디에서</td>
      <td class="pk-uz">어디에서 공부해요? — Qayerda oʻqiysiz?</td></tr>
  <tr><td class="pk-res">Toʻldiruvchi</td><td class="pk-stem">뭐를 / 무엇을</td>
      <td class="pk-uz">뭐를 먹어요? — Nima yeysiz?</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>누구 + 가 = 누가</b> — bu qisqarish majburiy. <s>누구가</s> deb yozilmaydi. PK-12 da
buni koʻrgan edingiz; endi sababini bilasiz.</div>

<h3>4. 뭐 va 무엇</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">뭐 — ogʻzaki</p>
    <p>Kundalik nutqda deyarli har doim shu.</p>
    <p><b>뭐 해요?</b> — Nima qilyapsiz?</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">무엇 — yozma</p>
    <p>Rasmiy matn, imtihon, kitob.</p>
    <p><b>무엇을 합니까?</b></p>
  </div>
</div>

<p>Ogʻzaki nutqda qoʻshimcha ham koʻpincha tushiriladi: <b>뭐 해요?</b>
(뭐를 해요? oʻrniga), <b>어디 가요?</b> (어디에 가요? oʻrniga). Bu xato emas —
kundalik qisqarish.</p>

<h3>5. 왜 va 어떻게</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 왜 학교에 안 가요?<br>나: 시간이 없어요.</p>
  <p class="pe-ex__uz">A: Nega maktabga bormaysiz?<br>B: Vaqtim yoʻq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 어떻게 한국어를 공부해요?<br>나: 매일 책을 읽어요.</p>
  <p class="pe-ex__uz">A: Koreys tilini qanday oʻrganasiz?<br>B: Har kuni kitob
     oʻqiyman.</p>
</div>

<h3>6. Yana uchta foydali soʻz</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Soʻz</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pk-stem">무슨 + ot</td><td class="pk-uz">qanaqa, qaysi</td>
      <td class="pk-res">무슨 책이에요? — Qanaqa kitob?</td></tr>
  <tr><td class="pk-stem">어느 + ot</td><td class="pk-uz">qaysi biri</td>
      <td class="pk-res">어느 나라 사람이에요? — Qaysi mamlakatdansiz?</td></tr>
  <tr><td class="pk-stem">얼마</td><td class="pk-uz">qancha (narx)</td>
      <td class="pk-res">이것은 얼마예요? — Bu qancha?</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>무슨</b> va <b>어느</b> farqi: 무슨 — turini soʻraydi (“qanaqa kitob?”), 어느 esa
maʼlum roʻyxatdan tanlashni soʻraydi (“qaysi kitob?”). Oʻzbekchada bu farq
<em>qanaqa</em> va <em>qaysi</em> bilan beriladi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>누구가</s> 왔어요?</p>
  <p class="pe-good">Majburiy qisqarish: <b>누가</b> 왔어요?</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Ingliz tilidagidek soʻzni oldinga koʻchirish:
     <s>뭐 저는 먹어요?</s></p>
  <p class="pe-good">Soʻroq soʻzi <b>oʻz oʻrnida</b>: 저는 <b>뭐</b> 먹어요?</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>어디 공부해요?</s> ("qayerda oʻqiysiz" maʼnosida)</p>
  <p class="pe-good">Harakat joyi → <b>에서</b>: <b>어디에서</b> 공부해요? (PK-14)</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Rasmiy yozuvda <s>뭐</s> ishlatish.</p>
  <p class="pe-good">Yozma matnda <b>무엇</b>: 무엇을 합니까?</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Koreys soʻroq soʻzi gapda qayerda turadi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Javob turadigan joyda</strong> — hech qayerga
    koʻchmaydi. 저는 학교에 가요 → 저는 <b>어디에</b> 가요? Oʻzbekchada ham shunday;
    ingliz tilida esa soʻroq soʻzi gap boshiga chiqadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga nima tushadi? <span class="pe-blank">?</span> 왔어요? (“Kim keldi?”)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>누가</strong>. 누구 + 가 majburiy ravishda
    <b>누가</b> boʻlib qisqaradi — <s>누구가</s> notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     “Qayerda oʻqiysiz?” ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>어디에서 공부해요?</strong> 공부하다 — harakat
    feʼli, shuning uchun joy <b>에서</b> oladi (PK-14). 어디에 boʻlsa “qayerga” degan
    maʼno chiqardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>무슨</b> va <b>어느</b> farqi nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>무슨</strong> turini soʻraydi — “<em>qanaqa</em>
    kitob?”. <strong>어느</strong> esa maʼlum roʻyxatdan tanlashni — “<em>qaysi</em>
    kitob?”. Ikkalasi ham otdan oldin turadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bekzod “저는 뭐를 먹어요?” dedi. Ogʻzaki nutqda buni qanday qisqartirish
     mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>저는 뭐 먹어요?</strong> Kundalik nutqda soʻroq
    soʻzidan keyingi qoʻshimcha koʻpincha tushiriladi: 뭐 해요?, 어디 가요?. Bu xato
    emas — tabiiy qisqarish.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>누구 / 누가</b><span>kim / kim (ega)</span></li>
  <li><b>뭐 / 무엇</b><span>nima (ogʻzaki / yozma)</span></li>
  <li><b>어디</b><span>qayer</span></li>
  <li><b>언제</b><span>qachon</span></li>
  <li><b>왜</b><span>nega</span></li>
  <li><b>어떻게</b><span>qanday</span></li>
  <li><b>무슨</b><span>qanaqa</span></li>
  <li><b>어느</b><span>qaysi biri</span></li>
  <li><b>얼마</b><span>qancha (narx)</span></li>
  <li><b>나라</b><span>mamlakat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>Soʻroq soʻzi <b>oʻz oʻrnida qoladi</b> — oʻzbekchadagidek, ingliz tilidagidek
        emas.</li>
    <li>Ular oddiy ot kabi <b>qoʻshimcha oladi</b>: 누구를, 어디에서, 무엇을.</li>
    <li><b>누구 + 가 = 누가</b> — majburiy qisqarish.</li>
    <li><b>뭐</b> ogʻzaki, <b>무엇</b> yozma.</li>
    <li>Ogʻzaki nutqda qoʻshimcha tushishi mumkin: <b>뭐 해요?</b></li>
    <li><b>무슨</b> = qanaqa (tur), <b>어느</b> = qaysi (tanlov).</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-27: 동사 + (으)ㄹ 거예요 — kelasi zamon va taxmin",
        "category": "korean",
        "order": 27,
        "summary": (
            "Kelasi zamon va niyat uchun asosiy shakl. Bir qolip ikki vazifada: "
            "oʻzingiz haqingizda — reja, boshqalar haqida — taxmin."
        ),
        "stories": ["내일 뭐 할 거예요?"],
        "content": """
<h2>PK-27: 동사 + (으)ㄹ 거예요 — kelasi zamon va taxmin</h2>

<p>Hozirgi va oʻtgan zamonni bilasiz. Endi uchinchisi — <b>kelasi</b>. Koreys tilida
buning eng koʻp ishlatiladigan shakli <b>(으)ㄹ 거예요</b>. Uning qiziq tomoni shundaki,
u <em>ikki xil ish</em> qiladi: oʻzingiz haqingizda gapirsangiz — reja va niyat,
boshqa odam yoki ob-havo haqida gapirsangiz — taxmin.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>(으)ㄹ 거예요 ni 받침 qoidasi boʻyicha yasaysiz</li>
    <li>Uning ikki maʼnosini ajratasiz: reja va taxmin</li>
    <li>Talaffuzdagi qattiqlashishni bilib olasiz</li>
    <li>Rasmiy shakl — (으)ㄹ 겁니다 ni tanib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kelasi zamon</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">(으)ㄹ 거예요</span>
</div>

<h3>1. Shakl — yana 받침 ayrisi</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-end">ㄹ 거예요</span></p>
    <p>가 → 갈 거예요</p>
    <p>오 → 올 거예요 · 배우 → 배울 거예요</p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-end">을 거예요</span></p>
    <p>먹 → 먹을 거예요</p>
    <p>읽 → 읽을 거예요 · 있 → 있을 거예요</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
받침 yoʻq boʻlsa <b>ㄹ oʻzakning tagiga tushadi</b> — xuddi PK-19 dagi ㅂ니다 kabi:
가 + ㄹ = <b>갈</b>, 배우 + ㄹ = <b>배울</b>. Bu qoʻshimcha emas, blokka qoʻshiladigan
harf.</div>

<p><b>ㄹ oʻzaklar:</b> agar oʻzak allaqachon ㄹ bilan tugasa, yangi ㄹ qoʻshilmaydi —
oʻsha ㄹ ning oʻzi ishlatiladi: 살다 → <b>살 거예요</b>, 알다 → <b>알 거예요</b>.</p>

<h3>2. Talaffuz — 거 qattiqlashadi</h3>

<div class="pk-say">
  <span class="pk-say__from">갈 거예요</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[갈 꺼예요]</span>
  <span class="pk-say__why">ㄹ dan keyin ㄱ qattiqlashadi</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">먹을 거예요</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[머글 꺼예요]</span>
  <span class="pk-say__why">연음화 + 경음화 birga</span>
</div>

<p>Yozilishi hech qachon oʻzgarmaydi — har doim <b>거예요</b>, lekin oʻqilishi
<b>[꺼예요]</b>.</p>

<h3>3. Birinchi maʼno: reja va niyat</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 내일 학교에 갈 거예요.</p>
  <p class="pe-ex__uz">Men ertaga maktabga boraman. / Bormoqchiman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">주말에 한국어를 공부할 거예요.</p>
  <p class="pe-ex__uz">Dam olish kunlari koreys tilini oʻrganaman.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada <em>“boraman”</em> ham hozirgi, ham kelasi zamonni bildiradi — kontekst hal
qiladi. Koreys tilida ham <b>가요</b> shunday ishlaydi. Lekin <b>갈 거예요</b> aniq
<em>niyat</em> qoʻshadi va oʻzbekcha <b>“bormoqchiman”</b> ga yaqinroq turadi. Ya'ni:
<br>• 가요 ≈ boraman (umumiy)
<br>• 갈 거예요 ≈ bormoqchiman, boraman (rejalashtirilgan)</div>

<h3>4. Ikkinchi maʼno: taxmin</h3>

<p>Gap <em>boshqa odam</em> yoki <em>tabiat</em> haqida borsa, xuddi shu shakl
“ehtimol” maʼnosini beradi — chunki siz uning niyatini bilolmaysiz:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">내일 비가 올 거예요.</p>
  <p class="pe-ex__uz">Ertaga yomgʻir yogʻsa kerak.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">자수르 씨는 집에 있을 거예요.</p>
  <p class="pe-ex__uz">Jasur uyda boʻlsa kerak.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Farqni <b>ega</b> hal qiladi:
<br>• <b>저는 …ㄹ 거예요</b> → reja (“men qilaman”)
<br>• <b>그 사람은 …ㄹ 거예요</b> → taxmin (“u qilsa kerak”)
<br>Bir xil shakl, ikki xil maʼno — kim haqida gapirayotganingizga bogʻliq.</div>

<h3>5. Inkor va oʻtgan zamon bilan</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">Tasdiq</td><td class="pk-stem">갈 거예요</td>
      <td class="pk-uz">boraman</td></tr>
  <tr><td class="pk-res">Inkor (안)</td><td class="pk-stem">안 갈 거예요</td>
      <td class="pk-uz">bormayman</td></tr>
  <tr><td class="pk-res">Inkor (지 않다)</td><td class="pk-stem">가지 않을 거예요</td>
      <td class="pk-uz">bormayman</td></tr>
  <tr><td class="pk-res">Savol</td><td class="pk-stem">갈 거예요?</td>
      <td class="pk-uz">borasizmi?</td></tr>
  <tr><td class="pk-res">Rasmiy</td><td class="pk-stem">갈 겁니다</td>
      <td class="pk-uz">boraman (합니다체)</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 내일 뭐 할 거예요?<br>나: 친구를 만날 거예요.</p>
  <p class="pe-ex__uz">A: Ertaga nima qilasiz?<br>B: Doʻstimni uchrataman.</p>
  <p class="pe-ex__why">하다 → 할 거예요, 만나다 → 만날 거예요.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">먹다 → <s>먹ㄹ 거예요</s></p>
  <p class="pe-good">받침 bor → <b>먹을 거예요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">가다 → <s>가을 거예요</s></p>
  <p class="pe-good">받침 yoʻq → ㄹ tagiga tushadi: <b>갈 거예요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">살다 → <s>살을 거예요</s></p>
  <p class="pe-good">Oʻzak allaqachon ㄹ bilan tugagan: <b>살 거예요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">갈 거예요 ni "kal ko-ye-yo" deb oʻqish.</p>
  <p class="pe-good">경음화: <b>[갈 꺼예요]</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>먹다</b> ni kelasi zamonga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>먹을 거예요</strong>. Oʻzak 먹 받침li (ㄱ),
    shuning uchun <b>을 거예요</b>. Oʻqilishi [머글 꺼예요].</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>배우다</b> ni kelasi zamonga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>배울 거예요</strong>. Oʻzak 배우 받침siz, shuning
    uchun ㄹ oxirgi blok tagiga tushadi: 우 + ㄹ = <b>울</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gap nega boshqacha tarjima qilinadi?<br>
     (a) 저는 집에 있을 거예요. &nbsp;(b) 자수르 씨는 집에 있을 거예요.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ega hal qiladi.</strong> (a) — oʻzingiz haqingizda,
    demak <em>reja</em>: “uyda boʻlaman”. (b) — boshqa odam haqida, demak
    <em>taxmin</em>: “Jasur uyda boʻlsa kerak”. Siz uning niyatini bilolmaysiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>살다</b> ni kelasi zamonga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>살 거예요</strong>. Oʻzak allaqachon ㄹ bilan
    tugaydi, shuning uchun yangi ㄹ qoʻshilmaydi — <s>살을 거예요</s> notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     “Ertaga nima qilasiz?” ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>내일 뭐 할 거예요?</strong> Uchta narsa:
    <b>내일</b> (에 olmaydi, PK-14), <b>뭐</b> oʻz oʻrnida (PK-26), va 하다 →
    <b>할 거예요</b>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>(으)ㄹ 거예요</b><span>…aman (kelasi zamon)</span></li>
  <li><b>(으)ㄹ 겁니다</b><span>…aman (rasmiy)</span></li>
  <li><b>갈 거예요</b><span>boraman</span></li>
  <li><b>할 거예요</b><span>qilaman</span></li>
  <li><b>만날 거예요</b><span>uchrataman</span></li>
  <li><b>내일 / 모레</b><span>ertaga / indinga</span></li>
  <li><b>비</b><span>yomgʻir</span></li>
  <li><b>비가 오다</b><span>yomgʻir yogʻmoq</span></li>
  <li><b>계획</b><span>reja</span></li>
  <li><b>아마</b><span>ehtimol</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>받침 <b>yoʻq → ㄹ 거예요</b> (갈), <b>bor → 을 거예요</b> (먹을).</li>
    <li>Oʻzak ㄹ bilan tugasa, <b>yangi ㄹ qoʻshilmaydi</b>: 살 거예요.</li>
    <li>Talaffuz har doim <b>[꺼예요]</b>, yozilishi esa 거예요.</li>
    <li><b>저는 …</b> → reja · <b>그 사람은 …</b> → taxmin.</li>
    <li>Rasmiy shakl — <b>(으)ㄹ 겁니다</b>.</li>
    <li>Oʻzbekcha <em>bormoqchiman</em> ga yaqin: 가요 dan aniqroq niyat.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-28: 동사 + 고 싶다 — xohish bildirish",
        "category": "korean",
        "order": 28,
        "summary": (
            "“…gim keladi” — xohish bildirish. Bitta muhim qoida bor: bu shakl faqat "
            "oʻzingiz va suhbatdoshingiz uchun, uchinchi shaxs uchun boshqasi kerak."
        ),
        "stories": ["저는 한국에 가고 싶어요"],
        "content": """
<h2>PK-28: 동사 + 고 싶다 — xohish bildirish</h2>

<p>PK-27 da <b>rejangizni</b> aytishni oʻrgandingiz. Bugun <b>xohishingizni</b>
aytasiz — bu boshqa narsa: reja amalga oshadi, xohish esa shunchaki istak. Qolip
oddiy, lekin bitta qoida bor va uni koʻpchilik oʻquvchi bilmaydi: koreys tilida
<b>boshqa odamning xohishini</b> aytish uchun boshqa shakl kerak.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>고 싶다 bilan xohish bildirasiz</li>
    <li>Uchinchi shaxs uchun 고 싶어하다 shaklini oʻrganasiz</li>
    <li>Xohishni inkor qilasiz va oʻtgan zamonga oʻtkazasiz</li>
    <li>Oʻzbekcha “…gim keladi” bilan taqqoslaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Xohish</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">고 싶어요</span>
</div>

<h3>1. Shakl — ayri yoʻq</h3>

<p>Bu darsda 받침 muammosi <b>yoʻq</b>: 고 oʻzakka toʻgʻridan-toʻgʻri yopishadi, keyin
싶다 tuslanadi.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Lugʻat</th><th>Oʻzak</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">가다</td><td class="pk-stem">가</td>
      <td class="pk-end">가고 싶어요</td><td class="pk-uz">borgim keladi</td></tr>
  <tr><td class="pk-res">먹다</td><td class="pk-stem">먹</td>
      <td class="pk-end">먹고 싶어요</td><td class="pk-uz">yegim keladi</td></tr>
  <tr><td class="pk-res">배우다</td><td class="pk-stem">배우</td>
      <td class="pk-end">배우고 싶어요</td><td class="pk-uz">oʻrganmoqchiman</td></tr>
  <tr><td class="pk-res">공부하다</td><td class="pk-stem">공부하</td>
      <td class="pk-end">공부하고 싶어요</td><td class="pk-uz">oʻqigim keladi</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
싶다 — sifat, shuning uchun PK-18 qoidasi boʻyicha tuslanadi: oxirgi unli <b>ㅣ</b>,
demak <b>싶어요</b>. Rasmiy shakli — <b>싶습니다</b>.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada xohish uchun ikkita yoʻl bor va ikkalasi ham koreyschaga yaqin:
<br>• <em>bor<b>gim keladi</b></em> — his-tuygʻu, ichki istak
<br>• <em>bor<b>moqchiman</b></em> — niyat
<br>Koreys <b>가고 싶어요</b> birinchisiga yaqinroq: bu <em>istak</em>, hali reja emas.
Reja uchun PK-27 dagi <b>갈 거예요</b> ishlatiladi. Ikkalasini aralashtirmang.</div>

<h3>2. Toʻldiruvchi: 을/를 yoki 이/가</h3>

<p>고 싶다 bilan toʻldiruvchi <b>ikki xil</b> qoʻshimcha olishi mumkin — ikkalasi ham
toʻgʻri:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">물<span class="pe-hl pe-hl--o">을</span> 마시고 싶어요.<br>
     물<span class="pe-hl pe-hl--o">이</span> 마시고 싶어요.</p>
  <p class="pe-ex__uz">Suv ichgim keladi.</p>
  <p class="pe-ex__why">을/를 — odatiy, 이/가 — xohishni biroz kuchaytiradi. Boshlangʻich
     darajada <b>을/를</b> ni ishlating.</p>
</div>

<h3>3. Eng muhim qoida: uchinchi shaxs</h3>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>고 싶다 faqat “men” va “siz” uchun.</b> Boshqa odam haqida gapirsangiz —
<b>고 싶어하다</b> kerak. Sabab mantiqiy: boshqa odamning ichki his-tuygʻusini siz
bilolmaysiz, faqat <em>tashqi belgilarini</em> koʻrasiz.</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Kim haqida</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td class="pk-res">Men (darak)</td><td class="pk-stem">고 싶어요</td>
      <td class="pk-uz">저는 가고 싶어요.</td></tr>
  <tr><td class="pk-res">Siz (savol)</td><td class="pk-stem">고 싶어요?</td>
      <td class="pk-uz">뭐 먹고 싶어요?</td></tr>
  <tr><td class="pk-res">U / boshqa odam</td><td class="pk-end">고 싶어해요</td>
      <td class="pk-uz">자수르 씨는 가고 싶어해요.</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 한국에 가고 싶어요.
     딜노자 씨는 일본에 가고 싶어해요.</p>
  <p class="pe-ex__uz">Men Koreyaga bormoqchiman. Dilnoza esa Yaponiyaga
     bormoqchi.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Boshlangʻich darajada <b>고 싶어해요</b> ni faqat <em>tanib olish</em> kifoya. Oʻzingiz
gapirganda deyarli har doim “men” yoki “siz” haqida gapirasiz, ya'ni <b>고 싶어요</b>
yetadi.</div>

<h3>4. Inkor va oʻtgan zamon</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">Hozirgi</td><td class="pk-stem">가고 싶어요</td>
      <td class="pk-uz">borgim keladi</td></tr>
  <tr><td class="pk-res">Oʻtgan</td><td class="pk-stem">가고 싶었어요</td>
      <td class="pk-uz">borgim kelgan edi</td></tr>
  <tr><td class="pk-res">Inkor</td><td class="pk-stem">가고 싶지 않아요</td>
      <td class="pk-uz">borgim kelmaydi</td></tr>
  <tr><td class="pk-res">Rasmiy</td><td class="pk-stem">가고 싶습니다</td>
      <td class="pk-uz">bormoqchiman (합니다체)</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Tuslanish har doim <b>싶다</b> da boʻladi, feʼlning oʻzida emas:
<s>갔고 싶어요</s> notoʻgʻri, toʻgʻrisi <b>가고 싶었어요</b>. Bu PK-21 dagi 지 않다
bilan bir xil mantiq — oxirgi soʻz tuslanadi.</div>

<h3>5. Savol berish</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 뭐 먹고 싶어요?<br>나: 김치찌개를 먹고 싶어요.</p>
  <p class="pe-ex__uz">A: Nima yegingiz keladi?<br>B: Kimchi-jjigae yegim keladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 어디에 가고 싶어요?<br>나: 서울에 가고 싶어요.</p>
  <p class="pe-ex__uz">A: Qayerga borgingiz keladi?<br>B: Seulga borgim keladi.</p>
  <p class="pe-ex__why">Soʻroq soʻzi oʻz oʻrnida (PK-26), 가다 yoʻnalish bildirgani
     uchun 에.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>갔고 싶어요</s>.</p>
  <p class="pe-good">Tuslanish 싶다 da: <b>가고 싶었어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">자수르 씨는 <s>가고 싶어요</s>.</p>
  <p class="pe-good">Uchinchi shaxs → <b>가고 싶어해요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">공부하다 → <s>공부 고 싶어요</s></p>
  <p class="pe-good">Oʻzak butunligicha: <b>공부하고 싶어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Reja va xohishni aralashtirish.</p>
  <p class="pe-good"><b>갈 거예요</b> — reja (boraman), <b>가고 싶어요</b> — xohish
     (borgim keladi).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>먹다</b> dan “yegim keladi” yasang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>먹고 싶어요</strong>. 고 oʻzakka toʻgʻridan-toʻgʻri
    yopishadi — bu yerda 받침 ayrisi yoʻq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     “Jasur Koreyaga bormoqchi” ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>자수르 씨는 한국에 가고 싶어해요.</strong> Gap
    <em>uchinchi shaxs</em> haqida, shuning uchun <b>고 싶어해요</b>. 고 싶어요 faqat
    “men” va “siz” uchun.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega uchinchi shaxs uchun boshqa shakl kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>boshqa odamning ichki his-tuygʻusini siz
    bilolmaysiz</strong> — faqat tashqi belgilarini koʻrasiz. Koreys tili buni
    grammatikada ajratadi: 싶다 (mening istagim) va 싶어하다 (uning koʻrinib turgan
    istagi).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     “가고 싶어요” ni oʻtgan zamonga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>가고 싶었어요</strong>. Tuslanish <b>싶다</b> da
    boʻladi, feʼlda emas — <s>갔고 싶어요</s> notoʻgʻri. Bu 지 않다 bilan bir xil
    mantiq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     <b>갈 거예요</b> va <b>가고 싶어요</b> farqi nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>갈 거예요</strong> — reja, qaror qilingan
    (“boraman”). <strong>가고 싶어요</strong> — xohish, hali reja emas (“borgim
    keladi”). Oʻzbekchada ham <em>boraman</em> va <em>borgim keladi</em>
    farqlanadi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>고 싶다 / 고 싶어요</b><span>…gim keladi</span></li>
  <li><b>고 싶어하다</b><span>…moqchi (uchinchi shaxs)</span></li>
  <li><b>고 싶었어요</b><span>…gim kelgan edi</span></li>
  <li><b>고 싶지 않아요</b><span>…gim kelmaydi</span></li>
  <li><b>한국 / 일본</b><span>Koreya / Yaponiya</span></li>
  <li><b>서울</b><span>Seul</span></li>
  <li><b>김치찌개</b><span>kimchi-jjigae (taom)</span></li>
  <li><b>물</b><span>suv</span></li>
  <li><b>여행</b><span>sayohat</span></li>
  <li><b>꿈</b><span>orzu</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>oʻzak + 고 싶어요</b> — 받침 ayrisi yoʻq, oddiy yopishadi.</li>
    <li>Tuslanish har doim <b>싶다</b> da: 가고 <b>싶었어요</b>, 가고
        <b>싶지 않아요</b>.</li>
    <li><b>고 싶다</b> — men va siz uchun; <b>고 싶어하다</b> — uchinchi shaxs uchun.</li>
    <li>Sabab: boshqa odamning <b>ichki</b> istagini bilib boʻlmaydi.</li>
    <li>Toʻldiruvchi 을/를 yoki 이/가 olishi mumkin — boshlangʻichda <b>을/를</b>.</li>
    <li><b>갈 거예요</b> = reja · <b>가고 싶어요</b> = xohish.</li>
  </ul>
</div>
""",
    },
]
