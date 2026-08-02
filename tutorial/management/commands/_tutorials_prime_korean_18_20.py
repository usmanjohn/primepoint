# -*- coding: utf-8 -*-
"""Prime Korean — Block B, darslar 18–20 (feʼl tizimi).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_18_20.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_18_20.py --author=prime
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
        "title": "PK-18: Feʼl va sifat + 아/어요 — norasmiy hurmat shakli",
        "category": "korean",
        "order": 18,
        "summary": (
            "Kursning eng muhim darsi. Bitta shakl — 해요체 — darak, savol, iltimos va "
            "taklif uchun birdek ishlaydi, va sifatlar ham xuddi feʼl kabi tuslanadi."
        ),
        "stories": ["저는 매일 공부해요"],
        "content": """
<h2>PK-18: Feʼl va sifat + 아/어요 — norasmiy hurmat shakli</h2>

<p>Shu paytgacha siz feʼllarni <b>tayyor holda</b> yodlab keldingiz: 읽습니다, 마십니다,
공부합니다. Bugun ularning ichini ochamiz. Va bu darsdan keyin sizda <em>istalgan</em>
koreys feʼlini oʻzingiz tuslash imkoni paydo boʻladi — lugʻatdan yangi soʻz topsangiz,
uni darhol gapga qoʻya olasiz. Shuning uchun bu Prime Korean'ning eng muhim darsi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Lugʻat shaklidan oʻzakni (어간) ajratib olasiz</li>
    <li>Unli uygʻunligi boʻyicha 아요 yoki 어요 ni tanlaysiz</li>
    <li>Unli bilan tugagan oʻzaklarning qisqarishini oʻrganasiz</li>
    <li>Sifatlar ham feʼl kabi tuslanishini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch qadam</span>
  <span class="pe-chip pe-chip--s">lugʻat shakli</span>
  <span class="pe-op">−다</span>
  <span class="pe-chip pe-chip--o">oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">아요 / 어요</span>
</div>

<h3>1. Oʻzak — 다 ni olib tashlang</h3>

<p>Lugʻatda har bir feʼl va sifat <b>다</b> bilan tugaydi. Undan oldingi qism —
<b>oʻzak (어간)</b>, va butun koreys grammatikasi shu oʻzakka qoʻshimchalar
yopishtirishdan iborat.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Lugʻat shakli</th><th>Oʻzak</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">먹다</td><td class="pk-stem">먹</td><td class="pk-uz">yemoq</td></tr>
  <tr><td class="pk-res">읽다</td><td class="pk-stem">읽</td><td class="pk-uz">oʻqimoq</td></tr>
  <tr><td class="pk-res">가다</td><td class="pk-stem">가</td><td class="pk-uz">bormoq</td></tr>
  <tr><td class="pk-res">좋다</td><td class="pk-stem">좋</td><td class="pk-uz">yaxshi boʻlmoq</td></tr>
  <tr><td class="pk-res">공부하다</td><td class="pk-stem">공부하</td><td class="pk-uz">oʻqimoq, tahsil olmoq</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu tuzilma sizga tanish: oʻzbekchada ham <em>bor-moq</em> → <em>bor</em> + qoʻshimchalar
(<em>bor<b>aman</b></em>, <em>bor<b>di</b></em>, <em>bor<b>gan</b></em>). Koreys tilida
ham xuddi shunday — <b>oʻzak oʻzgarmaydi, qoʻshimchalar almashadi</b>. Ingliz tilida esa
<em>go / went / gone</em> kabi butun soʻz oʻzgaradi. Yana bir joyda oʻzbek tili sizga
yordam beradi.</div>

<h3>2. Unli uygʻunligi — 아요 yoki 어요?</h3>

<p>Qaysi qoʻshimcha kelishini <b>oʻzakning oxirgi unlisi</b> hal qiladi. Faqat ikkita
holat bor:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">Oxirgi unli ㅏ yoki ㅗ</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-end">아요</span></p>
    <p>먹… yoʻq · 앉<b>아요</b> · 좋<b>아요</b></p>
    <p>살<b>아요</b> · 많<b>아요</b></p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">Boshqa har qanday unli</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-end">어요</span></p>
    <p>먹<b>어요</b> · 읽<b>어요</b></p>
    <p>있<b>어요</b> · 재미있<b>어요</b></p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Uchinchi holat — 하다</span>
