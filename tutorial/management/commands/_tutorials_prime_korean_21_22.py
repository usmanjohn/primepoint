# -*- coding: utf-8 -*-
"""Prime Korean — Block B yakuni, darslar 21–22 (inkor).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_21_22.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_21_22.py --author=prime
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
        "title": "PK-21: Inkor 1: 안 + feʼl va 지 않다",
        "category": "korean",
        "order": 21,
        "summary": (
            "Koreys tilida inkorning ikki yoʻli bor — biri feʼl oldiga, ikkinchisi "
            "oxiriga qoʻshiladi. Va uchta soʻz umuman inkor qoʻshimchasini olmaydi."
        ),
        "stories": ["저는 커피를 안 마셔요"],
        "content": """
<h2>PK-21: Inkor 1: 안 + feʼl va 지 않다</h2>

<p>Endi siz gap tuza olasiz — bugun ularni <b>inkor qilishni</b> oʻrganamiz. Koreys
tilida buning ikki yoʻli bor: biri qisqa va ogʻzaki, ikkinchisi uzunroq va yozmaroq.
Ikkalasining maʼnosi <em>bir xil</em>, shuning uchun tanlash erkin. Lekin uchta soʻz
bor — ular bu qoidalarga umuman boʻysunmaydi, va aynan shu uchtasi eng koʻp
ishlatiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>안 + feʼl bilan qisqa inkor yasaysiz</li>
    <li>지 않다 bilan uzun inkor yasaysiz</li>
    <li>하다 feʼllarining oʻziga xosligini bilib olasiz</li>
    <li>있다 → 없다, 알다 → 모르다 juftliklarini eslab qolasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki yoʻl, bitta maʼno</span>
  <span class="pe-chip pe-chip--neg">안 + feʼl</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--neg">oʻzak + 지 않다</span>
</div>

<h3>1. Qisqa inkor: 안</h3>

<p><b>안</b> feʼlning <em>oldiga</em> alohida soʻz boʻlib qoʻyiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 커피를 <span class="pe-hl pe-hl--neg">안</span> 마셔요.</p>
  <p class="pe-ex__uz">Men kofe ichmayman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">오늘은 학교에 <span class="pe-hl pe-hl--neg">안</span> 가요.</p>
  <p class="pe-ex__uz">Bugun maktabga bormayman.</p>
  <p class="pe-ex__why">오늘<b>은</b> — qiyoslash soyasi bor: “bugun esa” (PK-12).</p>
</div>

<p>Sifatlar bilan ham ishlaydi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">날씨가 안 좋아요.</p>
  <p class="pe-ex__uz">Havo yaxshi emas.</p>
</div>

<h3>2. Uzun inkor: 지 않다</h3>

<p>Bu safar qoʻshimcha <b>oʻzakka</b> yopishadi — va u ham oddiy feʼl kabi tuslanadi:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Lugʻat</th><th>Oʻzak</th><th>+ 지 않다</th><th>해요체</th></tr>
  <tr><td class="pk-res">먹다</td><td class="pk-stem">먹</td>
      <td class="pk-end">먹지 않다</td><td class="pk-uz">먹지 않아요</td></tr>
  <tr><td class="pk-res">가다</td><td class="pk-stem">가</td>
      <td class="pk-end">가지 않다</td><td class="pk-uz">가지 않아요</td></tr>
  <tr><td class="pk-res">마시다</td><td class="pk-stem">마시</td>
      <td class="pk-end">마시지 않다</td><td class="pk-uz">마시지 않아요</td></tr>
  <tr><td class="pk-res">좋다</td><td class="pk-stem">좋</td>
      <td class="pk-end">좋지 않다</td><td class="pk-uz">좋지 않아요</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>지 않다</b> ni yodlash oson: oʻzak oʻzgarmaydi, 지 않 qoʻshiladi, keyin 않다 ning
