# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-28 (lugʻat shakli) va PJ-29 / PJ-30 (て-shakli).

PJ-27 uchta guruhni berdi. Bu uchlik oʻsha guruhlarni ishga soladi: avval
lugʻat shakliga qaytish, keyin undan て-shaklini yasash — yapon tilidagi eng
koʻp ishlatiladigan ulagich.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_28_30.py --author=prime
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
        "title": "PJ-28: Lugʻat shakli (辞書形) — nega lugʻatda ます yoʻq",
        "category": "japanese",
        "order": 28,
        "summary": (
            "Yapon lugʻatida feʼl ます siz turadi. Bu darsda ます shaklidan "
            "lugʻat shakliga qaytishni oʻrganasiz — bu keyingi barcha "
            "shakllarning boshlangʻich nuqtasi."
        ),
        "stories": ["じしょに ありません"],
        "content": """
<h2>PJ-28: Lugʻat shakli (<ruby>辞書形<rt>じしょけい</rt></ruby>) — nega lugʻatda ます yoʻq</h2>

<p>Tasavvur qiling: matnda <ruby>飲<rt>の</rt></ruby>みます soʻzini koʻrdingiz
va lugʻatga qaradingiz. Lekin lugʻatda «のみます» degan soʻz <b>yoʻq</b>.
U yerda <ruby>飲<rt>の</rt></ruby>む turibdi.</p>

<p>Bu xato emas. Yapon lugʻati feʼlni doim <b>lugʻat shaklida</b> beradi, va
sizga ham aynan shu shakl kerak — chunki keyingi oʻn besh dars davomida har
bir yangi feʼl shakli undan yasaladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ます nima ekanini — va nega u feʼlning qismi emasligini bilib olasiz</li>
    <li>う qatorining toʻqqizta oxirini tanib olasiz</li>
    <li>ます shaklidan lugʻat shakliga qaytasiz, uchala guruhda</li>
    <li>ます shakliga qarab guruhni <em>doim ham</em> aniqlab boʻlmasligini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki tomonga yuradigan koʻprik</span>
  <span class="pe-chip pe-chip--s">lugʻat shakli</span>
  <span class="pe-op">⇄</span>
  <span class="pe-chip pe-chip--v">ます shakli</span>
</div>

<h3>1. ます — feʼlning qismi emas</h3>

<p>Yigirma dars davomida siz ます ni feʼl bilan birga oʻrgandingiz, shuning
uchun u soʻzning bir qismi boʻlib tuyulishi tabiiy. Aslida esa ます —
<b>alohida qoʻshimcha</b> (<ruby>助動詞<rt>じょどうし</rt></ruby>), va uning
yagona vazifasi <em>muloyimlik</em>.</p>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham xuddi shunday.</b> Lugʻatda «oʻqiyman» yoʻq —
  «<b>oʻqimoq</b>» bor. «-yman» — bu shaxs-son qoʻshimchasi, soʻzning oʻzi
  emas. Yapon lugʻati ham aynan shu mantiq bilan ishlaydi: u feʼlning
  <em>oʻzini</em> beradi, kiyimini emas. Farqi bitta — oʻzbekchada lugʻat
  shakli «-moq» bilan tugaydi, yaponchada esa <b>う qatoridagi tovush</b>
  bilan.</p>
</div>

<h3>2. Toʻqqizta oxir — う qatorining hammasi</h3>

<p>Lugʻat shakli faqat shu toʻqqizta tovushdan biri bilan tugashi mumkin.
Boshqa varianti yoʻq.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oxiri</th><th>Feʼl</th><th>ます shakli</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-end">う</td><td><ruby>買<rt>か</rt></ruby>う</td><td class="pj-res"><ruby>買<rt>か</rt></ruby>います</td><td class="pj-uz">sotib olmoq</td></tr>
  <tr><td class="pj-end">く</td><td><ruby>書<rt>か</rt></ruby>く</td><td class="pj-res"><ruby>書<rt>か</rt></ruby>きます</td><td class="pj-uz">yozmoq</td></tr>
  <tr><td class="pj-end">ぐ</td><td><ruby>泳<rt>およ</rt></ruby>ぐ</td><td class="pj-res"><ruby>泳<rt>およ</rt></ruby>ぎます</td><td class="pj-uz">suzmoq</td></tr>
  <tr><td class="pj-end">す</td><td><ruby>話<rt>はな</rt></ruby>す</td><td class="pj-res"><ruby>話<rt>はな</rt></ruby>します</td><td class="pj-uz">gapirmoq</td></tr>
  <tr><td class="pj-end">つ</td><td><ruby>待<rt>ま</rt></ruby>つ</td><td class="pj-res"><ruby>待<rt>ま</rt></ruby>ちます</td><td class="pj-uz">kutmoq</td></tr>
  <tr><td class="pj-end">ぬ</td><td><ruby>死<rt>し</rt></ruby>ぬ</td><td class="pj-res"><ruby>死<rt>し</rt></ruby>にます</td><td class="pj-uz">oʻlmoq</td></tr>
  <tr><td class="pj-end">ぶ</td><td><ruby>遊<rt>あそ</rt></ruby>ぶ</td><td class="pj-res"><ruby>遊<rt>あそ</rt></ruby>びます</td><td class="pj-uz">oʻynamoq</td></tr>
  <tr><td class="pj-end">む</td><td><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>みます</td><td class="pj-uz">oʻqimoq</td></tr>
  <tr><td class="pj-end">る</td><td><ruby>作<rt>つく</rt></ruby>る</td><td class="pj-res"><ruby>作<rt>つく</rt></ruby>ります</td><td class="pj-uz">yasamoq</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>ぬ bilan tugaydigan feʼl butun tilda bittagina:</b>
  <ruby>死<rt>し</rt></ruby>ぬ. Uni yodlash oson — chunki raqobatchisi yoʻq.</p>
</div>

<h3>3. III guruhdan qaytish</h3>

<p>Odatdagidek eng kichigidan boshlaymiz. Ikkita feʼl, ikkita javob.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>ます shakli</th><th>Lugʻat shakli</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res">します</td><td class="pj-stem">する</td><td class="pj-uz">qilmoq</td></tr>
  <tr><td class="pj-res"><ruby>来<rt>き</rt></ruby>ます</td><td class="pj-stem"><ruby>来<rt>く</rt></ruby>る</td><td class="pj-uz">kelmoq</td></tr>
</table></div>

<h3>4. II guruhdan qaytish — る ni qaytaring</h3>

<p>ます ni olib tashlang, oʻrniga <b>る</b> qoʻying. Xolos.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>ます shakli</th><th>Oʻzak</th><th>Lugʻat shakli</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res"><ruby>食<rt>た</rt></ruby>べます</td><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べ</td>
      <td class="pj-end"><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-uz">yemoq</td></tr>
  <tr><td class="pj-res"><ruby>寝<rt>ね</rt></ruby>ます</td><td class="pj-stem"><ruby>寝<rt>ね</rt></ruby></td>
      <td class="pj-end"><ruby>寝<rt>ね</rt></ruby>る</td><td class="pj-uz">uxlamoq</td></tr>
  <tr><td class="pj-res"><ruby>起<rt>お</rt></ruby>きます</td><td class="pj-stem"><ruby>起<rt>お</rt></ruby>き</td>
      <td class="pj-end"><ruby>起<rt>お</rt></ruby>きる</td><td class="pj-uz">turmoq</td></tr>
</table></div>

<h3>5. I guruhdan qaytish — い qatoridan う qatoriga</h3>

<p>PJ-27 dagi harakatning teskarisi. U yerda う qatori い qatoriga tushgan
edi; bu yerda い qatori <b>う qatoriga koʻtariladi</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>ます shakli</th><th>Oxirgi tovush</th><th>う qatoriga</th><th>Lugʻat shakli</th></tr>
  <tr><td class="pj-res"><ruby>読<rt>よ</rt></ruby>みます</td><td class="pj-uz">み</td><td class="pj-end">む</td>
      <td class="pj-stem"><ruby>読<rt>よ</rt></ruby>む</td></tr>
  <tr><td class="pj-res"><ruby>書<rt>か</rt></ruby>きます</td><td class="pj-uz">き</td><td class="pj-end">く</td>
      <td class="pj-stem"><ruby>書<rt>か</rt></ruby>く</td></tr>
  <tr><td class="pj-res"><ruby>話<rt>はな</rt></ruby>します</td><td class="pj-uz">し</td><td class="pj-end">す</td>
      <td class="pj-stem"><ruby>話<rt>はな</rt></ruby>す</td></tr>
  <tr><td class="pj-res"><ruby>待<rt>ま</rt></ruby>ちます</td><td class="pj-uz">ち</td><td class="pj-end">つ</td>
      <td class="pj-stem"><ruby>待<rt>ま</rt></ruby>つ</td></tr>
  <tr><td class="pj-res"><ruby>帰<rt>かえ</rt></ruby>ります</td><td class="pj-uz">り</td><td class="pj-end">る</td>
      <td class="pj-stem"><ruby>帰<rt>かえ</rt></ruby>る</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>し → す va ち → つ ga eʼtibor bering.</b> Bu yerda ham
  <ruby>五十音図<rt>ごじゅうおんず</rt></ruby> ishlaydi: し さ qatorining
  い pogʻonasi, uning う pogʻonasi — す. ち esa た qatorida, demak つ.
  Yapon tilida «si» va «ti» tovushlari yoʻqligi butun jadvalni shunday
  buradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>友<rt>とも</rt></ruby>だちを<ruby>待<rt>ま</rt></ruby>ちます。「<ruby>待<rt>ま</rt></ruby>つ」は<ruby>辞書形<rt>じしょけい</rt></ruby>です。</p>
  <p class="pe-ex__rom">tomodachi o machimasu. "matsu" wa jishokei desu</p>
  <p class="pe-ex__uz">Doʻstimni kutaman. «Matsu» — lugʻat shakli.</p>
  <p class="pe-ex__why">Lugʻatda <b><ruby>待<rt>ま</rt></ruby>つ</b> deb qidiring, «まちます» deb emas. Aks holda hech narsa topmaysiz.</p>
</div>

<h3>6. Diqqat: ます shakli guruhni <em>doim</em> aytmaydi</h3>

<p>Mana darsning eng muhim ogohlantirishi. Ikkita feʼlga qarang — ikkalasining
ham oʻzagi <b>き</b> bilan tugaydi:</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h"><ruby>起<rt>お</rt></ruby>きます</p>
    <p class="pj-big">II</p>
    <p>Lugʻat shakli: <b><ruby>起<rt>お</rt></ruby>きる</b><br>
    る qoʻshiladi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h"><ruby>聞<rt>き</rt></ruby>きます</p>
    <p class="pj-big">I</p>
    <p>Lugʻat shakli: <b><ruby>聞<rt>き</rt></ruby>く</b><br>
    き koʻtarilib く boʻladi.</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>Ikkala oʻzak ham «き» bilan tugaydi, lekin javob boshqacha.</b>
  Yaʼni ます shakliga <em>qarab turib</em> guruhni aniqlab boʻlmaydi. Xulosa
  esa amaliy va qatʼiy: <b>yangi feʼlni doim lugʻat shaklida yodlang</b> —
  <ruby>聞<rt>き</rt></ruby>く, <ruby>起<rt>お</rt></ruby>きる — shunda guruh
  ham, keyingi barcha shakllar ham oʻz-oʻzidan kelib chiqadi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Bitta ishonchli belgi bor:</b> agar oʻzak <b>え qatori</b> bilan
  tugasa (<ruby>食<rt>た</rt></ruby>べ, <ruby>寝<rt>ね</rt></ruby>,
  <ruby>教<rt>おし</rt></ruby>え), feʼl <b>albatta II guruhda</b> — chunki
  I guruh oʻzagi hech qachon え qatori bilan tugamaydi. Shubha faqat
  い qatorida qoladi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Lugʻatdan «のみます» ni qidirish</p>
  <p class="pe-fix__good">✓ <b><ruby>飲<rt>の</rt></ruby>む</b> ni qidiring — lugʻat feʼlni faqat lugʻat shaklida beradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>話<rt>はな</rt></ruby>します → «はなしる»</p>
  <p class="pe-fix__good">✓ <b><ruby>話<rt>はな</rt></ruby>す</b> — し ning う pogʻonasi <b>す</b>, «しる» emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>聞<rt>き</rt></ruby>きます → «ききる»</p>
  <p class="pe-fix__good">✓ <b><ruby>聞<rt>き</rt></ruby>く</b> — bu I guruh feʼli. き bilan tugagan oʻzak II guruhni <b>kafolatlamaydi</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>読<rt>よ</rt></ruby>みます ning lugʻat shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>読<rt>よ</rt></ruby>む</b> — み koʻtarilib む boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>食<rt>た</rt></ruby>べます ning lugʻat shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べる</b> — II guruh: ます oʻrniga る.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Nega lugʻatda ます yoʻq?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki ます — feʼlning qismi emas, <b>muloyimlik qoʻshimchasi</b>. Lugʻat feʼlning oʻzini beradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>話<rt>はな</rt></ruby>します ning lugʻat shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>話<rt>はな</rt></ruby>す</b>. し — さ qatorining い pogʻonasi, uning う pogʻonasi <b>す</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Oʻzagi <b>え</b> qatori bilan tugagan feʼl qaysi guruhda?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Albatta II guruhda.</b> I guruh oʻzagi hech qachon え qatori bilan tugamaydi — bu yagona 100% ishonchli belgi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>辞書形<rt>じしょけい</rt></ruby></b> — lugʻat shakli</li>
  <li><b><ruby>助動詞<rt>じょどうし</rt></ruby></b> — yordamchi qoʻshimcha (ます)</li>
  <li><b><ruby>聞<rt>き</rt></ruby>く</b> — eshitmoq; soʻramoq (I guruh!)</li>
  <li><b><ruby>泳<rt>およ</rt></ruby>ぐ</b> — suzmoq</li>
  <li><b><ruby>遊<rt>あそ</rt></ruby>ぶ</b> — oʻynamoq</li>
  <li><b><ruby>死<rt>し</rt></ruby>ぬ</b> — oʻlmoq (yagona ぬ feʼli)</li>
  <li><b><ruby>作<rt>つく</rt></ruby>る</b> — yasamoq</li>
  <li><b><ruby>乗<rt>の</rt></ruby>る</b> — minmoq, chiqmoq</li>
  <li><b><ruby>教<rt>おし</rt></ruby>える</b> — oʻrgatmoq (II guruh)</li>
  <li><b><ruby>友<rt>とも</rt></ruby>だち</b> — doʻst</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>ます — <b>qoʻshimcha</b>, feʼlning qismi emas. Lugʻat feʼlning oʻzini beradi.</li>
    <li>Qaytish yoʻli: III yodlanadi · II <b>+る</b> · I <b>い qatori → う qatori</b>.</li>
    <li>ます shakli guruhni doim aytmaydi — feʼlni <b>lugʻat shaklida</b> yodlang.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-29: て-shakli 1 — 一段 va 不規則 feʼllar",
        "category": "japanese",
        "order": 29,
        "summary": (
            "Yapon tilidagi eng koʻp ish bajaradigan shakl. Bu darsda uni "
            "II va III guruhdan yasaysiz va gaplarni oʻzbekcha «-ib» kabi "
            "bir-biriga ulaysiz."
        ),
        "stories": ["おきて、たべて、がっこうへ"],
        "content": """
