# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-73, PJ-74, PJ-75: taxminning toʻrt ovozi.

Bu batch bitta savolga javob beradi: «Men buni qayerdan bilaman?»
    降りそうです   ← koʻrib turibman (PJ-73, 様態)
    降るそうです   ← eshitdim, manba aniq (PJ-74, 伝聞)
    降るようです   ← dalilga qarab oʻzim xulosa qildim (PJ-75)
    降るらしいです ← eshitdim, manba noaniq (PJ-75)

⚠️ Uchta darsning butun qiyinchiligi ULANISHDA, maʼnoda emas:
    様態 そう  → ます-oʻzak · い-sifat (い tushadi) · な-sifat oʻzagi
    伝聞 そう  → oddiy shakl, だ SAQLANADI (学生だそうです)
    ようです   → oddiy shakl, lekin な-sifat な, ot の
    らしい     → oddiy shakl, na だ, na な, na の — yalangʻoch ulanadi
Shuning uchun har uch darsda ulanish jadvali birinchi oʻrinda turadi,
va PJ-75 toʻrttasini bitta jadvalda yopadi (PJ-52 shartlarni yopgani kabi).

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_73_75.py --author=prime
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
        "title": "PJ-73: 〜そうです 1: koʻrinish",
        "category": "japanese",
        "order": 73,
        "summary": (
            "Koʻzingiz bilan koʻrgan narsadan xulosa chiqarish. "
            "Oʻzbekcha «yogʻay deb turibdi», «yiqilay dedi» — aynan "
            "shu ohang, va u ます-oʻzakka ulanadi."
        ),
        "stories": ["あめが ふりそうな そら"],
        "content": """
<h2>PJ-73: 〜そうです 1: koʻrinish</h2>

<p>Osmonga qaraysiz. <ruby>雲<rt>くも</rt></ruby> qop-qora, shamol
turdi, hovlida kir yoyilgan. Yomgʻir hali <b>yogʻmadi</b> — lekin
siz uyga kirib ayangizga nima deysiz? «Yomgʻir yogʻay deb
turibdi, kirni olib kiraylik».</p>

<p>Mana shu «yogʻay deb turibdi» yapon tilida bitta
qoʻshimcha bilan chiqadi. Va u kursning eng koʻp
ishlatiladigan qoliplaridan biri, chunki inson kuniga oʻn marta
koʻrgan narsasidan xulosa chiqaradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Feʼl, い-sifat va な-sifatga 〜そう ni toʻgʻri ulaysiz</li>
    <li>いい → よさそう, ない → なさそう istisnolarini yodlaysiz</li>
    <li>そうな + ot va そうに + feʼl shakllarini yasaysiz</li>
    <li>Qachon 〜そう <em>ishlatilmasligini</em> bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Koʻrinish</span>
  <span class="pe-chip pe-chip--v">ます-oʻzak</span>
  <span class="pe-op">/</span>
  <span class="pe-chip pe-chip--adv">い-sifat <small>(い tushadi)</small></span>
  <span class="pe-op">/</span>
  <span class="pe-chip pe-chip--o">な-sifat oʻzagi</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">そうです</span>
</div>

<p>Yaponcha grammatika kitoblarida bu qolip
<ruby>様態<rt>ようたい</rt></ruby>の「そうだ」 deb ataladi —
«holat そう»i. Nomini yodlash shart emas, lekin bir narsani
yodlash shart: <b>ertaga keladigan darsda ham
〜そうです bor, lekin u butunlay boshqa narsani
bildiradi</b>. Ikkalasini ajratadigan yagona belgi — ulanish.
Shuning uchun bugun ulanishni <em>qoʻldan chiqarmasdan</em>
oʻrganamiz.</p>

<h3>1. Uchta ulanish</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Soʻz</th><th>Oʻzak</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">feʼl</td><td><ruby>降<rt>ふ</rt></ruby>る</td>
      <td class="pj-end"><ruby>降<rt>ふ</rt></ruby>り</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>りそうです</td>
      <td class="pj-uz">yogʻay deb turibdi</td></tr>
  <tr><td class="pj-stem">feʼl</td><td><ruby>落<rt>お</rt></ruby>ちる</td>
      <td class="pj-end"><ruby>落<rt>お</rt></ruby>ち</td>
      <td class="pj-res"><ruby>落<rt>お</rt></ruby>ちそうです</td>
      <td class="pj-uz">yiqilay dedi</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td>おいしい</td>
      <td class="pj-end">おいし</td>
      <td class="pj-res">おいしそうです</td>
      <td class="pj-uz">mazali koʻrinadi</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td><ruby>眠<rt>ねむ</rt></ruby>い</td>
      <td class="pj-end"><ruby>眠<rt>ねむ</rt></ruby></td>
      <td class="pj-res"><ruby>眠<rt>ねむ</rt></ruby>そうです</td>
      <td class="pj-uz">uyqusi kelganga oʻxshaydi</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td><ruby>元気<rt>げんき</rt></ruby>だ</td>
      <td class="pj-end"><ruby>元気<rt>げんき</rt></ruby></td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby>そうです</td>
      <td class="pj-uz">tetik koʻrinadi</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td><ruby>大変<rt>たいへん</rt></ruby>だ</td>
      <td class="pj-end"><ruby>大変<rt>たいへん</rt></ruby></td>
      <td class="pj-res"><ruby>大変<rt>たいへん</rt></ruby>そうです</td>
      <td class="pj-uz">qiyinga oʻxshaydi</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Uchta ulanishning ichida bittagina umumiy narsa bor:
  oxiri yoʻqoladi.</b> Feʼldan ます-oʻzak qoladi
  (<ruby>降<rt>ふ</rt></ruby>ります → <ruby>降<rt>ふ</rt></ruby>り),
  い-sifatdan い tushadi, な-sifatdan だ tushadi. Yaʼni
  〜そう <em>hech qachon</em> lugʻat shakliga ulanmaydi. Buni
  yodlab qoʻysangiz, keyingi darsdagi そう bilan umuman
  adashmaysiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>空<rt>そら</rt></ruby>が<ruby>暗<rt>くら</rt></ruby>いです。<span class="pe-hl pe-hl--v"><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りそうです</span>。</p>
  <p class="pe-ex__uz">Osmon qorongʻi. Yomgʻir yogʻay deb turibdi.</p>
  <p class="pe-ex__why">Men bulutni koʻrib turibman — xulosa oʻzimning koʻzimdan chiqdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">パリさんの<ruby>弁当<rt>べんとう</rt></ruby>は<span class="pe-hl pe-hl--adv">おいしそうです</span>ね。</p>
  <p class="pe-ex__uz">Parining ovqati mazali koʻrinadi-a.</p>
  <p class="pe-ex__why">Hali tatib koʻrmadim. Faqat koʻrinishiga qarab aytyapman — 〜そう ning eng tipik ishi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">イノムさんは<ruby>今日<rt>きょう</rt></ruby><span class="pe-hl pe-hl--o"><ruby>元気<rt>げんき</rt></ruby>そうです</span>。</p>
  <p class="pe-ex__uz">Inom bugun tetik koʻrinadi.</p>
  <p class="pe-ex__why"><ruby>元気<rt>げんき</rt></ruby>だ — な-sifat, demak だ tushadi. «<ruby>元気<rt>げんき</rt></ruby>だそうです» boshqa maʼno beradi (PJ-74).</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu qolipning ikkita tayyor tarjimasi
  bor, va ular feʼl bilan sifatda boshqa-boshqa.</b>
  Feʼlga qoʻshilsa — «<em>-ay deb turibdi</em>»,
  «<em>-ay dedi</em>»:
  <ruby>降<rt>ふ</rt></ruby>りそうです — yogʻay deb turibdi;
  <ruby>落<rt>お</rt></ruby>ちそうです — yiqilay dedi;
  <ruby>泣<rt>な</rt></ruby>きそうです — yigʻlay dedi. Sifatga
  qoʻshilsa — «<em>-ga oʻxshaydi</em>», «<em>koʻrinadi</em>»:
  おいしそうです — mazali koʻrinadi. Bu ikki tarjimani
  esda tutsangiz, gapni yaponchadan oʻzbekchaga
  <b>oʻgirishda ham</b> adashmaysiz — koʻp oʻquvchi
  «<ruby>落<rt>お</rt></ruby>ちそうです» ni «yiqildi shekilli»
  deb tarjima qiladi, holbuki hech kim hech qayerdan
  yiqilmagan.</p>
</div>

<h3>2. Feʼldagi ikki maʼno: «hozir boʻladi» va «shunday koʻrinadi»</h3>

<p>Feʼl bilan 〜そう ikkita ohangda chiqadi, va ularni vaziyat
ajratadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">Hozir boʻladi</p>
    <p>コップが<ruby>落<rt>お</rt></ruby>ちそうです。</p>
    <p>Stakan yiqilay dedi — <b>bir zumdan keyin</b> yiqiladi. Shoshiling!</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">Shunday koʻrinadi</p>
    <p>この<ruby>本<rt>ほん</rt></ruby>は<ruby>役<rt>やく</rt></ruby>に<ruby>立<rt>た</rt></ruby>ちそうです。</p>
    <p>Bu kitob foydali boʻladiganga oʻxshaydi — <b>bahoyim</b>, vaqt yoʻq bunda.</p></div>
</div>

<p>Bu ikki maʼnoni <em>alohida</em> yodlash kerak emas: ikkalasi
ham bir xil fikrdan chiqadi — «koʻrinib turgan narsa
menga shunday deydi». Faqat feʼl bir lahzalik ish
boʻlsa (yiqilmoq, sinmoq, yigʻlamoq), tabiiy ravishda
«hozir boʻladi» eshitiladi; feʼl davomli boʻlsa
(foyda bermoq, yetmoq), «shunday koʻrinadi» eshitiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">ムニラさんは<span class="pe-hl pe-hl--v"><ruby>泣<rt>な</rt></ruby>きそうな</span><ruby>顔<rt>かお</rt></ruby>をしていました。</p>
  <p class="pe-ex__uz">Muniraning yuzi yigʻlay degandek edi.</p>
  <p class="pe-ex__why">Otdan oldin <b>そうな</b> — keyingi boʻlimda shu haqida.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bir narsani oʻzbekcha mantiq bilan tekshirib
  koʻring.</b> «Yiqilay dedi» deganda oʻzbek tili ham
  feʼlning <em>oxirini</em> oʻzgartiradi: «yiqil<b>ay</b>»,
  «yogʻ<b>ay</b>» — lugʻat shakli «yiqilmoq» joyida
  turmaydi. Yaponcha ham xuddi shunday qiladi:
  <ruby>落<rt>お</rt></ruby>ち<b>る</b> emas,
  <ruby>落<rt>お</rt></ruby>ち. Yaʼni ikkala tilda ham bu
  qolip feʼlning oxirini <em>yeydi</em>. Buni eslab qolsangiz,
  ertangi darsdagi そう bilan adashmaysiz — u yerda
  feʼl butun qoladi, chunki u gapni emas, <b>xabarni</b>
  uzatadi.</p>
</div>

<h3>3. Ikkita istisno: いい va ない</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Kutilgan shakl</th><th>Toʻgʻri shakl</th></tr>
  <tr><td class="pj-stem">いい</td><td class="pj-uz">✗ いそう</td>
      <td class="pj-res"><b>よさそう</b></td></tr>
  <tr><td class="pj-stem">ない</td><td class="pj-uz">✗ なそう</td>
      <td class="pj-res"><b>なさそう</b></td></tr>
</table></div>

<p>Ikkalasi ham <b>さ</b> qoʻshib oladi. Sababi shundaki,
«い» dan keyin bitta bogʻin qolsa soʻz eshitilmas
boʻlib qoladi — <ruby>日本語<rt>にほんご</rt></ruby> bunga yoʻl
qoʻymaydi. Shuning uchun <ruby>元気<rt>げんき</rt></ruby>じゃ
なさそうです («tetik emasga oʻxshaydi») va
<ruby>都合<rt>つごう</rt></ruby>がよさそうです («qulay
koʻrinadi») — bu ikki shakl juda koʻp uchraydi, yodlab
qoʻying.</p>

<div class="pe-call pe-tip">
  <p><b>Bu istisno tanish boʻlishi kerak.</b> よさそう ning
  よ si — <ruby>良<rt>よ</rt></ruby>い ning oʻzagi, siz uni
  よく («yaxshi», hol shakli) va よかった («yaxshi
  boʻldi») da allaqachon koʻrgansiz. Yaʼni いい dan yasalgan
  <em>hech qanday</em> shakl «い» bilan boshlanmaydi. Bitta
  qoida — uchta shakl.</p>
</div>

<h3>4. Inkor: ikki yoʻl bor</h3>

<p>«Koʻrinmaydi» degan maʼno ikki xil yasaladi, va qaysi biri
ishlatilishi <b>soʻz turiga</b> bogʻliq.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Yoʻl</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-end">〜そうにない · 〜そうもない</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>りそうにありません</td>
      <td class="pj-uz">yogʻadiganga oʻxshamaydi</td></tr>
  <tr><td class="pj-stem">sifat</td><td class="pj-end">inkorni sifatning oʻziga</td>
      <td class="pj-res">おいしくなさそうです</td>
      <td class="pj-uz">mazali koʻrinmaydi</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end">inkorni sifatning oʻziga</td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby>じゃなさそうです</td>
      <td class="pj-uz">tetik koʻrinmaydi</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Feʼlda «<ruby>降<rt>ふ</rt></ruby>りそうじゃありません»
  demang.</b> Grammatik jihatdan tushunarli, lekin yaponlar
  bunday demaydi. Feʼlda inkor <b>そう</b> dan <em>keyin</em>
  keladi: <ruby>降<rt>ふ</rt></ruby>りそう<b>にありません</b>
  yoki <ruby>降<rt>ふ</rt></ruby>りそう<b>もありません</b>.
  Sifatda esa aksincha — inkor <b>そう</b> dan
  <em>oldin</em> keladi: おいし<b>くなさ</b>そうです.</p>
</div>

<h3>5. Otga va feʼlga bogʻlash: そうな va そうに</h3>

<p>〜そう ning oʻzi な-sifat kabi tuslanadi. Yaʼni:</p>

<div class="pj-joshi">
  <span class="pj-joshi__n">おいしそう</span>
  <span class="pj-joshi__p">な<small>+ OT</small></span>
  <span class="pj-joshi__n">ケーキ</span>
  <span class="pj-joshi__uz">mazali koʻrinadigan tort</span>
</div>

<div class="pj-joshi">
  <span class="pj-joshi__n">おいしそう</span>
  <span class="pj-joshi__p">に<small>+ FEʼL</small></span>
  <span class="pj-joshi__v"><ruby>食<rt>た</rt></ruby>べます</span>
  <span class="pj-joshi__uz">mazza qilib yeydi</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">イムロンさんは<ruby>幸<rt>しあわ</rt></ruby>せ<span class="pe-hl pe-hl--adv">そうに</span><ruby>笑<rt>わら</rt></ruby>いました。</p>
  <p class="pe-ex__uz">Imron baxtlidek kulib qoʻydi.</p>
  <p class="pe-ex__why">そうに + feʼl — «shunday koʻrinishda qildi». Bu shakl hikoyalarda juda koʻp uchraydi.</p>
</div>

<p>Bu ikki shaklni <em>alohida</em> yodlash kerak emas: な-sifat
qanday tuslansa, 〜そう ham shunday tuslanadi.
<ruby>静<rt>しず</rt></ruby>か<b>な</b><ruby>部屋<rt>へや</rt></ruby>,
<ruby>静<rt>しず</rt></ruby>か<b>に</b><ruby>話<rt>はな</rt></ruby>す —
xuddi shu ikki uyacha.</p>

<h3>6. Qachon 〜そう ishlatilmaydi</h3>

<p>Bu boʻlim qoidadan ham muhim, chunki oʻquvchilar
eng koʻp shu yerda xato qiladi.</p>

<div class="pe-call pe-rule">
  <p><b>Birinchi: otga ulanmaydi.</b>
  ✗ <ruby>学生<rt>がくせい</rt></ruby>そうです — bunday shakl
  yoʻq. «Talabaga oʻxshaydi» degan maʼno boshqa qolip
  bilan chiqadi va uni PJ-75 da koʻrasiz.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Ikkinchi: koʻz bilan <em>toʻgʻridan-toʻgʻri</em>
  koʻrinadigan sifatga ulanmaydi.</b> Gul chiroyli ekanini
  siz koʻrib turibsiz — bu xulosa emas, bu fakt. Shuning
  uchun «この<ruby>花<rt>はな</rt></ruby>はきれいそうです»
  gʻalati eshitiladi; toʻgʻrisi — きれいです. Xuddi shunday
  <ruby>赤<rt>あか</rt></ruby>い,
  <ruby>大<rt>おお</rt></ruby>きい,
  <ruby>長<rt>なが</rt></ruby>い kabi sifatlar ham 〜そう
  olmaydi.</p>
</div>

<p>Qoidani bitta savol bilan tekshirish mumkin:
<b>men buni koʻryapmanmi, yoki koʻrganimdan xulosa
chiqaryapmanmi?</b> Tortning rangini koʻryapman — demak
きれいです. Tortning <em>taʼmi</em>ni esa koʻrmayapman,
faqat taxmin qilyapman — demak おいしそうです. Yaʼni
〜そう doim <em>koʻrinmaydigan</em> narsa haqida:
taʼm, kayfiyat, ogʻirlik, kelajak.</p>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu chegara yoʻq, shuning uchun uni
  ataylab yodlash kerak.</b> Oʻzbek tilida «bu gul chiroyli
  koʻrinadi» deyish mumkin — hech kimni ajablantirmaydi.
  Yaponchada esa «koʻrinadi» soʻzi <em>faqat</em>
  koʻrilmagan narsaga qoʻyiladi. Shuning uchun tarjima
  qilganda «koʻrinadi» soʻziga emas, <b>vaziyatga</b>
  qarang: koʻz bilan hal boʻladigan narsa boʻlsa, 〜そう ni
  olib tashlang.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">降</span>
    <span class="pj-kanji__uz">yogʻmoq, tushmoq</span>
    <span class="pj-kanji__on">オン: コウ</span>
    <span class="pj-kanji__kun">KUN: ふ(る) · お(りる)</span>
    <span class="pj-kanji__note">雨が降る (あめがふる) — yomgʻir yogʻadi · 降りる (おりる) — tushmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">眠</span>
    <span class="pj-kanji__uz">uxlamoq, uyqu</span>
    <span class="pj-kanji__on">オン: ミン</span>
    <span class="pj-kanji__kun">KUN: ねむ(い) · ねむ(る)</span>
    <span class="pj-kanji__note">眠い (ねむい) — uyqusi kelgan · 眠る (ねむる) — uxlamoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ このケーキはおいしいそうです<br><small>(koʻrinishi haqida aytmoqchi boʻlsangiz)</small></p>
  <p class="pe-fix__good">✓ このケーキはおいし<b>そう</b>です — い-sifatdan <b>い</b> tushadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るそうです<br><small>(bulutni koʻrib turib)</small></p>
  <p class="pe-fix__good">✓ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<b>そう</b>です — koʻrinish <b>ます-oʻzakka</b> ulanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>都合<rt>つごう</rt></ruby>がいそうです</p>
  <p class="pe-fix__good">✓ <ruby>都合<rt>つごう</rt></ruby>が<b>よさ</b>そうです — いい istisno, さ qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ おいしそうケーキ</p>
  <p class="pe-fix__good">✓ おいしそう<b>な</b>ケーキ — 〜そう な-sifat kabi tuslanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>そうです</p>
  <p class="pe-fix__good">✓ Bunday shakl yoʻq — 〜そう <b>otga ulanmaydi</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>泣<rt>な</rt></ruby>く ni 〜そうです qolipiga qoʻying.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>泣<rt>な</rt></ruby>きそうです</b> — ます-oʻzagi <ruby>泣<rt>な</rt></ruby>き. «Yigʻlay dedi» degan ohang.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>元気<rt>げんき</rt></ruby>だ ni 〜そうです qolipiga qoʻying.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>元気<rt>げんき</rt></ruby>そうです</b> — な-sifatdan <b>だ</b> tushadi. <ruby>元気<rt>げんき</rt></ruby>だそうです boshqa maʼno (PJ-74).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Yomgʻir yogʻadiganga oʻxshamaydi» — qaysi shakl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>降<rt>ふ</rt></ruby>りそうにありません</b> (yoki <ruby>降<rt>ふ</rt></ruby>りそうもありません). Feʼlda inkor <b>そう</b> dan keyin keladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «この<ruby>花<rt>はな</rt></ruby>はきれいそうです» — nima xato?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Gulning chiroyliligini siz <b>koʻrib turibsiz</b> — bu xulosa emas, fakt. Toʻgʻrisi: きれいです.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Mazza qilib yedi» — そうな yoki そうに?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>おいしそうに<ruby>食<rt>た</rt></ruby>べました</b> — feʼldan oldin <b>そうに</b>. Otdan oldin esa そうな.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜そうです</b> — koʻrinadi, …ay deb turibdi</li>
  <li><b>よさそう</b> — yaxshi koʻrinadi (いい ning istisnosi)</li>
  <li><b>なさそう</b> — yoʻqqa oʻxshaydi (ない ning istisnosi)</li>
  <li><b>〜そうにない</b> — …adiganga oʻxshamaydi</li>
  <li><b>〜そうな + ot</b> — …ga oʻxshaydigan</li>
  <li><b>〜そうに + feʼl</b> — …dek qildi</li>
  <li><b><ruby>降<rt>ふ</rt></ruby>る</b> — yogʻmoq</li>
  <li><b><ruby>落<rt>お</rt></ruby>ちる</b> — yiqilmoq, tushmoq</li>
  <li><b><ruby>眠<rt>ねむ</rt></ruby>い</b> — uyqusi kelgan</li>
  <li><b><ruby>泣<rt>な</rt></ruby>く</b> — yigʻlamoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Koʻrinish そう — <b>ます-oʻzak</b>, い tushadi, だ tushadi.</li>
    <li>いい → <b>よさそう</b>, ない → <b>なさそう</b>.</li>
    <li>Koʻz bilan koʻrinadigan narsaga (きれい, <ruby>赤<rt>あか</rt></ruby>い) そう <b>qoʻyilmaydi</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-74: 〜そうです 2: eshitilgan xabar",
        "category": "japanese",
        "order": 74,
        "summary": (
            "Bir xil qoʻshimcha, butunlay boshqa maʼno. Oʻzbekcha "
            "«-arkan», «aytishlaricha» — va uni koʻrinish そう dan "
            "faqat ULANISH ajratadi."
        ),
        "stories": ["せんぱいの はなし"],
        "content": """
