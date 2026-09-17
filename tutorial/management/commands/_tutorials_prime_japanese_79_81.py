# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-79, PJ-80, PJ-81: Blok F ochiladi.

Blok F — yozma til va N3 ga eshik. Uchala dars bitta narsaning uch
qadami: **fikrni otga aylantirish va u bilan mantiq qurish**.
    PJ-79 — ということ: butun gapni bitta otga aylantirish. Yozma
            yapon tilining eng koʻp ishlatiladigan asbobi. Oʻzbekcha
            «degan» / «-lik» bilan bir xil mexanizm.
    PJ-80 — わけ: oʻsha otlashtirilgan fikr ustiga qurilgan xulosa.
            Toʻrtta aʼzo — わけです · わけではない · わけがない ·
            わけにはいかない.
    PJ-81 — はずがない va に違いない: ishonch shkalasi yopiladi.
            PJ-62 dagi はず endi inkorga va kuchaytirishga uzaytiriladi.

⚠️ PJ-80 ning eng katta tuzogʻi — **inkorning joyi**:
〜わけではない (qisman inkor: «degani emas») ≠ 〜ないわけです
(«shuning uchun qilmaydi ekan-da»). Ikkalasida ham bir xil ikki
boʻlak bor, faqat tartibi boshqa, va maʼnosi butunlay boshqa.

⚠️ PJ-81 va PJ-80 bir-biriga yaqin turadi: はずがない (mantiqiy
dalil) va わけがない (kuchliroq, soʻzlashuv). Dars ularni
ataylab yonma-yon qoʻyadi — PJ-80 dan keyin buni qilish mumkin.

