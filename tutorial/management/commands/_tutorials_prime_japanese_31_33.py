# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-31 … PJ-33: て-shakli ish boshlaydi.

PJ-29 va PJ-30 shaklni berdi. Bu uchlik uni ishga soladi: davom etayotgan ish,
iltimos va ruxsat, taqiq va majburiyat.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_31_33.py --author=prime
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
        "title": "PJ-31: 〜ています — davom etayotgan ish va holat",
        "category": "japanese",
        "order": 31,
        "summary": (
            "て-shaklining birinchi vazifasi. Bitta qolip ikki ish qiladi: "
            "«hozir qilyapti» va «shunday holatda». Ikkinchisi oʻzbek "
            "oʻquvchini eng koʻp adashtiradigan joy."
        ),
        "stories": ["いま なにを していますか"],
        "content": """
<h2>PJ-31: 〜ています — davom etayotgan ish va holat</h2>

<p>Oʻtgan ikki darsda て-shaklini yasashni oʻrgandingiz. Endi u ish boshlaydi.</p>

<p>Birinchi vazifasi eng koʻp uchraydigani: <b>て + います</b>. Bu qolip ikki
ish qiladi, va ikkinchisi oʻzbek oʻquvchini deyarli har doim adashtiradi —
shuning uchun ikkalasini boshidanoq ajratib olamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>«Hozir qilyapman» degan gapni tuzasiz</li>
    <li>Ikkinchi maʼnoni — <b>holat</b>ni — tanib olasiz</li>
    <li>Doim ています da turadigan feʼllarni yodlab olasiz</li>
    <li>«Bilmayman» ni <em>toʻgʻri</em> aytishni oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">て-shakli + います</span>
  <span class="pe-chip pe-chip--v"><ruby>読<rt>よ</rt></ruby>んで</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">います</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o"><ruby>読<rt>よ</rt></ruby>んでいます</span>
</div>

<h3>1. Birinchi maʼno: hozir davom etayotgan ish</h3>

<p>Eng oson qismi. Kimdir <em>ayni damda</em> nimadir qilyapti.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">ラノさんは<ruby>今<rt>いま</rt></ruby><ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んでいます。</p>
  <p class="pe-ex__rom">rano-san wa ima hon o yonde imasu</p>
  <p class="pe-ex__uz">Rano hozir kitob oʻqiyapti.</p>
  <p class="pe-ex__why"><ruby>読<rt>よ</rt></ruby>みます — «oʻqiyman» (odat yoki kelasi). <ruby>読<rt>よ</rt></ruby>んでいます — «hozir oʻqiyapman». Farq katta.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham ikkita shakl bor</b> va farqi aynan shu:
  «oʻqiyman» va «oʻqi<b>yapman</b>». Yapon tilida
  <ruby>読<rt>よ</rt></ruby>みます birinchisiga,
  <ruby>読<rt>よ</rt></ruby>んでいます ikkinchisiga toʻgʻri keladi. Yaʼni bu
  yerda ikki til bir-biriga juda yaqin — qiyinchilik keyingi qismda
  boshlanadi.</p>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oddiy shakl</th><th>Davom etayotgan</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べます</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べています</td><td class="pj-uz">yeyapti</td></tr>
  <tr><td class="pj-stem"><ruby>書<rt>か</rt></ruby>きます</td>
      <td class="pj-res"><ruby>書<rt>か</rt></ruby>いています</td><td class="pj-uz">yozyapti</td></tr>
  <tr><td class="pj-stem"><ruby>泳<rt>およ</rt></ruby>ぎます</td>
      <td class="pj-res"><ruby>泳<rt>およ</rt></ruby>いでいます</td><td class="pj-uz">suzyapti</td></tr>
  <tr><td class="pj-stem"><ruby>勉強<rt>べんきょう</rt></ruby>します</td>
      <td class="pj-res"><ruby>勉強<rt>べんきょう</rt></ruby>しています</td><td class="pj-uz">oʻqiyapti</td></tr>
</table></div>

<h3>2. Inkor va oʻtgan zamon</h3>

<p>います — bu oddiy feʼl, shuning uchun u odatdagidek tuslanadi. て-shakli esa
hech qachon oʻzgarmaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Yaponcha</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">hozirgi</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>んでいます</td><td class="pj-uz">oʻqiyapti</td></tr>
  <tr><td class="pj-stem">inkor</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>んでいません</td><td class="pj-uz">oʻqimayapti</td></tr>
  <tr><td class="pj-stem">oʻtgan</td><td class="pj-res"><ruby>読<rt>よ</rt></ruby>んでいました</td><td class="pj-uz">oʻqiyotgan edi</td></tr>
</table></div>

<h3>3. Ikkinchi maʼno: holat</h3>

<p>Mana darsning qiyin joyi. Baʼzi feʼllar bilan ています <em>davom etayotgan
ish</em>ni emas, <b>hozirgi holat</b>ni bildiradi — yaʼni oʻtmishda boʻlgan
bir ish natijasi hozir turibdi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">ISH DAVOM ETYAPTI</p>
    <p><ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んでいます</p>
    <p>Hozir oʻqiyapti — qoʻlida kitob.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">HOLAT</p>
    <p>タシケントに<ruby>住<rt>す</rt></ruby>んでいます</p>
    <p>Toshkentda yashaydi — bir marta koʻchib kelgan, natijasi davom etyapti.</p></div>
</div>

<div class="pe-call pe-rule">
  <p><b>Qanday ajratiladi?</b> Feʼlning maʼnosiga qarang. Agar ish
  <em>davom etadigan</em> boʻlsa (oʻqish, yeyish, yozish) — birinchi maʼno.
  Agar ish <em>bir zumda tugaydigan</em> boʻlsa (koʻchib kelish, turmush
  qurish, bilib olish) — ikkinchi maʼno: natija hozir turibdi.</p>
</div>

<h3>4. Doim ています da turadigan feʼllar</h3>

<p>Toʻrtta feʼl bor, ular oʻzbekcha oddiy hozirgi zamon bilan tarjima
qilinadi, lekin yaponchada <b>doim</b> ています shaklida turadi. Ularni
shunday, tayyor holda yodlang.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Yaponcha</th><th>Oʻzbekcha</th><th>Diqqat</th></tr>
  <tr><td class="pj-res"><ruby>知<rt>し</rt></ruby>っています</td><td class="pj-uz">bilaman</td>
      <td class="pj-end"><ruby>知<rt>し</rt></ruby>ります deyilmaydi</td></tr>
  <tr><td class="pj-res"><ruby>住<rt>す</rt></ruby>んでいます</td><td class="pj-uz">yashayman</td>
      <td class="pj-end"><ruby>住<rt>す</rt></ruby>みます deyilmaydi</td></tr>
  <tr><td class="pj-res"><ruby>持<rt>も</rt></ruby>っています</td><td class="pj-uz">bor, olib yurgan</td>
      <td class="pj-end"><ruby>持<rt>も</rt></ruby>ちます deyilmaydi</td></tr>
  <tr><td class="pj-res"><ruby>結婚<rt>けっこん</rt></ruby>しています</td><td class="pj-uz">turmush qurgan</td>
      <td class="pj-end">holat, ish emas</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">イノムさんは<ruby>私<rt>わたし</rt></ruby>の<ruby>名前<rt>なまえ</rt></ruby>を<ruby>知<rt>し</rt></ruby>っています。パリさんはサマルカンドに<ruby>住<rt>す</rt></ruby>んでいます。</p>
  <p class="pe-ex__rom">inomu-san wa watashi no namae o shitte imasu. pari-san wa samarukando ni sunde imasu</p>
  <p class="pe-ex__uz">Inom mening ismimni biladi. Pari Samarqandda yashaydi.</p>
  <p class="pe-ex__why">Oʻzbekchada ikkalasi ham oddiy hozirgi zamon, yaponchada esa ikkalasi ham <b>ています</b>. Bu — yodlanadigan farq.</p>
</div>

<h3>5. «Bilmayman» — kursdagi eng mashhur tuzoq</h3>

<p>Mantiq boʻyicha <ruby>知<rt>し</rt></ruby>っています ning inkori
«<ruby>知<rt>し</rt></ruby>っていません» boʻlishi kerak edi. Boʻlmaydi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">BILAMAN</p>
    <p class="pj-big">✓</p>
    <p><ruby>知<rt>し</rt></ruby>っています</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">BILMAYMAN</p>
    <p class="pj-big">✓</p>
    <p><ruby>知<rt>し</rt></ruby>りません</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>Faqat shu feʼlda shunday.</b> «Bilish» — bu holat: u
  <em>bor</em> yoki <em>yoʻq</em>. Yaponcha «yoʻq» ni oddiy inkor bilan
  aytadi: <b><ruby>知<rt>し</rt></ruby>りません</b>. Boshqa feʼllar
  odatdagidek ています → ていません yoʻlidan boradi.</p>
</div>

<h3>6. Odat maʼnosi</h3>

<p>Uchinchi, kichikroq vazifasi: <b>takrorlanadigan ish</b> — ish joyi, oʻqish
joyi, muntazam mashgʻulot.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">ムニラさんは<ruby>学校<rt>がっこう</rt></ruby>で<ruby>日本語<rt>にほんご</rt></ruby>を<ruby>教<rt>おし</rt></ruby>えています。</p>
  <p class="pe-ex__rom">munira-san wa gakkō de nihongo o oshiete imasu</p>
  <p class="pe-ex__uz">Munira maktabda yapon tili oʻqitadi.</p>
  <p class="pe-ex__why">Bu «hozir shu daqiqada oʻqityapti» degani emas — bu uning <b>ishi</b>. Kasb va muntazam mashgʻulot doim ています bilan aytiladi.</p>
</div>

<h3>7. Savol: «Nima qilyapsiz?»</h3>

<p>Bu qolipning eng koʻp eshitiladigan koʻrinishi — savol. PJ-18 dagi
soʻroq soʻzlari shu yerda ishga tushadi.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>今<rt>いま</rt></ruby></span>
  <span class="pj-joshi__n"><ruby>何<rt>なに</rt></ruby></span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__v">していますか</span>
  <span class="pj-joshi__uz">Hozir nima qilyapsiz?</span>
</div>

<p>Javob ham oʻsha shaklda qaytadi — bu yapon suhbatining odatiy qoidasi:
savol qanday shaklda berilsa, javob ham shunday shaklda keladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">— <ruby>今<rt>いま</rt></ruby><ruby>何<rt>なに</rt></ruby>をしていますか。<br>— <ruby>宿題<rt>しゅくだい</rt></ruby>をしています。</p>
  <p class="pe-ex__rom">ima nani o shite imasu ka / shukudai o shite imasu</p>
  <p class="pe-ex__uz">— Hozir nima qilyapsiz? — Uy vazifasi qilyapman.</p>
  <p class="pe-ex__why">Savolda ham, javobda ham <b>しています</b>. «します» deb javob bersangiz, «qilaman» chiqadi — savolga toʻgʻri kelmaydi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>知<rt>し</rt></ruby>っていません</p>
  <p class="pe-fix__good">✓ <ruby>知<rt>し</rt></ruby><b>りません</b> — «bilmayman». Butun tilda shu bitta feʼl bunday tutadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ タシケントに<ruby>住<rt>す</rt></ruby>みます</p>
  <p class="pe-fix__good">✓ タシケントに<ruby>住<rt>す</rt></ruby><b>んでいます</b> — «yashayman» doim ています shaklida.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>みています</p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby><b>んで</b>います — ています <b>ます dan emas, て-shaklidan</b> yasaladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>食<rt>た</rt></ruby>べる dan «yeyapti» ni yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>食<rt>た</rt></ruby>べています</b> — て-shakli + います.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Bilmayman» yaponchada qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>知<rt>し</rt></ruby>りません</b>. «<ruby>知<rt>し</rt></ruby>っていません» deyilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Toshkentda yashayman» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>タシケントに<ruby>住<rt>す</rt></ruby>んでいます。</b> Bu feʼl doim ています da turadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>読<rt>よ</rt></ruby>んでいます va <ruby>読<rt>よ</rt></ruby>みます farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisi — <b>hozir oʻqiyapti</b>, ikkinchisi — odat yoki kelasi zamon: «oʻqiyman».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Feʼl davom etadiganmi yoki bir zumda tugaydiganmi — buni bilish nega kerak?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki <b>ています</b> ning maʼnosi shunga qarab oʻzgaradi: davom etayotgan <b>ish</b> yoki qolgan <b>holat</b>.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜ています</b> — qilyapti; shunday holatda</li>
  <li><b><ruby>知<rt>し</rt></ruby>っています</b> — bilaman</li>
  <li><b><ruby>知<rt>し</rt></ruby>りません</b> — bilmayman</li>
  <li><b><ruby>住<rt>す</rt></ruby>む</b> — yashamoq (I guruh)</li>
  <li><b><ruby>持<rt>も</rt></ruby>つ</b> — ega boʻlmoq, olib yurmoq (I guruh)</li>
  <li><b><ruby>結婚<rt>けっこん</rt></ruby>する</b> — turmush qurmoq</li>
  <li><b><ruby>今<rt>いま</rt></ruby></b> — hozir</li>
  <li><b><ruby>名前<rt>なまえ</rt></ruby></b> — ism</li>
  <li><b>タシケント</b> — Toshkent</li>
  <li><b>サマルカンド</b> — Samarqand</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>て-shakli + います</b> — ます dan emas, て-shaklidan.</li>
    <li>Ikki maʼno: davom etayotgan <b>ish</b> yoki qolgan <b>holat</b>.</li>
    <li><b><ruby>知<rt>し</rt></ruby>りません</b> — «bilmayman». Yagona istisno, hozirdan yodlang.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-32: 〜てください va 〜てもいいです — iltimos va ruxsat",
        "category": "japanese",
        "order": 32,
        "summary": (
            "て-shaklining ikkinchi va uchinchi vazifasi: birov nimadir "
            "qilishini soʻrash, va nimadir qilsa boʻladimi deb soʻrash. "
            "Sinfda kuniga eshitiladigan ikki qolip."
        ),
        "stories": ["きょうしつの にほんご"],
        "content": """
