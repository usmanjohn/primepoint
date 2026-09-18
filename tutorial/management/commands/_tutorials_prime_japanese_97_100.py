# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-97 … PJ-100: KURSNING OXIRGI BLOKI.

Toʻrtta dars, chunki kurs shu yerda tugaydi (odatdagi batch — uchta).
    PJ-97  — xat, elektron xat va rasmiy murojaat. PJ-96 registrni
             berdi; bu dars oʻsha registrni QOLIPGA soladi. 拝啓 va
             敬具 — juftlik; birini yozib ikkinchisini unutish bu
             darsning eng koʻp uchraydigan xatosi.
    PJ-98  — 四字熟語 va ことわざ. Kursning eng kuchli oʻzbek
             levercha darsi: maqollar deyarli bittama-bitta mos
             tushadi (一石二鳥 = «bir oʻq bilan ikki quyon»).
    PJ-99  — 和語・漢語・外来語. Lugʻatning uch qatlami, va oʻzbek
             tilida ham AYNAN uchta qatlam bor: turkiy / arab-fors /
             rus-yevropa. yigʻilish · majlis · miting =
             集まり · 集会 · ミーティング. Bu — butun kursning eng
             aniq koʻprigi.
    PJ-100 — yoʻl xaritasi. Yangi grammatika yoʻq: nima qoʻlga
             kirdi, N3 va N2 gacha nima bor, va kundalik odat.

⚠️ PJ-97 da ikkita juftlikni aralashtirmaslik kerak:
拝啓…敬具 (toʻliq xat) va 前略…草々 (qisqa xat, mavsum salomi yoʻq).
Va elektron xatda 拝啓 YOZILMAYDI — u qogʻoz xatning qolipi.

⚠️ PJ-98 da 四字熟語 butunlay ON'YOMI bilan oʻqiladi, lekin
oʻqilishlari yodlanadi: 一期一会 = いちごいちえ.

⚠️ PJ-99 ning kaliti PJ-11 da allaqachon berilgan: KUN'YOMI → 和語,
ON'YOMI → 漢語, katakana → 外来語. Oʻquvchida asbob bor, u faqat
buni bilmaydi. 和製英語 (コンセント, マンション, サラリーマン) —
alohida tuzoq: bular ingliz soʻzlari EMAS.

