# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-52, PJ-53, PJ-54 (Block D: gapni bogʻlash).

PJ-52 shart gaplarini yopadi (toʻrttasi bir jadvalda), keyin ikkita
bogʻlovchi juftlik keladi: sabab (から / ので) va qarama-qarshilik
(が / けど). Uchalasida ham bitta naqsh takrorlanadi — <b>ikkitadan
bittasi rasmiyroq, ikkinchisi yumshoqroq</b>, va tanlov maʼnoda emas,
ohangda.

⚠️ PJ-54 da が ikki xil ish qiladi: qoʻshimcha (ega) va bogʻlovchi
(«lekin»). Ikkalasi bir dars ichida yonma-yon koʻrsatiladi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_52_54.py --author=prime
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
        "title": "PJ-52: Shart 3: 〜なら — va toʻrttasining farqi bir jadvalda",
        "category": "japanese",
        "order": 52,
        "summary": (
            "Toʻrtinchi va oxirgi shart. なら boshqalardan tubdan farq "
            "qiladi: u birov aytgan gapga javob beradi, va undan keyingi "
            "ish shartdan OLDIN ham boʻlishi mumkin."
        ),
        "stories": ["きょうとへ いくなら"],
        "content": """
<h2>PJ-52: Shart 3: 〜なら — va toʻrttasining farqi bir jadvalda</h2>

<p>Doʻstingiz sizga aytdi: «Yaponiyaga boryapman.» Siz maslahat
bermoqchisiz. Yaponchada bu gap <b>なら</b> bilan boshlanadi:</p>

<p><ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>く<b>なら</b>、<ruby>京都<rt>きょうと</rt></ruby>がいいですよ。</p>

<p>Mana bugungi darsning kaliti: <b>なら dagi shart sizniki emas —
u suhbatdoshingizdan olingan</b>. Boshqa uchtasi olamni tasvirlaydi;
なら esa suhbatga javob beradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>なら ni yasaysiz — va nega だ tushishini bilib olasiz</li>
    <li>なら va たら dagi <b>vaqt tartibi</b> farqini koʻrasiz</li>
    <li>Mavzu koʻrsatuvchi なら ni taniysiz</li>
    <li>Toʻrtta shartni bitta jadvalda yopasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Birovning gapiga javob</span>
  <span class="pe-chip pe-chip--s"><ruby>普通体<rt>ふつうたい</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">なら</span>
</div>

<h3>1. Yasalishi — bu yerda だ TUSHADI</h3>

<p>Toʻrtta shartning ichida yasalishi eng oson boʻlgani shu:
oddiy shaklga <b>なら</b> qoʻshiladi. Lekin bitta muhim gap bor —
ot va な-sifatdan keyin <b>だ yozilmaydi</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>なら dan oldin</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end">oddiy shakl</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>くなら</td><td class="pj-uz">boradigan boʻlsang</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">oʻzi</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>いなら</td><td class="pj-uz">arzon boʻlsa</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">だ <b>TUSHADI</b></td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かなら</td><td class="pj-uz">tinch boʻlsa</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end">だ <b>TUSHADI</b></td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>なら</td><td class="pj-uz">talaba boʻlsa</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Uchta joy, uchta boshqa qoida — endi hammasi bir joyda.</b>
  Bitta va oʻsha soʻz, <ruby>静<rt>しず</rt></ruby>か, uch xil
  qoʻshnisi oldida uch xil kiyinadi:
  <b>と</b> oldida <ruby>静<rt>しず</rt></ruby>か<b>だ</b>と (PJ-46) ·
  <b>ot</b> oldida <ruby>静<rt>しず</rt></ruby>か<b>な</b><ruby>部屋<rt>へや</rt></ruby> (PJ-48) ·
  <b>なら</b> oldida <ruby>静<rt>しず</rt></ruby>か<b>なら</b> — quruq.
  Sababi oddiy: なら ning oʻzi だ dan yasalgan, shuning uchun unga
  ikkinchi だ kerak emas.</p>
</div>

<h3>2. なら nima qiladi</h3>

<p>Boshqa uchta shart oʻzidan-oʻzi turadi. なら esa <b>oldin
aytilgan gapni koʻtarib oladi</b> va unga javob beradi. Shuning
uchun u deyarli doim suhbatda, deyarli doim maslahat yoki fikr
bilan keladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">A: <ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。<br>
  B: <ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くなら、<ruby>京都<rt>きょうと</rt></ruby>がいいですよ。</p>
  <p class="pe-ex__uz">A: Yaponiyaga boraman. — B: Yaponiyaga boradigan boʻlsang, Kioto yaxshi.</p>
  <p class="pe-ex__why">B ning sharti B niki emas — u A ning gapidan olingan.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «-adigan boʻlsang» — なら ning aynan oʻzi.</b>
  «Yaponiyaga <em>boradigan boʻlsang</em>, Kiotoga bor» — bu gap ham
  suhbatdoshning niyatini koʻtarib oladi, oʻzi shart qoʻymaydi.
  Oʻzbekchada oddiy «-sa» bilan «-adigan boʻlsa» orasida aynan shu
  farq bor, va siz uni allaqachon his qilasiz. Yaponchada shu farq
  <b>たら</b> va <b>なら</b> orasida turadi.</p>
</div>

<h3>3. Vaqt tartibi — darsning eng oʻtkir joyi</h3>

<p>Mana なら ni boshqa uchtasidan tubdan ajratadigan narsa.
<b>なら dan keyingi ish, shartdagi ishdan OLDIN ham boʻlishi
mumkin.</b> Boshqa hech qaysi shartda bunday emas.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">たら — keyin</p>
    <p><ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったら、カメラを<ruby>買<rt>か</rt></ruby>います。</p>
    <p>Avval boradi, <b>keyin</b> Yaponiyada kamera oladi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">なら — oldin</p>
    <p><ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くなら、カメラを<ruby>買<rt>か</rt></ruby>います。</p>
    <p>Avval kamera oladi, <b>keyin</b> boradi. Yaʼni safarga
    tayyorgarlik.</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>Bu farq amalda juda qimmat.</b> «Yaponiyaga
  <ruby>行<rt>い</rt></ruby>ったら kamera olaman» degan gapni
  doʻstingizga aytsangiz, u sizni Yaponiyada xarid qiladi deb
  tushunadi. «<ruby>行<rt>い</rt></ruby>くなら» desangiz — bu yerda,
  joʻnashdan oldin. Ikkala gap ham toʻgʻri, lekin ular boshqa reja
  haqida.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ham reja haqida gapirganda vaqtni oldinga
  suradi.</b> «Yaponiyaga <em>boradigan boʻlsang</em>, kamera ol» —
  bu gapdagi kamera hali shu yerda olinadi, va siz buni izohsiz
  tushunasiz. «Yaponiyaga <em>borsang</em>, kamera ol» desangiz esa
  quloq uni oʻsha yerda oladi deb eshitadi. Yaʼni oʻzbekcha bu
  farqni «-adigan boʻlsang» va «-sang» orasida qiladi — yaponcha
  esa <b>なら</b> va <b>たら</b> orasida. Ikkala tilda ham qurilma
  bir xil: rejani koʻtargan shakl vaqtni ham oldinga suradi.</p>
</div>

<h3>4. Mavzu koʻrsatuvchi なら</h3>

<p>なら ot bilan kelganda koʻpincha shart ham emas — u
<b>«… haqida gapiradigan boʻlsak»</b> degan maʼnoni beradi va
suhbatdagi mavzuni koʻtarib oladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">A: この<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みましたか。<br>
  B: その<ruby>本<rt>ほん</rt></ruby>なら<ruby>読<rt>よ</rt></ruby>みました。</p>
  <p class="pe-ex__uz">A: Bu kitobni oʻqidingizmi? — B: U kitobnimi, oʻqiganman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>駅<rt>えき</rt></ruby>なら、そこを<ruby>右<rt>みぎ</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ってください。</p>
  <p class="pe-ex__uz">Bekatnimi — u yerdan oʻngga boring.</p>
  <p class="pe-ex__why">Kimdir bekat qayerdaligini soʻragan. なら oʻsha savolni koʻtarib oladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu «-nimi», «-ga kelsak» degan ohang.</b>
  «U kitob<em>nimi</em> — oʻqiganman», «Bekat<em>ga kelsak</em>,
  oʻngga yuring». Ikkala tilda ham bu qurilma javobning boshida
  turadi va «siz soʻragan narsa haqida aytadigan boʻlsam» degani.
  Shuning uchun なら ni faqat «agar» deb tarjima qilish uni
  yarmini yoʻqotadi.</p>
</div>

<p>Bu ikkinchi ish なら ni grammatik qolipdan koʻra
<b>suhbat asbobi</b>ga aylantiradi. U savolni qaytarib olib,
javobni oʻsha savolning ustiga quradi — shuning uchun uni
yaponlar kuniga oʻnlab marta ishlatadi va shuning uchun uni
darslikdan koʻra suhbatda koʻproq eshitasiz. Agar biror kishi
sizdan yoʻl soʻrasa, javobingiz deyarli doim
<ruby>駅<rt>えき</rt></ruby>なら… yoki
<ruby>銀行<rt>ぎんこう</rt></ruby>なら… bilan boshlanadi.</p>

<h3>5. Toʻrttasi bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th></th><th>〜たら</th><th>〜ば</th><th>〜と</th><th>〜なら</th></tr>
  <tr><td class="pj-stem">Asosiy maʼnosi</td><td class="pj-uz">agar · …gach · kashfiyot</td>
      <td class="pj-uz">mantiqiy shart</td><td class="pj-uz">har doim shunday</td>
      <td class="pj-uz">birovning gapiga javob</td></tr>
  <tr><td class="pj-stem">Keyin buyruq/iltimos</td><td class="pj-res">✓</td>
      <td class="pj-uz">koʻpincha ✗</td><td class="pj-uz">✗</td><td class="pj-res">✓</td></tr>
  <tr><td class="pj-stem">Natija shartdan oldin</td><td class="pj-uz">✗</td>
      <td class="pj-uz">✗</td><td class="pj-uz">✗</td><td class="pj-res">✓</td></tr>
  <tr><td class="pj-stem">Ot bilan</td><td class="pj-uz">だったら</td>
      <td class="pj-uz">kam</td><td class="pj-uz">だと</td><td class="pj-res">なら (だ yoʻq)</td></tr>
  <tr><td class="pj-stem">Qayerda eshitiladi</td><td class="pj-uz">hamma joyda</td>
      <td class="pj-uz">maslahat, maqol</td><td class="pj-uz">yoʻriqnoma, xarita</td>
      <td class="pj-uz">suhbat, javob</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Amaliy maslahat oʻzgarmadi.</b> Shubha boʻlsa —
  <b>たら</b>. Suhbatdosh aytgan narsaga javob berayotgan boʻlsangiz —
  <b>なら</b>. Mashina yoki tabiat haqida boʻlsa — <b>と</b>. Qolgani
  vaqt bilan oʻzi keladi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">都</span>
    <span class="pj-kanji__uz">poytaxt, katta shahar</span>
    <span class="pj-kanji__on">オン: ト, ツ</span>
    <span class="pj-kanji__kun">KUN: みやこ</span>
    <span class="pj-kanji__note">京都 (きょうと) — Kioto · 東京都 (とうきょうと) — Tokio viloyati</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">選</span>
    <span class="pj-kanji__uz">tanlamoq</span>
    <span class="pj-kanji__on">オン: セン</span>
    <span class="pj-kanji__kun">KUN: えら(ぶ)</span>
    <span class="pj-kanji__note">選ぶ (えらぶ) — tanlamoq · 選手 (せんしゅ) — sportchi</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>だなら</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>なら</b> — なら ning oʻzi だ dan yasalgan, ikkinchi だ kerak emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>静<rt>しず</rt></ruby>かだなら</p>
  <p class="pe-fix__good">✓ <ruby>静<rt>しず</rt></ruby><b>かなら</b> — な-sifat ham だ ni tashlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>きますなら</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>くなら — なら dan oldin oddiy shakl.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るなら、<ruby>家<rt>いえ</rt></ruby>にいます <em>(hech kim yomgʻir haqida gapirmagan boʻlsa)</em></p>
  <p class="pe-fix__good">✓ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っ<b>たら</b>… — なら uchun suhbatdosh oldin bir narsa aytgan boʻlishi kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «<ruby>学生<rt>がくせい</rt></ruby>» ni なら qolipiga qoʻying.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>学生<rt>がくせい</rt></ruby>なら</b> — だ qoʻshilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «<ruby>静<rt>しず</rt></ruby>か» ni なら qolipiga qoʻying.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>静<rt>しず</rt></ruby>かなら</b> — な-sifat ham だ ni tashlaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>くならカメラを<ruby>買<rt>か</rt></ruby>います» — kamera qayerda olinadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Joʻnashdan oldin, shu yerda.</b> なら da natija shartdan oldin boʻlishi mumkin. «<ruby>行<rt>い</rt></ruby>ったら» boʻlsa Yaponiyada olinardi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «その<ruby>本<rt>ほん</rt></ruby>なら<ruby>読<rt>よ</rt></ruby>みました» — bu shartmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Yoʻq. Bu <b>mavzu koʻrsatuvchi なら</b>: «U kitobnimi — oʻqiganman». Suhbatdoshning savolini koʻtarib olyapti.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Toʻrtta shartdan qaysi biri suhbatdosh aytgan gapga javob beradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>なら</b>. Qolgan uchtasi olamni tasvirlaydi; なら suhbatga javob beradi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜なら</b> — …adigan boʻlsa, …ga kelsak</li>
  <li><b><ruby>京都<rt>きょうと</rt></ruby></b> — Kioto</li>
  <li><b><ruby>選<rt>えら</rt></ruby>ぶ</b> — tanlamoq (I guruh)</li>
  <li><b><ruby>旅行<rt>りょこう</rt></ruby></b> — sayohat</li>
  <li><b><ruby>地図<rt>ちず</rt></ruby></b> — xarita</li>
  <li><b>カメラ</b> — kamera</li>
  <li><b><ruby>準備<rt>じゅんび</rt></ruby></b> — tayyorgarlik</li>
  <li><b><ruby>季節<rt>きせつ</rt></ruby></b> — fasl</li>
  <li><b><ruby>桜<rt>さくら</rt></ruby></b> — gilos guli, sakura</li>
  <li><b><ruby>紅葉<rt>こうよう</rt></ruby></b> — kuzgi qizil barglar</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>なら oldida <b>だ tushadi</b> — なら ning oʻzi だ dan yasalgan.</li>
    <li>なら <b>birovning gapini</b> koʻtarib oladi.</li>
    <li>Faqat なら da natija shartdan <b>oldin</b> boʻla oladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-53: Sabab: 〜から va 〜ので",
        "category": "japanese",
        "order": 53,
        "summary": (
            "«Chunki» ning ikki yuzi. から — bu MENING sababim; "
            "ので — bu shunchaki shunday boʻlgani. Ikkinchisi "
            "kechirim soʻraganda ancha yumshoq eshitiladi."
        ),
        "stories": ["でんしゃが とまったので"],
        "content": """
