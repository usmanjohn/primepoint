# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-25, PJ-26 (Block B oxiri) va PJ-27 (Block C boshi).

PJ-27 — butun kursning kaliti: feʼl guruhlari. Undan keyingi har bir feʼl
shakli shu uchta guruhga qarab yasaladi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_25_27.py --author=prime
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
        "title": "PJ-25: い-sifatlar — ularning inkori va oʻtgan zamoni",
        "category": "japanese",
        "order": 25,
        "summary": (
            "Yaponcha sifatlar feʼl kabi tuslanadi va zamonni oʻzi tashiydi — "
            "bu oʻzbek va rus tillaridan tubdan farq qiladi."
        ),
        "stories": ["おおきい ねこと ちいさい ねこ"],
        "content": """
<h2>PJ-25: い-sifatlar — ularning inkori va oʻtgan zamoni</h2>

<p>Yigirma toʻrt dars davomida narsalarni <em>nomlash</em> va odamlarning
<em>ish qilishi</em> haqida gapirdingiz. Bugun ularni <b>taʼriflashni</b>
oʻrganasiz — va bu yerda yapon tili sizni hayratda qoldiradi.</p>

<p>Chunki yaponcha sifat <em>sifat kabi</em> emas, <b>feʼl kabi</b> ishlaydi:
u oʻzi inkor boʻladi, oʻzi oʻtgan zamonga oʻtadi va gap oxirida yolgʻiz
turishi mumkin. Oʻzbek va rus tillarida sifat bunday qila olmaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>い-sifatni otdan oldin qoʻyasiz — の <b>siz</b></li>
    <li>Inkor yasaysiz: い → くない</li>
    <li>Oʻtgan zamon yasaysiz: い → かった</li>
    <li>いい sifatining yagona tartibsizligini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Sifat zamonni OʻZI tashiydi</span>
  <span class="pe-chip pe-chip--s">おおきい</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--neg">おおきくない</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">おおきかった</span>
</div>

<h3>1. い-sifat nima</h3>

<p>Nomi hamma narsani aytadi: bu sifatlar <b>い</b> bilan tugaydi. Ularni
tanish oson.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Sifat</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>大<rt>おお</rt></ruby>きい</td><td class="pj-res">ōkii</td><td class="pj-uz">katta</td></tr>
  <tr><td><ruby>小<rt>ちい</rt></ruby>さい</td><td class="pj-res">chiisai</td><td class="pj-uz">kichik</td></tr>
  <tr><td><ruby>新<rt>あたら</rt></ruby>しい</td><td class="pj-res">atarashii</td><td class="pj-uz">yangi</td></tr>
  <tr><td><ruby>高<rt>たか</rt></ruby>い</td><td class="pj-res">takai</td><td class="pj-uz">baland; qimmat</td></tr>
  <tr><td><ruby>安<rt>やす</rt></ruby>い</td><td class="pj-res">yasui</td><td class="pj-uz">arzon</td></tr>
  <tr><td><ruby>面白<rt>おもしろ</rt></ruby>い</td><td class="pj-res">omoshiroi</td><td class="pj-uz">qiziqarli</td></tr>
  <tr><td>いい</td><td class="pj-res">ii</td><td class="pj-uz">yaxshi</td></tr>
</table></div>

<h3>2. Otdan oldin — の siz</h3>

<p>PJ-17 da aytgan edim: <b>の faqat ikki otni bogʻlaydi</b>. Sifat esa otga
<em>toʻgʻridan-toʻgʻri</em> yopishadi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">OT + OT — の kerak</p>
    <p class="pj-big">の</p>
    <p><ruby>日本語<rt>にほんご</rt></ruby><b>の</b><ruby>本<rt>ほん</rt></ruby><br>
    yapon tili kitobi</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">SIFAT + OT — の YOʻQ</p>
    <p class="pj-big">—</p>
    <p><ruby>大<rt>おお</rt></ruby>きい<ruby>本<rt>ほん</rt></ruby><br>
    katta kitob</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham xuddi shunday.</b> «Katta kitob» — hech qanday
  bogʻlovchi yoʻq, sifat otga yopishib turadi. «Kitob<em>ning</em> muqovasi» —
  bu yerda esa bogʻlovchi bor. Yaponchada ham aynan shu farq:
  <ruby>大<rt>おお</rt></ruby>きい<ruby>本<rt>ほん</rt></ruby> va
  <ruby>本<rt>ほん</rt></ruby>の<ruby>表紙<rt>ひょうし</rt></ruby>.</p>
</div>

<h3>3. Kesim boʻlib kelganda</h3>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>本<rt>ほん</rt></ruby>は<ruby>大<rt>おお</rt></ruby>きいです。</p>
  <p class="pe-ex__rom">kono hon wa ōkii desu</p>
  <p class="pe-ex__uz">Bu kitob katta.</p>
  <p class="pe-ex__why">Oxiridagi <b>です</b> — faqat <em>muloyimlik</em> uchun. Sifatning oʻzi allaqachon kesim; です unga hech narsa qoʻshmaydi. Bu — keyingi qism uchun muhim.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Mana shu joyda koʻpchilik adashadi.</b> です sifatga zamon
  <em>bermaydi</em>. Shuning uchun inkor va oʻtgan zamon yasaganda
  <b>です ga tegmaysiz</b> — <b>sifatning oʻzini</b> oʻzgartirasiz.</p>
</div>

<h3>4. Inkor: い → くない</h3>

<p>Oxirgi <b>い</b> ni olib tashlang, <b>くない</b> qoʻying.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Sifat</th><th>Oʻzak</th><th>Inkor</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>大<rt>おお</rt></ruby>きい</td><td class="pj-stem"><ruby>大<rt>おお</rt></ruby>き</td>
      <td class="pj-end"><ruby>大<rt>おお</rt></ruby>きくないです</td><td class="pj-uz">katta emas</td></tr>
  <tr><td><ruby>安<rt>やす</rt></ruby>い</td><td class="pj-stem"><ruby>安<rt>やす</rt></ruby></td>
      <td class="pj-end"><ruby>安<rt>やす</rt></ruby>くないです</td><td class="pj-uz">arzon emas</td></tr>
  <tr><td><ruby>面白<rt>おもしろ</rt></ruby>い</td><td class="pj-stem"><ruby>面白<rt>おもしろ</rt></ruby></td>
      <td class="pj-end"><ruby>面白<rt>おもしろ</rt></ruby>くないです</td><td class="pj-uz">qiziq emas</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Ikkinchi shakl ham bor:</b> <ruby>大<rt>おお</rt></ruby>き<b>くありません</b>.
  Maʼnosi bir xil, ozgina rasmiyroq. Kundalik nutqda <b>くないです</b>
  koʻproq eshitiladi, shuning uchun avval shuni oʻrganing.</p>
</div>

<h3>5. Oʻtgan zamon: い → かった</h3>

<p>Xuddi shu mantiq: oxirgi <b>い</b> ni olib tashlang, <b>かった</b> qoʻying.
Diqqat — <b>でした EMAS</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Yaponcha</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-res"><ruby>安<rt>やす</rt></ruby>いです</td><td class="pj-uz">arzon</td></tr>
  <tr><td class="pj-stem">hozirgi inkor</td><td class="pj-res"><ruby>安<rt>やす</rt></ruby>くないです</td><td class="pj-uz">arzon emas</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-res"><ruby>安<rt>やす</rt></ruby>かったです</td><td class="pj-uz">arzon edi</td></tr>
  <tr><td class="pj-stem">oʻtgan inkor</td><td class="pj-res"><ruby>安<rt>やす</rt></ruby>くなかったです</td><td class="pj-uz">arzon emas edi</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Oxirgi qatorga qarang.</b> <ruby>安<rt>やす</rt></ruby>く<b>なかった</b>です
  — bu aslida <b>ない</b> ning oʻzi い-sifat boʻlgani uchun shunday chiqadi:
  ない → なかった. Yaʼni siz bitta qoidani <em>ikki marta</em> qoʻllayapsiz.
  Yapon grammatikasi shunday: kichik qoidalar bir-birining ustiga
  qoʻyiladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>昨日<rt>きのう</rt></ruby>の<ruby>映画<rt>えいが</rt></ruby>は<ruby>面白<rt>おもしろ</rt></ruby>かったです。</p>
  <p class="pe-ex__rom">kinō no ēga wa omoshirokatta desu</p>
  <p class="pe-ex__uz">Kechagi kino qiziqarli edi.</p>
  <p class="pe-ex__why">です <b>oʻzgarmadi</b> — u hozirgi shaklda qoldi. Zamonni <b>sifat</b> tashidi. «<ruby>面白<rt>おもしろ</rt></ruby>いでした» — eng koʻp uchraydigan xato.</p>
</div>

<h3>6. Nega bu oʻzbek oʻquvchi uchun yangi</h3>

<p>Bir daqiqa toʻxtab, farqni aniq koʻring — chunki bu kursdagi eng katta
tuzilish farqlaridan biri.</p>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">OʻZBEKCHA</p>
    <p class="pj-pair__form">arzon <b>edi</b></p>
    <p>Sifat qimirlamaydi. Zamonni <b>alohida soʻz</b> («edi») yoki
    bogʻlama tashiydi.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">YAPONCHA</p>
    <p class="pj-pair__form"><ruby>安<rt>やす</rt></ruby><b>かった</b></p>
    <p>Sifatning <b>oʻzi</b> oʻzgaradi. Alohida soʻz kerak emas — sifat
    feʼl kabi tuslanadi.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Shuning uchun です ni «edi» deb tarjima qilish odati xato keltiradi.</b>
  Oʻquvchi «arzon edi» deyish uchun «です» ni «でした» ga oʻzgartirmoqchi
  boʻladi — va «<ruby>安<rt>やす</rt></ruby>いでした» chiqadi. Toʻgʻrisi esa
  <ruby>安<rt>やす</rt></ruby><b>かった</b>です: sifat oʻzgardi, です esa
  joyida qoldi. です bu yerda <em>faqat muloyimlik</em> belgisi, boshqa
  hech nima emas.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Tekshirish usuli:</b> gapdan です ni olib tashlang. Agar qolgani
  ham toʻgʻri yaponcha boʻlsa — sifat toʻgʻri tuslangan.
  <ruby>安<rt>やす</rt></ruby>かった — toʻgʻri (kundalik nutqda aynan shunday
  aytiladi). <ruby>安<rt>やす</rt></ruby>い<em>でした</em> dan です ni olsangiz
  <ruby>安<rt>やす</rt></ruby>い qoladi va zamon yoʻqoladi — demak xato edi.</p>
</div>

<h3>7. いい — yagona tartibsiz sifat</h3>

<p>Butun い-sifatlar ichida <b>bitta</b> istisno bor, va u eng koʻp
ishlatiladigan sifat: <b>いい</b> («yaxshi»).</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Kutilgan</th><th>Haqiqiy</th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-uz">いいです</td><td class="pj-res">いいです ✓</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-uz">いくないです</td><td class="pj-res">よくないです</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-uz">いかったです</td><td class="pj-res">よかったです</td></tr>
  <tr><td class="pj-stem">oʻtgan inkor</td><td class="pj-uz">いくなかったです</td><td class="pj-res">よくなかったです</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Sababi tarixiy:</b> bu sifatning eski shakli <b>よい</b> edi va
  tuslanish oʻsha eski oʻzakdan yasaladi. Faqat <em>lugʻat shakli</em>
  いい boʻlib oʻzgargan. Shuning uchun: <b>い bilan boshlanadi, よ bilan
  tuslanadi</b>. <b>よかった！</b> («yaxshi boʻldi!») — yaponlar kuniga
  koʻp marta aytadigan ibora.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>面白<rt>おもしろ</rt></ruby>いでした</p>
  <p class="pe-fix__good">✓ <ruby>面白<rt>おもしろ</rt></ruby><b>かった</b>です — zamonni <b>sifat</b> tashiydi, です emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>大<rt>おお</rt></ruby>きいの<ruby>本<rt>ほん</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>大<rt>おお</rt></ruby>きい<ruby>本<rt>ほん</rt></ruby> — sifat otga toʻgʻridan-toʻgʻri yopishadi, の <b>siz</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ いくないです</p>
  <p class="pe-fix__good">✓ <b>よ</b>くないです — いい yagona tartibsiz sifat: い bilan boshlanadi, <b>よ</b> bilan tuslanadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>安<rt>やす</rt></ruby>い ning inkorini ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>安<rt>やす</rt></ruby>くないです</b> — oxirgi い oʻrniga くない.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Qiziqarli edi» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>面白<rt>おもしろ</rt></ruby>かったです</b> — «<ruby>面白<rt>おもしろ</rt></ruby>いでした» notoʻgʻri. です oʻzgarmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Katta kitob» — の kerakmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> <ruby>大<rt>おお</rt></ruby>きい<ruby>本<rt>ほん</rt></ruby>. の faqat <b>ikki otni</b> bogʻlaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. いい ning oʻtgan zamoni qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>よかったです</b>. Eski shakli よい boʻlgani uchun tuslanish よ dan yasaladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. い-sifat nimasi bilan feʼlga oʻxshaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>U <b>zamonni oʻzi tashiydi</b> va oʻzi inkor boʻladi. Oʻzbek va rus tillarida sifat bunday qila olmaydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>大<rt>おお</rt></ruby>きい</b> — katta</li>
  <li><b><ruby>小<rt>ちい</rt></ruby>さい</b> — kichik</li>
  <li><b><ruby>新<rt>あたら</rt></ruby>しい</b> — yangi</li>
  <li><b><ruby>古<rt>ふる</rt></ruby>い</b> — eski</li>
  <li><b><ruby>高<rt>たか</rt></ruby>い</b> — baland, qimmat</li>
  <li><b><ruby>安<rt>やす</rt></ruby>い</b> — arzon</li>
  <li><b><ruby>面白<rt>おもしろ</rt></ruby>い</b> — qiziqarli</li>
  <li><b><ruby>難<rt>むずか</rt></ruby>しい</b> — qiyin</li>
  <li><b>いい</b> — yaxshi (tartibsiz)</li>
  <li><b>〜かった</b> — sifatning oʻtgan zamoni</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Sifat otga <b>の siz</b> yopishadi: <ruby>大<rt>おお</rt></ruby>きい<ruby>本<rt>ほん</rt></ruby>.</li>
    <li>Zamonni <b>sifat</b> tashiydi, です emas: い → <b>くない</b>, い → <b>かった</b>.</li>
    <li><b>いい</b> — yagona istisno: い bilan boshlanadi, <b>よ</b> bilan tuslanadi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-26: な-sifatlar — nega ular boshqacha tuslanadi",
        "category": "japanese",
        "order": 26,
        "summary": (
            "Ikkinchi sifat turi. い-sifat feʼl kabi, な-sifat esa OT kabi "
            "ishlaydi — va shu bilan uning butun tuslanishi tushunarli boʻladi."
        ),
        "stories": ["しずかな としょかん"],
        "content": """