⚠️ PJ-100 da hech qanday oʻylab topilgan sana, narx yoki markaz nomi
yoʻq — imtihonning TUZILISHI aytiladi, tafsilotlar uchun oʻquvchi
rasmiy manbaga yuboriladi (SAT olami shelfidagi qoidaning aynan
oʻzi).

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_97_100.py --author=prime
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
        "title": "PJ-97: Xat, elektron xat va rasmiy murojaat qoliplari",
        "category": "japanese",
        "order": 97,
        "summary": (
            "Qogʻoz xat, elektron xat va oddiy xabar — uchta boshqa "
            "qolip. 拝啓 va 敬具 juftligi, mavsum salomi, "
            "お世話になっております va よろしくお願いいたします."
        ),
        "stories": ["せんせいへの てがみ"],
        "content": """
<h2>PJ-97: Xat, elektron xat va rasmiy murojaat qoliplari</h2>

<p>Yapon tilida xat yozish — ijod emas, <b>qolipni toʻldirish</b>.
Boshi, salomi, oxiri va imzosi oldindan belgilangan; siz faqat
oʻrtadagi gapni yozasiz. Bu qoʻrqinchli eshitiladi, lekin aslida
bu — sovgʻa: qolipni bir marta yodlab olsangiz, umringiz oxirigacha
xat yozishdan qoʻrqmaysiz.</p>

<p>PJ-96 sizga <em>registr</em>ni berdi. Bu dars oʻsha registrni
<em>qolipga</em> soladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b><ruby>拝啓<rt>はいけい</rt></ruby> … <ruby>敬具<rt>けいぐ</rt></ruby></b> juftligi bilan toʻliq xat yozasiz</li>
    <li>Mavsum salomini (<b><ruby>時候<rt>じこう</rt></ruby>の<ruby>挨拶<rt>あいさつ</rt></ruby></b>) toʻgʻri joyga qoʻyasiz</li>
    <li>Elektron xatni <b>お<ruby>世話<rt>せわ</rt></ruby>になっております</b> bilan boshlaysiz</li>
    <li><b><ruby>様<rt>さま</rt></ruby></b>, <b><ruby>先生<rt>せんせい</rt></ruby></b>, <b><ruby>各位<rt>かくい</rt></ruby></b> ni adashtirmay ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻliq xatning skeleti</span>
  <span class="pe-chip pe-chip--s"><ruby>拝啓<rt>はいけい</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">mavsum salomi</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">asosiy gap</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--opt"><ruby>敬具<rt>けいぐ</rt></ruby></span>
</div>

<h3>1. Uchta xat, uchta dunyo</h3>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name"><ruby>手紙<rt>てがみ</rt></ruby></span>
    <span class="pj-level__ja"><ruby>拝啓<rt>はいけい</rt></ruby> … <ruby>敬具<rt>けいぐ</rt></ruby></span>
    <span class="pj-level__who">qogʻoz xat — rasmiy murojaat, minnatdorchilik, iltimos</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name">メール</span>
    <span class="pj-level__ja">お<ruby>世話<rt>せわ</rt></ruby>になっております</span>
    <span class="pj-level__who">elektron xat — ish, maktab, tashkilot</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">メッセージ</span>
    <span class="pj-level__ja">おつかれ！<ruby>今<rt>いま</rt></ruby>いい？</span>
    <span class="pj-level__who">doʻstga xabar — qolip yoʻq, oddiy shakl</span>
  </div>
</div>

<div class="pe-call pe-warn">
  <p><b>Eng koʻp uchraydigan xato shu yerda tugʻiladi:</b> elektron
  xatni <b><ruby>拝啓<rt>はいけい</rt></ruby></b> bilan boshlash. <ruby>拝啓<rt>はいけい</rt></ruby>
  — <em>qogʻoz</em> xatning qolipi. Elektron xatda u gʻalati, hatto
  kulgili chiqadi — xuddi telefonda SMS yozib, boshiga «Hurmatli
  janoblar!» deb qoʻygandek. Elektron xat
  <b>お<ruby>世話<rt>せわ</rt></ruby>になっております</b> bilan
  boshlanadi, xolos.</p>
</div>

<h3>2. <ruby>拝啓<rt>はいけい</rt></ruby> va <ruby>敬具<rt>けいぐ</rt></ruby> — juftlik</h3>

<p>Xatning boshidagi soʻz <b><ruby>頭語<rt>とうご</rt></ruby></b>,
oxiridagisi <b><ruby>結語<rt>けつご</rt></ruby></b> deyiladi. Ular
<b>juftlik</b>: birini yozsangiz, ikkinchisi majburiy.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th><ruby>頭語<rt>とうご</rt></ruby></th><th><ruby>結語<rt>けつご</rt></ruby></th><th>Qachon</th></tr>
  <tr><td class="pj-stem"><ruby>拝啓<rt>はいけい</rt></ruby></td>
      <td class="pj-res"><ruby>敬具<rt>けいぐ</rt></ruby></td>
      <td class="pj-uz">odatdagi toʻliq xat — mavsum salomi bilan</td></tr>
  <tr><td class="pj-stem"><ruby>前略<rt>ぜんりゃく</rt></ruby></td>
      <td class="pj-res"><ruby>草々<rt>そうそう</rt></ruby></td>
      <td class="pj-uz">qisqa xat — «salomni qoldirdim» degani</td></tr>
  <tr><td class="pj-stem"><ruby>謹啓<rt>きんけい</rt></ruby></td>
      <td class="pj-res"><ruby>謹言<rt>きんげん</rt></ruby></td>
      <td class="pj-uz">ayniqsa hurmatli — rasmiy tashkilotga</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b><ruby>前略<rt>ぜんりゃく</rt></ruby> soʻzma-soʻz «oldingisini
  qisqartirdim» degani</b> — yaʼni «mavsum salomini yozmayapman,
  toʻgʻridan-toʻgʻri ishga oʻtaman». Shuning uchun undan keyin
  mavsum salomi yozilsa, xat oʻz-oʻziga qarshi chiqadi. Qolipni
  tanladingizmi — oxirigacha oʻshanisida qoling.</p>
</div>

<h3>3. Mavsum salomi — <ruby>時候<rt>じこう</rt></ruby>の<ruby>挨拶<rt>あいさつ</rt></ruby></h3>

<p>Toʻliq xat havodan boshlanadi. Bu gʻalati tuyuladi, lekin
yapon xatining eng qadimiy qismi shu.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>拝啓<rt>はいけい</rt></ruby>　<span class="pe-hl pe-hl--adv"><ruby>桜<rt>さくら</rt></ruby>の<ruby>花<rt>はな</rt></ruby>が<ruby>美<rt>うつく</rt></ruby>しい<ruby>季節<rt>きせつ</rt></ruby>となりました</span>。<ruby>先生<rt>せんせい</rt></ruby>はお<ruby>元気<rt>げんき</rt></ruby>でいらっしゃいますか。</p>
  <p class="pe-ex__uz">Hurmatli ustoz! Gilos gullari chiroyli boʻlgan fasl keldi. Siz yaxshimisiz?</p>
  <p class="pe-ex__why">Ikki qadam: avval <b>mavsum</b>, keyin <b>odamning ahvoli</b>. いらっしゃいます — PJ-69 dagi <ruby>尊敬語<rt>そんけいご</rt></ruby>.</p>
</div>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><ruby>春<rt>はる</rt></ruby></p>
    <p><ruby>桜<rt>さくら</rt></ruby>の<ruby>花<rt>はな</rt></ruby>が<ruby>美<rt>うつく</rt></ruby>しい<ruby>季節<rt>きせつ</rt></ruby>となりました。</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><ruby>夏<rt>なつ</rt></ruby></p>
    <p><ruby>暑<rt>あつ</rt></ruby>い<ruby>日<rt>ひ</rt></ruby>が<ruby>続<rt>つづ</rt></ruby>いております。</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><ruby>秋<rt>あき</rt></ruby></p>
    <p><ruby>朝<rt>あさ</rt></ruby><ruby>晩<rt>ばん</rt></ruby><ruby>涼<rt>すず</rt></ruby>しくなってまいりました。</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><ruby>冬<rt>ふゆ</rt></ruby></p>
    <p><ruby>寒<rt>さむ</rt></ruby>さが<ruby>厳<rt>きび</rt></ruby>しくなってきました。</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek xati ham aynan shunday boshlanadi, faqat biz havo
  emas, odamdan boshlaymiz.</b> «Assalomu alaykum, hurmatli
  ustoz! Avvalambor sizdan hol-ahvol soʻrayman, oilangiz
  sogʻ-omonmi?» — bu oʻzbekcha
  <ruby>時候<rt>じこう</rt></ruby>の<ruby>挨拶<rt>あいさつ</rt></ruby>ning
  aynan oʻzi: <em>ishga oʻtishdan oldin majburiy iliq qism</em>.
  Farqi bitta va uni eslab qolish oson: <b>oʻzbek xati odamdan,
  yapon xati fasldan boshlanadi.</b> Ikkalasida ham bu qismni
  tashlab ketish qoʻpollik hisoblanadi, ikkalasida ham u deyarli
  tayyor jumla — oʻylab topish shart emas, yodlab qoʻyish
  kifoya.</p>
</div>

<h3>4. Elektron xat — eng kerakli qolip</h3>

<p>Amalda siz qogʻoz xatdan koʻra <b>yuz marta koʻproq</b> elektron
xat yozasiz. Uning tuzilishi qatʼiy, lekin qisqa:</p>

<div class="pe-steps">
  <ol>
    <li><b>Kimga</b> — <ruby>田中<rt>たなか</rt></ruby><ruby>先生<rt>せんせい</rt></ruby>／<ruby>山田<rt>やまだ</rt></ruby><ruby>様<rt>さま</rt></ruby></li>
    <li><b>Salom</b> — いつもお<ruby>世話<rt>せわ</rt></ruby>になっております。</li>
    <li><b>Oʻzingizni tanishtirish</b> — <ruby>二年生<rt>にねんせい</rt></ruby>のイノムと<ruby>申<rt>もう</rt></ruby>します。</li>
    <li><b>Asosiy gap</b> — bitta xatda bitta ish, uzunligi uch-toʻrt jumla.</li>
    <li><b>Yopish</b> — よろしくお<ruby>願<rt>ねが</rt></ruby>いいたします。</li>
    <li><b>Imzo</b> — ism, sinf yoki tashkilot, aloqa.</li>
  </ol>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>田中<rt>たなか</rt></ruby><ruby>先生<rt>せんせい</rt></ruby><br>いつも<span class="pe-hl pe-hl--s">お<ruby>世話<rt>せわ</rt></ruby>になっております</span>。<ruby>二年生<rt>にねんせい</rt></ruby>のイノムと<ruby>申<rt>もう</rt></ruby>します。<br><ruby>来週<rt>らいしゅう</rt></ruby>の<ruby>発表<rt>はっぴょう</rt></ruby>について<ruby>伺<rt>うかが</rt></ruby>いたいことがございます。<ruby>資料<rt>しりょう</rt></ruby>は<ruby>何<rt>なん</rt></ruby>ページまででしょうか。<br><ruby>お忙<rt>おいそが</rt></ruby>しいところ<ruby>恐<rt>おそ</rt></ruby>れ<ruby>入<rt>い</rt></ruby>りますが、<span class="pe-hl pe-hl--v">よろしくお<ruby>願<rt>ねが</rt></ruby>いいたします</span>。</p>
  <p class="pe-ex__uz">Tanaka ustoz! Doim gʻamxoʻrligingiz uchun rahmat. Men ikkinchi kurs talabasi Inomman. Keyingi haftadagi taqdimot haqida soʻramoqchi edim: material necha betgacha? Bandligingizda bezovta qilganim uchun uzr, iltimosimni eʼtiborga olsangiz.</p>
  <p class="pe-ex__why">Uchta qolip: <b>お<ruby>世話<rt>せわ</rt></ruby>になっております</b> (salom), <b>〜と<ruby>申<rt>もう</rt></ruby>します</b> (tanishtirish), <b>よろしくお<ruby>願<rt>ねが</rt></ruby>いいたします</b> (yopish). Oʻrtadagi ikki jumla — sizning oʻz gapingiz.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Ikkita soʻzni hozir yodlab qoʻying, ular butun umr
  ishlaydi.</b> <b>お<ruby>世話<rt>せわ</rt></ruby>になっております</b> —
  soʻzma-soʻz «gʻamxoʻrligingizda boʻlib turibman», lekin
  amalda bu shunchaki «Assalomu alaykum» ning ish varianti.
  <b>よろしくお<ruby>願<rt>ねが</rt></ruby>いいたします</b> — «iltimosimni
  eʼtiborga oling», va u har qanday xatni yopadi. Yaponiyada
  yoziladigan har uchinchi elektron xat shu ikkovi bilan
  boshlanib, shu ikkovi bilan tugaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>前略<rt>ぜんりゃく</rt></ruby>　さっそくですが、<ruby>来月<rt>らいげつ</rt></ruby>の<ruby>件<rt>けん</rt></ruby>についてご<ruby>連絡<rt>れんらく</rt></ruby>いたします。<br>… <ruby>草々<rt>そうそう</rt></ruby></p>
  <p class="pe-ex__uz">Salomni qoldiraman. Darrov maqsadga oʻtaman: kelasi oydagi masala yuzasidan xabar bermoqchiman. … Qisqacha, shu.</p>
  <p class="pe-ex__why">Qisqa xatning butun skeleti shu: <b><ruby>前略<rt>ぜんりゃく</rt></ruby></b> → さっそくですが → gap → <b><ruby>草々<rt>そうそう</rt></ruby></b>. Mavsum salomi yoʻq, va aynan shuning uchun bu juftlik tanlangan.</p>
</div>

<h3>5. <ruby>様<rt>さま</rt></ruby>, <ruby>先生<rt>せんせい</rt></ruby>, <ruby>各位<rt>かくい</rt></ruby> — ismdan keyin nima turadi</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h"><ruby>様<rt>さま</rt></ruby> — umumiy</p>
    <p><ruby>山田<rt>やまだ</rt></ruby><ruby>様<rt>さま</rt></ruby></p>
    <p>Mijoz, notanish odam, tashkilot xodimi. Eng xavfsiz tanlov.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h"><ruby>先生<rt>せんせい</rt></ruby> — kasb</p>
    <p><ruby>田中<rt>たなか</rt></ruby><ruby>先生<rt>せんせい</rt></ruby></p>
    <p>Oʻqituvchi, shifokor, yurist. <b><ruby>様<rt>さま</rt></ruby></b> qoʻshilmaydi.</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b><ruby>田中<rt>たなか</rt></ruby><ruby>先生<rt>せんせい</rt></ruby><ruby>様<rt>さま</rt></ruby>
  — xato.</b> <ruby>先生<rt>せんせい</rt></ruby> ning oʻzi allaqachon
  hurmat belgisi, shuning uchun uning ustiga
  <ruby>様<rt>さま</rt></ruby> qoʻyish ikki marta hurmat qilish
  boʻladi — yaponchada bu hurmatli emas, <em>savodsiz</em>
  koʻrinadi. Xuddi shunday
  <ruby>各位<rt>かくい</rt></ruby> («hurmatli hammangiz», guruhga
  murojaat) ham yolgʻiz turadi:
  <ruby>各位<rt>かくい</rt></ruby><ruby>様<rt>さま</rt></ruby> deb
  yozilmaydi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">拝</span>
    <span class="pj-kanji__uz">taʼzim qilmoq, hurmat bilan</span>
    <span class="pj-kanji__on">オン: ハイ</span>
    <span class="pj-kanji__kun">KUN: おが(む)</span>
    <span class="pj-kanji__note">拝啓 (はいけい) — xat boshi · 拝見する (はいけんする) — koʻrmoq (kamtarona)</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">敬</span>
    <span class="pj-kanji__uz">hurmat</span>
    <span class="pj-kanji__on">オン: ケイ</span>
    <span class="pj-kanji__kun">KUN: うやま(う)</span>
    <span class="pj-kanji__note">敬具 (けいぐ) — xat oxiri · 尊敬語 (そんけいご)</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">申</span>
    <span class="pj-kanji__uz">aytmoq (kamtarona)</span>
    <span class="pj-kanji__on">オン: シン</span>
    <span class="pj-kanji__kun">KUN: もう(す)</span>
    <span class="pj-kanji__note">申します (もうします) — deyman · 申し込む (もうしこむ) — ariza bermoq</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu darsning eng foydali fikri qoliplar haqida emas, balki
  qoliplarning <em>sababi</em> haqida.</b> Oʻzbekchada ham
  «Hurmatli …», «Hurmat bilan», «Sizga tashakkur bildiramiz»
  degan tayyor jumlalar bor, va biz ularni oʻylab topmaymiz —
  yodlab olganmiz. Yapon tili shu narsani shunchaki
  <em>koʻproq</em> qilgan: tayyor jumlalar soni koʻp, va ular
  qatʼiyroq. Demak xat yozish yapon tilida <b>oson</b>, qiyin
  emas — chunki ijod talab qilinmaydi. Sizdan faqat bitta narsa
  soʻraladi: qaysi qolipni tanlaganingizni eslab qolish va
  oxirigacha oʻshanisida qolish.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham murojaat soʻzi ikki marta takrorlanmaydi,
  va siz buni allaqachon his qilasiz.</b> «Hurmatli Karimov
  domla» deymiz — «hurmatli domla janoblari» emas. «Domla» ning
  oʻzida hurmat bor, ustiga yana bittasini qoʻyish gapni
  hurmatli emas, <em>gʻaliz</em> qiladi. Yaponchadagi
  <ruby>田中<rt>たなか</rt></ruby><ruby>先生<rt>せんせい</rt></ruby><ruby>様<rt>さま</rt></ruby>
  ham aynan shu: qoida yangi emas, faqat belgilari boshqa.
  Shuning uchun bu joyda qoidani yodlash shart emas — oʻzbekcha
  quloq bilan tekshiring: «ikki marta hurmat qildimmi?»</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>拝啓<rt>はいけい</rt></ruby> … <ruby>草々<rt>そうそう</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>拝啓<rt>はいけい</rt></ruby> … <b><ruby>敬具<rt>けいぐ</rt></ruby></b> — juftlik buzilmaydi. <ruby>草々<rt>そうそう</rt></ruby> faqat <ruby>前略<rt>ぜんりゃく</rt></ruby> bilan keladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ (elektron xat) <ruby>拝啓<rt>はいけい</rt></ruby>　いつもお<ruby>世話<rt>せわ</rt></ruby>になっております</p>
  <p class="pe-fix__good">✓ いつもお<ruby>世話<rt>せわ</rt></ruby>になっております — elektron xatda <ruby>頭語<rt>とうご</rt></ruby> yozilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>田中<rt>たなか</rt></ruby><ruby>先生<rt>せんせい</rt></ruby><ruby>様<rt>さま</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>田中<rt>たなか</rt></ruby><ruby>先生<rt>せんせい</rt></ruby> — <ruby>先生<rt>せんせい</rt></ruby> ning oʻzi hurmat belgisi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>前略<rt>ぜんりゃく</rt></ruby>　<ruby>桜<rt>さくら</rt></ruby>の<ruby>花<rt>はな</rt></ruby>が<ruby>美<rt>うつく</rt></ruby>しい<ruby>季節<rt>きせつ</rt></ruby>となりました</p>
  <p class="pe-fix__good">✓ <ruby>前略<rt>ぜんりゃく</rt></ruby>　さっそくですが… — <ruby>前略<rt>ぜんりゃく</rt></ruby> «salomni qoldirdim» degani, keyin salom yozilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ よろしくお<ruby>願<rt>ねが</rt></ruby>い<b>します</b> (ustozga yozilgan rasmiy xatda)</p>
  <p class="pe-fix__good">✓ よろしくお<ruby>願<rt>ねが</rt></ruby>い<b>いたします</b> — いたします — PJ-70 dagi <ruby>謙譲語<rt>けんじょうご</rt></ruby>, rasmiy xatning darajasi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>拝啓<rt>はいけい</rt></ruby> bilan boshlangan xat nima bilan tugaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>敬具<rt>けいぐ</rt></ruby></b>. Bu juftlik: <ruby>頭語<rt>とうご</rt></ruby> va <ruby>結語<rt>けつご</rt></ruby> doim birga yuradi. <ruby>草々<rt>そうそう</rt></ruby> boshqa juftlikka — <ruby>前略<rt>ぜんりゃく</rt></ruby> ga tegishli.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Elektron xat qanday boshlanadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>いつもお<ruby>世話<rt>せわ</rt></ruby>になっております</b>. <ruby>拝啓<rt>はいけい</rt></ruby> va mavsum salomi — qogʻoz xatniki; elektron xatda ular yozilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>前略<rt>ぜんりゃく</rt></ruby> nimani anglatadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>«Oldingi qismini qoldirdim»</b> — yaʼni mavsum salomi yozilmaydi. Shuning uchun undan keyin darrov ishga oʻtiladi, va xat <b><ruby>草々<rt>そうそう</rt></ruby></b> bilan yopiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>田中<rt>たなか</rt></ruby><ruby>先生<rt>せんせい</rt></ruby><ruby>様<rt>さま</rt></ruby> — nimasi xato?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Ikki marta hurmat.</b> <ruby>先生<rt>せんせい</rt></ruby> ning oʻzi hurmat belgisi, ustiga <ruby>様<rt>さま</rt></ruby> qoʻyilmaydi. Toʻgʻrisi — <b><ruby>田中<rt>たなか</rt></ruby><ruby>先生<rt>せんせい</rt></ruby></b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Men ikkinchi kurs talabasi Inomman» — rasmiy xatda?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>二年生<rt>にねんせい</rt></ruby>のイノムと<ruby>申<rt>もう</rt></ruby>します</b>. Xatda oʻzini tanishtirish uchun <b>〜と<ruby>申<rt>もう</rt></ruby>します</b> ishlatiladi — です emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Elektron xat nima bilan yopiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>よろしくお<ruby>願<rt>ねが</rt></ruby>いいたします</b>. Rasmiy darajada <b>いたします</b>, oddiyroq holatda <b>します</b>. <ruby>敬具<rt>けいぐ</rt></ruby> bu yerda kerak emas.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>拝啓<rt>はいけい</rt></ruby> … <ruby>敬具<rt>けいぐ</rt></ruby></b> — xat boshi va oxiri</li>
  <li><b><ruby>前略<rt>ぜんりゃく</rt></ruby> … <ruby>草々<rt>そうそう</rt></ruby></b> — qisqa xatning juftligi</li>
  <li><b><ruby>時候<rt>じこう</rt></ruby>の<ruby>挨拶<rt>あいさつ</rt></ruby></b> — mavsum salomi</li>
  <li><b>お<ruby>世話<rt>せわ</rt></ruby>になっております</b> — elektron xatning salomi</li>
  <li><b>よろしくお<ruby>願<rt>ねが</rt></ruby>いいたします</b> — xatning yopilishi</li>
  <li><b>〜と<ruby>申<rt>もう</rt></ruby>します</b> — men … man (kamtarona)</li>
  <li><b><ruby>様<rt>さま</rt></ruby></b> — ismdan keyingi umumiy hurmat</li>
  <li><b><ruby>各位<rt>かくい</rt></ruby></b> — hurmatli hammangiz (guruhga)</li>
  <li><b><ruby>伺<rt>うかが</rt></ruby>う</b> — soʻramoq, bormoq (kamtarona)</li>
  <li><b><ruby>恐<rt>おそ</rt></ruby>れ<ruby>入<rt>い</rt></ruby>りますが</b> — bezovta qilganim uchun uzr</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b><ruby>頭語<rt>とうご</rt></ruby> va <ruby>結語<rt>けつご</rt></ruby> — juftlik.</b> <ruby>拝啓<rt>はいけい</rt></ruby> ↔ <ruby>敬具<rt>けいぐ</rt></ruby>, <ruby>前略<rt>ぜんりゃく</rt></ruby> ↔ <ruby>草々<rt>そうそう</rt></ruby>.</li>
    <li>Elektron xatda <ruby>拝啓<rt>はいけい</rt></ruby> yoʻq — <b>お<ruby>世話<rt>せわ</rt></ruby>になっております</b> bor.</li>
    <li><ruby>先生<rt>せんせい</rt></ruby> va <ruby>各位<rt>かくい</rt></ruby> ga <ruby>様<rt>さま</rt></ruby> qoʻshilmaydi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-98: 四字熟語 va ことわざ — toʻrt belgili iboralar va maqollar",
        "category": "japanese",
        "order": 98,
        "summary": (
            "Toʻrtta kanjiga sigʻgan butun bir fikr (一石二鳥) va xalq "
            "maqollari (石の上にも三年). Koʻpchiligining oʻzbekcha jufti "
            "bor — shuning uchun bu dars yodlash emas, tanish darsi."
        ),
        "stories": ["いしの うえにも さんねん"],
        "content": """