<h2>PJ-53: Sabab: 〜から va 〜ので</h2>

<p>Darsga kech qoldingiz. Oʻqituvchi soʻraydi: «Nega?» Sizda ikkita
javob bor:</p>

<p><ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まった<b>から</b>、<ruby>遅<rt>おく</rt></ruby>れました。<br>
<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まった<b>ので</b>、<ruby>遅<rt>おく</rt></ruby>れました。</p>

<p>Ikkalasi ham «poyezd toʻxtagani uchun kech qoldim» degani.
Lekin birinchisi biroz himoyalanayotgandek, ikkinchisi esa
odobli eshitiladi. Bugun aynan shu farqni qoʻlga olasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>から va ので ni toʻgʻri yasaysiz</li>
    <li>ので nega な talab qilishini tushunasiz</li>
    <li>Qaysi biri qachon odobliroq ekanini bilib olasiz</li>
    <li>«Nega?» degan savolga toʻliq javob berasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Sabab</span>
  <span class="pe-chip pe-chip--s">SABAB</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">から / ので</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">NATIJA</span>
</div>

<h3>1. Sabab oldinda turadi</h3>

<p>Birinchi navbatda tartibni yodlab oling: yaponchada
<b>sabab doim birinchi</b>, natija ikkinchi. Gap teskari
yozilmaydi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まった</span>
  <span class="pj-joshi__p">ので<small>SABAB</small></span>
  <span class="pj-joshi__v"><ruby>遅<rt>おく</rt></ruby>れました</span>
  <span class="pj-joshi__uz">Poyezd toʻxtagani uchun kech qoldim.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha ham aynan shu tartibda.</b> «Poyezd
  toʻxta<em>gani uchun</em> kech qoldim» — sabab oldinda,
  «uchun» soʻzi sababning <em>orqasida</em>. Yaponchada ham
  から va ので sababning orqasiga yopishadi. Koʻp tillarda esa
  «chunki» degan soʻz sababning <em>oldiga</em> tushadi va butun
  gapni teskari oʻqishga majbur qiladi. Yaʼni bu qolipda ham
  oʻzbek tili sizga tayyor tartibni berib turibdi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Lekin bitta joyda oʻzbekcha erkinroq.</b> Oʻzbekchada
  sababni keyinga surib ham boʻladi: «Kech qoldim, <em>chunki</em>
  poyezd toʻxtadi». <b>Yaponchada bu mumkin emas.</b> から va ので
  — qoʻshimchalar, ular oʻzi turgan gapga yopishadi va uni sabab
  qilib qoʻyadi; ularni gap oxiriga surib boʻlmaydi. Shuning uchun
  yaponcha gap tuzayotganda birinchi savol doim bitta boʻlsin:
  <em>sabab nima?</em> — va oʻshani birinchi yozing.</p>
