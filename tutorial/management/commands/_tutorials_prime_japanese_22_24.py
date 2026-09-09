# -*- coding: utf-8 -*-
"""Prime Japanese — Block B, darslar 22–24.

Uchta boʻlak: dars + mashq (20 savol) + oʻqish matni (audio bilan).
PJ-20 dan beri hikoya ramkasi istisnosi yoʻq — matnlardagi har bir feʼl
darslarda berilgan boʻlishi shart.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_22_24.py --author=prime
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
        "title": "PJ-22: で va へ — vosita, joy va yoʻnalishning ikkinchi shakli",
        "category": "japanese",
        "order": 22,
        "summary": (
            "に va で farqi — yaponchadagi eng nozik juftliklardan biri: に narsa "
            "TURGAN joyni, で esa ish BAJARILAYOTGAN joyni koʻrsatadi."
        ),
        "stories": ["バスで がっこうへ"],
        "content": """
<h2>PJ-22: で va へ — vosita, joy va yoʻnalishning ikkinchi shakli</h2>

<p>Oʻtgan darsda bitta gapga izoh qoʻygan edim va uni tushuntirmagan edim:
«<ruby>学校<rt>がっこう</rt></ruby><b>で</b><ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます» —
nega bu yerda に emas, <b>で</b>? Bugun shu savolga javob beramiz.</p>

<p>Javob bir jumlada sigʻadi: <b>に narsa turgan joyni, で esa ish bajarilayotgan
joyni koʻrsatadi</b>. Oʻzbekchada ikkalasi ham «-da» — shuning uchun bu farq
oʻzbek oʻquvchi uchun yangi va uni alohida oʻrganish kerak.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>に va で ni bir umrga ajratasiz</li>
    <li>で bilan vositani aytasiz: «avtobusda», «qalamda»</li>
    <li>へ ni yoʻnalish uchun ishlatasiz va uni [e] deb oʻqiysiz</li>
    <li>で ning uchinchi vazifasini — «bilan, yordamida» ni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki xil «-da»</span>
  <span class="pe-chip pe-chip--s">に = TURGAN joy</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">で = ISH bajarilgan joy</span>
</div>

<h3>1. に yoki で — feʼl hal qiladi</h3>

<p>Qaysi birini tanlashni <b>feʼl</b> aytadi. Feʼl <em>harakat</em> bildirsa —
で. Feʼl faqat <em>mavjudlik</em> yoki <em>turish</em> bildirsa — に.</p>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">に — turadi, mavjud</p>
    <p class="pj-pair__form"><ruby>教室<rt>きょうしつ</rt></ruby>に います</p>
    <p>あります · います bilan. Narsa oʻsha yerda <b>bor</b>, hech nima
    qilmaydi.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">で — ish qiladi</p>
    <p class="pj-pair__form"><ruby>教室<rt>きょうしつ</rt></ruby>で <ruby>勉強<rt>べんきょう</rt></ruby>します</p>
    <p>Harakat feʼllari bilan. Oʻsha yerda nimadir <b>bajariladi</b>.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>図書館<rt>としょかん</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>があります。<ruby>図書館<rt>としょかん</rt></ruby>で<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます。</p>
  <p class="pe-ex__rom">toshokan ni hon ga arimasu. toshokan de hon o yomimasu</p>
  <p class="pe-ex__uz">Kutubxonada kitob bor. Kutubxonada kitob oʻqiyman.</p>
  <p class="pe-ex__why">Bir xil joy, ikki xil qoʻshimcha. Birinchi gapda kitob <b>turibdi</b> — に. Ikkinchisida men <b>ish qilyapman</b> — で. Oʻzbekchada ikkalasi ham «kutubxona<em>da</em>».</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu — oʻzbek oʻquvchi uchun yangi farq.</b> Oʻzbekchada bitta «-da»
  ikkala ishni ham bajaradi, shuning uchun sezgingiz bu yerda yordam bermaydi.
  Lekin sinash usuli oson: <em>feʼlga qarang</em>. Agar feʼl
  <ruby>行<rt>い</rt></ruby>きます, <ruby>読<rt>よ</rt></ruby>みます,
  <ruby>食<rt>た</rt></ruby>べます kabi <b>harakat</b> boʻlsa — <b>で</b>. Agar
  あります yoki います boʻlsa — <b>に</b>. Boshqa hech narsani oʻylash
  kerak emas.</p>
</div>

<h3>2. で — vosita: «nima bilan»</h3>

<p><b>で</b> ning ikkinchi vazifasi: ish <em>nima yordamida</em> bajarilishini
koʻrsatadi. Transport, asbob, til — hammasi で bilan.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Maʼnosi</th><th>Turi</th></tr>
  <tr><td>バス<b>で</b><ruby>行<rt>い</rt></ruby>きます</td>
      <td class="pj-uz">avtobusda boraman</td><td class="pj-uz">transport</td></tr>
  <tr><td><ruby>電車<rt>でんしゃ</rt></ruby><b>で</b><ruby>行<rt>い</rt></ruby>きます</td>
      <td class="pj-uz">poyezdda boraman</td><td class="pj-uz">transport</td></tr>
  <tr><td><ruby>鉛筆<rt>えんぴつ</rt></ruby><b>で</b><ruby>書<rt>か</rt></ruby>きます</td>
      <td class="pj-uz">qalamda yozaman</td><td class="pj-uz">asbob</td></tr>
  <tr><td><ruby>日本語<rt>にほんご</rt></ruby><b>で</b><ruby>話<rt>はな</rt></ruby>します</td>
      <td class="pj-uz">yaponchada gaplashaman</td><td class="pj-uz">til</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Yurish esa で olmaydi.</b> «Piyoda» — <ruby>歩<rt>ある</rt></ruby>いて,
  alohida ibora. Chunki oyoq vosita emas, harakatning oʻzi. Buni hozircha
  tayyor soʻz sifatida yodlab qoʻying.</p>
