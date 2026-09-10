# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-34 … PJ-36: ikkinchi va uchinchi oʻzak.

PJ-34 ない-shaklini toʻliq beradi (PJ-33 undan faqat oʻzakni olgan edi),
PJ-35 た-shaklini — u て-shaklidan bir harf bilan chiqadi — va PJ-36 oʻsha
た dan yasaladigan 〜たり qolipini.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_34_36.py --author=prime
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
        "title": "PJ-34: ない-shakli va 〜ないでください",
        "category": "japanese",
        "order": 34,
        "summary": (
            "Oʻtgan darsda ない-oʻzagini qarzga olgan edik — bugun uni toʻliq "
            "olamiz: uchala guruh, uchta tuzoq va «qilmang» degan gap."
        ),
        "stories": ["としょかんで まもる ことと まもらない こと"],
        "content": """
<h2>PJ-34: ない-shakli va 〜ないでください</h2>

<p>Oʻtgan darsda bir narsani <em>qarzga</em> oldik: 〜なければなりません
qolipini tuzish uchun ない-oʻzagi kerak edi, va biz uni shoshib olib
qoʻydik.</p>

<p>Bugun qarzni uzamiz. ない-shakli — feʼlning <b>ikkinchi asosiy oʻzagi</b>;
て-shakli qanchalik muhim boʻlsa, bu ham shunchalik. Undan inkorga oid
deyarli hamma narsa yasaladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>ない-shaklini uchala guruhda puxta yasaysiz</li>
    <li>Uchta tuzoqni bilib olasiz — う, <ruby>来<rt>く</rt></ruby>る va ある</li>
    <li>«Qilmang» degan gapni tuzasiz: 〜ないでください</li>
    <li>ない dan yasaladigan uchta qolipni bir joyga yigʻasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uchinchi oʻzak</span>
  <span class="pe-chip pe-chip--s">lugʻat</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">て</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">ない</span>
</div>

<h3>1. Yasalishi — uchala guruh</h3>

<div class="pj-group">
  <div class="pj-group__c">
    <p class="pj-group__h">I — <ruby>五段<rt>ごだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>読<rt>よ</rt></ruby>む → <ruby>読<rt>よ</rt></ruby>まない</p>
    <p>Oxirgi tovush <b>あ</b> qatoriga tushadi.</p>
  </div>
  <div class="pj-group__c pj-group__c--2">
    <p class="pj-group__h">II — <ruby>一段<rt>いちだん</rt></ruby></p>
    <p class="pj-group__ex"><ruby>食<rt>た</rt></ruby>べる → <ruby>食<rt>た</rt></ruby>べない</p>
    <p>る tushadi, ない qoʻyiladi.</p>
  </div>
  <div class="pj-group__c pj-group__c--3">
    <p class="pj-group__h">III — <ruby>不規則<rt>ふきそく</rt></ruby></p>
    <p class="pj-group__ex">しない · <ruby>来<rt>こ</rt></ruby>ない</p>
    <p>Yodlanadi.</p>
  </div>
</div>

<p>I guruhda oxirgi tovush <b>う qatoridan あ qatoriga</b> tushadi — yaʼni
ます shaklidagi harakatning teskarisi: u yerda い qatoriga tushgan edi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat</th><th>ます (い qatori)</th><th>ない (あ qatori)</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-uz"><ruby>読<rt>よ</rt></ruby>みます</td>
      <td class="pj-res"><ruby>読<rt>よ</rt></ruby>まない</td><td class="pj-uz">oʻqimaslik</td></tr>
  <tr><td><ruby>書<rt>か</rt></ruby>く</td><td class="pj-uz"><ruby>書<rt>か</rt></ruby>きます</td>
      <td class="pj-res"><ruby>書<rt>か</rt></ruby>かない</td><td class="pj-uz">yozmaslik</td></tr>
  <tr><td><ruby>話<rt>はな</rt></ruby>す</td><td class="pj-uz"><ruby>話<rt>はな</rt></ruby>します</td>
      <td class="pj-res"><ruby>話<rt>はな</rt></ruby>さない</td><td class="pj-uz">gapirmaslik</td></tr>
  <tr><td><ruby>待<rt>ま</rt></ruby>つ</td><td class="pj-uz"><ruby>待<rt>ま</rt></ruby>ちます</td>
      <td class="pj-res"><ruby>待<rt>ま</rt></ruby>たない</td><td class="pj-uz">kutmaslik</td></tr>
  <tr><td><ruby>入<rt>はい</rt></ruby>る</td><td class="pj-uz"><ruby>入<rt>はい</rt></ruby>ります</td>
      <td class="pj-res"><ruby>入<rt>はい</rt></ruby>らない</td><td class="pj-uz">kirmaslik</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Bitta feʼl, uchta oʻzak.</b> <ruby>読<rt>よ</rt></ruby>む dan
  <ruby>読<rt>よ</rt></ruby>み (い qatori — ます uchun),
  <ruby>読<rt>よ</rt></ruby>ん<b>で</b> (て-shakli) va
  <ruby>読<rt>よ</rt></ruby>ま (あ qatori — ない uchun) chiqadi. Keyingi
  darslarning har biri shu uchtadan biriga tayanadi, shuning uchun ularni
  <b>uchtasini birga</b> yodlagan maʼqul.</p>
</div>

<h3>2. Uchta tuzoq</h3>

<p>Ikkitasini oʻtgan darsda koʻrgan edingiz, uchinchisi bugun qoʻshiladi —
va u eng kutilmagani.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>Kutilgan</th><th>Haqiqiy</th><th>Nega</th></tr>
  <tr><td><ruby>買<rt>か</rt></ruby>う</td><td class="pj-uz"><ruby>買<rt>か</rt></ruby>あない</td>
      <td class="pj-res"><ruby>買<rt>か</rt></ruby>わない</td><td class="pj-uz">う → <b>わ</b>, あ emas</td></tr>
  <tr><td><ruby>来<rt>く</rt></ruby>る</td><td class="pj-uz"><ruby>来<rt>く</rt></ruby>ない</td>
      <td class="pj-res"><ruby>来<rt>こ</rt></ruby>ない</td><td class="pj-uz">oʻqilishi oʻzgaradi</td></tr>
  <tr><td>ある</td><td class="pj-uz">あらない</td>
      <td class="pj-res"><b>ない</b></td><td class="pj-uz">feʼl butunlay yoʻqoladi</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>ある ning inkori — shunchaki ない.</b> Yaʼni «yoʻq» degan soʻzning
  oʻzi. Aslida siz buni PJ-16 dan beri bilasiz:
  <ruby>本<rt>ほん</rt></ruby>が<b>ありません</b> — «kitob yoʻq». Uning
  oddiy shakli — <b>ない</b>. «あらない» degan soʻz yoʻq, va bu yagona
  feʼl bunday tutadi.</p>
</div>

<h3>3. 〜ないでください — «qilmang»</h3>

<p>Mana bugungi yangi qolip. ない-shakliga <b>でください</b> qoʻshiladi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">QILING</p>
    <p><ruby>入<rt>はい</rt></ruby>って<b>ください</b></p>
    <p>て-shakli + ください</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">QILMANG</p>
    <p><ruby>入<rt>はい</rt></ruby>らない<b>でください</b></p>
    <p>ない-shakli + でください</p></div>
</div>

<div class="pe-call pe-tip">
  <p><b>Nega で?</b> Chunki ない ham て-shaklga oʻxshash bir ulanish
  yasaydi — <b>ないで</b> — va oʻsha ulanishga ください qoʻshiladi.
  Yaʼni tuzilish ijobiy tomondagining aynan oʻzi: <em>ulagich +
  ください</em>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">ここで<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>らないでください。</p>
  <p class="pe-ex__rom">koko de shashin o toranai de kudasai</p>
  <p class="pe-ex__uz">Bu yerda rasmga olmang.</p>
  <p class="pe-ex__why"><ruby>撮<rt>と</rt></ruby>る → <ruby>撮<rt>と</rt></ruby>らない → <ruby>撮<rt>と</rt></ruby>らないでください. Uch qadam, har biri tanish.</p>
</div>

<h3>4. 〜ないでください va 〜てはいけません — farqi</h3>

<p>Ikkalasi ham «qilmang» degani, lekin ular <em>bir xil emas</em>, va farqi
grammatikada emas — <b>kimning gapi ekanida</b>.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">〜ないでください</p>
    <p class="pj-big">iltimos</p>
    <p>Shaxsiy iltimos. «Iltimos, qilmang.» Doʻstga, sinfdoshga, mehmonga.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">〜てはいけません</p>
    <p class="pj-big">qoida</p>
    <p>Qoida. «Mumkin emas.» Belgi, nizom, ustozning qatʼiy gapi.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham shu ikkilik bor.</b> «Iltimos, eshikni yopmang» va
  «Eshikni yopish mumkin emas» — birinchisi <em>menga</em> shunday qulay,
  ikkinchisi <em>qoida</em> shunday. Yaponchada bu farq yanada aniqroq
  ajratilgan, chunki kim kimga gapirayotgani yapon tilida doim muhim.</p>
</div>

<h3>5. 〜ないで — «…masdan»</h3>

<p>ないで oʻzi ham ishlaydi — ください siz. U ikki ishni ulaydi va
«birinchisini <b>qilmasdan</b>, ikkinchisini qildim» degan maʼnoni beradi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>朝<rt>あさ</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べないで、<ruby>学校<rt>がっこう</rt></ruby>へ<ruby>行<rt>い</rt></ruby>きました。</p>
  <p class="pe-ex__rom">asagohan o tabenai de, gakkō e ikimashita</p>
  <p class="pe-ex__uz">Nonushta qilmasdan, maktabga bordim.</p>
  <p class="pe-ex__why">て-shakli «qilib» degan boʻlsa, ないで «qilmasdan» degani. Bir juftlik: ijobiy va inkor ulagich.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham juftlik toʻliq mos keladi.</b> «Yeb, bordim» —
  yaponchada <ruby>食<rt>た</rt></ruby>べて; «ye<b>masdan</b>, bordim» —
  <ruby>食<rt>た</rt></ruby>べないで. Yaʼni oʻzbekchadagi <b>-ib</b> va
  <b>-masdan</b> juftligi yapon tilidagi <b>て</b> va <b>ないで</b>
  juftligining oʻzi. Bu — kursdagi eng toza mosliklardan biri, undan
  foydalaning.</p>
</div>

<h3>6. ない dan nima yasaladi — hammasi bir joyda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pj-end">〜ないで</td><td class="pj-uz">qilmasdan</td>
      <td class="pj-res"><ruby>走<rt>はし</rt></ruby>らないで</td></tr>
  <tr><td class="pj-end">〜ないでください</td><td class="pj-uz">qilmang (iltimos)</td>
      <td class="pj-res"><ruby>走<rt>はし</rt></ruby>らないでください</td></tr>
  <tr><td class="pj-end">〜なければなりません</td><td class="pj-uz">qilish shart</td>
      <td class="pj-res"><ruby>走<rt>はし</rt></ruby>らなければなりません</td></tr>
  <tr><td class="pj-end">〜なくてもいいです</td><td class="pj-uz">qilish shart emas</td>
      <td class="pj-res"><ruby>走<rt>はし</rt></ruby>らなくてもいいです</td></tr>
</table></div>

<p>Uchalasi ham bitta oʻzakdan. Shuning uchun ない-shaklini yasay bilish —
uchta qolipni birdan qoʻlga kiritish degani.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ あらない</p>
  <p class="pe-fix__good">✓ <b>ない</b> — ある ning inkori feʼlsiz qoladi. «Yoʻq» degan soʻzning oʻzi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>入<rt>はい</rt></ruby>らないください</p>
  <p class="pe-fix__good">✓ <ruby>入<rt>はい</rt></ruby>らない<b>で</b>ください — ない bilan ください orasida <b>で</b> turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>話<rt>はな</rt></ruby>しない</p>
  <p class="pe-fix__good">✓ <ruby>話<rt>はな</rt></ruby><b>さ</b>ない — ない <b>あ</b> qatorini oladi, ます esa い qatorini. Ikkalasini aralashtirmang.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>書<rt>か</rt></ruby>く ning ない-shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>書<rt>か</rt></ruby>かない</b> — く あ qatoriga tushadi: か.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. ある ning ない-shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ない</b>. «あらない» degan soʻz yoʻq — feʼl butunlay yoʻqoladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Bu yerda gaplashmang» ni iltimos shaklida ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ここで<ruby>話<rt>はな</rt></ruby>さないでください。</b></p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 〜ないでください va 〜てはいけません farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisi — <b>shaxsiy iltimos</b>, ikkinchisi — <b>qoida</b>. Grammatika emas, kimning gapi ekani hal qiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. ない oʻzagidan nechta qolip yasaladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Toʻrtta:</b> 〜ないで, 〜ないでください, 〜なければなりません, 〜なくてもいいです.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ない-shakli</b> — inkor oʻzagi</li>
  <li><b>〜ないでください</b> — qilmang (iltimos)</li>
  <li><b>〜ないで</b> — qilmasdan</li>
  <li><b>ない</b> — ある ning inkori</li>
  <li><b><ruby>来<rt>こ</rt></ruby>ない</b> — kelmaslik</li>
  <li><b><ruby>買<rt>か</rt></ruby>わない</b> — sotib olmaslik</li>
  <li><b><ruby>忘<rt>わす</rt></ruby>れる</b> — unutmoq (II guruh)</li>
  <li><b><ruby>守<rt>まも</rt></ruby>る</b> — rioya qilmoq (I guruh)</li>
  <li><b><ruby>捨<rt>す</rt></ruby>てる</b> — tashlamoq (II guruh)</li>
  <li><b>ここで</b> — bu yerda</li>
  <li><b><ruby>静<rt>しず</rt></ruby>かに</b> — jimgina</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>I guruh <b>あ qatorini</b> oladi — ます dagi い qatorining teskarisi.</li>
    <li>Uchta tuzoq: <ruby>買<rt>か</rt></ruby><b>わ</b>ない · <ruby>来<rt>こ</rt></ruby>ない · ある → <b>ない</b>.</li>
    <li><b>〜ないでください</b> iltimos, <b>〜てはいけません</b> qoida.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-35: た-shakli va 〜たことがあります — tajriba",
        "category": "japanese",
        "order": 35,
        "summary": (
            "Kursdagi eng arzon shakl: て-shaklidagi bitta harfni "
            "almashtirsangiz, た chiqadi. Undan «hech qachon qilganmisiz?» "
            "degan savol yasaladi."
        ),
        "stories": ["にほんへ いった ことが ありますか"],
        "content": """
