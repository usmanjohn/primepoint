# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-88, PJ-89, PJ-90: rol, mavzu va yozma qarshilik.

Blok F davom etadi. Birinchi ikkitasi — otga ulanadigan
<ruby>複合助詞</ruby> (qoʻshma qoʻshimcha) oilasi, uchinchisi esa
feʼlga ulanadigan yozma qarshilik.
    PJ-88 — として (rol: «… sifatida») va にとって (nuqtai nazar:
            «… uchun, … nazdida»). Oʻzbekcha «uchun» ikkalasini
            ham, PJ-56 dagi ために ni ham koʻtaradi — shuning
            uchun bu uchtasi bitta jadvalda solishtiriladi.
    PJ-89 — について (mavzu: «… haqida»), に関して (oʻsha maʼno,
            rasmiyroq) va に対して (yoʻnalish: «… ga nisbatan»,
            hamda «…ning aksiga»).
    PJ-90 — ながらも va つつ: PJ-38 dagi ながら ga も qoʻshilsa,
            «bir vaqtda» degan maʼno «…ga qaramay» ga aylanadi.
            つつ — oʻsha ikki maʼnoning kitobiy egizagi, va
            uning uchinchi ishi bor: つつある.

⚠️ PJ-88 ning eng katta tuzogʻi — **にとって va ために**. Ikkalasi
ham oʻzbekchada «uchun». Farqi: ために — manfaat va maqsad
(«kim uchun qilyapman»), にとって — baho nuqtasi («kimning
koʻzida shunday»). Shuning uchun にとって dan keyin deyarli doim
baho beruvchi soʻz keladi: <ruby>大切</ruby>だ,
<ruby>難</ruby>しい, ありがたい.

⚠️ PJ-89 da について va に対して ni adashtirmaslik kerak: について
— **nima haqida**, に対して — **kimga qaratilgan**.
<ruby>先生</ruby>について<ruby>話</ruby>す («ustoz haqida gapirmoq»)
≠ <ruby>先生</ruby>に<ruby>対</ruby>して<ruby>失礼</ruby>だ («ustozga
nisbatan qoʻpol»).

⚠️ PJ-90 da も bitta harf, lekin maʼno teskari tomonga buriladi:
<ruby>歩</ruby>きながら (bir vaqtda) ≠ <ruby>知</ruby>っていながらも
(…ga qaramay). Va ながら ikkala tomonda ham **bitta ega** talab
qiladi — PJ-54 dagi が bunday talab qilmaydi.