<h2>PJ-32: 〜てください va 〜てもいいです — iltimos va ruxsat</h2>

<p>Bugungi ikki qolip sinfda kuniga oʻn marta eshitiladi. Biri bilan
<b>soʻraysiz</b>, ikkinchisi bilan <b>ruxsat oʻlchaysiz</b> — va ikkalasi ham
oʻsha bir て-shaklidan yasaladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Muloyim iltimos qilasiz: 〜てください</li>
    <li>Ruxsat soʻraysiz: 〜てもいいですか</li>
    <li>Ruxsat berasiz va muloyim rad qilasiz</li>
    <li>てください ni <em>qachon ishlatmaslik</em> kerakligini bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta shakl, ikkita vazifa</span>
  <span class="pe-chip pe-chip--v">て + ください</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">て + もいいです</span>
</div>

<h3>1. 〜てください — «iltimos, qiling»</h3>

<p>て-shakliga <b>ください</b> qoʻshasiz. Xolos — hech qanday oʻzgarish yoʻq.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat shakli</th><th>て-shakli</th><th>Iltimos</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>待<rt>ま</rt></ruby>つ</td><td class="pj-stem"><ruby>待<rt>ま</rt></ruby>って</td>
      <td class="pj-res"><ruby>待<rt>ま</rt></ruby>ってください</td><td class="pj-uz">kuting</td></tr>
  <tr><td><ruby>見<rt>み</rt></ruby>せる</td><td class="pj-stem"><ruby>見<rt>み</rt></ruby>せて</td>
      <td class="pj-res"><ruby>見<rt>み</rt></ruby>せてください</td><td class="pj-uz">koʻrsating</td></tr>
  <tr><td><ruby>開<rt>あ</rt></ruby>ける</td><td class="pj-stem"><ruby>開<rt>あ</rt></ruby>けて</td>
      <td class="pj-res"><ruby>開<rt>あ</rt></ruby>けてください</td><td class="pj-uz">oching</td></tr>
  <tr><td><ruby>座<rt>すわ</rt></ruby>る</td><td class="pj-stem"><ruby>座<rt>すわ</rt></ruby>って</td>
      <td class="pj-res"><ruby>座<rt>すわ</rt></ruby>ってください</td><td class="pj-uz">oʻtiring</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">すみません、もう<ruby>一度<rt>いちど</rt></ruby><ruby>言<rt>い</rt></ruby>ってください。</p>
  <p class="pe-ex__rom">sumimasen, mō ichido itte kudasai</p>
  <p class="pe-ex__uz">Kechirasiz, yana bir marta ayting.</p>
  <p class="pe-ex__why">Bu — yapon tilini oʻrganayotgan odam eng koʻp ishlatadigan gap. Yodlab qoʻying, birinchi kundanoq kerak boʻladi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>てください iltimos emas, koʻrsatma.</b> U muloyim, lekin uning
  ostida «buni qiling» degan maʼno yotadi: oʻqituvchi oʻquvchiga, shifokor
  bemorga, doʻkonchi mijozga shunday gapiradi. <b>Katta yoshli
  begonadan xizmat soʻraganda</b> undan foydalanmang — u yerda boshqa,
  yumshoqroq qoliplar bor va ularni keyinroq koʻramiz.</p>