<h2>PJ-26: な-sifatlar — nega ular boshqacha tuslanadi</h2>

<p>Oʻtgan darsda い-sifat feʼl kabi tuslanishini koʻrdingiz. Endi ikkinchi
tur keladi — va uning butun mantiqi bitta jumlaga sigʻadi:</p>

<p><b>な-sifat ot kabi ishlaydi.</b> Shuning uchun uning inkori
ではありません, oʻtgan zamoni でした — <em>xuddi otniki kabi</em>. Yangi
qoida yodlash kerak emas: siz buni PJ-13 va PJ-23 da allaqachon
oʻrgangansiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>な-sifatni otdan oldin な bilan qoʻyasiz</li>
    <li>Uning tuslanishi ot bilan bir xil ekanini koʻrasiz</li>
    <li>Ikki sifat turini bir jadvalda taqqoslaysiz</li>
    <li>い bilan tugaydigan yolgʻonchi な-sifatlarni tanib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki tur, ikki mantiq</span>
  <span class="pe-chip pe-chip--v">い-sifat = FEʼL kabi</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">な-sifat = OT kabi</span>
</div>

<h3>1. な-sifat nima</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Sifat</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>静<rt>しず</rt></ruby>か</td><td class="pj-res">shizuka</td><td class="pj-uz">jimjit</td></tr>
  <tr><td><ruby>元気<rt>げんき</rt></ruby></td><td class="pj-res">genki</td><td class="pj-uz">tetik, sogʻlom</td></tr>
  <tr><td><ruby>有名<rt>ゆうめい</rt></ruby></td><td class="pj-res">yūmei</td><td class="pj-uz">mashhur</td></tr>
  <tr><td><ruby>便利<rt>べんり</rt></ruby></td><td class="pj-res">benri</td><td class="pj-uz">qulay</td></tr>
  <tr><td>きれい</td><td class="pj-res">kirei</td><td class="pj-uz">chiroyli; toza</td></tr>
  <tr><td><ruby>好<rt>す</rt></ruby>き</td><td class="pj-res">suki</td><td class="pj-uz">yoqadigan</td></tr>