⚠️ Kursda hech qachon berilmagan ikki shakl bu batchda ham yoʻq:
意向形 (行こう / 〜ようと思う) va 〜んです. Gate ikkalasini ham
mexanik tekshiradi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_79_81.py --author=prime
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
        "title": "PJ-79: 〜ということ va gapni otga aylantirish",
        "category": "japanese",
        "order": 79,
        "summary": (
            "こと, の va ということ — feʼlni, soʻzni va butun gapni "
            "otga aylantirishning uch yoʻli. Oʻzbekcha «degan» va "
            "«-lik» shu yerda toʻgʻridan-toʻgʻri ishlaydi."
        ),
        "stories": ["わからないということ"],
        "content": """
<h2>PJ-79: 〜ということ va gapni otga aylantirish</h2>

<p>ラノ yaponcha maqola oʻqiyapti. Bitta gap uni toʻxtatib qoʻyadi:</p>

<p><ruby>彼<rt>かれ</rt></ruby>が<ruby>来<rt>こ</rt></ruby>ないということは、みんな<ruby>知<rt>し</rt></ruby>っていた。</p>

<p>Har bir soʻz tanish. <ruby>彼<rt>かれ</rt></ruby> — u,
<ruby>来<rt>こ</rt></ruby>ない — kelmaydi,
<ruby>知<rt>し</rt></ruby>っていた — bilishardi. Lekin oʻrtadagi
«ということは» nima qilib turibdi?</p>

<p>Javob qisqa va butun blok F shu javob ustiga quriladi: yapon tili
<b>butun bir gapni bitta otga aylantira oladi</b>. Shundan keyin oʻsha
ot bilan hamma narsani qilish mumkin — uni bilish, eshitish, unutish,
undan xulosa chiqarish. Yozma yapon tilining eng koʻp ishlatiladigan
asbobi shu.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>feʼlni <b>こと</b> va <b>の</b> bilan otga aylantirasiz</li>
    <li>ikkovining orasidagi farqni bilib tanlaysiz</li>
    <li><b>という</b> bilan ismni, nomni va soʻzni otga ulaysiz</li>
    <li><b>ということ</b> bilan butun gapni bitta otga yigʻasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Gapni otga aylantirish</span>
  <span class="pe-chip pe-chip--s">butun gap, oddiy shaklda</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">ということ</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">bitta ot</span>
</div>

<h3>1. Nega bunga ehtiyoj bor</h3>

<p>Gap ichida faqat ot tura oladigan uyachalar bor. Masalan
<b>を</b> dan oldin ot turadi, <b>は</b> dan oldin ot turadi,
«qiyin», «qiziq», «muhim» degan sifatlarning egasi ham ot boʻladi.</p>

<p>Lekin biz aytmoqchi boʻlgan narsa koʻpincha ot emas —
<em>harakat</em> yoki butun bir <em>gap</em>. «Oʻqish qiyin»,
«kelmasligini bilaman», «uning talaba ekani muhim». Shu paytda
yapon tili feʼlga yoki gapga bitta kichik soʻz ulaydi va uni ot
qilib qoʻyadi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>む<b>こと</b></span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__v"><ruby>楽<rt>たの</rt></ruby>しい</span>
  <span class="pj-joshi__uz">Kitob oʻqish qiziq. — «oʻqi<b>sh</b>» oʻzbekchada ham ot.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu ish har kuni qilinadi, faqat siz sezmaysiz.</b>
  «Oʻqi<em>moq</em>» — feʼl. «Oʻqi<em>sh</em>» — ot. Bitta qoʻshimcha
  qoʻshdik, va soʻz endi «qiyin» ning egasi boʻla oladi:
  <em>oʻqish qiyin</em>. Yana bittasi bor: «kel<em>gan</em>-
  <em>lik</em>-ini bilaman» — bu yerda butun gap («u keldi») bitta
  otga aylanib, keyin <b>-ni</b> qoʻshimchasini olyapti.
  Yapon tili aynan shu ikki ishni qiladi, faqat qoʻshimcha
  soʻzning oxiriga emas, <b>gapning oxiriga</b> yopishadi:
  «-sh» oʻrnida <b>こと</b> yoki <b>の</b>, «-lik» oʻrnida
  <b>ということ</b>. Shuning uchun bu dars yangi mantiq emas —
  tanish mantiqning yaponcha kiyimi.</p>
</div>

<h3>2. こと va の — qaysi biri qachon</h3>

<p>Ikkalasi ham feʼlni otga aylantiradi va koʻp joyda oʻrnini
almashtira oladi. Lekin ular bir xil emas, va farq bitta savol bilan
hal boʻladi: <b>bu harakatni koʻz bilan koʻrasizmi, quloq bilan
eshitasizmi?</b></p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">の — koʻrinadigan, eshitiladigan</p>
    <p><ruby>子供<rt>こども</rt></ruby>が<ruby>泣<rt>な</rt></ruby>いている<b>の</b>を<ruby>見<rt>み</rt></ruby>ました。</p>
    <p>Bolaning yigʻlayotganini koʻrdim. Aniq, bir martalik, sezgi
    bilan ushlanadigan harakat.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">こと — fikr, gap, qaror</p>
    <p><ruby>毎日<rt>まいにち</rt></ruby><ruby>走<rt>はし</rt></ruby>る<b>こと</b>を<ruby>決<rt>き</rt></ruby>めました。</p>
    <p>Har kuni yugurishni qaror qildim. Mavhum, umumiy, boshda
    turadigan harakat.</p></div>
</div>

<p>Shuning uchun feʼlning oʻzi tanlovni deyarli aytib beradi.
Quyidagi jadvalni yodlash kerak emas — uni bir marta oʻqish kifoya,
keyin quloq oʻzi tanlaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Keyingi feʼl</th><th>Qaysi biri</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>見<rt>み</rt></ruby>る · <ruby>聞<rt>き</rt></ruby>く · <ruby>待<rt>ま</rt></ruby>つ · <ruby>手伝<rt>てつだ</rt></ruby>う</td>
      <td class="pj-end">の</td>
      <td class="pj-res"><ruby>歌<rt>うた</rt></ruby>っている<b>の</b>を<ruby>聞<rt>き</rt></ruby>いた</td>
      <td class="pj-uz">kuylayotganini eshitdim</td></tr>
  <tr><td class="pj-stem"><ruby>決<rt>き</rt></ruby>める · <ruby>約束<rt>やくそく</rt></ruby>する · <ruby>伝<rt>つた</rt></ruby>える</td>
      <td class="pj-end">こと</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>く<b>こと</b>を<ruby>約束<rt>やくそく</rt></ruby>した</td>
      <td class="pj-uz">borishga vada berdim</td></tr>
  <tr><td class="pj-stem"><ruby>好<rt>す</rt></ruby>き · <ruby>上手<rt>じょうず</rt></ruby> · <ruby>下手<rt>へた</rt></ruby></td>
      <td class="pj-end">の (こと ham boʻladi)</td>
      <td class="pj-res"><ruby>泳<rt>およ</rt></ruby>ぐ<b>の</b>が<ruby>好<rt>す</rt></ruby>きです</td>
      <td class="pj-uz">suzishni yaxshi koʻraman</td></tr>
  <tr><td class="pj-stem">〜ができる · <ruby>趣味<rt>しゅみ</rt></ruby>は〜です</td>
      <td class="pj-end">faqat こと</td>
      <td class="pj-res"><ruby>話<rt>はな</rt></ruby>す<b>こと</b>ができます</td>
      <td class="pj-uz">gapira olaman</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Ikkita joy qatʼiy.</b> PJ-41 dagi
  <b>〜ことができます</b> va «mening ovunchogʻim…» degan
  <b><ruby>趣味<rt>しゅみ</rt></ruby>は〜ことです</b> — bularda
  faqat <b>こと</b> turadi, の hech qachon emas. Qolgan
  hamma joyda tanlov yuqoridagi savol bilan hal boʻladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">イノムさんが<span class="pe-hl pe-hl--o"><ruby>走<rt>はし</rt></ruby>っているの</span>を<ruby>見<rt>み</rt></ruby>ました。</p>
  <p class="pe-ex__uz">Inomning yugurib ketayotganini koʻrdim.</p>
  <p class="pe-ex__why">Koʻz bilan koʻrilgan aniq sahna — <b>の</b>. Bu yerda こと ishlatilsa, gap kitobiy va gʻalati chiqadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>の<ruby>趣味<rt>しゅみ</rt></ruby>は<span class="pe-hl pe-hl--o"><ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ること</span>です。</p>
  <p class="pe-ex__uz">Mening ovunchogʻim — surat olish.</p>
  <p class="pe-ex__why">«Ovunchoq» — bir martalik harakat emas, umumiy odat. Qatʼiy qolip: <b>こと</b>.</p>
</div>

<h3>3. 〜という + ot — «degan»</h3>

<p>ということ ni tushunish uchun avval uning yarmini koʻrish kerak.
<b>という</b> — «deyiladigan», «degan» degani, va u ismni,
nomni yoki notanish soʻzni otga bogʻlaydi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s">「ムニラ」という<ruby>名前<rt>なまえ</rt></ruby></span>は<ruby>珍<rt>めずら</rt></ruby>しいです。</p>
  <p class="pe-ex__uz">«Munira» degan ism kam uchraydi.</p>
  <p class="pe-ex__why">Oʻzbekcha «degan» qayerda tursa, yaponcha <b>という</b> ham oʻsha yerda turadi — soʻzdan keyin, otdan oldin.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>去年<rt>きょねん</rt></ruby><span class="pe-hl pe-hl--o"><ruby>金沢<rt>かなざわ</rt></ruby>という<ruby>町<rt>まち</rt></ruby></span>へ<ruby>行<rt>い</rt></ruby>きました。</p>
  <p class="pe-ex__uz">Oʻtgan yili Kanazava degan shaharga bordim.</p>
  <p class="pe-ex__why">Tinglovchi bu shaharni bilmasligi mumkin — shuning uchun <b>という</b> qoʻyiladi. Tanish nom bilan u tushib qoladi: <ruby>東京<rt>とうきょう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu darsning eng qulay sovgʻasi.</b> Oʻzbek tilidagi
  <b>«degan»</b> va yaponcha <b>という</b> deyarli bir xil ishlaydi:
  ikkalasi ham gapiruvchi tomondan emas, <em>nomlash</em>
  tomonidan turadi. «Kanazava <b>degan</b> shahar»,
  «"Munira" <b>degan</b> ism», «"Ertaga kelmayman" <b>degani</b>».
  Shuning uchun bu qolipni yodlash oʻrniga, oʻzbekcha gapni
  ichingizda tuzing va «degan» qayerda turganini koʻring —
  という aynan oʻsha joyga tushadi. Rus tilidan yoki ingliz
  tilidan tarjima qilsangiz, bu qulaylik yoʻqoladi.</p>
</div>

<h3>4. ということ — butun gap, bitta ot</h3>

<p>Endi ikkisini qoʻshamiz. <b>という</b> gapni olib keladi,
<b>こと</b> uni otga aylantiradi. Natijada butun gap jumlaning
ichida bitta soʻzdek harakat qiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Gap</th><th>Otlashgani</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">feʼl</td>
      <td class="pj-end"><ruby>彼<rt>かれ</rt></ruby>が<ruby>来<rt>こ</rt></ruby>ない</td>
      <td class="pj-res"><ruby>彼<rt>かれ</rt></ruby>が<ruby>来<rt>こ</rt></ruby>ない<b>ということ</b></td>
      <td class="pj-uz">uning kelmasligi</td></tr>
  <tr><td class="pj-stem">い-sifat</td>
      <td class="pj-end"><ruby>試験<rt>しけん</rt></ruby>が<ruby>難<rt>むずか</rt></ruby>しい</td>
      <td class="pj-res"><ruby>試験<rt>しけん</rt></ruby>が<ruby>難<rt>むずか</rt></ruby>しい<b>ということ</b></td>
      <td class="pj-uz">imtihonning qiyinligi</td></tr>
  <tr><td class="pj-stem">な-sifat</td>
      <td class="pj-end"><ruby>元気<rt>げんき</rt></ruby><b>だ</b></td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby><b>だということ</b></td>
      <td class="pj-uz">sogʻ-salomatligi</td></tr>
  <tr><td class="pj-stem">ot</td>
      <td class="pj-end"><ruby>学生<rt>がくせい</rt></ruby><b>だ</b></td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby><b>だということ</b></td>
      <td class="pj-uz">talaba ekani</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Oxirgi ikki qator — darsning eng koʻp unutiladigan joyi.</b>
  ということ oldiga <b>oddiy shakl</b> tushadi, va ot bilan
  な-sifatning oddiy shakli <b>だ</b> bilan tugaydi. Shuning uchun
  «<ruby>学生<rt>がくせい</rt></ruby>ということ» yetarli emas —
  «<ruby>学生<rt>がくせい</rt></ruby><b>だ</b>ということ» kerak.
  Bu PJ-45 dagi <ruby>普通体<rt>ふつうたい</rt></ruby> ning bevosita davomi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--o">パリさんが<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>すということ</span>を<ruby>昨日<rt>きのう</rt></ruby><ruby>聞<rt>き</rt></ruby>きました。</p>
  <p class="pe-ex__uz">Parining koʻchib ketishini kecha eshitdim.</p>
  <p class="pe-ex__why">Butun gap («Pari koʻchadi») bitta otga aylandi va <b>を</b> ni oldi. Oʻzbekchada ham aynan shunday: «koʻchib ketish<b>-i-ni</b>».</p>
</div>

<h3>5. ということ ning uch vazifasi</h3>

<p>Bitta qolip, uch xil ish. Uchalasini tanib olsangiz, yaponcha
maqola oʻqish sezilarli osonlashadi.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h">1 — Faktni koʻtarib yurish</p>
    <p><ruby>彼<rt>かれ</rt></ruby>が<ruby>知<rt>し</rt></ruby>らないということ<b>を</b><ruby>忘<rt>わす</rt></ruby>れていた。</p>
    <p>Uning bilmasligini unutib qoʻygan edim.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">2 — Maʼnosini soʻrash</p>
    <p>「<ruby>遠慮<rt>えんりょ</rt></ruby>」とはどういうこと<b>ですか</b>。</p>
    <p>«Enryo» degani nima degani?</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">3 — Xulosa chiqarish</p>
    <p><ruby>電気<rt>でんき</rt></ruby>が<ruby>消<rt>き</rt></ruby>えている。ということ<b>は</b>、もう<ruby>寝<rt>ね</rt></ruby>た。</p>
    <p>Chiroq oʻchgan. Demak, allaqachon uxlagan.</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Uchinchisi — kundalik nutqda ham juda koʻp.</b>
  Gapning boshida yolgʻiz turgan «<b>ということは</b>» oʻzbekcha
  <b>«demak»</b> degan soʻzning oʻzi. Uni eshitsangiz, keyin
  xulosa kelishini bilasiz. Yaponlar telefonda, dars xonasida,
  doʻkonda shu soʻz bilan fikrni yigʻishtiradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>自分<rt>じぶん</rt></ruby>が<ruby>分<rt>わ</rt></ruby>からない<span class="pe-hl pe-hl--s">ということ</span>が<ruby>分<rt>わ</rt></ruby>かるのは<ruby>大切<rt>たいせつ</rt></ruby>だ。</p>
  <p class="pe-ex__uz">Oʻzining bilmasligini bilish muhim.</p>
  <p class="pe-ex__why">Bitta gapda ikkala asbob ham bor: <b>ということ</b> gapni otga aylantirdi, <b>の</b> esa «bilish» feʼlini otga aylantirdi.</p>
</div>

<h3>6. Uchtasi bitta jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Asbob</th><th>Nimani otga aylantiradi</th><th>Qayerda</th></tr>
  <tr><td class="pj-stem">の</td><td class="pj-uz">bitta feʼlni — koʻriladigan, eshitiladigan harakat</td>
      <td class="pj-res">kundalik nutq</td></tr>
  <tr><td class="pj-stem">こと</td><td class="pj-uz">bitta feʼlni — mavhum, umumiy harakat</td>
      <td class="pj-res">hamma joyda</td></tr>
  <tr><td class="pj-stem">ということ</td><td class="pj-uz">butun gapni — eshitilgan, oʻqilgan, xulosa qilingan fikr</td>
      <td class="pj-res">yozma til, xabar, maqola</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Qaysi birini tanlashni oʻzbekcha tarjima aytib beradi.</b>
  Gapni ichingizda oʻzbekchada tuzing va oxiriga qarang.
  «Yugur<b>ish</b> foydali» — bitta feʼl, mavhum: <b>こと</b>.
  «Yugur<b>ayotganini</b> koʻrdim» — koʻz bilan koʻrilgan sahna:
  <b>の</b>. «Kelma<b>sligini</b> eshitdim» — butun gap, birovdan
  eshitilgan: <b>ということ</b>. Uchala oʻzbekcha qoʻshimcha
  («-sh», «-ayotganini», «-sligini») bir-biridan farq qilgani
  uchun, yaponchada ham uchta boshqa asbob turishi mantiqiy
  koʻrinadi. Oʻzbek tili bu yerda lugʻatdan ham, jadvaldan ham
  tezroq ishlaydi — faqat unga ishonish kerak.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">事</span>
    <span class="pj-kanji__uz">ish, narsa, hodisa</span>
    <span class="pj-kanji__on">オン: ジ</span>
    <span class="pj-kanji__kun">KUN: こと</span>
    <span class="pj-kanji__note">事実 (じじつ) — haqiqat · 大事 (だいじ) — muhim · 仕事 (しごと) — ish</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">意</span>
    <span class="pj-kanji__uz">fikr, niyat, maʼno</span>
    <span class="pj-kanji__on">オン: イ</span>
    <span class="pj-kanji__kun">KUN: — </span>
    <span class="pj-kanji__note">意味 (いみ) — maʼno · 注意 (ちゅうい) — diqqat · 意見 (いけん) — fikr</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>日本語<rt>にほんご</rt></ruby>を<ruby>話<rt>はな</rt></ruby>す<b>の</b>ができます</p>
  <p class="pe-fix__good">✓ <ruby>話<rt>はな</rt></ruby>す<b>こと</b>ができます — 〜ことができる qatʼiy qolip, の bu yerga tushmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>趣味<rt>しゅみ</rt></ruby>は<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>む<b>の</b>です</p>
  <p class="pe-fix__good">✓ <ruby>趣味<rt>しゅみ</rt></ruby>は<ruby>読<rt>よ</rt></ruby>む<b>こと</b>です — «ovunchoq» qolipida ham faqat こと.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>子供<rt>こども</rt></ruby>が<ruby>泣<rt>な</rt></ruby>いている<b>こと</b>を<ruby>見<rt>み</rt></ruby>た</p>
  <p class="pe-fix__good">✓ <ruby>泣<rt>な</rt></ruby>いている<b>の</b>を<ruby>見<rt>み</rt></ruby>た — koʻz bilan koʻrilgan sahna har doim の.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ 「ムニラ」<b>と</b><ruby>名前<rt>なまえ</rt></ruby></p>
  <p class="pe-fix__good">✓ 「ムニラ」<b>という</b><ruby>名前<rt>なまえ</rt></ruby> — «degan» ni tashlab ketmang; と yolgʻiz otga ulanmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>ということを<ruby>知<rt>し</rt></ruby>らなかった</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>だ</b>ということを<ruby>知<rt>し</rt></ruby>らなかった — ot va な-sifat oddiy shaklda だ bilan tugaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Suzishni yaxshi koʻraman» — の yoki こと?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>泳<rt>およ</rt></ruby>ぐのが<ruby>好<rt>す</rt></ruby>きです</b>. 〜が<ruby>好<rt>す</rt></ruby>き bilan ikkalasi ham boʻladi, lekin kundalik nutqda <b>の</b> tabiiyroq eshitiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Boʻsh joyni toʻldiring: <ruby>先生<rt>せんせい</rt></ruby>が<ruby>病気<rt>びょうき</rt></ruby>___ということを<ruby>聞<rt>き</rt></ruby>きました。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>だ</b> — <ruby>病気<rt>びょうき</rt></ruby> na-sifat, oddiy shakli <ruby>病気<rt>びょうき</rt></ruby>だ. Toʻliq gap: <ruby>先生<rt>せんせい</rt></ruby>が<ruby>病気<rt>びょうき</rt></ruby>だということを<ruby>聞<rt>き</rt></ruby>きました.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Kanazava degan shahar» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>金沢<rt>かなざわ</rt></ruby>という<ruby>町<rt>まち</rt></ruby></b> — oʻzbekcha «degan» qayerda tursa, という ham oʻsha yerda.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>電気<rt>でんき</rt></ruby>が<ruby>消<rt>き</rt></ruby>えている。ということは、… — bu yerda «ということは» nima maʼnoni beryapti?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>«Demak»</b>. Gapning boshida yolgʻiz turgan ということは xulosa kelishini bildiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Bolaning yigʻlayotganini koʻrdim» va «Har kuni yugurishni qaror qildim» — qaysi biriga の, qaysi biriga こと?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisi — <b>の</b> (<ruby>泣<rt>な</rt></ruby>いているのを<ruby>見<rt>み</rt></ruby>ました), koʻz bilan koʻrilgan. Ikkinchisi — <b>こと</b> (<ruby>走<rt>はし</rt></ruby>ることを<ruby>決<rt>き</rt></ruby>めました), boshda turgan mavhum qaror.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜こと</b> — feʼlni otga aylantiradi (mavhum)</li>
  <li><b>〜の</b> — feʼlni otga aylantiradi (koʻrinadigan)</li>
  <li><b>〜という + ot</b> — «… degan …»</li>
  <li><b>〜ということ</b> — butun gap bitta ot</li>
  <li><b>ということは</b> — demak</li>
  <li><b>〜とはどういうことですか</b> — … nima degani?</li>
  <li><b><ruby>意味<rt>いみ</rt></ruby></b> — maʼno</li>
  <li><b><ruby>事実<rt>じじつ</rt></ruby></b> — haqiqat, fakt</li>
  <li><b><ruby>珍<rt>めずら</rt></ruby>しい</b> — kam uchraydigan</li>
  <li><b><ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>す</b> — koʻchib oʻtmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>の</b> — koʻrinadigan harakat, <b>こと</b> — mavhum harakat.</li>
    <li><b>という</b> = oʻzbekcha <b>«degan»</b>, oʻsha joyda turadi.</li>
    <li>ということ oldida <b>oddiy shakl</b> turadi — ot va な-sifat <b>だ</b> bilan.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-80: 〜わけです, 〜わけではない — mantiqiy xulosa",
        "category": "japanese",
        "order": 80,
        "summary": (
            "わけ — «sabab-mantiq» degan ot va uning toʻrtta aʼzosi: "
            "わけです (shuning uchun ekan-da), わけではない (degani "
            "emas), わけがない (boʻlishi mumkin emas), わけにはいかない "
            "(iloji yoʻq)."
        ),
        "stories": ["かようびの パンや"],
        "content": """