<h2>PJ-98: <ruby>四字熟語<rt>よじじゅくご</rt></ruby> va ことわざ — toʻrt belgili iboralar va maqollar</h2>

<p>Yaponcha matnda toʻsatdan toʻrtta kanji yonma-yon turadi va
lugʻat ularni alohida-alohida tarjima qiladi: «bir · tosh · ikki ·
qush». Hech nima tushunilmaydi. Keyin oʻzbekcha jufti esga tushadi —
<b>«bir oʻq bilan ikki quyon»</b> — va hammasi joyiga tushadi.</p>

<p>Bu darsning yaxshi xabari shu: siz bu iboralarning koʻpini
<em>allaqachon bilasiz</em>. Faqat oʻzbekcha bilasiz. Qilinadigan
ish — yodlash emas, <b>ulash</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b><ruby>四字熟語<rt>よじじゅくご</rt></ruby></b> nima ekanini va qanday oʻqilishini bilasiz</li>
    <li>Sakkizta eng koʻp uchraydiganini oʻzbekcha jufti bilan yodlaysiz</li>
    <li><b>ことわざ</b> bilan farqini ajratasiz</li>
    <li>Ularni gapda <b>oʻlchov bilan</b> ishlatishni oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrt belgi, ikki boʻlak</span>
  <span class="pe-chip pe-chip--s"><ruby>一石<rt>いっせき</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o"><ruby>二鳥<rt>にちょう</rt></ruby></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">bir tosh bilan ikki qush</span>
</div>

<h3>1. <ruby>四字熟語<rt>よじじゅくご</rt></ruby> nima</h3>

<p>Toʻrtta kanjidan tuzilgan, <b>bir butun maʼnoga ega</b> ibora.
Koʻpchiligi Xitoydan kelgan, shuning uchun deyarli hammasi
<b>on'yomi</b> bilan oʻqiladi. Ichki tuzilishi odatda
<b>2 + 2</b>: ikki belgi bir boʻlak.</p>

<div class="pj-yomi">
  <div class="pj-yomi__side">
    <p class="pj-yomi__h">QOIDA — butunlay ON'YOMI</p>
    <p class="pj-yomi__ex"><ruby>一石二鳥<rt>いっせきにちょう</rt></ruby> · <ruby>十人十色<rt>じゅうにんといろ</rt></ruby></p>
    <p>Toʻrt kanji yopishgan — xitoycha oʻqilish ishlaydi. Deyarli barchasi shunday.</p>
  </div>
  <div class="pj-yomi__side pj-yomi__side--kun">
    <p class="pj-yomi__h">ISTISNO — KUN'YOMI ham bor</p>
    <p class="pj-yomi__ex"><ruby>三日坊主<rt>みっかぼうず</rt></ruby></p>
    <p><ruby>三日<rt>みっか</rt></ruby> — yaponcha oʻqilish. Bunday istisnolar kam, lekin bor: har birini alohida yodlang.</p>
  </div>
</div>

<div class="pe-call pe-warn">
  <p><b>Oʻqilishni taxmin qilmang.</b>
  <ruby>一期一会<rt>いちごいちえ</rt></ruby> ni koʻrib «いっきいっかい»
  deyish juda tabiiy — va xato. Bu iboralar yuzlab yil oldin
  qotib qolgan, shuning uchun ularning oʻqilishi <em>qoida emas,
  tarix</em>. Har bir <ruby>四字熟語<rt>よじじゅくご</rt></ruby> —
  bitta soʻz: maʼnosi bilan birga oʻqilishini ham yodlang.</p>
</div>

<h3>2. Sakkiztasi — oʻzbekcha jufti bilan</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Ibora</th><th>Soʻzma-soʻz</th><th>Maʼnosi va oʻzbekcha jufti</th></tr>
  <tr><td class="pj-stem"><ruby>一石二鳥<rt>いっせきにちょう</rt></ruby></td>
      <td class="pj-end">bir tosh, ikki qush</td>
      <td class="pj-uz">bitta ish bilan ikki foyda — <b>«bir oʻq bilan ikki quyon»</b></td></tr>
  <tr><td class="pj-stem"><ruby>十人十色<rt>じゅうにんといろ</rt></ruby></td>
      <td class="pj-end">oʻn odam, oʻn rang</td>
      <td class="pj-uz">har kim boshqacha — <b>«har kimning didi har xil»</b></td></tr>
  <tr><td class="pj-stem"><ruby>自業自得<rt>じごうじとく</rt></ruby></td>
      <td class="pj-end">oʻz ishi, oʻz olgani</td>
      <td class="pj-uz">qilmishiga yarasha — <b>«nima eksang, shuni oʻrasan»</b></td></tr>
  <tr><td class="pj-stem"><ruby>一期一会<rt>いちごいちえ</rt></ruby></td>
      <td class="pj-end">bir umr, bir uchrashuv</td>
      <td class="pj-uz">bu uchrashuv boshqa takrorlanmaydi — shuning uchun qadrla</td></tr>
  <tr><td class="pj-stem"><ruby>三日坊主<rt>みっかぼうず</rt></ruby></td>
      <td class="pj-end">uch kunlik rohib</td>
      <td class="pj-uz">tez tashlab qoʻyadigan odam — <b>«bir kunlik gʻayrat»</b></td></tr>
  <tr><td class="pj-stem"><ruby>温故知新<rt>おんこちしん</rt></ruby></td>
      <td class="pj-end">eskini isit, yangini bil</td>
      <td class="pj-uz">eskini oʻrganib, yangisini tushunish</td></tr>
  <tr><td class="pj-stem"><ruby>初志貫徹<rt>しょしかんてつ</rt></ruby></td>
      <td class="pj-end">birinchi niyat, oxirigacha</td>
      <td class="pj-uz">boshlagan ishni oxiriga yetkazish</td></tr>
  <tr><td class="pj-stem"><ruby>意気投合<rt>いきとうごう</rt></ruby></td>
      <td class="pj-end">ruh mos tushdi</td>
      <td class="pj-uz">darrov til topishmoq — <b>«koʻngli bir boʻldi»</b></td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>歩<rt>ある</rt></ruby>いて<ruby>通<rt>かよ</rt></ruby>えば、お<ruby>金<rt>かね</rt></ruby>も<ruby>節約<rt>せつやく</rt></ruby>できるし<ruby>健康<rt>けんこう</rt></ruby>にもいい。<span class="pe-hl pe-hl--v">まさに<ruby>一石二鳥<rt>いっせきにちょう</rt></ruby>だ</span>。</p>
  <p class="pe-ex__uz">Piyoda qatnasang, pulni ham tejaysan, sogʻliq uchun ham foydali. Rosa bir oʻq bilan ikki quyon.</p>
  <p class="pe-ex__why">Odatdagi qolip: avval vaziyat, keyin <b>まさに〜だ</b> («aynan shu») bilan ibora. Iborani gap boshiga qoʻyish emas, <em>xulosa qilib</em> qoʻyish tabiiy.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu darsning butun qiymati bitta jadvalda: yuqoridagi
  iboralarning yarmi oʻzbek tilida ham bor.</b> Va bu tasodif
  emas. Yaponiya ham, Oʻrta Osiyo ham asrlar davomida bir xil
  narsalarni koʻrgan: mehnat, sabr, ochkoʻzlik, ustozlik. Shuning
  uchun «bir oʻq bilan ikki quyon» va
  <ruby>一石二鳥<rt>いっせきにちょう</rt></ruby> bir-biridan
  mustaqil ravishda, ikki chekkada tugʻilgan. Yodlaganingizda
  shuni qiling: <em>avval oʻzbekchasini eslang, keyin yaponchasini
  unga ilib qoʻying</em>. Nolldan yodlangan soʻz bir haftada
  unutiladi; bor narsaga ilingan soʻz qoladi.</p>