</div>

<h3>3. へ — yoʻnalishning ikkinchi shakli</h3>

<p><b>へ</b> ham に kabi yoʻnalishni bildiradi. Farqi juda nozik va boshlangʻich
darajada deyarli sezilmaydi — lekin bitta narsani albatta bilish kerak.</p>

<div class="pj-say">
  <span class="pj-say__from">へ</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to">[e]</span>
  <span class="pj-say__why">qoʻshimcha boʻlganda «he» emas — は kabi</span>
</div>

<div class="pe-call pe-rule">
  <p><b>Yana bir «yozilishi boshqa, oʻqilishi boshqa» qoʻshimcha.</b>
  <b>は</b> [wa], <b>を</b> [o], va endi <b>へ</b> [e]. Uchalasi ham eski
  yozuvdan qolgan va uchalasi ham <em>faqat qoʻshimcha sifatida</em> shunday
  oʻqiladi. Soʻz ichida へ oddiy «he» boʻlib qoladi.</p>
</div>

<div class="pj-pair">
  <div class="pj-pair__side">
    <p class="pj-pair__h">に — MANZIL</p>
    <p class="pj-pair__form"><ruby>学校<rt>がっこう</rt></ruby>に</p>
    <p>Aniq borish nuqtasi. «Maktabga» — va maktabga yetib boraman.</p>
  </div>
  <div class="pj-pair__side pj-pair__side--kata">
    <p class="pj-pair__h">へ — TOMON</p>
    <p class="pj-pair__form"><ruby>学校<rt>がっこう</rt></ruby>へ</p>
    <p>Yoʻnalish, tomon. «Maktab tomonga» — yetib borish urgʻulanmaydi.</p>
  </div>
</div>

<div class="pe-call pe-warn">
  <p><b>Amalda ikkalasi ham toʻgʻri.</b> <ruby>学校<rt>がっこう</rt></ruby>に
  <ruby>行<rt>い</rt></ruby>きます va <ruby>学校<rt>がっこう</rt></ruby>へ
  <ruby>行<rt>い</rt></ruby>きます — ikkalasi ham «maktabga boraman». Farq
  shu qadar nozikki, yaponlar ham ularni almashtirib ishlatadi. <b>へ</b>
  biroz rasmiyroq va yozma tilda koʻproq uchraydi; xat va manzillarda esa
  deyarli doim へ ishlatiladi. Boshlovchi uchun tavsiya: <b>に ni tanlang</b>,
  va へ ni koʻrganingizda tanib oling.</p>
</div>