<h2>PJ-80: 〜わけです, 〜わけではない — mantiqiy xulosa</h2>

<p>ムニラ sinfdoshi bilan gaplashyapti. Uning yaponchasi juda ravon,
va ムニラ sababini bilmaydi. Keyin bilib qoladi: u bolaligida uch yil
<ruby>大阪<rt>おおさか</rt></ruby>da yashagan ekan.</p>

<p><ruby>三年<rt>さんねん</rt></ruby><ruby>住<rt>す</rt></ruby>んでいた。ああ、それで<ruby>上手<rt>じょうず</rt></ruby>なわけですね。</p>

<p>Bu yerda ムニラ yangi xabar bermayapti. U <b>allaqachon</b>
bilgan narsani (yaponchasi yaxshi) endi sababga ulayapti va
«shuning uchun ekan-da» deyapti. Yapon tilida shu ish uchun
alohida soʻz bor: <b>わけ</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>わけです</b> bilan xulosani ovoz chiqarib aytasiz</li>
    <li><b>わけではない</b> bilan qisman inkor qilasiz</li>
    <li><b>わけがない</b> va <b>わけにはいかない</b> ni ajratasiz</li>
    <li>inkorning <em>joyi</em> maʼnoni qanday oʻzgartirishini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Xulosa</span>
  <span class="pe-chip pe-chip--s">oddiy shakl</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">わけです</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">shuning uchun ekan-da</span>
