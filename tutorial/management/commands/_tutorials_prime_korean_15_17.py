# -*- coding: utf-8 -*-
"""Prime Korean — Block B, darslar 15–17 (koʻrsatish olmoshlari va qolgan qoʻshimchalar).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_15_17.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_15_17.py --author=prime
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
        "title": "PK-15: 이거/그거/저거 va 여기/거기/저기 — koʻrsatish olmoshlari",
        "category": "korean",
        "order": 15,
        "summary": (
            "Koreys tilida koʻrsatish uch pogʻonali: 이 · 그 · 저. Oʻzbekchadagi "
            "bu · shu · u bilan deyarli aynan mos tushadi."
        ),
        "stories": ["이것은 무엇입니까?"],
        "content": """
<h2>PK-15: 이거/그거/저거 va 여기/거기/저기 — koʻrsatish olmoshlari</h2>

<p>Ingliz tilida koʻrsatish ikki pogʻonali: <em>this</em> va <em>that</em>, tamom.
Koreys tilida esa <b>uchta</b> — va bu ingliz tilidan oʻrganayotgan har qanday
oʻquvchini adashtiradi. Sizni esa adashtirmaydi, chunki oʻzbek tilida ham aynan
uchta: <b>bu · shu · u</b>. Bugun bu uchlikni koreyschaga koʻchiramiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>이 · 그 · 저 uchligini oʻzbekcha bu · shu · u orqali oʻzlashtirasiz</li>
    <li>Narsa, odam va joy uchun toʻgʻri shaklni tanlaysiz</li>
    <li>무엇, 누구, 어디 bilan savol berasiz</li>
    <li>저 (“anavi”) va 저 (“men”) ni adashtirmaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch pogʻona</span>
  <span class="pe-chip pe-chip--s">이 — bu</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">그 — shu</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--adv">저 — u, anavi</span>
</div>

<h3>1. Uchlikning mantiqi</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">이 — men tomonda</p>
    <p>Gapiruvchiga yaqin. Qoʻlim bilan ushlab turgan narsa.</p>
    <p style="font-size:1.3rem">이것 · 여기 · 이 사람</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">그 — sen tomonda</p>
    <p>Tinglovchiga yaqin, <b>yoki</b> ikkalamiz allaqachon gapirgan narsa.</p>
    <p style="font-size:1.3rem">그것 · 거기 · 그 사람</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>저</b> — uchinchi pogʻona: <em>ikkalamizdan ham uzoq</em>, lekin koʻrinib turibdi.
Oʻzbekcha "anavi" / "u": 저것, 저기, 저 사람.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu darsning eng qulay joyi — <b>oʻzbek tilida ham aynan uchta pogʻona bor</b>:
<br>• <b>bu</b> kitob → <b>이</b> 책 (menda)
<br>• <b>shu</b> kitob → <b>그</b> 책 (senda yoki gapirib boʻlgan kitobimiz)
<br>• <b>u / anavi</b> kitob → <b>저</b> 책 (u yoqda)
<br>Ingliz tilida bu uchlik ikkitaga siqilgan (<em>this / that</em>), shuning uchun
ingliz tilidan oʻrganuvchi 그 va 저 ni doim adashtiradi. Sizga esa tarjima
tayyor turibdi.</div>

<h3>2. Uch qator: narsa, joy, odam</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nimaga</th><th>이 (bu)</th><th>그 (shu)</th><th>저 (u)</th></tr>
  <tr><td class="pk-res">Narsa (rasmiy)</td><td class="pk-stem">이것</td>
      <td class="pk-end">그것</td><td class="pk-uz">저것</td></tr>
  <tr><td class="pk-res">Narsa (ogʻzaki)</td><td class="pk-stem">이거</td>
      <td class="pk-end">그거</td><td class="pk-uz">저거</td></tr>
  <tr><td class="pk-res">Joy</td><td class="pk-stem">여기</td>
      <td class="pk-end">거기</td><td class="pk-uz">저기</td></tr>
  <tr><td class="pk-res">Ot oldida</td><td class="pk-stem">이 책</td>
      <td class="pk-end">그 책</td><td class="pk-uz">저 책</td></tr>
  <tr><td class="pk-res">Odam</td><td class="pk-stem">이 사람</td>
      <td class="pk-end">그 사람</td><td class="pk-uz">저 사람</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>이것</b> — yozma va rasmiy, <b>이거</b> — ogʻzaki. Darslikda 이것 koʻrasiz, koʻchada