<h2>PJ-35: た-shakli va 〜たことがあります — tajriba</h2>

<p>Yaxshi xabar bilan boshlaymiz: bugungi shakl uchun <b>hech narsa
oʻrganish shart emas</b>. Siz uni allaqachon bilasiz.</p>

<p>た-shakli — bu て-shaklining oʻzi, faqat oxirgi harf almashadi:
<b>て → た</b>, <b>で → だ</b>. Xolos. Beshta qoida, uch guruh, tuzoqlar —
hammasi て-shaklida bir marta hal qilingan edi, va た ularni tekin
meros oladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>て-shaklidan た-shaklini bir harfda yasaysiz</li>
    <li>«Hech qachon qilganman» degan gapni tuzasiz</li>
    <li>Uni oddiy oʻtgan zamondan ajratasiz</li>
    <li>«Hech qachon qilmaganman» ni aytasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta harf</span>
  <span class="pe-chip pe-chip--v"><ruby>読<rt>よ</rt></ruby>ん<b>で</b></span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o"><ruby>読<rt>よ</rt></ruby>ん<b>だ</b></span>
</div>

<h3>1. て → た, で → だ</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat</th><th>て-shakli</th><th>た-shakli</th><th>Guruh</th></tr>
  <tr><td><ruby>買<rt>か</rt></ruby>う</td><td class="pj-stem"><ruby>買<rt>か</rt></ruby>って</td>
      <td class="pj-res"><ruby>買<rt>か</rt></ruby>った</td><td class="pj-uz">I</td></tr>
  <tr><td><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-stem"><ruby>読<rt>よ</rt></ruby>んで</td>
      <td class="pj-res"><ruby>読<rt>よ</rt></ruby>んだ</td><td class="pj-uz">I</td></tr>
  <tr><td><ruby>書<rt>か</rt></ruby>く</td><td class="pj-stem"><ruby>書<rt>か</rt></ruby>いて</td>
      <td class="pj-res"><ruby>書<rt>か</rt></ruby>いた</td><td class="pj-uz">I</td></tr>
  <tr><td><ruby>泳<rt>およ</rt></ruby>ぐ</td><td class="pj-stem"><ruby>泳<rt>およ</rt></ruby>いで</td>
      <td class="pj-res"><ruby>泳<rt>およ</rt></ruby>いだ</td><td class="pj-uz">I</td></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べて</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べた</td><td class="pj-uz">II</td></tr>
  <tr><td>する</td><td class="pj-stem">して</td><td class="pj-res">した</td><td class="pj-uz">III</td></tr>
  <tr><td><ruby>行<rt>い</rt></ruby>く</td><td class="pj-stem"><ruby>行<rt>い</rt></ruby>って</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>った</td><td class="pj-uz">istisno</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Istisno ham meros boʻlib oʻtadi.</b> <ruby>行<rt>い</rt></ruby>く
  ning て-shakli <ruby>行<rt>い</rt></ruby>って edi, demak た-shakli
  <ruby>行<rt>い</rt></ruby><b>った</b> — «いいた» emas. Yaʼni siz PJ-30 da
  bir marta yodlagan narsani ikkinchi marta yodlashingiz shart emas.</p>