<b>하다</b> bilan tugagan har qanday soʻz <b>해요</b> boʻladi. Bu istisno, lekin eng
foydali istisno: koreys tilidagi minglab soʻz 하다 bilan yasaladi.
<br>공부하다 → <b>공부해요</b> · 좋아하다 → <b>좋아해요</b> · 말하다 → <b>말해요</b></div>

<h3>3. Unli bilan tugagan oʻzaklar — qisqarish</h3>

<p>Agar oʻzak <b>unli bilan</b> tugasa, ikkita unli yonma-yon kelib qoladi va ular
qoʻshilib ketadi. Bu yerda yodlash emas, <b>ogʻizga quloq solish</b> kerak:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Oʻzak</th><th>+ qoʻshimcha</th><th>Natija</th><th>Nima boʻldi</th></tr>
  <tr><td class="pk-stem">가</td><td class="pk-end">아요</td><td class="pk-res">가요</td>
      <td class="pk-uz">bir xil unli — bittasi yoʻqoladi</td></tr>
  <tr><td class="pk-stem">서</td><td class="pk-end">어요</td><td class="pk-res">서요</td>
      <td class="pk-uz">bir xil unli — bittasi yoʻqoladi</td></tr>
  <tr><td class="pk-stem">오</td><td class="pk-end">아요</td><td class="pk-res">와요</td>
      <td class="pk-uz">ㅗ + ㅏ = ㅘ</td></tr>
  <tr><td class="pk-stem">보</td><td class="pk-end">아요</td><td class="pk-res">봐요</td>
      <td class="pk-uz">ㅗ + ㅏ = ㅘ</td></tr>
  <tr><td class="pk-stem">주</td><td class="pk-end">어요</td><td class="pk-res">줘요</td>
      <td class="pk-uz">ㅜ + ㅓ = ㅝ</td></tr>
  <tr><td class="pk-stem">배우</td><td class="pk-end">어요</td><td class="pk-res">배워요</td>
      <td class="pk-uz">ㅜ + ㅓ = ㅝ</td></tr>
  <tr><td class="pk-stem">마시</td><td class="pk-end">어요</td><td class="pk-res">마셔요</td>
      <td class="pk-uz">ㅣ + ㅓ = ㅕ</td></tr>
  <tr><td class="pk-stem">기다리</td><td class="pk-end">어요</td><td class="pk-res">기다려요</td>
      <td class="pk-uz">ㅣ + ㅓ = ㅕ</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bu jadvalni yodlamang — <b>PK-3 dagi qoʻshma unlilarni eslang</b>. ㅗ+ㅏ=ㅘ, ㅜ+ㅓ=ㅝ,
ㅣ+ㅓ=ㅕ — bularni allaqachon bilasiz. Bu yerda hech qanday yangi qoida yoʻq, faqat
oʻsha unlilar feʼl ichida uchrashmoqda.</div>

<h3>4. Sifatlar ham xuddi shunday tuslanadi</h3>

<p>Mana koreys tilining eng kutilmagan xususiyati: <b>sifat ham feʼl</b>. U ham 다 bilan
tugaydi, u ham oʻzak oladi, u ham 아/어요 bilan tuslanadi — va u ham
<b>yolgʻiz oʻzi butun gap boʻla oladi</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">좋아요.</p>
  <p class="pe-ex__uz">Yaxshi. / Yaxshi ekan.</p>
  <p class="pe-ex__why">Bitta soʻz — toʻliq gap. Hech qanday “boʻlmoq” kerak emas.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어가 재미있어요.</p>
  <p class="pe-ex__uz">Koreys tili qiziqarli.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada “Ovqat mazali” deyish uchun bogʻlama kerak emas — koreyschada ham shunday,
lekin sabab boshqacha: koreyschada <b>sifat feʼlning oʻzi</b>. Ingliz tilida esa
<em>is</em> majburiy (<em>The food <b>is</b> delicious</em>), shuning uchun ingliz
tilidan oʻrganuvchi 맛있어요 ga ortiqcha 이에요 qoʻshib xato qiladi. Siz bu xatoni
qilmang: <s>맛있이에요</s> emas, shunchaki <b>맛있어요</b>.</div>

<h3>5. 이다 ning 해요체 shakli — 이에요 / 예요</h3>

<p>입니다 ning kundalik shakli — bu yerda 받침 ayrisi ishlaydi:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">ot + <span class="pk-end">이에요</span></p>
    <p>학생<b>이에요</b> · 선생님<b>이에요</b></p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">ot + <span class="pk-end">예요</span></p>
    <p>의사<b>예요</b> · 친구<b>예요</b></p>
  </div>
</div>