</div>

<h3>2. から — oddiy shakl ham, muloyim shakl ham</h3>

<p>から oʻzidan oldingi gapga hech narsa talab qilmaydi:
oddiy shakl ham, です・ます ham turishi mumkin.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>から dan oldin</th><th>Misol</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end">oddiy yoki muloyim</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>くから · <ruby>行<rt>い</rt></ruby>きますから</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">oʻzi</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>いから</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">+ <b>だ</b></td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かだから</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end">+ <b>だ</b></td>
      <td class="pj-res"><ruby>雨<rt>あめ</rt></ruby>だから</td></tr>
</table></div>

<h3>3. ので — va nega u な talab qiladi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>ので dan oldin</th><th>Misol</th></tr>
  <tr><td class="pj-stem">Feʼl</td><td class="pj-end">oddiy shakl</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>くので</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">oʻzi</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>いので</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">+ <b>な</b></td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>か<b>な</b>ので</td></tr>
  <tr><td class="pj-stem">Ot</td><td class="pj-end">+ <b>な</b></td>
      <td class="pj-res"><ruby>雨<rt>あめ</rt></ruby><b>な</b>ので</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>な qayerdan keldi?</b> ので aslida ikki boʻlakdan iborat:
  <b>の</b> + <b>で</b>. Va <b>の</b> — ot, xuddi PJ-49 dagi とき
  kabi. Demak undan oldin PJ-48 ning qoidasi ishlaydi:
  な-sifat <b>な</b> kiyadi. Ot ham shunday, chunki bu yerda u
  boglama orqali ulanadi. Yaʼni bu ham yangi qoida emas —
  eskisining yangi joyda ishlashi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Ot bilan だから va なので ni chalkashtirmang.</b>
  <ruby>雨<rt>あめ</rt></ruby><b>だから</b> ✓ va
  <ruby>雨<rt>あめ</rt></ruby><b>なので</b> ✓ — ikkalasi ham
  toʻgʻri, lekin ular oʻrin almashmaydi:
  «<ruby>雨<rt>あめ</rt></ruby>なから» ham,
  «<ruby>雨<rt>あめ</rt></ruby>だので» ham yoʻq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>日本語<rt>にほんご</rt></ruby>が<ruby>好<rt>す</rt></ruby>きなので、<ruby>毎日<rt>まいにち</rt></ruby><ruby>勉強<rt>べんきょう</rt></ruby>します。</p>
  <p class="pe-ex__uz">Yapon tilini yaxshi koʻrganim uchun har kuni oʻqiyman.</p>
  <p class="pe-ex__why"><ruby>好<rt>す</rt></ruby>き — な-sifat, demak ので oldida <b>な</b>.</p>