esa deyarli har doim 이거 eshitasiz. Ikkalasi bir xil narsa.</div>

<h3>3. Ot oldida — 것 tushib qoladi</h3>

<p>Diqqat qiling: 이것 <em>yolgʻiz</em> turadi ("bu narsa"), lekin ot qoʻshsangiz
<b>것 yoʻqoladi</b>:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">이것은</span> 책입니다.</p>
  <p class="pe-ex__uz">Bu kitob. (Bu narsa — kitob.)</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">이 책은</span> 제 책입니다.</p>
  <p class="pe-ex__uz">Bu kitob mening kitobim.</p>
  <p class="pe-ex__why">Ot bor — shuning uchun <s>이것 책</s> emas, <b>이 책</b>.</p>
</div>

<h3>4. Joy: 여기 / 거기 / 저기</h3>

<p>Joy shakllari PK-14 dagi <b>에</b> bilan juftlashadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">책이 <span class="pe-hl pe-hl--adv">여기에</span> 있습니다.</p>
  <p class="pe-ex__uz">Kitob bu yerda.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">선생님은 <span class="pe-hl pe-hl--adv">저기에</span> 계십니다.</p>
  <p class="pe-ex__uz">Oʻqituvchi anavi yerda.</p>
  <p class="pe-ex__why">Hurmatli odam — shuning uchun 있습니다 emas, <b>계십니다</b>.</p>
</div>

<h3>5. Savol soʻzlari</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Savol</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pk-stem">무엇 / 뭐</td><td class="pk-uz">nima</td>
      <td class="pk-res">이것은 무엇입니까?</td></tr>
  <tr><td class="pk-stem">누구</td><td class="pk-uz">kim</td>
      <td class="pk-res">저 사람은 누구입니까?</td></tr>
  <tr><td class="pk-stem">어디</td><td class="pk-uz">qayer</td>
      <td class="pk-res">교실은 어디에 있습니까?</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 이것은 무엇입니까?<br>나: 그것은 가방입니다.</p>
  <p class="pe-ex__uz">A: Bu nima?<br>B: Shu — sumka.</p>
  <p class="pe-ex__why">Diqqat: savol beruvchi <b>이것</b> (menda) dedi, javob beruvchi
     esa <b>그것</b> (senda) deydi. Pogʻona <em>kimning tomonidan</em> qaralayotganiga
     qarab almashadi — xuddi oʻzbekchadagi "bu" va "shu" kabi.</p>
</div>

<h3>6. Ehtiyot boʻling: ikkita 저</h3>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>저</b> ikki xil soʻz:
<br>• <b>저는 학생입니다</b> — "Men talabaman" (kamtar olmosh, PK-10)
<br>• <b>저 사람은 학생입니다</b> — "Anavi odam talaba" (koʻrsatish)
<br>Farqni <b>keyingi soʻz</b> aytib turadi: 저 dan keyin darhol ot kelsa — "anavi".
Qoʻshimcha (는, 도, 의) kelsa — "men".</div>

<h3>7. Nutqda qisqarish</h3>