<h2>PJ-29: て-shakli 1 — <ruby>一段<rt>いちだん</rt></ruby> va <ruby>不規則<rt>ふきそく</rt></ruby> feʼllar</h2>

<p>Agar yapon grammatikasida bitta eng foydali shaklni tanlash kerak boʻlsa,
u <b>て-shakli</b> (<ruby>て形<rt>てけい</rt></ruby>) boʻlardi. Undan oʻn
beshdan ortiq qolip yasaladi: iltimos, ruxsat, taqiq, davom etayotgan ish,
tajriba, ish tartibi.</p>

<p>Shuning uchun uni ikki darsga boʻlamiz. Bugun <b>oson yarmi</b> — II va
III guruh; keyingi darsda I guruhning beshta qoidasi keladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>II guruhdan て yasaysiz: る → て</li>
    <li>III guruhning ikkita shaklini yodlab olasiz</li>
    <li>Ikki ishni bitta gapda ulaysiz</li>
    <li>て-shakli zamon koʻrsatmasligini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">II guruh — る oʻrniga て</span>
  <span class="pe-chip pe-chip--s"><ruby>食<rt>た</rt></ruby>べる</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v"><ruby>食<rt>た</rt></ruby>べて</span>
</div>

<h3>1. て-shakli nima</h3>