<h3>6. Bitta shakl — toʻrt vazifa</h3>

<p>해요체 ning eng qulay tomoni: <b>gap turini ohang hal qiladi</b>, shakl emas.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Vazifa</th><th>Shakl</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">Darak</td><td class="pk-end">가요.</td>
      <td class="pk-uz">Boraman. / Boradi.</td></tr>
  <tr><td class="pk-res">Savol</td><td class="pk-end">가요?</td>
      <td class="pk-uz">Borasizmi?</td></tr>
  <tr><td class="pk-res">Iltimos</td><td class="pk-end">가요.</td>
      <td class="pk-uz">Boring.</td></tr>
  <tr><td class="pk-res">Taklif</td><td class="pk-end">가요!</td>
      <td class="pk-uz">Ketdik!</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 매일 한국어를 공부해요.</p>
  <p class="pe-ex__uz">Men har kuni koreys tilini oʻrganaman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 커피 마셔요?<br>나: 네, 마셔요.</p>
  <p class="pe-ex__uz">A: Kofe ichasizmi?<br>B: Ha, ichaman.</p>
  <p class="pe-ex__why">Bir xil shakl — biri savol, biri javob. Faqat ohang farq
     qiladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">먹다 → <s>먹아요</s></p>
  <p class="pe-good">Oʻzak 먹, oxirgi unli <b>ㅓ</b> — demak <b>먹어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">공부하다 → <s>공부하어요</s></p>
  <p class="pe-good">하다 har doim <b>해요</b>: <b>공부해요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">맛있다 → <s>맛있이에요</s></p>
  <p class="pe-good">Sifat feʼlning oʻzi — bogʻlama kerak emas: <b>맛있어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">의사 <s>이에요</s></p>
  <p class="pe-good">의사 unli bilan tugaydi → 의사<b>예요</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>읽다</b> ni 해요체 ga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>읽어요</strong>. Oʻzak <b>읽</b>, oxirgi unli
    <b>ㅣ</b> — ㅏ ham, ㅗ ham emas, demak <b>어요</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>보다</b> ni 해요체 ga oʻgiring va nega shunday boʻlishini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>봐요</strong>. Oʻzak <b>보</b>, oxirgi unli ㅗ →
    <b>아요</b>. Lekin oʻzak unli bilan tugagani uchun ikkita unli qoʻshiladi:
    <b>ㅗ + ㅏ = ㅘ</b>. PK-3 dagi qoʻshma unli.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega "맛있이에요" notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>맛있다 — sifat, ya'ni feʼlning
    oʻzi</strong>. Unga bogʻlama (이에요) qoʻshish kerak emas — u oʻzi tuslanadi:
    <b>맛있어요</b>. Bu ingliz tilidan oʻrganuvchining eng koʻp qiladigan
    xatosi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga nima tushadi? 저는 학생<span class="pe-blank">?</span> (해요체)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>이에요</strong> — 학생 받침 (ㅇ) bilan tugaydi.
    Agar 의사 boʻlganida <b>예요</b> boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Afsona "저는 커피를 마시어요" dedi. Toʻgʻrilang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>마셔요</strong>. Oʻzak <b>마시</b> unli (ㅣ) bilan
    tugaydi, shuning uchun 어요 bilan qoʻshilib qisqaradi: <b>ㅣ + ㅓ = ㅕ</b>. Toʻgʻrisi:
    <b>저는 커피를 마셔요.</b></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>어간</b><span>oʻzak</span></li>
  <li><b>가요 / 와요</b><span>boraman / kelaman</span></li>
  <li><b>먹어요 / 마셔요</b><span>yeyman / ichaman</span></li>
  <li><b>봐요 / 읽어요</b><span>koʻraman / oʻqiyman</span></li>
  <li><b>배워요</b><span>oʻrganaman</span></li>
  <li><b>공부해요</b><span>tahsil olaman</span></li>
  <li><b>좋아요</b><span>yaxshi</span></li>
  <li><b>재미있어요</b><span>qiziqarli</span></li>
  <li><b>맛있어요</b><span>mazali</span></li>
  <li><b>이에요 / 예요</b><span>…dir (kundalik)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>다 ni olib tashlang</b> → oʻzak qoladi. Qolgan hamma narsa shunga
        yopishadi.</li>
    <li>Oxirgi unli <b>ㅏ yoki ㅗ → 아요</b>, boshqa hamma holatda <b>어요</b>.</li>
    <li><b>하다 → 해요.</b> Minglab soʻz shu qoidaga kiradi.</li>
    <li>Oʻzak unli bilan tugasa qisqaradi: 보+아요 = <b>봐요</b>, 마시+어요 =
        <b>마셔요</b>.</li>
    <li><b>Sifat ham feʼl</b> — bogʻlama kerak emas: 좋아요, 맛있어요.</li>
    <li>이다 → <b>이에요 / 예요</b> (받침 ayrisi).</li>
    <li>Bitta shakl — darak, savol, iltimos, taklif. <b>Ohang hal qiladi.</b></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-19: Feʼl va sifat + ㅂ니다/습니다 — rasmiy shakl",
        "category": "korean",
        "order": 19,
        "summary": (
            "합니다체 — rasmiy daraja. Bu safar unli uygʻunligi emas, 받침 ayrisi "
            "ishlaydi, shuning uchun u 해요체 dan ancha oson."
        ),
        "stories": ["자기소개를 합니다"],
        "content": """
<h2>PK-19: Feʼl va sifat + ㅂ니다/습니다 — rasmiy shakl</h2>

<p>Siz bu shaklni allaqachon ishlatib kelyapsiz: <b>입니다</b>, <b>있습니다</b>,
<b>감사합니다</b>. Bugun ularning ortidagi qoidani koʻramiz — va yaxshi xabar shuki,
bu qoida <b>PK-18 dagidan ancha oson</b>. Unli uygʻunligi ham, qisqarish ham yoʻq:
faqat 받침 bor-yoʻqligiga qaraysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ㅂ니다 va 습니다 ni 받침 boʻyicha tanlaysiz</li>
    <li>ㅂ니까? bilan rasmiy savol berasiz</li>
    <li>ㄹ oʻzaklarning oʻziga xosligini bilib olasiz</li>
    <li>합니다체 va 해요체 ni qachon ishlatishni ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">받침 ayrisi</span>
  <span class="pe-chip pe-chip--s">unli bilan tugasa → ㅂ니다</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">undosh bilan tugasa → 습니다</span>
</div>

<h3>1. Qoida</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">Oʻzak 받침siz</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-end">ㅂ니다</span></p>
    <p>가 → 갑<b>니다</b> · 오 → 옵<b>니다</b></p>
    <p>보 → 봅<b>니다</b> · 마시 → 마십<b>니다</b></p>
  </div>
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">Oʻzak 받침li</p>
    <p class="pk-batchim__form">oʻzak + <span class="pk-end">습니다</span></p>
    <p>먹 → 먹<b>습니다</b> · 읽 → 읽<b>습니다</b></p>
    <p>좋 → 좋<b>습니다</b> · 있 → 있<b>습니다</b></p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Diqqat qiling: <b>ㅂ니다</b> dagi ㅂ oʻzakning <em>tagiga</em> 받침 boʻlib tushadi —
가 + ㅂ니다 = <b>갑니다</b>, 마시 + ㅂ니다 = <b>마십니다</b>. Bu qoʻshimcha emas, blokka
qoʻshiladigan harf.</div>

<h3>2. Talaffuz — yana 비음화</h3>

<div class="pk-say">
  <span class="pk-say__from">갑니다</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[감니다]</span>
  <span class="pk-say__why">ㅂ + ㄴ → ㅁ</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">먹습니다</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[먹씀니다]</span>
  <span class="pk-say__why">경음화 + 비음화 birga</span>
</div>

<p>PK-8 dagi qoidalar bu yerda har bir gapda ishlaydi. <b>-ㅂ니다</b> hech qachon
"p-ni-da" deb aytilmaydi — har doim <b>[m-ni-da]</b>.</p>

<h3>3. Rasmiy savol: ㅂ니까? / 습니까?</h3>

<p>다 ni <b>까</b> ga almashtirasiz — xuddi 입니다 → 입니까 kabi (PK-10):</p>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 한국어를 공부합니까?<br>나: 네, 공부합니다.</p>
  <p class="pe-ex__uz">A: Koreys tilini oʻrganasizmi?<br>B: Ha, oʻrganaman.</p>
</div>

<h3>4. ㄹ oʻzaklar — bitta istisno</h3>

<p>Agar oʻzak <b>ㄹ</b> bilan tugasa, ㄹ <b>tushib qoladi</b> va ㅂ니다 qoʻshiladi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Lugʻat shakli</th><th>Oʻzak</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">살다</td><td class="pk-stem">살</td><td class="pk-end">삽니다</td>
      <td class="pk-uz">yashayman</td></tr>
  <tr><td class="pk-res">알다</td><td class="pk-stem">알</td><td class="pk-end">압니다</td>
      <td class="pk-uz">bilaman</td></tr>
  <tr><td class="pk-res">만들다</td><td class="pk-stem">만들</td><td class="pk-end">만듭니다</td>
      <td class="pk-uz">yasayman</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>ㄹ 받침 hisoblanmaydi</b> — shuning uchun 살다 → <s>살습니다</s> emas, <b>삽니다</b>.
해요체 da esa ㄹ joyida qoladi: 살<b>아요</b>. Bu qoidani PK-32 da toʻliq koʻramiz;
hozircha shu uch soʻzni eslab qoling.</div>

<h3>5. Sifatlar ham xuddi shunday</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">한국어가 재미있습니다.</p>
  <p class="pe-ex__uz">Koreys tili qiziqarli.</p>
  <p class="pe-ex__why">재미있 받침li → <b>습니다</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">날씨가 좋습니다.</p>
  <p class="pe-ex__uz">Havo yaxshi.</p>
</div>

<h3>6. Qaysi birini qachon</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">합니다체</p>
    <p>Yangiliklar, taqdimot, xizmat sohasi, armiya, rasmiy xat.</p>
    <p>Sovuqroq, masofali, professional.</p>
    <p><b>공부합니다</b></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">해요체</p>
    <p>Kundalik hayot — doʻkon, sinf, qoʻshni, doʻstlar.</p>
    <p>Muloyim va iliq. <b>Eng koʻp ishlatiladigan.</b></p>
    <p><b>공부해요</b></p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Farqni oʻzbekcha bilan tasavvur qiling: <em>“Hurmatli mehmonlar, marhamat”</em> va
<em>“Keling, oʻtiring”</em> — ikkalasi ham hurmatli, lekin biri rasmiy tadbir uchun,
ikkinchisi kundalik. 합니다체 birinchisiga, 해요체 ikkinchisiga toʻgʻri keladi.
Ikkalasi ham <b>존댓말</b> (PK-11).</div>

<h3>7. Yonma-yon</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Lugʻat</th><th>해요체</th><th>합니다체</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">가다</td><td class="pk-res">가요</td><td class="pk-end">갑니다</td>
      <td class="pk-uz">boraman</td></tr>
  <tr><td class="pk-stem">먹다</td><td class="pk-res">먹어요</td><td class="pk-end">먹습니다</td>
      <td class="pk-uz">yeyman</td></tr>
  <tr><td class="pk-stem">마시다</td><td class="pk-res">마셔요</td><td class="pk-end">마십니다</td>
      <td class="pk-uz">ichaman</td></tr>
  <tr><td class="pk-stem">공부하다</td><td class="pk-res">공부해요</td><td class="pk-end">공부합니다</td>
      <td class="pk-uz">oʻqiyman</td></tr>
  <tr><td class="pk-stem">좋다</td><td class="pk-res">좋아요</td><td class="pk-end">좋습니다</td>
      <td class="pk-uz">yaxshi</td></tr>
  <tr><td class="pk-stem">이다</td><td class="pk-res">이에요/예요</td><td class="pk-end">입니다</td>
      <td class="pk-uz">…dir</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">가다 → <s>가습니다</s></p>
  <p class="pe-good">가 받침siz → <b>갑니다</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">먹다 → <s>먹ㅂ니다</s></p>
  <p class="pe-good">먹 받침li → <b>먹습니다</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">살다 → <s>살습니다</s></p>
  <p class="pe-good">ㄹ tushadi: <b>삽니다</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">갑니다 ni "kap-ni-da" deb oʻqish.</p>
  <p class="pe-good">비음화: <b>[감니다]</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>읽다</b> ni 합니다체 ga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>읽습니다</strong>. Oʻzak <b>읽</b> 받침li (ㄺ) →
    <b>습니다</b>. Oʻqilishi [익씀니다].</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>마시다</b> ni 합니다체 ga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>마십니다</strong>. Oʻzak <b>마시</b> unli bilan
    tugaydi → ㅂ니다, va ㅂ oʻzakning oxirgi bloki tagiga tushadi: 시 + ㅂ =
    <b>십</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega 살다 → 삽니다, 살습니다 emas?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>ㄹ 받침 hisoblanmaydi</strong> — ㅂ니다
    oldidan u tushib qoladi. Shuning uchun 살 → 사 + ㅂ니다 = <b>삽니다</b>. 해요체 da esa
    ㄹ qoladi: <b>살아요</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Doʻkonda ishlaysiz va mijozga gapiryapsiz. Qaysi daraja mos?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>합니다체</strong> — xizmat sohasida professional
    masofa saqlanadi. Shuning uchun doʻkonda <em>어서 오세요, 감사합니다</em> kabi rasmiy
    shakllarni eshitasiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Jasur "저는 한국에 살습니다" dedi. Ikkita narsani tekshiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Feʼl xato: <strong>살습니다 → 삽니다</strong> (ㄹ tushadi).
    Qoʻshimcha esa toʻgʻri — 살다 “yashamoq” holatni bildiradi, shuning uchun
    <b>에</b> ishlatiladi (PK-14), 에서 emas. Toʻgʻrisi:
    <b>저는 한국에 삽니다.</b></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>갑니다 / 옵니다</b><span>boraman / kelaman</span></li>
  <li><b>먹습니다 / 마십니다</b><span>yeyman / ichaman</span></li>
  <li><b>읽습니다 / 봅니다</b><span>oʻqiyman / koʻraman</span></li>
  <li><b>삽니다</b><span>yashayman</span></li>
  <li><b>압니다</b><span>bilaman</span></li>
  <li><b>좋습니다</b><span>yaxshi</span></li>
  <li><b>재미있습니다</b><span>qiziqarli</span></li>
  <li><b>날씨</b><span>havo, ob-havo</span></li>
  <li><b>매일</b><span>har kuni</span></li>
  <li><b>자기소개</b><span>oʻzini tanishtirish</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>Oʻzak <b>받침siz → ㅂ니다</b>, <b>받침li → 습니다</b>. Unli uygʻunligi yoʻq.</li>
    <li>ㅂ oʻzakning oxirgi bloki <b>tagiga tushadi</b>: 마시 → 마십니다.</li>
    <li>Savol: <b>다 → 까</b>. 갑니까? 먹습니까?</li>
    <li><b>ㄹ tushadi</b>: 살다 → 삽니다, 알다 → 압니다.</li>
    <li>Talaffuz har doim <b>[ㅁ니다]</b> — 비음화.</li>
    <li><b>합니다체</b> rasmiy, <b>해요체</b> kundalik. Ikkalasi ham 존댓말.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-20: Oʻtgan zamon: 았/었어요",
        "category": "korean",
        "order": 20,
        "summary": (
            "Oʻtgan zamon uchun yangi qoida yoʻq — PK-18 dagi 아/어요 ni yasang, "
            "keyin ㅆ qoʻshing. Bir qadam, tamom."
        ),
        "stories": ["어제 무엇을 했어요?"],
        "content": """