<p>Ogʻzaki nutqda 이것이 → <b>이게</b>, 그것이 → <b>그게</b>, 저것이 → <b>저게</b>
boʻlib qisqaradi. Buni hozircha <b>tanib olish</b> darajasida bilsangiz yetarli —
koreyslar deyarli har doim shunday gapiradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">이게 뭐예요?</p>
  <p class="pe-ex__uz">Bu nima? (ogʻzaki)</p>
  <p class="pe-ex__why">이것이 무엇입니까? bilan bir xil maʼno, faqat kundalik shakl.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>이것 책은</s> 제 책입니다.</p>
  <p class="pe-good">Ot qoʻshilsa 것 tushadi: <b>이 책은</b> 제 책입니다.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Tinglovchining qoʻlidagi narsaga <s>저것</s> deyish.</p>
  <p class="pe-good">Tinglovchida boʻlsa — <b>그것</b>. 저것 faqat ikkalamizdan
     uzoqdagi narsa uchun.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저 사람은 학생입니다 ni "Men talabaman" deb tushunish.</p>
  <p class="pe-good">저 dan keyin darhol ot kelgan — demak bu <b>"anavi odam"</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">책이 <s>여기</s> 있습니다.</p>
  <p class="pe-good">Joy + <b>에</b>: 책이 <b>여기에</b> 있습니다.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Suhbatdoshingiz qoʻlida turgan kitobga qanday koʻrsatasiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>그 책</strong> (yoki 그것). <b>그</b> —
    tinglovchi tomonidagi narsa, oʻzbekcha "<em>shu</em>". 이 sizda boʻlgan narsa uchun,
    저 esa ikkalangizdan ham uzoqdagi narsa uchun.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Nega "이것 책" notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>것 — “narsa” degani</strong>, ya'ni
    이것 = “bu narsa”. Ot qoʻshsangiz 것 keraksiz boʻlib qoladi va tushadi:
    <b>이 책</b> = “bu kitob”.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     "Oʻqituvchi anavi yerda" ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>선생님은 저기에 계십니다.</strong> Uchta narsa:
    <b>저기</b> (uzoqdagi joy), <b>에</b> (있다/계시다 bilan har doim), va hurmatli odam
    boʻlgani uchun <b>계십니다</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu ikki gapdagi 저 bir xilmi?<br>
     (a) 저는 학생입니다. &nbsp; (b) 저 사람은 학생입니다.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Yoʻq. (a) da <strong>저 = “men”</strong> — keyin
    qoʻshimcha (는) kelgan. (b) da <strong>저 = “anavi”</strong> — keyin darhol ot
    (사람) kelgan. Keyingi soʻz farqni aytib turadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Afsona sizdan "이것은 무엇입니까?" deb soʻradi. Javobingizda qaysi shakl
     ishlatilishi tabiiy?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>그것</strong> — masalan "그것은 가방입니다".
    Narsa Afsonaning qoʻlida, ya'ni <em>tinglovchi</em> (siz) uchun u “shu” boʻladi.
    Pogʻona kim qarayotganiga qarab almashadi — xuddi oʻzbekchadagi bu/shu
    kabi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>이것 / 이거</b><span>bu (narsa)</span></li>
  <li><b>그것 / 그거</b><span>shu (narsa)</span></li>
  <li><b>저것 / 저거</b><span>anavi (narsa)</span></li>
  <li><b>여기 / 거기 / 저기</b><span>bu yer / shu yer / u yer</span></li>
  <li><b>이 사람 / 그 사람 / 저 사람</b><span>bu / shu / anavi odam</span></li>
  <li><b>무엇 / 뭐</b><span>nima</span></li>
  <li><b>누구</b><span>kim</span></li>
  <li><b>어디</b><span>qayer</span></li>
  <li><b>것</b><span>narsa</span></li>
  <li><b>분</b><span>kishi (사람 ning hurmatli shakli)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>이 = bu · 그 = shu · 저 = u/anavi</b> — oʻzbekcha uchlik bilan aynan mos.</li>
    <li><b>그</b> — tinglovchi tomonidagi <em>yoki</em> allaqachon gapirilgan narsa.</li>
    <li>Ot qoʻshilsa <b>것 tushadi</b>: 이것 → 이 책.</li>
    <li>Joy: 여기 / 거기 / 저기, va 있다 bilan har doim <b>에</b>.</li>
    <li><b>저 + ot</b> = “anavi”, <b>저 + qoʻshimcha</b> = “men”.</li>
    <li>Ogʻzaki nutqda 이것이 → <b>이게</b>, 이것 → <b>이거</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-16: 도, 만, 부터, 까지, 하고/와/과 — qolgan asosiy qoʻshimchalar",
        "category": "korean",
        "order": 16,
        "summary": (
            "“Ham”, “faqat”, “-dan … -gacha” va “va”. Beshta qoʻshimcha, beshtasi ham "
            "oʻzbekchada aniq ekvivalentga ega — eng oson darslardan biri."
        ),
        "stories": ["아침부터 저녁까지"],
        "content": """
<h2>PK-16: 도, 만, 부터, 까지, 하고/와/과 — qolgan asosiy qoʻshimchalar</h2>

<p>PK-12 dagi 은/는 va 이/가 qiyin edi, chunki oʻzbekchada ularning aniq ekvivalenti
yoʻq. Bugungi beshta qoʻshimcha esa buning aksi: <b>har biri oʻzbekchadagi bitta aniq
soʻzga toʻgʻri keladi</b>. Shuning uchun bu Block B ning eng oson darsi — lekin bitta
qoida bor, uni eʼtibordan qochirmang.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>도 (“ham”) va 만 (“faqat”) bilan gap tuzasiz</li>
    <li>부터 … 까지 orqali vaqt oraligʻini koʻrsatasiz</li>
    <li>와/과/하고 bilan ikki otni bogʻlaysiz</li>
    <li>도 va 만 nega 은/는 ni <em>almashtirishini</em> tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Besh qoʻshimcha</span>
  <span class="pe-chip pe-chip--v">도 — ham</span>
  <span class="pe-chip pe-chip--o">만 — faqat</span>
  <span class="pe-chip pe-chip--adv">부터 — dan</span>
  <span class="pe-chip pe-chip--adv">까지 — gacha</span>
  <span class="pe-chip pe-chip--s">와/과 — va</span>
</div>

<h3>1. 도 — “ham”</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">저<span class="pe-hl pe-hl--v">도</span> 학생입니다.</p>
  <p class="pe-ex__uz">Men ham talabaman.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida — darsning eng muhim joyi</span>
<b>도 qoʻshimchasi 은/는 va 이/가 ni ALMASHTIRADI, ular bilan birga kelmaydi.</b>
<br>✗ <s>저는도</s> · ✗ <s>저도는</s> · ✓ <b>저도</b>
<br>Xuddi shu qoida <b>만</b> ga ham tegishli: ✓ <b>저만</b>, ✗ <s>저는만</s>.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu qoida sizga tanish tuyulishi kerak. Oʻzbekchada ham "men<b>ham</b>" deymiz —
"men<em>ni</em>ham" emas. Qoʻshimcha egalik belgisini yutib yuboradi. Koreysda
ham xuddi shunday: 도 kelganda 는 yoʻqoladi.</div>

<h3>2. 만 — “faqat”</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 책<span class="pe-hl pe-hl--o">만</span> 있습니다.</p>
  <p class="pe-ex__uz">Menda faqat kitob bor.</p>
  <p class="pe-ex__why">만 이/가 ni ham almashtiradi: <s>책이만</s> emas,
     <b>책만</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">자수르 씨만 한국 사람입니다.</p>
  <p class="pe-ex__uz">Faqat Jasur koreys.</p>
</div>

<h3>3. 부터 … 까지 — “dan … gacha”</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">아침<span class="pe-hl pe-hl--adv">부터</span>
     저녁<span class="pe-hl pe-hl--adv">까지</span> 학교에 있습니다.</p>
  <p class="pe-ex__uz">Ertalabdan kechgacha maktabdaman.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
<b>부터 = -dan</b>, <b>까지 = -gacha</b>. Ikkalasi ham otdan keyin yopishadi va
tartibi ham bir xil: <em>ertalab<b>dan</b> kech<b>gacha</b></em> →
<em>아침<b>부터</b> 저녁<b>까지</b></em>. Soʻzma-soʻz koʻchiraverasiz.</div>

<p>Joy uchun esa <b>부터</b> emas, <b>에서</b> ishlatiladi — PK-14 dagi “…dan”:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Nima uchun</th><th>“…dan”</th><th>“…gacha”</th><th>Misol</th></tr>
  <tr><td class="pk-res">Vaqt</td><td class="pk-stem">부터</td><td class="pk-end">까지</td>
      <td class="pk-uz">아침부터 저녁까지</td></tr>
  <tr><td class="pk-res">Joy</td><td class="pk-stem">에서</td><td class="pk-end">까지</td>
      <td class="pk-uz">학교에서 집까지</td></tr>
</table></div>

<h3>4. 와 / 과 / 하고 — “va”</h3>

<p>Ikki otni bogʻlash uchun uchta shakl bor. Maʼnosi bir xil, uslubi boshqa:</p>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">과</span></p>
    <p>책<b>과</b> 가방</p>
    <p>선생님<b>과</b> 학생</p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">와</span></p>
    <p>친구<b>와</b> 저</p>
    <p>의사<b>와</b> 간호사</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ayri yodlash qiyin boʻlsa — <b>하고</b> ishlating. U <em>hech qachon oʻzgarmaydi</em>
va kundalik nutqda 와/과 dan koʻra koʻproq eshitiladi: 책<b>하고</b> 가방,
친구<b>하고</b> 저. Rasmiy yozuvda esa 와/과 afzal.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가방 안에 책과 돈이 있습니다.</p>
  <p class="pe-ex__uz">Sumka ichida kitob va pul bor.</p>
</div>

<h3>5. Hammasi birga</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 아침부터 저녁까지 학교에 있습니다.
     딜노자 씨도 여기에 있습니다.</p>
  <p class="pe-ex__uz">Men ertalabdan kechgacha maktabdaman. Dilnoza ham shu yerda.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가방 안에 책만 있습니다. 돈은 없습니다.</p>
  <p class="pe-ex__uz">Sumka ichida faqat kitob bor. Pul esa yoʻq.</p>
  <p class="pe-ex__why">Ikkinchi gapda <b>은</b> ishlatilgan — chunki qiyoslanmoqda
     (PK-12).</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>저는도</s> 학생입니다.</p>
  <p class="pe-good">도 은/는 ni almashtiradi: <b>저도</b> 학생입니다.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>책이만</s> 있습니다.</p>
  <p class="pe-good">만 ham 이/가 ni almashtiradi: <b>책만</b> 있습니다.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>책와</s> 가방</p>
  <p class="pe-good">책 받침 bilan tugaydi → <b>책과</b> 가방. Yoki oddiygina
     <b>책하고</b> 가방.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">학교<s>부터</s> 집까지 (joy haqida)</p>
  <p class="pe-good">Joy uchun <b>에서</b>: 학교<b>에서</b> 집까지. 부터 — vaqt
     uchun.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     "Men ham talabaman" ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>저도 학생입니다.</strong> <b>저는도</b> emas —
    도 mavzu qoʻshimchasini almashtiradi, u bilan birga kelmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga nima tushadi? 가방 안에 책<span class="pe-blank">?</span> 있습니다.
     (“faqat kitob”)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>만</strong> — 책만 있습니다. 만 ham 이/가 ni
    almashtiradi, shuning uchun <s>책이만</s> notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     "책 va 가방" ni ikki xil usulda yozing.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>책과 가방</strong> (rasmiy — 책 받침 bilan
    tugagani uchun 과) yoki <strong>책하고 가방</strong> (ogʻzaki — 하고 hech qachon
    oʻzgarmaydi).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     "Maktabdan uygacha" ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>학교에서 집까지.</strong> Bu <em>joy</em> oraligʻi,
    shuning uchun “…dan” uchun <b>부터</b> emas, <b>에서</b> ishlatiladi. “…gacha”
    esa ikkalasida ham <b>까지</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Sherbek "저는도 한국 사람입니다" dedi. Xatoni tuzating va sababini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Toʻgʻrisi — <strong>저도 한국 사람입니다.</strong>
    <b>도</b> mavzu (은/는) va ega (이/가) qoʻshimchalarini <em>almashtiradi</em>, ular
    bilan yonma-yon kelmaydi. Oʻzbekchada ham “men<b>ham</b>” deymiz, “menniham”
    emas.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>도</b><span>ham</span></li>
  <li><b>만</b><span>faqat</span></li>
  <li><b>부터</b><span>-dan (vaqt)</span></li>
  <li><b>까지</b><span>-gacha</span></li>
  <li><b>와 / 과 / 하고</b><span>va</span></li>
  <li><b>아침 / 점심 / 저녁</b><span>ertalab / tush / kechqurun</span></li>
  <li><b>집</b><span>uy</span></li>
  <li><b>학교</b><span>maktab</span></li>
  <li><b>돈</b><span>pul</span></li>
  <li><b>동갑</b><span>tengdosh</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>도 = ham · 만 = faqat</b> — ikkalasi ham 은/는 va 이/가 ni
        <b>almashtiradi</b>.</li>
    <li><b>부터 … 까지</b> = “-dan … -gacha”, vaqt uchun.</li>
    <li>Joy oraligʻida “…dan” uchun <b>에서</b>: 학교에서 집까지.</li>
    <li><b>와/과</b>: 받침 yoʻq → 와, bor → 과. <b>하고</b> hech qachon oʻzgarmaydi.</li>
    <li>Qiyoslash kerak boʻlsa 은/는 qaytib keladi: 책만 있습니다. 돈<b>은</b> 없습니다.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-17: 을/를 va 의 — toʻldiruvchi va egalik",
        "category": "korean",
        "order": 17,
        "summary": (
            "Koreys toʻldiruvchi qoʻshimchasi oʻzbekcha “-ni” bilan aynan bir xil "
            "ishlaydi — hatto soʻz tartibi ham mos. Feʼllar bilan birinchi tanishuv."
        ),
        "stories": ["제 가방 안에"],
        "content": """