<h3>4. Uchta qoʻshimcha bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qoʻshimcha</th><th>Vazifasi</th><th>Feʼl turi</th><th>Misol</th></tr>
  <tr><td class="pj-stem">に</td><td class="pj-uz">turgan joy</td>
      <td class="pj-uz">あります · います</td>
      <td><ruby>家<rt>いえ</rt></ruby>にいます</td></tr>
  <tr><td class="pj-stem">に</td><td class="pj-uz">manzil</td>
      <td class="pj-uz">harakat feʼli</td>
      <td><ruby>家<rt>いえ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ります</td></tr>
  <tr><td class="pj-stem">へ</td><td class="pj-uz">tomon</td>
      <td class="pj-uz">harakat feʼli</td>
      <td><ruby>家<rt>いえ</rt></ruby>へ<ruby>帰<rt>かえ</rt></ruby>ります</td></tr>
  <tr><td class="pj-stem">で</td><td class="pj-uz">ish joyi</td>
      <td class="pj-uz">harakat feʼli</td>
      <td><ruby>家<rt>いえ</rt></ruby>で<ruby>読<rt>よ</rt></ruby>みます</td></tr>
  <tr><td class="pj-stem">で</td><td class="pj-uz">vosita</td>
      <td class="pj-uz">har qanday</td>
      <td>バスで<ruby>行<rt>い</rt></ruby>きます</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>毎日<rt>まいにち</rt></ruby>バスで<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。<ruby>教室<rt>きょうしつ</rt></ruby>で<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>勉強<rt>べんきょう</rt></ruby>します。</p>
  <p class="pe-ex__rom">mainichi basu de gakkō e ikimasu. kyōshitsu de nihongo o benkyō shimasu</p>
  <p class="pe-ex__uz">Har kuni avtobusda maktabga boraman. Sinfda yapon tilini oʻrganaman.</p>
  <p class="pe-ex__why">Bitta gapda で ikki xil ishda: <b>バスで</b> — vosita, <b><ruby>教室<rt>きょうしつ</rt></ruby>で</b> — ish joyi. Va <b>へ</b> yoʻnalish beryapti.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>教室<rt>きょうしつ</rt></ruby>に<ruby>勉強<rt>べんきょう</rt></ruby>します</p>
  <p class="pe-fix__good">✓ <ruby>教室<rt>きょうしつ</rt></ruby><b>で</b>… — <ruby>勉強<rt>べんきょう</rt></ruby>します harakat feʼli, demak で.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>教室<rt>きょうしつ</rt></ruby>で<ruby>先生<rt>せんせい</rt></ruby>がいます</p>
  <p class="pe-fix__good">✓ <ruby>教室<rt>きょうしつ</rt></ruby><b>に</b>… — います mavjudlik bildiradi, demak に.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ へ ni «he» deb oʻqish</p>
  <p class="pe-fix__good">✓ Qoʻshimcha boʻlganda <b>[e]</b>. は [wa] va を [o] bilan bir qatorda — uchta eski qoʻshimcha.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>教室<rt>きょうしつ</rt></ruby>___<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>みます — に yoki で?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>で</b> — <ruby>読<rt>よ</rt></ruby>みます harakat feʼli, ish oʻsha yerda bajarilyapti.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>教室<rt>きょうしつ</rt></ruby>___<ruby>先生<rt>せんせい</rt></ruby>がいます — に yoki で?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>に</b> — います mavjudlikni bildiradi, harakat emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Avtobusda boraman» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>バス<b>で</b><ruby>行<rt>い</rt></ruby>きます。 — で bu yerda <b>vosita</b>: nima yordamida.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. へ qanday oʻqiladi va u yana qaysi ikkita qoʻshimchaga oʻxshaydi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>[e]</b>. は [wa] va を [o] bilan bir qatorda — uchalasi ham eski yozuvdan qolgan va faqat qoʻshimcha sifatida shunday oʻqiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. に va で ni qanday tez ajratasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Feʼlga qarang.</b> あります / います — <b>に</b>. Harakat feʼli — <b>で</b>. Boshqa hech narsani oʻylash kerak emas.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>で</b> — …da (ish joyi), …bilan (vosita)</li>
  <li><b>へ</b> — …tomonga, [e]</li>
  <li><b>バス</b> — avtobus</li>
  <li><b><ruby>電車<rt>でんしゃ</rt></ruby></b> — poyezd</li>
  <li><b><ruby>自転車<rt>じてんしゃ</rt></ruby></b> — velosiped</li>
  <li><b><ruby>鉛筆<rt>えんぴつ</rt></ruby></b> — qalam</li>
  <li><b><ruby>話<rt>はな</rt></ruby>します</b> — gaplashaman</li>
  <li><b><ruby>歩<rt>ある</rt></ruby>いて</b> — piyoda</li>
  <li><b><ruby>図書館<rt>としょかん</rt></ruby></b> — kutubxona</li>
  <li><b><ruby>公園<rt>こうえん</rt></ruby></b> — bogʻ, skver</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>に</b> = turgan joy (あります · います), <b>で</b> = ish bajarilgan joy (harakat feʼli).</li>
    <li><b>で</b> vositani ham bildiradi: バスで, <ruby>鉛筆<rt>えんぴつ</rt></ruby>で.</li>
    <li><b>へ</b> [e] — に ning rasmiyroq varianti; boshlovchi <b>に</b> ni tanlasa boʻladi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-23: 〜ました / 〜ませんでした — oʻtgan zamon",
        "category": "japanese",
        "order": 23,
        "summary": (
            "Yaponchaning ikkinchi va oxirgi zamoni. です ham, feʼl ham bir xil "
            "mantiq bilan oʻtgan zamonga oʻtadi."
        ),
        "stories": ["きのうの にちようび"],
        "content": """
<h2>PJ-23: 〜ました / 〜ませんでした — oʻtgan zamon</h2>

<p>PJ-20 da aytgan edim: yapon tilida kelasi zamon yoʻq, faqat <b>oʻtgan</b>
va <b>oʻtmagan</b> bor. Oʻtmaganini oʻrgandingiz. Bugun ikkinchisi keladi —
va shu bilan <b>yapon tilining butun zamon tizimi tugaydi</b>.</p>

<p>Ikki dona shakl, ikkitasi ham qoidali. Ingliz tilida oʻnlab tartibsiz
feʼl bor; yaponchada esa <b>bitta istisno ham yoʻq</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ます → ました bilan oʻtgan zamonni yasaysiz</li>
    <li>ません → ませんでした bilan oʻtgan zamon inkorini yasaysiz</li>
    <li>です ning oʻtgan shakli でした ni oʻrganasiz</li>
    <li>Oʻtgan zamon vaqt soʻzlarini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Butun zamon tizimi</span>
  <span class="pe-chip pe-chip--v">ます / ません</span>
  <span class="pe-op">↔</span>
  <span class="pe-chip pe-chip--o">ました / ませんでした</span>
</div>

<h3>1. ました — «qildim»</h3>

<p>Qoida bir qatorda sigʻadi: <b>ます</b> ni <b>ました</b> ga almashtiring.
Boshqa hech narsa oʻzgarmaydi — na feʼl oʻzagi, na qoʻshimchalar.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Hozirgi</th><th>Oʻtgan</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res"><ruby>行<rt>い</rt></ruby>きます</td>
      <td class="pj-end"><ruby>行<rt>い</rt></ruby>きました</td><td class="pj-uz">bordim</td></tr>
  <tr><td class="pj-res"><ruby>食<rt>た</rt></ruby>べます</td>
      <td class="pj-end"><ruby>食<rt>た</rt></ruby>べました</td><td class="pj-uz">yedim</td></tr>
  <tr><td class="pj-res"><ruby>読<rt>よ</rt></ruby>みます</td>
      <td class="pj-end"><ruby>読<rt>よ</rt></ruby>みました</td><td class="pj-uz">oʻqidim</td></tr>
  <tr><td class="pj-res">します</td><td class="pj-end">しました</td><td class="pj-uz">qildim</td></tr>
  <tr><td class="pj-res"><ruby>来<rt>き</rt></ruby>ます</td>
      <td class="pj-end"><ruby>来<rt>き</rt></ruby>ました</td><td class="pj-uz">keldim</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu — kursdagi eng saxiy qoida.</b> Oʻzbekchada oʻtgan zamon uchun
  bir necha shakl bor («bordim», «borgan edim», «borardim») va feʼl oʻzagi
  ham oʻzgarishi mumkin. Yaponchada esa <b>bitta almashtirish</b>:
  ます → ました. Istisno <em>yoʻq</em>. Bu tilda oʻtgan zamon eng oson
  mavzulardan biri.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>昨日<rt>きのう</rt></ruby><ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>ました。</p>
  <p class="pe-ex__rom">kinō ēga o mimashita</p>
  <p class="pe-ex__uz">Kecha kino koʻrdim.</p>
  <p class="pe-ex__why"><ruby>昨日<rt>きのう</rt></ruby> («kecha») — oʻtgan zamon vaqt soʻzi. Unga ham に qoʻyilmaydi, xuddi <ruby>明日<rt>あした</rt></ruby> kabi.</p>
</div>

<h3>2. ませんでした — «qilmadim»</h3>

<p>Inkor uzunroq, lekin mantiqi shaffof: <b>ません</b> (inkor) +
<b>でした</b> (oʻtgan). Ikki boʻlak qoʻshiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Yaponcha</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">hozirgi tasdiq</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>きます</td><td class="pj-uz">boraman</td></tr>
  <tr><td class="pj-stem">hozirgi inkor</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>きません</td><td class="pj-uz">bormayman</td></tr>
  <tr><td class="pj-stem">oʻtgan tasdiq</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>きました</td><td class="pj-uz">bordim</td></tr>
  <tr><td class="pj-stem">oʻtgan inkor</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>きませんでした</td><td class="pj-uz">bormadim</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Toʻrtta katak — butun tizim.</b> Har qanday muloyim feʼl shu toʻrt
  shakldan birida boʻladi. Boshqa zamon yoʻq. Bu jadvalni yodlab qoʻysangiz,
  yapon feʼlining zamon qismini butunlay yopgan boʻlasiz.</p>
</div>

<h3>3. です → でした</h3>

<p>Kesim ham oʻtgan zamonga oʻtadi, va oʻsha でした boʻlagi bu yerda ham
ishlaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Yaponcha</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-res">です</td><td class="pj-uz">…dir</td></tr>
  <tr><td class="pj-stem">hozirgi inkor</td><td class="pj-res">ではありません</td><td class="pj-uz">…emas</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-res">でした</td><td class="pj-uz">…edi</td></tr>
  <tr><td class="pj-stem">oʻtgan inkor</td><td class="pj-res">ではありませんでした</td><td class="pj-uz">…emas edi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>昨日<rt>きのう</rt></ruby>は<ruby>日曜日<rt>にちようび</rt></ruby>でした。</p>
  <p class="pe-ex__rom">kinō wa nichiyōbi deshita</p>
  <p class="pe-ex__uz">Kecha yakshanba edi.</p>
  <p class="pe-ex__why">です → でした. Oxirgi shakl <b>ではありませんでした</b> uzun koʻrinadi, lekin u shunchaki «ではありません + でした».</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Kundalik nutqda qisqaroq shakl bor:</b>
  <b>じゃありませんでした</b>, yoki undan ham koʻproq eshitiladigan
  <b>じゃなかったです</b>. Ikkinchisi PJ-45 dagi oddiy shakldan yasalgan —
  hozircha uni faqat tanib olsangiz yetadi.</p>
</div>

<h3>4. Nega yaponcha oʻtgan zamon shunchalik oson</h3>

<p>Bir daqiqa toʻxtab, nimaga erishganingizni koʻring. Ingliz tilida oʻtgan
zamon uchun yuzdan ortiq tartibsiz feʼl yodlanadi (go → went, eat → ate).
Rus tilida feʼl jinsga va songa qarab oʻzgaradi. Oʻzbekchada bir necha
oʻtgan zamon shakli bor va ular maʼno jihatidan farq qiladi.</p>

<p>Yapon tilida esa <b>bitta almashtirish</b>, <b>hamma feʼl uchun</b>,
<b>istisnosiz</b>. Bu tasodif emas: yapon feʼli <em>agglutinativ</em> — yaʼni
oʻzak qimirlamaydi, unga qoʻshimchalar ketma-ket yopishadi. Xuddi oʻzbek
tilidagi kabi.</p>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bilan taqqoslang:</b> «bor-di-m», «bor-ma-di-m» — oʻzak
  <em>bor</em> qimirlamaydi, qoʻshimchalar ketma-ket qoʻshiladi. Yaponcha
  <ruby>行<rt>い</rt></ruby>き-ませ-ん-でした ham xuddi shunday qurilgan:
  har bir boʻlak oʻz maʼnosini olib keladi. Bu — ikki tilning eng chuqur
  oʻxshashligi va u butun kurs davomida sizga yordam beradi.</p>
</div>

<h3>5. Oʻtgan zamon vaqt soʻzlari</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>昨日<rt>きのう</rt></ruby></td><td class="pj-res">kinō</td><td class="pj-uz">kecha</td></tr>
  <tr><td><ruby>一昨日<rt>おととい</rt></ruby></td><td class="pj-res">ototoi</td><td class="pj-uz">avvalgi kun</td></tr>
  <tr><td><ruby>先週<rt>せんしゅう</rt></ruby></td><td class="pj-res">senshū</td><td class="pj-uz">oʻtgan hafta</td></tr>
  <tr><td><ruby>先月<rt>せんげつ</rt></ruby></td><td class="pj-res">sengetsu</td><td class="pj-uz">oʻtgan oy</td></tr>
  <tr><td><ruby>去年<rt>きょねん</rt></ruby></td><td class="pj-res">kyonen</td><td class="pj-uz">oʻtgan yil</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b><ruby>先<rt>せん</rt></ruby> belgisiga eʼtibor bering.</b> U «oldingi» degan maʼnoni beradi va
  <ruby>先週<rt>せんしゅう</rt></ruby>, <ruby>先月<rt>せんげつ</rt></ruby> da
  takrorlanadi — lekin <b>«oʻtgan yil»</b> uchun ishlatilmaydi: u
  <ruby>去年<rt>きょねん</rt></ruby>. Bu tartibsizlikni yodlab qoʻying,
  chunki <ruby>先年<rt>せんねん</rt></ruby> deb aytish tabiiy tuyuladi, lekin
  notoʻgʻri.</p>
</div>

<h3>6. Oʻtgan zamon va PJ-16 dagi «bor» gapi</h3>

<p>あります va います ham oʻtgan zamonga oʻtadi, va ular xuddi shu qoidaga
boʻysunadi:</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Hozirgi</th><th>Oʻtgan</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res">あります</td><td class="pj-end">ありました</td><td class="pj-uz">bor edi</td></tr>
  <tr><td class="pj-res">ありません</td><td class="pj-end">ありませんでした</td><td class="pj-uz">yoʻq edi</td></tr>
  <tr><td class="pj-res">います</td><td class="pj-end">いました</td><td class="pj-uz">bor edi (jonli)</td></tr>
  <tr><td class="pj-res">いません</td><td class="pj-end">いませんでした</td><td class="pj-uz">yoʻq edi (jonli)</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p>Jonli va jonsiz farqi oʻtgan zamonda ham saqlanadi — mushuk uchun
  <b>いました</b>, kitob uchun <b>ありました</b>.</p>
</div>

<h3>7. Savol va javob</h3>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>昨日<rt>きのう</rt></ruby><ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きましたか。</p>
  <p class="pe-ex__rom">kinō gakkō e ikimashita ka</p>
  <p class="pe-ex__uz">Kecha maktabga bordingizmi?</p>
  <p class="pe-ex__why">Javob: <b>はい、<ruby>行<rt>い</rt></ruby>きました</b> yoki <b>いいえ、<ruby>行<rt>い</rt></ruby>きませんでした</b>. Savol yasash usuli oʻzgarmadi — か oʻsha joyda.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>きませんした</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>き<b>ませんでした</b> — ません + でした, ikki toʻliq boʻlak.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>昨日<rt>きのう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きました</p>
  <p class="pe-fix__good">✓ <ruby>昨日<rt>きのう</rt></ruby><ruby>行<rt>い</rt></ruby>きました — <ruby>昨日<rt>きのう</rt></ruby> oʻzi vaqtni bildiradi, に kerak emas (PJ-21).</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>先年<rt>せんねん</rt></ruby> («oʻtgan yil»)</p>
  <p class="pe-fix__good">✓ <ruby>去年<rt>きょねん</rt></ruby> — <ruby>先<rt>せん</rt></ruby> <ruby>週<rt>しゅう</rt></ruby> va <ruby>月<rt>げつ</rt></ruby> bilan ishlaydi, yil bilan emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>食<rt>た</rt></ruby>べます ning oʻtgan zamoni qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べました</b> — ます oʻrniga ました. Istisno yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Bormadim» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>行<rt>い</rt></ruby>き<b>ませんでした</b> — ません (inkor) + でした (oʻtgan).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. です ning oʻtgan shakli qaysi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>でした</b>. Oʻtgan inkor esa <b>ではありませんでした</b> — «ではありません + でした».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Yapon tilida nechta zamon bor?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Ikkita</b>: oʻtgan va oʻtmagan. Kelasi zamon alohida shaklga ega emas — uni vaqt soʻzi koʻrsatadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Oʻtgan yil» qanday aytiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>去年<rt>きょねん</rt></ruby></b> — <ruby>先年<rt>せんねん</rt></ruby> emas. <ruby>先<rt>せん</rt></ruby> faqat hafta va oy bilan ishlaydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ました</b> — oʻtgan zamon</li>
  <li><b>〜ませんでした</b> — oʻtgan zamon inkori</li>
  <li><b>でした</b> — …edi</li>
  <li><b><ruby>昨日<rt>きのう</rt></ruby></b> — kecha</li>
  <li><b><ruby>一昨日<rt>おととい</rt></ruby></b> — avvalgi kun</li>
  <li><b><ruby>先週<rt>せんしゅう</rt></ruby></b> — oʻtgan hafta</li>
  <li><b><ruby>先月<rt>せんげつ</rt></ruby></b> — oʻtgan oy</li>
  <li><b><ruby>去年<rt>きょねん</rt></ruby></b> — oʻtgan yil</li>
  <li><b><ruby>会<rt>あ</rt></ruby>いました</b> — uchrashdim</li>
  <li><b><ruby>買<rt>か</rt></ruby>いました</b> — sotib oldim</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>ます → ました</b>, <b>ません → ませんでした</b>. Istisno <b>yoʻq</b>.</li>
    <li><b>です → でした</b>, va oʻtgan inkor <b>ではありませんでした</b>.</li>
    <li>Yapon tilida <b>ikkita</b> zamon bor: oʻtgan va oʻtmagan. Tizim tugadi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-24: Vaqt — soat, hafta kunlari, 〜から 〜まで",
        "category": "japanese",
        "order": 24,
        "summary": (
            "Soatni aytish, hafta kunlarini ishlatish va から〜まで bilan «…dan …gacha» "
            "deyish — kundalik hayotning vaqt tili."
        ),
        "stories": ["なんじから なんじまで"],
        "content": """