</div>

<h3>1. わけ nima</h3>

<p><ruby>訳<rt>わけ</rt></ruby> — mustaqil ot, maʼnosi «sabab»,
«mantiq», «ish shunday boʻlgani». PJ-79 dagi こと kabi, u ham
<em>rasmiy ot</em> (<ruby>形式名詞<rt>けいしきめいし</rt></ruby>):
oldiga butun gap tushadi va uni bitta otga aylantiradi. Farqi
shundaki, こと gapni shunchaki ot qiladi, わけ esa unga
<b>«bu yerda mantiq bor»</b> degan maʼno qoʻshadi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>三年<rt>さんねん</rt></ruby><ruby>住<rt>す</rt></ruby>んでいた</span>
  <span class="pj-joshi__p">から<small>SABAB</small></span>
  <span class="pj-joshi__v"><ruby>上手<rt>じょうず</rt></ruby>なわけです</span>
  <span class="pj-joshi__uz">Uch yil yashagan — shuning uchun yaxshi bilar ekan-da.</span>
</div>

<div class="pe-call pe-rule">
  <p><b>Ulanish PJ-75 dagi ようだ bilan bir xil.</b>
  feʼl va い-sifat — yalangʻoch
  (<ruby>降<rt>ふ</rt></ruby>るわけです);
  な-sifat — <b>な</b> bilan
  (<ruby>上手<rt>じょうず</rt></ruby><b>な</b>わけです);
  ot — <b>という</b> bilan
  (<ruby>学生<rt>がくせい</rt></ruby><b>という</b>わけです).
  Oxirgi qatorni PJ-79 dan tanidingiz — という oʻsha «degan».</p>
</div>

<h3>2. わけです — sabab emas, natija</h3>

<p>Bu darsning eng nozik joyi. PJ-53 da siz <b>から</b> va
<b>ので</b> ni oʻrgandingiz — ular <em>sababni</em> aytadi.
わけ esa sababni aytmaydi: u <em>natijani</em> aytadi, va
uni allaqachon maʼlum boʻlgan sababga ulaydi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">から — sababni beradi</p>
    <p><ruby>三年<rt>さんねん</rt></ruby><ruby>住<rt>す</rt></ruby>んでいた<b>から</b>、<ruby>上手<rt>じょうず</rt></ruby>です。</p>
    <p>Uch yil yashagani uchun yaxshi biladi. Yangi maʼlumot — sabab.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">わけです — xulosani beradi</p>
    <p>ああ、それで<ruby>上手<rt>じょうず</rt></ruby>な<b>わけです</b>ね。</p>
    <p>Voy, shuning uchun yaxshi bilar ekan-da. Yangi maʼlumot yoʻq — tushunish bor.</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>Shuning uchun わけです bilan yangi xabar berib boʻlmaydi.</b>
  «Ertaga yomgʻir yogʻadi» deb birinchi marta aytayotgan boʻlsangiz,
  <ruby>降<rt>ふ</rt></ruby>るわけです emas —
  <ruby>降<rt>ふ</rt></ruby>るそうです (PJ-74) yoki
  <ruby>降<rt>ふ</rt></ruby>るでしょう (PJ-62) kerak. わけ faqat
  tinglovchi <em>oʻzi ham chiqara oladigan</em> xulosani ovoz
  chiqarib aytadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>止<rt>と</rt></ruby>まっている。<span class="pe-hl pe-hl--v">それで<ruby>道<rt>みち</rt></ruby>が<ruby>混<rt>こ</rt></ruby>んでいるわけです</span>。</p>
  <p class="pe-ex__uz">Poyezd toʻxtab qolibdi. Shuning uchun yoʻl tiqilinch ekan-da.</p>
  <p class="pe-ex__why">Tiqilinchni gapiruvchi allaqachon koʻrgan. Yangilik — uning <b>sababi</b> bilan bogʻlanishi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">イノムさんは<ruby>毎日<rt>まいにち</rt></ruby><ruby>五時<rt>ごじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きる。<span class="pe-hl pe-hl--v">よく<ruby>寝<rt>ね</rt></ruby>ているわけです</span>。</p>
  <p class="pe-ex__uz">Inom har kuni soat beshda turadi. Demak, yaxshi uxlar ekan-da.</p>
  <p class="pe-ex__why">Birinchi gap dalil, ikkinchisi undan chiqadigan xulosa. PJ-79 dagi «ということは» bilan deyarli bir xil ish.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu ish bitta qoʻshimcha bilan qilinadi:
  «-ekan-da».</b> «Voy, shuning uchun yaxshi bilar <b>ekan-da</b>»,
  «Demak, charchagan <b>ekan-da</b>». Bu qoʻshimcha ham yangi
  xabar bermaydi — u gapiruvchining boshida endigina yopilgan
  mantiqni ovoz chiqarib aytadi. わけです aynan shu narsa.
  Shuning uchun tarjima qilganda «sabab» degan soʻzni izlamang:
  «ekan-da» ni izlang. Agar oʻzbekcha gapga «ekan-da» tabiiy
  tushsa, yaponchasida わけです turadi; tushmasa —
  から yoki ので kerak.</p>
</div>

<h3>3. わけではない — «degani emas»</h3>