</div>

<h3>4. Farqi: kimning sababi</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">から — MENING sababim</p>
    <p><ruby>危<rt>あぶ</rt></ruby>ないから、<ruby>来<rt>こ</rt></ruby>ないでください。</p>
    <p>Men shuni sabab deb <b>hisobladim</b>. Kuchli, aniq,
    baʼzan biroz qatʼiy. Buyruq va iltimos bilan yaxshi
    keladi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">ので — shunchaki shunday</p>
    <p><ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まったので、<ruby>遅<rt>おく</rt></ruby>れました。</p>
    <p>Bu <b>holat</b>, mening qarorim emas. Yumshoq, odobli.
    Kechirim va tushuntirish bilan yaxshi keladi.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham ikki xil ohang bor.</b> «Poyezd
  toʻxtadi, <em>shuning uchun</em> kech qoldim» — bu oʻzimni
  himoya qilyapman. «Poyezd toʻxta<em>gani uchun</em> kech
  qoldim» — bu esa shunchaki voqeani aytyapman. Farq juda
  nozik, lekin ustoz bilan gaplashganda eshitiladi. Yaponchada
  aynan shu nozik farq <b>から</b> va <b>ので</b> orasida
  turibdi — va u yerda u ancha kuchliroq sezilaqoladi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Amaliy qoida: kechirim soʻrasangiz — ので.</b>
  Kechikkanda, uy vazifasini qilmaganda, iltimos qilganda —
  ので tanlang. から bu joylarda «men aybdor emasman» degandek
  eshitilishi mumkin.</p>