</div>

<h3>2. Inkor bilan aralashtirmang</h3>

<p>Tabiiy savol: «qilmang» qanday aytiladi? Javob — <b>てください ning
inkori yoʻq</b>. て-shakli oʻzi ijobiy, unga ください qoʻshib inkor
chiqarib boʻlmaydi.</p>

<p>«Qilmang» ning oʻz shakli bor — <b>〜ないでください</b> — va u butunlay
boshqa oʻzakdan, <b>ない-shaklidan</b> yasaladi. Uni PJ-34 da koʻramiz.
Bugun faqat <b>ijobiy</b> iltimos: nimadir qilishni soʻrash.</p>

<h3>3. Sinf yaponchasi — teng yarmi てください bilan</h3>

<p>Yapon tili darsida oʻqituvchi aytadigan koʻrsatmalarning deyarli hammasi
shu qolipda. Ularni <b>tayyor ibora</b> sifatida yodlab qoʻysangiz, darsni
tarjimasiz tushuna boshlaysiz.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Koʻrsatma</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res"><ruby>見<rt>み</rt></ruby>てください</td><td class="pj-uz">qarang</td></tr>
  <tr><td class="pj-res"><ruby>聞<rt>き</rt></ruby>いてください</td><td class="pj-uz">tinglang</td></tr>
  <tr><td class="pj-res"><ruby>読<rt>よ</rt></ruby>んでください</td><td class="pj-uz">oʻqing</td></tr>
  <tr><td class="pj-res"><ruby>書<rt>か</rt></ruby>いてください</td><td class="pj-uz">yozing</td></tr>
  <tr><td class="pj-res"><ruby>言<rt>い</rt></ruby>ってください</td><td class="pj-uz">ayting</td></tr>
  <tr><td class="pj-res"><ruby>座<rt>すわ</rt></ruby>ってください</td><td class="pj-uz">oʻtiring</td></tr>
  <tr><td class="pj-res"><ruby>立<rt>た</rt></ruby>ってください</td><td class="pj-uz">turing</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Beshtasi I guruhdan.</b> <ruby>聞<rt>き</rt></ruby>いて,
  <ruby>読<rt>よ</rt></ruby>んで, <ruby>書<rt>か</rt></ruby>いて,
  <ruby>言<rt>い</rt></ruby>って, <ruby>立<rt>た</rt></ruby>って — yaʼni bu
  jadval PJ-30 dagi beshta qoidaning tirik takrori. Har birini koʻrganda
  oʻzingizga «qaysi qoida?» deb savol bering.</p>