</div>

<h3>2. Nima uchun kerak</h3>

<p>た-shakli oʻzi — <b>oddiy shakldagi oʻtgan zamon</b>
(<ruby>読<rt>よ</rt></ruby>んだ = «oʻqidim», muloyimsiz). Uni gap oxirida
ishlatishni PJ-45 da koʻramiz; bugun bizga u <em>oʻzak</em> sifatida
kerak — undan bir necha muhim qolip yasaladi, va birinchisi bugun.</p>

<p>Nega bu oʻzak alohida oʻrgatiladi? Chunki oldinda uni talab qiladigan
qoliplar koʻp: bugungi tajriba qolipi, keyingi darsdagi 〜たり, shart
gaplaridagi 〜たら, ish tartibini bildiradigan 〜たあとで. Har birida
oʻsha bir shakl turadi — va u sizda allaqachon bor.</p>

<h3>3. 〜たことがあります — «qilganman»</h3>

<p>Bu qolip <b>tajriba</b> haqida: hayotingizda hech qachon shunday
boʻlganmi. Qachon boʻlgani, necha marta boʻlgani muhim emas — faqat
<em>boʻlgan-boʻlmagani</em> muhim.</p>

<div class="pj-joshi">
  <span class="pj-joshi__v"><ruby>行<rt>い</rt></ruby>った</span>
  <span class="pj-joshi__n">こと</span>
  <span class="pj-joshi__p">が<small>EGA</small></span>
  <span class="pj-joshi__v">あります</span>
  <span class="pj-joshi__uz">Borganman. — soʻzma-soʻz: «borgan ish bor».</span>