</div>

<h3>3. ことわざ — maqollar</h3>

<p>Farqi shakl bilan: <ruby>四字熟語<rt>よじじゅくご</rt></ruby> —
toʻrtta kanjidan iborat <b>soʻz</b>; ことわざ — toʻliq
<b>gap</b>, va u yaponcha oʻqiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Maqol</th><th>Soʻzma-soʻz</th><th>Oʻzbekcha jufti</th></tr>
  <tr><td class="pj-stem"><ruby>石<rt>いし</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にも<ruby>三年<rt>さんねん</rt></ruby></td>
      <td class="pj-end">toshning ustida ham uch yil</td>
      <td class="pj-uz"><b>«sabr tagi — sariq oltin»</b></td></tr>
  <tr><td class="pj-stem"><ruby>塵<rt>ちり</rt></ruby>も<ruby>積<rt>つ</rt></ruby>もれば<ruby>山<rt>やま</rt></ruby>となる</td>
      <td class="pj-end">chang ham yigʻilsa togʻ boʻladi</td>
      <td class="pj-uz"><b>«tomchi tomchi koʻl boʻlar»</b></td></tr>
  <tr><td class="pj-stem"><ruby>急<rt>いそ</rt></ruby>がば<ruby>回<rt>まわ</rt></ruby>れ</td>
      <td class="pj-end">shoshsang — aylanib oʻt</td>
      <td class="pj-uz"><b>«yetti oʻlchab, bir kes»</b></td></tr>
  <tr><td class="pj-stem"><ruby>猿<rt>さる</rt></ruby>も<ruby>木<rt>き</rt></ruby>から<ruby>落<rt>お</rt></ruby>ちる</td>
      <td class="pj-end">maymun ham daraxtdan yiqiladi</td>
      <td class="pj-uz"><b>«otning ham oyogʻi qoqiladi»</b></td></tr>
  <tr><td class="pj-stem"><ruby>七転<rt>ななころ</rt></ruby>び<ruby>八起<rt>やお</rt></ruby>き</td>
      <td class="pj-end">yetti yiqilish, sakkiz turish</td>
      <td class="pj-uz">aniq jufti yoʻq: «yiqilsang ham, turib ket»</td></tr>
  <tr><td class="pj-stem"><ruby>花<rt>はな</rt></ruby>より<ruby>団子<rt>だんご</rt></ruby></td>
      <td class="pj-end">guldan koʻra shirinlik</td>
      <td class="pj-uz">goʻzallikdan koʻra foyda — aniq jufti yoʻq</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>毎日<rt>まいにち</rt></ruby><ruby>十分<rt>じゅっぷん</rt></ruby>でもいい。<span class="pe-hl pe-hl--s"><ruby>塵<rt>ちり</rt></ruby>も<ruby>積<rt>つ</rt></ruby>もれば<ruby>山<rt>やま</rt></ruby>となる</span>。</p>
  <p class="pe-ex__uz">Har kuni oʻn daqiqa boʻlsa ham boʻldi. Tomchi tomchi koʻl boʻlar.</p>
  <p class="pe-ex__why">Maqol gapning <b>oxirida</b> yolgʻiz turadi — u xulosa. Oldiga «〜と<ruby>言<rt>い</rt></ruby>うように» qoʻyilsa, biroz kitobiy chiqadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>先生<rt>せんせい</rt></ruby>でも<ruby>間違<rt>まちが</rt></ruby>えることがある。<ruby>猿<rt>さる</rt></ruby>も<ruby>木<rt>き</rt></ruby>から<ruby>落<rt>お</rt></ruby>ちるのだから。</p>
  <p class="pe-ex__uz">Ustoz ham xato qilishi mumkin. Axir otning ham oyogʻi qoqiladi.</p>
  <p class="pe-ex__why">Bu maqol <b>oʻzingizdan kattaga nisbatan</b> ishlatilmaydi: «siz ham maymunsiz» degan ohang chiqadi. Uchinchi shaxs haqida — mumkin.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Maqolning ohangiga eʼtibor bering, maʼnosiga emas.</b>
  <ruby>猿<rt>さる</rt></ruby>も<ruby>木<rt>き</rt></ruby>から
  <ruby>落<rt>お</rt></ruby>ちる — toʻgʻri maqol, lekin uni
  ustozingizga yoki boshligʻingizga qaratib aytsangiz, siz uni
  maymunga qiyoslagan boʻlasiz. Oʻzbekchada ham xuddi shunday:
  «otning ham oyogʻi qoqiladi» — oʻrtoqqa aytiladi, otangizga
  emas. Maqol — oʻtkir asbob; oʻtkir asbobni kimga qaratganingizni
  bilish kerak.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Maqol tarjima qilinmaydi — almashtiriladi.</b> Bu
  tarjimonlikning eng birinchi qoidasi va uni hozir bilib
  qoʻyganingiz maʼqul.
  <ruby>猿<rt>さる</rt></ruby>も<ruby>木<rt>き</rt></ruby>から<ruby>落<rt>お</rt></ruby>ちる
  ni «maymun ham daraxtdan yiqiladi» deb oʻgirsangiz, oʻzbek
  oʻquvchisi maymun haqida oʻylab qoladi va gapning maʼnosi
  yoʻqoladi. «Otning ham oyogʻi qoqiladi» desangiz — maʼno
  toʻliq yetadi, garchi na ot bor, na oyoq. <b>Maqolda soʻzlar
  emas, <em>vazifa</em> tarjima qilinadi.</b> Teskarisi ham
  shunday: «sabr tagi sariq oltin» ni yaponchaga soʻzma-soʻz
  emas, <ruby>石<rt>いし</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にも<ruby>三年<rt>さんねん</rt></ruby>
  deb oʻgiring.</p>
</div>