<p>Avval bitta narsani aniq ayting: <b>て-shakli oʻzi maʼno bermaydi</b>.
U zamon ham koʻrsatmaydi, gapni ham tugatmaydi. U — <em>ulagich</em>:
oʻzidan keyin nima kelishini kutib turadigan shakl.</p>

<div class="pe-call pe-tip">
  <p><b>Nimaga ochiladi.</b> 〜てください («iltimos, qiling»),
  〜ています («qilyapti»), 〜てもいいです («qilsa boʻladi»),
  〜てはいけません («qilib boʻlmaydi»), 〜てから («qilgandan keyin»).
  Hammasi keyingi darslarda — lekin hammasi <b>shu bitta shakldan</b>
  boshlanadi. Shuning uchun uni puxta yasay bilish kerak.</p>
</div>

<h3>2. II guruh — る ni て ga almashtiring</h3>

<p>Bu guruh yana eng oson chiqdi. Lugʻat shaklidagi <b>る</b> ni olib
tashlab, <b>て</b> qoʻyasiz.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat shakli</th><th>Oʻzak</th><th>て-shakli</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べ</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べて</td><td class="pj-uz">yemoq</td></tr>
  <tr><td><ruby>見<rt>み</rt></ruby>る</td><td class="pj-stem"><ruby>見<rt>み</rt></ruby></td>
      <td class="pj-res"><ruby>見<rt>み</rt></ruby>て</td><td class="pj-uz">koʻrmoq</td></tr>
  <tr><td><ruby>起<rt>お</rt></ruby>きる</td><td class="pj-stem"><ruby>起<rt>お</rt></ruby>き</td>
      <td class="pj-res"><ruby>起<rt>お</rt></ruby>きて</td><td class="pj-uz">turmoq</td></tr>
  <tr><td><ruby>寝<rt>ね</rt></ruby>る</td><td class="pj-stem"><ruby>寝<rt>ね</rt></ruby></td>
      <td class="pj-res"><ruby>寝<rt>ね</rt></ruby>て</td><td class="pj-uz">uxlamoq</td></tr>
  <tr><td><ruby>教<rt>おし</rt></ruby>える</td><td class="pj-stem"><ruby>教<rt>おし</rt></ruby>え</td>
      <td class="pj-res"><ruby>教<rt>おし</rt></ruby>えて</td><td class="pj-uz">oʻrgatmoq</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Diqqat qiling:</b> ます shakli bilan て-shakli <b>bir xil oʻzakdan</b>
  yasaladi. <ruby>食<rt>た</rt></ruby>べ + ます,
  <ruby>食<rt>た</rt></ruby>べ + て. Yaʼni II guruhda ikkinchi qoida yodlash
  kerak emas — oʻzak oʻsha, faqat oxiri almashadi.</p>