<h2>PK-20: Oʻtgan zamon: 았/었어요</h2>

<p>Bu dars sizga sovgʻa: <b>yangi qoida yoʻq</b>. PK-18 da 아/어요 ni yasashni
oʻrgangansiz — oʻtgan zamon uchun oʻsha ishni qilib, oxiriga bitta harf qoʻshasiz,
tamom. Shuning uchun PK-18 kursning kaliti edi: bir marta oʻrgansangiz, undan keyingi
oʻnlab shakl shu asosga quriladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>았어요 / 었어요 / 했어요 shakllarini yasaysiz</li>
    <li>Qisqargan oʻzaklarda oʻtgan zamonni toʻgʻri tuzasiz</li>
    <li>Rasmiy oʻtgan zamonni — 았/었습니다 ni bilasiz</li>
    <li>이다 ning oʻtgan shaklini oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta qoʻshimcha qadam</span>
  <span class="pe-chip pe-chip--s">아/어요 shakli</span>
  <span class="pe-op">→ 요 ni olib, + ㅆ어요</span>
  <span class="pe-chip pe-chip--v">았/었어요</span>
</div>

<h3>1. Eng oson yoʻl</h3>

<p>Oʻtgan zamonni yasashning eng ishonchli usuli — <b>hozirgi shakldan boshlash</b>:</p>