</div>

<h3>4. 〜てもいいです — «qilsa boʻladi»</h3>

<p>て-shakliga <b>もいいです</b> qoʻshiladi. Soʻzma-soʻz maʼnosi «qilsa ham
yaxshi» — yaʼni ruxsat bor.</p>

<div class="pj-joshi">
  <span class="pj-joshi__v"><ruby>座<rt>すわ</rt></ruby>って</span>
  <span class="pj-joshi__p">も<small>HAM</small></span>
  <span class="pj-joshi__n">いい</span>
  <span class="pj-joshi__v">ですか</span>
  <span class="pj-joshi__uz">Oʻtirsam boʻladimi?</span>
</div>

<div class="pe-call pe-tip">
  <p><b>も va いい tanish.</b> PJ-19 da も — «ham», PJ-25 da いい —
  «yaxshi». Yaʼni bu yangi soʻz emas, tanish boʻlaklardan yigʻilgan qolip:
  «qilsa <em>ham</em> yaxshi». Yapon grammatikasi shunday ishlaydi — kichik
  qismlar bir-birining ustiga qoʻyiladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>先生<rt>せんせい</rt></ruby>、<ruby>窓<rt>まど</rt></ruby>を<ruby>開<rt>あ</rt></ruby>けてもいいですか。</p>
  <p class="pe-ex__rom">sensei, mado o akete mo ii desu ka</p>
  <p class="pe-ex__uz">Ustoz, derazani ochsam boʻladimi?</p>
  <p class="pe-ex__why">Savol shaklida — <b>ですか</b>. Nuqtasiz, oddiy gap sifatida aytilsa, u ruxsat <em>berish</em> boʻladi.</p>