<h3>4. Qanchalik ishlatiladi</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">✓ Bitta, oʻz joyida</p>
    <p>Suhbat yoki insho oxirida bitta ibora — kuchli, esda qoladi, oʻqigan odamni koʻrsatadi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">✗ Uchta, ketma-ket</p>
    <p>Har jumlada bittadan maqol — yapon quloqqa <b>gʻalati</b> eshitiladi: bilim emas, koʻz-koʻz qilish.</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>Imtihonda bu iboralar <em>tanish</em> uchun keladi, yozish
  uchun emas.</b> N3 va N2 oʻqish qismida matn ichida bitta
  <ruby>四字熟語<rt>よじじゅくご</rt></ruby> uchrashi mumkin va
  undan butun xatboshining maʼnosi osilib turadi. Shuning uchun
  vazifangiz — koʻrganda tanish. Yozma ishda esa bittasi yetadi,
  va u xulosaga qoʻyiladi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">熟</span>
    <span class="pj-kanji__uz">pishgan, yetilgan</span>
    <span class="pj-kanji__on">オン: ジュク</span>
    <span class="pj-kanji__kun">KUN: う(れる)</span>
    <span class="pj-kanji__note">熟語 (じゅくご) — turgʻun ibora · 熟れる (うれる) — pishmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">積</span>
    <span class="pj-kanji__uz">toʻplamoq, yigʻmoq</span>
    <span class="pj-kanji__on">オン: セキ</span>
    <span class="pj-kanji__kun">KUN: つ(もる)・つ(む)</span>
    <span class="pj-kanji__note">積もる (つもる) — yigʻilmoq · 面積 (めんせき) — yuza</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">貫</span>
    <span class="pj-kanji__uz">teshib oʻtmoq, oxiriga yetkazmoq</span>
    <span class="pj-kanji__on">オン: カン</span>
    <span class="pj-kanji__kun">KUN: つらぬ(く)</span>
    <span class="pj-kanji__note">初志貫徹 (しょしかんてつ) · 貫く (つらぬく) — oxirigacha olib bormoq</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Bir narsani alohida aytib qoʻyish kerak:
  <ruby>七転<rt>ななころ</rt></ruby>び<ruby>八起<rt>やお</rt></ruby>き
  va <ruby>花<rt>はな</rt></ruby>より<ruby>団子<rt>だんご</rt></ruby>
  ning oʻzbekcha aniq jufti yoʻq.</b> Bu — normal holat, va uni
  yashirmaslik kerak. Til oʻrganishda eng katta xato — <em>har bir
  narsaga majburan juft topish</em>. Jufti yoʻq narsani jufti yoʻq
  deb qabul qiling va uni <b>tasviri bilan</b> yodlang: yetti marta
  yiqilib, sakkiz marta turgan odam; gulga qaramay, shirinlikni
  tanlagan odam. Rasm — tarjimadan mustahkamroq xotira.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>一期一会<rt>いっきいっかい</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>一期一会<rt>いちごいちえ</rt></ruby> — oʻqilishi qoidadan emas, tarixdan keladi. Har iborani oʻqilishi bilan yodlang.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>三日坊主<rt>さんにちぼうず</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>三日坊主<rt>みっかぼうず</rt></ruby> — bu kam sonli KUN'YOMI istisnolaridan biri.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ (ustozga) <ruby>先生<rt>せんせい</rt></ruby>も<ruby>猿<rt>さる</rt></ruby>も<ruby>木<rt>き</rt></ruby>から<ruby>落<rt>お</rt></ruby>ちますね</p>
  <p class="pe-fix__good">✓ Bu maqolni yuqoridagi odamga qaratmang — uni uchinchi shaxs haqida yoki umumiy gapda ishlating.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>一石二鳥<rt>いっせきにちょう</rt></ruby>を<ruby>使<rt>つか</rt></ruby>った</p>
  <p class="pe-fix__good">✓ まさに<ruby>一石二鳥<rt>いっせきにちょう</rt></ruby>だ — bu ibora <b>ot</b>, va odatda <b>だ／である</b> bilan xulosa qilib qoʻyiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Bitta xatboshida uchta maqol</p>
  <p class="pe-fix__good">✓ Bitta matnda bitta — maqol xulosa uchun, bezak uchun emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>一石二鳥<rt>いっせきにちょう</rt></ruby> ning oʻzbekcha jufti nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>«Bir oʻq bilan ikki quyon»</b> — bitta ish bilan ikki foyda. Soʻzma-soʻz «bir tosh, ikki qush»; qush yoki quyon — maʼno bir xil.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>石<rt>いし</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にも<ruby>三年<rt>さんねん</rt></ruby> nimani aytadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Sabr.</b> Sovuq toshda ham uch yil oʻtirsang, u isiydi — «sabr tagi sariq oltin». Qiyin ishni tashlab qoʻymaslik haqida.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>三日坊主<rt>みっかぼうず</rt></ruby> nega alohida eslab qolinadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Oʻqilishi.</b> Deyarli barcha <ruby>四字熟語<rt>よじじゅくご</rt></ruby> butunlay on'yomi bilan oʻqiladi, bu esa <ruby>三日<rt>みっか</rt></ruby> — kun'yomi bilan. Istisno, demak yodlanadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Yetti oʻlchab, bir kes» — qaysi yaponcha maqolga toʻgʻri keladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>急<rt>いそ</rt></ruby>がば<ruby>回<rt>まわ</rt></ruby>れ</b> — «shoshsang, aylanib oʻt». Ikkalasi ham bitta narsani aytadi: shoshilinch yoʻl koʻpincha uzunroq chiqadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>四字熟語<rt>よじじゅくご</rt></ruby> va ことわざ farqi nimada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Shakl.</b> <ruby>四字熟語<rt>よじじゅくご</rt></ruby> — toʻrtta kanjidan iborat <b>soʻz</b>, on'yomi bilan. ことわざ — toʻliq <b>gap</b>, yaponcha oʻqiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Insho yozayotibsiz. Nechta maqol ishlatasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Bittasi.</b> Va uni xulosaga qoʻying. Uchta maqol bilim emas, koʻz-koʻz qilish boʻlib eshitiladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>四字熟語<rt>よじじゅくご</rt></ruby></b> — toʻrt belgili turgʻun ibora</li>
  <li><b>ことわざ</b> — xalq maqoli</li>
  <li><b><ruby>一石二鳥<rt>いっせきにちょう</rt></ruby></b> — bir oʻq bilan ikki quyon</li>
  <li><b><ruby>十人十色<rt>じゅうにんといろ</rt></ruby></b> — har kimning didi har xil</li>
  <li><b><ruby>自業自得<rt>じごうじとく</rt></ruby></b> — nima eksang, shuni oʻrasan</li>
  <li><b><ruby>一期一会<rt>いちごいちえ</rt></ruby></b> — takrorlanmas uchrashuv</li>
  <li><b><ruby>三日坊主<rt>みっかぼうず</rt></ruby></b> — bir kunlik gʻayrat</li>
  <li><b><ruby>石<rt>いし</rt></ruby>の<ruby>上<rt>うえ</rt></ruby>にも<ruby>三年<rt>さんねん</rt></ruby></b> — sabr tagi sariq oltin</li>
  <li><b><ruby>塵<rt>ちり</rt></ruby>も<ruby>積<rt>つ</rt></ruby>もれば<ruby>山<rt>やま</rt></ruby>となる</b> — tomchi tomchi koʻl boʻlar</li>
  <li><b>まさに</b> — aynan, rosa</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><ruby>四字熟語<rt>よじじゅくご</rt></ruby> — <b>soʻz</b>, on'yomi bilan; ことわざ — <b>gap</b>, yaponcha oʻqilishda.</li>
    <li>Yarmining <b>oʻzbekcha jufti bor</b> — oʻshanga ilib yodlang.</li>
    <li>Bitta matnda <b>bitta</b> maqol, va u xulosaga qoʻyiladi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-99: 和語・漢語・外来語 — lugʻatning uch qatlami va uslub tanlash",
        "category": "japanese",
        "order": 99,
        "summary": (
            "Bitta maʼno, uchta soʻz: 集まり · 集会 · ミーティング. "
            "Yapon lugʻati uch qatlamdan iborat, va oʻzbek tilida ham "
            "aynan uchtasi bor: yigʻilish · majlis · miting."
        ),
        "stories": ["みっつの ことば"],
        "content": """
<h2>PJ-99: <ruby>和語<rt>わご</rt></ruby>・<ruby>漢語<rt>かんご</rt></ruby>・<ruby>外来語<rt>がいらいご</rt></ruby> — lugʻatning uch qatlami va uslub tanlash</h2>

<p>Maktab devoriga uchta eʼlon osilgan. Uchalasi ham bitta narsani
aytadi — «uchrashuv boʻladi» — lekin uchta boshqa soʻz bilan:
<b><ruby>集<rt>あつ</rt></ruby>まり</b>,
<b><ruby>集会<rt>しゅうかい</rt></ruby></b>, <b>ミーティング</b>.
Uchalasi ham toʻgʻri. Uchalasi ham boshqa narsa
<em>his qildiradi</em>.</p>

<p>Bu — yapon lugʻatining uch qatlami. Va bu dars sizga yangi
tushuncha bermaydi: oʻzbek tilida ham <b>aynan shu uchtasi</b>
bor, siz ularni har kuni ishlatasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uch qatlamni — <b><ruby>和語<rt>わご</rt></ruby> · <ruby>漢語<rt>かんご</rt></ruby> · <ruby>外来語<rt>がいらいご</rt></ruby></b> — ajratasiz</li>
    <li>Soʻzning <b>oʻqilishidan</b> uning qatlamini bilib olasiz</li>
    <li>Matn uslubiga qarab toʻgʻri qatlamni tanlaysiz</li>
    <li><b><ruby>和製英語<rt>わせいえいご</rt></ruby></b> tuzogʻiga tushmaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta maʼno, uch qatlam</span>
  <span class="pe-chip pe-chip--s"><ruby>集<rt>あつ</rt></ruby>まり</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v"><ruby>集会<rt>しゅうかい</rt></ruby></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">ミーティング</span>
</div>

<h3>1. Uch qatlam</h3>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name"><ruby>和語<rt>わご</rt></ruby></span>
    <span class="pj-level__ja"><ruby>集<rt>あつ</rt></ruby>まり</span>
    <span class="pj-level__who">asl yaponcha — iliq, kundalik, gapiriladigan</span>
  </div>
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name"><ruby>漢語<rt>かんご</rt></ruby></span>
    <span class="pj-level__ja"><ruby>集会<rt>しゅうかい</rt></ruby></span>
    <span class="pj-level__who">xitoy ildizli — zich, rasmiy, yoziladigan</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name"><ruby>外来語<rt>がいらいご</rt></ruby></span>
    <span class="pj-level__ja">ミーティング</span>
    <span class="pj-level__who">chetdan kelgan — yangi, zamonaviy, ish muhiti</span>
  </div>
</div>

<h3>2. Oʻqilish qatlamni aytib turadi</h3>

<p>Eng yaxshi xabar: bu asbob sizda <b>PJ-11 dan beri bor</b>.
Siz uni shunchaki shu maqsadda ishlatmagansiz.</p>

<div class="pj-yomi">
  <div class="pj-yomi__side pj-yomi__side--kun">
    <p class="pj-yomi__h">KUN'YOMI → <ruby>和語<rt>わご</rt></ruby></p>
    <p class="pj-yomi__ex"><ruby>集<rt>あつ</rt></ruby>まり · <ruby>速<rt>はや</rt></ruby>さ · <ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby></p>
    <p>Kanji hiragana bilan tugasa — asl yaponcha soʻz.</p>
  </div>
  <div class="pj-yomi__side">
    <p class="pj-yomi__h">ON'YOMI → <ruby>漢語<rt>かんご</rt></ruby></p>
    <p class="pj-yomi__ex"><ruby>集会<rt>しゅうかい</rt></ruby> · <ruby>速度<rt>そくど</rt></ruby> · <ruby>食品<rt>しょくひん</rt></ruby></p>
    <p>Ikki kanji yopishgan — xitoy ildizli soʻz.</p>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>Uchinchisini ajratish esa umuman mehnat talab qilmaydi:
  <ruby>外来語<rt>がいらいご</rt></ruby> har doim
  <b>katakana</b>da yoziladi.</b> Aynan shu ish uchun katakana
  bor (PJ-7). Demak yapon matniga qaraganingizda uch qatlam
  koʻzga darrov tashlanadi: kana bilan tugagan kanji, yopishgan
  kanjilar, va katakana.</p>
</div>

<h3>3. Uchtalik jadval</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th><ruby>和語<rt>わご</rt></ruby></th><th><ruby>漢語<rt>かんご</rt></ruby></th><th><ruby>外来語<rt>がいらいご</rt></ruby></th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>集<rt>あつ</rt></ruby>まり</td>
      <td class="pj-end"><ruby>集会<rt>しゅうかい</rt></ruby></td>
      <td class="pj-res">ミーティング</td>
      <td class="pj-uz">yigʻilish</td></tr>
  <tr><td class="pj-stem"><ruby>速<rt>はや</rt></ruby>さ</td>
      <td class="pj-end"><ruby>速度<rt>そくど</rt></ruby></td>
      <td class="pj-res">スピード</td>
      <td class="pj-uz">tezlik</td></tr>
  <tr><td class="pj-stem"><ruby>手伝<rt>てつだ</rt></ruby>う</td>
      <td class="pj-end"><ruby>援助<rt>えんじょ</rt></ruby>する</td>
      <td class="pj-res">サポートする</td>
      <td class="pj-uz">yordam bermoq</td></tr>
  <tr><td class="pj-stem">やめる</td>
      <td class="pj-end"><ruby>中止<rt>ちゅうし</rt></ruby>する</td>
      <td class="pj-res">キャンセルする</td>
      <td class="pj-uz">toʻxtatmoq</td></tr>
  <tr><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べ<ruby>物<rt>もの</rt></ruby></td>
      <td class="pj-end"><ruby>食品<rt>しょくひん</rt></ruby></td>
      <td class="pj-res">フード</td>
      <td class="pj-uz">ovqat</td></tr>
  <tr><td class="pj-stem"><ruby>考<rt>かんが</rt></ruby>え</td>
      <td class="pj-end"><ruby>意見<rt>いけん</rt></ruby></td>
      <td class="pj-res">アイデア</td>
      <td class="pj-uz">fikr</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s"><ruby>明日<rt>あした</rt></ruby>の<ruby>集<rt>あつ</rt></ruby>まり、<ruby>行<rt>い</rt></ruby>く？</span></p>
  <p class="pe-ex__uz">Ertagi yigʻilishga borasanmi?</p>
  <p class="pe-ex__why"><ruby>和語<rt>わご</rt></ruby> — doʻstga aytilgan gap. Bu yerda <ruby>集会<rt>しゅうかい</rt></ruby> desangiz, gap birdan sovuq va rasmiy boʻlib qoladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>本校<rt>ほんこう</rt></ruby>では<ruby>毎月<rt>まいつき</rt></ruby><span class="pe-hl pe-hl--v"><ruby>集会<rt>しゅうかい</rt></ruby></span>を<ruby>実施<rt>じっし</rt></ruby>している。</p>
  <p class="pe-ex__uz">Maktabimizda har oy yigʻilish oʻtkaziladi.</p>
  <p class="pe-ex__why">Rasmiy eʼlon, である<ruby>体<rt>たい</rt></ruby>ga yaqin uslub — bu yerda <ruby>漢語<rt>かんご</rt></ruby> oʻz uyida. Diqqat qiling: <ruby>実施<rt>じっし</rt></ruby> ham <ruby>漢語<rt>かんご</rt></ruby>, ular bir-birini chaqiradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>十時<rt>じゅうじ</rt></ruby>から<span class="pe-hl pe-hl--aux">ミーティング</span>です。<ruby>資料<rt>しりょう</rt></ruby>のチェックをお<ruby>願<rt>ねが</rt></ruby>いします。</p>
  <p class="pe-ex__uz">Soat oʻndan yigʻilish. Materialni tekshirib chiqishingizni soʻrayman.</p>
  <p class="pe-ex__why">Ish muhiti — <ruby>外来語<rt>がいらいご</rt></ruby>ning uyi. Yaponiyada ofis tili katakanaga toʻla, va bu qasddan: u zamonaviy va xalqaro eshitiladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Va endi bu darsning asosiy gapi: oʻzbek tilida ham aynan
  uchta qatlam bor.</b> Turkiy oʻz qatlamimiz, arab-fors qatlami,
  va rus-yevropa qatlami. Ularni siz har kuni, hech oʻylamay
  almashtirib turasiz:</p>
  <ul>
    <li><b>yigʻilish · majlis · miting</b> — aynan
      <ruby>集<rt>あつ</rt></ruby>まり ·
      <ruby>集会<rt>しゅうかい</rt></ruby> · ミーティング</li>
    <li><b>oʻy · fikr · ideya</b> —
      <ruby>考<rt>かんが</rt></ruby>え ·
      <ruby>意見<rt>いけん</rt></ruby> · アイデア</li>
    <li><b>kuch · quvvat · energiya</b></li>
    <li><b>boshliq · rahbar · direktor</b></li>
    <li><b>tezlik · surʼat · skorost</b></li>
  </ul>
  <p>Qaysi birini tanlashni sizga hech kim oʻrgatmagan — siz uni
  quloq bilan bilasiz. «Majlis» rasmiy, «yigʻilish» oddiy,
  «miting» zamonaviy. <b>Yapon tilida ham tanlov aynan shu
  mantiq bilan qilinadi.</b> Demak sizda yangi koʻnikma emas,
  eski koʻnikmani boshqa tilga koʻchirish vazifasi bor — bu
  esa ancha oson.</p>
</div>

<h3>4. Qaysi matnga qaysi qatlam</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h">Doʻstga xabar</p>
    <p><b><ruby>和語<rt>わご</rt></ruby></b> — iliq va qisqa. <ruby>漢語<rt>かんご</rt></ruby> bu yerda sovuq chiqadi.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">Insho, maqola</p>
    <p><b><ruby>漢語<rt>かんご</rt></ruby></b> — zich va aniq. PJ-96 dagi である<ruby>体<rt>たい</rt></ruby>ning tabiiy sherigi.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">Ish, texnika</p>
    <p><b><ruby>外来語<rt>がいらいご</rt></ruby></b> — yangi tushunchalar koʻpincha faqat shu qatlamda bor.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">Hikoya, sheʼr</p>
    <p><b><ruby>和語<rt>わご</rt></ruby></b> — yumshoq ohang. Adabiyot shu qatlamda yashaydi.</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>Bitta amaliy qoida: <ruby>漢語<rt>かんご</rt></ruby> zichroq,
  <ruby>和語<rt>わご</rt></ruby> aniqroq.</b>
  <ruby>実施<rt>じっし</rt></ruby>する bitta soʻzda «amalga oshirmoq»
  deydi, lekin quruq; <ruby>行<rt>おこな</rt></ruby>う uzunroq,
  lekin issiqroq. Shuning uchun rasmiy matn
  <ruby>漢語<rt>かんご</rt></ruby> bilan <em>qisqaradi</em>, va
  aynan shuning uchun gazeta sarlavhasi (PJ-96) deyarli butunlay
  <ruby>漢語<rt>かんご</rt></ruby>dan iborat.</p>
</div>

<h3>5. <ruby>和製英語<rt>わせいえいご</rt></ruby> — yaponiyada yasalgan «chet» soʻzlar</h3>

<p>Katakanada yozilgan har bir soʻz chet tilidan olingan degani
emas. Bir qismi Yaponiyaning <b>oʻzida</b> yasalgan va asl tilda
umuman boshqa maʼnoni bildiradi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Yaponchada maʼnosi</th><th>Tuzoq</th></tr>
  <tr><td class="pj-stem">コンセント</td><td class="pj-res">rozetka</td>
      <td class="pj-uz">«rozilik» degani emas</td></tr>
  <tr><td class="pj-stem">マンション</td><td class="pj-res">koʻp qavatli uydagi kvartira</td>
      <td class="pj-uz">qasr yoki saroy emas</td></tr>
  <tr><td class="pj-stem">サラリーマン</td><td class="pj-res">idorada ishlaydigan xodim</td>
      <td class="pj-uz">bu soʻz ingliz tilida yoʻq</td></tr>
  <tr><td class="pj-stem">バイキング</td><td class="pj-res">toʻla stol, ochiq taomnoma</td>
      <td class="pj-uz">skandinav dengizchisi emas</td></tr>
  <tr><td class="pj-stem">ノートパソコン</td><td class="pj-res">noutbuk</td>
      <td class="pj-uz">daftar emas</td></tr>
  <tr><td class="pj-stem">クレーム</td><td class="pj-res">shikoyat</td>
      <td class="pj-uz">talab yoki daʼvo emas</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu hodisa oʻzbek tiliga ham begona emas.</b> Bizda ham
  rus tilidan kirgan soʻzlar oʻz maʼnosini oʻzgartirgan yoki
  butunlay oʻzimizda yasalgan shakllari bor. Shuning uchun
  qoida bitta va u ikkala tilga baravar tegishli:
  <em>katakanada yozilgan soʻzni koʻrganingizda uni ingliz
  tilidan taxmin qilmang — lugʻatdan qarang.</em> Taxmin
  toʻgʻri chiqqan paytlari koʻp, lekin xato chiqqan paytlari
  aynan eng muhim joylarda boʻladi: shartnomada, koʻrsatmada,
  imtihon matnida.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">和</span>
    <span class="pj-kanji__uz">yaponcha; totuvlik</span>
    <span class="pj-kanji__on">オン: ワ</span>
    <span class="pj-kanji__kun">KUN: やわ(らぐ)</span>
    <span class="pj-kanji__note">和語 (わご) — asl yaponcha soʻz · 和食 (わしょく) — yapon taomi</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">援</span>
    <span class="pj-kanji__uz">yordam bermoq</span>
    <span class="pj-kanji__on">オン: エン</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">援助 (えんじょ) — yordam · 応援 (おうえん) — qoʻllab-quvvatlash</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">層</span>
    <span class="pj-kanji__uz">qatlam</span>
    <span class="pj-kanji__on">オン: ソウ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">三層 (さんそう) — uch qatlam · 高層 (こうそう) — koʻp qavatli</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu dars bilan PJ-11 va PJ-96 bir halqaga bogʻlanadi, va
  buni koʻrib qoʻying — kursning eng foydali koʻrinishi shu.</b>
  PJ-11 sizga on'yomi va kun'yomini berdi; siz uni
  <em>oʻqish</em> qoidasi deb bilgansiz. PJ-96 sizga registrni
  berdi; siz uni <em>gap oxiri</em> qoidasi deb bilgansiz. Bugun
  maʼlum boʻldiki, ikkovi bitta narsa: <b>soʻzning oʻqilishi uning
  qaysi uslubga tegishli ekanini aytib turadi.</b> Yaponcha matn
  oʻqiyotganda endi bitta savol bilan koʻp narsani bilasiz —
  «bu yerda kanjilar yopishganmi yoki kana bilan tugaganmi?»
  Yopishgan boʻlsa, matn rasmiy; kana bilan tugagan boʻlsa,
  iliq va kundalik.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ (doʻstga) <ruby>明日<rt>あした</rt></ruby>の<ruby>集会<rt>しゅうかい</rt></ruby>、<ruby>行<rt>い</rt></ruby>く？</p>
  <p class="pe-fix__good">✓ <ruby>明日<rt>あした</rt></ruby>の<ruby>集<rt>あつ</rt></ruby>まり、<ruby>行<rt>い</rt></ruby>く？ — oddiy gapda <ruby>和語<rt>わご</rt></ruby>. <ruby>漢語<rt>かんご</rt></ruby> bu yerda sovuq chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ (rasmiy eʼlon) <ruby>毎月<rt>まいつき</rt></ruby><ruby>集<rt>あつ</rt></ruby>まりをやっています</p>
  <p class="pe-fix__good">✓ <ruby>毎月<rt>まいつき</rt></ruby><ruby>集会<rt>しゅうかい</rt></ruby>を<ruby>実施<rt>じっし</rt></ruby>している — rasmiy matn <ruby>漢語<rt>かんご</rt></ruby>ni chaqiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ コンセント = «rozilik»</p>
  <p class="pe-fix__good">✓ コンセント = <b>rozetka</b> — bu <ruby>和製英語<rt>わせいえいご</rt></ruby>, ingliz tilidan taxmin qilinmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>集会<rt>しゅうかい</rt></ruby>まり</p>
  <p class="pe-fix__good">✓ <ruby>集<rt>あつ</rt></ruby>まり yoki <ruby>集会<rt>しゅうかい</rt></ruby> — ikki qatlamni bitta soʻzga yopishtirib boʻlmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Butun insho katakanada yozilgan <ruby>外来語<rt>がいらいご</rt></ruby>lar bilan</p>
  <p class="pe-fix__good">✓ Inshoda <ruby>漢語<rt>かんご</rt></ruby> asos, <ruby>外来語<rt>がいらいご</rt></ruby> esa faqat jufti yoʻq tushunchalar uchun.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>集<rt>あつ</rt></ruby>まり qaysi qatlamga tegishli va buni qayerdan bildingiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>和語<rt>わご</rt></ruby></b>. Kanji hiragana bilan tugayapti (<ruby>集<rt>あつ</rt></ruby>まり) — demak <b>kun'yomi</b>, demak asl yaponcha soʻz.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Rasmiy eʼlon yozyapsiz. «Yigʻilish» — qaysi soʻz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>集会<rt>しゅうかい</rt></ruby></b>. Rasmiy matn <ruby>漢語<rt>かんご</rt></ruby>ni chaqiradi, va u である<ruby>体<rt>たい</rt></ruby> bilan bir uslubda turadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. コンセント nimani anglatadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Rozetka.</b> Bu <ruby>和製英語<rt>わせいえいご</rt></ruby> — Yaponiyada yasalgan soʻz. Ingliz tilidan taxmin qilish bu yerda xato javob beradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Oʻy · fikr · ideya» — bu oʻzbekcha uchtalik yaponchada nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>考<rt>かんが</rt></ruby>え · <ruby>意見<rt>いけん</rt></ruby> · アイデア</b>. Ikki tilda ham bir xil uch qatlam, bir xil tartibda: oʻz qatlam → klassik oʻzlashma → zamonaviy oʻzlashma.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega gazeta sarlavhasi deyarli butunlay <ruby>漢語<rt>かんご</rt></ruby>dan iborat?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Zichligi uchun.</b> <ruby>漢語<rt>かんご</rt></ruby> bir xil maʼnoni kamroq belgida aytadi, sarlavhada esa joy tor — PJ-96 dagi tejamkorlikning davomi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Katakanada yozilgan notanish soʻzni koʻrdingiz. Nima qilasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Lugʻatdan qaraysiz.</b> Ingliz tilidan taxmin qilish koʻp hollarda ishlaydi, lekin <ruby>和製英語<rt>わせいえいご</rt></ruby> aynan eng muhim joylarda adashtiradi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>和語<rt>わご</rt></ruby></b> — asl yaponcha soʻz (kun'yomi)</li>
  <li><b><ruby>漢語<rt>かんご</rt></ruby></b> — xitoy ildizli soʻz (on'yomi)</li>
  <li><b><ruby>外来語<rt>がいらいご</rt></ruby></b> — chetdan kirgan soʻz (katakana)</li>
  <li><b><ruby>和製英語<rt>わせいえいご</rt></ruby></b> — Yaponiyada yasalgan «chet» soʻz</li>
  <li><b><ruby>集会<rt>しゅうかい</rt></ruby></b> — yigʻilish (rasmiy)</li>
  <li><b><ruby>実施<rt>じっし</rt></ruby>する</b> — amalga oshirmoq</li>
  <li><b><ruby>援助<rt>えんじょ</rt></ruby>する</b> — yordam bermoq (rasmiy)</li>
  <li><b><ruby>中止<rt>ちゅうし</rt></ruby>する</b> — toʻxtatmoq, bekor qilmoq</li>
  <li><b><ruby>速度<rt>そくど</rt></ruby></b> — tezlik (rasmiy)</li>
  <li><b>コンセント</b> — rozetka</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>Oʻqilish qatlamni aytadi:</b> kun'yomi → <ruby>和語<rt>わご</rt></ruby>, on'yomi → <ruby>漢語<rt>かんご</rt></ruby>, katakana → <ruby>外来語<rt>がいらいご</rt></ruby>.</li>
    <li>Oʻzbekcha <b>yigʻilish · majlis · miting</b> — aynan shu uchlik; tanlovni siz allaqachon bilasiz.</li>
    <li>Katakana ≠ ingliz tili: <b><ruby>和製英語<rt>わせいえいご</rt></ruby></b>ni taxmin qilmang.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-100: Bundan keyin qayerga: N3 dan N2 gacha yoʻl xaritasi",
        "category": "japanese",
        "order": 100,
        "summary": (
            "Kursning soʻnggi darsi. Qoʻlingizda nima bor, N3 va N2 "
            "gacha qancha yoʻl qolgan, JLPT qanday tuzilgan va har kuni "
            "qiladigan toʻrtta ish — halol raqamlar bilan."
        ),
        "stories": ["じしょを ひらかなかった ひ"],
        "content": """