</div>

<h3>3. III guruh — ikkitasi, yodlanadi</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat shakli</th><th>て-shakli</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">する</td><td class="pj-res">して</td><td class="pj-uz">qilmoq</td></tr>
  <tr><td class="pj-stem"><ruby>来<rt>く</rt></ruby>る</td><td class="pj-res"><ruby>来<rt>き</rt></ruby>て</td><td class="pj-uz">kelmoq</td></tr>
</table></div>

<p>する ning barcha qoʻshma feʼllari ham shu yoʻldan boradi:
<ruby>勉強<rt>べんきょう</rt></ruby>する → <b><ruby>勉強<rt>べんきょう</rt></ruby>して</b>,
<ruby>電話<rt>でんわ</rt></ruby>する → <b><ruby>電話<rt>でんわ</rt></ruby>して</b>.</p>

<div class="pe-call pe-warn">
  <p><ruby>来<rt>く</rt></ruby>る yana oʻqilishini oʻzgartiradi:
  <ruby>来<rt>き</rt></ruby>て. Kanji uch xil oʻqiladi —
  <ruby>来<rt>く</rt></ruby>る, <ruby>来<rt>き</rt></ruby>ます,
  <ruby>来<rt>き</rt></ruby>て — va faqat furigana buni koʻrsatadi.</p>
</div>

<h3>4. Ulagich sifatida: «…-ib, …»</h3>

<p>Endi eng yoqimli qismi. Ikki ishni bitta gapga ulash uchun birinchi feʼlni
<b>て-shaklida</b> qoʻyasiz, ikkinchisini esa odatdagidek tugatasiz.</p>