<ol class="pe-steps">
  <li>Avval 해요체 ni yasang: 먹다 → <b>먹어요</b></li>
  <li>Oxiridagi <b>요</b> ni olib tashlang: 먹어</li>
  <li>Oxiriga <b>ㅆ어요</b> qoʻshing: <b>먹었어요</b></li>
</ol>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Lugʻat</th><th>Hozirgi</th><th>Oʻtgan</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">먹다</td><td class="pk-res">먹어요</td><td class="pk-end">먹었어요</td>
      <td class="pk-uz">yedim</td></tr>
  <tr><td class="pk-stem">읽다</td><td class="pk-res">읽어요</td><td class="pk-end">읽었어요</td>
      <td class="pk-uz">oʻqidim</td></tr>
  <tr><td class="pk-stem">앉다</td><td class="pk-res">앉아요</td><td class="pk-end">앉았어요</td>
      <td class="pk-uz">oʻtirdim</td></tr>
  <tr><td class="pk-stem">좋다</td><td class="pk-res">좋아요</td><td class="pk-end">좋았어요</td>
      <td class="pk-uz">yaxshi edi</td></tr>
  <tr><td class="pk-stem">가다</td><td class="pk-res">가요</td><td class="pk-end">갔어요</td>
      <td class="pk-uz">bordim</td></tr>
  <tr><td class="pk-stem">보다</td><td class="pk-res">봐요</td><td class="pk-end">봤어요</td>
      <td class="pk-uz">koʻrdim</td></tr>
  <tr><td class="pk-stem">마시다</td><td class="pk-res">마셔요</td><td class="pk-end">마셨어요</td>
      <td class="pk-uz">ichdim</td></tr>
  <tr><td class="pk-stem">배우다</td><td class="pk-res">배워요</td><td class="pk-end">배웠어요</td>
      <td class="pk-uz">oʻrgandim</td></tr>
  <tr><td class="pk-stem">하다</td><td class="pk-res">해요</td><td class="pk-end">했어요</td>
      <td class="pk-uz">qildim</td></tr>
  <tr><td class="pk-stem">공부하다</td><td class="pk-res">공부해요</td><td class="pk-end">공부했어요</td>
      <td class="pk-uz">oʻqidim</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Qisqargan shakllarga alohida qoida <b>kerak emas</b> — 봐요 dan 봤어요 hosil boʻladi,