</table></div>

<h3>2. Otdan oldin — <b>な</b> qoʻshiladi</h3>

<p>Bu turning nomi shundan: otdan oldin turganda ular <b>な</b> oladi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">い-SIFAT</p>
    <p class="pj-big">—</p>
    <p><ruby>大<rt>おお</rt></ruby>きい<ruby>本<rt>ほん</rt></ruby><br>
    Hech narsa qoʻshilmaydi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">な-SIFAT</p>
    <p class="pj-big">な</p>
    <p><ruby>静<rt>しず</rt></ruby>か<b>な</b><ruby>教室<rt>きょうしつ</rt></ruby><br>
    な qoʻshiladi.</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>Bu な aslida nima?</b> U <b>だ</b> (です ning oddiy shakli) ning eski
  aniqlovchi koʻrinishi. Yaʼni
  <ruby>静<rt>しず</rt></ruby>かな<ruby>教室<rt>きょうしつ</rt></ruby> asli
  «jimjit <em>boʻlgan</em> sinf» degani. Shuning uchun ham bu sifatlar
  ot kabi tuslanadi — ular <em>aslida</em> ot bilan bir oilada.</p>
</div>

<h3>3. Kesim boʻlganda — ot bilan aynan bir xil</h3>

<p>Mana darsning eng yengil qismi. な-sifatning toʻrtta shakli — bu PJ-13
va PJ-23 dagi ot shakllarining oʻzi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>OT (<ruby>学生<rt>がくせい</rt></ruby>)</th><th>な-SIFAT (<ruby>静<rt>しず</rt></ruby>か)</th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>です</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かです</td></tr>
  <tr><td class="pj-stem">hozirgi inkor</td><td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>ではありません</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かではありません</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>でした</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かでした</td></tr>
  <tr><td class="pj-stem">oʻtgan inkor</td><td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>ではありませんでした</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かではありませんでした</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Ikki ustun aynan bir xil.</b> Yaʼni な-sifat uchun yangi tuslanish
  yodlash <b>kerak emas</b> — siz uni PJ-13 da otlar bilan birga
  oʻrgangansiz. Faqat bitta narsani eslab qoling: <b>kesim boʻlganda な
  YOʻQOLADI</b>. な faqat otdan oldin turganda paydo boʻladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>教室<rt>きょうしつ</rt></ruby>は<ruby>静<rt>しず</rt></ruby>かです。<ruby>静<rt>しず</rt></ruby>かな<ruby>教室<rt>きょうしつ</rt></ruby>です。</p>
  <p class="pe-ex__rom">kono kyōshitsu wa shizuka desu. shizuka na kyōshitsu desu</p>
  <p class="pe-ex__uz">Bu sinf jimjit. Jimjit sinf.</p>
  <p class="pe-ex__why">Birinchi gapda sifat <b>kesim</b> — な yoʻq. Ikkinchisida u <b>otdan oldin</b> — な bor. Bitta sifat, ikki holat.</p>