</div>

<h3>5. Javob berish</h3>

<p>Ruxsat berish oson. Rad qilish esa yaponchada deyarli hech qachon
toʻgʻridan-toʻgʻri boʻlmaydi — bu madaniy qoida, grammatik emas.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">RUXSAT BOR</p>
    <p>はい、いいですよ。</p>
    <p>«Ha, boʻladi.» Qisqa va tabiiy.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">RUXSAT YOʻQ</p>
    <p>すみません、ちょっと…</p>
    <p>«Kechirasiz, biroz…» — gap tugatilmaydi.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>«ちょっと…» ni tarjima qilib boʻlmaydi, lekin oʻzbek oʻquvchi uni
  yaxshi tushunadi.</b> Oʻzbekchada ham «Yoʻq» deb kesib tashlamaymiz —
  «Qiyinroq boʻladi-da…» yoki «Hozir bir oz…» deb qoʻyamiz va suhbatdosh
  hammasini tushunadi. Yapon tilida bu odat yanada kuchli: gapni
  <b>tugatmaslik</b> ning oʻzi javob. Yaponcha «yoʻq» ni izlamang — u
  koʻpincha aytilmaydi.</p>
</div>

<h3>6. Ikkalasini bir suhbatda</h3>

<div class="pe-ex">
  <p class="pe-ex__ja">— <ruby>教科書<rt>きょうかしょ</rt></ruby>を<ruby>見<rt>み</rt></ruby>せてください。<br>— どうぞ。<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ってもいいですか。<br>— はい、いいですよ。</p>
  <p class="pe-ex__rom">kyōkasho o misete kudasai / dōzo. shashin o totte mo ii desu ka / hai, ii desu yo</p>
  <p class="pe-ex__uz">— Darslikni koʻrsating. — Marhamat. Rasmga olsam boʻladimi? — Ha, boʻladi.</p>
  <p class="pe-ex__why">Birinchisi — <b>soʻrov</b> (men senga aytyapman), ikkinchisi — <b>ruxsat soʻrash</b> (men sendan soʻrayapman). Yoʻnalish qarama-qarshi.</p>
</div>

<h3>7. どうぞ — kichkina, lekin kerakli soʻz</h3>

<p>Ruxsat berishning eng qisqa yoʻli — <b>どうぞ</b>. U «marhamat»,
«bemalol», «oling» degan maʼnolarni bir oʻzi bajaradi va gapsiz ham
ishlaydi: eshikni ochib turib ham, choy uzatib turib ham どうぞ deyiladi.</p>

<p>Uning juftligi — <b>ありがとうございます</b>. Yaponiyada どうぞ va
ありがとう bir-birini deyarli avtomat chaqiradi: kimdir どうぞ desa, javob
albatta ありがとうございます boʻladi. Ikkalasini birga yodlang — ular bitta
juftlik va yolgʻiz deyarli uchramaydi.</p>