</div>

<div class="pe-call pe-tip">
  <p><b>こと — «ish, narsa» degan ot.</b> Yaʼni gap soʻzma-soʻz «borgan
  <em>ish</em> bor» degani, va shuning uchun oxirida ある feʼli turadi
  hamda こと が oladi. Yangi grammatika yoʻq: PJ-16 dagi «なにか
  <b>あります</b>» qolipining oʻzi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>私<rt>わたし</rt></ruby>は<ruby>日本<rt>にほん</rt></ruby>へ<ruby>行<rt>い</rt></ruby>ったことがあります。</p>
  <p class="pe-ex__rom">watashi wa nihon e itta koto ga arimasu</p>
  <p class="pe-ex__uz">Men Yaponiyaga borganman.</p>
  <p class="pe-ex__why">Qachon borgani aytilmayapti — faqat <b>tajriba bor</b>ligi aytilyapti. Aniq vaqt qoʻshilsa, bu qolip ishlatilmaydi.</p>
</div>

<h3>4. Inkori: «hech qachon qilmaganman»</h3>

<p>ある ning inkori esdami? PJ-34 da koʻrgan edingiz. Bu yerda muloyim
shakli kerak: <b>ありません</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Shakl</th><th>Yaponcha</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">bor</td><td class="pj-res"><ruby>食<rt>た</rt></ruby>べたことがあります</td>
      <td class="pj-uz">yeb koʻrganman</td></tr>
  <tr><td class="pj-stem">yoʻq</td><td class="pj-res"><ruby>食<rt>た</rt></ruby>べたことがありません</td>
      <td class="pj-uz">hech qachon yeb koʻrmaganman</td></tr>
  <tr><td class="pj-stem">savol</td><td class="pj-res"><ruby>食<rt>た</rt></ruby>べたことがありますか</td>
      <td class="pj-uz">yeb koʻrganmisiz?</td></tr>