<h2>PJ-24: Vaqt — soat, hafta kunlari, 〜から 〜まで</h2>

<p>Sonlarni PJ-12 da oʻrgandingiz, <b>に</b> ni PJ-21 da. Endi ikkalasini
birlashtiramiz va vaqtni <em>ishlatishni</em> oʻrganamiz: soat nechada,
qaysi kuni, qachondan qachongacha.</p>

<p>Bitta ogohlantirish bilan boshlaymiz: soat aytishda <b>4, 7 va 9</b> yana
oʻsha eski muammoni keltiradi — va bu safar ular <em>boshqacha</em>
tanlanadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Soatni aytasiz va uning uchta istisnosini bilasiz</li>
    <li>Daqiqani qoʻshasiz: 〜<ruby>分<rt>ふん</rt></ruby></li>
    <li>から va まで bilan oraliq aytasiz</li>
    <li>Hafta kunlari bilan gap tuzasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oraliq</span>
  <span class="pe-chip pe-chip--s">A</span>
  <span class="pe-chip pe-chip--opt">から</span>
  <span class="pe-chip pe-chip--o">B</span>
  <span class="pe-chip pe-chip--opt">まで</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--v">A dan B gacha</span>
</div>

<h3>1. Soat — 〜<ruby>時<rt>じ</rt></ruby></h3>

