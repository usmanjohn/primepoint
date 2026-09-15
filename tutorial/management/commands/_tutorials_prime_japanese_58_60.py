# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-58, PJ-59, PJ-60 (Blok D oxiri va Blok E ga oʻtish).

Batchning ipi — て-shaklining ustiga qoʻyiladigan YORDAMCHI FEʼLLAR:
    PJ-58  〜てしまう   — tugatib qoʻymoq / qilib qoʻymoq (afsus)
    PJ-59  〜ておく     — oldindan qilib qoʻymoq
           〜てみる     — qilib koʻrmoq
Uchalasi ham oʻzbekcha «-ib qoʻymoq» va «-ib koʻrmoq» ning aynan
nusxasi, shuning uchun bu ikki dars oʻzbek oʻquvchisiga eng oson
tushadigan darslardan.

PJ-60 esa boshqa narsa: u yerda oʻzbek tili YORDAM BERMAYDI. «Bermoq»
oʻzbekchada bitta feʼl, yaponchada esa uchta — va tanlov <b>kimga</b>
degan savolga qarab qilinadi. Dars shu farqni ochiq tan olishdan
boshlanadi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_58_60.py --author=prime
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
        "title": "PJ-58: 〜てしまいます — tugatish va afsus",
        "category": "japanese",
        "order": 58,
        "summary": (
            "Bitta qolip, ikki maʼno: «butunlay tugatdim» va «qilib "
            "qoʻydim». Oʻzbekcha «-ib qoʻymoq» ham aynan shu ikki ishni "
            "qiladi."
        ),
        "stories": ["けして しまった"],
        "content": """
<h2>PJ-58: 〜てしまいます — tugatish va afsus</h2>

<p>Ikkita oʻzbekcha gapni oʻqing:</p>

<p>Kitobni bir kunda oʻqib <b>boʻldim</b>.<br>
Telefonimni sindirib <b>qoʻydim</b>.</p>

<p>Birinchisida ish <em>toʻliq tugadi</em>. Ikkinchisida ish
<em>xohlamagan holda</em> sodir boʻldi — va gapda afsus bor.
Yapon tilida ikkalasi ham bitta qolip bilan aytiladi:
<b>〜てしまう</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>〜てしまう ni yasaysiz</li>
    <li>Ikki maʼnoni kontekstdan ajratasiz</li>
    <li>Ogʻzaki nutqdagi 〜ちゃう va 〜じゃう ni taniysiz</li>
    <li>Nega yaponlar afsusni feʼl bilan koʻrsatishini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tugatish / afsus</span>
  <span class="pe-chip pe-chip--s">て-shakli</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">しまう</span>
</div>

<h3>1. Yasalishi</h3>

<p>Yana oʻsha て-shakli. PJ-55 da unga <b>も</b> qoʻshgan edingiz,
bugun esa butun bir feʼl qoʻshiladi: <b>しまう</b> (I guruh).</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>て-shakli</th><th>+ しまう</th><th>Muloyim shakl</th></tr>
  <tr><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-end"><ruby>食<rt>た</rt></ruby>べて</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べてしまう</td><td class="pj-uz"><ruby>食<rt>た</rt></ruby>べてしまいます</td></tr>
  <tr><td class="pj-stem"><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-end"><ruby>読<rt>よ</rt></ruby>んで</td>
      <td class="pj-res"><ruby>読<rt>よ</rt></ruby>んでしまう</td><td class="pj-uz"><ruby>読<rt>よ</rt></ruby>んでしまいます</td></tr>
  <tr><td class="pj-stem"><ruby>忘<rt>わす</rt></ruby>れる</td><td class="pj-end"><ruby>忘<rt>わす</rt></ruby>れて</td>
      <td class="pj-res"><ruby>忘<rt>わす</rt></ruby>れてしまう</td><td class="pj-uz"><ruby>忘<rt>わす</rt></ruby>れてしまいました</td></tr>
  <tr><td class="pj-stem">する</td><td class="pj-end">して</td>
      <td class="pj-res">してしまう</td><td class="pj-uz">してしまいました</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bu qolip koʻpincha oʻtgan zamonda chiqadi.</b> Sababi
  oddiy: tugagan ish ham, afsus ham — ikkalasi ham allaqachon
  boʻlgan narsa. Shuning uchun matnlarda siz eng koʻp
  <b>〜てしまいました</b> va oddiy shaklda
  <b>〜てしまった</b> ni koʻrasiz.</p>
</div>

<p>Diqqat qiling: <b>しまう</b> yolgʻiz turganda «yigʻishtirib
qoʻymoq» degani — kiyimni javonga solish, oʻyinchoqni quticha
ichiga qaytarish. Shundan ikkala maʼno ham oʻsib chiqqan:
ishni <em>yigʻishtirib boʻlsangiz</em> — tugatish; bir narsa
oʻzi <em>yigʻishtirilib ketsa</em>, siz xohlamagan holda —
afsus. Qolipni shu tasvir bilan eslab qolish uni
yodlashdan ancha oson.</p>

<h3>2. Birinchi maʼno: butunlay tugatish</h3>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>宿題<rt>しゅくだい</rt></ruby>を<ruby>全部<rt>ぜんぶ</rt></ruby>してしまいました。</p>
  <p class="pe-ex__uz">Uy vazifasini butunlay qilib boʻldim.</p>
  <p class="pe-ex__why">Afsus yoʻq. «<ruby>全部<rt>ぜんぶ</rt></ruby>» soʻzi maʼnoni aniqlab turibdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>本<rt>ほん</rt></ruby>を<ruby>一日<rt>いちにち</rt></ruby>で<ruby>読<rt>よ</rt></ruby>んでしまいました。</p>
  <p class="pe-ex__uz">Bu kitobni bir kunda oʻqib boʻldim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «-ib boʻlmoq» — bu maʼnoning aynan oʻzi.</b>
  «Oʻqib <em>boʻldim</em>», «yeb <em>boʻldim</em>», «yozib
  <em>boʻldim</em>» — oʻzbekchada ham asosiy feʼl <b>-ib</b>
  shaklida turadi va ustiga ikkinchi feʼl qoʻyiladi. Yaponchada
  ham xuddi shunday: <b>て</b> + <b>しまう</b>. Ikkala tilda ham
  bu qurilma «ish tugadi» emas, <em>«ishdan hech nima
  qolmadi»</em> degani.</p>
</div>

<p>Bu maʼno bir qarashda ortiqchadek koʻrinadi: «oʻqidim»
deyish ham yetarli-ku? Farq shundaki, oddiy
<ruby>読<rt>よ</rt></ruby>みました gapi ishning
<em>boʻlganini</em> aytadi, xolos. てしまう esa ishning
<b>oxirigacha yetganini</b> aytadi: sahifa qolmadi, ovqat
qolmadi, vazifadan hech nima qolmadi. Shuning uchun bu qolip
koʻpincha もう («allaqachon») va
<ruby>全部<rt>ぜんぶ</rt></ruby> («hammasi») bilan birga
yuradi — ular bir-birini quvvatlaydi.</p>

<h3>3. Ikkinchi maʼno: afsus</h3>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>財布<rt>さいふ</rt></ruby>をなくしてしまいました。</p>
  <p class="pe-ex__uz">Hamyonimni yoʻqotib qoʻydim.</p>
  <p class="pe-ex__why">Gapda hech qanday «afsus» soʻzi yoʻq — afsusni <b>しまう</b> ning oʻzi olib yuribdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>寝坊<rt>ねぼう</rt></ruby>して、<ruby>電車<rt>でんしゃ</rt></ruby>に<ruby>遅<rt>おく</rt></ruby>れてしまいました。</p>
  <p class="pe-ex__uz">Uxlab qolib, poyezdga kechikib qoldim.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Va bu — oʻzbekcha «-ib qoʻymoq».</b> «Unutib
  <em>qoʻydim</em>», «sindirib <em>qoʻydim</em>», «aytib
  <em>qoʻydim</em>» — bu gaplarda ham afsus alohida soʻz bilan
  emas, <b>ikkinchi feʼl</b> bilan beriladi. Yaʼni oʻzbek tili
  ham aynan yapon tili kabi ishlaydi: asosiy feʼl nima
  boʻlganini aytadi, yordamchi feʼl esa <em>unga
  munosabatni</em>. Ingliz tilida bunday qurilma umuman yoʻq —
  u yerda «unfortunately» degan alohida soʻz qoʻshiladi.</p>
</div>

<p>Yana bir joyi bor, va u oʻzbek oʻquvchisi uchun tanish:
afsus maʼnosi koʻpincha <em>oʻzingizga</em> emas, <b>oʻz
aybingizga</b> ishora qiladi. «Unutib qoʻydim» degan gapda
ayb sizda; «unutildi» desangiz esa ayb yoʻqoladi. Yaponchada
ham shunday: てしまう gapiruvchini voqeaning ichiga
qaytaradi. Shuning uchun uzr soʻraganda bu qolip juda koʻp
ishlatiladi — u «men qildim va buni yoqtirmayapman» degan
maʼnoni bir vaqtda beradi.</p>

<h3>4. Qaysi maʼno? Kontekst aytadi</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">TUGATISH</p>
    <p>Ish — <b>reja</b> edi.<br>Natija — <b>yaxshi</b>.</p>
    <p><ruby>全部<rt>ぜんぶ</rt></ruby>, <ruby>一日<rt>いちにち</rt></ruby>で, もう kabi soʻzlar bilan keladi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">AFSUS</p>
    <p>Ish — <b>xohlanmagan</b>.<br>Natija — <b>yomon</b>.</p>
    <p>なくす, <ruby>忘<rt>わす</rt></ruby>れる, <ruby>壊<rt>こわ</rt></ruby>れる, <ruby>遅<rt>おく</rt></ruby>れる kabi feʼllar bilan keladi.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Feʼlning oʻzi koʻpincha javobni berib turadi.</b>
  «Yoʻqotmoq», «unutmoq», «sinmoq» — bularning yaxshi tomoni
  yoʻq, demak afsus. «Qilmoq», «oʻqimoq», «yozmoq» — bular
  vazifa, demak tugatish. Shubha qolgan paytda esa gapdagi
  boshqa soʻzlarga qarang.</p>
</div>

<p>Diqqat qiling: bu yerda afsus <em>gapning mazmunidan</em>
kelib chiqmaydi — u <b>grammatikada</b> turadi. «Hamyonimni
yoʻqotdim» degan gapni しまう siz ham aytsa boʻladi
(<ruby>財布<rt>さいふ</rt></ruby>をなくしました), va u shunchaki
fakt boʻlib qoladi — xuddi politsiyaga bergan maʼlumotdek.
しまう qoʻshilganda esa gapga <em>odam</em> qaytadi: gapiruvchi
buni yoqtirmaganini ham aytib turadi. Aynan shuning uchun bu
qolipni imtihonda emas, kundalik hikoyada koʻp
eshitasiz.</p>

<h3>5. Ogʻzaki nutq: ちゃう va じゃう</h3>

<p>Suhbatda <b>てしまう</b> qisqaradi, va qisqarishi て yoki で
ga qarab ikki xil boʻladi.</p>

<div class="pj-say">
  <span class="pj-say__from"><ruby>食<rt>た</rt></ruby>べてしまう</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to"><ruby>食<rt>た</rt></ruby>べちゃう</span>
  <span class="pj-say__why"><b>て</b>しまう → <b>ちゃ</b>う</span>
</div>

<div class="pj-say">
  <span class="pj-say__from"><ruby>読<rt>よ</rt></ruby>んでしまう</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to"><ruby>読<rt>よ</rt></ruby>んじゃう</span>
  <span class="pj-say__why"><b>で</b>しまう → <b>じゃ</b>う</span>
</div>

<div class="pe-call pe-warn">
  <p><b>Qoidani jarangliligi hal qiladi.</b> て — jarangsiz,
  shuning uchun ちゃ. で — jarangli, shuning uchun じゃ. Bu PJ-6
  dagi dakuten qoidasining oʻzi: <b>ち</b> ustiga ikki nuqta
  qoʻysangiz <b>じ</b> boʻladi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>ちゃう ni yozmang, lekin taniy oling.</b> U animeda,
  qoʻshiqda va doʻstlar suhbatida toʻxtovsiz eshitiladi.
  Yozma ishda, imtihonda va ustoz bilan doim toʻliq
  <b>〜てしまいました</b>.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">財</span>
    <span class="pj-kanji__uz">boylik, mol</span>
    <span class="pj-kanji__on">オン: ザイ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">財布 (さいふ) — hamyon</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">壊</span>
    <span class="pj-kanji__uz">sindirmoq, buzilmoq</span>
    <span class="pj-kanji__on">オン: カイ</span>
    <span class="pj-kanji__kun">KUN: こわ(す), こわ(れる)</span>
    <span class="pj-kanji__note">壊す (こわす) — sindirmoq · 壊れる (こわれる) — sinmoq</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b><ruby>壊<rt>こわ</rt></ruby>す / <ruby>壊<rt>こわ</rt></ruby>れる — yana oʻsha する / なる chizigʻi.</b>
  PJ-57 da siz <ruby>決<rt>き</rt></ruby>める va
  <ruby>決<rt>き</rt></ruby>まる ni koʻrgansiz. Bu ham oʻsha juftlik:
  <ruby>壊<rt>こわ</rt></ruby>す — <em>men sindirdim</em>,
  <ruby>壊<rt>こわ</rt></ruby>れる — <em>oʻzi sindi</em>.
  Oʻzbekchada ham «sindirdim» va «sindi» — ikki boshqa feʼl.
  Va afsus qolipiga koʻpincha <em>ikkinchisi</em> qoʻshiladi:
  <ruby>壊<rt>こわ</rt></ruby>れてしまいました — «sinib qoldi».</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>むしまいました</p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby><b>んで</b>しまいました — しまう て-shakliga qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>んでちゃいました</p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby><b>んじゃ</b>いました — で dan keyin doim <b>じゃ</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ Inshoda: <ruby>忘<rt>わす</rt></ruby>れちゃいました</p>
  <p class="pe-fix__good">✓ <ruby>忘<rt>わす</rt></ruby>れて<b>しまいました</b> — yozma ishda toʻliq shakl.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>宿題<rt>しゅくだい</rt></ruby>をしてしまいました = «afsus, uy vazifasini qildim»</p>
  <p class="pe-fix__good">✓ Bu yerda maʼno <b>tugatish</b>: «hammasini qilib boʻldim». Feʼl yomon emas, demak afsus emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>忘<rt>わす</rt></ruby>れる ning てしまう shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>忘<rt>わす</rt></ruby>れてしまう</b> — II guruh, て-shakli <ruby>忘<rt>わす</rt></ruby>れて.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>読<rt>よ</rt></ruby>む ning qisqargan shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>読<rt>よ</rt></ruby>んじゃう</b> — て-shakli <ruby>読<rt>よ</rt></ruby>んで, demak <b>じゃ</b>う.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «<ruby>財布<rt>さいふ</rt></ruby>をなくしてしまいました» — qaysi maʼno?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Afsus.</b> «Yoʻqotmoq» feʼlining yaxshi tomoni yoʻq.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>宿題<rt>しゅくだい</rt></ruby>を<ruby>全部<rt>ぜんぶ</rt></ruby>してしまいました» — qaysi maʼno?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Tugatish.</b> «<ruby>全部<rt>ぜんぶ</rt></ruby>» soʻzi buni aniqlab turibdi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Nega <ruby>食<rt>た</rt></ruby>べてしまう → <ruby>食<rt>た</rt></ruby>べちゃう, lekin <ruby>飲<rt>の</rt></ruby>んでしまう → <ruby>飲<rt>の</rt></ruby>んじゃう?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki qisqarish <b>て / で</b> ga qarab boʻladi: て → ちゃ (jarangsiz), で → じゃ (jarangli).</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜てしまう</b> — …ib boʻlmoq; …ib qoʻymoq</li>
  <li><b>〜ちゃう · 〜じゃう</b> — ogʻzaki qisqargan shakl</li>
  <li><b><ruby>財布<rt>さいふ</rt></ruby></b> — hamyon</li>
  <li><b>なくす</b> — yoʻqotmoq (I guruh)</li>
  <li><b><ruby>壊<rt>こわ</rt></ruby>す</b> — sindirmoq (I guruh)</li>
  <li><b><ruby>壊<rt>こわ</rt></ruby>れる</b> — sinmoq (II guruh)</li>
  <li><b><ruby>寝坊<rt>ねぼう</rt></ruby>する</b> — uxlab qolmoq</li>
  <li><b><ruby>宿題<rt>しゅくだい</rt></ruby></b> — uy vazifasi</li>
  <li><b><ruby>消<rt>け</rt></ruby>す</b> — oʻchirmoq (I guruh)</li>
  <li><b><ruby>全部<rt>ぜんぶ</rt></ruby></b> — hammasi</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Bitta qolip, ikki maʼno: <b>«-ib boʻldim»</b> va <b>«-ib qoʻydim»</b>.</li>
    <li>Qaysi maʼno ekanini <b>feʼlning oʻzi</b> koʻrsatadi.</li>
    <li>て → <b>ちゃう</b>, で → <b>じゃう</b> — faqat ogʻzaki nutqda.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-59: 〜ておきます va 〜てみます — oldindan qilish va sinab koʻrish",
        "category": "japanese",
        "order": 59,
        "summary": (
            "Yana ikki yordamchi feʼl — va ikkalasi ham oʻzbekchada bor: "
            "«qilib qoʻymoq» (oldindan) va «qilib koʻrmoq». Ikkinchisida "
            "ikkala til ham aynan «koʻrmoq» feʼlini ishlatadi."
        ),
        "stories": ["ぶんかさいの じゅんび"],
        "content": """