<p>Endi inkorga oʻtamiz, va bu qolip yapon tilida juda koʻp
ishlatiladi. <b>〜わけではない</b> butun gapni emas, undan
chiqadigan <em>xulosani</em> inkor qiladi — yaʼni qisman
inkor.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>嫌<rt>きら</rt></ruby>い<span class="pe-hl pe-hl--neg">なわけではありません</span>。ただ、<ruby>時間<rt>じかん</rt></ruby>がないだけです。</p>
  <p class="pe-ex__uz">Yomon koʻraman degani emas. Shunchaki vaqt yoʻq.</p>
  <p class="pe-ex__why">«Yoqtirmaydi» degan xulosani rad etyapti, «yoqtiraman» deb tasdiqlamayapti. Oradagi yumshoq javob shu.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchasi shu qadar aniqki, yodlashning hojati yoʻq:
  «… degani emas».</b> «Yomon koʻraman <b>degani emas</b>»,
  «Hammasini tushundim <b>degani emas</b>», «Boy <b>degani emas</b>».
  Yaponcha わけではない ham xuddi shu ikki qismdan iborat:
  <b>わけ</b> — «degani», <b>ではない</b> — «emas». Soʻzma-soʻz
  bir xil. Va vazifasi ham bir xil — toʻgʻridan-toʻgʻri
  «yoʻq» deyish qoʻpol boʻlgan joyda ishlatiladi. Yapon
  madaniyatida bu juda qadrlanadi, shuning uchun bu qolipni
  suhbatda tez-tez eshitasiz.</p>
</div>

<h3>4. ⚠️ Inkorning joyi — darsning eng katta tuzogʻi</h3>

<p>Bitta gapda ikkita boʻlak bor: <b>わけ</b> va <b>ない</b>.
Ularning tartibi maʼnoni butunlay oʻzgartiradi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h"><ruby>好<rt>す</rt></ruby>きなわけではない</p>
    <p>«Yoqtiraman degani emas.»</p>
    <p>Inkor <b>xulosaga</b> tegadi. Ehtimol biroz yoqtiradi, ehtimol beparvo — lekin «yoqtiradi» deyish notoʻgʻri.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h"><ruby>好<rt>す</rt></ruby>きではないわけです</p>
    <p>«Demak, yoqtirmas ekan-da.»</p>
    <p>Inkor <b>gapga</b> tegadi, わけ esa uni xulosa qiladi. Yoqtirmasligi aniq.</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>Qoidani bitta jumla bilan yodlang:</b> ない
  <em>わけdan oldin</em> boʻlsa — gap inkor qilinadi;
  ない <em>わけdan keyin</em> boʻlsa — xulosa inkor qilinadi.
  Oʻzbekcha ham shunday: «yoqtirmaydi <em>ekan-da</em>» va
  «yoqtiradi <em>degani emas</em>» — ikkalasida ham «emas»
  bor, lekin boshqa joyda turibdi.</p>
</div>

<h3>5. わけがない va わけにはいかない</h3>

<p>わけ oilasining qolgan ikki aʼzosi. Ular ham inkor bilan
tugaydi, lekin butunlay boshqa ish qiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Maʼnosi</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem">〜わけです</td><td class="pj-uz">xulosa</td>
      <td class="pj-end"><ruby>上手<rt>じょうず</rt></ruby>なわけです</td>
      <td class="pj-res">yaxshi bilar ekan-da</td></tr>
  <tr><td class="pj-stem">〜わけではない</td><td class="pj-uz">qisman inkor</td>
      <td class="pj-end"><ruby>嫌<rt>きら</rt></ruby>いなわけではない</td>
      <td class="pj-res">yomon koʻraman degani emas</td></tr>
  <tr><td class="pj-stem">〜わけがない</td><td class="pj-uz">qatʼiy inkor</td>
      <td class="pj-end"><ruby>彼<rt>かれ</rt></ruby>が<ruby>知<rt>し</rt></ruby>っているわけがない</td>
      <td class="pj-res">bilishi mumkin emas</td></tr>
  <tr><td class="pj-stem">〜わけにはいかない</td><td class="pj-uz">iloji yoʻq</td>
      <td class="pj-end"><ruby>休<rt>やす</rt></ruby>むわけにはいかない</td>
      <td class="pj-res">dam olishning iloji yoʻq</td></tr>
</table></div>

<p><b>わけがない</b> — «mantiqan imkonsiz». Bu kuchli soʻz:
gapiruvchi shunchaki shubhalanmayapti, ehtimolni butunlay
rad etyapti.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">パリさんが<ruby>約束<rt>やくそく</rt></ruby>を<span class="pe-hl pe-hl--neg"><ruby>忘<rt>わす</rt></ruby>れるわけがありません</span>。</p>
  <p class="pe-ex__uz">Pari vadasini unutishi mumkin emas.</p>
  <p class="pe-ex__why">Muloyim shakli — わけが<b>ありません</b>. Kundalik nutqda わけがない.</p>
</div>

<p><b>〜わけにはいかない</b> esa qobiliyat haqida emas.
Jismonan qila olasiz — lekin vada, burch yoki odob yoʻl
bermaydi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>約束<rt>やくそく</rt></ruby>したから、<span class="pe-hl pe-hl--v"><ruby>行<rt>い</rt></ruby>かないわけにはいきません</span>。</p>
  <p class="pe-ex__uz">Vada berganman, shuning uchun bormasdan boʻlmaydi.</p>
  <p class="pe-ex__why">Ikki inkor bir-birini yeydi: «bormaslikning iloji yoʻq» = <b>borishim shart</b>. PJ-33 dagi 〜なければなりません bilan bir maʼno, ohangi ogʻirroq.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>〜ないわけにはいかない — eng foydali shakl.</b>
  U «qilishim kerak» ni juda tabiiy qilib aytadi va
  sababni ham sezdiradi: men xohlamayman, lekin holat
  majbur qilyapti. Imtihon, ish, oilaviy majlis —
  yaponcha kundalik hayotda bu ohang har kuni kerak
  boʻladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>«Iloji yoʻq» — oʻzbekchada ham qobiliyat haqida emas.</b>
  «Bora olmayman» va «borishning iloji yoʻq» — ikki boshqa gap.
  Birinchisi kuchim yetmaydi deydi, ikkinchisi esa kuchim
  yetadi, lekin holat yoʻl bermaydi deydi. Yapon tilida bu
  farq juda aniq boʻlingan: qobiliyat uchun PJ-42 dagi
  imkoniyat shakli
  (<ruby>行<rt>い</rt></ruby>けません), burch uchun esa
  <b>わけにはいきません</b>. Oʻquvchilar koʻpincha ikkalasini
  ham <ruby>行<rt>い</rt></ruby>けません deb aytadi va gap
  bir oz yolgʻon chiqadi — chunki ular aslida bora oladi,
  shunchaki bormasligi kerak. Ikkita gapni yonma-yon
  yodlang, farqi umrbod esda qoladi.</p>
</div>

<h3>6. わけ va はず — ikkovi bir narsa emas</h3>

<p>PJ-62 da siz <b>はずです</b> ni koʻrgansiz. Ular
oʻxshab ketadi, lekin vaqt oʻqi boʻyicha qarama-qarshi
turadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Qachon aytiladi</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">〜はずです</td><td class="pj-uz"><b>oldin</b> — hali koʻrmadim</td>
      <td class="pj-res">shunday boʻlishi kerak, kutyapman</td></tr>
  <tr><td class="pj-stem">〜わけです</td><td class="pj-uz"><b>keyin</b> — koʻrdim va tushundim</td>
      <td class="pj-res">shuning uchun shunday ekan-da</td></tr>
