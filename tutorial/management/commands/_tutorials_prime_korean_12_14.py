# -*- coding: utf-8 -*-
"""Prime Korean — Block B, darslar 12–14 (qoʻshimchalar va 있다/없다).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md
Lesson list: tutorial/management/commands/toc_prime_korean.txt

Oʻqish matnlari: corner/management/commands/_stories_prime_korean_12_14.py

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_korean_12_14.py --author=prime
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
        "title": "PK-12: 은/는 va 이/가 — mavzu va ega orasidagi farq",
        "category": "korean",
        "order": 12,
        "summary": (
            "Koreys tilidagi eng qiyin qoʻshimcha juftligi. 은/는 mavzuni belgilaydi, "
            "이/가 esa egani — va oʻzbekchadagi “esa” bu farqni tushunishga yordam beradi."
        ),
        "stories": ["제 친구 아프소나"],
        "content": """
<h2>PK-12: 은/는 va 이/가 — mavzu va ega orasidagi farq</h2>

<p>Bu juftlik koreys tilini oʻrganayotgan har bir odamni qiynaydi — hatto bir necha yil
oʻqiganlarni ham. Sababi shuki, oʻzbekchada ham, ingliz tilida ham ularning aniq
ekvivalenti yoʻq: ikkalasi ham koʻpincha shunchaki "ega" boʻlib tarjima qilinadi.
Lekin farq bor va u <b>maʼnoni oʻzgartiradi</b>. Bugun uni ochamiz — va sizda
oʻzbekchadagi bitta kichkina soʻz tufayli katta afzallik bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>은/는 va 이/가 ni 받침 qoidasi boʻyicha toʻgʻri tanlaysiz</li>
    <li>Mavzu (주제) va ega (주어) farqini tushunasiz</li>
    <li>Qachon qaysi birini ishlatishni uchta aniq holatda bilasiz</li>
    <li>Oʻzbekcha "esa" orqali 는 ning maʼnosini his qilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qoʻshimcha, ikki vazifa</span>
  <span class="pe-chip pe-chip--s">은/는 — mavzu</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">이/가 — ega</span>
</div>

<h3>1. Avval shakl — 받침 qoidasi</h3>

<p>Har ikkala juftlik ham bir xil qoidaga boʻysunadi. Bu PK-10 da 이/가 아닙니다 da
koʻrgan ayringiz — endi u mustaqil ishlaydi.</p>

<div class="pk-batchim">
  <div class="pk-batchim__side">
    <p class="pk-batchim__h">받침 BOR</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">은</span> /
       <span class="pk-par">이</span></p>
    <p>선생님<b>은</b> · 학생<b>이</b></p>
    <p>책<b>은</b> · 가방<b>이</b></p>
  </div>
  <div class="pk-batchim__side pk-batchim__side--no">
    <p class="pk-batchim__h">받침 YOʻQ</p>
    <p class="pk-batchim__form">ot + <span class="pk-par">는</span> /
       <span class="pk-par">가</span></p>
    <p>저<b>는</b> · 의사<b>가</b></p>
    <p>친구<b>는</b> · 어머니<b>가</b></p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Shaklni tanlash oson: <b>quloq bilan tekshiring</b>. 학생는 deb aytib koʻring — ogʻiz
qiynaladi. 학생은 esa oʻz-oʻzidan chiqadi. Koreys tilidagi 받침 ayrilari deyarli har doim
talaffuzni yengillashtirish uchun mavjud.</div>

<h3>2. Endi maʼno — 는 nima qiladi</h3>

<p><b>은/는</b> — bu <em>ega</em> qoʻshimchasi emas. U gapning <b>mavzusini</b>
belgilaydi: "men hozir <em>shu narsa haqida</em> gapiryapman".</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana sizning afzalligingiz. Oʻzbekchada bu maʼnoni <b>"esa"</b> yoki
<b>"…ga kelsak"</b> beradi:
<br>• 저<b>는</b> 학생입니다 → "Men<b>ga kelsak</b>, talabaman."
<br>• 아프소나<b>는</b> 의사입니다 → "Afsona<b>esa</b> shifokor."
<br>Ingliz tilini oʻrganayotgan bola bu tuygʻuni noldan quradi. Sizda u allaqachon bor —
faqat koreyschada u <em>alohida soʻz emas, qoʻshimcha</em>.</div>

