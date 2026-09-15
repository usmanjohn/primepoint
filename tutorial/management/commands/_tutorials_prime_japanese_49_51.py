# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-49, PJ-50, PJ-51 (Block D: gapni bogʻlash).

Batchning ipi: PJ-48 aniqlovchi ergash gapni berdi, PJ-49 esa uni bitta
otga — 時 ga — qoʻllaydi, yaʼni yangi grammatika emas. Shundan keyin
shart gaplari boshlanadi: PJ-50 〜たら, PJ-51 〜ば va 〜と. Toʻrtinchisi
(〜なら) PJ-52 da, shuning uchun bu yerdagi taqqoslash jadvali ataylab
uchtalik — uni PJ-52 toʻldiradi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_49_51.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Japanese",
    "category": "japanese",
    "description": (
        "Yapon tili noldan ishonchli N4 gacha — 100 ta dars. Hiragana, katakana, kanji, "
        "grammatika qoliplari, oʻzbekcha tushuntirish va oʻzingiz tekshiradigan mashqlar."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-49: 〜とき — «ganda»",
        "category": "japanese",
        "order": 49,
        "summary": (
            "とき — yangi grammatika emas: bu kecha oʻrgangan aniqlovchi "
            "ergash gap, faqat bitta ot bilan. Lekin uning ichidagi zamon "
            "gapning maʼnosini butunlay oʻzgartiradi."
        ),
        "stories": ["ちいさい ときの なつ"],
        "content": """
<h2>PJ-49: 〜とき — «…ganda»</h2>

<p>Ikkita gapni oʻqing:</p>

<p><ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>く<b>とき</b>、カメラを<ruby>買<rt>か</rt></ruby>いました。<br>
<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>った<b>とき</b>、カメラを<ruby>買<rt>か</rt></ruby>いました。</p>

<p>Ularning farqi bitta harf. Lekin birinchisida kamera
<b>Oʻzbekistonda</b> sotib olingan, ikkinchisida —
<b>Yaponiyada</b>. Bugungi darsning yarmi shu bitta harf haqida.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>とき ning aslida <b>ot</b> ekanini koʻrasiz</li>
    <li>Ichkaridagi zamon nimani oʻzgartirishini bilib olasiz</li>
    <li>Sifat va ot bilan とき ni toʻgʻri ulaysiz</li>
    <li>〜ときに va 〜ときは farqini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">…ganda</span>
  <span class="pe-chip pe-chip--s"><ruby>普通体<rt>ふつうたい</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">とき</span>
</div>

<h3>1. とき yangi grammatika emas</h3>

<p>Mana darsning eng yengil xabari: <b>とき — bu ot</b>. Kanji bilan
<ruby>時<rt>とき</rt></ruby> deb yoziladi va «vaqt», «payt» degani.
Demak «…ganda» degan qolip — kecha oʻrgangan aniqlovchi ergash gapning
oʻzi, faqat aniqlanayotgan ot doim bitta: <ruby>時<rt>とき</rt></ruby>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Aniqlovchi</th><th>Ot</th><th>Natija</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem"><ruby>高<rt>たか</rt></ruby>い</td><td class="pj-end"><ruby>本<rt>ほん</rt></ruby></td>
      <td class="pj-res"><ruby>高<rt>たか</rt></ruby>い<ruby>本<rt>ほん</rt></ruby></td><td class="pj-uz">qimmat kitob</td></tr>
  <tr><td class="pj-stem"><ruby>私<rt>わたし</rt></ruby>が<ruby>読<rt>よ</rt></ruby>んだ</td><td class="pj-end"><ruby>本<rt>ほん</rt></ruby></td>
      <td class="pj-res"><ruby>私<rt>わたし</rt></ruby>が<ruby>読<rt>よ</rt></ruby>んだ<ruby>本<rt>ほん</rt></ruby></td><td class="pj-uz">men oʻqigan kitob</td></tr>
  <tr><td class="pj-stem"><ruby>私<rt>わたし</rt></ruby>が<ruby>読<rt>よ</rt></ruby>んだ</td><td class="pj-end">とき</td>
      <td class="pj-res"><ruby>私<rt>わたし</rt></ruby>が<ruby>読<rt>よ</rt></ruby>んだとき</td><td class="pj-uz">men oʻqiganda</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Shuning uchun だ bu yerda ham な / の boʻladi.</b> とき — ot,
  demak undan oldin PJ-48 ning qoidasi ishlaydi, PJ-46 niki emas:
  <ruby>静<rt>しず</rt></ruby>か<b>な</b>とき,
  <ruby>子<rt>こ</rt></ruby>ども<b>の</b>とき. Hech qanday yangi qoida
  yodlash kerak emas.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>とき dan oldin</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end">oddiy shakl</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べるとき</td><td class="pj-uz">yeyayotganda</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">oʻzi</td>
      <td class="pj-res"><ruby>小<rt>ちい</rt></ruby>さいとき</td><td class="pj-uz">kichkinaligida</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">+ <b>な</b></td>
      <td class="pj-res">ひま<b>な</b>とき</td><td class="pj-uz">boʻsh vaqtda</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end">+ <b>の</b></td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby><b>の</b>とき</td><td class="pj-uz">talabalik paytida</td></tr>
</table></div>

<h3>2. Ichkaridagi zamon — darsning yuragi</h3>

<p>Endi eng muhim qismi. とき dan oldingi feʼl <b>hozirgi</b> yoki
<b>oʻtgan</b> shaklda turishi mumkin, va u gap oxiridagi zamonga
qaramaydi. U faqat bitta narsani aytadi: asosiy ish sodir boʻlgan
paytda, <ruby>時<rt>とき</rt></ruby> dagi ish
<b>tugaganmi yoki yoʻqmi</b>.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h"><ruby>行<rt>い</rt></ruby>くとき</p>
    <p><ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くとき、カメラを<ruby>買<rt>か</rt></ruby>いました。</p>
    <p>Borish hali <b>tugamagan</b> — yoʻlga chiqishdan oldin yoki
    yoʻlda. Kamera Oʻzbekistonda olingan.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h"><ruby>行<rt>い</rt></ruby>ったとき</p>
    <p><ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったとき、カメラを<ruby>買<rt>か</rt></ruby>いました。</p>
    <p>Borish <b>tugagan</b> — yetib borgandan keyin. Kamera
    Yaponiyada olingan.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bu farqni allaqachon qiladi — faqat siz sezmaysiz.</b>
  «Yaponiyaga <em>borayotganda</em> kamera oldim» va «Yaponiyaga
  <em>borganda</em> kamera oldim» — ikki boshqa voqea, shundaymi?
  Yaponchada ayni shu farq feʼlning zamoni bilan koʻrsatiladi:
  <b><ruby>行<rt>い</rt></ruby>くとき</b> = borayotganda,
  <b><ruby>行<rt>い</rt></ruby>ったとき</b> = borganda. Demak siz yangi
  fikrni emas, oʻzingizdagi fikrning yaponcha kiyimini oʻrganyapsiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>るとき、<ruby>電気<rt>でんき</rt></ruby>を<ruby>消<rt>け</rt></ruby>してください。</p>
  <p class="pe-ex__uz">Uydan chiqayotganda chiroqni oʻchiring.</p>
  <p class="pe-ex__why">Chiroq hali uyda turib oʻchiriladi — demak chiqish tugamagan: <b><ruby>出<rt>で</rt></ruby>るとき</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>入<rt>はい</rt></ruby>ったとき、<ruby>先生<rt>せんせい</rt></ruby>はもういました。</p>
  <p class="pe-ex__uz">Sinfga kirganimda oʻqituvchi allaqachon u yerda edi.</p>
  <p class="pe-ex__why">Oʻqituvchini koʻrish uchun avval kirib boʻlish kerak — demak <b><ruby>入<rt>はい</rt></ruby>ったとき</b>.</p>
</div>

<h3>3. Gap oxiridagi zamon alohida yashaydi</h3>

<p>PJ-47 va PJ-48 dagi qoida bu yerda ham ishlaydi, va u shu darsda
eng chalkash koʻrinadi: <b>とき dan oldingi zamon «hozir» ga emas,
asosiy ishga nisbatan oʻlchanadi</b>.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>く</span>
  <span class="pj-joshi__p">とき<small>OT</small></span>
  <span class="pj-joshi__n">カメラ</span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__v"><ruby>買<rt>か</rt></ruby>いました</span>
  <span class="pj-joshi__uz">Gapning oxiri oʻtgan zamonda, ichkarisi esa hozirgi — va bu xato emas.</span>
</div>

<p>Bu chalkashlikning sababi oddiy: koʻp tillarda ergash gapning
zamoni gap oxiridagi feʼlga <em>ergashadi</em>. Yapon tilida esa u
mustaqil. Yaponcha gapning ichi — bu kichkina, yopiq olam: u
faqat oʻz voqeasi haqida gapiradi va tashqaridagi zamonni
koʻrmaydi. Siz buni PJ-47 da koʻrgansiz
(«<ruby>明日<rt>あした</rt></ruby><ruby>来<rt>く</rt></ruby>ると
<ruby>言<rt>い</rt></ruby>いました»), PJ-48 da ham koʻrgansiz
(«<ruby>明日<rt>あした</rt></ruby><ruby>来<rt>く</rt></ruby>る
<ruby>人<rt>ひと</rt></ruby>»), va bugun uchinchi marta koʻryapsiz.
Uchalasi bitta qoidaning uchta koʻrinishi.</p>

<div class="pe-call pe-rule">
  <p><b>Tekshirishning bir soʻzlik usuli.</b> Oʻzingizdan soʻrang:
  «asosiy ish boʻlayotganda, とき dagi ish <em>tugaganmi</em>?»
  Tugagan boʻlsa — <b>た</b>. Tugamagan boʻlsa — <b>lugʻat shakli</b>.
  Hozir soat nechaligi buning ichiga umuman kirmaydi.</p>
</div>

<h3>4. 〜ときに va 〜ときは</h3>

<p>とき ot boʻlgani uchun u boshqa otlardek qoʻshimcha ola oladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Nima qoʻshadi</th><th>Misol</th></tr>
  <tr><td class="pj-stem">とき</td><td class="pj-uz">eng oddiy, eng koʻp ishlatiladigan</td>
      <td class="pj-res"><ruby>小<rt>ちい</rt></ruby>さいとき、よく<ruby>泣<rt>な</rt></ruby>きました</td></tr>
  <tr><td class="pj-stem">ときに</td><td class="pj-uz">aniq bir paytga ishora qiladi</td>
      <td class="pj-res"><ruby>三時<rt>さんじ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたときに<ruby>電話<rt>でんわ</rt></ruby>しました</td></tr>
  <tr><td class="pj-stem">ときは</td><td class="pj-uz">«…ganda esa» — boshqa paytga qarshi qoʻyadi</td>
      <td class="pj-res"><ruby>忙<rt>いそが</rt></ruby>しいときは<ruby>電話<rt>でんわ</rt></ruby>しません</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Shubha boʻlsa quruq とき.</b> に qoʻshish deyarli hech qachon
  xato emas, lekin kerak ham emas. は esa maʼnoni oʻzgartiradi —
  uni faqat «boshqa paytda boshqacha» demoqchi boʻlsangiz qoʻying.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «payt» soʻzi ham xuddi shunday ishlaydi.</b> Siz
  «kelgan <em>payt</em>da», «band <em>payt</em>imda», «bolalik
  <em>payt</em>imda» deysiz — yaʼni oʻzbekchada ham bu qurilmaning
  markazida <b>ot</b> turibdi, grammatik qoʻshimcha emas. Va oʻzbekcha
  ham unga egalik va kelishik qoʻshadi: «paytimda», «paytda»,
  «paytdan». Yaponcha ときに va ときは — aynan shu ish: otga
  qoʻshimcha qoʻyish. Shuning uchun とき ni qoida deb emas,
  <b>soʻz</b> deb eslab qoling — qolgani oʻzidan kelib chiqadi.</p>
</div>

<h3>5. Xotira gapirish — とき ning eng tabiiy ishi</h3>

<p>Yaponchada bolalik haqida gapirishning deyarli yagona yoʻli —
<ruby>小<rt>ちい</rt></ruby>さいとき va
<ruby>子<rt>こ</rt></ruby>どものとき.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>子<rt>こ</rt></ruby>どものとき、<ruby>毎年<rt>まいとし</rt></ruby><ruby>夏<rt>なつ</rt></ruby>に<ruby>村<rt>むら</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました。</p>
  <p class="pe-ex__uz">Bolaligimda har yili yozda qishloqqa borardim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>学生<rt>がくせい</rt></ruby>のとき、この<ruby>店<rt>みせ</rt></ruby>で<ruby>働<rt>はたら</rt></ruby>いていました。</p>
  <p class="pe-ex__uz">Talabalik paytimda shu doʻkonda ishlardim.</p>
  <p class="pe-ex__why">Ot + <b>の</b> + とき. «<ruby>学生<rt>がくせい</rt></ruby>だとき» — notoʻgʻri.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">時</span>
    <span class="pj-kanji__uz">vaqt, payt, soat</span>
    <span class="pj-kanji__on">オン: ジ</span>
    <span class="pj-kanji__kun">KUN: とき</span>
    <span class="pj-kanji__note">時間 (じかん) — vaqt · 三時 (さんじ) — soat uch · 時々 (ときどき) — baʼzan</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">子</span>
    <span class="pj-kanji__uz">bola</span>
    <span class="pj-kanji__on">オン: シ</span>
    <span class="pj-kanji__kun">KUN: こ</span>
    <span class="pj-kanji__note">子ども (こども) — bola · 女の子 (おんなのこ) — qizcha</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Nega «とき» deb yozganimiz maʼqul?</b> Kanji
  <ruby>時<rt>とき</rt></ruby> ham toʻgʻri va kitoblarda uchraydi, lekin
  grammatik qolip sifatida ishlaganda yaponlar odatda uni hiragana
  bilan yozadi. Sabab oddiy: <ruby>時<rt>じ</rt></ruby> kanjisi «soat»
  maʼnosida ham oʻqiladi, hiragana esa oʻquvchini adashtirmaydi.
  Oʻzbekchada ham «-gan payt» va «payt» alohida soʻz sifatida boshqa
  ohangda yozilgani kabi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>だとき</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>の</b>とき — とき ot, demak ot oldida だ emas, <b>の</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ひまだとき</p>
  <p class="pe-fix__good">✓ ひま<b>な</b>とき — な-sifat otdan oldin <b>な</b> kiyadi (PJ-48).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>きますとき</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>くとき — otdan oldin faqat oddiy shakl.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>たとき、<ruby>電気<rt>でんき</rt></ruby>を<ruby>消<rt>け</rt></ruby>してください</p>
  <p class="pe-fix__good">✓ <ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby><b>る</b>とき… — chiroq uydan chiqishdan oldin oʻchiriladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Bolaligimda» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>子<rt>こ</rt></ruby>どものとき</b> — ot + <b>の</b> + とき.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Boʻsh vaqtda» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ひまなとき</b> — ひま な-sifat, demak <b>な</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Yaponiyaga <em>yetib borganimda</em> kamera oldim» — qaysi shakl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>行<rt>い</rt></ruby>ったとき</b> — borish tugagan, demak <b>た</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>___とき、<ruby>手<rt>て</rt></ruby>を<ruby>洗<rt>あら</rt></ruby>います» — boʻsh joyga nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>った</b>: <ruby>帰<rt>かえ</rt></ruby>ったとき. Qoʻlni uyga <em>kirgandan keyin</em> yuviladi — demak qaytish tugagan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega «とき» dan oldin だ turmaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki <b>とき — ot</b>, va otdan oldin だ emas, <b>な</b> (な-sifat) yoki <b>の</b> (ot) turadi. Bu PJ-48 ning qoidasi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>とき (<ruby>時<rt>とき</rt></ruby>)</b> — payt, vaqt</li>
  <li><b><ruby>子<rt>こ</rt></ruby>ども</b> — bola</li>
  <li><b>ひま</b> — boʻsh vaqt (な-sifat)</li>
  <li><b><ruby>電気<rt>でんき</rt></ruby></b> — chiroq, elektr</li>
  <li><b><ruby>消<rt>け</rt></ruby>す</b> — oʻchirmoq (I guruh)</li>
  <li><b><ruby>着<rt>つ</rt></ruby>く</b> — yetib bormoq (I guruh)</li>
  <li><b><ruby>働<rt>はたら</rt></ruby>く</b> — ishlamoq (I guruh)</li>
  <li><b><ruby>村<rt>むら</rt></ruby></b> — qishloq</li>
  <li><b><ruby>洗<rt>あら</rt></ruby>う</b> — yuvmoq (I guruh)</li>
  <li><b><ruby>時々<rt>ときどき</rt></ruby></b> — baʼzan</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>とき — <b>ot</b>, demak undan oldin PJ-48 ning qoidasi: <b>な / の</b>.</li>
    <li><b>Lugʻat shakli</b> = ish tugamagan · <b>た-shakli</b> = ish tugagan.</li>
    <li>Ichkaridagi zamon «hozir» ga emas, <b>asosiy ishga</b> qarab oʻlchanadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-50: Shart 1: 〜たら",
        "category": "japanese",
        "order": 50,
        "summary": (
            "Yaponchaning eng ishonchli shart qolipi. た-shaklga bitta ら "
            "qoʻshiladi — va u «agar», «…gach» hamda «qarasam» degan uch "
            "xil maʼnoni bir oʻzi koʻtaradi."
        ),
        "stories": ["テストが おわったら"],
        "content": """
<h2>PJ-50: Shart 1: 〜たら</h2>

<p>Yapon tilida shart gapining <b>toʻrtta</b> qolipi bor: 〜たら,
〜ば, 〜と va 〜なら. Chet elliklar aynan shu yerda koʻp toʻxtab
qoladi, chunki toʻrttasi ham «agar» deb tarjima qilinadi.</p>

<p>Shuning uchun biz eng foydalisidan boshlaymiz. <b>〜たら</b> —
toʻrttasidan eng keng qamrovlisi va eng xavfsizi. Agar bir umr faqat
shuni ishlatsangiz ham, gapingiz deyarli hech qachon notoʻgʻri
boʻlmaydi. Qolgan uchtasi keyingi ikki darsda.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Har qanday soʻzdan たら shaklini yasaysiz</li>
    <li>«Agar» va «…gach» maʼnolarini ajratasiz</li>
    <li>Kutilmagan kashfiyot たら sini taniysiz</li>
    <li>もし ni qachon qoʻshishni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Shart</span>
  <span class="pe-chip pe-chip--s">た-shakli</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">ら</span>
</div>

<h3>1. Yasalishi — bu ham yangi narsa emas</h3>

<p>PJ-35 da siz た-shaklini oʻrgangansiz. Bugun unga bitta
<b>ら</b> qoʻshiladi. Xolos. Boshqa hech qanday qoida yoʻq —
shuning uchun bu toʻrtta shartning ichida yodlash eng oson
boʻlgani.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>た-shakli</th><th>+ ら</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end"><ruby>行<rt>い</rt></ruby>った</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>ったら</td><td class="pj-uz">borsa</td></tr>
  <tr><td class="pj-stem">Feʼl (inkor)</td><td class="pj-end"><ruby>行<rt>い</rt></ruby>かなかった</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かなかったら</td><td class="pj-uz">bormasa</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end"><ruby>安<rt>やす</rt></ruby>かった</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>かったら</td><td class="pj-uz">arzon boʻlsa</td></tr>
  <tr><td class="pj-stem">い-sifat (inkor)</td><td class="pj-end"><ruby>安<rt>やす</rt></ruby>くなかった</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>くなかったら</td><td class="pj-uz">arzon boʻlmasa</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end"><ruby>静<rt>しず</rt></ruby>かだった</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かだったら</td><td class="pj-uz">tinch boʻlsa</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end"><ruby>雨<rt>あめ</rt></ruby>だった</td>
      <td class="pj-res"><ruby>雨<rt>あめ</rt></ruby>だったら</td><td class="pj-uz">yomgʻir boʻlsa</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha <em>-sa</em> ning aynan oʻzi.</b> «Yomgʻir yogʻ<b>sa</b>,
  bormayman» — <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っ<b>たら</b>、
  <ruby>行<rt>い</rt></ruby>きません. Ikkala tilda ham shart gap
  <em>oldinda</em> turadi va natija keyin keladi. Ingliz tilida esa u
  ikkala tomonga ham qoʻyilishi mumkin — shuning uchun oʻzbek
  oʻquvchisi bu yerda ustunlikka ega.</p>
</div>

<p>Bitta narsani darrov aytib qoʻyish kerak: <b>たら ning oʻtgan
zamonga hech qanday aloqasi yoʻq</b>. た-shakli bu yerda zamon emas,
shunchaki <em>yasash uchun olingan shakl</em> — xuddi PJ-35 dagi
〜たことがあります da boʻlgani kabi. «<ruby>安<rt>やす</rt></ruby>かったら
<ruby>買<rt>か</rt></ruby>います» gapi kelajak haqida, garchi ichida
かった tursa ham. Buni boshda koʻz ilgʻamaydi, shuning uchun
qoidani shunday eslang: <em>た-shakli — qurilish materiali, zamon
emas</em>.</p>

<h3>2. Birinchi maʼno: «agar»</h3>

<p>Eng oddiy ishlatilishi — hali boʻlmagan, boʻlishi ham
noaniq narsa.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>安<rt>やす</rt></ruby>かったら<ruby>買<rt>か</rt></ruby>います。</p>
  <p class="pe-ex__uz">Arzon boʻlsa, sotib olaman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>時間<rt>じかん</rt></ruby>がなかったら、<ruby>明日<rt>あした</rt></ruby>でもいいです。</p>
  <p class="pe-ex__uz">Vaqtingiz boʻlmasa, ertaga ham boʻladi.</p>
</div>

<h3>3. Ikkinchi maʼno: «…gach» — aniq kelajak</h3>

<p>Mana bu yerda oʻquvchilar koʻp adashadi. たら har doim «agar»
degani emas. Agar shartdagi ish <b>albatta boʻladigan</b> narsa
boʻlsa, たら «…gandan keyin» degan maʼnoni beradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ったら<ruby>電話<rt>でんわ</rt></ruby>します。</p>
  <p class="pe-ex__uz">Uyga borgach telefon qilaman.</p>
  <p class="pe-ex__why">«Agar uyga borsam» emas — uyga borish aniq. Demak bu <b>vaqt</b>, shart emas.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">テストが<ruby>終<rt>お</rt></ruby>わったら、<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます。</p>
  <p class="pe-ex__uz">Imtihon tugagach kinoga boramiz.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ham bitta qoʻshimchani ikki ishga soladi.</b>
  «Uyga bor<em>sam</em> telefon qilaman» — bu yerda «-sam» shubha emas,
  vaqt. «Yomgʻir yogʻ<em>sa</em> bormayman» — bu esa haqiqiy shubha.
  Farqni gapning oʻzi emas, <b>mazmun</b> koʻrsatadi: ish albatta
  boʻladimi yoki yoʻqmi. Yaponchada ham xuddi shunday.</p>
</div>

<h3>4. Uchinchi maʼno: kutilmagan kashfiyot</h3>

<p>Eng chiroyli ishlatilishi. Agar <b>ikkala qism ham oʻtgan
zamonda</b> boʻlsa, たら «bordim — va koʻrdimki…» degan maʼnoni
beradi. Bu shart emas: ish allaqachon boʻlgan, va ikkinchi qism
gapiruvchi uchun <b>kutilmagan</b> boʻlib chiqqan.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ったら、<ruby>手紙<rt>てがみ</rt></ruby>がありました。</p>
  <p class="pe-ex__uz">Uyga borsam, xat turibdi.</p>
  <p class="pe-ex__why">Ikkala feʼl ham oʻtgan zamonda. Gapiruvchi xatni kutmagan edi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けたら、<ruby>雪<rt>ゆき</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っていました。</p>
  <p class="pe-ex__uz">Derazani ochsam, qor yogʻayotgan ekan.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu oʻzbekchada ham aynan shunday aytiladi.</b> «Uyga
  <em>borsam</em>, xat turibdi», «Derazani <em>ochsam</em>, qor
  yogʻyapti» — oʻzbek tilidagi bu «-sam» ham shart emas, kashfiyot.
  Yapon tili bu maʼno uchun alohida qolip oʻylab topmagan, xuddi
  oʻzbek tilidek. Shuning uchun uni tarjima qilib emas,
  <b>tanib</b> oʻrganish kerak: <em>ikkala qism ham oʻtgan
  zamondami — demak bu kashfiyot</em>.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Bu maʼnoda ikkinchi qism sizga bogʻliq boʻlmasligi kerak.</b>
  «<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ったら、
  ごはんを<ruby>食<rt>た</rt></ruby>べました» — notabiiy, chunki ovqat
  yeyishni siz oʻzingiz qilgansiz, u kutilmagan emas. Bunday holatda
  PJ-37 dagi <b>〜てから</b> ni ishlating.</p>
</div>

<p>Bu uchinchi maʼnoni tanib olishning ikkita belgisi bor, va
ikkalasi ham gapning oʻzida koʻrinib turadi. Birinchisi:
<b>ikkala qism ham oʻtgan zamonda</b>. Ikkinchisi: ikkinchi qism
gapiruvchining <b>ixtiyorida emas</b> — xat allaqachon kelgan, qor
allaqachon yogʻayotgan edi. Agar shu ikkisi ham bor boʻlsa, gapni
«agar» deb tarjima qilmang: u shart emas, hikoya.</p>

<h3>5. もし — ixtiyoriy kuchaytirgich</h3>

<p><b>もし</b> gap boshida turadi va «agar» degan maʼnoni
kuchaytiradi. U grammatik jihatdan majburiy emas — gapni たら
allaqachon shart qilib turibdi — lekin tinglovchini oldindan
ogohlantiradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">もし<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったら、<ruby>試合<rt>しあい</rt></ruby>はありません。</p>
  <p class="pe-ex__uz">Agar yomgʻir yogʻsa, oʻyin boʻlmaydi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>もし ni «…gach» maʼnosi bilan qoʻshmang.</b>
  «もし<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ったら
  <ruby>電話<rt>でんわ</rt></ruby>します» gʻalati eshitiladi — uyga
  borishingizga shubha yoʻq-ku. もし faqat haqiqatan ham noaniq
  narsalar bilan keladi.</p>
</div>

<h3>6. Nima uchun たら eng xavfsiz</h3>

<p>Keyingi darsda 〜ば va 〜と keladi, va ularning ikkalasida ham
qattiq cheklovlar bor: nima bilan ishlatib boʻlmasligi haqida
alohida qoidalar. <b>〜たら da esa bunday cheklov yoʻq</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Gap oxirida</th><th>たら bilan</th><th>Misol</th></tr>
  <tr><td class="pj-stem">Buyruq / iltimos</td><td class="pj-end">✓ boʻladi</td>
      <td class="pj-res"><ruby>着<rt>つ</rt></ruby>いたら<ruby>電話<rt>でんわ</rt></ruby>してください</td></tr>
  <tr><td class="pj-stem">Taklif</td><td class="pj-end">✓ boʻladi</td>
      <td class="pj-res"><ruby>暇<rt>ひま</rt></ruby>だったら<ruby>行<rt>い</rt></ruby>きましょう</td></tr>
  <tr><td class="pj-stem">Xohish</td><td class="pj-end">✓ boʻladi</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>かったら<ruby>買<rt>か</rt></ruby>いたいです</td></tr>
  <tr><td class="pj-stem">Oʻtgan zamon</td><td class="pj-end">✓ boʻladi</td>
      <td class="pj-res"><ruby>開<rt>あ</rt></ruby>けたら<ruby>雪<rt>ゆき</rt></ruby>でした</td></tr>
</table></div>

<p>Jadvalga diqqat bilan qarang: toʻrtta qatorning toʻrttasida ham
belgi bir xil. Keyingi darsda esa oʻsha jadval 〜と uchun deyarli
boʻm-boʻsh boʻlib chiqadi. Aynan shu farq «shubha boʻlsa たら» degan
maslahatning butun sababi — たら ni qayerga qoʻysangiz ham, u sizni
xato qildirmaydi.</p>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">終</span>
    <span class="pj-kanji__uz">tugamoq, oxir</span>
    <span class="pj-kanji__on">オン: シュウ</span>
    <span class="pj-kanji__kun">KUN: お(わる)</span>
    <span class="pj-kanji__note">終わる (おわる) — tugamoq · 最終 (さいしゅう) — eng oxirgi</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">開</span>
    <span class="pj-kanji__uz">ochmoq, ochilmoq</span>
    <span class="pj-kanji__on">オン: カイ</span>
    <span class="pj-kanji__kun">KUN: あ(ける), あ(く), ひら(く)</span>
    <span class="pj-kanji__note">開ける (あける) — ochmoq · 開く (あく) — ochilmoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>くたら</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>っ<b>たら</b> — ら た-shaklga qoʻshiladi, lugʻat shakliga emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>安<rt>やす</rt></ruby>いだったら</p>
  <p class="pe-fix__good">✓ <ruby>安<rt>やす</rt></ruby><b>かったら</b> — い-sifatning た-shakli かった.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>かったら</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>だったら</b> — ot だった oladi, かった emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ もし<ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ったら<ruby>電話<rt>でんわ</rt></ruby>します</p>
  <p class="pe-fix__good">✓ <ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ったら… — uyga qaytish aniq, demak もし oʻrinsiz.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>食<rt>た</rt></ruby>べる ning たら shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べたら</b> — た-shakli <ruby>食<rt>た</rt></ruby>べた, unga ら.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>高<rt>たか</rt></ruby>い ning たら shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>高<rt>たか</rt></ruby>かったら</b> — い-sifatning た-shakli かった.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «<ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたら<ruby>電話<rt>でんわ</rt></ruby>してください» — bu «agar» maʼnosidami?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yoʻq. Bekatga yetib borish aniq, demak bu <b>«…gach»</b>: «bekatga yetgach telefon qiling».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けたら、<ruby>雪<rt>ゆき</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っていました» — bu qaysi maʼno?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Kutilmagan kashfiyot</b> — ikkala qism ham oʻtgan zamonda. «Derazani ochsam, qor yogʻayotgan ekan.»</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Yomgʻir yogʻmasa boramiz» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>らなかったら<ruby>行<rt>い</rt></ruby>きます</b> — inkorning た-shakli なかった, unga ら.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜たら</b> — agar…, …gach</li>
  <li><b>もし</b> — agar (kuchaytirgich)</li>
  <li><b><ruby>終<rt>お</rt></ruby>わる</b> — tugamoq (I guruh)</li>
  <li><b><ruby>開<rt>あ</rt></ruby>ける</b> — ochmoq (II guruh)</li>
  <li><b><ruby>窓<rt>まど</rt></ruby></b> — deraza</li>
  <li><b><ruby>雪<rt>ゆき</rt></ruby></b> — qor</li>
  <li><b><ruby>手紙<rt>てがみ</rt></ruby></b> — xat</li>
  <li><b><ruby>試合<rt>しあい</rt></ruby></b> — oʻyin, musobaqa</li>
  <li><b><ruby>暇<rt>ひま</rt></ruby></b> — boʻsh vaqt (な-sifat)</li>
  <li><b><ruby>駅<rt>えき</rt></ruby></b> — bekat</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>た-shakli + ら</b> — boshqa hech qanday qoida yoʻq.</li>
    <li>Ish aniq boʻlsa — «…gach»; noaniq boʻlsa — «agar».</li>
    <li>Ikkala qism ham oʻtgan zamonda boʻlsa — bu <b>kashfiyot</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-51: Shart 2: 〜ば va 〜と",
        "category": "japanese",
        "order": 51,
        "summary": (
            "Ikkinchi va uchinchi shart qolipi. 〜ば — mantiqiy shart va "
            "maqollar tili; 〜と — tugma bosilsa suv chiqadi degan "
            "avtomatik natija, va uning bitta qattiq taqiqi bor."
        ),
        "stories": ["じどうはんばいきの なか"],
        "content": """
<h2>PJ-51: Shart 2: 〜ば va 〜と</h2>

<p>Yaxshi xabar bilan boshlaymiz: <b>ば ni siz PJ-33 dan beri
ishlatib kelyapsiz</b>. «Qilishim kerak» degan qolipni eslang —
<ruby>行<rt>い</rt></ruby>か<b>なければ</b>なりません. Oʻsha
<b>なければ</b> ning ichidagi ば aynan bugungi ば.</p>

<p>Demak bugun oʻrganadiganingiz ikkita narsa: ば ni boshqa
feʼllardan ham yasash, va uning yonidagi uchinchi shart — <b>と</b>.
と esa butunlay boshqa ish qiladi: u «agar» emas,
<b>«har doim shunday boʻladi»</b> degani.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Har uch guruh feʼlidan ば shaklini yasaysiz</li>
    <li>ば qachon tabiiy eshitilishini bilib olasiz</li>
    <li>と ning avtomatik natija maʼnosini tushunasiz</li>
    <li>と ning bitta qattiq taqigʻini yodlab olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki shart</span>
  <span class="pe-chip pe-chip--s">え-qator + ば</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v"><ruby>普通体<rt>ふつうたい</rt></ruby> + と</span>
</div>

<h3>1. ば yasalishi — う-qator え-qatorga tushadi</h3>

<p>PJ-20 da <ruby>行<rt>い</rt></ruby>き<b>ます</b> uchun oxirgi bogʻin
<b>い-qator</b>ga tushgan edi. Bu safar u <b>え-qator</b>ga tushadi
va ustiga ば qoʻshiladi.</p>

<div class="pj-group">
  <div class="pj-group__c">
    <p class="pj-group__h">I — <ruby>五段<rt>ごだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>行<rt>い</rt></ruby>く → <ruby>行<rt>い</rt></ruby>けば</p>
    <p>Oxirgi bogʻin え-qatorga: く→け, む→め, す→せ, う→え, つ→て, ぐ→げ, ぶ→べ, る→れ.</p>
  </div>
  <div class="pj-group__c pj-group__c--2">
    <p class="pj-group__h">II — <ruby>一段<rt>いちだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>食<rt>た</rt></ruby>べる → <ruby>食<rt>た</rt></ruby>べれば</p>
    <p>る tushadi, れば qoʻyiladi. Yana eng oson guruh.</p>
  </div>
  <div class="pj-group__c pj-group__c--3">
    <p class="pj-group__h">III — <ruby>不規則<rt>ふきそく</rt></ruby></p>
    <p class="pj-group__ex">する → すれば · <ruby>来<rt>く</rt></ruby>る → <ruby>来<rt>く</rt></ruby>れば</p>
    <p>Faqat ikkita, va ikkalasi ham れば bilan tugaydi.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Guruh</th><th>ば-shakli</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-uz">I</td>
      <td class="pj-res"><ruby>読<rt>よ</rt></ruby>めば</td><td class="pj-uz">oʻqisa</td></tr>
  <tr><td class="pj-stem"><ruby>話<rt>はな</rt></ruby>す</td><td class="pj-uz">I</td>
      <td class="pj-res"><ruby>話<rt>はな</rt></ruby>せば</td><td class="pj-uz">gapirsa</td></tr>
  <tr><td class="pj-stem"><ruby>買<rt>か</rt></ruby>う</td><td class="pj-uz">I</td>
      <td class="pj-res"><ruby>買<rt>か</rt></ruby>えば</td><td class="pj-uz">sotib olsa</td></tr>
  <tr><td class="pj-stem"><ruby>待<rt>ま</rt></ruby>つ</td><td class="pj-uz">I</td>
      <td class="pj-res"><ruby>待<rt>ま</rt></ruby>てば</td><td class="pj-uz">kutsa</td></tr>
  <tr><td class="pj-stem"><ruby>急<rt>いそ</rt></ruby>ぐ</td><td class="pj-uz">I</td>
      <td class="pj-res"><ruby>急<rt>いそ</rt></ruby>げば</td><td class="pj-uz">shoshilsa</td></tr>
  <tr><td class="pj-stem"><ruby>帰<rt>かえ</rt></ruby>る</td><td class="pj-uz">I</td>
      <td class="pj-res"><ruby>帰<rt>かえ</rt></ruby>れば</td><td class="pj-uz">qaytsa</td></tr>
  <tr><td class="pj-stem"><ruby>見<rt>み</rt></ruby>る</td><td class="pj-uz">II</td>
      <td class="pj-res"><ruby>見<rt>み</rt></ruby>れば</td><td class="pj-uz">koʻrsa</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b><ruby>帰<rt>かえ</rt></ruby>る bu yerda sizni aldamaydi.</b> U る bilan
  tugaydi va PJ-27 dagi istisno roʻyxatida (<ruby>帰<rt>かえ</rt></ruby>る,
  <ruby>入<rt>はい</rt></ruby>る, <ruby>走<rt>はし</rt></ruby>る, <ruby>知<rt>し</rt></ruby>る) —
  yaʼni I guruh feʼli. Lekin ば da bu farqning
  <em>ahamiyati yoʻq</em>: I guruh boʻyicha る → れ + ば ham,
  II guruh boʻyicha る → れば ham bir xil natija beradi —
  <b><ruby>帰<rt>かえ</rt></ruby>れば</b>. Istisno ない va て shakllarida
  tishlaydi (<ruby>帰<rt>かえ</rt></ruby>らない, <ruby>帰<rt>かえ</rt></ruby>って — hech
  qachon «<ruby>帰<rt>かえ</rt></ruby>ない», «<ruby>帰<rt>かえ</rt></ruby>て» emas), ば da
  esa dam oladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ham majburiyatni shartdan yasaydi.</b> «Bor<em>masam
  boʻlmaydi</em>» — bu, soʻzma-soʻz olganda, shart gap: <em>agar
  bormasam, ish chiqmaydi</em>. Yaponcha
  <ruby>行<rt>い</rt></ruby>か<b>なければ</b>なりません ham aynan
  shunday tuzilgan: «bormasa — boʻlmaydi». Yaʼni PJ-33 da siz
  majburiyat qolipini emas, <b>shart gapni</b> yodlagan ekansiz —
  faqat buni endi bilyapsiz.</p>
</div>

<h3>2. Sifat va inkorning ば shakli</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Qoida</th><th>Misol</th></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">い → ければ</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>い → <ruby>安<rt>やす</rt></ruby>ければ</td></tr>
  <tr><td class="pj-stem">Feʼl inkori</td><td class="pj-end">ない → なければ</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かない → <ruby>行<rt>い</rt></ruby>かなければ</td></tr>
  <tr><td class="pj-stem">い-sifat inkori</td><td class="pj-end">くない → くなければ</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>くない → <ruby>安<rt>やす</rt></ruby>くなければ</td></tr>
  <tr><td class="pj-stem">いい</td><td class="pj-end">istisno</td>
      <td class="pj-res">いい → よければ</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>ない har doim い-sifatdek yuradi.</b> PJ-45 da siz uni
  <ruby>行<rt>い</rt></ruby>かなかった da koʻrgansiz (い → かった),
  bugun esa <ruby>行<rt>い</rt></ruby>かなければ da koʻryapsiz
  (い → ければ). Bitta qoida, ikki joyda ishlayapti. Shuning uchun
  PJ-33 dagi <b>なければなりません</b> aslida shart gap: «qilmasang —
  boʻlmaydi».</p>
</div>

<div class="pe-call pe-tip">
  <p><b>な-sifat va ot ば olmaydi.</b> «<ruby>静<rt>しず</rt></ruby>か
  ならば» degan shakl bor, lekin u kitobiy va kam uchraydi.
  Ular uchun keyingi darsdagi <b>なら</b> ishlatiladi — shuning uchun
  PJ-52 bu jadvalning boʻsh katagini toʻldiradi.</p>
</div>

<h3>3. ば nima uchun ishlatiladi</h3>

<p>ば — <b>mantiqiy shart</b>: «bu boʻlsa, u boʻladi». U koʻpincha
maslahat, maqol va umumiy haqiqat gaplarida chiqadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>安<rt>やす</rt></ruby>ければ<ruby>買<rt>か</rt></ruby>います。</p>
  <p class="pe-ex__uz">Arzon boʻlsa sotib olaman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>急<rt>いそ</rt></ruby>げば<ruby>間<rt>ま</rt></ruby>に<ruby>合<rt>あ</rt></ruby>います。</p>
  <p class="pe-ex__uz">Shoshilsak ulguramiz.</p>
  <p class="pe-ex__why">Sof mantiq: shoshilish → ulgurish. Aynan ば ning maydoni.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>練習<rt>れんしゅう</rt></ruby>すればできます。</p>
  <p class="pe-ex__uz">Mashq qilsangiz, uddalaysiz.</p>
</div>

<h3>4. と — «har doim shunday boʻladi»</h3>

<p>Uchinchi shart butunlay boshqa tabiatga ega. <b>と</b> shubha
bildirmaydi; u <b>avtomatik, har safar takrorlanadigan natija</b>ni
aytadi. Mashina, tabiat qonuni, yoʻl koʻrsatish — hammasi と bilan.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Avtomatik natija</span>
  <span class="pe-chip pe-chip--s">lugʻat shakli</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">と</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">natija</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">このボタンを<ruby>押<rt>お</rt></ruby>すと、<ruby>水<rt>みず</rt></ruby>が<ruby>出<rt>で</rt></ruby>ます。</p>
  <p class="pe-ex__uz">Bu tugmani bossangiz, suv chiqadi.</p>
  <p class="pe-ex__why">Har safar. Shubha yoʻq — shuning uchun たら emas, <b>と</b>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>右<rt>みぎ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くと、<ruby>駅<rt>えき</rt></ruby>があります。</p>
  <p class="pe-ex__uz">Oʻngga borsangiz, bekat boʻladi.</p>
  <p class="pe-ex__why">Yoʻl koʻrsatish — yaponcha xaritaning tili.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu «-sa, doim» degan ohang.</b> «Tugmani bossang,
  suv chiqadi» — siz buni ehtimol deb emas, <em>qoida</em> deb
  aytyapsiz. Oʻzbek tili bu farqni ohang bilan koʻrsatadi, yapon tili
  esa alohida qoʻshimcha bilan. Shuning uchun と ni «agar» deb emas,
  <b>«…sa, har doim»</b> deb tarjima qilib oʻrganing — shunda uni
  qayerga qoʻyish kerakligi oʻzi aniq boʻladi.</p>
</div>

<h3>5. と ning qattiq taqigʻi</h3>

<p>Mana bu darsdagi eng muhim bitta qoida, va u istisnosiz:</p>

<div class="pe-call pe-warn">
  <p><b>と dan keyin buyruq, iltimos, taklif yoki xohish
  kelolmaydi.</b> Sababi mantiqiy: と «har doim shunday boʻladi»
  degani, shuning uchun undan keyin <em>tabiat</em> turishi kerak,
  sizning irodangiz emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>時間<rt>じかん</rt></ruby>があると、<ruby>来<rt>き</rt></ruby>てください</p>
  <p class="pe-fix__good">✓ <ruby>時間<rt>じかん</rt></ruby>があっ<b>たら</b>、<ruby>来<rt>き</rt></ruby>てください — iltimos bor, demak たら.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>安<rt>やす</rt></ruby>いと<ruby>買<rt>か</rt></ruby>いたいです</p>
  <p class="pe-fix__good">✓ <ruby>安<rt>やす</rt></ruby>かっ<b>たら</b><ruby>買<rt>か</rt></ruby>いたいです — xohish bor, demak たら.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Shuning uchun «shubha boʻlsa たら» qoidasi ishlaydi.</b>
  たら da hech qanday cheklov yoʻq: undan keyin buyruq ham, taklif
  ham, xohish ham, oʻtgan zamon ham kela oladi. と va ば esa tor
  maydonlarga ega.</p>
</div>

<h3>6. Uchtasi bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th></th><th>〜たら</th><th>〜ば</th><th>〜と</th></tr>
  <tr><td class="pj-stem">Asosiy maʼnosi</td><td class="pj-uz">agar · …gach · kashfiyot</td>
      <td class="pj-uz">mantiqiy shart</td><td class="pj-uz">har doim shunday</td></tr>
  <tr><td class="pj-stem">Keyin buyruq/iltimos</td><td class="pj-res">✓</td>
      <td class="pj-uz">koʻpincha ✗</td><td class="pj-uz">✗ hech qachon</td></tr>
  <tr><td class="pj-stem">Oʻtgan zamon natija</td><td class="pj-res">✓</td>
      <td class="pj-uz">✗</td><td class="pj-uz">✓ (kashfiyot maʼnosida)</td></tr>
  <tr><td class="pj-stem">Ot va な-sifat bilan</td><td class="pj-res">✓ だったら</td>
      <td class="pj-uz">kam</td><td class="pj-uz">✓ だと</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bitta <em>-sa</em>, yaponchada toʻrtta shart.</b>
  «Arzon boʻl<em>sa</em> olaman», «Tugmani bos<em>sa</em>ng suv
  chiqadi», «Uyga bor<em>sa</em>m telefon qilaman» — oʻzbekcha
  uchalasini ham bitta qoʻshimcha bilan aytadi. Yaponchada esa siz
  <b>tanlashingiz</b> kerak, va tanlov maʼno haqida emas,
  <em>aniqlik darajasi</em> haqida: ish har safar shundaymi (と),
  mantiqan kelib chiqadimi (ば), yoki shunchaki boʻlishi mumkinmi
  (たら). Shuning uchun bu darsni «yangi soʻzlar» deb emas,
  <b>«bitta oʻzbekcha qoʻshimchani uchga ajratish»</b> deb
  oʻrganing.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Jadval ataylab uchta ustunli.</b> Toʻrtinchisi — <b>なら</b> —
  keyingi darsda keladi va u boshqalardan ham farq qiladi: なら
  <em>birov aytgan narsaga</em> javob beradi. PJ-52 shu ustunni
  qoʻshadi va toʻrttasini bitta jadvalda yopadi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">押</span>
    <span class="pj-kanji__uz">bosmoq, itarmoq</span>
    <span class="pj-kanji__on">オン: オウ</span>
    <span class="pj-kanji__kun">KUN: お(す)</span>
    <span class="pj-kanji__note">押す (おす) — bosmoq · 押し入れ (おしいれ) — devor shkafi</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">急</span>
    <span class="pj-kanji__uz">shoshilmoq, tez</span>
    <span class="pj-kanji__on">オン: キュウ</span>
    <span class="pj-kanji__kun">KUN: いそ(ぐ)</span>
    <span class="pj-kanji__note">急ぐ (いそぐ) — shoshilmoq · 急行 (きゅうこう) — tezyurar poyezd</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>食<rt>た</rt></ruby>べば</p>
  <p class="pe-fix__good">✓ <ruby>食<rt>た</rt></ruby><b>べれば</b> — II guruh る ni れば ga almashtiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>安<rt>やす</rt></ruby>いば</p>
  <p class="pe-fix__good">✓ <ruby>安<rt>やす</rt></ruby><b>ければ</b> — い-sifat い ni ければ ga almashtiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>来<rt>こ</rt></ruby>ば</p>
  <p class="pe-fix__good">✓ <ruby>来<rt>く</rt></ruby><b>れば</b> — <ruby>来<rt>く</rt></ruby>る III guruh, va uning ば shakli れば bilan tugaydi. こ faqat ない-shaklida chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>くと<ruby>電話<rt>でんわ</rt></ruby>してください</p>
  <p class="pe-fix__good">✓ <ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>い<b>たら</b>… — と dan keyin iltimos turolmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>読<rt>よ</rt></ruby>む ning ば shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>読<rt>よ</rt></ruby>めば</b> — む め ga tushadi (I guruh).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>見<rt>み</rt></ruby>る ning ば shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>見<rt>み</rt></ruby>れば</b> — II guruh, る → れば.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>高<rt>たか</rt></ruby>い ning ば shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>高<rt>たか</rt></ruby>ければ</b> — い → ければ.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>時間<rt>じかん</rt></ruby>があると<ruby>来<rt>き</rt></ruby>てください» — nima xato?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>と dan keyin <b>iltimos turolmaydi</b>. Toʻgʻrisi — <ruby>時間<rt>じかん</rt></ruby>があっ<b>たら</b><ruby>来<rt>き</rt></ruby>てください.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Bu tugmani bossang, eshik ochiladi» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>このボタンを<ruby>押<rt>お</rt></ruby>すと、ドアが<ruby>開<rt>あ</rt></ruby>きます</b> — avtomatik natija, demak <b>と</b>.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ば</b> — mantiqiy shart</li>
  <li><b>〜と</b> — har doim shunday boʻladi</li>
  <li><b><ruby>押<rt>お</rt></ruby>す</b> — bosmoq (I guruh)</li>
  <li><b><ruby>急<rt>いそ</rt></ruby>ぐ</b> — shoshilmoq (I guruh)</li>
  <li><b><ruby>間<rt>ま</rt></ruby>に<ruby>合<rt>あ</rt></ruby>う</b> — ulgurmoq (I guruh)</li>
  <li><b>ボタン</b> — tugma</li>
  <li><b>ドア</b> — eshik</li>
  <li><b><ruby>開<rt>あ</rt></ruby>く</b> — ochilmoq (I guruh)</li>
  <li><b><ruby>出<rt>で</rt></ruby>る</b> — chiqmoq (II guruh)</li>
  <li><b><ruby>右<rt>みぎ</rt></ruby></b> — oʻng</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>え-qator + ば</b>; い-sifat <b>ければ</b>; ない → <b>なければ</b>.</li>
    <li>と = «har doim shunday», shuning uchun keyin <b>buyruq turolmaydi</b>.</li>
    <li>Shubha boʻlsa — <b>たら</b>. Unda cheklov yoʻq.</li>
  </ul>
</div>
""",
    },
]