<h2>PK-17: 을/를 va 의 — toʻldiruvchi va egalik</h2>

<p>Bugungi dars oʻzbek oʻquvchi uchun sovgʻa. <b>책을 읽습니다</b> — “kitob<b>ni</b>
oʻqiyman”. Qoʻshimcha ham bir xil vazifada, soʻz tartibi ham bir xil: <em>ega →
toʻldiruvchi → kesim</em>. Ingliz tilida bu butunlay boshqacha (<em>I read a book</em>,
toʻldiruvchi feʼldan keyin), shuning uchun ingliz tilidan oʻrganuvchi bu yerda
qiynaladi. Siz esa oʻzbekcha gapni deyarli soʻzma-soʻz koʻchirasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>을/를 bilan toʻldiruvchini belgilaysiz</li>
    <li>Koreys va oʻzbek soʻz tartibi bir xil ekanini koʻrasiz</li>
    <li>의 bilan egalikni bildirasiz va 제 / 내 qisqarishini bilasiz</li>
    <li>Birinchi feʼllaringizni ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻliq koreys gapi</span>
  <span class="pe-chip pe-chip--s">ega + 은/는</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">toʻldiruvchi + 을/를</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">feʼl</span>
</div>

<div class="pe-legend">
  <span><i style="background:#2563eb"></i>ega — 주어</span>
  <span><i style="background:#d97706"></i>toʻldiruvchi — 목적어</span>
  <span><i style="background:#16a34a"></i>kesim — 서술어</span>