<h2>PJ-59: 〜ておきます va 〜てみます — oldindan qilish va sinab koʻrish</h2>

<p>Oʻtgan darsda て-shakli ustiga <b>しまう</b> qoʻygan edingiz.
Bugun yana ikkita feʼl qoʻshiladi, va ularning ikkalasi ham
oʻzbek tilida allaqachon bor:</p>

<p>Ertaga uchun bilet olib <b>qoʻyaman</b>. → <b>〜ておく</b><br>
Bu taomni yeb <b>koʻraman</b>. → <b>〜てみる</b></p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>〜ておく — «oldindan qilib qoʻymoq» ni yasaysiz</li>
    <li>〜てみる — «qilib koʻrmoq» ni yasaysiz</li>
    <li>てみる va 〜たい farqini koʻrasiz</li>
    <li>Ogʻzaki 〜とく ni taniysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki yordamchi</span>
  <span class="pe-chip pe-chip--s">て + おく</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">て + みる</span>
</div>

<h3>1. 〜ておく — oldindan qilib qoʻymoq</h3>

<p><b>おく</b> yolgʻiz turganda «qoʻymoq» degani
(<ruby>本<rt>ほん</rt></ruby>を<ruby>机<rt>つくえ</rt></ruby>に
おく — kitobni stolga qoʻymoq). て-shakli ustiga qoʻyilganda
u <b>«kelajak uchun qilib qoʻymoq»</b> maʼnosini beradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>明日<rt>あした</rt></ruby>のチケットを<ruby>買<rt>か</rt></ruby>っておきます。</p>
  <p class="pe-ex__uz">Ertangi biletni olib qoʻyaman.</p>
  <p class="pe-ex__why">Ish hozir qilinadi, foydasi keyin koʻrinadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>会議<rt>かいぎ</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>に<ruby>資料<rt>しりょう</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んでおいてください。</p>
  <p class="pe-ex__uz">Yigʻilishdan oldin hujjatlarni oʻqib qoʻying.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «-ib qoʻymoq» — bu maʼnoning aynan oʻzi.</b>
  «Olib <em>qoʻyaman</em>», «yozib <em>qoʻyaman</em>», «tayyorlab
  <em>qoʻyaman</em>» — bu gaplarda ham ikkinchi feʼl ishning
  <em>kelajakka qaratilganini</em> aytadi. Yaponcha おく ham,
  oʻzbekcha «qoʻymoq» ham asl maʼnosida bir narsani joyiga
  qoʻyishni bildiradi — ikkala til ham oʻsha tasvirdan
  «tayyorlab qoʻyish» maʼnosini oʻstirgan.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Ikkinchi maʼnosi: shundayligicha qoldirmoq.</b>
  <ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けておいて
  ください — «derazani ochiq qoldiring». Bu yerda ham mantiq
  bir xil: ish <em>keyingi paytga</em> qaratilgan.</p>