<p>Shuning uchun 는 ikki narsani anglatadi:</p>

<ul class="pe-steps">
  <li><b>Tanish mavzu</b> — suhbatdosh bu haqda allaqachon biladi yoki bu umumiy mavzu.</li>
  <li><b>Qiyoslash</b> — "boshqasi boshqacha" degan soya har doim ostida turadi.</li>
</ul>

<div class="pe-ex">
  <p class="pe-ex__ko">자수르 씨<span class="pe-hl pe-hl--s">는</span> 학생입니다.
     딜노자 씨<span class="pe-hl pe-hl--s">는</span> 선생님입니다.</p>
  <p class="pe-ex__uz">Jasur talaba. Dilnoza esa oʻqituvchi.</p>
  <p class="pe-ex__why">Ikki mavzu qiyoslanmoqda — aynan shu yerda 는 kerak.</p>
</div>

<h3>3. 이/가 nima qiladi</h3>

<p><b>이/가</b> — haqiqiy <b>ega</b> qoʻshimchasi. U "<em>kim</em>?" degan savolga javob
beradi va koʻpincha <b>yangi maʼlumot</b> keltiradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 누가 학생입니까?<br>
     나: 자수르 씨<span class="pe-hl pe-hl--o">가</span> 학생입니다.</p>
  <p class="pe-ex__uz">A: Kim talaba?<br>B: Jasur talaba.</p>
  <p class="pe-ex__why">Savol aynan "kim?" — javobda yangi odam nomlanmoqda,
     shuning uchun <b>가</b>. Bu yerda 는 ishlatilsa, gʻalati chiqadi.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>"누가?" (kim?) savoliga javobda har doim 이/가.</b> Bu eng ishonchli belgi — buni
eslab qolsangiz, xatolaringizning yarmi yoʻqoladi.</div>

<h3>4. Uchta aniq holat</h3>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Holat</th><th>Qaysi biri</th><th>Misol</th></tr>
  <tr><td class="pk-res">Oʻzini tanishtirish</td><td class="pk-end">은/는</td>
      <td class="pk-uz">저<b>는</b> 아프소나입니다.</td></tr>
  <tr><td class="pk-res">Ikki narsani qiyoslash</td><td class="pk-end">은/는</td>
      <td class="pk-uz">이것<b>은</b> 책입니다. 저것<b>은</b> 가방입니다.</td></tr>
  <tr><td class="pk-res">"Kim?" savoliga javob</td><td class="pk-end">이/가</td>
      <td class="pk-uz">지영 씨<b>가</b> 선생님입니다.</td></tr>
  <tr><td class="pk-res">Birinchi marta tilga olinayotgan narsa</td><td class="pk-end">이/가</td>
      <td class="pk-uz">친구<b>가</b> 왔습니다.</td></tr>
  <tr><td class="pk-res">아니다 dan oldin</td><td class="pk-end">이/가</td>
      <td class="pk-uz">저는 의사<b>가</b> 아닙니다.</td></tr>
</table></div>

<h3>5. Ikkalasi bir gapda</h3>

<p>Koʻpincha ikkalasi birga keladi — va bu mutlaqo normal:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저<span class="pe-hl pe-hl--s">는</span>
     이름<span class="pe-hl pe-hl--o">이</span> 벡조드입니다.</p>
  <p class="pe-ex__uz">Menga kelsak, ismim Bekzod.</p>
  <p class="pe-ex__why">저는 — mavzu ("men haqimda"), 이름이 — ega ("ism"). Oʻzbekchada
     ham "menikim ismim…" desa boʻladi.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Bitta gapda <b>ikkita 는 qoʻymang</b> — mavzu bitta boʻladi.
<s>저는 이름은 벡조드입니다</s> notoʻgʻri.</div>

<h3>6. Eng koʻp qilinadigan xato</h3>