</div>

<h3>1. Avval feʼllar — hozircha butunligicha</h3>

<p>Toʻldiruvchi feʼlsiz yashamaydi, shuning uchun bugun bir nechta feʼlni
<b>tayyor holda</b> olamiz. Ular qanday yasalishini PK-18 va PK-19 darslari
koʻrsatadi — hozircha shunchaki soʻz sifatida yodlang:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Shakl</th><th>Maʼnosi</th><th>Oʻqilishi</th></tr>
  <tr><td class="pk-res">읽습니다</td><td class="pk-uz">oʻqiyman (kitobni)</td>
      <td class="pk-end">[익씀니다]</td></tr>
  <tr><td class="pk-res">봅니다</td><td class="pk-uz">koʻraman</td>
      <td class="pk-end">[봄니다]</td></tr>
  <tr><td class="pk-res">먹습니다</td><td class="pk-uz">yeyman</td>
      <td class="pk-end">[먹씀니다]</td></tr>
  <tr><td class="pk-res">마십니다</td><td class="pk-uz">ichaman</td>
      <td class="pk-end">[마심니다]</td></tr>
  <tr><td class="pk-res">공부합니다</td><td class="pk-uz">oʻqiyman, tahsil olaman</td>
      <td class="pk-end">[공부함니다]</td></tr>
  <tr><td class="pk-res">좋아합니다</td><td class="pk-uz">yoqtiraman</td>
      <td class="pk-end">[조아함니다]</td></tr>