</div>

<p>Bu qolipning kuchi shundaki, u <b>vaqtni ikkiga
boʻladi</b>: ish hozir bajariladi, lekin uning maʼnosi
keyinroq ochiladi. Shuning uchun ておく deyarli doim
«nima uchun?» degan savolga javob beradi — bilet
<em>ertaga uchun</em> olinadi, hujjat <em>yigʻilishdan
oldin</em> oʻqiladi. Gapda bu sabab koʻrsatilmagan
boʻlsa ham, tinglovchi uni oʻzi tushunadi.</p>

<h3>2. Ogʻzaki nutq: 〜とく</h3>

<div class="pj-say">
  <span class="pj-say__from"><ruby>買<rt>か</rt></ruby>っておく</span>
  <span class="pj-say__arrow">→</span>
  <span class="pj-say__to"><ruby>買<rt>か</rt></ruby>っとく</span>
  <span class="pj-say__why">ておく → とく · でおく → どく</span>
</div>

<div class="pe-call pe-warn">
  <p><b>Bu ham jaranglilik qoidasi.</b> PJ-58 dagi
  ちゃう / じゃう bilan bir xil: <b>て</b>おく → <b>と</b>く,
  <b>で</b>おく → <b>ど</b>く. Yozma ishda esa doim toʻliq
  shakl.</p>