<h2>PJ-74: 〜そうです 2: eshitilgan xabar</h2>

<p>Tanaffusda sinfdoshingiz yugurib keladi: «Ertaga imtihon
boʻlarkan!» Siz oʻzingiz eʼlonni oʻqimadingiz, direktorni
koʻrmadingiz — <b>faqat eshitdingiz</b>. Va oʻzbek tili buni
bitta qoʻshimcha bilan aytadi: «boʻl<em>arkan</em>».</p>

<p>Yapon tili ham bitta qoʻshimcha bilan aytadi. Yomon xabar
shundaki, bu qoʻshimcha <b>kechagi darsdagi bilan bir xil
yoziladi</b>: 〜そうです. Yaxshi xabar shundaki, ikkalasini
ajratish uchun bitta narsaga qarash yetadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Oddiy shaklga 〜そうです ni ulaysiz</li>
    <li>Nega <ruby>学生<rt>がくせい</rt></ruby>だそうです da <b>だ</b> qolishini bilasiz</li>
    <li>Xabar manbasini koʻrsatadigan 〜によると ni ishlatasiz</li>
    <li>Ikki そう ni bir jadvalda ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Eshitilgan xabar</span>
  <span class="pe-chip pe-chip--s">oddiy shakl <small>(<ruby>普通体<rt>ふつうたい</rt></ruby>)</small></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">そうです</span>