oʻzi PK-18 qoidasi boʻyicha tuslanadi — oxirgi unli <b>ㅏ</b>, demak
<b>않아요</b>. Har doim shunday.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada inkor <b>qoʻshimcha</b> bilan beriladi: <em>bor<b>ma</b>yman</em>,
<em>ich<b>ma</b>yman</em>. Shuning uchun <b>지 않다</b> sizga tabiiyroq tuyuladi — u ham
oʻzakka yopishadi. <b>안</b> esa alohida soʻz, ya'ni oʻzbekchada ekvivalenti yoʻq. Lekin
ogʻzaki nutqda koreyslar aynan <b>안</b> ni koʻproq ishlatadi, shuning uchun ikkalasini
ham bilish kerak.</div>

<h3>3. Qaysi birini qachon</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">안 — qisqa</p>
    <p>Kundalik nutq, tez javob, ogʻzaki suhbat.</p>
    <p><b>안 가요.</b></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">지 않다 — uzun</p>
    <p>Yozma matn, rasmiy uslub, biroz taʼkidli.</p>
    <p><b>가지 않아요.</b></p>
  </div>
</div>

<p>Maʼno farqi yoʻq — ikkalasi ham “bormayman”. Boshlangʻich darajada
<b>안</b> ni ishlating, <b>지 않다</b> ni esa oʻqiganda tanib oling.</p>

<h3>4. 하다 feʼllari — 안 oʻrtaga tushadi</h3>

<p>Mana darsning eng koʻp xato qilinadigan joyi. <b>Ot + 하다</b> tuzilishidagi
feʼllarda 안 <em>butun soʻz oldiga emas</em>, <b>하다 ning oldiga</b> qoʻyiladi:</p>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>안 공부해요</s>.</p>
  <p class="pe-good">저는 <b>공부 안 해요</b>.</p>
</div>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Feʼl</th><th>안 bilan</th><th>지 않다 bilan</th></tr>
  <tr><td class="pk-stem">공부하다</td><td class="pk-res">공부 안 해요</td>
      <td class="pk-end">공부하지 않아요</td></tr>
  <tr><td class="pk-stem">일하다</td><td class="pk-res">일 안 해요</td>
      <td class="pk-end">일하지 않아요</td></tr>
  <tr><td class="pk-stem">말하다</td><td class="pk-res">말 안 해요</td>
      <td class="pk-end">말하지 않아요</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Sabab oddiy: 공부하다 aslida <b>공부</b> (ot) + <b>하다</b> (qilmoq) — ya'ni “tahsilni
qilmoq”. 안 esa har doim <em>feʼlning</em> oldiga tushadi, ot oldiga emas. Diqqat:
<b>지 않다</b> bunday boʻlinmaydi — u har doim butun oʻzakka yopishadi.</div>

<h3>5. Uchta istisno — inkor qoʻshimchasi olmaydiganlar</h3>

<p>Koreys tilida uchta juda muhim soʻz bor: ularning inkori <b>alohida soʻz</b>, va siz
ularni allaqachon bilasiz.</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Tasdiq</th><th>Inkor</th><th>Maʼnosi</th><th>Notoʻgʻri</th></tr>
  <tr><td class="pk-stem">있다</td><td class="pk-end">없다</td>
      <td class="pk-uz">bor → yoʻq</td><td class="pk-uz">✗ 안 있다</td></tr>
  <tr><td class="pk-stem">알다</td><td class="pk-end">모르다</td>
      <td class="pk-uz">bilmoq → bilmaslik</td><td class="pk-uz">✗ 안 알다</td></tr>
  <tr><td class="pk-stem">이다</td><td class="pk-end">이/가 아니다</td>
      <td class="pk-uz">…dir → …emas</td><td class="pk-uz">✗ 안 이다</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 시간이 없어요.</p>
  <p class="pe-ex__uz">Menda vaqt yoʻq.</p>
  <p class="pe-ex__why">PK-13 dan tanish — endi bilasizki, bu 있다 ning inkori.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 그 사람을 몰라요.</p>
  <p class="pe-ex__uz">Men u odamni bilmayman.</p>
  <p class="pe-ex__why">모르다 → 몰라요. Bu tuslanish PK-47 mavzusi; hozircha
     shakl sifatida yodlang.</p>