</div>

<p>Bu qolip yapon tilida ayniqsa koʻp uchraydi, chunki u
gapga <b>ehtiyotkorlik</b> qoʻshadi. «Bugun qilaman» degan
gap qatʼiy; «bugun qilib qoʻyaman» esa yumshoqroq — ish
kelajak uchun, hozirgi paytga daʼvo qilmaydi. Yaponlar bunday
yumshatishni juda qadrlaydi, shuning uchun ておく ish
joylarida va xizmat koʻrsatishda deyarli har gapda
eshitiladi.</p>

<h3>3. 〜てみる — qilib koʻrmoq</h3>

<p>Mana darsdagi eng chiroyli joy. <b>みる</b> — «koʻrmoq».
て-shakli ustiga qoʻyilganda u <b>«qilib koʻrmoq»</b>
degani: ishni qilasiz va <em>natijasini koʻrasiz</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>料理<rt>りょうり</rt></ruby>を<ruby>食<rt>た</rt></ruby>べてみます。</p>
  <p class="pe-ex__uz">Bu taomni yeb koʻraman.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>服<rt>ふく</rt></ruby>を<ruby>着<rt>き</rt></ruby>てみてもいいですか。</p>
  <p class="pe-ex__uz">Bu kiyimni kiyib koʻrsam boʻladimi?</p>
  <p class="pe-ex__why">てみる + てもいいですか (PJ-55) — doʻkonda eng koʻp ishlatiladigan gap.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu ikki tilning eng aniq ustma-ust tushgan joyi.</b>
  Oʻzbekcha «yeb <em>koʻraman</em>», «kiyib
  <em>koʻraman</em>», «aytib <em>koʻraman</em>» — va yaponcha
  <b>〜てみる</b>. Ikkala tilda ham yordamchi feʼl
  <em>aynan «koʻrmoq»</em>: <ruby>見<rt>み</rt></ruby>る =
  koʻrmoq. Bu tasodif emas — ikkala xalq ham «sinab koʻrish»
  degan fikrni bir xil tasvir bilan qurgan: <em>qilasan va
  natijaga qaraysan</em>. Shuning uchun bu qolipni yodlash
  kerak emas; uni shunchaki tanib olish kifoya.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Faqat bitta izoh: みる bu yerda kana bilan yoziladi.</b>
  <ruby>見<rt>み</rt></ruby>る kanjisi asl «koʻrmoq» maʼnosida
  ishlatiladi; yordamchi feʼl boʻlganda esa <b>みる</b> deb
  yoziladi. Bu yapon tilining umumiy odati: yordamchi boʻlib
  qolgan feʼl kanjisini yoʻqotadi. <ruby>置<rt>お</rt></ruby>く →
  おく da ham shunday.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Ikkala yordamchi ham oʻz maʼnosini saqlab turibdi.</b>
  Oʻzbekcha «qoʻymoq» asl maʼnosida narsani joyiga qoʻyishdir —
  «kitobni stolga qoʻydim». «Koʻrmoq» esa koʻz bilan koʻrishdir.
  Yaponcha <ruby>置<rt>お</rt></ruby>く va <ruby>見<rt>み</rt></ruby>る ham xuddi
  shunday. Ikkala til ham bu ikki oddiy harakatdan bir xil
  koʻchma maʼno oʻstirgan: <em>joyiga qoʻyish</em> →
  tayyorlab qoʻyish, <em>koʻrish</em> → sinab koʻrish.
  Shuning uchun bu ikki qolipni tarjimadan emas, <b>tasvirdan</b>
  eslab qoling — shunda ular hech qachon aralashmaydi.</p>