⚠️ Kursda hech qachon berilmagan shakllar bu batchda ham yoʻq:
意向形, 〜んです va uning yozma egizagi 〜のです. Gate uchalasini
ham mexanik tekshiradi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_88_90.py --author=prime
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
        "title": "PJ-88: 〜として va 〜にとって",
        "category": "japanese",
        "order": 88,
        "summary": (
            "として — «… sifatida», rolni koʻrsatadi. にとって — "
            "«… uchun, … nazdida», baho beriladigan nuqtani koʻrsatadi. "
            "Va nega oʻzbekcha «uchun» bu ikkisini ham, PJ-56 dagi "
            "ために ni ham koʻtaradi."
        ),
        "stories": ["ふたつの かお"],
        "content": """
<h2>PJ-88: 〜として va 〜にとって</h2>

<p>イムロン yapon tilidagi taqdimotni tayyorlayapti va bitta
oʻzbekcha jumlani tarjima qila olmayapti: <em>«Men uchun bu
qiyin»</em>. Lugʻat unga uchta javob beradi:</p>

<p><ruby>私<rt>わたし</rt></ruby><b>として</b>は…</p>

<p><ruby>私<rt>わたし</rt></ruby><b>にとって</b>…</p>

<p><ruby>私<rt>わたし</rt></ruby>の<b>ために</b>…</p>

<p>Uchalasi ham oʻzbekchada «men uchun» deb tarjima qilinadi, va
uchalasi ham boshqa gapni aytadi. Birinchisi — <em>mening
rolimda turib</em>. Ikkinchisi — <em>mening koʻzimda</em>.
Uchinchisi — <em>mening manfaatim uchun</em>.</p>

<p>Bu dars oʻsha uchta «uchun» ni bir-biridan ajratadi — va
aslida bu oʻzbek tilining kambagʻalligi emas, yapon tilining
aniqligi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>〜として</b> bilan rolni koʻrsatasiz</li>
    <li><b>〜にとって</b> bilan baho nuqtasini koʻrsatasiz</li>
    <li><b>にとって</b> va PJ-56 dagi <b>ために</b> ni ajratasiz</li>
    <li>ikkovining ot oldidagi shaklini yasaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Rol</span>
  <span class="pe-chip pe-chip--s">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">として</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">… sifatida</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Baho nuqtasi</span>
  <span class="pe-chip pe-chip--s">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">にとって</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">… nazdida</span>
</div>

<h3>1. 〜として — «… sifatida»</h3>

<p>として odamning yoki narsaning <b>roli</b>ni koʻrsatadi: qaysi
sifatda, qaysi vazifada, qaysi maqomda. Ulanish oddiy — ot
yalangʻoch turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">ラノさんは<span class="pe-hl pe-hl--s"><ruby>通訳<rt>つうやく</rt></ruby>として</span><ruby>会議<rt>かいぎ</rt></ruby>に<ruby>出<rt>で</rt></ruby>ました。</p>
  <p class="pe-ex__uz">Rano tarjimon sifatida yigʻilishga qatnashdi.</p>
  <p class="pe-ex__why">Rano yigʻilishga tomoshabin sifatida emas, aynan tarjimon sifatida keldi. として shu farqni aytadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>部屋<rt>へや</rt></ruby>は<span class="pe-hl pe-hl--s"><ruby>倉庫<rt>そうこ</rt></ruby>として</span><ruby>使<rt>つか</rt></ruby>われている。</p>
  <p class="pe-ex__uz">Bu xona ombor sifatida ishlatiladi.</p>
  <p class="pe-ex__why">として odamga ham, narsaga ham ulanadi — muhimi <em>vazifa</em> nomlanishi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu yerda oʻzbekcha «-dek» bilan «sifatida» ni adashtirmang
  — yaponchada ular ikki boshqa qolip.</b> «Shifokor<em>dek</em>
  gapiradi» degani — u shifokor emas, faqat oʻxshatyapmiz. Buning
  yaponchasi PJ-56 dagi <b>ように</b>:
  <ruby>医者<rt>いしゃ</rt></ruby>のように<ruby>話<rt>はな</rt></ruby>す.
  «Shifokor <em>sifatida</em> gapiradi» degani esa — u
  <em>haqiqatan</em> shifokor, va shu maqomda gapiryapti:
  <ruby>医者<rt>いしゃ</rt></ruby>として<ruby>話<rt>はな</rt></ruby>す.
  Ikki gap bir-biriga juda yaqin koʻrinadi, lekin ular teskari
  narsani aytadi — biri maqomni rad etadi, ikkinchisi tasdiqlaydi.
  Rus tilidan tarjima qilsangiz bu tuzoq yanada yaqinlashadi,
  chunki u yerda ikkalasi ham bitta soʻz bilan beriladi. Shuning
  uchun bitta savol soʻrang: <em>«bu odam rostdan ham shumi?»</em>
  Ha — <b>として</b>. Yoʻq — <b>ように</b>.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Ikkita qardosh shakli bor.</b> <b>〜としては</b> — «…ning
  nazarida esa», fikrni ajratib koʻrsatadi:
  <ruby>私<rt>わたし</rt></ruby>としてはこの<ruby>案<rt>あん</rt></ruby>に<ruby>賛成<rt>さんせい</rt></ruby>です
  («men esa bu taklifni maʼqullayman»). <b>〜としても</b> —
  «… sifatida ham»:
  <ruby>学生<rt>がくせい</rt></ruby>としても<ruby>選手<rt>せんしゅ</rt></ruby>としても<ruby>有名<rt>ゆうめい</rt></ruby>だ.</p>
</div>

<h3>2. 〜にとって — «… nazdida»</h3>

<p>にとって esa rolni emas, <b>baho beriladigan nuqtani</b>
koʻrsatadi: kimning koʻzi bilan qaralyapti. Shuning uchun undan
keyin deyarli doim <em>baho beruvchi soʻz</em> keladi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>子供<rt>こども</rt></ruby></span>
  <span class="pj-joshi__p">にとって<small>BAHO NUQTASI</small></span>
  <span class="pj-joshi__n">これは</span>
  <span class="pj-joshi__v"><ruby>難<rt>むずか</rt></ruby>しい</span>
  <span class="pj-joshi__uz">Bola uchun bu qiyin. — qiyinlik bolaning koʻzida.</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s"><ruby>私<rt>わたし</rt></ruby>にとって</span><ruby>家族<rt>かぞく</rt></ruby>がいちばん<ruby>大切<rt>たいせつ</rt></ruby>です。</p>
  <p class="pe-ex__uz">Men uchun oila eng muhim.</p>
  <p class="pe-ex__why">«Muhim» — baho. Kimning bahosi? Meniki. Aynan shu にとって ning ishi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>にとって dan keyin harakat kelmaydi.</b> Bu qolipdan
  keyin sifat yoki holat turadi —
  <ruby>大切<rt>たいせつ</rt></ruby>だ,
  <ruby>難<rt>むずか</rt></ruby>しい,
  <ruby>必要<rt>ひつよう</rt></ruby>だ, ありがたい,
  <ruby>忘<rt>わす</rt></ruby>れられない. «Men uchun kitob sotib
  oldi» degan gapda esa harakat bor, va u にとって ni
  <b>olmaydi</b>: bu yerda PJ-56 dagi ために kerak.</p>
</div>

<h3>3. にとって va ために — oʻzbekcha «uchun» ning ikki yuzi</h3>

<p>Bu darsning eng muhim yarim sahifasi. Ikkala qolip ham
oʻzbekchada «uchun» deb tarjima qilinadi, lekin ular bir-birining
oʻrnini bosmaydi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">ために — manfaat, maqsad</p>
    <p><ruby>子供<rt>こども</rt></ruby>のために<ruby>本<rt>ほん</rt></ruby>を<ruby>買<rt>か</rt></ruby>いました。</p>
    <p>Bola uchun kitob sotib oldim. Ish bolaning <b>foydasiga</b>
    qilindi. Keyin <b>harakat</b> keladi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">にとって — baho nuqtasi</p>
    <p><ruby>子供<rt>こども</rt></ruby>にとって<ruby>難<rt>むずか</rt></ruby>しい<ruby>本<rt>ほん</rt></ruby>です。</p>
    <p>Bola uchun qiyin kitob. Qiyinlik bolaning <b>koʻzida</b>.
    Keyin <b>baho</b> keladi.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilining «uchun» soʻzi juda mehnatkash, va aynan
  shuning uchun bu yerda adashamiz.</b> Ikkita gapni yonma-yon
  qoʻying: «Bola <em>uchun</em> kitob oldim» va «Bola
  <em>uchun</em> bu kitob qiyin». Bitta soʻz, lekin birinchisida
  men <em>bola foydasiga</em> ish qildim, ikkinchisida esa
  <em>bolaning koʻzi bilan</em> qarayapman. Oʻzbekchada farqni
  faqat gapning davomi aytadi — «oldim» yoki «qiyin». Yapon
  tili esa buni <b>qoʻshimchaning oʻzida</b> hal qiladi:
  ために + harakat, にとって + baho. Demak tarjima qilishdan oldin
  gapning oxiriga qarang: feʼlmi yoki sifatmi? Javob qolipni
  tanlaydi, va bu qoida deyarli hech qachon adashtirmaydi.</p>
</div>

<h3>4. Uchtasi bitta jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Nimani koʻrsatadi</th><th>Keyin nima keladi</th><th>Misol</th></tr>
  <tr><td class="pj-stem">〜として</td><td class="pj-uz">rol, maqom</td>
      <td class="pj-end">harakat yoki holat</td>
      <td class="pj-res"><ruby>通訳<rt>つうやく</rt></ruby>として<ruby>働<rt>はたら</rt></ruby>く</td></tr>
  <tr><td class="pj-stem">〜にとって</td><td class="pj-uz">baho nuqtasi</td>
      <td class="pj-end">baho beruvchi soʻz</td>
      <td class="pj-res"><ruby>私<rt>わたし</rt></ruby>にとって<ruby>大切<rt>たいせつ</rt></ruby>だ</td></tr>
  <tr><td class="pj-stem">〜のために</td><td class="pj-uz">manfaat, maqsad</td>
      <td class="pj-end">harakat</td>
      <td class="pj-res"><ruby>家族<rt>かぞく</rt></ruby>のために<ruby>働<rt>はたら</rt></ruby>く</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bitta harf farqiga ham eʼtibor bering.</b>
  <b>にとって</b> otga <em>yalangʻoch</em> ulanadi
  (<ruby>私<rt>わたし</rt></ruby>にとって), <b>ために</b> esa
  otdan keyin <b>の</b> talab qiladi
  (<ruby>私<rt>わたし</rt></ruby>のために). Bu ikkovini yodda
  saqlashning eng arzon yoʻli — の bor-yoʻqligiga qarash.</p>
</div>

<h3>5. Ot oldidagi shakllar</h3>

<p>Ikkala qolip ham otni aniqlashi mumkin, va shakl bir oz
oʻzgaradi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Ot oldida</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">として</td><td class="pj-end">としての</td>
      <td class="pj-res"><ruby>親<rt>おや</rt></ruby>としての<ruby>責任<rt>せきにん</rt></ruby></td>
      <td class="pj-uz">ota-ona sifatidagi masʼuliyat</td></tr>
  <tr><td class="pj-stem">にとって</td><td class="pj-end">にとっての</td>
      <td class="pj-res"><ruby>私<rt>わたし</rt></ruby>にとっての<ruby>幸<rt>しあわ</rt></ruby>せ</td>
      <td class="pj-uz">mening nazdimdagi baxt</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--o"><ruby>親<rt>おや</rt></ruby>としての<ruby>責任<rt>せきにん</rt></ruby></span>を<ruby>忘<rt>わす</rt></ruby>れてはいけない。</p>
  <p class="pe-ex__uz">Ota-ona sifatidagi masʼuliyatni unutmaslik kerak.</p>
  <p class="pe-ex__why">Ot oldida <b>の</b> qoʻshiladi. としての<ruby>責任<rt>せきにん</rt></ruby> — bitta ot birikmasi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>«Sifatida» — oʻzbekcha tayyor kalit.</b> として ni
  koʻrganingizda ichingizda <em>«… sifatida»</em> deb oʻqing,
  va gap deyarli har doim toʻgʻri chiqadi: «tarjimon
  <em>sifatida</em>», «ombor <em>sifatida</em>», «ota-ona
  <em>sifatida</em>». Bu soʻz oʻzbekchada ham xuddi shu joyda —
  otdan keyin — turadi. Aksincha, にとって uchun «sifatida»
  hech qachon toʻgʻri kelmaydi: «bola <em>sifatida</em> qiyin»
  degan gap maʼnoni buzadi. Demak ikkovini ajratish uchun
  bitta sinov yetarli: <em>«sifatida» deb qoʻysam, gap
  turadimi?</em></p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">親</span>
    <span class="pj-kanji__uz">ota-ona; yaqin</span>
    <span class="pj-kanji__on">オン: シン</span>
    <span class="pj-kanji__kun">KUN: おや・した(しい)</span>
    <span class="pj-kanji__note">両親 (りょうしん) — ota-ona · 親切 (しんせつ) — mehribon</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">責</span>
    <span class="pj-kanji__uz">masʼuliyat, ayblamoq</span>
    <span class="pj-kanji__on">オン: セキ</span>
    <span class="pj-kanji__kun">KUN: せ(める)</span>
    <span class="pj-kanji__note">責任 (せきにん) — masʼuliyat · 無責任 (むせきにん) — masʼuliyatsiz</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">訳</span>
    <span class="pj-kanji__uz">tarjima qilmoq</span>
    <span class="pj-kanji__on">オン: ヤク</span>
    <span class="pj-kanji__kun">KUN: わけ</span>
    <span class="pj-kanji__note">通訳 (つうやく) — ogʻzaki tarjimon · 翻訳 (ほんやく) — yozma tarjima</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>子供<rt>こども</rt></ruby>にとって<ruby>本<rt>ほん</rt></ruby>を<ruby>買<rt>か</rt></ruby>いました</p>
  <p class="pe-fix__good">✓ <ruby>子供<rt>こども</rt></ruby><b>のために</b><ruby>本<rt>ほん</rt></ruby>を<ruby>買<rt>か</rt></ruby>いました — keyin harakat kelsa, ために turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby><b>の</b>にとって<ruby>大切<rt>たいせつ</rt></ruby>です</p>
  <p class="pe-fix__good">✓ <ruby>私<rt>わたし</rt></ruby>にとって — にとって otga yalangʻoch ulanadi; の faqat ために ga kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>通訳<rt>つうやく</rt></ruby>にとって<ruby>会議<rt>かいぎ</rt></ruby>に<ruby>出<rt>で</rt></ruby>ました</p>
  <p class="pe-fix__good">✓ <ruby>通訳<rt>つうやく</rt></ruby><b>として</b> — «sifatida» degani rol, va rol として bilan beriladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>親<rt>おや</rt></ruby>として<ruby>責任<rt>せきにん</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>親<rt>おや</rt></ruby>として<b>の</b><ruby>責任<rt>せきにん</rt></ruby> — ot oldida の qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby><b>だ</b>として<ruby>頑張<rt>がんば</rt></ruby>る</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby>として — として ham otga yalangʻoch ulanadi, だ olmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Rano tarjimon sifatida yigʻilishga qatnashdi» — として yoki にとって?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>として</b>: <ruby>通訳<rt>つうやく</rt></ruby>として<ruby>会議<rt>かいぎ</rt></ruby>に<ruby>出<rt>で</rt></ruby>ました. «Sifatida» — rol, va rolni faqat として koʻrsatadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Boʻsh joyni toʻldiring: <ruby>私<rt>わたし</rt></ruby>___<ruby>家族<rt>かぞく</rt></ruby>がいちばん<ruby>大切<rt>たいせつ</rt></ruby>です。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>にとって</b>. Gapning oxirida baho beruvchi soʻz (<ruby>大切<rt>たいせつ</rt></ruby>だ) turibdi — demak baho nuqtasi kerak, manfaat emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Bola uchun kitob sotib oldim» — qaysi qolip?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>のために</b>: <ruby>子供<rt>こども</rt></ruby>のために<ruby>本<rt>ほん</rt></ruby>を<ruby>買<rt>か</rt></ruby>いました. Keyin harakat kelyapti, demak manfaat — にとって bu yerga tushmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Ota-ona sifatidagi masʼuliyat» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>親<rt>おや</rt></ruby>としての<ruby>責任<rt>せきにん</rt></ruby></b>. Ot oldida として ga <b>の</b> qoʻshiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. にとって va ために — qaysi biri otdan keyin の talab qiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ために</b>: <ruby>私<rt>わたし</rt></ruby>のために. にとって esa yalangʻoch ulanadi: <ruby>私<rt>わたし</rt></ruby>にとって. Bu — ikkovini ajratishning eng arzon belgisi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜として</b> — … sifatida</li>
  <li><b>〜としては</b> — … ning nazarida esa</li>
  <li><b>〜としての + ot</b> — … sifatidagi …</li>
  <li><b>〜にとって</b> — … nazdida, … uchun (baho)</li>
  <li><b>〜のために</b> — … uchun (manfaat, maqsad)</li>
  <li><b><ruby>通訳<rt>つうやく</rt></ruby></b> — ogʻzaki tarjimon</li>
  <li><b><ruby>責任<rt>せきにん</rt></ruby></b> — masʼuliyat</li>
  <li><b><ruby>会議<rt>かいぎ</rt></ruby></b> — yigʻilish</li>
  <li><b><ruby>倉庫<rt>そうこ</rt></ruby></b> — ombor</li>
  <li><b><ruby>幸<rt>しあわ</rt></ruby>せ</b> — baxt</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>として</b> = «sifatida» (rol); <b>にとって</b> = «nazdida» (baho).</li>
    <li>にとって dan keyin <b>baho</b>, ために dan keyin <b>harakat</b> keladi.</li>
    <li>にとって yalangʻoch ulanadi, <b>のために</b> esa の oladi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-89: 〜に関して, 〜について, 〜に対して",
        "category": "japanese",
        "order": 89,
        "summary": (
            "について — «… haqida», mavzuni koʻrsatadi. に関して — oʻsha "
            "maʼno, rasmiyroq. に対して — «… ga nisbatan»: munosabat "
            "qaratilgan tomon, hamda ikki narsaning qarshi qoʻyilishi."
        ),
        "stories": ["アンケートの けっか"],
        "content": """