<p>Son + <b><ruby>時<rt>じ</rt></ruby></b>. Oddiy — uchta istisnodan tashqari.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soat</th><th>Yaponcha</th><th>Oʻqilishi</th><th>Diqqat</th></tr>
  <tr><td>1</td><td><ruby>一時<rt>いちじ</rt></ruby></td><td class="pj-res">ichiji</td><td class="pj-uz">—</td></tr>
  <tr><td>4</td><td><ruby>四時<rt>よじ</rt></ruby></td><td class="pj-res">yoji</td><td class="pj-uz"><b>よんじ EMAS</b></td></tr>
  <tr><td>7</td><td><ruby>七時<rt>しちじ</rt></ruby></td><td class="pj-res">shichiji</td><td class="pj-uz"><b>ななじ EMAS</b></td></tr>
  <tr><td>9</td><td><ruby>九時<rt>くじ</rt></ruby></td><td class="pj-res">kuji</td><td class="pj-uz"><b>きゅうじ EMAS</b></td></tr>
  <tr><td>10</td><td><ruby>十時<rt>じゅうじ</rt></ruby></td><td class="pj-res">jūji</td><td class="pj-uz">—</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>4 yana boshqacha!</b> Oylarda 4 <b>し</b> edi
  (<ruby>四月<rt>しがつ</rt></ruby>), soatda esa <b>よ</b> —
  <ruby>四時<rt>よじ</rt></ruby>. Na «よん», na «し». Bu yapon tilidagi eng
  tartibsiz son va uni har bir sanoq soʻzi bilan alohida yodlash kerak.
  7 va 9 esa oylardagi kabi: <b>しち</b> va <b>く</b>.</p>