마셔요 dan 마셨어요. ㅆ shunchaki mavjud blokning tagiga 받침 boʻlib tushadi. Shuning
uchun "avval hozirgi shaklni yasang" usuli har doim ishlaydi.</div>

<h3>2. Oʻzbekcha bilan solishtiring</h3>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada oʻtgan zamon ham <b>oʻzakka qoʻshiladigan qoʻshimcha</b>:
<em>bor</em> → <em>bor<b>dim</b></em>, <em>yoz</em> → <em>yoz<b>dim</b></em>.
Koreysda ham xuddi shunday: 먹 → 먹<b>었어요</b>. Ingliz tilida esa yarim feʼllar
notoʻgʻri (<em>go → went</em>, <em>eat → ate</em>) va ularni alohida yodlash kerak.
Koreysda bunday roʻyxat <b>yoʻq</b> — qoida hamma feʼlga bir xil ishlaydi.</div>

<h3>3. Rasmiy oʻtgan zamon: 았/었습니다</h3>

<p>합니다체 da ham xuddi shu ㅆ ishlatiladi, faqat oxiri boshqacha:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>해요체 (oʻtgan)</th><th>합니다체 (oʻtgan)</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-res">먹었어요</td><td class="pk-end">먹었습니다</td>
      <td class="pk-uz">yedim</td></tr>
  <tr><td class="pk-res">갔어요</td><td class="pk-end">갔습니다</td>
      <td class="pk-uz">bordim</td></tr>
  <tr><td class="pk-res">했어요</td><td class="pk-end">했습니다</td>
      <td class="pk-uz">qildim</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Oʻtgan zamon oʻzagi (먹었, 갔, 했) <b>har doim 받침li</b> — chunki oxirida ㅆ turibdi.