<p>Yangi oʻquvchi deyarli hamma joyda <b>는</b> ishlatadi, chunki u birinchi
oʻrganilgan qoʻshimcha. Natijada har bir gap "…ga kelsak" bilan boshlangandek
tuyuladi — go'yo har jumlada mavzuni almashtirayotgandek.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 누가 의사입니까?<br>
     나: <s>지영 씨는 의사입니다.</s> → 지영 씨<b>가</b> 의사입니다.</p>
  <p class="pe-ex__uz">A: Kim shifokor?<br>B: Jiyoung shifokor.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">학생<s>는</s> 왔습니다.</p>
  <p class="pe-good">학생 받침 bilan tugaydi → 학생<b>은</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">"누가 학생입니까?" savoliga: 자수르 씨<s>는</s> 학생입니다.</p>
  <p class="pe-good">"Kim?" savoliga javob → 자수르 씨<b>가</b> 학생입니다.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저<s>는</s> 이름<s>은</s> 벡조드입니다.</p>
  <p class="pe-good">저<b>는</b> 이름<b>이</b> 벡조드입니다 — bitta mavzu, bitta ega.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 의사<s>는</s> 아닙니다.</p>
  <p class="pe-good">아니다 dan oldin har doim 이/가: 의사<b>가</b> 아닙니다.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga nima tushadi? 선생님<span class="pe-blank">?</span> 지영입니다.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>은</strong> — 선생님 받침 (ㅁ) bilan tugaydi.
    "Oʻqituvchiga kelsak, u Jiyoung."</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     "누가 선생님입니까?" savoliga javob bering.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>지영 씨가 선생님입니다.</strong> "Kim?" savoliga
    javobda har doim <b>이/가</b>, chunki javob <em>yangi maʼlumot</em> keltiradi. 씨
    unli bilan tugaydi → 가.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega bu gapda 는 ishlatilgan?<br>
     자수르 씨는 학생입니다. 딜노자 씨는 선생님입니다.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki ikki odam <strong>qiyoslanmoqda</strong>. 는
    ning ostida har doim "boshqasi boshqacha" degan soya turadi — oʻzbekchadagi
    <em>esa</em> kabi: "Jasur talaba, Dilnoza <b>esa</b> oʻqituvchi".</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Xatoni toping: 저는 의사는 아닙니다.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Ikkinchi <strong>는</strong> notoʻgʻri.
    <b>아니다</b> dan oldin har doim <b>이/가</b> turadi: 의사 unli bilan tugagani uchun
    <b>가</b>. Toʻgʻrisi: <strong>저는 의사가 아닙니다.</strong></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Oʻzbekchadagi qaysi soʻz 는 ning maʼnosiga eng yaqin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>"esa"</strong> (yoki "…ga kelsak").
    저는 학생입니다 → "Men<b>ga kelsak</b>, talabaman". Bu tuygʻu sizda allaqachon bor —
    faqat koreyschada u alohida soʻz emas, <em>qoʻshimcha</em>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>은 / 는</b><span>mavzu qoʻshimchasi</span></li>
  <li><b>이 / 가</b><span>ega qoʻshimchasi</span></li>
  <li><b>주제</b><span>mavzu</span></li>
  <li><b>주어</b><span>ega</span></li>
  <li><b>누가</b><span>kim (ega shaklida)</span></li>
  <li><b>이름</b><span>ism</span></li>
  <li><b>이것 / 저것</b><span>bu narsa / anavi narsa</span></li>
  <li><b>어머니</b><span>ona</span></li>
  <li><b>책</b><span>kitob</span></li>
  <li><b>가방</b><span>sumka</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li>Shakl: 받침 bor → <b>은 / 이</b>, 받침 yoʻq → <b>는 / 가</b>.</li>
    <li><b>은/는 = mavzu</b> — oʻzbekcha "<b>esa</b>", "…ga kelsak".</li>
    <li><b>이/가 = ega</b> — "kim?" savoliga javob, yangi maʼlumot.</li>
    <li><b>"누가?" savoliga javobda har doim 이/가.</b></li>
    <li>아니다 dan oldin har doim <b>이/가</b>.</li>
    <li>Bitta gapda <b>bitta mavzu</b> — ikkita 는 qoʻymang.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-13: 있다 / 없다 — bor va yoʻq",
        "category": "korean",
        "order": 13,
        "summary": (
            "Nihoyat haqiqiy kesim: 있습니다 va 없습니다. “Menda kitob bor” tuzilishi "
            "oʻzbekchada ham, koreyschada ham bir xil ishlaydi."
        ),
        "stories": ["저는 친구가 있습니다"],
        "content": """
<h2>PK-13: 있다 / 없다 — bor va yoʻq</h2>

<p>Shu paytgacha siz faqat <b>입니다</b> bilan gap tuzdingiz — ya'ni "A — B dir" turidagi
gaplar. Bugun ikkinchi kesimni olasiz va shu bilan gapira oladigan narsalaringiz
keskin koʻpayadi: nima <em>bor</em>, nima <em>yoʻq</em>, kimda nima <em>bor</em>.
Va yana bir yaxshi xabar — bu qolipning tuzilishi oʻzbekchaga <b>deyarli aynan</b>
mos tushadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>있습니다 va 없습니다 bilan gap tuzasiz</li>
    <li>"Bor" va "ega boʻlmoq" maʼnolarini bir qolipda berasiz</li>
    <li>PK-12 dagi 은/는 va 이/가 ni amalda ishlatasiz</li>
    <li>계시다 — hurmatli shaklni tanib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Egalik va mavjudlik</span>
  <span class="pe-chip pe-chip--s">저는</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">ot + 이/가</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">있습니다</span>
</div>

<h3>1. Shakl</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">있다 — bor</p>
    <p style="font-size:1.3rem">있습니다 / 있습니까?</p>
    <p>Oʻqilishi: <b>[읻씀니다]</b></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">없다 — yoʻq</p>
    <p style="font-size:1.3rem">없습니다 / 없습니까?</p>
    <p>Oʻqilishi: <b>[업씀니다]</b></p>
  </div>
</div>

<div class="pk-say">
  <span class="pk-say__from">있습니다</span>
  <span class="pk-say__arrow">→</span>
  <span class="pk-say__to">[읻씀니다]</span>
  <span class="pk-say__why">받침 ㅆ → [ㄷ], keyin 경음화 va 비음화</span>
</div>

<p>PK-7 va PK-8 dagi uchta qoida shu bitta soʻzda birga ishlaydi: 받침 ㅆ toʻxtab
[ㄷ] boʻladi, undan keyingi ㅅ qattiqlashadi (경음화), va oxirgi ㅂ+ㄴ birikmasi ㅁ
beradi (비음화). Yodlashning hojati yoʻq — bir marta sekin aytib koʻrsangiz, ogʻiz
oʻzi shu yoʻlni topadi.</p>

<h3>2. Birinchi maʼno — mavjudlik</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">책<span class="pe-hl pe-hl--o">이</span>
     <span class="pe-hl pe-hl--v">있습니다</span>.</p>
  <p class="pe-ex__uz">Kitob bor.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">시간<span class="pe-hl pe-hl--o">이</span> 없습니다.</p>
  <p class="pe-ex__uz">Vaqt yoʻq.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
있다/없다 dan oldingi ot <b>이/가</b> qoʻshimchasini oladi — 은/는 emas. Chunki bu ot
gapning <b>egasi</b>: "nima bor?" degan savolga javob beradi.</div>

<h3>3. Ikkinchi maʼno — egalik</h3>

<p>Koreys tilida "menda … bor" degan alohida feʼl yoʻq. Uning oʻrniga <b>mavzu + ega +
있다</b> tuzilishi ishlatiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko"><span class="pe-hl pe-hl--s">저는</span>
     친구<span class="pe-hl pe-hl--o">가</span>
     <span class="pe-hl pe-hl--v">있습니다</span>.</p>
  <p class="pe-ex__uz">Mening doʻstim bor. (Menga kelsak, doʻst bor.)</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu yerda oʻzbek tili sizga katta yordam beradi. Oʻzbekchada ham "egalik" alohida feʼl
bilan emas, <b>"bor" soʻzi</b> bilan beriladi:
<br>• <b>Menda</b> kitob <b>bor</b> → 저는 책이 있습니다
<br>• <b>Menda</b> vaqt <b>yoʻq</b> → 저는 시간이 없습니다
<br>Ingliz tilida bu butunlay boshqa feʼl (<em>have</em>), shuning uchun ingliz tilidan
oʻrganayotgan bola qiynaladi. Sizda esa tuzilma <b>bir xil</b>: kimda + nima + bor.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">지영 씨는 가방이 없습니다.</p>
  <p class="pe-ex__uz">Jiyoungda sumka yoʻq.</p>
</div>

<h3>4. Nega 은/는 va 이/가 bir gapda</h3>

<p>Endi PK-12 dagi farq amalda koʻrinadi. Egalik gapida <b>ikkalasi ham</b> kerak:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Boʻlak</th><th>Qoʻshimcha</th><th>Vazifasi</th></tr>
  <tr><td class="pk-res">저</td><td class="pk-end">는</td>
      <td class="pk-uz">mavzu — kim haqida gapiryapmiz</td></tr>
  <tr><td class="pk-res">친구</td><td class="pk-end">가</td>
      <td class="pk-uz">ega — nima bor</td></tr>
  <tr><td class="pk-res">있습니다</td><td class="pk-end">—</td>
      <td class="pk-uz">kesim — bor</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<s>저는 친구는 있습니다</s> — notoʻgʻri. Bitta gapda bitta mavzu. Ikkinchi boʻlak
<b>이/가</b> olishi shart.</div>

<h3>5. Savol va javob</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 시간이 있습니까?<br>나: 네, 있습니다. / 아니요, 없습니다.</p>
  <p class="pe-ex__uz">A: Vaqtingiz bormi?<br>B: Ha, bor. / Yoʻq, yoʻq.</p>
  <p class="pe-ex__why">Javobda otni takrorlash shart emas — koreyschada bu juda
     tabiiy.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">가: 무엇이 있습니까?<br>나: 책이 있습니다.</p>
  <p class="pe-ex__uz">A: Nima bor?<br>B: Kitob bor.</p>
</div>

<h3>6. 계시다 — odamlar uchun hurmatli shakl</h3>

<p>Agar "bor" deyilayotgan narsa <b>hurmatli odam</b> boʻlsa, 있다 oʻrniga
<b>계시다</b> ishlatiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">선생님이 계십니다.</p>
  <p class="pe-ex__uz">Oʻqituvchi bor / oʻqituvchi shu yerda.</p>
  <p class="pe-ex__why">Narsalar uchun hech qachon 계시다 ishlatilmaydi:
     <s>책이 계십니다</s>.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
계시다 ni hozircha <b>tanib olish</b> darajasida bilsangiz yetarli — oʻzingiz
ishlatishingiz shart emas. Lekin uni eshitganda "demak gap hurmatli odam haqida"
deb tushunasiz. Hurmat tizimini PK-11 da koʻrgan edingiz; mana u feʼlga ham
tarqaladi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">저는 친구<s>는</s> 있습니다.</p>
  <p class="pe-good">저는 친구<b>가</b> 있습니다 — bitta mavzu, keyin ega.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">시간<s>은</s> 없습니다. (oddiy "vaqt yoʻq" demoqchi boʻlsangiz)</p>
  <p class="pe-good">시간<b>이</b> 없습니다. 은 faqat qiyoslash boʻlsa.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">있습니다 ni "it-sup-ni-da" deb oʻqish.</p>
  <p class="pe-good"><b>[읻씀니다]</b> — 경음화 va 비음화 birga ishlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">책이 <s>계십니다</s>.</p>
  <p class="pe-good">계시다 faqat <b>odamlar</b> uchun: 책이 <b>있습니다</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga nima tushadi? 저는 가방<span class="pe-blank">?</span> 있습니다.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>이</strong> — 가방 받침 (ㅇ) bilan tugaydi.
    있다 dan oldingi ot har doim <b>이/가</b> oladi, chunki u gapning egasi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     "Menda vaqt yoʻq" ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>저는 시간이 없습니다.</strong> Tuzilma oʻzbekcha
    bilan bir xil: <em>menda</em> (저는) + <em>vaqt</em> (시간이) + <em>yoʻq</em>
    (없습니다).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega "저는 친구가 있습니다" da ikki xil qoʻshimcha bor?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>저는</strong> — mavzu ("men haqimda"),
    <strong>친구가</strong> — ega ("nima bor"). Bu PK-12 dagi farqning amaliy koʻrinishi:
    bitta gapda bitta mavzu va bitta ega boʻlishi mutlaqo normal.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     "선생님이 계십니다" nima degani va nega 있습니다 emas?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>"Oʻqituvchi bor / shu yerda". <strong>계시다</strong> —
    있다 ning hurmatli shakli va u faqat <em>odamlarga</em> nisbatan ishlatiladi. Narsa
    uchun ishlatilsa (책이 계십니다) kulgili chiqadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Sherbek "저는 시간은 없습니다" dedi. Xato bormi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Odatda ha — toʻgʻrisi <strong>시간이 없습니다</strong>,
    chunki 시간 bu yerda ega. <em>Lekin</em> agar Sherbek "pulim bor, <b>vaqtim esa</b>
    yoʻq" demoqchi boʻlsa, 은 toʻgʻri boʻladi — chunki u qiyoslamoqda. Qoʻshimcha maʼnoni
    oʻzgartiradi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>있습니다</b><span>bor</span></li>
  <li><b>없습니다</b><span>yoʻq</span></li>
  <li><b>계십니다</b><span>bor (hurmatli, odamlar uchun)</span></li>
  <li><b>시간</b><span>vaqt</span></li>
  <li><b>책</b><span>kitob</span></li>
  <li><b>가방</b><span>sumka</span></li>
  <li><b>친구</b><span>doʻst</span></li>
  <li><b>돈</b><span>pul</span></li>
  <li><b>무엇</b><span>nima</span></li>
  <li><b>질문</b><span>savol</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>있습니다</b> = bor · <b>없습니다</b> = yoʻq. Savoli: 있습니까? / 없습니까?</li>
    <li>있다/없다 dan oldingi ot <b>이/가</b> oladi — bu gapning egasi.</li>
    <li>Egalik: <b>mavzu + ega + 있다</b> — oʻzbekcha "menda … bor" bilan bir xil.</li>
    <li>Bitta gapda <b>bitta 는</b>: 저<b>는</b> 친구<b>가</b> 있습니다.</li>
    <li>Talaffuz: <b>[읻씀니다]</b> va <b>[업씀니다]</b>.</li>
    <li><b>계시다</b> — faqat hurmatli odamlar uchun, narsalar uchun emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PK-14: 에 va 에서 — joy va vaqt qoʻshimchalari",
        "category": "korean",
        "order": 14,
        "summary": (
            "Ikkalasi ham oʻzbekchada “-da” boʻlib tarjima qilinadi — aynan shuning "
            "uchun chalkashadi. Farqi bitta savolda hal boʻladi: turibdimi yoki qilyaptimi?"
        ),
        "stories": ["우리 교실에 있습니다"],
        "content": """