</table></div>

<h3>5. Oddiy oʻtgan zamondan farqi</h3>

<p>Mana darsning eng muhim ajratishi. Ikkalasi ham «qildim» deb tarjima
qilinadi, lekin ular boshqa narsa haqida gapiradi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">TAJRIBA</p>
    <p><ruby>行<rt>い</rt></ruby>ったことがあります</p>
    <p>Hayotimda boʻlgan. Qachonligi muhim emas.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">OʻTGAN ZAMON</p>
    <p><ruby>行<rt>い</rt></ruby>きました</p>
    <p>Aniq bir marta boʻlgan ish. Kecha, oʻtgan hafta.</p></div>
</div>

<div class="pe-call pe-warn">
  <p><b>Aniq vaqt bilan bu qolip ishlatilmaydi.</b>
  «<ruby>昨日<rt>きのう</rt></ruby><ruby>行<rt>い</rt></ruby>ったことが
  あります» notoʻgʻri: kecha boʻlgan ish tajriba emas, u shunchaki
  oʻtgan zamon — <ruby>昨日<rt>きのう</rt></ruby><ruby>行<rt>い</rt></ruby>きました.
  Tajriba deb aytish uchun ish <b>uzoqroq oʻtmishda</b> va
  <b>takrorlanishi mumkin</b> boʻlishi kerak.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu farqni «-ganman» koʻrsatadi.</b> «Yaponiyaga
  bor<b>ganman</b>» — tajriba; «Kecha bor<b>dim</b>» — aniq voqea. Yapon
  tilidagi ajratish aynan shu. Shuning uchun 〜たことがあります ni
  «<b>-gan</b>man» deb tarjima qiling, «-dim» deb emas — shunda aniq
  vaqt qoʻshish istagi ham oʻz-oʻzidan yoʻqoladi.</p>
</div>

<h3>6. Suhbatda — eng koʻp ishlatiladigan joyi</h3>