</table></div>

<h3>2. 을/를 — toʻldiruvchi qoʻshimchasi</h3>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">을</span></p>
    <p>책<b>을</b> · 밥<b>을</b> · 물<b>을</b></p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">를</span></p>
    <p>커피<b>를</b> · 친구<b>를</b> · 우유<b>를</b></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">저는</span>
     <span class="pe-hl pe-hl--o">책을</span>
     <span class="pe-hl pe-hl--v">읽습니다</span>.</p>
  <p class="pe-ex__uz">Men kitobni oʻqiyman.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Ikki gapni yonma-yon qoʻying:
<br>• <em>Men</em> · <em>kitob<b>ni</b></em> · <em>oʻqiyman</em>
<br>• <em>저는</em> · <em>책<b>을</b></em> · <em>읽습니다</em>
<br><b>Uchala boʻlak ham bir xil tartibda</b>, qoʻshimcha ham bir xil vazifada:
oʻzbekcha <b>-ni</b> = koreyscha <b>을/를</b>. Ingliz tilida esa toʻldiruvchi feʼldan
<em>keyin</em> keladi va hech qanday qoʻshimcha olmaydi. Bu — koreys tilini
oʻrganishdagi eng katta afzalligingiz.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 커피를 마십니다.</p>
  <p class="pe-ex__uz">Men kofe ichaman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">자수르 씨는 한국어를 공부합니다.</p>
  <p class="pe-ex__uz">Jasur koreys tilini oʻrganadi.</p>