<h2>PK-14: 에 va 에서 — joy va vaqt qoʻshimchalari</h2>

<p>Bu ikkala qoʻshimcha ham oʻzbekchaga koʻpincha bitta narsa — <b>"-da"</b> boʻlib
tarjima qilinadi. <em>Maktabda</em> turibman, <em>maktabda</em> oʻqiyman — oʻzbekchada
bir xil, koreyschada esa <b>ikki xil</b>. Mana shu sababdan oʻzbek oʻquvchi bu yerda
adashadi. Yaxshi xabar: farqni ajratish uchun bitta savol yetarli, va bugun shu
savolni oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>에 bilan joy va vaqtni koʻrsatasiz</li>
    <li>에서 ning ikki maʼnosini bilib olasiz</li>
    <li>Bitta savol orqali ikkalasini ajratasiz</li>
    <li>있다/없다 bilan birga toʻliq gap tuzasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ajratuvchi savol</span>
  <span class="pe-chip pe-chip--s">turibdi / bor → 에</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">ish qilyapti → 에서</span>
</div>

<h3>1. 에 — joyda turish</h3>

<p>에 <b>있다 / 없다</b> bilan juftlik hosil qiladi. U narsa yoki odam <em>qayerda
turgani</em>ni koʻrsatadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ko">책이 가방<span class="pe-hl pe-hl--adv">에</span> 있습니다.</p>
  <p class="pe-ex__uz">Kitob sumkada.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ko">지영 씨는 교실<span class="pe-hl pe-hl--adv">에</span> 있습니다.</p>
  <p class="pe-ex__uz">Jiyoung sinfxonada.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>있다 yoki 없다 koʻrsangiz — har doim 에.</b> Bu istisnosiz ishlaydigan qoida va