</div>

<h3>4. Ikki turni yonma-yon</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>い-sifat (<ruby>安<rt>やす</rt></ruby>い)</th><th>な-sifat (<ruby>静<rt>しず</rt></ruby>か)</th></tr>
  <tr><td class="pj-stem">ot bilan</td><td class="pj-res"><ruby>安<rt>やす</rt></ruby>い<ruby>本<rt>ほん</rt></ruby></td>
      <td class="pj-end"><ruby>静<rt>しず</rt></ruby>か<b>な</b><ruby>本<rt>ほん</rt></ruby></td></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-res"><ruby>安<rt>やす</rt></ruby>いです</td>
      <td class="pj-end"><ruby>静<rt>しず</rt></ruby>かです</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-res"><ruby>安<rt>やす</rt></ruby><b>くない</b>です</td>
      <td class="pj-end"><ruby>静<rt>しず</rt></ruby>か<b>ではありません</b></td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-res"><ruby>安<rt>やす</rt></ruby><b>かった</b>です</td>
      <td class="pj-end"><ruby>静<rt>しず</rt></ruby>か<b>でした</b></td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu jadvalni yodlashning eng oson yoʻli — nomlash.</b> い-sifat
  <em>feʼl</em> tomonda: oʻzi tuslanadi. な-sifat <em>ot</em> tomonda:
  です unga zamon beradi. Oʻzbekchada sifatlar bunday ikkiga
  boʻlinmaydi — hammasi bir xil ishlaydi. Shuning uchun har bir yangi
  sifatni oʻrganganda <b>qaysi turga tegishli ekanini birga yodlang</b>.</p>
</div>

<h3>5. <ruby>好<rt>す</rt></ruby>き va <ruby>嫌<rt>きら</rt></ruby>い — «yoqadi» ni yaponcha aytish</h3>

<p>Ikkita な-sifat bor, ular juda koʻp ishlatiladi va oʻzbek oʻquvchini
doim adashtiradi: <b><ruby>好<rt>す</rt></ruby>き</b> («yoqadigan») va
<b><ruby>嫌<rt>きら</rt></ruby>い</b> («yoqmaydigan»).</p>

<p>Adashtiradigan joyi shu: yaponchada bular <em>feʼl emas, sifat</em>. Yaʼni
«men yaxshi koʻraman» degan feʼl gap emas, «menga yoqimli» degan
<b>sifat gap</b>. Va yoqadigan narsa <b>が</b> oladi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>音楽<rt>おんがく</rt></ruby></span>
  <span class="pj-joshi__p">が<small>EGA</small></span>
  <span class="pj-joshi__v"><ruby>好<rt>す</rt></ruby>きです</span>
  <span class="pj-joshi__uz">Menga musiqa yoqadi. — soʻzma-soʻz: «men — musiqa yoqimli».</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>は<ruby>数学<rt>すうがく</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。でも<ruby>朝<rt>あさ</rt></ruby>が<ruby>嫌<rt>きら</rt></ruby>いです。</p>
  <p class="pe-ex__rom">watashi wa sūgaku ga suki desu. demo asa ga kirai desu</p>
  <p class="pe-ex__uz">Menga matematika yoqadi. Lekin ertalab yoqmaydi.</p>
  <p class="pe-ex__why">Ikkalasida ham yoqadigan (yoki yoqmaydigan) narsa <b>を</b> emas, <b>が</b> oladi. を toʻldiruvchi qoʻshimchasi — u faqat feʼl bilan keladi, sifat bilan emas.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bu yerda yaponchaga yaqin, rus tili esa uzoq.</b>
  Oʻzbekchada ham «men musiqani yaxshi koʻraman» dan tashqari
  «men<b>ga</b> musiqa yoqadi» degan tuzilma bor — va yoqadigan narsa oʻsha
  gapda <em>ega</em> boʻlib turadi, xuddi yaponchadagi kabi. Yapon gapini
  esda saqlashning eng oson yoʻli — uni «menga … yoqadi» deb tarjima
  qilish, «men … ni yaxshi koʻraman» deb emas. Shunda を qoʻyish istagi
  oʻz-oʻzidan yoʻqoladi.</p>