</div>

<p>Bu qolipning yaponcha nomi —
<ruby>伝聞<rt>でんぶん</rt></ruby>の「そうだ」, yaʼni «uzatilgan
xabar そう»i. Nomidan koʻra muhimi: <b>bu yerda soʻzning
oxiri hech qachon kesilmaydi</b>. Kechagi darsda oxiri
kesilgan edi; bugun butun soʻz oʻz shaklida turadi va
ustiga そうです qoʻyiladi. Mana shu — butun farq.</p>

<h3>1. Ulanish jadvali</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Oddiy shakl</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-end"><ruby>降<rt>ふ</rt></ruby>る</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>るそうです</td>
      <td class="pj-uz">yogʻarkan</td></tr>
  <tr><td class="pj-stem">feʼl, oʻtgan</td><td class="pj-end"><ruby>降<rt>ふ</rt></ruby>った</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>ったそうです</td>
      <td class="pj-uz">yogʻgan ekan</td></tr>
  <tr><td class="pj-stem">feʼl, inkor</td><td class="pj-end"><ruby>降<rt>ふ</rt></ruby>らない</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>らないそうです</td>
      <td class="pj-uz">yogʻmasakan</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">おいしい</td>
      <td class="pj-res">おいしいそうです</td>
      <td class="pj-uz">mazali ekan</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end"><ruby>元気<rt>げんき</rt></ruby><b>だ</b></td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby><b>だ</b>そうです</td>
      <td class="pj-uz">tetik ekan</td></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end"><ruby>学生<rt>がくせい</rt></ruby><b>だ</b></td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby><b>だ</b>そうです</td>
      <td class="pj-uz">talaba ekan</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Oxirgi ikki qatorga alohida qarang.</b> Kechagi
  darsda な-sifat va otdan <b>だ</b> tushib qolgan edi
  (<ruby>元気<rt>げんき</rt></ruby>そうです). Bugun esa <b>だ</b>
  joyida qoladi (<ruby>元気<rt>げんき</rt></ruby>だそうです).
  Ikki qolipni ajratadigan eng aniq belgi — mana shu bitta
  bogʻin. Va u ot bilan ayniqsa foydali: 〜そう otga
  ulanmasdi, lekin <ruby>学生<rt>がくせい</rt></ruby>だそうです
  butunlay normal gap.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>天気予報<rt>てんきよほう</rt></ruby>によると、<ruby>明日<rt>あした</rt></ruby><span class="pe-hl pe-hl--v"><ruby>雪<rt>ゆき</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るそうです</span>。</p>
  <p class="pe-ex__uz">Ob-havo maʼlumotiga koʻra, ertaga qor yogʻarkan.</p>
  <p class="pe-ex__why">Men osmonga qaramadim — maʼlumotni <b>eshitdim</b>. Shuning uchun <ruby>降<rt>ふ</rt></ruby>る, lugʻat shakli.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">パリさんのお<ruby>兄<rt>にい</rt></ruby>さんは<span class="pe-hl pe-hl--o"><ruby>医者<rt>いしゃ</rt></ruby>だそうです</span>。</p>
  <p class="pe-ex__uz">Parining akasi shifokor ekan.</p>
  <p class="pe-ex__why">Ot + <b>だ</b> + そうです. «<ruby>医者<rt>いしゃ</rt></ruby>そうです» degan shakl yoʻq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">ムニラさんは<ruby>去年<rt>きょねん</rt></ruby><ruby>日本<rt>にほん</rt></ruby>へ<span class="pe-hl pe-hl--v"><ruby>行<rt>い</rt></ruby>ったそうです</span>。</p>
  <p class="pe-ex__uz">Munira oʻtgan yili Yaponiyaga borgan ekan.</p>
  <p class="pe-ex__why">Oʻtgan zamon <b>gapning oʻzida</b> turadi — <ruby>行<rt>い</rt></ruby>った. そうです oʻzgarmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu qolipning tayyor muqobili bor, va
  u aynan shu ishni qiladi: «-ekan».</b>
  <ruby>降<rt>ふ</rt></ruby>るそうです — «yogʻarkan»;
  <ruby>医者<rt>いしゃ</rt></ruby>だそうです — «shifokor ekan»;
  <ruby>行<rt>い</rt></ruby>ったそうです — «borgan ekan».
  Boshqa hech qanday qolip bilan bu darajada aniq
  tushmaydi. Faqat bitta ogohlantirish bor: oʻzbekcha
  «-ekan» baʼzan <em>hayratni</em> ham bildiradi
  («voy, sovuq ekan-ku!»). Yaponchada bu ikki ish
  boʻlinadi: eshitilgan xabar — そうです, oʻzi koʻrib
  hayron boʻlish — oddiy gap yoki 〜んです. Shuning uchun
  «-ekan» ni koʻrsangiz, avval oʻzingizdan
  <b>«men buni kimdandir eshitdimmi?»</b> deb soʻrang.</p>