<h2>PJ-100: Bundan keyin qayerga — N3 dan N2 gacha yoʻl xaritasi</h2>

<p>Birinchi darsda siz bitta belgini ham oʻqiy olmasdingiz. Hozir
esa bu sahifadagi yaponcha gaplarni furigana bilan oʻqiyapsiz,
ularning grammatikasini nomi bilan atay olasiz va oʻzingiz xat
yoza olasiz. Yuzta dars orqada qoldi.</p>

<p>Bu dars yangi grammatika bermaydi. U boshqa ishni qiladi —
<b>sizga halol xarita beradi</b>: qayerdasiz, keyingi belgigacha
qancha bor, va har kuni nima qilish kerak. Chunki tilni tashlab
qoʻyishning eng koʻp uchraydigan sababi qiyinchilik emas,
<em>xaritasizlik</em>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Hozirgi darajangizni <b>aniq</b> nomlay olasiz</li>
    <li>N3 va N2 gacha qancha kanji va soʻz borligini bilasiz</li>
    <li>JLPT qanday tuzilganini va nega tinglashni tashlab boʻlmasligini bilasiz</li>
    <li>Har kuni qiladigan <b>toʻrtta ish</b>ni aniqlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kundalik odat</span>
  <span class="pe-chip pe-chip--s">1 sahifa oʻqish</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">10 daqiqa tinglash</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">10 ta soʻz</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">3 ta gap yozish</span>