<p>Bu qolip yangi tanishuvda deyarli har doim chiqadi. Savol berish oson,
javob berish esa undan ham oson.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">— <ruby>富士山<rt>ふじさん</rt></ruby>に<ruby>登<rt>のぼ</rt></ruby>ったことがありますか。<br>— いいえ、まだありません。ラノさんは？</p>
  <p class="pe-ex__rom">fujisan ni nobotta koto ga arimasu ka / iie, mada arimasen</p>
  <p class="pe-ex__uz">— Fuji togʻiga chiqqanmisiz? — Yoʻq, hali yoʻq. Siz-chi, Rano?</p>
  <p class="pe-ex__why">Javobda butun qolipni takrorlash shart emas — <b>ありません</b> ning oʻzi kifoya. <b>まだ</b> «hali» degani va u «lekin qilishim mumkin» degan ohang qoʻshadi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>まだありません va ありません farqi bor.</b> Yolgʻiz ありません —
  quruq «yoʻq». <b>まだ</b>ありません — «hali yoʻq», yaʼni eshik ochiq.
  Yaponlar deyarli doim ikkinchisini tanlaydi: bu muloyimroq eshitiladi
  va suhbatni davom ettiradi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>んて</p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby>ん<b>だ</b> — て-shakli で bilan tugagan boʻlsa, た-shakli <b>だ</b> boʻladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>昨日<rt>きのう</rt></ruby><ruby>行<rt>い</rt></ruby>ったことがあります</p>
  <p class="pe-fix__good">✓ <ruby>昨日<rt>きのう</rt></ruby><ruby>行<rt>い</rt></ruby>きました — aniq vaqt bilan tajriba qolipi ishlatilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>ったことをあります</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>ったこと<b>が</b>あります — こと bu yerda <b>ega</b>, toʻldiruvchi emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>泳<rt>およ</rt></ruby>ぐ ning た-shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>泳<rt>およ</rt></ruby>いだ</b> — て-shakli <ruby>泳<rt>およ</rt></ruby>いで, demak で → <b>だ</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>行<rt>い</rt></ruby>く ning た-shakli qanday?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>行<rt>い</rt></ruby>った</b> — istisno て-shaklidan meros boʻlib oʻtadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Sushi yeb koʻrganman» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>すしを<ruby>食<rt>た</rt></ruby>べたことがあります。</b></p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Nega «<ruby>昨日<rt>きのう</rt></ruby>…たことがあります» notoʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Bu qolip <b>tajriba</b> haqida, aniq voqea haqida emas. Aniq vaqt bilan oddiy oʻtgan zamon ishlatiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Hech qachon koʻrmaganman» ni ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>見<rt>み</rt></ruby>たことがありません。</b> ある ning muloyim inkori — ありません.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>た-shakli</b> — oddiy oʻtgan zamon oʻzagi</li>
  <li><b>〜たことがあります</b> — qilganman (tajriba)</li>
  <li><b>〜たことがありません</b> — hech qachon qilmaganman</li>
  <li><b>こと</b> — ish, narsa (mavhum ot)</li>
  <li><b><ruby>日本<rt>にほん</rt></ruby></b> — Yaponiya</li>
  <li><b>すし</b> — sushi</li>
  <li><b><ruby>富士山<rt>ふじさん</rt></ruby></b> — Fuji togʻi</li>
  <li><b><ruby>登<rt>のぼ</rt></ruby>る</b> — chiqmoq, koʻtarilmoq (I guruh)</li>
  <li><b><ruby>会<rt>あ</rt></ruby>う</b> — uchrashmoq (I guruh)</li>
  <li><b>まだ</b> — hali</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>て → た, で → だ</b>. Boshqa hech narsa oʻzgarmaydi.</li>
    <li><b>〜たことがあります</b> — «-ganman». こと が oladi, を emas.</li>
    <li>Aniq vaqt bor boʻlsa — bu qolip <b>emas</b>, oddiy oʻtgan zamon.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-36: 〜たり〜たりします — ishlarni sanash",
        "category": "japanese",
        "order": 36,
        "summary": (
            "«U ham qildim, bu ham» degan qolip. た-shaklidan yasaladi va "
            "roʻyxatning TUGALLANMAGANini bildiradi — て bilan ulashdan "
            "asosiy farqi shu."
        ),
        "stories": ["にちようびに なにを したり しますか"],
        "content": """
<h2>PJ-36: 〜たり〜たりします — ishlarni sanash</h2>

<p>«Yakshanba kuni nima qilasiz?» degan savolga javob berib koʻring. Hozircha
sizda ikki yoʻl bor: て bilan ulash
(<ruby>読<rt>よ</rt></ruby>んで、<ruby>寝<rt>ね</rt></ruby>ます) yoki
alohida gaplar.</p>

<p>Ikkalasi ham notoʻgʻri emas, lekin ikkalasi ham
<em>hammasini aytdim</em> degan taassurot qoldiradi. Yaponchada esa bunday
paytda boshqa qolip ishlatiladi — u «<b>masalan, shular</b>» degan maʼnoni
beradi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>た-shaklidan 〜たり yasaysiz</li>
    <li>Ikki-uch ishni misol tariqasida sanaysiz</li>
    <li>Zamonni oxirdagi します bilan boshqarasiz</li>
    <li>〜て bilan ulashdan farqini tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">た + り, ikki marta, keyin する</span>
  <span class="pe-chip pe-chip--v"><ruby>読<rt>よ</rt></ruby>んだり</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o"><ruby>寝<rt>ね</rt></ruby>たり</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">します</span>
</div>

<h3>1. Yasalishi</h3>

<p>た-shakliga <b>り</b> qoʻshasiz — xolos. Odatda ikkitasini sanaysiz, keyin
gapni <b>します</b> bilan yopasiz.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Lugʻat</th><th>た-shakli</th><th>たり</th></tr>
  <tr><td><ruby>読<rt>よ</rt></ruby>む</td><td class="pj-stem"><ruby>読<rt>よ</rt></ruby>んだ</td>
      <td class="pj-res"><ruby>読<rt>よ</rt></ruby>んだり</td></tr>
  <tr><td><ruby>見<rt>み</rt></ruby>る</td><td class="pj-stem"><ruby>見<rt>み</rt></ruby>た</td>
      <td class="pj-res"><ruby>見<rt>み</rt></ruby>たり</td></tr>
  <tr><td><ruby>泳<rt>およ</rt></ruby>ぐ</td><td class="pj-stem"><ruby>泳<rt>およ</rt></ruby>いだ</td>
      <td class="pj-res"><ruby>泳<rt>およ</rt></ruby>いだり</td></tr>
  <tr><td>する</td><td class="pj-stem">した</td><td class="pj-res">したり</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>日曜日<rt>にちようび</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んだり、<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いたりします。</p>
  <p class="pe-ex__rom">nichiyōbi ni hon o yondari, ongaku o kiitari shimasu</p>
  <p class="pe-ex__uz">Yakshanba kuni kitob oʻqiyman, musiqa tinglayman — shunaqa ishlar qilaman.</p>
  <p class="pe-ex__why">Ikkita ish aytildi, lekin maʼnosi «faqat shu ikkitasi» emas. Bu — <b>misol</b>: yana boshqa ishlar ham bor.</p>
</div>

<h3>2. Roʻyxat tugallanmagan — asosiy farq shu</h3>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">〜て — TARTIB</p>
    <p><ruby>読<rt>よ</rt></ruby>んで、<ruby>寝<rt>ね</rt></ruby>ました</p>
    <p>Avval oʻqidim, <b>keyin</b> uxladim. Tartib aniq, roʻyxat toʻliq.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">〜たり — MISOL</p>
    <p><ruby>読<rt>よ</rt></ruby>んだり、<ruby>寝<rt>ね</rt></ruby>たりしました</p>
    <p>Oʻqidim, uxladim — <b>shunaqa ishlar</b>. Tartib muhim emas.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bunga «-di-yu, -di» yoki «u yoq-bu yoq» yaqin turadi:</b>
  «Kitob oʻqidim, televizor koʻrdim, <em>shunaqa</em>». Yaʼni siz roʻyxatni
  <b>ochiq</b> qoldirasiz. Yapon tilida bu maʼno alohida grammatik shaklga
  ega — oʻzbekchada esa uni ohang va «shunaqa» kabi soʻzlar tashiydi.
  Shuning uchun tarjimada koʻpincha «…lar qildim» yoki «shunga oʻxshash
  ishlar» deb beriladi.</p>
</div>

<h3>3. Zamonni oxiri hal qiladi</h3>

<p>たり qismlari <b>hech qachon oʻzgarmaydi</b>. Butun gapning zamoni va
muloyimligi faqat oxirdagi する ga bogʻliq.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oxiri</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-res">〜たり〜たり<b>します</b></td><td class="pj-uz">qilaman (odat)</td></tr>
  <tr><td class="pj-res">〜たり〜たり<b>しました</b></td><td class="pj-uz">qildim</td></tr>
  <tr><td class="pj-res">〜たり〜たり<b>しています</b></td><td class="pj-uz">qilib turibman</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>土曜日<rt>どようび</rt></ruby>に<ruby>泳<rt>およ</rt></ruby>いだり、<ruby>写真<rt>しゃしん</rt></ruby>を<ruby>撮<rt>と</rt></ruby>ったりしました。</p>
  <p class="pe-ex__rom">doyōbi ni oyoidari, shashin o tottari shimashita</p>
  <p class="pe-ex__uz">Shanba kuni suzdim, rasmga oldim — shunaqa ishlar qildim.</p>
  <p class="pe-ex__why">Oʻtgan zamonni faqat <b>しました</b> tashiydi. <ruby>泳<rt>およ</rt></ruby>いだり va <ruby>撮<rt>と</rt></ruby>ったり oʻzgarmadi.</p>
</div>

<h3>4. Nechta boʻlishi kerak</h3>

<p>Odatda <b>ikkita</b>. Uchta ham boʻladi, lekin koʻpi bilan uchta — undan
ortigʻi gapni ogʻirlashtiradi. Bittasi ham mumkin: unda maʼno «masalan, shu»
boʻlib qoladi va koʻpincha yumshoq, ehtiyotkor ohang beradi.</p>

<p>Sanalgan ishlar bir-biriga <b>maʼnoda yaqin</b> boʻlgani maʼqul: dam
olish kuni qiladigan ishlar, uyda qiladigan ishlar, sayohatda koʻriladigan
narsalar. Butunlay bogʻlanmagan ikki ishni bir roʻyxatga qoʻysangiz, gap
gʻalati eshitiladi — xuddi oʻzbekchada «kitob oʻqidim, tishimni yuvdim,
shunaqa ishlar» degandek.</p>

<div class="pe-call pe-tip">
  <p><b>Qarama-qarshi juftlik ham koʻp uchraydi:</b>
  <ruby>行<rt>い</rt></ruby>ったり<ruby>来<rt>き</rt></ruby>たりします —
  «borib-kelib turaman». <ruby>降<rt>ふ</rt></ruby>ったり
  <ruby>止<rt>や</rt></ruby>んだり — «yogʻib-tinib turadi». Bunday juftlikda
  maʼno «misol» emas, <b>takrorlanish</b> boʻladi.</p>
</div>

<h3>5. Nega oxirida doim する?</h3>

<p>Tabiiy savol: gapda <ruby>読<rt>よ</rt></ruby>む va
<ruby>聞<rt>き</rt></ruby>く feʼllari bor edi, nega oxirida uchinchi feʼl —
する — paydo boʻlyapti?</p>

<p>Chunki 〜たり qismlari <b>gap tugatmaydi</b>: ular «shunaqa ish» degan
atamaning bir boʻlagiga aylanadi. Butun roʻyxatni bitta feʼl yopishi kerak,
va oʻsha feʼl — «qilmoq», yaʼni <b>する</b>. Soʻzma-soʻz tarjima qilsak:
«oʻqish-tinglash <em>qabilidagi</em> ishlarni <b>qilaman</b>».</p>

<div class="pe-call pe-rule">
  <p><b>Shuning uchun ham zamon faqat oxirida turadi.</b> Gapda haqiqiy
  kesim bitta — する. Qolganlari uning taʼrifi. Bu tuzilishni bir marta
  koʻrsangiz, qolip mantiqiy boʻlib qoladi va yodlash osonlashadi.</p>
</div>

<h3>6. Savol va javob</h3>

<div class="pe-ex">
  <p class="pe-ex__ja">— <ruby>日曜日<rt>にちようび</rt></ruby>に<ruby>何<rt>なに</rt></ruby>をしたりしますか。<br>— <ruby>公園<rt>こうえん</rt></ruby>で<ruby>休<rt>やす</rt></ruby>んだり、<ruby>友<rt>とも</rt></ruby>だちに<ruby>会<rt>あ</rt></ruby>ったりします。</p>
  <p class="pe-ex__rom">nichiyōbi ni nani o shitari shimasu ka / kōen de yasundari, tomodachi ni attari shimasu</p>
  <p class="pe-ex__uz">— Yakshanba kuni nimalar qilasiz? — Bogʻda dam olaman, doʻstlarim bilan uchrashaman — shunaqa ishlar.</p>
  <p class="pe-ex__why">Savolda ham <b>したり</b> turibdi — bu «nimalar qilasiz» degan ochiq savol. «<ruby>何<rt>なに</rt></ruby>をしますか» esa «nima qilasiz» — bitta aniq javob kutadi.</p>
</div>

<h3>7. Uch shaklni yonma-yon</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oʻzak</th><th>Qolip</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">て</td><td class="pj-end"><ruby>読<rt>よ</rt></ruby>んで、…</td>
      <td class="pj-uz">oʻqib, keyin…</td></tr>
  <tr><td class="pj-stem">た</td><td class="pj-end"><ruby>読<rt>よ</rt></ruby>んだことがあります</td>
      <td class="pj-uz">oʻqiganman</td></tr>
  <tr><td class="pj-stem">た</td><td class="pj-end"><ruby>読<rt>よ</rt></ruby>んだりします</td>
      <td class="pj-uz">oʻqiyman, shunaqa ishlar</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>んだり、<ruby>寝<rt>ね</rt></ruby>ました</p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby>んだり、<ruby>寝<rt>ね</rt></ruby>たり<b>しました</b> — ikkinchisi ham たり boʻladi, gapni esa します yopadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>読<rt>よ</rt></ruby>んでり</p>
  <p class="pe-fix__good">✓ <ruby>読<rt>よ</rt></ruby>ん<b>だ</b>り — り <b>た-shaklga</b> qoʻshiladi, て-shaklga emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>泳<rt>およ</rt></ruby>いだりしましたり</p>
  <p class="pe-fix__good">✓ <ruby>泳<rt>およ</rt></ruby>いだり…<b>しました</b> — oxirgi する たり olmaydi, u gapni tugatadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>見<rt>み</rt></ruby>る dan たり yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>見<rt>み</rt></ruby>たり</b> — た-shakli <ruby>見<rt>み</rt></ruby>た, keyin り.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>泳<rt>およ</rt></ruby>ぐ dan たり yasang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>泳<rt>およ</rt></ruby>いだり</b> — で → だ, keyin り.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Gapning zamonini nima hal qiladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Oxirdagi する.</b> します — hozirgi, しました — oʻtgan. たり qismlari oʻzgarmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. 〜て va 〜たり farqi nima?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>〜て <b>tartib</b>ni koʻrsatadi va roʻyxat toʻliq; 〜たり esa <b>misol</b> keltiradi va roʻyxat ochiq qoladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Yakshanba kuni kitob oʻqiyman, musiqa tinglayman» ni たり bilan ayting.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>日曜日<rt>にちようび</rt></ruby>に<ruby>本<rt>ほん</rt></ruby>を<ruby>読<rt>よ</rt></ruby>んだり、<ruby>音楽<rt>おんがく</rt></ruby>を<ruby>聞<rt>き</rt></ruby>いたりします。</b></p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜たり〜たりします</b> — shunaqa ishlar qilaman</li>
  <li><b><ruby>日曜日<rt>にちようび</rt></ruby></b> — yakshanba</li>
  <li><b><ruby>音楽<rt>おんがく</rt></ruby></b> — musiqa</li>
  <li><b><ruby>聞<rt>き</rt></ruby>いたり</b> — tinglash (misol)</li>
  <li><b><ruby>掃除<rt>そうじ</rt></ruby>する</b> — tozalamoq</li>
  <li><b><ruby>洗<rt>あら</rt></ruby>う</b> — yuvmoq (I guruh)</li>
  <li><b><ruby>手伝<rt>てつだ</rt></ruby>う</b> — yordam bermoq (I guruh)</li>
  <li><b><ruby>公園<rt>こうえん</rt></ruby></b> — bogʻ, park</li>
  <li><b><ruby>休<rt>やす</rt></ruby>む</b> — dam olmoq (I guruh)</li>
  <li><b>いろいろ</b> — turli-tuman</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>た-shakli + り</b>, odatda ikki marta, keyin <b>します</b>.</li>
    <li>Roʻyxat <b>ochiq</b>: «shunaqa ishlar», hammasi emas.</li>
    <li>Zamonni faqat oxirdagi <b>する</b> tashiydi.</li>
  </ul>
</div>
""",
    },
]