u sizni xatolarning yarmidan qutqaradi.</div>

<h3>2. 에 — vaqt</h3>

<p>Xuddi shu qoʻshimcha vaqtni ham koʻrsatadi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">아침<span class="pe-hl pe-hl--adv">에</span> 시간이 있습니다.</p>
  <p class="pe-ex__uz">Ertalab vaqtim bor.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Uchta vaqt soʻzi <b>에</b> olmaydi: <b>오늘</b> (bugun), <b>어제</b> (kecha),
<b>내일</b> (ertaga). Ular yolgʻiz ishlatiladi: <s>오늘에</s> emas, shunchaki
<b>오늘</b>.</div>

<h3>3. 에 — yoʻnalish</h3>

<div class="pe-ex">
  <p class="pe-ex__ko">학교<span class="pe-hl pe-hl--adv">에</span> 갑니다.</p>
  <p class="pe-ex__uz">Maktabga boraman.</p>
  <p class="pe-ex__why">가다 (bormoq) va 오다 (kelmoq) bilan 에 "…ga" maʼnosini
     beradi — xuddi oʻzbekcha <b>-ga</b> kabi.</p>
</div>

<h3>4. 에서 — harakat joyi</h3>

<p>Endi ikkinchisi. <b>에서</b> — bu joyda <em>biror ish bajarilayotganini</em>
koʻrsatadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">에 — holat</p>
    <p style="font-size:1.15rem">학교<b>에</b> 있습니다.</p>
    <p>Maktabda<b>man</b>. (turibman)</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">에서 — harakat</p>
    <p style="font-size:1.15rem">학교<b>에서</b> 공부합니다.</p>
    <p>Maktabda <b>oʻqiyman</b>. (ish qilyapman)</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana chalkashlikning sababi: <b>oʻzbekchada ikkalasi ham "-da"</b>.