</div>

<h3>2. Manbani koʻrsatish</h3>

<p>Eshitilgan xabar aytilganda, koʻpincha uning
<b>qayerdan</b> kelgani ham aytiladi. Uchta tayyor qolip bor:</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pj-stem">〜によると</td><td class="pj-uz">…ga koʻra (rasmiy manba)</td>
      <td class="pj-res"><ruby>新聞<rt>しんぶん</rt></ruby>によると</td></tr>
  <tr><td class="pj-stem">〜の<ruby>話<rt>はなし</rt></ruby>では</td><td class="pj-uz">…ning aytishicha</td>
      <td class="pj-res">パリさんの<ruby>話<rt>はなし</rt></ruby>では</td></tr>
  <tr><td class="pj-stem">〜から<ruby>聞<rt>き</rt></ruby>きました</td><td class="pj-uz">…dan eshitdim</td>
      <td class="pj-res"><ruby>先生<rt>せんせい</rt></ruby>から<ruby>聞<rt>き</rt></ruby>きました</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>〜によると deyarli doim そうです bilan juftlashadi.</b>
  Yaponcha yangiliklarda, ob-havo maʼlumotida va rasmiy
  matnlarda bu juftlik shu qadar koʻp uchraydiki, gapning
  boshida «〜によると» ni eshitishingiz bilan oxirida
  «〜そうです» ni kutishingiz mumkin. Bu — yaponcha
  eshitishni osonlashtiradigan kichik hiyla.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «-ga koʻra» va «-ning aytishicha» ham
  xuddi shunday joylashadi — gapning <em>boshida</em>.</b>
  «Gazetaga koʻra, ertaga qor yogʻarkan» — manba oldinda,
  tamgʻa orqada. Yapon tilida ham aynan shu tartib:
  <ruby>新聞<rt>しんぶん</rt></ruby>によると … そうです.
  Ikki tilning gap qurilishi bu yerda bir-biriga toʻliq
  tushadi, shuning uchun bu qolipni tarjima orqali
  oʻrganish <em>xavfsiz</em> — kam sondagi shunday
  joylardan biri.</p>