<div class="pj-joshi">
  <span class="pj-joshi__v"><ruby>起<rt>お</rt></ruby>きて</span>
  <span class="pj-joshi__p">、<small>VA KEYIN</small></span>
  <span class="pj-joshi__n"><ruby>朝<rt>あさ</rt></ruby>ごはん</span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__v"><ruby>食<rt>た</rt></ruby>べます</span>
  <span class="pj-joshi__uz">Turib, nonushta qilaman.</span>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu — oʻzbekchaning «-(i)b» qoʻshimchasining oʻzi.</b> «Tur<b>ib</b>,
  nonushta qilaman», «Ko'r<b>ib</b>, tushunaman» — oʻzbekchada birinchi feʼl
  tugallanmagan holda qoladi va zamonni <em>oxirgi</em> feʼl tashiydi.
  Yapon tilida ham aynan shunday: <ruby>起<rt>お</rt></ruby>きて —
  tugallanmagan, <ruby>食<rt>た</rt></ruby>べます — tugatadi. Ikki til
  bu joyda deyarli bir xil ishlaydi, shuning uchun bu qolipni oʻzbek
  oʻquvchi juda tez oʻzlashtiradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>朝<rt>あさ</rt></ruby><ruby>六時<rt>ろくじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きて、<ruby>顔<rt>かお</rt></ruby>を<ruby>見<rt>み</rt></ruby>て、<ruby>朝<rt>あさ</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べます。</p>
  <p class="pe-ex__rom">asa rokuji ni okite, kao o mite, asagohan o tabemasu</p>
  <p class="pe-ex__uz">Ertalab soat oltida turib, yuzimga qarab, nonushta qilaman.</p>
  <p class="pe-ex__why">Uchta ish, bitta gap. Faqat <b>oxirgi</b> feʼl ます oladi — qolganlari て da qoladi.</p>
</div>

<h3>5. Tartib — vaqt tartibi</h3>

<p>て bilan ulangan ishlar <b>sodir boʻlgan tartibda</b> yoziladi. Oʻrinlarini
almashtirsangiz, maʼno ham oʻzgaradi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">TOʻGʻRI TARTIB</p>
    <p><ruby>食<rt>た</rt></ruby>べて、<ruby>寝<rt>ね</rt></ruby>ます。</p>
    <p>Yeb, uxlayman.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">BOSHQA MAʼNO</p>
    <p><ruby>寝<rt>ね</rt></ruby>て、<ruby>食<rt>た</rt></ruby>べます。</p>
    <p>Uxlab, yeyman.</p></div>
</div>

<h3>6. て zamon koʻrsatmaydi</h3>

<p>Bu koʻp adashtiradi. «Kecha turib, nonushta qildim» deyish uchun
<ruby>起<rt>お</rt></ruby>きて ni oʻtgan zamonga <b>oʻtkazmaysiz</b> —
u oʻzgarmaydi. Zamonni faqat oxirgi feʼl tashiydi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>昨日<rt>きのう</rt></ruby><ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>て、<ruby>寝<rt>ね</rt></ruby>ました。</p>
  <p class="pe-ex__rom">kinō ēga o mite, nemashita</p>
  <p class="pe-ex__uz">Kecha kino koʻrib, uxladim.</p>
  <p class="pe-ex__why"><ruby>見<rt>み</rt></ruby>て — oʻzgarmadi, garchi ish kecha boʻlgan boʻlsa ham. Oʻtgan zamonni <b><ruby>寝<rt>ね</rt></ruby>ました</b> tashidi.</p>
</div>

<h3>7. と emas — と otlarni ulaydi</h3>

<p>PJ-19 da <b>と</b> qoʻshimchasini oʻrgangansiz: «Rano <b>va</b> Inom».
Oʻzbekchada «va» ikkalasiga ham yaraydi, shuning uchun oʻquvchi と ni feʼllar
orasiga ham qoʻyib yuboradi. Yaponchada esa ish boʻlinadi:</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">OT + OT — と</p>
    <p class="pj-big">と</p>
    <p><ruby>本<rt>ほん</rt></ruby><b>と</b><ruby>鉛筆<rt>えんぴつ</rt></ruby><br>
    kitob va qalam</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">FEʼL + FEʼL — て</p>
    <p class="pj-big">て</p>
    <p><ruby>見<rt>み</rt></ruby><b>て</b>、<ruby>寝<rt>ね</rt></ruby>ます<br>
    koʻrib, uxlayman</p></div>
</div>