<br>• Maktab<b>da</b>man → 학교<b>에</b> 있습니다
<br>• Maktab<b>da</b> oʻqiyman → 학교<b>에서</b> 공부합니다
<br>Oʻzbek tili bu farqni belgilamaydi, koreys tili esa belgilaydi. Shuning uchun
tarjimaga tayanmang — <b>kesimga qarang</b>: 있다/없다 boʻlsa 에, harakat feʼli boʻlsa
에서.</div>

<h3>5. 에서 — "…dan"</h3>

<p>에서 ning ikkinchi maʼnosi — <b>kelib chiqish</b>. Bu oʻzbekcha <b>-dan</b> ga toʻgʻri
keladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ko">저는 우즈베키스탄<span class="pe-hl pe-hl--adv">에서</span>
     왔습니다.</p>
  <p class="pe-ex__uz">Men Oʻzbekistondan keldim.</p>
  <p class="pe-ex__why">Tanishuvda eng koʻp ishlatiladigan gaplardan biri —
     hozirdan yodlab qoʻying.</p>
</div>

<h3>6. Joy soʻzlari</h3>

<p>에 bilan birga ishlatiladigan oʻrin soʻzlari — ular otdan <b>keyin</b> keladi,
oʻzbekchadagidek:</p>

<div class="pe-table-wrap"><table class="pk-conj">
  <tr><th>Koreyscha</th><th>Oʻzbekcha</th><th>Misol</th></tr>
  <tr><td class="pk-stem">안</td><td class="pk-uz">ich</td>
      <td class="pk-res">가방 안에 — sumka ichida</td></tr>
  <tr><td class="pk-stem">밖</td><td class="pk-uz">tashqari</td>
      <td class="pk-res">교실 밖에 — sinf tashqarisida</td></tr>
  <tr><td class="pk-stem">위</td><td class="pk-uz">ust</td>
      <td class="pk-res">책상 위에 — stol ustida</td></tr>
  <tr><td class="pk-stem">아래 / 밑</td><td class="pk-uz">ost</td>
      <td class="pk-res">책상 아래에 — stol ostida</td></tr>
  <tr><td class="pk-stem">앞</td><td class="pk-uz">old</td>
      <td class="pk-res">학교 앞에 — maktab oldida</td></tr>
  <tr><td class="pk-stem">뒤</td><td class="pk-uz">orqa</td>
      <td class="pk-res">집 뒤에 — uy orqasida</td></tr>
  <tr><td class="pk-stem">옆</td><td class="pk-uz">yon</td>
      <td class="pk-res">친구 옆에 — doʻst yonida</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Diqqat qiling: <b>가방 안에</b> — "sumka ich<b>ida</b>". Koreyscha ham, oʻzbekcha ham