</div>

<h3>3. Ikki narsa bu qolipda YOʻQ</h3>

<div class="pe-call pe-warn">
  <p><b>Birinchi: そうです ning oʻzi oʻtgan zamonga
  kirmaydi.</b> ✗ <ruby>降<rt>ふ</rt></ruby>るそうでした —
  bunday shakl yoʻq. Zamon <b>gapning ichida</b> turadi:
  <ruby>降<rt>ふ</rt></ruby>っ<b>た</b>そうです.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Ikkinchi: そうです ning oʻzi inkor boʻlmaydi.</b>
  ✗ <ruby>降<rt>ふ</rt></ruby>るそうではありません. Inkor ham
  <b>gapning ichida</b>: <ruby>降<rt>ふ</rt></ruby>ら<b>ない</b>そうです.</p>
</div>

<p>Buning sababi mantiqiy. そうです — bu <em>gapning
oʻzi emas</em>, gapning <em>qayerdan kelgani</em>. Siz
eshitgan xabarni oʻzgartira olmaysiz: xabar qanday
boʻlsa, shundayligicha uzatasiz va oxiriga «eshitdim»
degan tamgʻani bosasiz. Shuning uchun zamon ham,
inkor ham xabarning <b>ichida</b> qoladi. Bu qolipni
«tamgʻa» deb tasavvur qilsangiz, ikkala qoida ham
oʻzidan-oʻzi kelib chiqadi.</p>

<h3>4. Ikki そう bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th></th><th>Koʻrinish (PJ-73)</th><th>Xabar (PJ-74)</th></tr>
  <tr><td class="pj-stem">Qayerdan bilaman</td><td class="pj-uz">koʻzim bilan koʻrdim</td>
      <td class="pj-res">birovdan eshitdim</td></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-uz"><ruby>降<rt>ふ</rt></ruby>り<b>そうです</b></td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>る<b>そうです</b></td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-uz">おいし<b>そうです</b></td>
      <td class="pj-res">おいしい<b>そうです</b></td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-uz"><ruby>元気<rt>げんき</rt></ruby><b>そうです</b></td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby>だ<b>そうです</b></td></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-uz">— (yoʻq)</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>だ<b>そうです</b></td></tr>
  <tr><td class="pj-stem">Oʻzbekcha</td><td class="pj-uz">yogʻay deb turibdi</td>
      <td class="pj-res">yogʻarkan</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Jadvalning ikkinchi qatorini yodlasangiz, qolgani
  oʻzi keladi.</b> <ruby>降<rt>ふ</rt></ruby>り<b>そう</b> —
  bitta bogʻin kam; <ruby>降<rt>ふ</rt></ruby>る<b>そう</b> —
  butun feʼl. Yaponlar ham bu ikkisini <em>aynan shu</em>
  farq bilan eshitadi, boshqa hech qanday belgi yoʻq.
  Shuning uchun gapirganda bu bogʻinni yutib yubormang.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bu ikki ohangni butunlay boshqa
  soʻzlar bilan ajratadi, shuning uchun adashish
  qiyin — toʻgʻri tarjimani tanlang, shakl oʻzi
  chiqadi.</b> «Yogʻay deb turibdi» deyapsizmi — demak
  ます-oʻzak. «Yogʻarkan» deyapsizmi — demak lugʻat
  shakli. Gapni avval oʻzbekcha aniq ayting, keyin
  yaponchaga oʻting: bu tartib xatoni deyarli
  yoʻq qiladi.</p>
</div>

<h3>5. Ohang: bu qolip nima deydi</h3>