<h2>PJ-89: 〜に<ruby>関<rt>かん</rt></ruby>して, 〜について, 〜に<ruby>対<rt>たい</rt></ruby>して</h2>

<p>Ikki gap, bitta ot, ikkita qoʻshimcha:</p>

<p><ruby>先生<rt>せんせい</rt></ruby><b>について</b><ruby>話<rt>はな</rt></ruby>しました。</p>

<p><ruby>先生<rt>せんせい</rt></ruby><b>に<ruby>対<rt>たい</rt></ruby>して</b><ruby>失礼<rt>しつれい</rt></ruby>でした。</p>

<p>Birinchisi — <em>ustoz haqida gapirdik</em>: ustoz suhbatning
<b>mavzusi</b>. Ikkinchisi — <em>ustozga nisbatan qoʻpol edi</em>:
ustoz munosabatning <b>nishoni</b>. Mavzu va nishon — ikki
boshqa narsa, va yapon tili ularni ikki boshqa qoʻshimcha bilan
ajratadi.</p>

<p>Bu dars uchta yozma qoʻshimchani yonma-yon qoʻyadi. Ikkitasi
deyarli bir xil, uchinchisi esa butunlay boshqa ish qiladi — va
aynan oʻsha uchinchisi imtihonda soʻraladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>〜について</b> bilan mavzuni koʻrsatasiz</li>
    <li><b>〜に<ruby>関<rt>かん</rt></ruby>して</b> ni rasmiy matnda ishlatasiz</li>
    <li><b>〜に<ruby>対<rt>たい</rt></ruby>して</b> bilan munosabat qaratilgan tomonni koʻrsatasiz</li>
    <li>uchalasining <b>ot oldidagi</b> shaklini yasaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Mavzu</span>
  <span class="pe-chip pe-chip--o">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">について</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">… haqida</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Nishon</span>
  <span class="pe-chip pe-chip--o">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">に<ruby>対<rt>たい</rt></ruby>して</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">… ga nisbatan</span>