</div>

<p>Farqni his qilishning yana bir yoʻli — <b>kim aybdor</b> degan
savol. から bilan gapirganingizda siz sababni <em>tanlab</em>
qoʻyyapsiz, yaʼni «bu shunday, chunki men shunday deb hisoblayman».
ので bilan esa siz hech narsa tanlamaysiz — voqea oʻzi shunday
boʻlgan va siz uni shunchaki aytyapsiz. Ustoz, ish beruvchi yoki
notanish odam oldida ikkinchisi doim xavfsiz.</p>

<p>Shuning uchun yapon tilida kechikkan odam deyarli doim
<b>ので</b> bilan boshlaydi. から bilan boshlagan odam esa,
oʻzi sezmasa ham, «men aybdor emasman» degan ohangni qoʻshib
yuboradi — va bu ohang oʻzbekchada ham, yaponchada ham
eshitiladi.</p>

<h3>5. «Nega?» degan savolga javob</h3>

<p>Savol <b>どうして</b> yoki <b>なぜ</b> bilan beriladi.
Javobda sabab yolgʻiz qolsa, oxiriga <b>からです</b>
qoʻyiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">A: どうして<ruby>来<rt>き</rt></ruby>ませんでしたか。<br>
  B: <ruby>病気<rt>びょうき</rt></ruby>だったからです。</p>
  <p class="pe-ex__uz">A: Nega kelmadingiz? — B: Kasal boʻlganim uchun.</p>
  <p class="pe-ex__why">Natija aytilmaydi — u savolning oʻzida bor. Shuning uchun からです bilan yopiladi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>«のでです» degan shakl yoʻq.</b> Javob yolgʻiz sababdan
  iborat boʻlsa, doim <b>からです</b>. ので faqat gap ichida,
  natija bilan birga keladi.</p>
</div>

<h3>6. だから — keyingi gapning boshida</h3>