</div>

<p>Tuslanishi esa — hech qanday yangilik yoʻq, ular oddiy な-sifat:
<ruby>好<rt>す</rt></ruby>きです · <ruby>好<rt>す</rt></ruby>きではありません ·
<ruby>好<rt>す</rt></ruby>きでした. Va otdan oldin な oladi:
<b><ruby>好<rt>す</rt></ruby>きな<ruby>音楽<rt>おんがく</rt></ruby></b> —
«yoqadigan musiqa».</p>

<h3>6. Yolgʻonchi な-sifatlar</h3>

<p>Endi tuzoq. Baʼzi な-sifatlar <b>い</b> bilan tugaydi — lekin ular
い-sifat <em>emas</em>. Ularni yodlashdan boshqa yoʻl yoʻq, chunki
yozilishidan bilib boʻlmaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Sifat</th><th>Turi</th><th>Ot bilan</th><th>Inkor</th></tr>
  <tr><td>きれい</td><td class="pj-end">な-sifat!</td><td>きれい<b>な</b><ruby>花<rt>はな</rt></ruby></td>
      <td class="pj-uz">きれいではありません</td></tr>
  <tr><td><ruby>有名<rt>ゆうめい</rt></ruby></td><td class="pj-end">な-sifat!</td>
      <td><ruby>有名<rt>ゆうめい</rt></ruby><b>な</b><ruby>人<rt>ひと</rt></ruby></td>
      <td class="pj-uz"><ruby>有名<rt>ゆうめい</rt></ruby>ではありません</td></tr>
  <tr><td><ruby>嫌<rt>きら</rt></ruby>い</td><td class="pj-end">な-sifat!</td>
      <td><ruby>嫌<rt>きら</rt></ruby><b>な</b><ruby>音<rt>おと</rt></ruby></td>
      <td class="pj-uz"><ruby>嫌<rt>きら</rt></ruby>いではありません</td></tr>
  <tr><td><ruby>高<rt>たか</rt></ruby>い</td><td class="pj-stem">い-sifat</td>
      <td><ruby>高<rt>たか</rt></ruby>い<ruby>山<rt>やま</rt></ruby></td>
      <td class="pj-uz"><ruby>高<rt>たか</rt></ruby>くないです</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Nega shunday?</b> Haqiqiy い-sifatda <b>い</b> — <em>tuslanadigan
  qoʻshimcha</em>. きれい da esa い soʻzning bir qismi
  (<ruby>綺麗<rt>きれい</rt></ruby> — bitta soʻz, ikkita kanji). Yaʼni uni
  ajratib boʻlmaydi. Bu uchtasi eng koʻp uchraydiganlari, shuning uchun
  ularni hozirdan yodlab qoʻying.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>静<rt>しず</rt></ruby>かな です</p>
  <p class="pe-fix__good">✓ <ruby>静<rt>しず</rt></ruby>か<b>です</b> — kesim boʻlganda な <b>yoʻqoladi</b>. な faqat otdan oldin.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ きれいくないです</p>
  <p class="pe-fix__good">✓ きれい<b>ではありません</b> — きれい な-sifat, い bilan tugasa ham.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>は<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>好<rt>す</rt></ruby>きです</p>
  <p class="pe-fix__good">✓ <ruby>音楽<rt>おんがく</rt></ruby><b>が</b><ruby>好<rt>す</rt></ruby>きです — <ruby>好<rt>す</rt></ruby>き feʼl emas, <b>sifat</b>. を faqat feʼl bilan keladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>静<rt>しず</rt></ruby>かかったです</p>
  <p class="pe-fix__good">✓ <ruby>静<rt>しず</rt></ruby>か<b>でした</b> — な-sifat ot kabi tuslanadi, かった emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Jimjit sinf» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>静<rt>しず</rt></ruby><b>かな</b><ruby>教室<rt>きょうしつ</rt></ruby> — otdan oldin な qoʻshiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>静<rt>しず</rt></ruby>か ning oʻtgan zamoni qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>静<rt>しず</rt></ruby>かでした</b> — ot kabi. «かった» い-sifatlarniki.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. きれい qaysi turga tegishli?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>な-sifat</b>, い bilan tugasa ham. Chunki bu い soʻzning bir qismi, tuslanadigan qoʻshimcha emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Kesim boʻlganda な ga nima boʻladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻqoladi.</b> <ruby>静<rt>しず</rt></ruby>かです — な yoʻq. な faqat <b>otdan oldin</b> turganda paydo boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Menga koreys tili yoqadi» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>私<rt>わたし</rt></ruby>は<ruby>韓国語<rt>かんこくご</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです</b> — を emas, <b>が</b>. <ruby>好<rt>す</rt></ruby>き sifat, feʼl emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Ikki sifat turini bir jumlada taʼriflang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>い-sifat feʼl kabi</b> (oʻzi tuslanadi), <b>な-sifat ot kabi</b> (です unga zamon beradi).</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>静<rt>しず</rt></ruby>か</b> — jimjit</li>
  <li><b><ruby>元気<rt>げんき</rt></ruby></b> — tetik, sogʻlom</li>
  <li><b><ruby>有名<rt>ゆうめい</rt></ruby></b> — mashhur</li>
  <li><b><ruby>便利<rt>べんり</rt></ruby></b> — qulay</li>
  <li><b>きれい</b> — chiroyli, toza (な-sifat!)</li>
  <li><b><ruby>好<rt>す</rt></ruby>き</b> — yoqadigan</li>
  <li><b><ruby>嫌<rt>きら</rt></ruby>い</b> — yoqmaydigan (な-sifat!)</li>
  <li><b><ruby>大変<rt>たいへん</rt></ruby></b> — ogʻir, mushkul</li>
  <li><b><ruby>花<rt>はな</rt></ruby></b> — gul</li>
  <li><b>な</b> — な-sifatning aniqlovchi belgisi</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>な-sifat ot kabi tuslanadi</b>: ではありません, でした. Yangi qoida yoʻq.</li>
    <li><b>な faqat otdan oldin</b> paydo boʻladi; kesim boʻlganda yoʻqoladi.</li>
    <li>きれい, <ruby>有名<rt>ゆうめい</rt></ruby>, <ruby>嫌<rt>きら</rt></ruby>い — い bilan tugaydigan <b>な-sifatlar</b>. Yodlab qoʻying.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-27: Uchta feʼl guruhi — 五段, 一段, 不規則",
        "category": "japanese",
        "order": 27,
        "summary": (
            "Butun kursning kaliti. Bundan keyingi har bir feʼl shakli — て, た, "
            "ない, potensial — shu uchta guruhning qaysi biriga qarab yasaladi."
        ),
        "stories": ["がっこうの あさ"],
        "content": """
<h2>PJ-27: Uchta feʼl guruhi — <ruby>五段<rt>ごだん</rt></ruby>, <ruby>一段<rt>いちだん</rt></ruby>, <ruby>不規則<rt>ふきそく</rt></ruby></h2>

<p>Yigirma olti dars davomida feʼllarni tayyor holda oldingiz:
<ruby>読<rt>よ</rt></ruby>みます, <ruby>食<rt>た</rt></ruby>べます. Ular bitta
boʻlak boʻlib koʻrindi va buning zarari yoʻq edi.</p>

<p>Endi zarari boʻladi. Oldinda yigirmadan ortiq yangi feʼl shakli turibdi —
iltimos, taqiq, ruxsat, xohish — va ularning <b>hech biri</b> ます dan
yasalmaydi. Hammasi feʼlning asl shaklidan yasaladi, yasash yoʻli esa feʼl
qaysi <b>guruhga</b> tegishli ekaniga bogʻliq. Shuning uchun bu dars —
butun kursning kaliti.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Feʼlning lugʻat shaklini tanib olasiz</li>
    <li>Uchta guruhni ajratasiz</li>
    <li>Har bir guruhdan ます shaklini yasaysiz</li>
    <li>る bilan tugaydigan tuzoq feʼllarni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchta guruh, kamayib boradigan tartibda</span>
  <span class="pe-chip pe-chip--v">III — faqat 2 ta</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">II — る + い/え</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">I — qolgani</span>
</div>

<h3>1. Avval — lugʻat shakli</h3>

<p>Yapon lugʻatida feʼl <b>ます siz</b> yoziladi. Bu uning bezaksiz shakli va
u doim <b>う qatoridagi</b> bir tovush bilan tugaydi: う, く, ぐ, す, つ, ぬ,
ぶ, む, る.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat shakli</th><th>Siz bilgan shakl</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>みます</td><td class="pj-uz">oʻqimoq</td></tr>
  <tr><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-res"><ruby>食<rt>た</rt></ruby>べます</td><td class="pj-uz">yemoq</td></tr>
  <tr><td class="pj-stem">する</td><td class="pj-res">します</td><td class="pj-uz">qilmoq</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Bu shaklning nomi <b><ruby>辞書形<rt>じしょけい</rt></ruby></b> — «lugʻat
  shakli». Keyingi darsda uning oʻz vazifalarini koʻramiz; bugun u bizga
  bitta narsa uchun kerak: <b>guruh faqat shu shaklda koʻrinadi</b>.</p>
</div>

<h3>2. III guruh — <ruby>不規則<rt>ふきそく</rt></ruby>: bor-yoʻgʻi ikkita</h3>

<p>Eng kichigidan boshlaymiz. Butun yapon tilida <b>ikkita</b> tartibsiz feʼl
bor. Ikkitasi. Bugun yodlab qoʻysangiz, mavzu yopiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat</th><th>ます</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">する</td><td class="pj-res">します</td><td class="pj-uz">qilmoq</td></tr>
  <tr><td class="pj-stem"><ruby>来<rt>く</rt></ruby>る</td><td class="pj-res"><ruby>来<rt>き</rt></ruby>ます</td><td class="pj-uz">kelmoq</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b><ruby>来<rt>く</rt></ruby>る</b> ga diqqat: kanji oʻzgarmaydi, lekin
  <em>oʻqilishi</em> oʻzgaradi. Aynan shuning uchun har bir kanji furigana
  bilan yuradi — aks holda siz buni koʻrmagan boʻlar edingiz.</p>
</div>

<p>する ning qiymati kattaroq: u yuzlab otni feʼlga aylantiradi —
<ruby>勉強<rt>べんきょう</rt></ruby>する, <ruby>電話<rt>でんわ</rt></ruby>する.</p>

<h3>3. II guruh — <ruby>一段<rt>いちだん</rt></ruby>: る tushadi, xolos</h3>

<p>Bu guruh eng oson tuslanadigani. Belgisi ikkita va ikkalasi ham bir
vaqtda bajarilishi kerak: feʼl <b>る</b> bilan tugaydi, <b>va</b> る dan
oldingi tovush <b>い</b> yoki <b>え</b> qatoridan. ます yasash uchun る ni
olib tashlab, ます qoʻyasiz.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>る dan oldin</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-uz">べ — え qatori</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べます</td><td class="pj-uz">yemoq</td></tr>
  <tr><td><ruby>見<rt>み</rt></ruby>る</td><td class="pj-uz">み — い qatori</td>
      <td class="pj-res"><ruby>見<rt>み</rt></ruby>ます</td><td class="pj-uz">koʻrmoq</td></tr>
  <tr><td><ruby>起<rt>お</rt></ruby>きる</td><td class="pj-uz">き — い qatori</td>
      <td class="pj-res"><ruby>起<rt>お</rt></ruby>きます</td><td class="pj-uz">turmoq</td></tr>
  <tr><td><ruby>寝<rt>ね</rt></ruby>る</td><td class="pj-uz">ね — え qatori</td>
      <td class="pj-res"><ruby>寝<rt>ね</rt></ruby>ます</td><td class="pj-uz">uxlamoq</td></tr>
</table></div>

<h3>4. I guruh — <ruby>五段<rt>ごだん</rt></ruby>: qolganlarning hammasi</h3>

<p>Uchinchi va ikkinchi guruhga tushmagan har bir feʼl — birinchi guruhda.
Uning nomi «besh qator» degani, va mantiq shunda: oxirgi tovush
<ruby>五十音図<rt>ごじゅうおんず</rt></ruby> ning qatorlari boʻylab yuradi.
ます yasash uchun oxirgi tovushni <b>う qatoridan い qatoriga</b>
tushirasiz — Block A da yodlagan jadval mana shu yerda ishga tushadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Oxiri</th><th>い qatoriga</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-uz">む</td><td class="pj-end">み</td>
      <td class="pj-res"><ruby>読<rt>よ</rt></ruby>みます</td><td class="pj-uz">oʻqimoq</td></tr>
  <tr><td><ruby>書<rt>か</rt></ruby>く</td><td class="pj-uz">く</td><td class="pj-end">き</td>
      <td class="pj-res"><ruby>書<rt>か</rt></ruby>きます</td><td class="pj-uz">yozmoq</td></tr>
  <tr><td><ruby>話<rt>はな</rt></ruby>す</td><td class="pj-uz">す</td><td class="pj-end">し</td>
      <td class="pj-res"><ruby>話<rt>はな</rt></ruby>します</td><td class="pj-uz">gapirmoq</td></tr>
  <tr><td><ruby>待<rt>ま</rt></ruby>つ</td><td class="pj-uz">つ</td><td class="pj-end">ち</td>
      <td class="pj-res"><ruby>待<rt>ま</rt></ruby>ちます</td><td class="pj-uz">kutmoq</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>す → し va つ → ち ga eʼtibor bering.</b> Jadval boʻyicha «si» va «ti»
  chiqishi kerak edi, lekin yapon tilida bunday tovushlar yoʻq — PJ-3 da
  koʻrgansiz. Bu istisno emas: jadval aynan shunday tuzilgan.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>は<ruby>毎朝<rt>まいあさ</rt></ruby><ruby>新聞<rt>しんぶん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます。<ruby>妹<rt>いもうと</rt></ruby>は<ruby>手紙<rt>てがみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>きます。</p>
  <p class="pe-ex__rom">watashi wa maiasa shinbun o yomimasu. imōto wa tegami o kakimasu</p>
  <p class="pe-ex__uz">Men har kuni ertalab gazeta oʻqiyman. Singlim xat yozadi.</p>
  <p class="pe-ex__why">Ikkalasi ham I guruh: む → み, く → き. Bitta qoida, ikkita feʼl.</p>
</div>

<h3>5. Tuzoq: る bilan tugagan har bir feʼl II guruhda emas</h3>

<p>Mana darsning yagona qiyin joyi. Agar る dan oldin <b>あ, う</b> yoki
<b>お</b> tursa, feʼl albatta I guruhda — <ruby>作<rt>つく</rt></ruby>る,
<ruby>乗<rt>の</rt></ruby>る. Haqiqiy tuzoq boshqasi: baʼzi feʼllarda る dan
oldin い yoki え turadi, yaʼni ular II guruhga oʻxshaydi — <em>lekin aslida
I guruhda</em>. Ularni yodlashdan boshqa yoʻl yoʻq, va ular koʻp emas.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Koʻrinishi</th><th>Aslida</th><th>ます</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>帰<rt>かえ</rt></ruby>る</td><td class="pj-uz">え + る</td>
      <td class="pj-end">I guruh</td><td class="pj-res"><ruby>帰<rt>かえ</rt></ruby>ります</td><td class="pj-uz">qaytmoq</td></tr>
  <tr><td><ruby>入<rt>はい</rt></ruby>る</td><td class="pj-uz">い + る</td>
      <td class="pj-end">I guruh</td><td class="pj-res"><ruby>入<rt>はい</rt></ruby>ります</td><td class="pj-uz">kirmoq</td></tr>
  <tr><td><ruby>走<rt>はし</rt></ruby>る</td><td class="pj-uz">し + る</td>
      <td class="pj-end">I guruh</td><td class="pj-res"><ruby>走<rt>はし</rt></ruby>ります</td><td class="pj-uz">yugurmoq</td></tr>
  <tr><td><ruby>知<rt>し</rt></ruby>る</td><td class="pj-uz">し + る</td>
      <td class="pj-end">I guruh</td><td class="pj-res"><ruby>知<rt>し</rt></ruby>ります</td><td class="pj-uz">bilmoq</td></tr>
  <tr><td><ruby>切<rt>き</rt></ruby>る</td><td class="pj-uz">き + る</td>
      <td class="pj-end">I guruh</td><td class="pj-res"><ruby>切<rt>き</rt></ruby>ります</td><td class="pj-uz">kesmoq</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Farqni ります dan koʻrasiz.</b> II guruhda boʻlganda edi,
  <ruby>帰<rt>かえ</rt></ruby>る dan «かえます» chiqar edi. Chiqmaydi:
  <ruby>帰<rt>かえ</rt></ruby><b>り</b>ます. Shuning uchun yangi feʼlni
  <b>ikkita shaklda birga yodlang</b> — lugʻat shakli va ます shakli. Shunda
  guruh oʻz-oʻzidan koʻrinib turadi.</p>
</div>

<h3>6. Qaror zinapoyasi</h3>

<p>Notanish feʼl uchraganda shu uch savolni <b>shu tartibda</b> bering.</p>

<div class="pe-steps">
  <p><b>1.</b> Bu する yoki <ruby>来<rt>く</rt></ruby>る mi? → III guruh.</p>
  <p><b>2.</b> る bilan tugaydimi va oldida い yoki え bormi? → II guruh — tuzoq roʻyxatidagi beshtasidan boʻlmasa.</p>
  <p><b>3.</b> Qolgani → I guruh.</p>
</div>

<div class="pj-group">
  <div class="pj-group__c">
    <p class="pj-group__h">I — <ruby>五段<rt>ごだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>読<rt>よ</rt></ruby>む → <ruby>読<rt>よ</rt></ruby>みます</p>
    <p>Oxirgi tovush い qatoriga tushadi.</p>
  </div>
  <div class="pj-group__c pj-group__c--2">
    <p class="pj-group__h">II — <ruby>一段<rt>いちだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>食<rt>た</rt></ruby>べる → <ruby>食<rt>た</rt></ruby>べます</p>
    <p>る tushadi, ます qoʻyiladi.</p>
  </div>
  <div class="pj-group__c pj-group__c--3">
    <p class="pj-group__h">III — <ruby>不規則<rt>ふきそく</rt></ruby></p>
    <p class="pj-group__ex">する · <ruby>来<rt>く</rt></ruby>る</p>
    <p>Faqat ikkita. Yodlab qoʻying.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham feʼllar tuslanishda bir xil tutmaydi</b> — «oʻqi-di»
  va «ye-di» oʻzagi bilan boshqacha. Farqi shundaki, oʻzbek oʻquvchi buni
  <em>eshitib</em> biladi. Yapon tilida ham oxir-oqibat shunday boʻladi;
  hozircha guruhni ongli tekshirib turing — bu vaqtinchalik ish.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>六時<rt>ろくじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます。<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。<ruby>五時<rt>ごじ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ります。</p>
  <p class="pe-ex__rom">rokuji ni okimasu. gakkō e ikimasu. goji ni kaerimasu</p>
  <p class="pe-ex__uz">Soat oltida turaman. Maktabga boraman. Soat beshda qaytaman.</p>
  <p class="pe-ex__why">Uchta feʼl, uchta hikoya: <ruby>起<rt>お</rt></ruby>きる — II guruh, <ruby>行<rt>い</rt></ruby>く — I guruh, <ruby>帰<rt>かえ</rt></ruby>る — tuzoq feʼl, I guruh.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>帰<rt>かえ</rt></ruby>ます</p>
  <p class="pe-fix__good">✓ <ruby>帰<rt>かえ</rt></ruby><b>り</b>ます — beshta tuzoq feʼlning eng koʻp uchraydigani: koʻrinishi II, aslida <b>I guruh</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>話<rt>はな</rt></ruby>すます</p>
  <p class="pe-fix__good">✓ <ruby>話<rt>はな</rt></ruby><b>し</b>ます — I guruhda oxirgi tovush <b>oʻzgaradi</b>, ます shunchaki qoʻshilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>来<rt>く</rt></ruby>ます</p>
  <p class="pe-fix__good">✓ <ruby>来<rt>き</rt></ruby>ます — kanji oʻsha, <b>oʻqilishi</b> oʻzgardi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>飲<rt>の</rt></ruby>む qaysi guruhda va ます shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>I guruh</b> — <ruby>飲<rt>の</rt></ruby>みます. む → み, う qatoridan い qatoriga.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>見<rt>み</rt></ruby>る qaysi guruhda?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>II guruh</b> — る dan oldin <b>み</b> (い qatori). る tushadi: <ruby>見<rt>み</rt></ruby>ます.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>入<rt>はい</rt></ruby>る ning ます shakli «はいます» mi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> <ruby>入<rt>はい</rt></ruby><b>り</b>ます — beshta tuzoq feʼldan biri.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Butun yapon tilida nechta tartibsiz feʼl bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Ikkita:</b> する va <ruby>来<rt>く</rt></ruby>る.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>待<rt>ま</rt></ruby>つ dan ます yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>待<rt>ま</rt></ruby>ちます</b>. つ → <b>ち</b>, chunki yapon tilida «ti» tovushi yoʻq.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>辞書形<rt>じしょけい</rt></ruby></b> — lugʻat shakli</li>
  <li><b><ruby>五段<rt>ごだん</rt></ruby></b> — I guruh</li>
  <li><b><ruby>一段<rt>いちだん</rt></ruby></b> — II guruh</li>
  <li><b><ruby>不規則<rt>ふきそく</rt></ruby></b> — III guruh, tartibsiz</li>
  <li><b><ruby>起<rt>お</rt></ruby>きる</b> — turmoq</li>
  <li><b><ruby>寝<rt>ね</rt></ruby>る</b> — uxlamoq</li>
  <li><b><ruby>帰<rt>かえ</rt></ruby>る</b> — qaytmoq (I guruh!)</li>
  <li><b><ruby>入<rt>はい</rt></ruby>る</b> — kirmoq (I guruh!)</li>
  <li><b><ruby>待<rt>ま</rt></ruby>つ</b> — kutmoq</li>
  <li><b><ruby>買<rt>か</rt></ruby>う</b> — sotib olmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Guruh <b>lugʻat shaklida</b> koʻrinadi, ます shaklida emas.</li>
    <li>Zinapoya: する/<ruby>来<rt>く</rt></ruby>る → III · る + い/え → II · qolgani → I.</li>
    <li><ruby>帰<rt>かえ</rt></ruby>る, <ruby>入<rt>はい</rt></ruby>る, <ruby>走<rt>はし</rt></ruby>る, <ruby>知<rt>し</rt></ruby>る, <ruby>切<rt>き</rt></ruby>る — II ga oʻxshagan <b>I guruh</b> feʼllari.</li>
  </ul>
</div>
""",
    },
]