</div>

<h3>2. Daqiqa — 〜<ruby>分<rt>ふん</rt></ruby></h3>

<p>Daqiqada tovush <b>oʻzgaradi</b>: baʼzi sonlardan keyin ふん, baʼzilaridan
keyin ぷん. Bu PJ-12 dagi ひゃく → びゃく → ぴゃく bilan bir xil hodisa.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Daqiqa</th><th>Oʻqilishi</th><th>Daqiqa</th><th>Oʻqilishi</th></tr>
  <tr><td>1<ruby>分<rt>ぷん</rt></ruby></td><td class="pj-res">ippun</td>
      <td>5<ruby>分<rt>ふん</rt></ruby></td><td class="pj-res">gofun</td></tr>
  <tr><td>2<ruby>分<rt>ふん</rt></ruby></td><td class="pj-res">nifun</td>
      <td>6<ruby>分<rt>ぷん</rt></ruby></td><td class="pj-res">roppun</td></tr>
  <tr><td>3<ruby>分<rt>ぷん</rt></ruby></td><td class="pj-res">sanpun</td>
      <td>10<ruby>分<rt>ぷん</rt></ruby></td><td class="pj-res">juppun</td></tr>
  <tr><td>4<ruby>分<rt>ふん</rt></ruby></td><td class="pj-res">yonpun</td>
      <td>30<ruby>分<rt>ぷん</rt></ruby></td><td class="pj-res">sanjuppun</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Yarim soat uchun qisqa soʻz bor:</b> <b><ruby>半<rt>はん</rt></ruby></b>.
  «<ruby>七時半<rt>しちじはん</rt></ruby>» = «yetti yarim» —
  <ruby>三十分<rt>さんじゅっぷん</rt></ruby> deb aytishdan ancha
  qulayroq va yaponlar deyarli doim shuni ishlatadi.</p>