<p>〜そうです (xabar) qoʻyilgan gap — bu sizning
gapingiz emas. Siz faqat <b>pochtachisiz</b>. Shuning
uchun bu qolip ikki joyda juda koʻp ishlatiladi:
yangiliklar va gʻiybat.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">イノムさんは<ruby>来月<rt>らいげつ</rt></ruby><ruby>大阪<rt>おおさか</rt></ruby>へ<ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>すそうですよ。</p>
  <p class="pe-ex__uz">Inom kelasi oy Osakaga koʻchib ketarkan-a.</p>
  <p class="pe-ex__why">よ bilan birga bu gap «senga ayta turay» degan ohangni oladi — tipik maktab tanaffusi gapi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Va shuning uchun bu qolip javobgarlikni
  yengillashtiradi.</b> «<ruby>試験<rt>しけん</rt></ruby>は
  <ruby>難<rt>むずか</rt></ruby>しいそうです» degan odam
  «imtihon qiyin» demayapti — «shunday deyishdi» deyapti.
  Agar imtihon oson chiqsa, u yolgʻonchi boʻlmaydi. Yapon
  tilida bunday «masofa saqlovchi» qoliplar koʻp, va
  keyingi darsda ulardan yana ikkitasini koʻrasiz.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">報</span>
    <span class="pj-kanji__uz">xabar, xabar bermoq</span>
    <span class="pj-kanji__on">オン: ホウ</span>
    <span class="pj-kanji__kun">KUN: しら(せる)</span>
    <span class="pj-kanji__note">天気予報 (てんきよほう) — ob-havo maʼlumoti · 情報 (じょうほう) — axborot</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">聞</span>
    <span class="pj-kanji__uz">eshitmoq, soʻramoq</span>
    <span class="pj-kanji__on">オン: ブン</span>
    <span class="pj-kanji__kun">KUN: き(く)</span>
    <span class="pj-kanji__note">新聞 (しんぶん) — gazeta · 聞く (きく) — eshitmoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るそうでした</p>
  <p class="pe-fix__good">✓ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>っ<b>た</b>そうです — zamon <b>gapning ichida</b> turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るそうではありません</p>
  <p class="pe-fix__good">✓ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ら<b>ない</b>そうです — inkor ham gapning ichida.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>そうです</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>だ</b>そうです — ot <b>だ</b> ni saqlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>元気<rt>げんき</rt></ruby>そうです<br><small>(«tetik ekan» demoqchi boʻlsangiz)</small></p>
  <p class="pe-fix__good">✓ <ruby>元気<rt>げんき</rt></ruby><b>だ</b>そうです — だ siz bu gap «tetik koʻrinadi» boʻlib qoladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Parining akasi shifokor ekan» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>パリさんのお<ruby>兄<rt>にい</rt></ruby>さんは<ruby>医者<rt>いしゃ</rt></ruby>だそうです</b> — ot + <b>だ</b> + そうです.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Kecha yomgʻir yogʻgan ekan» — qaysi shakl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>昨日<rt>きのう</rt></ruby><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったそうです</b> — そうでした emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>元気<rt>げんき</rt></ruby>そうです va <ruby>元気<rt>げんき</rt></ruby>だそうです — farqi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisi — <b>koʻrdim</b> («tetik koʻrinadi»), ikkinchisi — <b>eshitdim</b> («tetik ekan»). Farq — bitta <b>だ</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Gapga «gazetaga koʻra» qoʻshing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>新聞<rt>しんぶん</rt></ruby>によると</b> — va gapning oxirida deyarli doim そうです turadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Yomgʻir yogʻmasakan» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>雨<rt>あめ</rt></ruby>は<ruby>降<rt>ふ</rt></ruby>らないそうです</b> — inkor gapning ichida, そうです oʻzgarmaydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>oddiy shakl + そうです</b> — …ekan (eshitilgan xabar)</li>
  <li><b>〜によると</b> — …ga koʻra</li>
  <li><b>〜の<ruby>話<rt>はなし</rt></ruby>では</b> — …ning aytishicha</li>
  <li><b><ruby>天気予報<rt>てんきよほう</rt></ruby></b> — ob-havo maʼlumoti</li>
  <li><b><ruby>新聞<rt>しんぶん</rt></ruby></b> — gazeta</li>
  <li><b><ruby>医者<rt>いしゃ</rt></ruby></b> — shifokor</li>
  <li><b><ruby>雪<rt>ゆき</rt></ruby></b> — qor</li>
  <li><b><ruby>引<rt>ひ</rt></ruby>っ<ruby>越<rt>こ</rt></ruby>す</b> — koʻchib oʻtmoq</li>
  <li><b><ruby>試験<rt>しけん</rt></ruby></b> — imtihon</li>
  <li><b><ruby>情報<rt>じょうほう</rt></ruby></b> — axborot</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Xabar そう — <b>oddiy shakl</b>, hech nima kesilmaydi.</li>
    <li>な-sifat va ot <b>だ</b> ni saqlaydi: <ruby>学生<rt>がくせい</rt></ruby>だそうです.</li>
    <li>Zamon ham, inkor ham <b>gapning ichida</b>; そうです oʻzgarmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-75: 〜ようです va 〜らしいです — taxminning ikki darajasi",
        "category": "japanese",
        "order": 75,
        "summary": (
            "ようです — dalilga qarab oʻzim chiqargan xulosa. らしい "
            "— tashqaridan kelgan gap. Dars oxirida toʻrtala taxmin "
            "qolipi bitta jadvalga yigʻiladi."
        ),
        "stories": ["となりの へやの おと"],
        "content": """
<h2>PJ-75: 〜ようです va 〜らしいです</h2>

<p>Qoʻshni xonadan bir haftadan beri ovoz kelmayapti. Eshik
oldida poyabzal yoʻq. Pochta qutisi toʻlib ketgan. Siz
qoʻshningizni koʻrmadingiz, hech kim sizga hech nima
aytmadi — lekin miyangiz allaqachon xulosa chiqardi:
<b>«Koʻchib ketishganga oʻxshaydi»</b>.</p>

<p>Mana shu — bugungi darsning birinchi qolipi. Ikkinchisi esa
boshqa vaziyatdan chiqadi: birov sizga «ular koʻchib
ketishganmish» dedi, siz esa buni uzatyapsiz, lekin
javobgarlikni oʻz zimmangizga olmaysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ようです ni dalilga tayangan xulosa uchun ishlatasiz</li>
    <li>らしい ni tashqaridan kelgan gap uchun ishlatasiz</li>
    <li>Ikkalasining <b>ulanishi</b>dagi farqni yodlaysiz</li>
    <li>Toʻrtala taxmin qolipini bitta jadvalda ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki taxmin</span>
  <span class="pe-chip pe-chip--s">oddiy shakl</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">ようです</span>
  <span class="pe-op">/</span>
  <span class="pe-chip pe-chip--aux">らしいです</span>
</div>

<h3>1. ようです — mening xulosam</h3>

<p>ようです qoʻyilgan gapda <b>dalil menda</b>. Men bir
narsani koʻrdim, eshitdim, sezdim — va shundan xulosa
chiqardim. Shuning uchun bu qolip
<em>javobgarlikni oʻzimga oladi</em>: agar xulosam
notoʻgʻri chiqsa, aybdor men boʻlaman.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>電気<rt>でんき</rt></ruby>が<ruby>消<rt>き</rt></ruby>えています。<span class="pe-hl pe-hl--v"><ruby>誰<rt>だれ</rt></ruby>もいないようです</span>。</p>
  <p class="pe-ex__uz">Chiroq oʻchgan. Hech kim yoʻqqa oʻxshaydi.</p>
  <p class="pe-ex__why">Dalil — oʻchgan chiroq. Xulosa — meniki.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">ムニラさんは<ruby>咳<rt>せき</rt></ruby>をしています。<span class="pe-hl pe-hl--o"><ruby>風邪<rt>かぜ</rt></ruby>を<ruby>引<rt>ひ</rt></ruby>いたようです</span>。</p>
  <p class="pe-ex__uz">Munira yoʻtalyapti. Shamollaganga oʻxshaydi.</p>
  <p class="pe-ex__why">Yoʻtalni men eshityapman; «shamollagan» degan xulosani men chiqaryapman.</p>
</div>

<h3>2. らしいです — tashqaridan kelgan gap</h3>

<p>らしい esa boshqacha: dalil <b>menda emas</b>. Men
eshitdim, oʻqidim, odamlar shunday deyishdi. Shuning uchun
bu qolip <em>javobgarlikni oʻzimdan uzoqlashtiradi</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">あの<ruby>店<rt>みせ</rt></ruby>は<span class="pe-hl pe-hl--adv"><ruby>安<rt>やす</rt></ruby>いらしいです</span>よ。</p>
  <p class="pe-ex__uz">Anavi doʻkon arzonmish.</p>
  <p class="pe-ex__why">Men u yerdan hech nima olmadim. Shunday deyishdi, xolos.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bu ikkisini juda aniq ajratadi, va
  tarjimani tanlash shaklni ham tanlaydi.</b>
  ようです — «<em>-ga oʻxshaydi</em>», «<em>shekilli</em>»,
  «<em>chogʻi</em>»: <ruby>誰<rt>だれ</rt></ruby>もいない
  ようです — «hech kim yoʻqqa oʻxshaydi». らしい —
  «<em>-mish</em>», «<em>aytishlaricha</em>»,
  «<em>emish</em>»: <ruby>安<rt>やす</rt></ruby>いらしいです —
  «arzonmish». Yaʼni «oʻxshaydi» deyapsizmi — よう;
  «-mish» deyapsizmi — らしい. Bu oddiy tekshiruv
  oʻquvchini deyarli hech qachon aldamaydi.</p>
</div>

<h3>3. Ulanish — darsning eng muhim jadvali</h3>

<p>Ikki qolip <b>maʼnosi bilan emas, ulanishi bilan</b>
qiynaydi. ようだ oʻzi な-sifat kabi tutadi: oldidan
な yoki の talab qiladi. らしい esa い-sifat kabi tutadi
va <b>yalangʻoch</b> ulanadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Soʻz</th><th>ようです</th><th>らしいです</th></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-end"><ruby>降<rt>ふ</rt></ruby>る</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>るようです</td>
      <td class="pj-uz"><ruby>降<rt>ふ</rt></ruby>るらしいです</td></tr>
  <tr><td class="pj-stem">feʼl, oʻtgan</td><td class="pj-end"><ruby>降<rt>ふ</rt></ruby>った</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>ったようです</td>
      <td class="pj-uz"><ruby>降<rt>ふ</rt></ruby>ったらしいです</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end"><ruby>高<rt>たか</rt></ruby>い</td>
      <td class="pj-res"><ruby>高<rt>たか</rt></ruby>いようです</td>
      <td class="pj-uz"><ruby>高<rt>たか</rt></ruby>いらしいです</td></tr>
  <tr><td class="pj-stem">な-sifat</td><td class="pj-end"><ruby>元気<rt>げんき</rt></ruby></td>
      <td class="pj-res"><ruby>元気<rt>げんき</rt></ruby><b>な</b>ようです</td>
      <td class="pj-uz"><ruby>元気<rt>げんき</rt></ruby>らしいです</td></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end"><ruby>学生<rt>がくせい</rt></ruby></td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby><b>の</b>ようです</td>
      <td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby>らしいです</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Faqat oxirgi ikki qatorni yodlang.</b> Feʼl va
  い-sifat ikkalasida ham bir xil ulanadi — u yerda
  xato qilish imkoni yoʻq. Butun qiyinchilik
  <ruby>元気<rt>げんき</rt></ruby> va
  <ruby>学生<rt>がくせい</rt></ruby> qatorlarida:
  <b>な</b>ようです / <b>の</b>ようです, lekin らしい
  oldida <em>hech narsa yoʻq</em>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu ulanish tanish boʻlishi kerak.</b> PJ-48 da
  siz otni butun gap bilan aniqlagansiz, va u yerda ham
  な-sifat <b>な</b>, ot esa <b>の</b> olgan edi:
  <ruby>元気<rt>げんき</rt></ruby>な<ruby>人<rt>ひと</rt></ruby>,
  <ruby>学生<rt>がくせい</rt></ruby>の<ruby>兄<rt>あに</rt></ruby>.
  ようだ oʻzi ham <em>ot</em>dan kelib chiqqan
  (<ruby>様<rt>よう</rt></ruby> — «koʻrinish»), shuning uchun
  u ham xuddi shu ulanishni talab qiladi. Yaʼni bu yangi
  qoida emas — eski qoidaning yangi joyi.</p>
</div>

<h3>4. ような va ように</h3>

<p>ようだ な-sifat kabi tuslangani uchun, otdan oldin
<b>ような</b>, feʼldan oldin <b>ように</b> boʻladi — xuddi
PJ-73 dagi そうな / そうに kabi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>子供<rt>こども</rt></ruby>の</span>
  <span class="pj-joshi__p">ような<small>+ OT</small></span>
  <span class="pj-joshi__n"><ruby>声<rt>こえ</rt></ruby></span>
  <span class="pj-joshi__uz">bolanikiga oʻxshagan ovoz</span>
</div>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>雪<rt>ゆき</rt></ruby>の</span>
  <span class="pj-joshi__p">ように<small>+ SIFAT/FEʼL</small></span>
  <span class="pj-joshi__v"><ruby>白<rt>しろ</rt></ruby>い</span>
  <span class="pj-joshi__uz">qordek oq</span>
</div>

<div class="pe-call pe-tip">
  <p><b>Yaʼni ようだ ikki ish qiladi:</b> taxmin
  («…ga oʻxshaydi») va oʻxshatish («…dek»). Ikkalasining
  ildizi bitta —
  <ruby>様<rt>よう</rt></ruby> «koʻrinish» soʻzi. Farqni
  vaziyat ajratadi: <ruby>雪<rt>ゆき</rt></ruby>のように
  <ruby>白<rt>しろ</rt></ruby>い da hech kim qorni haqiqatan
  koʻrmagan — bu oʻxshatish; qoʻshni xonadagi misolda esa
  bu haqiqiy taxmin.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «-dek» ham ikki ishni qiladi, xuddi
  ように kabi.</b> «Qordek oq» — oʻxshatish; «kelmaydigandek
  koʻrinadi» — taxmin. Yaʼni oʻzbek tilida ham bitta
  qoʻshimcha ikkala ishni koʻtaradi va ularni faqat vaziyat
  ajratadi. Shuning uchun ようだ ning ikki maʼnosini ikkita
  alohida qoida deb yodlamang — ular bitta fikrning ikki
  ishlatilishi.</p>
</div>

<h3>5. らしい ning ikkinchi ishi: «…ga xos»</h3>

<p>らしい otdan keyin kelganda yana bir maʼno beradi —
«oʻsha narsaga <b>xos</b>», «chinakam». Bu maʼnoda u
eshitilgan xabar emas, <em>baho</em>.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">Eshitdim</p>
    <p><ruby>田中<rt>たなか</rt></ruby>さんは<ruby>学生<rt>がくせい</rt></ruby>らしいです。</p>
    <p>Tanaka talabamish. — Men bilmayman, shunday deyishdi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">…ga xos</p>
    <p><ruby>田中<rt>たなか</rt></ruby>さんは<ruby>学生<rt>がくせい</rt></ruby>らしい<ruby>学生<rt>がくせい</rt></ruby>です。</p>
    <p>Tanaka — chinakam talaba. — Talabaga xos talaba.</p></div>
</div>

<p>Ikki maʼnoni ajratish qiyin emas: «xos» maʼnosida
らしい dan keyin koʻpincha <b>oʻsha otning oʻzi</b> yoki
boshqa bir ot keladi, va gap baho beradi.
<ruby>男<rt>おとこ</rt></ruby>らしい («erkakka xos»),
<ruby>春<rt>はる</rt></ruby>らしい
<ruby>天気<rt>てんき</rt></ruby> («bahorga xos ob-havo») —
bu iboralar tayyor holda yodlanadi.</p>

<h3>6. Toʻrtala taxmin bitta jadvalda</h3>

<p>Uch dars davomida siz toʻrtta qolip koʻrdingiz. Hammasi
bir xil gapga qoʻyilganda farq juda aniq koʻrinadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Gap</th><th>Men buni qayerdan bilaman</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem"><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<b>そうです</b></td>
      <td class="pj-uz">bulutni <b>koʻryapman</b></td>
      <td class="pj-res">yogʻay deb turibdi</td></tr>
  <tr><td class="pj-stem"><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>る<b>そうです</b></td>
      <td class="pj-uz">aniq manbadan <b>eshitdim</b></td>
      <td class="pj-res">yogʻarkan</td></tr>
  <tr><td class="pj-stem"><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>る<b>ようです</b></td>
      <td class="pj-uz">dalil bor, <b>xulosa meniki</b></td>
      <td class="pj-res">yogʻadigan shekilli</td></tr>
  <tr><td class="pj-stem"><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>る<b>らしいです</b></td>
      <td class="pj-uz"><b>odamlar</b> shunday deyishdi</td>
      <td class="pj-res">yogʻarmish</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Jadvalning birinchi qatoriga eʼtibor bering: faqat
  u ます-oʻzakka ulanadi.</b> Qolgan uchtasi oddiy shaklga
  ulanadi. Yaʼni butun toʻrtlikni ikki savol bilan ajratish
  mumkin: <em>(1) oxiri kesilganmi?</em> — kesilgan boʻlsa
  koʻrinish そう. <em>(2) kesilmagan boʻlsa — qaysi
  soʻz turgan?</em> そう eshitdim, よう oʻzim
  xulosa qildim, らしい odamlar aytdi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>らしい va <ruby>伝聞<rt>でんぶん</rt></ruby> そう juda yaqin, lekin bir xil emas.</b>
  そうです aniq manbani nazarda tutadi va odatda
  «〜によると» bilan yuradi. らしい esa manbani
  koʻrsatmaydi: «hamma shunday deydi», «shunaqa gap bor».
  Shuning uchun rasmiy yangilikda そうです, tanaffusdagi
  gapda らしい eshitiladi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">様</span>
    <span class="pj-kanji__uz">koʻrinish, holat; hurmat qoʻshimchasi</span>
    <span class="pj-kanji__on">オン: ヨウ</span>
    <span class="pj-kanji__kun">KUN: さま</span>
    <span class="pj-kanji__note">〜のようだ — …ga oʻxshaydi · お客様 (おきゃくさま) — mijoz</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">風</span>
    <span class="pj-kanji__uz">shamol; uslub</span>
    <span class="pj-kanji__on">オン: フウ</span>
    <span class="pj-kanji__kun">KUN: かぜ</span>
    <span class="pj-kanji__note">風 (かぜ) — shamol · 風邪を引く (かぜをひく) — shamollamoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>ようです</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>の</b>ようです — ようだ otdan keyin <b>の</b> talab qiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>元気<rt>げんき</rt></ruby><b>の</b>ようです</p>
  <p class="pe-fix__good">✓ <ruby>元気<rt>げんき</rt></ruby><b>な</b>ようです — な-sifat <b>な</b> oladi, の emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby><b>だ</b>らしいです</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby>らしいです — らしい <b>yalangʻoch</b> ulanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>りようです</p>
  <p class="pe-fix__good">✓ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby><b>る</b>ようです — ようだ <b>oddiy shaklga</b> ulanadi, ます-oʻzakka emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>元気<rt>げんき</rt></ruby> ni ようです bilan bogʻlang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>元気<rt>げんき</rt></ruby>なようです</b> — な-sifat <b>な</b> oladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>学生<rt>がくせい</rt></ruby> ni らしいです bilan bogʻlang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>学生<rt>がくせい</rt></ruby>らしいです</b> — na だ, na の, na な. Yalangʻoch.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Chiroq oʻchgan, poyabzal yoʻq. «Hech kim yoʻqqa oʻxshaydi» — qaysi qolip?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>誰<rt>だれ</rt></ruby>もいないようです</b> — dalil menda, xulosa ham meniki.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Qordek oq» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>雪<rt>ゆき</rt></ruby>のように<ruby>白<rt>しろ</rt></ruby>い</b> — sifatdan oldin <b>ように</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>降<rt>ふ</rt></ruby>りそうです va <ruby>降<rt>ふ</rt></ruby>るようです — farqi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisi — <b>bevosita koʻrinish</b> (qora bulut). Ikkinchisi — <b>dalildan chiqarilgan xulosa</b> (hamma soyabon koʻtargan). Shakli ham farq qiladi: ます-oʻzak ↔ oddiy shakl.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ようです</b> — …ga oʻxshaydi, shekilli (dalil menda)</li>
  <li><b>〜らしいです</b> — …mish (gap tashqaridan)</li>
  <li><b>〜のようです</b> — ot bilan ulanish</li>
  <li><b>〜なようです</b> — な-sifat bilan ulanish</li>
  <li><b>〜ような + ot</b> — …ga oʻxshagan</li>
  <li><b>〜ように + sifat/feʼl</b> — …dek</li>
  <li><b><ruby>風邪<rt>かぜ</rt></ruby>を<ruby>引<rt>ひ</rt></ruby>く</b> — shamollamoq</li>
  <li><b><ruby>咳<rt>せき</rt></ruby>をする</b> — yoʻtalmoq</li>
  <li><b><ruby>電気<rt>でんき</rt></ruby>が<ruby>消<rt>き</rt></ruby>える</b> — chiroq oʻchadi</li>
  <li><b><ruby>春<rt>はる</rt></ruby>らしい</b> — bahorga xos</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>ようです — <b>dalil menda</b>; らしいです — <b>gap tashqaridan</b>.</li>
    <li>ようだ <b>な / の</b> talab qiladi; らしい <b>yalangʻoch</b> ulanadi.</li>
    <li>Toʻrtlikni ikki savol ajratadi: oxiri kesilganmi, va kim aytdi.</li>
  </ul>
</div>
""",
    },
]