</div>

<h3>4. てみる va 〜たい — chalkashtirmang</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">〜たい (PJ-39)</p>
    <p><ruby>食<rt>た</rt></ruby>べたいです。</p>
    <p>«Yegim kelyapti.» Bu <b>xohish</b> — hali qilmadim.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">〜てみる</p>
    <p><ruby>食<rt>た</rt></ruby>べてみます。</p>
    <p>«Yeb koʻraman.» Bu <b>qaror</b> — qilaman va natijaga
    qarayman.</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>Ikkalasini birga ham ishlatsa boʻladi:</b>
  <ruby>食<rt>た</rt></ruby>べて<b>みたい</b>です — «yeb koʻrgim
  kelyapti». Bu yaponchada juda koʻp uchraydi va oʻzbekchada
  ham xuddi shunday tuziladi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>てみる «harakat qilmoq» degani EMAS.</b> «Qancha
  harakat qilsam ham» degan maʼno uchun boshqa soʻzlar bor —
  <ruby>頑張<rt>がんば</rt></ruby>る yoki PJ-55 dagi
  いくら〜ても. てみる shunchaki <em>«bir marta qilib,
  nima boʻlishini koʻrmoq»</em>.</p>
</div>

<h3>5. Uchta yordamchi feʼl bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Oʻzbekcha</th><th>Ish qachon qaratilgan</th></tr>
  <tr><td class="pj-stem">〜てしまう</td><td class="pj-uz">-ib boʻlmoq · -ib qoʻymoq</td>
      <td class="pj-res">oʻtmishga — ish tugagan</td></tr>
  <tr><td class="pj-stem">〜ておく</td><td class="pj-uz">oldindan qilib qoʻymoq</td>
      <td class="pj-res">kelajakka — foydasi keyin</td></tr>
  <tr><td class="pj-stem">〜てみる</td><td class="pj-uz">qilib koʻrmoq</td>
      <td class="pj-res">hozirga — natijani bilmayman</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Uchalasi ham bitta qurilma.</b> て-shakli asosiy ishni
  aytadi, ikkinchi feʼl esa unga <em>munosabat</em> qoʻshadi.
  Yapon tilida bunday yordamchi feʼllar oʻnlab, va keyingi
  ikki dars (PJ-60, PJ-61) yana uchtasini qoʻshadi. Shuning
  uchun bu qurilmani hozir mustahkam oʻzlashtirib olish
  kerak.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">準</span>
    <span class="pj-kanji__uz">tayyorgarlik</span>
    <span class="pj-kanji__on">オン: ジュン</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">準備 (じゅんび) — tayyorgarlik</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">置</span>
    <span class="pj-kanji__uz">qoʻymoq</span>
    <span class="pj-kanji__on">オン: チ</span>
    <span class="pj-kanji__kun">KUN: お(く)</span>
    <span class="pj-kanji__note">置く (おく) — qoʻymoq · 位置 (いち) — joylashuv</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>買<rt>か</rt></ruby>うておきます</p>
  <p class="pe-fix__good">✓ <ruby>買<rt>か</rt></ruby><b>って</b>おきます — おく て-shakliga qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>食<rt>た</rt></ruby>べて<ruby>見<rt>み</rt></ruby>ます</p>
  <p class="pe-fix__good">✓ <ruby>食<rt>た</rt></ruby>べて<b>みます</b> — yordamchi feʼl kana bilan yoziladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>んでとく</p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby>ん<b>どく</b> — で dan keyin <b>ど</b>, xuddi じゃう kabi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ てみる = «harakat qilmoq»</p>
  <p class="pe-fix__good">✓ てみる = «<b>bir marta qilib koʻrmoq</b>». Harakat uchun — <ruby>頑張<rt>がんば</rt></ruby>る.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>買<rt>か</rt></ruby>う ning ておく shaklini yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>買<rt>か</rt></ruby>っておきます</b> — て-shakli <ruby>買<rt>か</rt></ruby>って (I guruh, う → って).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Bu taomni yeb koʻraman» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>この<ruby>料理<rt>りょうり</rt></ruby>を<ruby>食<rt>た</rt></ruby>べてみます</b> — みる kana bilan.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Bu kiyimni kiyib koʻrsam boʻladimi?» ni yozing.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>この<ruby>服<rt>ふく</rt></ruby>を<ruby>着<rt>き</rt></ruby>てみてもいいですか</b> — てみる + てもいいですか.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>読<rt>よ</rt></ruby>んでおく ning ogʻzaki shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>読<rt>よ</rt></ruby>んどく</b> — で dan keyin <b>ど</b>く.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>食<rt>た</rt></ruby>べたい va <ruby>食<rt>た</rt></ruby>べてみる — farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisi — <b>xohish</b> («yegim kelyapti»), ikkinchisi — <b>qaror</b> («yeb koʻraman»). Ikkalasini birga ham ishlatsa boʻladi: <ruby>食<rt>た</rt></ruby>べてみたいです.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ておく</b> — oldindan qilib qoʻymoq</li>
  <li><b>〜てみる</b> — qilib koʻrmoq</li>
  <li><b>〜とく · 〜どく</b> — ておく ning ogʻzaki shakli</li>
  <li><b><ruby>準備<rt>じゅんび</rt></ruby>する</b> — tayyorlamoq</li>
  <li><b><ruby>置<rt>お</rt></ruby>く</b> — qoʻymoq (I guruh)</li>
  <li><b><ruby>服<rt>ふく</rt></ruby></b> — kiyim</li>
  <li><b><ruby>着<rt>き</rt></ruby>る</b> — kiymoq (II guruh)</li>
  <li><b><ruby>資料<rt>しりょう</rt></ruby></b> — hujjat, material</li>
  <li><b><ruby>文化祭<rt>ぶんかさい</rt></ruby></b> — maktab madaniyat bayrami</li>
  <li><b><ruby>頑張<rt>がんば</rt></ruby>る</b> — harakat qilmoq (I guruh)</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>〜ておく = <b>oldindan qilib qoʻymoq</b> — ish kelajakka qaratilgan.</li>
    <li>〜てみる = <b>qilib koʻrmoq</b> — ikkala tilda ham «koʻrmoq» feʼli.</li>
    <li>Yordamchi feʼl <b>kana bilan</b> yoziladi: おく, みる.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-60: Berish-olish 1: あげる, くれる, もらう",
        "category": "japanese",
        "order": 60,
        "summary": (
            "Yaponchada «bermoq» degan bitta feʼl yoʻq — uchtasi bor, "
            "va qaysi birini tanlash sovgʻa QAYSI TOMONGA ketayotganiga "
            "bogʻliq. Bu dars oʻzbekchadan yordam olmaydi."
        ),
        "stories": ["おとしだま"],
        "content": """
<h2>PJ-60: Berish-olish 1: あげる, くれる, もらう</h2>

<p>Ochiq aytamiz: <b>bu dars oʻzbek tilidan yordam olmaydi.</b>
Oʻzbekchada «bermoq» bitta feʼl — kim kimga bersa ham, oʻsha
soʻz ishlatiladi. Yapon tilida esa uchta feʼl bor, va tanlov
<em>maʼnoga</em> emas, <b>yoʻnalishga</b> qarab qilinadi.</p>

<p>Shuning uchun bu darsni yodlash emas, <em>rasm chizib</em>
oʻrganish kerak. Oʻrtada siz turasiz; sovgʻa sizdan chiqadimi
yoki sizga keladimi — javob shu.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchta feʼlni yoʻnalish boʻyicha ajratasiz</li>
    <li>Har biriga qaysi qoʻshimchalar kelishini bilib olasiz</li>
    <li>Nega «<ruby>私<rt>わたし</rt></ruby>にあげました» notoʻgʻri ekanini tushunasiz</li>
    <li>«Oʻz odamim» tushunchasi bilan tanishasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch yoʻnalish</span>
  <span class="pe-chip pe-chip--s">あげる →</span>
  <span class="pe-chip pe-chip--v">← くれる</span>
  <span class="pe-chip pe-chip--o">もらう ←</span>
</div>

<h3>1. Uchta feʼl, uchta yoʻnalish</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Kim beradi</th><th>Kim oladi</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem">あげる</td><td class="pj-uz">MEN (yoki oʻz odamim)</td>
      <td class="pj-end">boshqa odam</td><td class="pj-res">men berdim</td></tr>
  <tr><td class="pj-stem">くれる</td><td class="pj-uz">boshqa odam</td>
      <td class="pj-end">MEN (yoki oʻz odamim)</td><td class="pj-res">u menga berdi</td></tr>
  <tr><td class="pj-stem">もらう</td><td class="pj-uz">boshqa odam</td>
      <td class="pj-end">MEN</td><td class="pj-res">men oldim</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>くれる va もらう bir voqeani ikki tomondan aytadi.</b>
  Tanaka menga kitob berdi — bu bitta voqea. Agar gapning egasi
  <b>Tanaka</b> boʻlsa: <ruby>田中<rt>たなか</rt></ruby>さんが
  くれました. Agar gapning egasi <b>men</b> boʻlsam:
  <ruby>私<rt>わたし</rt></ruby>がもらいました. Voqea bir xil,
  kamera boshqa joyda turibdi.</p>
</div>

<p>Bu uchta feʼlni yodlashning eng yomon yoʻli — ularni
uchta alohida soʻz sifatida yodlash. Eng yaxshi yoʻli esa
<b>bitta rasm</b>: qogʻozga oʻzingizni oʻrtaga chizing,
atrofingizga boshqa odamlarni qoʻying, va uchta strelka
torting. Tashqariga ketgani — あげる. Ichkariga kelgani —
くれる. Ichkariga kelganini <em>siz</em> aytsangiz —
もらう. Shu rasmni bir marta chizsangiz, dars tugadi;
qolgani faqat mashq.</p>

<h3>2. Qoʻshimchalar</h3>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MEN</small></span>
  <span class="pj-joshi__n">パリさん</span>
  <span class="pj-joshi__p">に<small>KIMGA</small></span>
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-joshi__p">を</span>
  <span class="pj-joshi__v">あげました</span>
  <span class="pj-joshi__uz">Men Pariga kitob berdim.</span>
</div>

<div class="pj-joshi">
  <span class="pj-joshi__n">パリさん</span>
  <span class="pj-joshi__p">が<small>KIM</small></span>
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">に<small>MENGA</small></span>
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-joshi__p">を</span>
  <span class="pj-joshi__v">くれました</span>
  <span class="pj-joshi__uz">Pari menga kitob berdi.</span>
</div>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>私<rt>わたし</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MEN</small></span>
  <span class="pj-joshi__n">パリさん</span>
  <span class="pj-joshi__p">に<small>KIMDAN</small></span>
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-joshi__p">を</span>
  <span class="pj-joshi__v">もらいました</span>
  <span class="pj-joshi__uz">Men Paridan kitob oldim.</span>
</div>

<div class="pe-call pe-warn">
  <p><b>もらう da に «-dan» degani.</b> Bu chalkash joy:
  bitta qoʻshimcha ikki xil ishlaydi. あげる va くれる bilan
  <b>に</b> — «kimga»; もらう bilan esa <b>に</b> — «kimdan».
  Ishonchsiz boʻlsangiz, もらう uchun <b>から</b> ham ishlatsa
  boʻladi: パリさん<b>から</b>もらいました.</p>
</div>

<p>Qoʻshimchalarga alohida eʼtibor bering: uchala qolipda
ham narsa <b>を</b> oladi, odam esa <b>に</b>. Oʻzgaradigan
narsa faqat bitta — <em>kim ega boʻlib turibdi</em>.
あげる va もらう da ega men boʻlaman, くれる da esa
boshqa odam. Shuning uchun gap tuzayotganda birinchi savol
«kim berdi?» emas, <b>«kimni gap boshiga qoʻyaman?»</b>
boʻlishi kerak — feʼl shundan keyin oʻzi tanlanadi.</p>

<h3>3. Eng koʻp qilinadigan xato</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">✗ NOTOʻGʻRI</p>
    <p>パリさんは<ruby>私<rt>わたし</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>を<b>あげました</b>。</p>
    <p>あげる menga qarab yoʻnala olmaydi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">✓ TOʻGʻRI</p>
    <p>パリさんは<ruby>私<rt>わたし</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>を<b>くれました</b>。</p>
    <p>Menga kelayotgan sovgʻa doim <b>くれる</b>.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bu farqni feʼlda emas, QOʻSHIMCHAda
  koʻrsatadi.</b> «U <em>menga</em> berdi» va «Men
  <em>unga</em> berdim» — ikkala gapda ham feʼl bitta:
  «bermoq». Yoʻnalishni «menga» va «unga» soʻzlari olib
  yuribdi. Yaponchada esa aksincha: yoʻnalish <b>feʼlning
  ichida</b>, shuning uchun feʼlni notoʻgʻri tanlasangiz, gap
  buziladi — hatto «<ruby>私<rt>わたし</rt></ruby>に» soʻzi
  oʻrnida tursa ham. Yodda tuting: <b>oʻzbekcha yoʻnalish —
  qoʻshimchada; yaponcha yoʻnalish — feʼlda.</b></p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">ムニラさんは<ruby>妹<rt>いもうと</rt></ruby>にプレゼントをあげました。</p>
  <p class="pe-ex__uz">Munira singlisiga sovgʻa berdi.</p>
  <p class="pe-ex__why">Gapda men yoʻqman — ikkalasi ham tashqaridagi odamlar. Bunday holda doim <b>あげる</b>.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Ikkala odam ham begona boʻlsa nima boʻladi?</b>
  Oʻzbekcha «Munira singlisiga berdi» degan gapda hech qanday
  muammo yoʻq. Yaponchada ham yoʻq — bunday holda
  <b>あげる</b> ishlatiladi, chunki sovgʻa sizdan uzoqlashib
  ketyapti. Qoidani shunday eslab qoling: <b>くれる</b> faqat
  sovgʻa <em>sizga yoki sizniki</em>ga kelganda chiqadi;
  qolgan hamma holatda <b>あげる</b>. Shuning uchun くれる —
  uchalasidan eng tor, va eng koʻp unutiladigan feʼl.</p>
</div>

<h3>4. «Oʻz odamim» — うち</h3>

<p>Yapon tili sizni yolgʻiz emas, <b>bir guruh</b> deb koʻradi:
oilangiz, sinfingiz, ishxonangiz. Bu guruh <b>うち</b> («ichkari»)
deb ataladi, qolganlari esa <b>そと</b> («tashqari»).</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>先生<rt>せんせい</rt></ruby>が<ruby>弟<rt>おとうと</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>をくれました。</p>
  <p class="pe-ex__uz">Oʻqituvchi ukamga kitob berdi.</p>
  <p class="pe-ex__why">Sovgʻa menga emas, <em>ukamga</em> kelgan — lekin ukam ham «oʻz odamim», shuning uchun くれる.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Bu tushuncha keyinroq katta mavzuga aylanadi.</b>
  PJ-72 butunlay <ruby>内<rt>うち</rt></ruby> va
  <ruby>外<rt>そと</rt></ruby> haqida, va keigo (PJ-68 … PJ-71)
  ham shu chiziq ustiga qurilgan. Hozircha bitta qoida yetarli:
  <em>oilangiz sizning tomoningizda</em>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>友<rt>とも</rt></ruby>だちに<ruby>誕生日<rt>たんじょうび</rt></ruby>のプレゼントをもらいました。</p>
  <p class="pe-ex__uz">Doʻstimdan tugʻilgan kun sovgʻasini oldim.</p>
  <p class="pe-ex__why">Ega — men, demak <b>もらう</b>. Oʻsha voqeani doʻstim ega qilib aytsa: <ruby>友<rt>とも</rt></ruby>だちがくれました.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada «oldim» va «berdi» bor — bu yarmi.</b>
  «Doʻstimdan sovgʻa <em>oldim</em>» va «doʻstim sovgʻa
  <em>berdi</em>» — siz bu ikki gapni allaqachon farqlaysiz,
  va ular yaponchadagi <b>もらう</b> va <b>くれる</b> ga
  toʻgʻri tushadi. Qiyin joyi faqat bitta: oʻzbekchada
  «berdi» ikkala yoʻnalishga ham xizmat qiladi, yaponchada
  esa yoʻq. Yaʼni siz uchta feʼlning <em>ikkitasini</em>
  allaqachon bilasiz — faqat uchinchisini, くれる ni,
  ajratib olish kerak.</p>
</div>

<h3>5. Muloyim shakllari</h3>

<p>Uchala feʼlning ham hurmatli shakli bor. Hozircha ularni
<b>tanib olish</b> kifoya — yasashni PJ-68 … PJ-71 da
oʻrganasiz.</p>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">あげる</span>
    <span class="pj-level__ja">さしあげる</span>
    <span class="pj-level__who">kattaroq odamga berganda</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name">くれる</span>
    <span class="pj-level__ja">くださる</span>
    <span class="pj-level__who">kattaroq odam menga berganda</span>
  </div>
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name">もらう</span>
    <span class="pj-level__ja">いただく</span>
    <span class="pj-level__who">kattaroq odamdan olganda</span>
  </div>
</div>

<div class="pe-call pe-rule">
  <p><b>いただきます — endi tushunarli boʻldi.</b> Ovqatdan
  oldin aytiladigan bu ibora <b>いただく</b> feʼlining muloyim
  shakli: «<em>olaman</em>». Yaʼni siz taomni kimdandir —
  pishirgan odamdan, dehqondan, tabiatdan — olayotganingizni
  tan olasiz. Shuning uchun uni «yoqimli ishtaha» deb tarjima
  qilish notoʻgʻri.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">贈</span>
    <span class="pj-kanji__uz">sovgʻa qilmoq</span>
    <span class="pj-kanji__on">オン: ゾウ</span>
    <span class="pj-kanji__kun">KUN: おく(る)</span>
    <span class="pj-kanji__note">贈り物 (おくりもの) — sovgʻa</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">弟</span>
    <span class="pj-kanji__uz">ini, kichik uka</span>
    <span class="pj-kanji__on">オン: ダイ, テイ</span>
    <span class="pj-kanji__kun">KUN: おとうと</span>
    <span class="pj-kanji__note">弟 (おとうと) — uka · 兄弟 (きょうだい) — aka-uka</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ パリさんは<ruby>私<rt>わたし</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>をあげました</p>
  <p class="pe-fix__good">✓ …<b>くれました</b> — menga kelayotgan sovgʻa doim くれる.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>はパリさんに<ruby>本<rt>ほん</rt></ruby>をくれました</p>
  <p class="pe-fix__good">✓ …<b>あげました</b> — mendan chiqayotgan sovgʻa doim あげる.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>私<rt>わたし</rt></ruby>はパリさん<b>を</b>もらいました</p>
  <p class="pe-fix__good">✓ パリさん<b>に</b> (yoki <b>から</b>) もらいました — «kimdan» に yoki から oladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>先生<rt>せんせい</rt></ruby>が<ruby>弟<rt>おとうと</rt></ruby>にあげました</p>
  <p class="pe-fix__good">✓ …<b>くれました</b> — ukam ham «oʻz odamim», demak sovgʻa ichkariga kelyapti.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Men Muniraga sovgʻa berdim» — qaysi feʼl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>あげました</b> — sovgʻa mendan chiqyapti.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Munira menga sovgʻa berdi» — qaysi feʼl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>くれました</b> — sovgʻa menga kelyapti. «あげました» notoʻgʻri boʻlardi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Oʻsha voqeani «men» ni ega qilib ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>私<rt>わたし</rt></ruby>はムニラさんにプレゼントをもらいました</b> — bir voqea, boshqa kamera.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «<ruby>先生<rt>せんせい</rt></ruby>が<ruby>弟<rt>おとうと</rt></ruby>に…» — qaysi feʼl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>くれました</b> — ukam <b>うち</b>, yaʼni oʻz odamim.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. いただきます nima degani?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>«Olaman»</b> — いただく feʼlining muloyim shakli. Taomni kimdandir olayotganingizni tan olasiz.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>あげる</b> — bermoq (mendan chiqadi, II guruh)</li>
  <li><b>くれる</b> — bermoq (menga keladi, II guruh)</li>
  <li><b>もらう</b> — olmoq (I guruh)</li>
  <li><b>さしあげる · くださる · いただく</b> — muloyim shakllari</li>
  <li><b><ruby>内<rt>うち</rt></ruby></b> — oʻz guruhim</li>
  <li><b><ruby>外<rt>そと</rt></ruby></b> — tashqaridagilar</li>
  <li><b>プレゼント</b> — sovgʻa</li>
  <li><b><ruby>贈<rt>おく</rt></ruby>り<ruby>物<rt>もの</rt></ruby></b> — sovgʻa (rasmiyroq)</li>
  <li><b><ruby>弟<rt>おとうと</rt></ruby></b> — uka</li>
  <li><b>お<ruby>年玉<rt>としだま</rt></ruby></b> — Yangi yil puli</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Oʻzbekchada yoʻnalish <b>qoʻshimchada</b>, yaponchada <b>feʼlda</b>.</li>
    <li>Menga kelsa — <b>くれる</b>; mendan chiqsa — <b>あげる</b>; men olsam — <b>もらう</b>.</li>
    <li>Oilam <b>mening tomonimda</b> turadi.</li>
  </ul>
</div>
""",
    },
]