Shuning uchun rasmiy shaklda har doim <b>습니다</b>, hech qachon ㅂ니다 emas.</div>

<h3>4. 이다 ning oʻtgan shakli</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">ot + <span class="pk-end">이었어요</span></p>
    <p>학생<b>이었어요</b> — talaba edim</p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">ot + <span class="pk-end">였어요</span></p>
    <p>의사<b>였어요</b> — shifokor edim</p>
  </div>
</div>

<p>있다 va 없다 ham oddiy qoidaga boʻysunadi: <b>있었어요</b> (bor edi),
<b>없었어요</b> (yoʻq edi).</p>

<h3>5. Vaqt soʻzlari bilan</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 저는 친구를 만났어요.</p>
  <p class="pe-ex__uz">Kecha men doʻstimni uchratdim.</p>
  <p class="pe-ex__why">어제 — 에 olmaydi (PK-14).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">아침에 집에서 우유를 마셨어요.</p>
  <p class="pe-ex__uz">Ertalab uyda sut ichdim.</p>
  <p class="pe-ex__why">아침 — 에 oladi. 마시다 harakat feʼli — joy <b>에서</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 어제 무엇을 했어요?<br>나: 한국어를 공부했어요.</p>
  <p class="pe-ex__uz">A: Kecha nima qildingiz?<br>B: Koreys tilini oʻrgandim.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">먹다 → <s>먹았어요</s></p>
  <p class="pe-good">Avval 먹<b>어</b>요 → shuning uchun <b>먹었어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">하다 → <s>하었어요</s></p>
  <p class="pe-good">해요 dan boshlang → <b>했어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">갔다 → <s>갔ㅂ니다</s></p>
  <p class="pe-good">Oʻtgan oʻzak har doim 받침li → <b>갔습니다</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>어제에</s> 친구를 만났어요.</p>
  <p class="pe-good">어제, 오늘, 내일 — <b>에</b> olmaydi: <b>어제</b> 만났어요.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>읽다</b> ni oʻtgan zamonga (해요체) oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>읽었어요</strong>. Avval hozirgi shakl —
    <b>읽어요</b>; 요 ni olib, ㅆ어요 qoʻshamiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>보다</b> ni oʻtgan zamonga oʻgiring va qadamlarni koʻrsating.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>봤어요</strong>. Qadamlar: 보다 → <b>봐요</b>
    (ㅗ+ㅏ=ㅘ) → 요 ni olamiz (봐) → ㅆ어요 qoʻshamiz = <b>봤어요</b>. Qisqargan
    shaklga alohida qoida kerak emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega oʻtgan zamonda har doim <b>습니다</b> boʻladi, ㅂ니다 emas?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki oʻtgan zamon oʻzagi oxirida <strong>ㅆ 받침</strong>
    turadi — 갔, 먹었, 했. 받침li oʻzak esa har doim <b>습니다</b> oladi (PK-19).
    Shuning uchun <b>갔습니다</b>, hech qachon 갔ㅂ니다 emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     "Kecha nima qildingiz?" ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>어제 무엇을 했어요?</strong> Uchta narsa:
    <b>어제</b> (에 olmaydi), <b>무엇을</b> (toʻldiruvchi — PK-17), va
    <b>했어요</b> (하다 → 해요 → 했어요).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Dilnoza "저는 어제에 학교에 갔어요" dedi. Xatoni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>어제에 → 어제.</strong> 오늘, 어제, 내일 hech
    qachon 에 olmaydi (PK-14). Qolgani toʻgʻri: <b>학교에</b> — 가다 yoʻnalish
    bildirgani uchun 에, va <b>갔어요</b> — 가요 dan yasalgan oʻtgan zamon. Toʻgʻrisi:
    <b>저는 어제 학교에 갔어요.</b></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>했어요</b><span>qildim</span></li>
  <li><b>갔어요 / 왔어요</b><span>bordim / keldim</span></li>
  <li><b>먹었어요 / 마셨어요</b><span>yedim / ichdim</span></li>
  <li><b>봤어요 / 읽었어요</b><span>koʻrdim / oʻqidim</span></li>
  <li><b>배웠어요</b><span>oʻrgandim</span></li>
  <li><b>만났어요</b><span>uchratdim</span></li>
  <li><b>있었어요 / 없었어요</b><span>bor edi / yoʻq edi</span></li>
  <li><b>이었어요 / 였어요</b><span>…edi</span></li>
  <li><b>어제</b><span>kecha</span></li>
  <li><b>주말</b><span>dam olish kuni</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>Yangi qoida yoʻq</b>: 아/어요 ni yasang → 요 ni oling → <b>ㅆ어요</b>
        qoʻshing.</li>
    <li>Qisqargan shakllar oʻz-oʻzidan ishlaydi: 봐요 → <b>봤어요</b>, 마셔요 →
        <b>마셨어요</b>.</li>
    <li><b>하다 → 했어요.</b> Yana minglab soʻz shu qoidada.</li>
    <li>Rasmiy shaklda har doim <b>았/었습니다</b> — oʻzak ㅆ bilan tugagani uchun.</li>
    <li>이다 → <b>이었어요 / 였어요</b> (받침 ayrisi).</li>
    <li>Oʻzbekcha kabi — oʻzak oʻzgarmaydi, qoʻshimcha almashadi. Notoʻgʻri feʼllar
        roʻyxati <b>yoʻq</b>.</li>
  </ul>
</div>
""",
    },
]