</div>

<h3>3. Soʻz tartibi — kesim har doim oxirida</h3>

<p>Koreys tili ham, oʻzbek tili ham <b>SOV</b> tilidir: ega — toʻldiruvchi — kesim.
Boshqa boʻlaklar (joy, vaqt) toʻldiruvchidan oldin turadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">저는</span>
     <span class="pe-hl pe-hl--adv">아침에</span>
     <span class="pe-hl pe-hl--adv">집에서</span>
     <span class="pe-hl pe-hl--o">우유를</span>
     <span class="pe-hl pe-hl--v">마십니다</span>.</p>
  <p class="pe-ex__uz">Men ertalab uyda sut ichaman.</p>
  <p class="pe-ex__why">Oʻzbekcha gapdagi tartib bilan solishtiring — deyarli aynan
     bir xil.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Bu yerda <b>에서</b> ishlatilgani bejiz emas: 마십니다 — harakat feʼli, demak PK-14
qoidasi boʻyicha joy uchun <b>에</b> emas, <b>에서</b> kerak. Mana endi bu farq
haqiqatan ishlay boshladi.</div>

<h3>4. 의 — egalik qoʻshimchasi</h3>

<p>“…ning” maʼnosini <b>의</b> beradi. U oʻzbekcha <b>-ning</b> bilan bir xil
vazifada:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">친구<span class="pe-hl pe-hl--s">의</span> 가방</p>
  <p class="pe-ex__rom">[친구에 가방]</p>
  <p class="pe-ex__uz">doʻstning sumkasi</p>
  <p class="pe-ex__why">Egalik qoʻshimchasi boʻlganda 의 <b>[에]</b> deb oʻqiladi —
     PK-3 dagi qoida.</p>
</div>

<h3>5. 제 va 내 — qisqargan shakllar</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Toʻliq</th><th>Qisqargan</th><th>Maʼnosi</th></tr>
  <tr><td class="pk-stem">저의</td><td class="pk-end">제</td>
      <td class="pk-uz">mening (hurmatli)</td></tr>
  <tr><td class="pk-stem">나의</td><td class="pk-end">내</td>
      <td class="pk-uz">mening (oddiy)</td></tr>
  <tr><td class="pk-stem">너의</td><td class="pk-end">네</td>
      <td class="pk-uz">sening</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Amalda deyarli har doim <b>제</b> va <b>내</b> ishlatiladi — 저의 va 나의 juda rasmiy
eshitiladi. Siz PK-11 dan beri <b>제 이름</b> deb kelyapsiz; endi nega shunday
ekanini bilasiz.</div>

<h3>6. 의 koʻpincha tushib qoladi</h3>