</div>

<h3>1. Qoʻlingizda nima bor</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h">Uchta yozuv</p>
    <p>Hiragana, katakana va taxminan <b>600</b> kanji — furigana bilan har qanday matnni oʻqiy olasiz.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">Grammatika</p>
    <p>Butun N4 va N3 ning katta qismi: feʼl guruhlari, て-shakli, shart gaplar, passiv, kauzativ, <ruby>敬語<rt>けいご</rt></ruby>.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">Uch registr</p>
    <p>です・ます, <ruby>普通体<rt>ふつうたい</rt></ruby> va である<ruby>体<rt>たい</rt></ruby> — gap, kundalik va maqola tillari.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">88 ta matn</p>
    <p>Har bir darsning oʻqish matni, audiosi bilan. Bu — sizning birinchi kutubxonangiz.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Bir narsani aniq aytib qoʻyay, chunki u sizga keyin ham
  kerak boʻladi: grammatika sizning qiyin qismingiz emas edi va
  bundan keyin ham boʻlmaydi.</b> Oʻzbek tili ham, yapon tili ham
  kesimni oxiriga qoʻyadi va maʼnoni qoʻshimchalar bilan quradi —
  shuning uchun <ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます
  sizga birinchi kundanoq tabiiy tuyulgan. Ingliz yoki rus tilida
  gapiradigan oʻquvchi aynan shu joyda oylab qiynaladi.
  <b>Sizning qiyin qismingiz — hajm:</b> kanji soni va soʻz
  boyligi. Bu esa aql emas, <em>takror</em> talab qiladi. Xushxabar
  shuki, takror — bu bajarish mumkin boʻlgan ish; qobiliyat esa
  emas.</p>
</div>

<h3>2. Halol raqamlar</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Daraja</th><th>Kanji (taxminan)</th><th>Soʻz (taxminan)</th><th>Nimani oʻqiy olasiz</th></tr>
  <tr><td class="pj-stem">N5</td><td class="pj-end">100</td><td class="pj-res">800</td>
      <td class="pj-uz">qisqa eʼlon, oddiy gap</td></tr>
  <tr><td class="pj-stem">N4</td><td class="pj-end">300</td><td class="pj-res">1 500</td>
      <td class="pj-uz">kundalik matn, oddiy hikoya — <b>siz shu yerdasiz</b></td></tr>
  <tr><td class="pj-stem">N3</td><td class="pj-end">650</td><td class="pj-res">3 750</td>
      <td class="pj-uz">yengil maqola, blog, ish yozishmasi</td></tr>
  <tr><td class="pj-stem">N2</td><td class="pj-end">1 000</td><td class="pj-res">6 000</td>
      <td class="pj-uz">gazeta, roman, ishga joylashish</td></tr>
  <tr><td class="pj-stem">N1</td><td class="pj-end">2 000</td><td class="pj-res">10 000</td>
      <td class="pj-uz">ilmiy matn, klassik adabiyot</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Bu raqamlar — yoʻl belgisi, qonun emas.</b> JLPT ni
  oʻtkazadigan tashkilot 2010-yildan beri har bir daraja uchun
  aniq soʻz va kanji roʻyxatini <em>eʼlon qilmaydi</em>: maqsad
  roʻyxat yodlash emas, tilni ishlata olish. Yuqoridagi sonlar —
  darsliklar va oʻqituvchilar orasida qabul qilingan taxminiy
  moʻljal. Ularni «shuncha yodlasam, oʻtaman» deb emas, <b>«yoʻl
  qanchalik uzun» deb</b> oʻqing.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Jadvalda koʻzga tashlanmaydigan, lekin eng muhim narsa
  bor: N4 dan N3 gacha soʻz soni ikki yarim baravar oshadi.</b>
  Aynan shu joyda koʻp odam toʻxtaydi, va ular buni «grammatika
  qiyinlashdi» deb tushuntiradi. Aslida grammatika qiyinlashmaydi
  — <em>matn tezlashadi</em>. N3 imtihonida siz bilgan gapni
  bilmagan soʻzlar bilan toʻldirib beradilar va vaqt qoʻyadilar.
  Bunga qarshi bitta dori bor va u grammatika kitobida emas:
  <b>koʻp oʻqish</b>. Kuniga bir sahifa — yilda uch yuz oltmish
  besh sahifa, yaʼni bir nechta kitob.</p>
</div>

<h3>3. JLPT qanday tuzilgan</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Daraja</th><th>Qismlar</th><th>Ball</th></tr>
  <tr><td class="pj-stem">N3 · N2 · N1</td>
      <td class="pj-res"><ruby>言語知識<rt>げんごちしき</rt></ruby> · <ruby>読解<rt>どっかい</rt></ruby> · <ruby>聴解<rt>ちょうかい</rt></ruby></td>
      <td class="pj-uz">uchta boʻlim, har biri 0–60 → jami 0–180</td></tr>
  <tr><td class="pj-stem">N5 · N4</td>
      <td class="pj-res"><ruby>言語知識<rt>げんごちしき</rt></ruby>・<ruby>読解<rt>どっかい</rt></ruby> · <ruby>聴解<rt>ちょうかい</rt></ruby></td>
      <td class="pj-uz">ikkita baholanadigan boʻlim → jami 0–180</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Eng muhim qoida — <ruby>基準点<rt>きじゅんてん</rt></ruby>.</b>
  Oʻtish uchun umumiy ball yetishi <em>kifoya emas</em>: <b>har
  bir boʻlimdan</b> alohida eng kam ball ham olinishi shart.
  Yaʼni oʻqishdan aʼlo, tinglashdan nol olgan odam imtihondan
  oʻtmaydi, jami bali yetsa ham. Amaliy xulosa bitta: <b>tinglashni
  tashlab boʻlmaydi.</b> Aynan shuning uchun bu kursning har bir
  oʻqish matnida audio bor.</p>
</div>

<p>Imtihon koʻp mamlakatlarda yiliga <b>ikki marta</b> — yozda va
qishda — oʻtkaziladi, lekin baʼzi mamlakatlarda yiliga bir marta.
Sana, ariza muddati va topshirish joyi har yili oʻzgaradi, shuning
uchun ularni bu yerdan emas, <b>JLPT ning rasmiy manbasidan</b>
tekshiring.</p>

<h3>4. Har kuni qiladigan toʻrtta ish</h3>