</div>

<h3>1. 〜について — mavzu</h3>

<p>Eng koʻp ishlatiladigani va eng osoni. について otdan keyin
kelib, «shu narsa <b>haqida</b>» deydi. Keyin esa mavzu bilan
ishlaydigan feʼl turadi: gapirmoq, yozmoq, oʻylamoq, oʻrganmoq,
soʻramoq.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--o"><ruby>日本<rt>にほん</rt></ruby>の<ruby>文化<rt>ぶんか</rt></ruby>について</span><ruby>発表<rt>はっぴょう</rt></ruby>しました。</p>
  <p class="pe-ex__uz">Yaponiya madaniyati haqida taqdimot qildim.</p>
  <p class="pe-ex__why">Madaniyat — taqdimotning mavzusi. Oʻzbekcha «haqida» qayerda tursa, について ham oʻsha yerda.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «haqida» bu qolipning aniq jufti.</b>
  «Madaniyat <em>haqida</em> gapirdim», «bu masala
  <em>haqida</em> oʻyladim», «u <em>haqida</em> hech narsa
  bilmayman» — uchalasida ham について turadi, va u oʻzbekcha
  soʻz bilan <b>bir xil joyda</b>: otdan keyin, feʼldan oldin.
  Shuning uchun bu qolipni yodlash shart emas — «haqida» ni
  eshiting, について ni qoʻying. Bitta ogohlantirish bor,
  xolos: oʻzbekcha «haqida» baʼzan «nisbatan» maʼnosida ham
  ishlatiladi («unga nisbatan adolatsiz»), va <em>oʻsha</em>
  holatda について emas, に<ruby>対<rt>たい</rt></ruby>して
  kerak boʻladi.</p>
</div>

<h3>2. 〜に<ruby>関<rt>かん</rt></ruby>して — oʻsha maʼno, boshqa kiyim</h3>

<p>に<ruby>関<rt>かん</rt></ruby>して について bilan deyarli bir
xil maʼnoni beradi. Farq faqat <b>ohangda</b>: に<ruby>関<rt>かん</rt></ruby>して —
rasmiy hujjat, ilmiy maqola va yangiliklarning tili.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">について — kundalik va yozma</p>
    <p>この<ruby>問題<rt>もんだい</rt></ruby>について<ruby>話<rt>はな</rt></ruby>しましょう。</p>
    <p>Bu masala haqida gaplashaylik. Sinfda ham, xatda ham,
    suhbatda ham tabiiy.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">に<ruby>関<rt>かん</rt></ruby>して — rasmiy</p>
    <p>この<ruby>件<rt>けん</rt></ruby>に<ruby>関<rt>かん</rt></ruby>して<ruby>調査<rt>ちょうさ</rt></ruby>を<ruby>行<rt>おこな</rt></ruby>う。</p>
    <p>Ushbu masala yuzasidan tekshiruv oʻtkaziladi. Hujjat,
    eʼlon, maqola tili.</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>Ikkovi oʻrin almashtira oladi, lekin bir tomonga.</b>
  Rasmiy gapda について qoʻysangiz, gap biroz yumshaydi —
  lekin xato boʻlmaydi. Kundalik suhbatda に<ruby>関<rt>かん</rt></ruby>して qoʻysangiz
  esa gap <em>gʻalati rasmiy</em> eshitiladi, xuddi doʻstingizga
  ariza yozgandek. Shubhalansangiz, について ni tanlang.</p>
</div>

<h3>3. 〜に<ruby>対<rt>たい</rt></ruby>して — nishon</h3>

<p>Mana bu uchinchisi butunlay boshqa ish qiladi.
に<ruby>対<rt>たい</rt></ruby>して — «… <b>ga qaratilgan</b>,
… ga nisbatan». U mavzuni emas, <b>munosabat yoki harakat
yoʻnalgan tomonni</b> koʻrsatadi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>質問<rt>しつもん</rt></ruby></span>
  <span class="pj-joshi__p">に<ruby>対<rt>たい</rt></ruby>して<small>NISHON</small></span>
  <span class="pj-joshi__n"><ruby>丁寧<rt>ていねい</rt></ruby>に</span>
  <span class="pj-joshi__v"><ruby>答<rt>こた</rt></ruby>えた</span>
  <span class="pj-joshi__uz">Savolga javoban xushmuomala javob berdi.</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--o"><ruby>先生<rt>せんせい</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して</span>そんな<ruby>態度<rt>たいど</rt></ruby>をとってはいけない。</p>
  <p class="pe-ex__uz">Ustozga nisbatan bunday munosabatda boʻlmaslik kerak.</p>
  <p class="pe-ex__why">Ustoz — suhbatning mavzusi emas, munosabatning nishoni. Shuning uchun について bu yerga tushmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu farqni feʼl emas, kelishik koʻrsatadi.</b>
  «Ustoz <em>haqida</em> gapirdim» — chiqish maʼnosi, mavzu.
  «Ustoz<em>ga</em> qoʻpollik qildim» — joʻnalish kelishigi, nishon.
  Sezyapsizmi: oʻzbekchada ikkinchi gapda <b>-ga</b> paydo boʻldi,
  chunki harakat kimgadir <em>qaratildi</em>. Yaponcha ham aynan
  shuni qiladi — に<ruby>対<rt>たい</rt></ruby>して ning ichida
  turgan <b>に</b> oʻsha «-ga» ning oʻzi, qolgani esa
  «qaragan holda» degan qoʻshimcha. Shuning uchun bu qolipni
  yodlash oʻrniga oʻzbekcha gapni tuzing va <b>-ga</b> bormi deb
  qarang. Bor boʻlsa — に<ruby>対<rt>たい</rt></ruby>して; yoʻq
  boʻlsa — について.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Bu darsning eng koʻp adashtiradigan jufti.</b>
  <ruby>先生<rt>せんせい</rt></ruby>について<ruby>話<rt>はな</rt></ruby>す
  — «ustoz <em>haqida</em> gapirmoq», ustoz xonada boʻlmasligi
  ham mumkin. <ruby>先生<rt>せんせい</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して<ruby>失礼<rt>しつれい</rt></ruby>だ
  — «ustoz<em>ga nisbatan</em> qoʻpol», bu yerda ustoz —
  munosabat yoʻnalgan odam. Bitta savol hal qiladi:
  <em>«bu narsa gapning mavzusimi yoki nishonimi?»</em></p>
</div>

<h3>4. に<ruby>対<rt>たい</rt></ruby>して ning ikkinchi ishi — qarshi qoʻyish</h3>

<p>に<ruby>対<rt>たい</rt></ruby>して ning yana bir vazifasi bor, va u yozma matnda juda
koʻp uchraydi: <b>ikki narsani qarshi qoʻyish</b>. Bu maʼnoda
u oddiy shakldan keyin ham keladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>兄<rt>あに</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かな<span class="pe-hl pe-hl--adv">のに<ruby>対<rt>たい</rt></ruby>して</span>、<ruby>弟<rt>おとうと</rt></ruby>はよくしゃべる。</p>
  <p class="pe-ex__uz">Akam tinch boʻlsa, ukam koʻp gapiradi.</p>
  <p class="pe-ex__why">Ikki odam yonma-yon qoʻyilib solishtirilyapti. な-sifat va ot bu maʼnoda oldiga <b>な</b> + <b>の</b> oladi.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Qarshi qoʻyish shakli</th><th>Misol</th></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-end">oddiy shakl + のに<ruby>対<rt>たい</rt></ruby>して</td>
      <td class="pj-res"><ruby>兄<rt>あに</rt></ruby>は<ruby>働<rt>はたら</rt></ruby>くのに<ruby>対<rt>たい</rt></ruby>して…</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">oddiy shakl + のに<ruby>対<rt>たい</rt></ruby>して</td>
      <td class="pj-res"><ruby>夏<rt>なつ</rt></ruby>は<ruby>暑<rt>あつ</rt></ruby>いのに<ruby>対<rt>たい</rt></ruby>して…</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">な + のに<ruby>対<rt>たい</rt></ruby>して</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かなのに<ruby>対<rt>たい</rt></ruby>して…</td></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end">な + のに<ruby>対<rt>たい</rt></ruby>して</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>なのに<ruby>対<rt>たい</rt></ruby>して…</td></tr>