</div>

<h3>3. から va まで — «dan» va «gacha»</h3>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>九時<rt>くじ</rt></ruby></span>
  <span class="pj-joshi__p">から<small>DAN</small></span>
  <span class="pj-joshi__n"><ruby>五時<rt>ごじ</rt></ruby></span>
  <span class="pj-joshi__p">まで<small>GACHA</small></span>
  <span class="pj-joshi__v"><ruby>働<rt>はたら</rt></ruby>きます</span>
  <span class="pj-joshi__uz">Toʻqqizdan beshgacha ishlayman.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu ham oʻzbekchaga aynan mos tushadi.</b> «Toʻqqiz<em>dan</em>
  besh<em>gacha</em>» — ikkala qoʻshimcha ham soʻzga yopishadi va shu
  tartibda turadi. Yaponchada <b>から</b> = «-dan», <b>まで</b> = «-gacha».
  Ular faqat vaqt bilan emas, joy bilan ham ishlaydi:
  <ruby>家<rt>いえ</rt></ruby>から<ruby>学校<rt>がっこう</rt></ruby>まで —
  «uydan maktabgacha».</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>月曜日<rt>げつようび</rt></ruby>から<ruby>金曜日<rt>きんようび</rt></ruby>まで<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。</p>
  <p class="pe-ex__rom">getsuyōbi kara kin-yōbi made gakkō e ikimasu</p>
  <p class="pe-ex__uz">Dushanbadan jumagacha maktabga boraman.</p>
  <p class="pe-ex__why">から va まで hafta kunlari bilan ham ishlaydi. Diqqat: bu yerda <b>に qoʻyilmaydi</b> — から va まで oʻzi vaqt munosabatini bildiradi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>から yolgʻiz ham ishlatiladi</b> — «…dan (boshlab)»:
  «<ruby>九時<rt>くじ</rt></ruby>から<ruby>始<rt>はじ</rt></ruby>まります»
  («toʻqqizdan boshlanadi»). Xuddi shunday まで ham yolgʻiz turishi mumkin.
  Ikkalasi doim juft boʻlishi shart emas.</p>
</div>

<h3>4. Hafta kunlari bilan gap</h3>

<p>Hafta kunlarini PJ-12 da koʻrgan edingiz. Endi ularni gapda ishlatamiz —
va bu yerda bitta nozik joy bor.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Gap</th><th>に bormi</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>月曜日<rt>げつようび</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます</td>
      <td class="pj-end">ha</td><td class="pj-uz">dushanba kuni boraman</td></tr>
  <tr><td><ruby>月曜日<rt>げつようび</rt></ruby>は<ruby>行<rt>い</rt></ruby>きます</td>
      <td class="pj-stem">は</td><td class="pj-uz">dushanba kuni esa boraman (taqqoslash)</td></tr>
  <tr><td><ruby>毎週<rt>まいしゅう</rt></ruby><ruby>行<rt>い</rt></ruby>きます</td>
      <td class="pj-end">yoʻq</td><td class="pj-uz">har hafta boraman</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Qoida oʻzgarmadi</b> (PJ-21): <b>aniq</b> vaqtga に qoʻyiladi, oʻzi
  vaqtni bildiradigan soʻzga qoʻyilmaydi. Hafta kuni — aniq nuqta, demak
  に oladi. <ruby>毎週<rt>まいしゅう</rt></ruby> («har hafta») esa
  <ruby>毎日<rt>まいにち</rt></ruby> kabi — に olmaydi.</p>
</div>

<h3>5. <ruby>午前<rt>ごぜん</rt></ruby> va <ruby>午後<rt>ごご</rt></ruby></h3>

<p>Yaponiyada kundalik nutqda <b>12 soatlik</b> tizim ishlatiladi, shuning
uchun «tushdan oldin» va «tushdan keyin» ni aytish kerak boʻladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pj-stem"><ruby>午前<rt>ごぜん</rt></ruby></td><td class="pj-uz">tushdan oldin</td>
      <td><ruby>午前<rt>ごぜん</rt></ruby><ruby>九時<rt>くじ</rt></ruby> — ertalabki 9</td></tr>
  <tr><td class="pj-stem"><ruby>午後<rt>ごご</rt></ruby></td><td class="pj-uz">tushdan keyin</td>
      <td><ruby>午後<rt>ごご</rt></ruby><ruby>三時<rt>さんじ</rt></ruby> — kunduzgi 3</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Tartibga eʼtibor bering:</b> <ruby>午前<rt>ごぜん</rt></ruby> va
  <ruby>午後<rt>ごご</rt></ruby> soatdan <b>oldin</b> turadi — oʻzbekchadagi
  «ertalabki soat toʻqqiz» kabi. Rasmiy jadvallarda esa 24 soatlik tizim ham
  uchraydi va u yerda bu soʻzlar kerak emas.</p>