<div class="pe-steps">
  <ol>
    <li><b>Bir sahifa oʻqing.</b> Tushunmagan soʻzni belgilang, lekin toʻxtamang — oxirigacha oʻqib, keyin qaytib qarang.</li>
    <li><b>Oʻn daqiqa tinglang.</b> Matnni koʻz bilan kuzatib, ovoz bilan birga oʻqing — bu <ruby>音読<rt>おんどく</rt></ruby>, eng samarali mashq.</li>
    <li><b>Oʻn soʻz yozing.</b> Soʻzni yolgʻiz emas, <b>gap ichida</b> yozing: yolgʻiz soʻz unutiladi, gap qoladi.</li>
    <li><b>Uchta gap tuzing.</b> Bugun oʻqigan narsangiz haqida. Xato boʻlsa ham — yozilgan xato oʻrganilgan xato.</li>
  </ol>
</div>

<div class="pe-call pe-tip">
  <p><b>Bu roʻyxatdagi eng kuchli band — ikkinchisi.</b>
  <ruby>音読<rt>おんどく</rt></ruby> (ovoz chiqarib oʻqish) bir
  vaqtning oʻzida talaffuzni, oʻqish tezligini va eshitishni
  mashq qiladi — uchta ish, oʻn daqiqa. Matnni bir marta jimgina
  oʻqib chiqing, keyin audio bilan birga ovoz chiqarib oʻqing.
  Bir oy qilsangiz, farqini oʻzingiz eshitasiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>毎日<rt>まいにち</rt></ruby><ruby>十分<rt>じゅっぷん</rt></ruby>でも、<span class="pe-hl pe-hl--v"><ruby>続<rt>つづ</rt></ruby>けることが<ruby>大切<rt>たいせつ</rt></ruby>である</span>。</p>
  <p class="pe-ex__uz">Har kuni oʻn daqiqa boʻlsa ham, davom ettirish muhim.</p>
  <p class="pe-ex__why">である<ruby>体<rt>たい</rt></ruby>da (PJ-96) — chunki bu maslahat emas, umumiy fikr. <ruby>続<rt>つづ</rt></ruby>けること — PJ-48 dagi aniqlovchi ergash gap.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>分<rt>わ</rt></ruby>からない<ruby>言葉<rt>ことば</rt></ruby>があっても、<span class="pe-hl pe-hl--s"><ruby>最後<rt>さいご</rt></ruby>まで<ruby>読<rt>よ</rt></ruby>んでみてください</span>。</p>
  <p class="pe-ex__uz">Tushunmaydigan soʻz boʻlsa ham, oxirigacha oʻqib koʻring.</p>
  <p class="pe-ex__why">〜ても (PJ-55) va 〜てみる (PJ-59). Bu — oʻqish odatining eng muhim qoidasi: har soʻzda toʻxtagan odam hech qachon tezlashmaydi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>音読<rt>おんどく</rt></ruby>は、<ruby>読<rt>よ</rt></ruby>む<ruby>力<rt>ちから</rt></ruby>と<ruby>聞<rt>き</rt></ruby>く<ruby>力<rt>ちから</rt></ruby>を<ruby>同時<rt>どうじ</rt></ruby>に<ruby>伸<rt>の</rt></ruby>ばす。</p>
  <p class="pe-ex__uz">Ovoz chiqarib oʻqish oʻqish va tinglash qobiliyatini bir vaqtda oʻstiradi.</p>
  <p class="pe-ex__why">Oddiy shaklda tugagan xabar gapi — yaʼni bu matn である<ruby>体<rt>たい</rt></ruby>da. Feʼl oʻzgarmaydi, shuning uchun である koʻrinmaydi (PJ-96).</p>
</div>

<h3>5. Real muddat</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Maqsad</th><th>Kuniga 30 daqiqa</th><th>Kuniga 2 soat</th></tr>
  <tr><td class="pj-stem">N4 → N3</td><td class="pj-res">10–12 oy</td><td class="pj-uz">4–6 oy</td></tr>
  <tr><td class="pj-stem">N3 → N2</td><td class="pj-res">1,5–2 yil</td><td class="pj-uz">8–12 oy</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Kuniga ikki soat — bir hafta; kuniga oʻttiz daqiqa —
  besh yil.</b> Bu darsdagi eng qimmatli gap shu. Koʻp odam
  birinchi hafta kuniga uch soat oʻqiydi, charchaydi, bir oy
  yoʻqoladi va qaytganda hammasini unutgan boʻladi.
  <ruby>三日坊主<rt>みっかぼうず</rt></ruby> — PJ-98 da koʻrgan
  soʻzimiz — aynan shu odam. Uning davosi ham oʻsha darsda edi:
  <ruby>塵<rt>ちり</rt></ruby>も<ruby>積<rt>つ</rt></ruby>もれば
  <ruby>山<rt>やま</rt></ruby>となる.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">継</span>
    <span class="pj-kanji__uz">davom ettirmoq, ulamoq</span>
    <span class="pj-kanji__on">オン: ケイ</span>
    <span class="pj-kanji__kun">KUN: つ(ぐ)</span>
    <span class="pj-kanji__note">継続 (けいぞく) — davomiylik · 継ぐ (つぐ) — davom ettirmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">慣</span>
    <span class="pj-kanji__uz">odatlanmoq</span>
    <span class="pj-kanji__on">オン: カン</span>
    <span class="pj-kanji__kun">KUN: な(れる)</span>
    <span class="pj-kanji__note">習慣 (しゅうかん) — odat · 慣れる (なれる) — koʻnikmoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">標</span>
    <span class="pj-kanji__uz">belgi, moʻljal</span>
    <span class="pj-kanji__on">オン: ヒョウ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">目標 (もくひょう) — maqsad · 標識 (ひょうしき) — yoʻl belgisi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Va nihoyat, oʻzbek oʻquvchisiga tegishli bitta aniq
  maslahat.</b> Yapon tilini oʻrganayotgan koʻp yurtdoshimiz
  materialni ingliz tili orqali oʻqiydi — darslik inglizcha,
  izoh inglizcha, lugʻat inglizcha. Bu <em>ikki marta</em>
  tarjima qilish demak: yaponchadan inglizchaga, keyin
  inglizchadan oʻzbekchaga. Har bir tarjimada maʼnoning bir
  qismi toʻkiladi, va eng yomoni — grammatika tushuntirishlari
  ingliz tilining mantiqiga moslab yozilgan boʻladi, sizniki
  esa boshqa. Iloji boricha <b>oʻzbekcha yoki toʻgʻridan-toʻgʻri
  yaponcha</b> manbadan foydalaning. Bu kurs boshdan oxirigacha
  shuning uchun oʻzbek tilida yozilgan.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Kanjini yolgʻiz, roʻyxat boʻyicha yodlash</p>
  <p class="pe-fix__good">✓ Kanjini <b>soʻz ichida</b> yodlang: <ruby>学<rt>がく</rt></ruby> emas, <ruby>学校<rt>がっこう</rt></ruby> va <ruby>学生<rt>がくせい</rt></ruby>. Oʻqilish kontekstdan keladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Grammatikani tugatib, keyin oʻqishni boshlash</p>
  <p class="pe-fix__good">✓ Birinchi kundanoq oʻqing. Grammatika matnni tushuntiradi, matn esa grammatikani <b>eslab qoldiradi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Kuniga uch soat, keyin bir oy tanaffus</p>
  <p class="pe-fix__good">✓ Kuniga oʻttiz daqiqa, har kuni. <ruby>継続<rt>けいぞく</rt></ruby> tezlikdan kuchliroq.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Tinglashni «keyinroq» qoldirish</p>
  <p class="pe-fix__good">✓ <ruby>基準点<rt>きじゅんてん</rt></ruby> qoidasi buni kechirmaydi — har bir boʻlimdan alohida eng kam ball kerak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ «Tayyor boʻlganimda gapiraman»</p>
  <p class="pe-fix__good">✓ Hech kim tayyor boʻlmaydi. Bugun uchta gap yozing va birini ovoz chiqarib ayting — <ruby>習慣<rt>しゅうかん</rt></ruby> shundan boshlanadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Hozir siz qaysi darajadasiz va keyingisi qaysi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Mustahkam N4, N3 ga kirib.</b> Keyingisi — <b>N3</b>: taxminan 650 kanji va 3 750 soʻz. Grammatikaning katta qismi sizda bor; qolgani hajm.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Umumiy bal yetarli, lekin tinglashdan juda kam ball olindi. Natija?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Oʻtmaydi.</b> <ruby>基準点<rt>きじゅんてん</rt></ruby> — har bir boʻlimdan alohida eng kam ball talab qilinadi. Shuning uchun tinglash tashlab qoʻyilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. N4 dan N3 gacha nima eng koʻp oshadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Soʻz boyligi</b> — taxminan ikki yarim baravar (1 500 → 3 750). Grammatika emas, hajm va oʻqish tezligi qiyinlashadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>音読<rt>おんどく</rt></ruby> nega samarali?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Uchta ishni birdan qiladi:</b> talaffuz, oʻqish tezligi va eshitish. Audio bilan birga ovoz chiqarib oʻqish — oʻn daqiqada uchta mashq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Kuniga 30 daqiqa bilan N3 gacha qancha vaqt ketadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Taxminan 10–12 oy.</b> Kuniga ikki soat bilan 4–6 oy. Lekin muhimi tezlik emas — <b>uzilishsizlik</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Imtihon sanasini qayerdan bilasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>JLPT ning rasmiy manbasidan.</b> Sana, ariza muddati va topshirish joyi har yili va har mamlakatda oʻzgaradi — bu yerda yozilgan son eskirgan boʻlishi mumkin.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>継続<rt>けいぞく</rt></ruby></b> — davomiylik, uzilmaslik</li>
  <li><b><ruby>習慣<rt>しゅうかん</rt></ruby></b> — odat</li>
  <li><b><ruby>目標<rt>もくひょう</rt></ruby></b> — maqsad, moʻljal</li>
  <li><b><ruby>音読<rt>おんどく</rt></ruby></b> — ovoz chiqarib oʻqish</li>
  <li><b><ruby>読解<rt>どっかい</rt></ruby></b> — oʻqib tushunish</li>
  <li><b><ruby>聴解<rt>ちょうかい</rt></ruby></b> — tinglab tushunish</li>
  <li><b><ruby>語彙<rt>ごい</rt></ruby></b> — soʻz boyligi</li>
  <li><b><ruby>基準点<rt>きじゅんてん</rt></ruby></b> — boʻlim boʻyicha eng kam ball</li>
  <li><b><ruby>慣<rt>な</rt></ruby>れる</b> — koʻnikmoq</li>
  <li><b><ruby>続<rt>つづ</rt></ruby>ける</b> — davom ettirmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Yuzta darsdan keyin esda qoladigan uch narsa</p>
  <ul>
    <li><b>Grammatika sizning qiyin qismingiz emas edi</b> — oʻzbek tili yapon tiliga shu jihatdan qarindosh. Qolgani hajm, hajm esa takror bilan olinadi.</li>
    <li><b>Har kuni bir sahifa.</b> Kuniga uch soat emas — har kuni. <ruby>塵<rt>ちり</rt></ruby>も<ruby>積<rt>つ</rt></ruby>もれば<ruby>山<rt>やま</rt></ruby>となる.</li>
    <li><b>Bu kurs tugadi, til tugamadi.</b> Siz endi oʻqiy olasiz — demak bundan keyin sizga ustoz emas, matn kerak. Yaxshi yoʻl boʻlsin: <ruby>頑張<rt>がんば</rt></ruby>ってください。</li>
  </ul>
</div>
""",
    },
]