<em>ot → oʻrin soʻzi → qoʻshimcha</em> tartibida. Ingliz tilida esa teskari
(<em>in the bag</em>). Yana bir joy, oʻzbek tili sizga yordam beradi.</div>

<div class="pe-ex">
  <p class="pe-ex__ko">책이 책상 위에 있습니다.</p>
  <p class="pe-ex__uz">Kitob stol ustida.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad">학교<s>에서</s> 있습니다.</p>
  <p class="pe-good">있다 bilan har doim <b>에</b>: 학교<b>에</b> 있습니다.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>오늘에</s> 시간이 있습니다.</p>
  <p class="pe-good">오늘, 어제, 내일 — <b>에</b> olmaydi:
     <b>오늘</b> 시간이 있습니다.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">저는 우즈베키스탄<s>에</s> 왔습니다. ("Oʻzbekistondan keldim")</p>
  <p class="pe-good">"…dan" maʼnosida <b>에서</b>: 우즈베키스탄<b>에서</b> 왔습니다.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>안 가방에</s> 책이 있습니다.</p>
  <p class="pe-good">Oʻrin soʻzi otdan <b>keyin</b>: <b>가방 안에</b> 책이 있습니다.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga nima tushadi? 지영 씨는 교실<span class="pe-blank">?</span> 있습니다.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>에</strong>. Kesim <b>있습니다</b> — demak bu
    holat, harakat emas. 있다/없다 bilan har doim 에.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Nega oʻzbek oʻquvchi 에 va 에서 ni chalkashtiradi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <strong>oʻzbekchada ikkalasi ham "-da"</strong>:
    "maktab<em>da</em>man" va "maktab<em>da</em> oʻqiyman". Oʻzbek tili bu farqni
    belgilamaydi. Yechim — tarjimaga emas, <b>kesimga</b> qarash.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     "Kitob stol ustida" ni koreyschaga oʻgiring.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>책이 책상 위에 있습니다.</strong> Oʻrin soʻzi
    (위) otdan <em>keyin</em> keladi — xuddi oʻzbekchadagidek "stol ust<b>ida</b>".
    있습니다 bilan 에.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Xatoni toping: 오늘에 시간이 없습니다.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>오늘에</strong> notoʻgʻri. 오늘, 어제, 내일 —
    bu uch soʻz <b>에</b> olmaydi, ular yolgʻiz ishlatiladi. Toʻgʻrisi:
    <strong>오늘 시간이 없습니다.</strong></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bekzod oʻzini tanishtirmoqchi: "Men Oʻzbekistondan keldim." Qaysi qoʻshimcha
     kerak va nega?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>에서</strong> —
    <b>우즈베키스탄에서 왔습니다.</b> Bu 에서 ning ikkinchi maʼnosi: "…dan", ya'ni kelib
    chiqish. Oʻzbekcha <em>-dan</em> ga toʻgʻri keladi. 에 ishlatilsa, "Oʻzbekistonga
    keldim" boʻlib qolardi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>에</b><span>-da, -ga (holat, vaqt, yoʻnalish)</span></li>
  <li><b>에서</b><span>-da (harakat), -dan</span></li>
  <li><b>교실</b><span>sinfxona</span></li>
  <li><b>책상</b><span>stol, parta</span></li>
  <li><b>안 / 밖</b><span>ich / tashqari</span></li>
  <li><b>위 / 아래</b><span>ust / ost</span></li>
  <li><b>앞 / 뒤</b><span>old / orqa</span></li>
  <li><b>옆</b><span>yon</span></li>
  <li><b>오늘 / 어제 / 내일</b><span>bugun / kecha / ertaga</span></li>
  <li><b>아침 / 저녁</b><span>ertalab / kechqurun</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda saqlang</p>
  <ul>
    <li><b>있다/없다 koʻrsangiz — har doim 에.</b> Istisnosiz.</li>
    <li><b>에</b> = holat, vaqt, yoʻnalish. <b>에서</b> = harakat joyi, "…dan".</li>
    <li>Oʻzbekchada ikkalasi ham "-da" — shuning uchun <b>tarjimaga emas, kesimga
        qarang</b>.</li>
    <li><b>오늘, 어제, 내일</b> hech qachon 에 olmaydi.</li>
    <li>Oʻrin soʻzi otdan <b>keyin</b>: 가방 <b>안에</b>, 책상 <b>위에</b>.</li>
    <li>"…dan keldim" = <b>에서 왔습니다</b> — tanishuvda doim kerak.</li>
  </ul>
</div>
""",
    },
]