</div>

<h3>6. Oʻtgan zamon va rasmiy shakl</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>안 bilan</th><th>지 않다 bilan</th></tr>
  <tr><td class="pk-res">Hozirgi (해요체)</td><td class="pk-stem">안 먹어요</td>
      <td class="pk-end">먹지 않아요</td></tr>
  <tr><td class="pk-res">Oʻtgan (해요체)</td><td class="pk-stem">안 먹었어요</td>
      <td class="pk-end">먹지 않았어요</td></tr>
  <tr><td class="pk-res">Hozirgi (합니다체)</td><td class="pk-stem">안 먹습니다</td>
      <td class="pk-end">먹지 않습니다</td></tr>
</table></div>

<p>Diqqat qiling: <b>안</b> hech qachon oʻzgarmaydi — tuslanadigan narsa feʼlning
oʻzi. <b>지 않다</b> da esa tuslanadigan narsa <b>않다</b>.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>안 공부해요</s>.</p>
  <p class="pe-good">하다 feʼllarida 안 oʻrtaga: <b>공부 안 해요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">시간이 <s>안 있어요</s>.</p>
  <p class="pe-good">있다 ning inkori — alohida soʻz: 시간이 <b>없어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>안 알아요</s>.</p>
  <p class="pe-good">알다 ning inkori — <b>몰라요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 학생 <s>안 이에요</s>.</p>
  <p class="pe-good">이다 ning inkori: 학생<b>이 아니에요</b> (PK-10).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     "저는 커피를 마셔요" ni ikki xil usulda inkor qiling.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>저는 커피를 안 마셔요.</strong> (qisqa) va
    <strong>저는 커피를 마시지 않아요.</strong> (uzun). Maʼnosi bir xil — “kofe
    ichmayman”.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Nega "안 공부해요" notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki 공부하다 = <strong>공부</strong> (ot) +
    <strong>하다</strong> (feʼl), va 안 har doim <em>feʼlning</em> oldiga tushadi.
    Toʻgʻrisi: <b>공부 안 해요</b>. Uzun shakl esa boʻlinmaydi:
    <b>공부하지 않아요</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>있다</b> ning inkori nima va nega "안 있다" notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>없다</strong>. Koreys tilida uchta soʻzning
    inkori alohida soʻz bilan beriladi: 있다 → 없다, 알다 → 모르다, 이다 → 아니다. Siz
    ularning ikkitasini allaqachon PK-10 va PK-13 da koʻrgansiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     "먹지 않다" ni 해요체 ga oʻgiring va nega shunday boʻlishini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>먹지 않아요</strong>. Tuslanadigan narsa —
    <b>않다</b>, va uning oxirgi unlisi <b>ㅏ</b>, demak PK-18 qoidasi boʻyicha
    <b>아요</b>. Shuning uchun 지 않다 har doim <b>지 않아요</b> boʻladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bekzod "저는 어제 일 안 했어요" dedi. Toʻgʻrimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Toʻliq toʻgʻri.</strong> 일하다 — ot (일) + 하다,
    shuning uchun 안 oʻrtaga tushdi: <b>일 안 했어요</b> (“ishlamadim”). Oʻtgan zamon
    esa feʼlning oʻzida — 했어요. Uzun shakli: <b>일하지 않았어요</b>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>안</b><span>…ma (qisqa inkor)</span></li>
  <li><b>지 않다</b><span>…ma (uzun inkor)</span></li>
  <li><b>없다</b><span>yoʻq (있다 ning inkori)</span></li>
  <li><b>모르다 / 몰라요</b><span>bilmaslik</span></li>
  <li><b>아니다</b><span>…emas</span></li>
  <li><b>일하다</b><span>ishlamoq</span></li>
  <li><b>말하다</b><span>gapirmoq</span></li>
  <li><b>날씨</b><span>havo</span></li>
  <li><b>오늘은</b><span>bugun esa</span></li>
  <li><b>안 좋아요</b><span>yaxshi emas</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>안 + feʼl</b> = <b>oʻzak + 지 않다</b>. Maʼnosi bir xil.</li>
    <li><b>안</b> — ogʻzaki va qisqa; <b>지 않다</b> — yozma va biroz taʼkidli.</li>
    <li>하다 feʼllarida <b>안 oʻrtaga tushadi</b>: 공부 안 해요.</li>
    <li>지 않다 esa <b>boʻlinmaydi</b>: 공부하지 않아요.</li>
    <li>Uchta istisno: 있다 → <b>없다</b>, 알다 → <b>모르다</b>,
        이다 → <b>아니다</b>.</li>
    <li>Tuslanish har doim <b>oxirgi soʻzda</b>: 안 먹었어요 · 먹지 않았어요.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-22: Inkor 2: 못 + feʼl va 지 못하다 (imkoniyat yoʻqligi)",
        "category": "korean",
        "order": 22,
        "summary": (
            "“Qilmayman” va “qila olmayman” — koreys tilida ikki boshqa soʻz. "
            "Oʻzbekchada ham shunday, shuning uchun bu farq sizga tanish."
        ),
        "stories": ["오늘은 못 가요"],
        "content": """
<h2>PK-22: Inkor 2: 못 + feʼl va 지 못하다 (imkoniyat yoʻqligi)</h2>

<p>PK-21 da <b>안 가요</b> ni oʻrgandingiz — “bormayman”. Lekin agar borishni
<em>xohlasangiz-u, imkoningiz boʻlmasa</em>? Oʻzbekchada bu ikkisi boshqa-boshqa:
<b>bormayman</b> va <b>bora olmayman</b>. Koreys tilida ham xuddi shunday, va bugun
ikkinchisini oʻrganamiz. Bu dars bilan Block B — “Birinchi gaplar” bloki tugaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>못 bilan imkoniyat yoʻqligini bildirasiz</li>
    <li>안 va 못 ni aniq ajratasiz</li>
    <li>지 못하다 uzun shaklini yasaysiz</li>
    <li>못 ning talaffuzidagi uchta oʻzgarishni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki boshqa inkor</span>
  <span class="pe-chip pe-chip--neg">안 — qilmayman</span>
  <span class="pe-op">≠</span>
  <span class="pe-chip pe-chip--aux">못 — qila olmayman</span>
</div>

<h3>1. Farqning oʻzagi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">안 — tanlov</p>
    <p>Xohlamayman, qilmayman, odatim yoʻq.</p>
    <p><b>저는 커피를 안 마셔요.</b></p>
    <p>Kofe ichmayman (yoqtirmayman).</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">못 — imkoniyat yoʻq</p>
    <p>Xohlayman, lekin qila olmayman. Nimadir toʻsqinlik qilyapti.</p>
    <p><b>저는 커피를 못 마셔요.</b></p>
    <p>Kofe icholmayman (salomatlik, alergiya…).</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu farq oʻzbek tilida <b>allaqachon bor</b>, shuning uchun sizga qiyin boʻlmaydi:
<br>• <em>bor<b>mayman</b></em> → <b>안 가요</b> (xohlamayman)
<br>• <em>bora <b>olmayman</b></em> → <b>못 가요</b> (imkonim yoʻq)
<br>Ingliz tilida bu <em>don't</em> va <em>can't</em>, ya'ni u yerda ham farq bor.
Lekin oʻzbekchadagi <em>-a olmoq</em> tuzilishi koreyschaga yaqinroq: ikkalasi ham
<b>alohida boʻlak</b> qoʻshadi.</div>

<h3>2. Qisqa shakl: 못</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">오늘은 학교에 <span class="pe-hl pe-hl--aux">못</span> 가요.</p>
  <p class="pe-ex__uz">Bugun maktabga borolmayman.</p>
  <p class="pe-ex__why">Sabab tashqarida — kasal, band, avtobus yoʻq…</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시간이 없어요. 그래서 책을 못 읽었어요.</p>
  <p class="pe-ex__uz">Vaqtim yoʻq edi. Shuning uchun kitob oʻqiy olmadim.</p>
</div>

<h3>3. Uzun shakl: 지 못하다</h3>

<p>Xuddi 지 않다 kabi tuziladi, faqat 않다 oʻrniga <b>못하다</b>:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Lugʻat</th><th>Qisqa</th><th>Uzun</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">가다</td><td class="pk-res">못 가요</td>
      <td class="pk-end">가지 못해요</td><td class="pk-uz">borolmayman</td></tr>
  <tr><td class="pk-stem">먹다</td><td class="pk-res">못 먹어요</td>
      <td class="pk-end">먹지 못해요</td><td class="pk-uz">yeyolmayman</td></tr>
  <tr><td class="pk-stem">읽다</td><td class="pk-res">못 읽어요</td>
      <td class="pk-end">읽지 못해요</td><td class="pk-uz">oʻqiy olmayman</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>못하다</b> — bu 하다 feʼli, demak PK-18 qoidasi boʻyicha <b>못해요</b> boʻladi.
Shuning uchun 지 못하다 har doim <b>지 못해요</b>. Yodlash kerak boʻlgan yangi narsa
yoʻq.</div>

<h3>4. Talaffuz — uchta oʻzgarish</h3>

<p>못 ning 받침i <b>ㅅ</b>, ya'ni PK-7 qoidasi boʻyicha u <b>[ㄷ]</b> boʻlib toʻxtaydi.
Keyingi soʻz bilan uchrashganda esa PK-8 dagi qoidalar ishga tushadi:</p>

<div class="pk-say">
  <span class="pk-say__from">못 가요</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[몯까요]</span>
  <span class="pk-say__why">경음화 — ㄱ qattiqlashadi</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">못 먹어요</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[몬머거요]</span>
  <span class="pk-say__why">비음화 — ㅁ oldidan ㄷ → ㄴ</span>
</div>

<div class="pk-say">
  <span class="pk-say__from">못 해요</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[모태요]</span>
  <span class="pk-say__why">격음화 — ㄷ + ㅎ = ㅌ</span>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Bu uchta qoidani PK-8 da oʻrgangansiz. Bugun ular <b>bitta soʻzda</b> uchrashdi —
못 dan keyin qaysi harf kelishiga qarab uchta xil talaffuz chiqadi. Yodlamang: 못 ni
[몯] deb toʻxtating, keyin ogʻiz oʻzi toʻgʻri yoʻlni topadi.</div>

<h3>5. 하다 feʼllari — yana oʻrtaga</h3>

<p>PK-21 dagi qoida bu yerda ham ishlaydi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">어제 공부 못 했어요.</p>
  <p class="pe-ex__rom">[공부 모태써요]</p>
  <p class="pe-ex__uz">Kecha oʻqiy olmadim.</p>
  <p class="pe-ex__why">공부하다 → 공부 <b>못</b> 했어요, <s>못 공부했어요</s> emas.</p>
</div>

<h3>6. 못 sifatlar bilan ishlatilmaydi</h3>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>못 sifatga qoʻshilmaydi.</b> “Yaxshi boʻla olmaslik” degan maʼno yoʻq —
<s>못 좋아요</s> notoʻgʻri. Sifatni inkor qilish uchun faqat <b>안</b> yoki
<b>지 않다</b> ishlatiladi: <b>안 좋아요</b>, <b>좋지 않아요</b>.</div>

<h3>7. Yonma-yon</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Gap</th><th>Maʼnosi</th><th>Nima nazarda tutilgan</th></tr>
  <tr><td class="pk-res">한국어를 안 배워요</td><td class="pk-uz">oʻrganmayman</td>
      <td class="pk-end">xohlamayman, vaqtim bor lekin oʻrganmayman</td></tr>
  <tr><td class="pk-res">한국어를 못 배워요</td><td class="pk-uz">oʻrgana olmayman</td>
      <td class="pk-end">maktab yoʻq, vaqt yoʻq, imkoniyat yoʻq</td></tr>
  <tr><td class="pk-res">밥을 안 먹어요</td><td class="pk-uz">yemayman</td>
      <td class="pk-end">och emasman</td></tr>
  <tr><td class="pk-res">밥을 못 먹어요</td><td class="pk-uz">yeyolmayman</td>
      <td class="pk-end">kasalman yoki vaqtim yoʻq</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">날씨가 <s>못 좋아요</s>.</p>
  <p class="pe-good">Sifat bilan faqat 안: 날씨가 <b>안 좋아요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">어제 <s>못 공부했어요</s>.</p>
  <p class="pe-good">하다 feʼlida 못 oʻrtaga: <b>공부 못 했어요</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">못 해요 ni "mot he-yo" deb oʻqish.</p>
  <p class="pe-good">격음화: <b>[모태요]</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">"Kofe yoqtirmayman" degani uchun <s>커피를 못 마셔요</s>.</p>
  <p class="pe-good">Bu tanlov — demak <b>안 마셔요</b>. 못 imkoniyat yoʻqligi
     uchun.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     "Bugun bandman, shuning uchun borolmayman" — qaysi inkor kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>못</strong> — <b>오늘은 못 가요.</b> Borishni
    xohlaysiz, lekin imkoniyat yoʻq. Agar 안 가요 desangiz, “bormoqchi emasman”
    degan boshqa maʼno chiqadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>못 먹어요</b> qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[몬머거요]</strong>. 못 ning 받침i [ㄷ] boʻlib
    toʻxtaydi, keyin ㅁ oldidan <em>비음화</em> boʻyicha [ㄴ] ga aylanadi. Bu PK-8 dagi
    qoida.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega "못 좋아요" notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>못 sifatga qoʻshilmaydi</strong> —
    “yaxshi boʻla olmaslik” degan maʼno yoʻq. Sifatni inkor qilish uchun
    <b>안 좋아요</b> yoki <b>좋지 않아요</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     "가지 못하다" ni 해요체 ga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>가지 못해요</strong>. Tuslanadigan narsa —
    <b>못하다</b>, va u 하다 feʼli, demak <b>못해요</b> (PK-18). Shuning uchun 지 못하다
    har doim <b>지 못해요</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Afsona kofe yoqtirmaydi. Dilnoza esa shifokor kofeni taqiqlagan. Ikkalasi nima
     deydi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Afsona — <strong>커피를 안 마셔요</strong> (yoqtirmayman,
    bu tanlov). Dilnoza — <strong>커피를 못 마셔요</strong> (icholmayman, taqiq bor).
    Bir xil harakat, ikki xil sabab, ikki xil inkor.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>못</b><span>…ay olmayman (qisqa)</span></li>
  <li><b>지 못하다</b><span>…ay olmayman (uzun)</span></li>
  <li><b>못 가요</b><span>borolmayman</span></li>
  <li><b>못 해요</b><span>qila olmayman</span></li>
  <li><b>그래서</b><span>shuning uchun</span></li>
  <li><b>바빠요</b><span>bandman</span></li>
  <li><b>아파요</b><span>ogʻriyapti, kasalman</span></li>
  <li><b>오늘은</b><span>bugun esa</span></li>
  <li><b>어려워요</b><span>qiyin</span></li>
  <li><b>쉬워요</b><span>oson</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>안 = qilmayman</b> (tanlov) · <b>못 = qila olmayman</b> (imkoniyat yoʻq).</li>
    <li>Oʻzbekcha bilan bir xil: <em>bormayman</em> va <em>bora olmayman</em>.</li>
    <li>Uzun shakl: <b>지 못해요</b> — 못하다 ham 하다 feʼli.</li>
    <li>하다 feʼllarida <b>못 oʻrtaga tushadi</b>: 공부 못 했어요.</li>
    <li><b>못 sifat bilan ishlatilmaydi</b> — faqat 안 yoki 지 않다.</li>
    <li>Talaffuz: 못 가요 <b>[몯까요]</b> · 못 먹어요 <b>[몬머거요]</b> ·
        못 해요 <b>[모태요]</b>.</li>
  </ul>
</div>
""",
    },
]