<p>Shu ikki soʻz bilan siz allaqachon butun bir muomalani yaponcha olib
chiqa olasiz: soʻrash, ruxsat berish va minnatdorchilik.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>待<rt>ま</rt></ruby>ちてください</p>
  <p class="pe-fix__good">✓ <ruby>待<rt>ま</rt></ruby><b>って</b>ください — ください ます oʻzagiga emas, <b>て-shakliga</b> qoʻshiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>座<rt>すわ</rt></ruby>ってもいいますか</p>
  <p class="pe-fix__good">✓ <ruby>座<rt>すわ</rt></ruby>っても<b>いいです</b>か — いい sifat, feʼl emas: います emas, <b>です</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>開<rt>あ</rt></ruby>けてもいいですか — «Oching!» maʼnosida</p>
  <p class="pe-fix__good">✓ <ruby>開<rt>あ</rt></ruby>けて<b>ください</b> — «Oching». もいいですか esa <b>oʻzingizga</b> ruxsat soʻraydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>待<rt>ま</rt></ruby>つ dan «kuting» ni yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>待<rt>ま</rt></ruby>ってください</b> — て-shakli + ください.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. «Oʻtirsam boʻladimi?» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>座<rt>すわ</rt></ruby>ってもいいですか。</b></p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «すみません、ちょっと…» nima maʼnoni beradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Muloyim rad javobi.</b> Gap ataylab tugatilmaydi — yaponchada «yoʻq» koʻpincha aytilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. てください ni kimga ishlatmaslik kerak?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Begona kattalarga xizmat soʻraganda.</b> U muloyim, lekin baribir <b>koʻrsatma</b>: oʻqituvchi, shifokor, doʻkonchi shunday gapiradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>見<rt>み</rt></ruby>せてください va <ruby>見<rt>み</rt></ruby>せてもいいですか — farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisi — <b>sen koʻrsat</b>. Ikkinchisi — <b>men koʻrsatsam boʻladimi</b>. Yoʻnalish qarama-qarshi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜てください</b> — iltimos, qiling</li>
  <li><b>〜てもいいですか</b> — qilsam boʻladimi?</li>
  <li><b>どうぞ</b> — marhamat, bemalol</li>
  <li><b>ちょっと…</b> — muloyim rad javobi</li>
  <li><b><ruby>見<rt>み</rt></ruby>せる</b> — koʻrsatmoq (II guruh)</li>
  <li><b><ruby>開<rt>あ</rt></ruby>ける</b> — ochmoq (II guruh)</li>
  <li><b><ruby>閉<rt>し</rt></ruby>める</b> — yopmoq (II guruh)</li>
  <li><b><ruby>座<rt>すわ</rt></ruby>る</b> — oʻtirmoq (I guruh)</li>
  <li><b><ruby>窓<rt>まど</rt></ruby></b> — deraza</li>
  <li><b>もう<ruby>一度<rt>いちど</rt></ruby></b> — yana bir marta</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>て + ください</b> — «qiling». Muloyim, lekin koʻrsatma.</li>
    <li><b>て + もいいですか</b> — «qilsam boʻladimi». Yoʻnalish teskari.</li>
    <li>Rad javobi <b>tugatilmaydi</b>: «すみません、ちょっと…».</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-33: 〜てはいけません va 〜なければなりません — taqiq va majburiyat",
        "category": "japanese",
        "order": 33,
        "summary": (
            "«Mumkin emas» va «shart». Birinchisi て-shaklidan, ikkinchisi "
            "esa yangi oʻzakdan — ない-oʻzagidan — yasaladi; uni shu darsda "
            "kerak boʻlgani uchun kiritamiz."
        ),
        "stories": ["プールの きそく"],
        "content": """
<h2>PJ-33: 〜てはいけません va 〜なければなりません — taqiq va majburiyat</h2>

<p>Oʻtgan darsda ruxsat oldingiz: <ruby>座<rt>すわ</rt></ruby>ってもいいです —
«oʻtirsa boʻladi». Bugun tanganing ikkinchi tomoni: <b>boʻlmaydi</b> va
<b>shart</b>.</p>

<p>Bu ikki qolip har qanday qoidalar roʻyxatining asosi — maktab, basseyn,
kutubxona, muzey. Ular doim juft yuradi, shuning uchun birga oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Taqiqni aytasiz: 〜てはいけません</li>
    <li>ない-oʻzagini yasaysiz — uchala guruhda</li>
    <li>Majburiyatni aytasiz: 〜なければなりません</li>
    <li>Uchta qolipni bir jadvalda taqqoslaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ruxsat oʻqi — uchta nuqta</span>
  <span class="pe-chip pe-chip--o">てもいいです</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">てはいけません</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">なければなりません</span>
</div>

<h3>1. 〜てはいけません — «mumkin emas»</h3>

<p>Yasalishi oson: <b>て-shakli + はいけません</b>. Yangi oʻzak kerak emas.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>て-shakli</th><th>Taqiq</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem"><ruby>走<rt>はし</rt></ruby>って</td>
      <td class="pj-res"><ruby>走<rt>はし</rt></ruby>ってはいけません</td><td class="pj-uz">yugurish mumkin emas</td></tr>
  <tr><td class="pj-stem"><ruby>入<rt>はい</rt></ruby>って</td>
      <td class="pj-res"><ruby>入<rt>はい</rt></ruby>ってはいけません</td><td class="pj-uz">kirish mumkin emas</td></tr>
  <tr><td class="pj-stem"><ruby>使<rt>つか</rt></ruby>って</td>
      <td class="pj-res"><ruby>使<rt>つか</rt></ruby>ってはいけません</td><td class="pj-uz">ishlatish mumkin emas</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>図書館<rt>としょかん</rt></ruby>で<ruby>話<rt>はな</rt></ruby>してはいけません。</p>
  <p class="pe-ex__rom">toshokan de hanashite wa ikemasen</p>
  <p class="pe-ex__uz">Kutubxonada gaplashish mumkin emas.</p>
  <p class="pe-ex__why">Bu — qatʼiy taqiq: qoida, belgi, ustozning gapi. Doʻstingizga «qilma» deyish uchun boshqa, yumshoqroq shakl ishlatiladi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>は bu yerda oʻsha tanish mavzu qoʻshimchasi.</b> Gapning
  soʻzma-soʻz maʼnosi «qilish <em>degani</em> — yaramaydi». Shuning uchun u
  <b>[wa]</b> deb oʻqiladi, <b>[ha]</b> emas — PJ-14 dagi qoida bu yerda ham
  ishlaydi.</p>
</div>

<h3>2. Yangi oʻzak: ない-oʻzagi</h3>

<p>Ikkinchi qolip uchun bizga <b>boshqa oʻzak</b> kerak. Uni toʻliq PJ-34 da
koʻramiz; bugun faqat <em>yasalishini</em> olamiz, chunki usiz
«shart» degan gapni tuza olmaymiz.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Guruh</th><th>Qoida</th><th>Misol</th><th>ない-shakli</th></tr>
  <tr><td class="pj-end">I</td><td class="pj-uz">う qatori → <b>あ</b> qatori + ない</td>
      <td><ruby>行<rt>い</rt></ruby>く</td><td class="pj-res"><ruby>行<rt>い</rt></ruby>かない</td></tr>
  <tr><td class="pj-end">II</td><td class="pj-uz">る tushadi + ない</td>
      <td><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-res"><ruby>食<rt>た</rt></ruby>べない</td></tr>
  <tr><td class="pj-end">III</td><td class="pj-uz">yodlanadi</td>
      <td>する · <ruby>来<rt>く</rt></ruby>る</td><td class="pj-res">しない · <ruby>来<rt>こ</rt></ruby>ない</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Ikki narsaga diqqat.</b> Birinchisi: I guruhda oxirgi tovush
  <b>あ</b> qatoriga tushadi — <ruby>読<rt>よ</rt></ruby>む →
  <ruby>読<rt>よ</rt></ruby><b>ま</b>ない. Ikkinchisi:
  <b>う bilan tugagan feʼl «あ» emas, «わ» oladi</b> —
  <ruby>買<rt>か</rt></ruby>う → <ruby>買<rt>か</rt></ruby><b>わ</b>ない,
  «かあない» emas. Va <ruby>来<rt>く</rt></ruby>る yana oʻqilishini
  oʻzgartiradi: <ruby>来<rt>こ</rt></ruby>ない.</p>
</div>

<h3>3. 〜なければなりません — «shart»</h3>

<p>ない-shaklini oling, oxirgi <b>い</b> ni olib tashlang, oʻrniga
<b>ければなりません</b> qoʻying.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>ない-shakli</th><th>Oʻzak</th><th>Majburiyat</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>行<rt>い</rt></ruby>かない</td><td class="pj-stem"><ruby>行<rt>い</rt></ruby>かな</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かなければなりません</td><td class="pj-uz">borish shart</td></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べない</td><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べな</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べなければなりません</td><td class="pj-uz">yeyish shart</td></tr>
  <tr><td>しない</td><td class="pj-stem">しな</td>
      <td class="pj-res">しなければなりません</td><td class="pj-uz">qilish shart</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu qolip ikki marta inkor qiladi — va oʻzbekcha ham xuddi
  shunday qila oladi.</b> Soʻzma-soʻz maʼnosi «qil<em>ma</em>sa
  boʻl<em>maydi</em>». Oʻzbekchada ham «bormasam boʻlmaydi» degan tuzilma
  bor va u aynan «borishim shart» degani. Shuning uchun bu uzun qolipni
  yodlashning eng oson yoʻli — uni <b>«…masa boʻlmaydi»</b> deb tarjima
  qilish, «shart» deb emas. Uzunligi ham shundan: yaponcha majburiyatni
  toʻgʻridan-toʻgʻri emas, ikki inkor orqali aytadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>明日<rt>あした</rt></ruby><ruby>八時<rt>はちじ</rt></ruby>に<ruby>来<rt>こ</rt></ruby>なければなりません。</p>
  <p class="pe-ex__rom">ashita hachiji ni konakereba narimasen</p>
  <p class="pe-ex__uz">Ertaga soat sakkizda kelish shart.</p>
  <p class="pe-ex__why"><ruby>来<rt>く</rt></ruby>る ning ない-shakli — <ruby>来<rt>こ</rt></ruby>ない. Yaʼni bu kanji endi <b>toʻrt xil</b> oʻqiladi: く, き, こ va yana き (て-shaklida).</p>
</div>

<h3>4. Uchta qolip bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Maʼno</th><th>Qolip</th><th>Misol</th></tr>
  <tr><td class="pj-uz">Ruxsat bor</td><td class="pj-end">て + もいいです</td>
      <td class="pj-res"><ruby>使<rt>つか</rt></ruby>ってもいいです</td></tr>
  <tr><td class="pj-uz">Mumkin emas</td><td class="pj-end">て + はいけません</td>
      <td class="pj-res"><ruby>使<rt>つか</rt></ruby>ってはいけません</td></tr>
  <tr><td class="pj-uz">Shart</td><td class="pj-end">ない → なければなりません</td>
      <td class="pj-res"><ruby>使<rt>つか</rt></ruby>わなければなりません</td></tr>
  <tr><td class="pj-uz">Shart emas</td><td class="pj-end">ない → なくてもいいです</td>
      <td class="pj-res"><ruby>使<rt>つか</rt></ruby>わなくてもいいです</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Birinchi ikkitasi て-shaklidan, uchinchisi ない-shaklidan.</b>
  Mana shuning uchun PJ-27 dagi guruhlar shu qadar muhim edi: har bir yangi
  qolip oʻsha uchta guruhning biriga qarab yasaladi, va oʻzaklar
  koʻpayib boradi.</p>
</div>

<h3>5. Toʻrtinchi burchak: 〜なくてもいいです</h3>

<p>Jadvalda bitta katak boʻsh qoldi. «Shart emas» degani —
<b>qilmasa ham boʻladi</b>. U ham oʻsha ない-oʻzagidan yasaladi, va bu safar
oxirgi <b>い</b> oʻrniga <b>くてもいいです</b> qoʻyiladi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>ない-shakli</th><th>«Shart emas»</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>行<rt>い</rt></ruby>かない</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かなくてもいいです</td><td class="pj-uz">borish shart emas</td></tr>
  <tr><td><ruby>使<rt>つか</rt></ruby>わない</td>
      <td class="pj-res"><ruby>使<rt>つか</rt></ruby>わなくてもいいです</td><td class="pj-uz">ishlatish shart emas</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>い → くない → くて — bu tanish yoʻl.</b> PJ-25 da い-sifatning
  oxirgi い <b>く</b> ga aylanganini koʻrgansiz
  (<ruby>安<rt>やす</rt></ruby>い → <ruby>安<rt>やす</rt></ruby>く). ない
  ham い-sifat, shuning uchun u ham xuddi shunday tutadi. Yaʼni bu yangi
  qoida emas — eski qoidaning yangi joyda ishlashi.</p>
</div>

<p>Endi toʻrtala burchak ham bor: ruxsat bor, mumkin emas, shart, shart emas.
Bu toʻrtlik bilan har qanday qoidalar roʻyxatini yaponcha oʻqiy va yoza
olasiz.</p>

<h3>6. Belgilarda qanday yoziladi</h3>

<p>Haqiqiy taqiq belgilarida uzun shakl kamdan-kam uchraydi — u yerda qisqa,
kesik yozuv turadi: <b><ruby>立入禁止<rt>たちいりきんし</rt></ruby></b>
(«kirish taqiqlanadi»), <b><ruby>禁煙<rt>きんえん</rt></ruby></b>
(«chekish taqiqlanadi»). Ularni <em>oʻqiy bilish</em> kifoya; gapirganda
esa siz bugungi qolipni ishlatasiz.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>買<rt>か</rt></ruby>あない</p>
  <p class="pe-fix__good">✓ <ruby>買<rt>か</rt></ruby><b>わ</b>ない — う bilan tugagan feʼl <b>わ</b> oladi. Yagona, lekin doim uchraydigan istisno.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>話<rt>はな</rt></ruby>してはいけます</p>
  <p class="pe-fix__good">✓ <ruby>話<rt>はな</rt></ruby>しては<b>いけません</b> — bu qolip faqat inkor shaklda yashaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>くなければなりません</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby><b>かな</b>ければなりません — lugʻat shaklidan emas, <b>ない-shaklidan</b>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Kutubxonada gaplashish mumkin emas» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>図書館<rt>としょかん</rt></ruby>で<ruby>話<rt>はな</rt></ruby>してはいけません。</b></p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>買<rt>か</rt></ruby>う ning ない-shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>買<rt>か</rt></ruby>わない</b> — う bilan tugagan feʼl あ emas, <b>わ</b> oladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>来<rt>く</rt></ruby>る ning ない-shakli qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>来<rt>こ</rt></ruby>ない</b> — oʻqilishi <b>こ</b> ga oʻzgaradi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 〜なければなりません ni soʻzma-soʻz qanday tarjima qilish oson?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>«…masa boʻlmaydi.»</b> Ikki inkor — xuddi oʻzbekchadagi kabi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Uchta qolipdan qaysi biri ない-shaklidan yasaladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>〜なければなりません.</b> Qolgan ikkitasi — てもいいです va てはいけません — <b>て-shaklidan</b>.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜てはいけません</b> — qilish mumkin emas</li>
  <li><b>〜なければなりません</b> — qilish shart</li>
  <li><b>〜なくてもいいです</b> — qilish shart emas</li>
  <li><b>ない-shakli</b> — inkor oʻzagi</li>
  <li><b><ruby>使<rt>つか</rt></ruby>う</b> — ishlatmoq (I guruh)</li>
  <li><b><ruby>立<rt>た</rt></ruby>つ</b> — turmoq (I guruh)</li>
  <li><b><ruby>規則<rt>きそく</rt></ruby></b> — qoida</li>
  <li><b><ruby>立入禁止<rt>たちいりきんし</rt></ruby></b> — kirish taqiqlanadi</li>
  <li><b><ruby>禁煙<rt>きんえん</rt></ruby></b> — chekish taqiqlanadi</li>
  <li><b><ruby>明日<rt>あした</rt></ruby></b> — ertaga</li>
  <li><b>プール</b> — basseyn</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>て + はいけません</b> — «mumkin emas». は bu yerda [wa].</li>
    <li><b>ない → なければなりません</b> — «shart», soʻzma-soʻz «…masa boʻlmaydi».</li>
    <li><ruby>買<rt>か</rt></ruby><b>わ</b>ない va <ruby>来<rt>こ</rt></ruby>ない — ない-shaklining ikkita tuzogʻi.</li>
  </ul>
</div>
""",
    },
]