</table></div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">訳</span>
    <span class="pj-kanji__uz">sabab; tarjima</span>
    <span class="pj-kanji__on">オン: ヤク</span>
    <span class="pj-kanji__kun">KUN: わけ</span>
    <span class="pj-kanji__note">訳 (わけ) — sabab, mantiq · 翻訳 (ほんやく) — tarjima · 通訳 (つうやく) — ogʻzaki tarjimon</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">混</span>
    <span class="pj-kanji__uz">aralashmoq, tiqilmoq</span>
    <span class="pj-kanji__on">オン: コン</span>
    <span class="pj-kanji__kun">KUN: こ(む) · ま(ぜる)</span>
    <span class="pj-kanji__note">混んでいる (こんでいる) — tiqilinch · 混雑 (こんざつ) — gavjumlik</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>上手<rt>じょうず</rt></ruby>わけです</p>
  <p class="pe-fix__good">✓ <ruby>上手<rt>じょうず</rt></ruby><b>な</b>わけです — な-sifat わけ oldida な ni saqlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>わけではありません</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>という</b>わけではありません — ot わけ oldida という ni oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>明日<rt>あした</rt></ruby><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るわけです<br><small>(birinchi marta xabar berayotib)</small></p>
  <p class="pe-fix__good">✓ <ruby>降<rt>ふ</rt></ruby>るそうです — わけ yangi xabar bermaydi, faqat tanish narsani sababga ulaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>好<rt>す</rt></ruby>きではないわけです<br><small>(«yoqtiraman degani emas» demoqchi boʻlsangiz)</small></p>
  <p class="pe-fix__good">✓ <ruby>好<rt>す</rt></ruby>きなわけではありません — inkor わけ<b>dan keyin</b> turishi kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>かないわけにはいきません = «bormayman»</p>
  <p class="pe-fix__good">✓ = «bormasdan boʻlmaydi», yaʼni <b>borishim shart</b> — ikki inkor bir-birini yeydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>元気<rt>げんき</rt></ruby> ni わけです bilan bogʻlang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>元気<rt>げんき</rt></ruby>なわけです</b> — な-sifat わけ oldida <b>な</b> ni saqlaydi, xuddi ようだ oldidagidek.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Yomon koʻraman degani emas» — わけではない qayerga tushadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>嫌<rt>きら</rt></ruby>いなわけではありません</b>. Inkor わけ<b>dan keyin</b>, chunki inkor qilinayotgani xulosa.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Ertaga yomgʻir yogʻadi» degan yangi xabarni わけです bilan aytsa boʻladimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> わけ yangi maʼlumot bermaydi — u tinglovchi ham chiqara oladigan xulosani aytadi. Yangi xabar uchun そうです yoki でしょう.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>休<rt>やす</rt></ruby>むわけにはいきません — maʼnosi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>«Dam olishning iloji yoʻq.»</b> Jismonan dam ola oladi — lekin burch yoʻl bermaydi. Bu qobiliyat haqida emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. はずです va わけです — qaysi biri hodisadan <em>keyin</em> aytiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>わけです</b>. はず — koʻrmasdan oldingi kutish; わけ — koʻrgandan keyingi tushunish.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜わけです</b> — shuning uchun … ekan-da</li>
  <li><b>〜わけではない</b> — … degani emas</li>
  <li><b>〜わけがない</b> — … boʻlishi mumkin emas</li>
  <li><b>〜わけにはいかない</b> — … ning iloji yoʻq</li>
  <li><b>〜ないわけにはいかない</b> — … qilmasdan boʻlmaydi</li>
  <li><b>それで</b> — shuning uchun</li>
  <li><b>ただ</b> — shunchaki, faqat</li>
  <li><b><ruby>混<rt>こ</rt></ruby>んでいる</b> — tiqilinch</li>
  <li><b><ruby>約束<rt>やくそく</rt></ruby></b> — vada</li>
  <li><b><ruby>訳<rt>わけ</rt></ruby></b> — sabab, mantiq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>わけです yangi xabar bermaydi — u <b>«ekan-da»</b> deydi.</li>
    <li>わけではない = <b>«degani emas»</b>; inkor わけ<b>dan keyin</b>.</li>
    <li>〜ないわけにはいかない = <b>«qilmasdan boʻlmaydi»</b>, yaʼni shart.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-81: 〜はずがない, 〜に違いない — ishonch darajalari",
        "category": "japanese",
        "order": 81,
        "summary": (
            "PJ-62 dagi はず endi inkorga va kuchaytirishga uzayadi: "
            "はずがない (boʻlishi mumkin emas), に違いない (shubhasiz "
            "shunday) va はずだったのに (shunday boʻlishi kerak edi). "
            "Butun ishonch shkalasi bitta jadvalda yopiladi."
        ),
        "stories": ["だれの てぶくろ"],
        "content": """
<h2>PJ-81: 〜はずがない, 〜に<ruby>違<rt>ちが</rt></ruby>いない — ishonch darajalari</h2>

<p>Yaponcha detektiv oʻqiyapsiz. Ikki kishi bahslashadi:</p>

<p><ruby>犯人<rt>はんにん</rt></ruby>は<ruby>田中<rt>たなか</rt></ruby>さん<b>に<ruby>違<rt>ちが</rt></ruby>いない</b>。<br>
いや、<ruby>田中<rt>たなか</rt></ruby>さんの<b>はずがない</b>。</p>

<p>Ikkalasi ham ishonch bilan gapiryapti — biri «aniq shu»,
ikkinchisi «aslo mumkin emas». Ikkalasi ham dalilga suyanadi.
Bu dars shu ikki qutbni beradi va PJ-62 dan boshlangan ishonch
shkalasini yopadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>はずがない</b> bilan ehtimolni butunlay rad etasiz</li>
    <li><b>に<ruby>違<rt>ちが</rt></ruby>いない</b> bilan qatʼiy ishonchni bildirasiz</li>
    <li><b>はずだったのに</b> bilan amalga oshmagan rejani aytasiz</li>
    <li>beshta qolipni ishonch darajasi boʻyicha tartibga qoʻyasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki qutb</span>
  <span class="pe-chip pe-chip--neg">はずがない</span>
  <span class="pe-op">↔</span>
  <span class="pe-chip pe-chip--v">に<ruby>違<rt>ちが</rt></ruby>いない</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">0% ↔ 95%</span>
</div>

<h3>1. はず — bir daqiqalik takrorlash</h3>

<p>PJ-62 da <b>はずです</b> ni koʻrgansiz: «shunday boʻlishi
kerak» — dalilga asoslangan kutish. Ulanishi
<ruby>形式名詞<rt>けいしきめいし</rt></ruby> qoidasiga boʻysunadi:
feʼl va い-sifat yalangʻoch, な-sifat <b>な</b> bilan, ot
<b>の</b> bilan.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>田中<rt>たなか</rt></ruby>さん</span>
  <span class="pj-joshi__p">の<small>OT + の</small></span>
  <span class="pj-joshi__v">はずです</span>
  <span class="pj-joshi__uz">Tanaka boʻlsa kerak. — ot はず oldida <b>の</b> ni oladi.</span>
</div>

<h3>2. はずがない — ehtimolni yopish</h3>

<p>はず ning egasi bor: がある yoki がない. <b>はずがない</b>
soʻzma-soʻz «bunday boʻlishining asosi yoʻq» degani, yaʼni
<em>mantiqan imkonsiz</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">ラノさんは<ruby>今<rt>いま</rt></ruby><ruby>京都<rt>きょうと</rt></ruby>にいます。ここにいる<span class="pe-hl pe-hl--neg">はずがありません</span>。</p>
  <p class="pe-ex__uz">Rano hozir Kiotoda. Bu yerda boʻlishi mumkin emas.</p>
  <p class="pe-ex__why">Dalil birinchi gapda turibdi. はずがない dalilsiz ishlatilmaydi — u his emas, <b>xulosa</b>.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Bu yerda oʻquvchilar eng koʻp adashadi.</b>
  <ruby>来<rt>こ</rt></ruby>ない<b>はずです</b> va
  <ruby>来<rt>く</rt></ruby>る<b>はずがない</b> — ikkalasi
  ham inkor tarafda, lekin kuchi butunlay boshqa.
  Birinchisi «kelmasa kerak» — kutish. Ikkinchisi
  «kelishi mumkin emas» — eshik yopiq. Tanlash uchun
  bitta savol bering: men shunchaki kutmayapmanmi, yoki
  ehtimolni <em>rad etyapmanmi</em>?</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>はずです</th><th>はずがない</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">feʼl</td>
      <td class="pj-end"><ruby>来<rt>く</rt></ruby>るはずです</td>
      <td class="pj-res"><ruby>来<rt>く</rt></ruby>るはずがない</td>
      <td class="pj-uz">kelsa kerak / kelishi mumkin emas</td></tr>
  <tr><td class="pj-stem">い-sifat</td>
      <td class="pj-end"><ruby>高<rt>たか</rt></ruby>いはずです</td>
      <td class="pj-res"><ruby>高<rt>たか</rt></ruby>いはずがない</td>
      <td class="pj-uz">qimmat boʻlsa kerak / qimmat boʻlishi mumkin emas</td></tr>
  <tr><td class="pj-stem">な-sifat</td>
      <td class="pj-end"><ruby>元気<rt>げんき</rt></ruby><b>な</b>はずです</td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby><b>な</b>はずがない</td>
      <td class="pj-uz">sogʻ boʻlsa kerak / sogʻ boʻlishi mumkin emas</td></tr>
  <tr><td class="pj-stem">ot</td>
      <td class="pj-end"><ruby>学生<rt>がくせい</rt></ruby><b>の</b>はずです</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby><b>の</b>はずがない</td>
      <td class="pj-uz">talaba boʻlsa kerak / talaba boʻlishi mumkin emas</td></tr>
</table></div>

<h3>3. はずがない va わけがない</h3>

<p>Kecha (PJ-80) siz <b>わけがない</b> ni koʻrdingiz.
Maʼnosi deyarli bir xil, va koʻp joyda ikkisi ham toʻgʻri.
Farq ohangda.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">はずがない — mantiq</p>
    <p><ruby>今日<rt>きょう</rt></ruby><ruby>来<rt>く</rt></ruby>るはずがない。</p>
    <p>Sovuq, tekshirilgan xulosa. Dalilni koʻrsatish mumkin.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">わけがない — his</p>
    <p><ruby>今日<rt>きょう</rt></ruby><ruby>来<rt>く</rt></ruby>るわけがない。</p>
    <p>Kuchliroq, soʻzlashuvga yaqin. «Qanaqasiga kelsin!»</p></div>
</div>

<h3>4. に<ruby>違<rt>ちが</rt></ruby>いない — ikkinchi qutb</h3>

<p><b><ruby>違<rt>ちが</rt></ruby>い</b> — «farq», <b>ない</b> —
«yoʻq». Yaʼni «bunda farq boʻlishi mumkin emas», «shubhasiz
shunday». Bu shkaladagi eng kuchli taxmin.</p>

<div class="pe-call pe-rule">
  <p><b>Ulanishi PJ-76 dagi みたい bilan bir xil — yalangʻoch.</b>
  Feʼl, い-sifat, な-sifat va ot — toʻrtalasi ham hech qanday
  qoʻshimchasiz ulanadi:
  <ruby>来<rt>く</rt></ruby>るに<ruby>違<rt>ちが</rt></ruby>いない ·
  <ruby>高<rt>たか</rt></ruby>いに<ruby>違<rt>ちが</rt></ruby>いない ·
  <ruby>元気<rt>げんき</rt></ruby>に<ruby>違<rt>ちが</rt></ruby>いない ·
  <ruby>学生<rt>がくせい</rt></ruby>に<ruby>違<rt>ちが</rt></ruby>いない.
  Shuning uchun はず ning な va の si bu yerga tushmaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>机<rt>つくえ</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>に<ruby>赤<rt>あか</rt></ruby>い<ruby>傘<rt>かさ</rt></ruby>がある。ムニラさんの<ruby>傘<rt>かさ</rt></ruby><span class="pe-hl pe-hl--v">に<ruby>違<rt>ちが</rt></ruby>いない</span>。</p>
  <p class="pe-ex__uz">Stol ustida qizil soyabon turibdi. Bu shubhasiz Muniraning soyaboni.</p>
  <p class="pe-ex__why">Otdan keyin <b>hech qanday qoʻshimcha yoʻq</b>. «ムニラさん<b>の</b>に<ruby>違<rt>ちが</rt></ruby>いない» boshqa maʼno beradi — «shubhasiz Muniraniki».</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu ikki qutb uchun tayyor soʻzlar bor, va
  ularni topib qoʻysangiz, tarjima oʻzi chiqadi.</b>
  に<ruby>違<rt>ちが</rt></ruby>いない — <b>«shubhasiz»</b>, «aniq», «albatta shunday».
  はずがない — <b>«boʻlishi mumkin emas»</b>, «aslo». Diqqat
  qiling: ikkala oʻzbekcha ibora ham <em>dalilga</em>
  suyanadi. «Shubhasiz Muniraniki» deb aytish uchun soyabonni
  koʻrgan boʻlishingiz kerak; «boʻlishi mumkin emas» deyish
  uchun esa nega mumkin emasligini bilishingiz kerak. Yapon
  tilida ham shunday — bu ikki qolip hissiyot emas,
  <b>xulosa</b> bildiradi. Agar dalil boʻlmasa, PJ-62 dagi
  かもしれません («boʻlishi mumkin») kerak boʻladi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Register.</b> に<ruby>違<rt>ちが</rt></ruby>いない —
  kitobiy va biroz dramatik. Kitobda, maqolada, detektivda
  koʻp uchraydi; kundalik suhbatda yaponlar koʻpincha
  <b>きっと〜でしょう</b> yoki <b>ぜったい〜</b> deb qoʻya
  qoladi. Yozganda ishlating, gaplashganda tanib oling.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>«Shubhasiz» va «boʻlishi mumkin emas» — ikkalasi ham
  oʻzbekchada <em>ikki soʻzli</em> iboralar, va bu tasodif
  emas.</b> Bir soʻzli «aniq» yoki «yoʻq» dan farqli oʻlaroq,
  ular gapiruvchining <em>fikrlash jarayonini</em> koʻrsatadi:
  men qaradim, oʻyladim, va shu xulosaga keldim. Yaponcha
  qoliplar ham ikki-uch boʻlakdan yigʻilgan —
  <ruby>違<rt>ちが</rt></ruby>い + ない, はず + が + ない.
  Shuning uchun ularni bitta soʻzdek emas, <b>qisqa jumladek</b>
  yodlang: «farqi yoʻq», «asosi yoʻq». Shunda ulanish qoidasi
  ham oʻzi esda qoladi — jumlaning oldiga butun gap tushadi,
  va はず ot oldida の ni oladi, chunki u haqiqiy ot.</p>
</div>

<h3>5. はずだったのに — amalga oshmagan reja</h3>

<p>はず ning oʻtgan zamon shakli alohida bir maʼno beradi:
<b>shunday boʻlishi kerak edi — lekin boʻlmadi</b>. Bu
oʻzbekcha «kerak edi» bilan aynan mos tushadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>三時<rt>さんじ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>く<span class="pe-hl pe-hl--neg">はずだったのに</span>、<ruby>電車<rt>でんしゃ</rt></ruby>が<ruby>遅<rt>おく</rt></ruby>れた。</p>
  <p class="pe-ex__uz">Soat uchda yetib borishim kerak edi, lekin poyezd kechikdi.</p>
  <p class="pe-ex__why">のに (PJ-54 dagi けど ga yaqin) afsusni qoʻshadi. はずだった yolgʻiz ham boʻladi, lekin のに bilan gap tirikroq chiqadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">イノムさんも<ruby>来<rt>く</rt></ruby>る<span class="pe-hl pe-hl--neg">はずでした</span>が、<ruby>病気<rt>びょうき</rt></ruby>になりました。</p>
  <p class="pe-ex__uz">Inom ham kelishi kerak edi, lekin kasal boʻlib qoldi.</p>
  <p class="pe-ex__why">Muloyim shakli — はず<b>でした</b>. Gap oxiridagi が PJ-54 dagi «lekin».</p>
</div>

<h3>6. Butun shkala bitta jadvalda</h3>

<p>PJ-62 dan PJ-81 gacha oltita qolip toʻplandi. Ularni
ishonch darajasi boʻyicha tartibga qoʻyamiz.</p>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">30%</span>
    <span class="pj-level__ja"><ruby>来<rt>く</rt></ruby>るかもしれません</span>
    <span class="pj-level__who">kelishi mumkin — dalil kam</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name">60%</span>
    <span class="pj-level__ja"><ruby>来<rt>く</rt></ruby>るでしょう</span>
    <span class="pj-level__who">kelsa kerak — umumiy taxmin</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">80%</span>
    <span class="pj-level__ja"><ruby>来<rt>く</rt></ruby>るはずです</span>
    <span class="pj-level__who">kelishi kerak — asosim bor</span>
  </div>
  <div class="pj-level__row pj-level__row--4">
    <span class="pj-level__name">95%</span>
    <span class="pj-level__ja"><ruby>来<rt>く</rt></ruby>るに<ruby>違<rt>ちが</rt></ruby>いない</span>
    <span class="pj-level__who">shubhasiz keladi — kitobiy</span>
  </div>
</div>

<p>Inkor tarafi ham xuddi shunday tartiblanadi:</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Daraja</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem"><ruby>来<rt>こ</rt></ruby>ないかもしれません</td>
      <td class="pj-uz">30%</td><td class="pj-res">kelmasligi mumkin</td></tr>
  <tr><td class="pj-stem"><ruby>来<rt>こ</rt></ruby>ないでしょう</td>
      <td class="pj-uz">60%</td><td class="pj-res">kelmasa kerak</td></tr>
  <tr><td class="pj-stem"><ruby>来<rt>こ</rt></ruby>ないはずです</td>
      <td class="pj-uz">80%</td><td class="pj-res">kelmasligi kerak</td></tr>
  <tr><td class="pj-stem"><ruby>来<rt>く</rt></ruby>るはずがない</td>
      <td class="pj-uz">0%</td><td class="pj-res">kelishi mumkin emas</td></tr>
  <tr><td class="pj-stem"><ruby>来<rt>く</rt></ruby>るわけがない</td>
      <td class="pj-uz">0%, kuchliroq</td><td class="pj-res">qanaqasiga kelsin</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu jadvalning foizlari haqiqiy raqam emas — ular
  tartibni koʻrsatadi.</b> Yapon tilida taxminni
  <em>darajalab</em> aytish odob hisoblanadi: kerak
  boʻlgandan kuchliroq gapirish qoʻpol, kerak boʻlgandan
  kuchsizroq gapirish esa masʼuliyatsiz koʻrinadi.
  Oʻzbek tilida ham shunday — «kelsa kerak», «kelishi
  kerak», «shubhasiz keladi» bir xil narsa emas, va
  birini ikkinchisining oʻrniga qoʻysangiz, odam sizni
  boshqacha tushunadi. Yaponcha yozganda shu shkalani
  yoningizda tuting va har safar soʻrang: menda qancha
  dalil bor?</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">違</span>
    <span class="pj-kanji__uz">farq qilmoq, notoʻgʻri boʻlmoq</span>
    <span class="pj-kanji__on">オン: イ</span>
    <span class="pj-kanji__kun">KUN: ちが(う)</span>
    <span class="pj-kanji__note">違う (ちがう) — farq qilmoq · 間違い (まちがい) — xato · 違反 (いはん) — qoidabuzarlik</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">犯</span>
    <span class="pj-kanji__uz">jinoyat qilmoq</span>
    <span class="pj-kanji__on">オン: ハン</span>
    <span class="pj-kanji__kun">KUN: おか(す)</span>
    <span class="pj-kanji__note">犯人 (はんにん) — jinoyatchi · 犯罪 (はんざい) — jinoyat</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby><b>の</b>に<ruby>違<rt>ちが</rt></ruby>いない</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby>に<ruby>違<rt>ちが</rt></ruby>いない — に<ruby>違<rt>ちが</rt></ruby>いない otga yalangʻoch ulanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>元気<rt>げんき</rt></ruby><b>な</b>に<ruby>違<rt>ちが</rt></ruby>いない</p>
  <p class="pe-fix__good">✓ <ruby>元気<rt>げんき</rt></ruby>に<ruby>違<rt>ちが</rt></ruby>いない — な-sifat ham yalangʻoch, xuddi みたい oldidagidek.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>はずがありません</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>の</b>はずがありません — はず esa ot oldida の ni talab qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>来<rt>く</rt></ruby>るはずがない<br><small>(«kelmasa kerak» demoqchi boʻlsangiz)</small></p>
  <p class="pe-fix__good">✓ <ruby>来<rt>こ</rt></ruby>ないはずです — はずがない ehtimolni butunlay yopadi, oddiy kutish emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Doʻstga: <ruby>絶対<rt>ぜったい</rt></ruby><ruby>来<rt>く</rt></ruby>るに<ruby>違<rt>ちが</rt></ruby>いないよ</p>
  <p class="pe-fix__good">✓ きっと<ruby>来<rt>く</rt></ruby>るよ — に<ruby>違<rt>ちが</rt></ruby>いない kitobiy; suhbatda きっと tabiiyroq.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>学生<rt>がくせい</rt></ruby> ni はずがない va に<ruby>違<rt>ちが</rt></ruby>いない bilan bogʻlang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>学生<rt>がくせい</rt></ruby>のはずがない</b> (はず — の bilan) va <b><ruby>学生<rt>がくせい</rt></ruby>に<ruby>違<rt>ちが</rt></ruby>いない</b> (に<ruby>違<rt>ちが</rt></ruby>いない — yalangʻoch).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Kelmasa kerak» va «kelishi mumkin emas» — qaysi qolip qaysi biri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>«Kelmasa kerak» — <b><ruby>来<rt>こ</rt></ruby>ないはずです</b>. «Kelishi mumkin emas» — <b><ruby>来<rt>く</rt></ruby>るはずがありません</b>. Birinchisi kutish, ikkinchisi rad etish.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Doʻstingiz bilan gaplashayotganda «albatta keladi» ni qanday aytasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>きっと<ruby>来<rt>く</rt></ruby>るよ</b>. に<ruby>違<rt>ちが</rt></ruby>いない kitobiy — uni yozma matnda ishlating.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>三時<rt>さんじ</rt></ruby>に<ruby>着<rt>つ</rt></ruby>くはずだったのに — bu gap nima haqida?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Amalga oshmagan reja.</b> «Uchda yetib borishim kerak edi» — lekin boʻlmadi. のに afsusni qoʻshadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. はずがない va わけがない — farqi nimada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Maʼnosi deyarli bir xil. <b>はずがない</b> — sovuq mantiq, dalilni koʻrsatish mumkin; <b>わけがない</b> — kuchliroq, soʻzlashuvga yaqin.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜はずがない</b> — … boʻlishi mumkin emas</li>
  <li><b>〜に<ruby>違<rt>ちが</rt></ruby>いない</b> — shubhasiz …</li>
  <li><b>〜はずだった</b> — … boʻlishi kerak edi</li>
  <li><b>〜のに</b> — …ga qaramay, afsuski</li>
  <li><b>きっと</b> — albatta, aniq (suhbatda)</li>
  <li><b><ruby>絶対<rt>ぜったい</rt></ruby></b> — mutlaqo, aslo</li>
  <li><b><ruby>犯人<rt>はんにん</rt></ruby></b> — jinoyatchi</li>
  <li><b><ruby>間違<rt>まちが</rt></ruby>い</b> — xato</li>
  <li><b><ruby>傘<rt>かさ</rt></ruby></b> — soyabon</li>
  <li><b><ruby>遅<rt>おく</rt></ruby>れる</b> — kechikmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>はず ot oldida <b>の</b>, に<ruby>違<rt>ちが</rt></ruby>いない esa <b>yalangʻoch</b>.</li>
    <li><ruby>来<rt>こ</rt></ruby>ないはずです (kutish) ≠ <ruby>来<rt>く</rt></ruby>るはずがない (rad etish).</li>
    <li>に<ruby>違<rt>ちが</rt></ruby>いない — <b>yozma</b>; suhbatda きっと〜でしょう.</li>
  </ul>
</div>
""",
    },
]