</div>

<h3>6. Kunning qismlari</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz</th><th>Oʻqilishi</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>朝<rt>あさ</rt></ruby></td><td class="pj-res">asa</td><td class="pj-uz">ertalab</td></tr>
  <tr><td><ruby>昼<rt>ひる</rt></ruby></td><td class="pj-res">hiru</td><td class="pj-uz">tush payti</td></tr>
  <tr><td><ruby>夕方<rt>ゆうがた</rt></ruby></td><td class="pj-res">yūgata</td><td class="pj-uz">kechqurun</td></tr>
  <tr><td><ruby>夜<rt>よる</rt></ruby></td><td class="pj-res">yoru</td><td class="pj-uz">tun</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bularga ham に qoʻyilmaydi</b> — ular <ruby>今日<rt>きょう</rt></ruby>
  kabi oʻzi vaqtni bildiradi: «<ruby>朝<rt>あさ</rt></ruby>コーヒーを
  <ruby>飲<rt>の</rt></ruby>みます». Qoida butun kurs davomida bir xil:
  <b>son bor — に bor, son yoʻq — に yoʻq</b>. Bu — vaqt qoʻshimchalarini
  eslab qolishning eng sodda usuli.</p>
</div>

<h3>7. «Soat nechada?» deb soʻrash</h3>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>何時<rt>なんじ</rt></ruby>から<ruby>何時<rt>なんじ</rt></ruby>まで<ruby>勉強<rt>べんきょう</rt></ruby>しますか。</p>
  <p class="pe-ex__rom">nanji kara nanji made benkyō shimasu ka</p>
  <p class="pe-ex__uz">Soat nechadan nechagacha oʻqiysiz?</p>
  <p class="pe-ex__why"><ruby>何時<rt>なんじ</rt></ruby> — «soat necha». Sanoq soʻzi bilan doim <b>なん</b> (PJ-18). Va u から / まで bilan bemalol birikadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>四時<rt>よんじ</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>四時<rt>よじ</rt></ruby> — soatda 4 «よ». Oylarda esa «し» edi. Har sanoq soʻzi bilan alohida.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>九時<rt>くじ</rt></ruby>から<ruby>五時<rt>ごじ</rt></ruby>までに<ruby>働<rt>はたら</rt></ruby>きます</p>
  <p class="pe-fix__good">✓ …まで<ruby>働<rt>はたら</rt></ruby>きます — から va まで oʻzi vaqt munosabatini bildiradi, に ortiqcha.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>毎週<rt>まいしゅう</rt></ruby>に<ruby>行<rt>い</rt></ruby>きます</p>
  <p class="pe-fix__good">✓ <ruby>毎週<rt>まいしゅう</rt></ruby><ruby>行<rt>い</rt></ruby>きます — «har hafta» oʻzi vaqtni bildiradi, に olmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. Soat 4 qanday aytiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>四時<rt>よじ</rt></ruby></b> — «よじ». Na «よんじ», na «しじ». Soatda 4 uchun maxsus shakl.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Toʻqqizdan beshgacha» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><ruby>九時<rt>くじ</rt></ruby><b>から</b><ruby>五時<rt>ごじ</rt></ruby><b>まで</b>。 — に qoʻyilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Yetti yarim» ni qanday aytasiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>七時半<rt>しちじはん</rt></ruby></b> — <ruby>半<rt>はん</rt></ruby> «yarim» degani va yaponlar deyarli doim shuni ishlatadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>月曜日<rt>げつようび</rt></ruby> ga に qoʻyiladimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Ha</b> — hafta kuni aniq vaqt nuqtasi. Lekin <ruby>毎週<rt>まいしゅう</rt></ruby> ga <b>qoʻyilmaydi</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. から va まで faqat vaqt bilan ishlaydimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq</b> — joy bilan ham: <ruby>家<rt>いえ</rt></ruby>から<ruby>学校<rt>がっこう</rt></ruby>まで («uydan maktabgacha»).</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜<ruby>時<rt>じ</rt></ruby></b> — soat</li>
  <li><b>〜<ruby>分<rt>ふん</rt></ruby></b> — daqiqa</li>
  <li><b><ruby>半<rt>はん</rt></ruby></b> — yarim</li>
  <li><b>から</b> — …dan</li>
  <li><b>まで</b> — …gacha</li>
  <li><b><ruby>何時<rt>なんじ</rt></ruby></b> — soat necha</li>
  <li><b><ruby>毎週<rt>まいしゅう</rt></ruby></b> — har hafta</li>
  <li><b><ruby>働<rt>はたら</rt></ruby>きます</b> — ishlayman</li>
  <li><b><ruby>始<rt>はじ</rt></ruby>まります</b> — boshlanadi</li>
  <li><b><ruby>午前<rt>ごぜん</rt></ruby>・<ruby>午後<rt>ごご</rt></ruby></b> — tushdan oldin, tushdan keyin</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Soatda <b>4 = よじ</b>, 7 = しちじ, 9 = くじ. Oylardagidan farq qiladi.</li>
    <li><b>から … まで</b> = «…dan …gacha», vaqt uchun ham, joy uchun ham. に kerak emas.</li>
    <li>Hafta kuni <b>に oladi</b>, <ruby>毎週<rt>まいしゅう</rt></ruby> esa <b>olmaydi</b>.</li>
  </ul>
</div>
""",
    },
]