<p>Ikkita alohida gap yozmoqchi boʻlsangiz, ikkinchisini
<b>だから</b> (oddiy) yoki <b>ですから</b> (muloyim) bilan
boshlang.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>今日<rt>きょう</rt></ruby>は<ruby>雨<rt>あめ</rt></ruby>です。ですから、<ruby>試合<rt>しあい</rt></ruby>はありません。</p>
  <p class="pe-ex__uz">Bugun yomgʻir. Shuning uchun oʻyin boʻlmaydi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">理</span>
    <span class="pj-kanji__uz">mantiq, tartib</span>
    <span class="pj-kanji__on">オン: リ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">理由 (りゆう) — sabab · 料理 (りょうり) — taom · 無理 (むり) — imkonsiz</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">遅</span>
    <span class="pj-kanji__uz">kech, sekin</span>
    <span class="pj-kanji__on">オン: チ</span>
    <span class="pj-kanji__kun">KUN: おそ(い), おく(れる)</span>
    <span class="pj-kanji__note">遅れる (おくれる) — kechikmoq · 遅い (おそい) — kech, sekin</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>静<rt>しず</rt></ruby>かだので</p>
  <p class="pe-fix__good">✓ <ruby>静<rt>しず</rt></ruby>か<b>な</b>ので — ので dan oldin な-sifat な kiyadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>なから</p>
  <p class="pe-fix__good">✓ <ruby>雨<rt>あめ</rt></ruby><b>だ</b>から — から esa だ oladi. Ikkisi teskari.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>遅<rt>おく</rt></ruby>れました、<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まったので</p>
  <p class="pe-fix__good">✓ <ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まったので、<ruby>遅<rt>おく</rt></ruby>れました — sabab doim oldinda.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>病気<rt>びょうき</rt></ruby>だったのでです</p>
  <p class="pe-fix__good">✓ <ruby>病気<rt>びょうき</rt></ruby>だった<b>からです</b> — yolgʻiz sabab doim からです.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «<ruby>静<rt>しず</rt></ruby>か» ni ので bilan ulang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>静<rt>しず</rt></ruby>かなので</b> — ので dagi の ot, demak な.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «<ruby>雨<rt>あめ</rt></ruby>» ni から bilan ulang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>雨<rt>あめ</rt></ruby>だから</b> — から esa だ oladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Ustozga kechikkaningizni tushuntiryapsiz. Qaysi birini tanlaysiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ので</b> — yumshoq va odobli. から «men aybdor emasman» degandek eshitilishi mumkin.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «どうして<ruby>来<rt>き</rt></ruby>ませんでしたか» ga qisqa javob bering: kasal edim.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>病気<rt>びょうき</rt></ruby>だったからです</b> — yolgʻiz sabab からです bilan yopiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. ので nega な talab qiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki ので = <b>の + で</b>, va の — <b>ot</b>. Otdan oldin な-sifat な kiyadi (PJ-48).</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜から</b> — chunki (mening sababim)</li>
  <li><b>〜ので</b> — chunki (shunchaki shunday)</li>
  <li><b>だから · ですから</b> — shuning uchun</li>
  <li><b>どうして · なぜ</b> — nega</li>
  <li><b><ruby>理由<rt>りゆう</rt></ruby></b> — sabab</li>
  <li><b><ruby>遅<rt>おく</rt></ruby>れる</b> — kechikmoq (II guruh)</li>
  <li><b><ruby>止<rt>と</rt></ruby>まる</b> — toʻxtamoq (I guruh)</li>
  <li><b><ruby>病気<rt>びょうき</rt></ruby></b> — kasallik</li>
  <li><b><ruby>危<rt>あぶ</rt></ruby>ない</b> — xavfli</li>
  <li><b><ruby>事故<rt>じこ</rt></ruby></b> — baxtsiz hodisa</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Sabab oldinda</b>, natija keyin — oʻzbekchadagidek.</li>
    <li>から <b>だ</b> oladi, ので esa <b>な</b> — teskari.</li>
    <li>Kechirim soʻrasangiz — <b>ので</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-54: Qarama-qarshilik: 〜が va 〜けど",
        "category": "japanese",
        "order": 54,
        "summary": (
            "«Lekin» — va u gapning oxiriga yopishadi, boshiga emas. "
            "Bundan tashqari が va けど yaponchaning eng koʻp "
            "ishlatiladigan muloyim ochqichlari."
        ),
        "stories": ["ながいけど おもしろい"],
        "content": """
<h2>PJ-54: Qarama-qarshilik: 〜が va 〜けど</h2>

<p>PJ-14 dan beri siz <b>が</b> ni bir ishda koʻrgansiz: ega
koʻrsatuvchi qoʻshimcha. Bugun oʻsha belgi butunlay boshqa ish
qiladi — u ikki gapni ulaydi va «lekin» degan maʼnoni beradi.</p>

<p>Ikkisi bir-biriga aloqasiz. Ularni ajratish esa juda oson,
va buni dars boshida qilib qoʻyamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Bogʻlovchi が ni qoʻshimcha が dan ajratasiz</li>
    <li>が va けど orasidan toʻgʻrisini tanlaysiz</li>
    <li>Nega ular oldingi gapning muloyimligini saqlashini bilib olasiz</li>
    <li>«Kechirasiz, lekin…» degan muloyim ochqichni ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Lekin</span>
  <span class="pe-chip pe-chip--s">GAP 1</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">が / けど</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">GAP 2</span>
</div>

<h3>1. Ikki xil が</h3>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-joshi__p">が<small>EGA</small></span>
  <span class="pj-joshi__v">あります</span>
  <span class="pj-joshi__uz">Kitob bor. — が bitta OTdan keyin turibdi.</span>
</div>

<div class="pj-joshi">
  <span class="pj-joshi__n">この<ruby>本<rt>ほん</rt></ruby>は<ruby>高<rt>たか</rt></ruby>いです</span>
  <span class="pj-joshi__p">が<small>LEKIN</small></span>
  <span class="pj-joshi__v"><ruby>買<rt>か</rt></ruby>います</span>
  <span class="pj-joshi__uz">Bu kitob qimmat, lekin sotib olaman. — が butun GAPdan keyin turibdi.</span>
</div>

<div class="pe-call pe-rule">
  <p><b>Ajratish qoidasi bitta savolda.</b> が dan oldin <b>ot</b>
  turibdimi yoki <b>tugallangan gap</b>? Ot boʻlsa — bu ega
  koʻrsatkichi. Gap boʻlsa (yaʼni oldida kesim bor) — bu
  «lekin». Chalkashish deyarli mumkin emas, chunki
  «<ruby>高<rt>たか</rt></ruby>いです» ot emas.</p>
</div>

<h3>2. Yasalishi — va bitta gʻalati xususiyat</h3>

<p>Boshqa hamma bogʻlovchi oldida oddiy shakl talab qilgan edi:
と (PJ-46), とき (PJ-49), ので (PJ-53). <b>が va けど esa
talab qilmaydi.</b> Ular oldingi gapning muloyimligini
<em>oʻzgarmasdan</em> saqlaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Uslub</th><th>Gap 1</th><th>Bogʻlovchi</th><th>Gap 2</th></tr>
  <tr><td class="pj-stem">Muloyim</td><td class="pj-uz"><ruby>高<rt>たか</rt></ruby>いです</td>
      <td class="pj-end">が</td><td class="pj-res"><ruby>買<rt>か</rt></ruby>います</td></tr>
  <tr><td class="pj-stem">Oddiy</td><td class="pj-uz"><ruby>高<rt>たか</rt></ruby>い</td>
      <td class="pj-end">けど</td><td class="pj-res"><ruby>買<rt>か</rt></ruby>う</td></tr>
  <tr><td class="pj-stem">Aralash (tabiiy)</td><td class="pj-uz"><ruby>高<rt>たか</rt></ruby>いけど</td>
      <td class="pj-end">けど</td><td class="pj-res"><ruby>買<rt>か</rt></ruby>います</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu oʻzbekchadan farq qiladigan joy.</b> Oʻzbekchada
  «lekin» <em>ikkinchi</em> gapning boshida turadi: «Qimmat,
  <b>lekin</b> olaman». Yaponchada esa が va けど
  <em>birinchi</em> gapning oxiriga yopishadi:
  «<ruby>高<rt>たか</rt></ruby>いです<b>が</b>、<ruby>買<rt>か</rt></ruby>います».
  Yaʼni oʻzbekcha «lekin» ni yaponchaga koʻchirganda u
  <b>bir gap chapga suriladi</b>. Buni bir marta sezsangiz,
  boshqa xato qilmaysiz.</p>
</div>

<h3>3. が va けど — qaysi biri qachon</h3>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">けど</span>
    <span class="pj-level__ja"><ruby>高<rt>たか</rt></ruby>いけど</span>
    <span class="pj-level__who">suhbat, doʻstlar, kundalik — eng koʻp eshitiladi</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">が</span>
    <span class="pj-level__ja"><ruby>高<rt>たか</rt></ruby>いですが</span>
    <span class="pj-level__who">yozma til, rasmiy nutq, imtihon</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Oʻrtada yana ikkitasi bor.</b> <b>けれども</b> —
  eng rasmiysi, <b>けれど</b> — oʻrtacha. Yaʼni bitta soʻzning
  toʻrtta uzunligi bor:
  けど → けれど → けれども → が. Qanchalik uzun boʻlsa,
  shunchalik rasmiy. Yozganda が ni, gapirganda けど ni
  ishlating.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>日本語<rt>にほんご</rt></ruby>は<ruby>難<rt>むずか</rt></ruby>しいですが、<ruby>面白<rt>おもしろ</rt></ruby>いです。</p>
  <p class="pe-ex__uz">Yapon tili qiyin, lekin qiziqarli.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>買<rt>か</rt></ruby>いたいけど、お<ruby>金<rt>かね</rt></ruby>がない。</p>
  <p class="pe-ex__uz">Olgim kelyapti, lekin pulim yoʻq.</p>
  <p class="pe-ex__why">Ikkala qism ham oddiy shaklda — doʻstlar orasidagi gap.</p>
</div>

<p>Bu xususiyat が va けど ni butun Blok D dagi eng erkin
bogʻlovchiga aylantiradi. Ular bilan gap tuzishdan oldin hech
narsani oʻzgartirish kerak emas: qanday aytgan boʻlsangiz,
shundayligicha ulayverasiz. Faqat bitta shart bor —
<b>gapning eng oxiri butun gapning uslubini belgilaydi</b>,
shuning uchun muloyim gapni oddiy shakl bilan tugatmang.</p>

<h3>4. Muloyim ochqich — qarama-qarshilik emas</h3>

<p>Mana yaponchada eng koʻp uchraydigan が. Bu yerda u hech
qanday qarama-qarshilik bildirmaydi — u shunchaki gapni
<b>yumshoq boshlash</b> uchun turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">すみませんが、<ruby>駅<rt>えき</rt></ruby>はどこですか。</p>
  <p class="pe-ex__uz">Kechirasiz, bekat qayerda?</p>
  <p class="pe-ex__why">«Kechirasiz, <em>lekin</em> bekat qayerda?» emas. が bu yerda faqat odob.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>失礼<rt>しつれい</rt></ruby>ですが、お<ruby>名前<rt>なまえ</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ですか。</p>
  <p class="pe-ex__uz">Uzr, ismingiz nima?</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham xuddi shunday boʻsh «-u» bor.</b>
  «Kechirasiz-<em>u</em>, soat nechchi boʻldi?» — bu yerdagi
  «-u» ham hech nimani qarshi qoʻymaydi, u faqat gapni
  yumshatadi. Yaponcha すみませんが aynan shu ish. Shuning
  uchun bu が ni tarjima qilishga urinmang — uni
  <b>ohang</b> deb qabul qiling.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Bu ochqichlarni yodlab oling — ular tayyor ibora.</b>
  すみませんが · <ruby>失礼<rt>しつれい</rt></ruby>ですが ·
  あのう、すみませんが. Yaponiyada koʻchada birovga
  murojaat qilishning deyarli yagona yoʻli shu.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>でも — oʻzbekcha «lekin» ga eng oʻxshaydigan soʻz, va
  aynan shuning uchun xavfli.</b> でも <em>yangi gapning
  boshida</em> turadi:
  «<ruby>高<rt>たか</rt></ruby>いです。でも、<ruby>買<rt>か</rt></ruby>います。» — bu
  toʻgʻri va oʻzbekcha tartibga toʻliq mos. Lekin yaponlar bir
  fikrni ikkiga boʻlmasdan aytishni afzal koʻradi, shuning uchun
  kundalik nutqda
  «<ruby>高<rt>たか</rt></ruby>いですけど、<ruby>買<rt>か</rt></ruby>います» ancha koʻp
  eshitiladi. Yaʼni でも xato emas — u shunchaki gapni
  <em>ikkiga sindiradi</em>, けど esa butun qoldiradi.</p>
</div>

<p>Bu ochqichlarning ishlashi ham bir xil mantiqqa asoslangan.
«Kechirasiz» deb boshlab, keyin darrov savol berish yaponchada
biroz keskin eshitiladi: siz odamni toʻxtatdingiz va shu zahoti
undan bir narsa talab qilyapsiz. が esa oʻrtaga kichkina
<em>boʻshliq</em> qoʻyadi — goʻyo «kechirasiz, bir narsa bor
edi…» degandek. Shuning uchun uni tarjima qilib boʻlmaydi:
u soʻz emas, <b>pauza</b>.</p>

<h3>5. けど gapni ochiq qoldiradi</h3>

<p>Suhbatda けど dan keyin hech narsa aytmaslik ham mumkin.
Bu qoʻpollik emas — aksincha, muloyimlik: siz fikringizni
oxirigacha aytmay, suhbatdoshga joy qoldiryapsiz.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">A: <ruby>明日<rt>あした</rt></ruby>、<ruby>来<rt>き</rt></ruby>ますか。<br>
  B: <ruby>行<rt>い</rt></ruby>きたいですけど…</p>
  <p class="pe-ex__uz">A: Ertaga kelasizmi? — B: Borgim kelardi-yu…</p>
  <p class="pe-ex__why">Davomi aytilmaydi: «…lekin vaqtim yoʻq». Yaponchada bu «yoʻq» degan javobning eng odobli shakli.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Yozma ishda gapni けど bilan tugatmang.</b> Bu faqat
  ogʻzaki nutqning uslubi. Insho va imtihonda gap toʻliq
  boʻlishi kerak.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">反</span>
    <span class="pj-kanji__uz">qarshi, teskari</span>
    <span class="pj-kanji__on">オン: ハン</span>
    <span class="pj-kanji__kun">KUN: そ(る)</span>
    <span class="pj-kanji__note">反対 (はんたい) — qarshi, teskari</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">失</span>
    <span class="pj-kanji__uz">yoʻqotmoq</span>
    <span class="pj-kanji__on">オン: シツ</span>
    <span class="pj-kanji__kun">KUN: うしな(う)</span>
    <span class="pj-kanji__note">失礼 (しつれい) — odobsizlik; «uzr» degan ibora</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>高<rt>たか</rt></ruby>いです。が、<ruby>買<rt>か</rt></ruby>います。</p>
  <p class="pe-fix__good">✓ <ruby>高<rt>たか</rt></ruby>いです<b>が</b>、<ruby>買<rt>か</rt></ruby>います。 — が birinchi gapga <b>yopishadi</b>, ikkinchisining boshida turmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>高<rt>たか</rt></ruby>いですけど、<ruby>買<rt>か</rt></ruby>う</p>
  <p class="pe-fix__good">✓ <ruby>高<rt>たか</rt></ruby>いですけど、<ruby>買<rt>か</rt></ruby>います — gap oxiri butun gapning uslubini belgilaydi; oxirini muloyim qoldiring.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>だですが</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby>ですが (muloyim) yoki ✓ <ruby>学生<rt>がくせい</rt></ruby>だけど (oddiy) — ikkisini aralashtirmang.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Inshoda: <ruby>難<rt>むずか</rt></ruby>しいけど…</p>
  <p class="pe-fix__good">✓ <ruby>難<rt>むずか</rt></ruby>しいですが、… — yozma ishda が, va gap toʻliq.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «この<ruby>本<rt>ほん</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです» dagi が qanaqa が?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Ega koʻrsatkichi</b> — undan oldin <b>ot</b> turibdi (<ruby>本<rt>ほん</rt></ruby>), gap emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «<ruby>安<rt>やす</rt></ruby>いですが、<ruby>買<rt>か</rt></ruby>いません» dagi が-chi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Bogʻlovchi «lekin»</b> — undan oldin tugallangan gap turibdi (<ruby>安<rt>やす</rt></ruby>いです).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Doʻstingizga aytyapsiz: «Qiyin, lekin qiziqarli.» Qaysi bogʻlovchi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>けど</b> — <ruby>難<rt>むずか</rt></ruby>しいけど<ruby>面白<rt>おもしろ</rt></ruby>い. が yozma va rasmiy.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «すみませんが、<ruby>駅<rt>えき</rt></ruby>はどこですか» — bu yerda が nima qilyapti?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Hech qanday qarama-qarshilik yoʻq. Bu <b>muloyim ochqich</b> — gapni yumshoq boshlash uchun.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «<ruby>行<rt>い</rt></ruby>きたいですけど…» — nega gap tugamagan?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Bu <b>ataylab</b>. «…lekin vaqtim yoʻq» aytilmaydi — yaponchada «yoʻq» degan javobning eng odobli shakli shu.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜が</b> — lekin (rasmiy, yozma)</li>
  <li><b>〜けど</b> — lekin (suhbat)</li>
  <li><b>けれども · けれど</b> — が va けど orasidagi shakllar</li>
  <li><b>すみませんが</b> — kechirasiz-u…</li>
  <li><b><ruby>失礼<rt>しつれい</rt></ruby>ですが</b> — uzr, lekin…</li>
  <li><b><ruby>反対<rt>はんたい</rt></ruby></b> — qarshi, teskari</li>
  <li><b>でも</b> — lekin (gap boshida)</li>
  <li><b>お<ruby>金<rt>かね</rt></ruby></b> — pul</li>
  <li><b><ruby>長<rt>なが</rt></ruby>い</b> — uzun</li>
  <li><b><ruby>短<rt>みじか</rt></ruby>い</b> — qisqa</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>が / けど <b>birinchi gapga yopishadi</b> — oʻzbekcha «lekin» dan bir gap chapda.</li>
    <li>Ular oldingi gapning <b>muloyimligini saqlaydi</b> — oddiy shakl talab qilmaydi.</li>
    <li>すみませんが — bu qarama-qarshilik emas, <b>odob</b>.</li>
  </ul>
</div>
""",
    },
]