<p>Yaʼni yaponchada «va» degan yagona soʻz yoʻq: otlar uchun bitta vosita,
feʼllar uchun butunlay boshqasi. Buni bir marta ajratib olsangiz, keyingi
darslarda hech qachon adashmaysiz.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>食<rt>た</rt></ruby>べるて</p>
  <p class="pe-fix__good">✓ <ruby>食<rt>た</rt></ruby>べ<b>て</b> — る <b>almashadi</b>, て unga qoʻshilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>昨日<rt>きのう</rt></ruby><ruby>見<rt>み</rt></ruby>まして、<ruby>寝<rt>ね</rt></ruby>ました</p>
  <p class="pe-fix__good">✓ <ruby>昨日<rt>きのう</rt></ruby><ruby>見<rt>み</rt></ruby><b>て</b>、<ruby>寝<rt>ね</rt></ruby>ました — て-shakli ます dan emas, <b>lugʻat shaklidan</b> yasaladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>来<rt>く</rt></ruby>て</p>
  <p class="pe-fix__good">✓ <ruby>来<rt>き</rt></ruby>て — oʻqilishi <b>き</b> ga oʻtadi, xuddi <ruby>来<rt>き</rt></ruby>ます kabi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>見<rt>み</rt></ruby>る ning て-shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>見<rt>み</rt></ruby>て</b> — II guruh: る oʻrniga て.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. する va <ruby>来<rt>く</rt></ruby>る ning て-shakllari?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>して</b> va <b><ruby>来<rt>き</rt></ruby>て</b>. Yodlanadi — III guruhda boshqa feʼl yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Turib, maktabga boraman» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>起<rt>お</rt></ruby>きて、<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きます。</b></p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. て-shakli qaysi zamonni koʻrsatadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Hech qaysi.</b> Zamonni gapning <b>oxirgi</b> feʼli tashiydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>勉強<rt>べんきょう</rt></ruby>する ning て-shakli?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>勉強<rt>べんきょう</rt></ruby>して</b> — する ning har bir qoʻshma feʼli して boʻladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>て形<rt>てけい</rt></ruby></b> — て-shakli</li>
  <li><b><ruby>食<rt>た</rt></ruby>べて</b> — yeb</li>
  <li><b><ruby>見<rt>み</rt></ruby>て</b> — koʻrib</li>
  <li><b><ruby>起<rt>お</rt></ruby>きて</b> — turib</li>
  <li><b><ruby>寝<rt>ね</rt></ruby>て</b> — uxlab</li>
  <li><b>して</b> — qilib</li>
  <li><b><ruby>来<rt>き</rt></ruby>て</b> — kelib</li>
  <li><b><ruby>教<rt>おし</rt></ruby>えて</b> — oʻrgatib</li>
  <li><b><ruby>顔<rt>かお</rt></ruby></b> — yuz</li>
  <li><b><ruby>朝<rt>あさ</rt></ruby>ごはん</b> — nonushta</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>II guruh: <b>る → て</b>. Oʻzak ます dagi bilan bir xil.</li>
    <li>III guruh: <b>して</b> va <b><ruby>来<rt>き</rt></ruby>て</b> — yodlanadi.</li>
    <li>て zamon <b>koʻrsatmaydi</b>; uni gapning oxirgi feʼli tashiydi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-30: て-shakli 2 — 五段 feʼllar va ularning beshta qoidasi",
        "category": "japanese",
        "order": 30,
        "summary": (
            "I guruhning て-shakli oxirgi tovushga qarab beshga boʻlinadi. "
            "Shu beshtasini bilsangiz, yapon tilidagi har qanday feʼldan "
            "て yasay olasiz."
        ),
        "stories": ["うみで およいで"],
        "content": """
<h2>PJ-30: て-shakli 2 — <ruby>五段<rt>ごだん</rt></ruby> feʼllar va ularning beshta qoidasi</h2>

<p>Oʻtgan darsda て-shaklining oson yarmini oldingiz: II guruhda る → て,
III guruhda ikkita yodlanadigan shakl. Bugun qiyin yarmi keladi — lekin
qiyinligi faqat <em>hajmda</em>, mantiqda emas.</p>

<p>I guruhda te-shakli feʼlning <b>oxirgi tovushiga</b> qarab yasaladi, va
toʻqqizta oxir beshta guruhga yigʻiladi. Shu beshtasini bilsangiz, yapon
tilidagi <b>istalgan</b> feʼldan て yasay olasiz — chunki uchala guruh ham
tugadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Beshta qoidani oxirgi tovushga bogʻlab yodlaysiz</li>
    <li>って va んで orasidagi farqni eshitasiz</li>
    <li>いて / いで juftligini ajratasiz</li>
    <li>Butun kursdagi yagona istisnoni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Beshta qoida, oxirgi tovushga qarab</span>
  <span class="pe-chip pe-chip--s">う・つ・る → って</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">む・ぶ・ぬ → んで</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">く → いて</span>
</div>

<h3>1. Butun jadval — bir qarashda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oxiri</th><th>Qoida</th><th>Misol</th><th>て-shakli</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-end">う・つ・る</td><td class="pj-uz">→ って</td>
      <td><ruby>買<rt>か</rt></ruby>う</td><td class="pj-res"><ruby>買<rt>か</rt></ruby>って</td><td class="pj-uz">sotib olib</td></tr>
  <tr><td class="pj-end">む・ぶ・ぬ</td><td class="pj-uz">→ んで</td>
      <td><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>んで</td><td class="pj-uz">oʻqib</td></tr>
  <tr><td class="pj-end">く</td><td class="pj-uz">→ いて</td>
      <td><ruby>書<rt>か</rt></ruby>く</td><td class="pj-res"><ruby>書<rt>か</rt></ruby>いて</td><td class="pj-uz">yozib</td></tr>
  <tr><td class="pj-end">ぐ</td><td class="pj-uz">→ いで</td>
      <td><ruby>泳<rt>およ</rt></ruby>ぐ</td><td class="pj-res"><ruby>泳<rt>およ</rt></ruby>いで</td><td class="pj-uz">suzib</td></tr>
  <tr><td class="pj-end">す</td><td class="pj-uz">→ して</td>
      <td><ruby>話<rt>はな</rt></ruby>す</td><td class="pj-res"><ruby>話<rt>はな</rt></ruby>して</td><td class="pj-uz">gapirib</td></tr>
</table></div>

<h3>2. Birinchi uchlik: う・つ・る → って</h3>

<p>Uchta har xil oxir bitta natijaga keladi. Bu yaxshi xabar: uchtasini
alohida yodlash shart emas.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>て-shakli</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>買<rt>か</rt></ruby>う</td><td class="pj-res"><ruby>買<rt>か</rt></ruby>って</td><td class="pj-uz">sotib olib</td></tr>
  <tr><td><ruby>待<rt>ま</rt></ruby>つ</td><td class="pj-res"><ruby>待<rt>ま</rt></ruby>って</td><td class="pj-uz">kutib</td></tr>
  <tr><td><ruby>帰<rt>かえ</rt></ruby>る</td><td class="pj-res"><ruby>帰<rt>かえ</rt></ruby>って</td><td class="pj-uz">qaytib</td></tr>
  <tr><td><ruby>作<rt>つく</rt></ruby>る</td><td class="pj-res"><ruby>作<rt>つく</rt></ruby>って</td><td class="pj-uz">yasab</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>っ nima qilyapti?</b> Bu — PJ-6 da oʻrgangan <b>sokuon</b>: keyingi
  undoshni ikkilantiradigan kichkina つ. <ruby>待<rt>ま</rt></ruby>って
  «matte» deb oʻqiladi, «mate» emas — toʻxtash bir zumga uzayadi. Uni
  eshitmasangiz, boshqa soʻz chiqadi.</p>
</div>

<h3>3. Ikkinchi uchlik: む・ぶ・ぬ → んで</h3>

<p>Bu uchtasi <b>jarangli</b> tovushlar bilan tugaydi, shuning uchun ulanish
ham jarangli chiqadi: て emas, <b>で</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>て-shakli</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>んで</td><td class="pj-uz">oʻqib</td></tr>
  <tr><td><ruby>飲<rt>の</rt></ruby>む</td><td class="pj-res"><ruby>飲<rt>の</rt></ruby>んで</td><td class="pj-uz">ichib</td></tr>
  <tr><td><ruby>遊<rt>あそ</rt></ruby>ぶ</td><td class="pj-res"><ruby>遊<rt>あそ</rt></ruby>んで</td><td class="pj-uz">oʻynab</td></tr>
  <tr><td><ruby>死<rt>し</rt></ruby>ぬ</td><td class="pj-res"><ruby>死<rt>し</rt></ruby>んで</td><td class="pj-uz">oʻlib</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu — talaffuzning qonuni, grammatikaning injiqligi emas.</b>
  «yomte» deyishga urinib koʻring — til uni qiynaladi va oʻz-oʻzidan
  «yonde» ga oʻzgaradi. Oʻzbekchada ham xuddi shunday jarayonlar bor:
  «ket + di» → <em>ketti</em>, «tut + di» → <em>tutti</em>. Yozuvda bir xil
  turadi, ogʻizda esa tovush qoʻshnisiga moslashadi. Yapon tili shu
  oʻzgarishni <b>yozuvda ham</b> koʻrsatadi.</p>
</div>

<h3>4. く → いて va ぐ → いで</h3>

<p>Bu ikkitasi bir juftlik: jarangsiz <b>く</b> jarangsiz て oladi, jarangli
<b>ぐ</b> esa jarangli で oladi. Qolgan qismi bir xil.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>手紙<rt>てがみ</rt></ruby>を<ruby>書<rt>か</rt></ruby>いて、<ruby>友<rt>とも</rt></ruby>だちに<ruby>話<rt>はな</rt></ruby>して、<ruby>海<rt>うみ</rt></ruby>で<ruby>泳<rt>およ</rt></ruby>いで、<ruby>帰<rt>かえ</rt></ruby>りました。</p>
  <p class="pe-ex__rom">tegami o kaite, tomodachi ni hanashite, umi de oyoide, kaerimashita</p>
  <p class="pe-ex__uz">Xat yozib, doʻstim bilan gaplashib, dengizda suzib, qaytdim.</p>
  <p class="pe-ex__why">Bitta gapda toʻrtta qoida: <b>く→いて</b>, <b>す→して</b>, <b>ぐ→いで</b>, va oxirida zamonni tashigan <ruby>帰<rt>かえ</rt></ruby>りました.</p>
</div>

<h3>5. す → して — tanish shakl</h3>

<p>Bu qoida sizga allaqachon tanish: III guruhning する ham <b>して</b>
boʻlgan edi. Bir xil chiqishining sababi ham bir xil — <b>す</b> tovushi.</p>

<p>Bu yerda hech qanday qisqarish yoʻq: す shunchaki oʻzining い pogʻonasiga
tushadi va て qoʻshiladi — xuddi ます shaklidagi kabi
(<ruby>話<rt>はな</rt></ruby>します · <ruby>話<rt>はな</rt></ruby>して).
Shuning uchun す bilan tugagan feʼllar eng oson eslab qolinadi:
<ruby>返<rt>かえ</rt></ruby>す → <ruby>返<rt>かえ</rt></ruby>して
(«qaytarib»), <ruby>貸<rt>か</rt></ruby>す → <ruby>貸<rt>か</rt></ruby>して
(«qarzga berib»).</p>

<h3>6. Yagona istisno: <ruby>行<rt>い</rt></ruby>く</h3>

<p>Butun kursda bitta feʼl qoidadan chiqadi, va u — eng koʻp ishlatiladigan
feʼllardan biri.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">QOIDA BOʻYICHA</p>
    <p class="pj-big">✗</p>
    <p><ruby>行<rt>い</rt></ruby>く → «いいて»<br>
    く → いて qoidasi shuni beradi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">HAQIQATDA</p>
    <p class="pj-big">✓</p>
    <p><ruby>行<rt>い</rt></ruby>く → <b><ruby>行<rt>い</rt></ruby>って</b><br>
    Birinchi uchlik kabi.</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>Faqat shu bitta feʼl.</b> Boshqa hech qaysi く feʼli bunday
  qilmaydi: <ruby>書<rt>か</rt></ruby>く → <ruby>書<rt>か</rt></ruby>いて,
  <ruby>聞<rt>き</rt></ruby>く → <ruby>聞<rt>き</rt></ruby>いて. Istisno
  <ruby>行<rt>い</rt></ruby>く da tugaydi — va u shu qadar koʻp
  ishlatiladiki, bir haftada oʻz-oʻzidan yodda qoladi.</p>
</div>

<h3>7. Endi hammasi joyida</h3>

<p>Uchala guruh ham tugadi. Notanish feʼl uchraganda tartib oʻsha-oʻsha:
avval <b>guruhni</b> aniqlaysiz (PJ-27), keyin shu guruhning て qoidasini
qoʻllaysiz.</p>

<div class="pj-group">
  <div class="pj-group__c">
    <p class="pj-group__h">I — <ruby>五段<rt>ごだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>読<rt>よ</rt></ruby>む → <ruby>読<rt>よ</rt></ruby>んで</p>
    <p>Beshta qoida, oxirgi tovushga qarab.</p>
  </div>
  <div class="pj-group__c pj-group__c--2">
    <p class="pj-group__h">II — <ruby>一段<rt>いちだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>食<rt>た</rt></ruby>べる → <ruby>食<rt>た</rt></ruby>べて</p>
    <p>る oʻrniga て. Bitta qoida.</p>
  </div>
  <div class="pj-group__c pj-group__c--3">
    <p class="pj-group__h">III — <ruby>不規則<rt>ふきそく</rt></ruby></p>
    <p class="pj-group__ex">して · <ruby>来<rt>き</rt></ruby>て</p>
    <p>Ikkitasi yodlanadi.</p>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>いて</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby><b>って</b> — kursdagi yagona istisno. Qoida bu yerda ishlamaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>んて</p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby>ん<b>で</b> — む・ぶ・ぬ dan keyin ulanish <b>jarangli</b> boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>待<rt>ま</rt></ruby>て (kichik っ siz)</p>
  <p class="pe-fix__good">✓ <ruby>待<rt>ま</rt></ruby><b>って</b> — sokuon boʻlmasa boshqa soʻz chiqadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>飲<rt>の</rt></ruby>む ning て-shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>飲<rt>の</rt></ruby>んで</b> — む・ぶ・ぬ → んで.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>買<rt>か</rt></ruby>う ning て-shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>買<rt>か</rt></ruby>って</b> — う・つ・る → って.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>行<rt>い</rt></ruby>く ning て-shakli — «いいて» mi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq: <ruby>行<rt>い</rt></ruby>って.</b> Butun kursdagi yagona istisno.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>泳<rt>およ</rt></ruby>ぐ va <ruby>書<rt>か</rt></ruby>く ning て-shakllari nimasi bilan farq qiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>泳<rt>およ</rt></ruby>いで</b> va <b><ruby>書<rt>か</rt></ruby>いて</b> — ぐ jarangli, shuning uchun で; く jarangsiz, shuning uchun て.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Kitob oʻqib, uxladim» ni yaponchada ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んで、<ruby>寝<rt>ね</rt></ruby>ました。</b> Zamonni oxirgi feʼl tashiydi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>買<rt>か</rt></ruby>って</b> — sotib olib</li>
  <li><b><ruby>待<rt>ま</rt></ruby>って</b> — kutib</li>
  <li><b><ruby>帰<rt>かえ</rt></ruby>って</b> — qaytib</li>
  <li><b><ruby>読<rt>よ</rt></ruby>んで</b> — oʻqib</li>
  <li><b><ruby>飲<rt>の</rt></ruby>んで</b> — ichib</li>
  <li><b><ruby>遊<rt>あそ</rt></ruby>んで</b> — oʻynab</li>
  <li><b><ruby>書<rt>か</rt></ruby>いて</b> — yozib</li>
  <li><b><ruby>泳<rt>およ</rt></ruby>いで</b> — suzib</li>
  <li><b><ruby>行<rt>い</rt></ruby>って</b> — borib (istisno!)</li>
  <li><b><ruby>海<rt>うみ</rt></ruby></b> — dengiz</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>う・つ・る → って</b> · <b>む・ぶ・ぬ → んで</b> · <b>く → いて</b> · <b>ぐ → いで</b> · <b>す → して</b>.</li>
    <li>Jaranglilikka qarang: ぐ va む・ぶ・ぬ dan keyin <b>で</b>, qolganidan keyin <b>て</b>.</li>
    <li><ruby>行<rt>い</rt></ruby>く → <b><ruby>行<rt>い</rt></ruby>って</b> — yagona istisno.</li>
  </ul>
</div>
""",
    },
]