</table></div>

<h3>5. Ot oldidagi uchta shakl</h3>

<p>Uchala qolip ham otni aniqlashi mumkin, va uchalasi ham
boshqacha oʻzgaradi. Bu jadval imtihon savolining tayyor
manbai.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--o"><ruby>環境<rt>かんきょう</rt></ruby>に<ruby>関<rt>かん</rt></ruby>する<ruby>法律<rt>ほうりつ</rt></ruby></span>が<ruby>変<rt>か</rt></ruby>わりました。</p>
  <p class="pe-ex__uz">Atrof-muhitga oid qonun oʻzgardi.</p>
  <p class="pe-ex__why">Ot oldida に<ruby>関<rt>かん</rt></ruby>して emas, <b>に<ruby>関<rt>かん</rt></ruby>する</b> turadi — chunki u <ruby>関<rt>かん</rt></ruby>する degan feʼlning lugʻat shakli.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Ot oldida</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">について</td><td class="pj-end">についての</td>
      <td class="pj-res"><ruby>環境<rt>かんきょう</rt></ruby>についての<ruby>本<rt>ほん</rt></ruby></td>
      <td class="pj-uz">atrof-muhit haqidagi kitob</td></tr>
  <tr><td class="pj-stem">に<ruby>関<rt>かん</rt></ruby>して</td><td class="pj-end">に<ruby>関<rt>かん</rt></ruby>する</td>
      <td class="pj-res"><ruby>環境<rt>かんきょう</rt></ruby>に<ruby>関<rt>かん</rt></ruby>する<ruby>法律<rt>ほうりつ</rt></ruby></td>
      <td class="pj-uz">atrof-muhitga oid qonun</td></tr>
  <tr><td class="pj-stem">に<ruby>対<rt>たい</rt></ruby>して</td><td class="pj-end">に<ruby>対<rt>たい</rt></ruby>する</td>
      <td class="pj-res"><ruby>子供<rt>こども</rt></ruby>に<ruby>対<rt>たい</rt></ruby>する<ruby>態度<rt>たいど</rt></ruby></td>
      <td class="pj-uz">bolaga boʻlgan munosabat</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Ikkitasi する, bittasi の.</b> に<ruby>関<rt>かん</rt></ruby>して va に<ruby>対<rt>たい</rt></ruby>して —
  ikkalasi ham <ruby>関<rt>かん</rt></ruby>する va
  <ruby>対<rt>たい</rt></ruby>する degan feʼllardan kelgan,
  shuning uchun ot oldida lugʻat shakliga qaytadi (PJ-48 dagi
  aniqlovchi ergash gap). について esa feʼl emas, shuning uchun
  unga oddiygina <b>の</b> qoʻshiladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tili bu yerda ham ajratib beradi, faqat boshqa
  soʻzlar bilan.</b> について — «<em>haqida</em>», «<em>yuzasidan</em>».
  に<ruby>対<rt>たい</rt></ruby>して — «<em>ga nisbatan</em>», «<em>ga qarshi</em>»,
  «<em>ga javoban</em>». Uchala oʻzbekcha ibora ham bitta narsani
  bildiradi: <em>bir tomon bor, va biz oʻsha tomonga qaraymiz</em>.
  «Haqida» esa hech kimga qaramaydi — u shunchaki mavzuni
  nomlaydi. Shuning uchun gapni tarjima qilishdan oldin
  oʻzbekcha variantni ichingizda ayting: «haqida» chiqdimi —
  について; «ga nisbatan», «ga javoban», «ga qarshi» chiqdimi —
  に<ruby>対<rt>たい</rt></ruby>して. Bu sinov imtihonda ham,
  yozganda ham ishlaydi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">関</span>
    <span class="pj-kanji__uz">bogʻliq boʻlmoq, aloqa</span>
    <span class="pj-kanji__on">オン: カン</span>
    <span class="pj-kanji__kun">KUN: かか(わる)・せき</span>
    <span class="pj-kanji__note">関係 (かんけい) — munosabat · 関心 (かんしん) — qiziqish · 玄関 (げんかん) — kirish</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">対</span>
    <span class="pj-kanji__uz">qarama-qarshi, qarshi tomon</span>
    <span class="pj-kanji__on">オン: タイ・ツイ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">反対 (はんたい) — qarshi · 対話 (たいわ) — muloqot</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">態</span>
    <span class="pj-kanji__uz">holat, munosabat</span>
    <span class="pj-kanji__on">オン: タイ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">態度 (たいど) — munosabat, yurish-turish · 状態 (じょうたい) — holat</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>先生<rt>せんせい</rt></ruby>について<ruby>失礼<rt>しつれい</rt></ruby>な<ruby>態度<rt>たいど</rt></ruby>をとった</p>
  <p class="pe-fix__good">✓ <ruby>先生<rt>せんせい</rt></ruby>に<b><ruby>対<rt>たい</rt></ruby>して</b> — munosabat qaratilgan tomon, mavzu emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>環境<rt>かんきょう</rt></ruby>に<ruby>関<rt>かん</rt></ruby>して<ruby>法律<rt>ほうりつ</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>環境<rt>かんきょう</rt></ruby>に<ruby>関<rt>かん</rt></ruby><b>する</b><ruby>法律<rt>ほうりつ</rt></ruby> — ot oldida する shakli turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>環境<rt>かんきょう</rt></ruby>について<ruby>本<rt>ほん</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>環境<rt>かんきょう</rt></ruby>について<b>の</b><ruby>本<rt>ほん</rt></ruby> — について feʼl emas, shuning uchun の oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>日本<rt>にほん</rt></ruby>の<ruby>文化<rt>ぶんか</rt></ruby><b>の</b>について<ruby>発表<rt>はっぴょう</rt></ruby>した</p>
  <p class="pe-fix__good">✓ <ruby>文化<rt>ぶんか</rt></ruby>について — について otga yalangʻoch ulanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>兄<rt>あに</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かに<ruby>対<rt>たい</rt></ruby>して、<ruby>弟<rt>おとうと</rt></ruby>はうるさい</p>
  <p class="pe-fix__good">✓ <ruby>静<rt>しず</rt></ruby>か<b>なの</b>に<ruby>対<rt>たい</rt></ruby>して — qarshi qoʻyishda な-sifat な + の oladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Ustoz haqida gapirdik» — について yoki に<ruby>対<rt>たい</rt></ruby>して?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>について</b>: <ruby>先生<rt>せんせい</rt></ruby>について<ruby>話<rt>はな</rt></ruby>しました. Ustoz — suhbatning mavzusi. «Haqida» chiqdi, demak について.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Ustozga nisbatan qoʻpol edi» — qaysi qolip?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>に<ruby>対<rt>たい</rt></ruby>して</b>: <ruby>先生<rt>せんせい</rt></ruby>に<ruby>対<rt>たい</rt></ruby>して<ruby>失礼<rt>しつれい</rt></ruby>でした. «Ga nisbatan» chiqdi — bu nishon, mavzu emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Boʻsh joyni toʻldiring: <ruby>環境<rt>かんきょう</rt></ruby>に<ruby>関<rt>かん</rt></ruby>___<ruby>法律<rt>ほうりつ</rt></ruby>。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>する</b> — <ruby>環境<rt>かんきょう</rt></ruby>に<ruby>関<rt>かん</rt></ruby>する<ruby>法律<rt>ほうりつ</rt></ruby>. に<ruby>関<rt>かん</rt></ruby>して va に<ruby>対<rt>たい</rt></ruby>して ot oldida lugʻat shakliga qaytadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>環境<rt>かんきょう</rt></ruby>について___<ruby>本<rt>ほん</rt></ruby> — boʻsh joyga nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>の</b>. について feʼldan kelmagani uchun otni aniqlashda oddiygina <b>の</b> qoʻshiladi — する emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Akam tinch, ukam esa koʻp gapiradi» — qarshi qoʻyish qolipini yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>兄<rt>あに</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かなのに<ruby>対<rt>たい</rt></ruby>して、<ruby>弟<rt>おとうと</rt></ruby>はよくしゃべる</b>. な-sifat bu qolipda な + の oladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜について</b> — … haqida</li>
  <li><b>〜についての + ot</b> — … haqidagi …</li>
  <li><b>〜に<ruby>関<rt>かん</rt></ruby>して</b> — … yuzasidan (rasmiy)</li>
  <li><b>〜に<ruby>関<rt>かん</rt></ruby>する + ot</b> — … ga oid …</li>
  <li><b>〜に<ruby>対<rt>たい</rt></ruby>して</b> — … ga nisbatan; … ning aksiga</li>
  <li><b><ruby>態度<rt>たいど</rt></ruby></b> — munosabat, yurish-turish</li>
  <li><b><ruby>環境<rt>かんきょう</rt></ruby></b> — atrof-muhit</li>
  <li><b><ruby>発表<rt>はっぴょう</rt></ruby>する</b> — taqdimot qilmoq, eʼlon qilmoq</li>
  <li><b><ruby>調査<rt>ちょうさ</rt></ruby></b> — tekshiruv, soʻrov</li>
  <li><b><ruby>失礼<rt>しつれい</rt></ruby></b> — qoʻpollik, odobsizlik</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>について</b> = mavzu («haqida»); <b>に<ruby>対<rt>たい</rt></ruby>して</b> = nishon («ga nisbatan»).</li>
    <li><b>に<ruby>関<rt>かん</rt></ruby>して</b> = について ning rasmiy kiyimi.</li>
    <li>Ot oldida: <b>についての</b>, lekin <b>に<ruby>関<rt>かん</rt></ruby>する</b> va <b>に<ruby>対<rt>たい</rt></ruby>する</b>.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-90: 〜ながらも, 〜つつ — yozma qarama-qarshilik",
        "category": "japanese",
        "order": 90,
        "summary": (
            "PJ-38 dagi ながら ga bitta も qoʻshilsa, «bir vaqtda» degan "
            "maʼno «…ga qaramay» ga aylanadi. つつ — oʻsha ikki maʼnoning "
            "kitobiy egizagi, va uning uchinchi ishi bor: つつある — "
            "«… boʻlib bormoqda»."
        ),
        "stories": ["ちいさいながらも"],
        "content": """
<h2>PJ-90: 〜ながらも, 〜つつ — yozma qarama-qarshilik</h2>

<p>PJ-38 da siz shu gapni oʻrgangansiz:</p>

<p><ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>き<b>ながら</b><ruby>勉強<rt>べんきょう</rt></ruby>します。</p>

<p>«Musiqa tinglab oʻqiyman» — ikki ish bir vaqtda. Endi
oxiriga bitta harf qoʻshamiz:</p>

<p><ruby>知<rt>し</rt></ruby>ってい<b>ながらも</b>、<ruby>教<rt>おし</rt></ruby>えてくれなかった。</p>

<p>Maʼno butunlay burildi: «Bilgani <b>holda ham</b>, aytmadi».
Endi bu «bir vaqtda» emas — bu <b>qarama-qarshilik</b>. Bitta
<b>も</b> qolipni teskari tomonga aylantirdi.</p>

<p>Bu dars oʻsha bitta harf va uning kitobiy egizagi
<b>つつ</b> haqida. Ikkalasi ham yozma tilning soʻzlari —
maqolada, kitobda, rasmiy nutqda yashaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>〜ながらも</b> bilan «…ga qaramay» deysiz</li>
    <li><b>〜つつ</b> ni ikkala maʼnosida taniysiz</li>
    <li><b>〜つつある</b> bilan «… boʻlib bormoqda» deysiz</li>
    <li>ながら <b>bitta ega</b> talab qilishini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qarama-qarshilik</span>
  <span class="pe-chip pe-chip--v">ます-oʻzagi</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">ながらも</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--neg">… ga qaramay</span>
</div>

<h3>1. Ulanish — ます-oʻzagi</h3>

<p>Ikkala qolip ham feʼlning <b>ます-oʻzagiga</b> ulanadi:
ます-shaklini oling va ます ni olib tashlang. Bu PJ-38 dan
tanish.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>ます-shakli</th><th>Oʻzagi</th><th>Natija</th></tr>
  <tr><td><ruby>知<rt>し</rt></ruby>っている</td><td class="pj-stem"><ruby>知<rt>し</rt></ruby>っています</td>
      <td class="pj-end"><ruby>知<rt>し</rt></ruby>ってい</td>
      <td class="pj-res"><ruby>知<rt>し</rt></ruby>っていながらも</td></tr>
  <tr><td><ruby>歩<rt>ある</rt></ruby>く</td><td class="pj-stem"><ruby>歩<rt>ある</rt></ruby>きます</td>
      <td class="pj-end"><ruby>歩<rt>ある</rt></ruby>き</td>
      <td class="pj-res"><ruby>歩<rt>ある</rt></ruby>きつつ</td></tr>
  <tr><td><ruby>思<rt>おも</rt></ruby>う</td><td class="pj-stem"><ruby>思<rt>おも</rt></ruby>います</td>
      <td class="pj-end"><ruby>思<rt>おも</rt></ruby>い</td>
      <td class="pj-res"><ruby>思<rt>おも</rt></ruby>いつつ</td></tr>
  <tr><td><ruby>増<rt>ふ</rt></ruby>える</td><td class="pj-stem"><ruby>増<rt>ふ</rt></ruby>えます</td>
      <td class="pj-end"><ruby>増<rt>ふ</rt></ruby>え</td>
      <td class="pj-res"><ruby>増<rt>ふ</rt></ruby>えつつある</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Lugʻat shakli bu yerga tushmaydi.</b>
  «<ruby>歩<rt>ある</rt></ruby>くつつ» ham,
  «<ruby>歩<rt>ある</rt></ruby>きますながら» ham notoʻgʻri.
  Faqat oʻzak: <ruby>歩<rt>ある</rt></ruby>き + つつ. Sifat va ot
  esa boshqacha ulanadi — pastda alohida koʻramiz.</p>
</div>

<h3>2. 〜ながらも — «…ga qaramay»</h3>

<p>も qoʻshilishi bilan gap <em>kutilmagan qarama-qarshilik</em>ni
aytadi: birinchi qism toʻgʻri, lekin ikkinchisi undan
chiqmaydi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>知<rt>し</rt></ruby>ってい</span>
  <span class="pj-joshi__p">ながらも<small>QARSHILIK</small></span>
  <span class="pj-joshi__n"><ruby>教<rt>おし</rt></ruby>えて</span>
  <span class="pj-joshi__v">くれなかった</span>
  <span class="pj-joshi__uz">Bilgani holda ham aytmadi.</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--neg"><ruby>狭<rt>せま</rt></ruby>いながらも</span>、<ruby>楽<rt>たの</rt></ruby>しい<ruby>我<rt>わ</rt></ruby>が<ruby>家<rt>や</rt></ruby>。</p>
  <p class="pe-ex__uz">Tor boʻlsa-da, quvnoq uyimiz.</p>
  <p class="pe-ex__why">Mashhur ibora. い-sifat ながらも ga <b>yalangʻoch</b> ulanadi — oʻzak kerak emas.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Nima ulanadi</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-end">ます-oʻzagi</td>
      <td class="pj-res"><ruby>知<rt>し</rt></ruby>っていながらも</td>
      <td class="pj-uz">bilgani holda ham</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">yalangʻoch</td>
      <td class="pj-res"><ruby>狭<rt>せま</rt></ruby>いながらも</td>
      <td class="pj-uz">tor boʻlsa-da</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">yalangʻoch</td>
      <td class="pj-res"><ruby>残念<rt>ざんねん</rt></ruby>ながらも</td>
      <td class="pj-uz">afsuski boʻlsa-da</td></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end">yalangʻoch</td>
      <td class="pj-res"><ruby>子供<rt>こども</rt></ruby>ながらも</td>
      <td class="pj-uz">bola boʻlsa-da</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «-sa-da» va «-ga qaramay» shu qolipning
  oʻzi.</b> «Bil<em>sa-da</em> aytmadi», «tor bo<em>lsa-da</em>
  quvnoq», «bola bo<em>lsa-da</em> tushunadi» — uchalasida ham
  bitta narsa bor: <em>birinchi qismdan kutilgan natija
  chiqmadi</em>. Yaponcha ながらも ham aynan shu kutilmaganlikni
  koʻtaradi. Eʼtibor bering, oʻzbekchada ham qoʻshimcha
  <b>«-da»</b> — kichkina, bir boʻgʻinli, va aynan oʻsha
  kichkina boʻlak maʼnoni burib yuboradi. Yaponchada oʻsha ish
  <b>も</b> ning zimmasida. Ikki tilda ham: bitta harf,
  butun gap teskari.</p>
</div>

<h3>3. ながら ning ikki yuzi — qaysi biri qachon</h3>

<p>Bir savol tugʻiladi: も boʻlmasa ham ながら qarshilik
maʼnosini bera oladimi? Javob — <b>ha</b>, va tanlovni
<em>mazmun</em> qiladi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">ながら — bir vaqtda (PJ-38)</p>
    <p><ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>する。</p>
    <p>Ikkala ish ham bir vaqtda ketyapti, hech qanday gʻalatilik
    yoʻq.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">ながら(も) — qarshilik</p>
    <p><ruby>知<rt>し</rt></ruby>っていながら、<ruby>教<rt>おし</rt></ruby>えてくれなかった。</p>
    <p>Bilardi — demak aytishi kerak edi. Aytmadi. Kutilgan
    natija chiqmadi.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>も qarshilikni faqat kuchaytiradi, yaratmaydi.</b>
  も siz ham gap qarshilikni bildirishi mumkin, lekin も
  boʻlsa — bu <em>albatta</em> qarshilik, va u
  taʼkidlangan. Shuning uchun shubhalansangiz も ni qoʻying:
  gap aniqroq boʻladi. Bir vaqtda maʼnosida esa も
  <b>hech qachon</b> qoʻyilmaydi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>ながら ikkala tomonda ham bitta ega talab qiladi.</b>
  «<ruby>兄<rt>あに</rt></ruby>は<ruby>知<rt>し</rt></ruby>っていながら、
  <ruby>弟<rt>おとうと</rt></ruby>は<ruby>知<rt>し</rt></ruby>らなかった»
  degan gap notoʻgʻri — ikki boshqa odam. Bunday paytda PJ-54
  dagi <b>が</b> yoki <b>けど</b> kerak. Bu cheklov PJ-38 dan
  beri oʻzgarmagan.</p>
</div>

<h3>4. 〜つつ — kitobiy egizak</h3>

<p><b>つつ</b> ながら ning ikkala maʼnosini ham qaytaradi, faqat
bir pogʻona yuqori uslubda. Uni suhbatda eshitmaysiz — u
maqolada, esseda va rasmiy nutqda yashaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Maʼnosi</th><th>Kundalik</th><th>Kitobiy</th><th>Misol</th></tr>
  <tr><td class="pj-stem">bir vaqtda</td><td class="pj-uz">〜ながら</td>
      <td class="pj-end">〜つつ</td>
      <td class="pj-res"><ruby>歩<rt>ある</rt></ruby>きつつ<ruby>考<rt>かんが</rt></ruby>える</td></tr>
  <tr><td class="pj-stem">qarshilik</td><td class="pj-uz">〜ながらも</td>
      <td class="pj-end">〜つつも</td>
      <td class="pj-res"><ruby>悪<rt>わる</rt></ruby>いと<ruby>知<rt>し</rt></ruby>りつつも…</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>悪<rt>わる</rt></ruby>いと<span class="pe-hl pe-hl--neg"><ruby>知<rt>し</rt></ruby>りつつも</span>、やってしまった。</p>
  <p class="pe-ex__uz">Yomon ekanini bila turib ham, qilib qoʻydim.</p>
  <p class="pe-ex__why">つつも — ながらも ning kitobiy shakli. Oxiridagi 〜てしまった (PJ-58) afsusni qoʻshadi va bu qolip bilan juda tez-tez keladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham kitobiy va soʻzlashuv shakllari
  juftlashib yuradi.</b> «Bil<em>gani holda</em>» —
  yozma; «bil<em>sa ham</em>» — kundalik. «Shu<em>ning
  uchun</em>» — oddiy; «<em>binobarin</em>» — maqola tili.
  Ikkala juftda ham maʼno bir xil, farq faqat <em>qayerda
  yozilishida</em>. Yaponcha ながら va つつ aynan shunday juft:
  gapiradigan odam ながら deydi, maqola yozadigan odam つつ
  yozadi. Shuning uchun bu ikkovini «qaysi biri toʻgʻri» deb
  emas, <b>«bu matn qanday matn?»</b> deb tanlang. Insho yoki
  taqdimot yozsangiz — つつ sizning foydangizga ishlaydi;
  doʻstingizga xabar yozsangiz — u gʻalati eshitiladi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>つつ faqat feʼl bilan keladi.</b> ながらも sifatga ham,
  otga ham ulanadi (<ruby>狭<rt>せま</rt></ruby>いながらも,
  <ruby>子供<rt>こども</rt></ruby>ながらも), つつ esa
  <b>faqat feʼlning ます-oʻzagiga</b>. Shuning uchun
  «<ruby>狭<rt>せま</rt></ruby>いつつ» degan gap yoʻq.</p>
</div>

<h3>5. 〜つつある — «… boʻlib bormoqda»</h3>

<p>Va endi つつ ning uchinchi, butunlay boshqa ishi.
<b>〜つつある</b> — harakat yoki oʻzgarish <em>davom
etayotganini</em>, sekin-asta borayotganini bildiradi. Bu
qarshilik emas, bu <b>jarayon</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>町<rt>まち</rt></ruby>の<ruby>本屋<rt>ほんや</rt></ruby>は<span class="pe-hl pe-hl--v"><ruby>減<rt>へ</rt></ruby>りつつある</span>。</p>
  <p class="pe-ex__uz">Shahardagi kitob doʻkonlari kamayib bormoqda.</p>
  <p class="pe-ex__why">〜ている ham boʻlardi, lekin つつある «jarayon hali tugamagan, yoʻnalish shu» degan yozma ohangni beradi.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">〜つつある — jarayon</p>
    <p><ruby>雪<rt>ゆき</rt></ruby>が<ruby>消<rt>き</rt></ruby>えつつある。</p>
    <p>Qor erib bormoqda. Oʻzgarish davom etyapti.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">〜つつも — qarshilik</p>
    <p><ruby>雪<rt>ゆき</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りつつも、<ruby>試合<rt>しあい</rt></ruby>は<ruby>続<rt>つづ</rt></ruby>いた。</p>
    <p>Qor yogʻayotganiga qaramay, oʻyin davom etdi.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada «-ib bormoqda» aynan shu jarayonni
  aytadi.</b> «Kamay<em>ib bormoqda</em>», «isi<em>b
  bormoqda</em>», «oʻzgar<em>ib bormoqda</em>» — uchalasida ham
  ish tugamagan, yoʻnalish koʻrsatilyapti. Oddiy «kamayyapti»
  bilan solishtiring: u shu topdagi holatni aytadi,
  «kamayib bormoqda» esa <em>tendensiyani</em>. Yapon tilida
  ham xuddi shu ikkilik bor — <b>〜ている</b> holat,
  <b>〜つつある</b> tendensiya. Shuning uchun gazeta va ilmiy
  matnda つつある juda koʻp: ular dunyoni holat sifatida emas,
  harakat sifatida tasvirlaydi. Oʻzbekcha tarjimada esa
  «-ib bormoqda» ni qoʻysangiz, ohang ham, maʼno ham
  joyida chiqadi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">狭</span>
    <span class="pj-kanji__uz">tor, tang</span>
    <span class="pj-kanji__on">オン: キョウ</span>
    <span class="pj-kanji__kun">KUN: せま(い)</span>
    <span class="pj-kanji__note">狭い部屋 — tor xona · 手狭 (てぜま) — torlik qilmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">残</span>
    <span class="pj-kanji__uz">qolmoq; afsus</span>
    <span class="pj-kanji__on">オン: ザン</span>
    <span class="pj-kanji__kun">KUN: のこ(る)</span>
    <span class="pj-kanji__note">残念 (ざんねん) — afsus · 残業 (ざんぎょう) — qoʻshimcha ish</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">続</span>
    <span class="pj-kanji__uz">davom etmoq</span>
    <span class="pj-kanji__on">オン: ゾク</span>
    <span class="pj-kanji__kun">KUN: つづ(く)・つづ(ける)</span>
    <span class="pj-kanji__note">続ける — davom ettirmoq · 連続 (れんぞく) — ketma-ketlik</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>歩<rt>ある</rt></ruby>くつつ<ruby>考<rt>かんが</rt></ruby>える</p>
  <p class="pe-fix__good">✓ <ruby>歩<rt>ある</rt></ruby><b>き</b>つつ — つつ ます-oʻzagiga ulanadi, lugʻat shakliga emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>狭<rt>せま</rt></ruby>いつつも、<ruby>楽<rt>たの</rt></ruby>しい</p>
  <p class="pe-fix__good">✓ <ruby>狭<rt>せま</rt></ruby>い<b>ながらも</b> — つつ faqat feʼl bilan keladi, sifat bilan emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>兄<rt>あに</rt></ruby>は<ruby>知<rt>し</rt></ruby>っていながら、<ruby>弟<rt>おとうと</rt></ruby>は<ruby>知<rt>し</rt></ruby>らなかった</p>
  <p class="pe-fix__good">✓ <ruby>兄<rt>あに</rt></ruby>は<ruby>知<rt>し</rt></ruby>っていた<b>が</b>、<ruby>弟<rt>おとうと</rt></ruby>は<ruby>知<rt>し</rt></ruby>らなかった — ながら ikkala tomonda bitta ega talab qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>きながら<b>も</b><ruby>勉強<rt>べんきょう</rt></ruby>する (bir vaqtda maʼnosida)</p>
  <p class="pe-fix__good">✓ <ruby>聞<rt>き</rt></ruby>きながら<ruby>勉強<rt>べんきょう</rt></ruby>する — «bir vaqtda» maʼnosiga も qoʻshilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>本屋<rt>ほんや</rt></ruby>が<ruby>減<rt>へ</rt></ruby>るつつある</p>
  <p class="pe-fix__good">✓ <ruby>減<rt>へ</rt></ruby><b>り</b>つつある — bu yerda ham oʻzak kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Bilgani holda ham aytmadi» — boʻsh joyga nima? <ruby>知<rt>し</rt></ruby>ってい___、<ruby>教<rt>おし</rt></ruby>えてくれなかった。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ながらも</b>. も qarshilikni taʼkidlaydi. も siz ham toʻgʻri boʻlardi, lekin も bilan gap aniqroq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>歩<rt>ある</rt></ruby>く ni つつ bilan qoʻshing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>歩<rt>ある</rt></ruby>きつつ</b>. ます-shakli <ruby>歩<rt>ある</rt></ruby>きます, oʻzagi <ruby>歩<rt>ある</rt></ruby>き — oʻshanga つつ ulanadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Tor boʻlsa-da, quvnoq uyimiz» — つつも yoki ながらも?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ながらも</b>: <ruby>狭<rt>せま</rt></ruby>いながらも、<ruby>楽<rt>たの</rt></ruby>しい<ruby>我<rt>わ</rt></ruby>が<ruby>家<rt>や</rt></ruby>. つつ faqat feʼlga ulanadi, sifatga emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>減<rt>へ</rt></ruby>りつつある — maʼnosi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>«Kamayib bormoqda»</b> — jarayon, tendensiya. Bu qarshilik emas: つつある va つつも butunlay boshqa ikki qolip.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega «<ruby>兄<rt>あに</rt></ruby>は<ruby>知<rt>し</rt></ruby>っていながら、<ruby>弟<rt>おとうと</rt></ruby>は<ruby>知<rt>し</rt></ruby>らなかった» notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki <b>ikki boshqa ega</b> bor. ながら ikkala tomonda ham bitta odam talab qiladi. Toʻgʻrisi — PJ-54 dagi が: <ruby>知<rt>し</rt></ruby>っていたが、…</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ながらも</b> — … ga qaramay, … boʻlsa-da</li>
  <li><b>〜つつ</b> — … ib turib (kitobiy)</li>
  <li><b>〜つつも</b> — … ga qaramay (kitobiy)</li>
  <li><b>〜つつある</b> — … boʻlib bormoqda</li>
  <li><b><ruby>狭<rt>せま</rt></ruby>い</b> — tor</li>
  <li><b><ruby>残念<rt>ざんねん</rt></ruby></b> — afsus</li>
  <li><b><ruby>我<rt>わ</rt></ruby>が<ruby>家<rt>や</rt></ruby></b> — oʻz uyimiz</li>
  <li><b><ruby>続<rt>つづ</rt></ruby>く</b> — davom etmoq</li>
  <li><b><ruby>本屋<rt>ほんや</rt></ruby></b> — kitob doʻkoni</li>
  <li><b><ruby>試合<rt>しあい</rt></ruby></b> — musobaqa, oʻyin</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Bitta <b>も</b> «bir vaqtda» ni «…ga qaramay» ga aylantiradi.</li>
    <li><b>つつ</b> = ながら ning kitobiy egizagi, va u <b>faqat feʼl</b> bilan keladi.</li>
    <li><b>〜つつある</b> — qarshilik emas, <b>jarayon</b>: «… boʻlib bormoqda».</li>
  </ul>
</div>
""",
    },
]