<p>Ikki ot yonma-yon turganda va munosabat aniq boʻlganda, <b>의 yozilmaydi</b>:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">의 kerak emas</p>
    <p>한국 사람 — koreys odam</p>
    <p>학교 친구 — maktab doʻsti</p>
    <p>커피 잔 — kofe stakani</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">의 kerak</p>
    <p>친구<b>의</b> 가방 — doʻstning sumkasi</p>
    <p>선생님<b>의</b> 책 — oʻqituvchining kitobi</p>
    <p>egasi <em>aniq bir kishi</em> boʻlganda</p>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>읽습니다 책을</s>.</p>
  <p class="pe-good">Kesim oxirida: 저는 <b>책을 읽습니다</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 <s>커피을</s> 마십니다.</p>
  <p class="pe-good">커피 unli bilan tugaydi → <b>커피를</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 집<s>에</s> 우유를 마십니다.</p>
  <p class="pe-good">Harakat feʼli — demak <b>에서</b>: 집<b>에서</b> 마십니다.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>저의</s> 이름은 벡조드입니다.</p>
  <p class="pe-good">Amalda qisqargan shakl: <b>제</b> 이름은 벡조드입니다.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga nima tushadi? 저는 밥<span class="pe-blank">?</span> 먹습니다.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>을</strong> — 밥 받침 (ㅂ) bilan tugaydi.
    “Men ovqat<b>ni</b> yeyman”.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     "Men koreys tilini oʻrganaman" ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>저는 한국어를 공부합니다.</strong> 한국어 unli
    (ㅓ) bilan tugaydi → <b>를</b>. Kesim gap oxirida — xuddi oʻzbekchadagidek.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega "집에서 마십니다" toʻgʻri, "집에 마십니다" notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>마시다 — harakat feʼli</strong>. PK-14
    qoidasi: 있다/없다 bilan 에, harakat feʼli bilan <b>에서</b>. Uyda <em>turibman</em>
    boʻlsa 집에 있습니다, uyda <em>ichaman</em> boʻlsa 집에서 마십니다.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     "저의" ning amaldagi qisqargan shakli qaysi va u qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>제</strong>. Toʻliq shakl 저의 juda rasmiy
    eshitiladi. Agar 의 yozilsa ham, egalik maʼnosida u <b>[에]</b> deb oʻqiladi:
    친구의 → [친구에].</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Dilnoza "저는 아침에 학교에 한국어를 공부합니다" dedi. Bitta xatoni toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>학교에 → 학교에서.</strong> 공부합니다 harakat
    feʼli, shuning uchun joy <b>에서</b> bilan keladi. Toʻgʻrisi:
    <b>저는 아침에 학교에서 한국어를 공부합니다.</b> Diqqat: <em>아침에</em> toʻgʻri —
    vaqt uchun har doim 에.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>을 / 를</b><span>toʻldiruvchi qoʻshimchasi (-ni)</span></li>
  <li><b>의</b><span>egalik qoʻshimchasi (-ning)</span></li>
  <li><b>제 / 내</b><span>mening</span></li>
  <li><b>읽습니다</b><span>oʻqiyman</span></li>
  <li><b>봅니다</b><span>koʻraman</span></li>
  <li><b>먹습니다</b><span>yeyman</span></li>
  <li><b>마십니다</b><span>ichaman</span></li>
  <li><b>공부합니다</b><span>tahsil olaman</span></li>
  <li><b>좋아합니다</b><span>yoqtiraman</span></li>
  <li><b>밥 / 물 / 우유</b><span>ovqat / suv / sut</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>을/를 = oʻzbekcha -ni.</b> 받침 bor → 을, yoʻq → 를.</li>
    <li>Soʻz tartibi: <b>ega → toʻldiruvchi → kesim</b>, ikkala tilda ham bir xil.</li>
    <li>Harakat feʼli bilan joy <b>에서</b> oladi, 있다/없다 bilan esa 에.</li>
    <li><b>의 = -ning</b>, egalik maʼnosida <b>[에]</b> deb oʻqiladi.</li>
    <li>Amalda <b>제</b> (저의) va <b>내</b> (나의) ishlatiladi.</li>
    <li>Ikki ot tabiiy bogʻliq boʻlsa 의 <b>tushadi</b>: 한국 사람, 학교 친구.</li>
  </ul>
</div>
""",
    },
]
