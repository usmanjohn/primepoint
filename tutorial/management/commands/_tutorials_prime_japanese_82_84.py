# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-82, PJ-83, PJ-84: burch va vaqtning aniq nuqtasi.

Blok F davom etadi. Uchala dars bitta savolga javob beradi:
**gapning oldiga nima ulanadi va shundan maʼno qanday oʻzgaradi**.
    PJ-82 — べき: oʻzbekcha bitta «kerak» soʻzi yapon tilida ikkiga
            boʻlinadi. なければならない (iloj yoʻq) va べきだ
            (toʻgʻri ish) — bu chegara oʻzbek oʻquvchisi uchun
            koʻrinmaydi, shuning uchun dars uni ataylab chizadi.
    PJ-83 — ばかり: bitta soʻz, uch xil ulanish, uch xil maʼno.
            ot + ばかり (faqat) · て-shakli + ばかりいる (faqat shu
            ish) · た-shakli + ばかり (endigina).
    PJ-84 — ところ: «joy» degan ot vaqt oʻqiga koʻchadi. 辞書形 →
            hali boshlanmagan, ている → aynan hozir, た → hozirgina
            tugagan. PJ-83 dagi たばかり bilan yonma-yon qoʻyiladi —
            soat va his oʻrtasidagi farq.

⚠️ PJ-83 va PJ-84 ATAYLAB yonma-yon: たばかり va たところ ikkalasi ham
«endigina» deb tarjima qilinadi, lekin たところ soat boʻyicha bir necha
daqiqa, たばかり esa gapiruvchining hissi (bir oy ham boʻlishi mumkin).
Shu sababli PJ-83 da ところ soʻzi umuman yoʻq — solishtirish PJ-84 ning
ishi. Gate buni mexanik tekshiradi.

⚠️ PJ-84 dagi eng nozik joy — 〜ているところ **holat** feʼliga
tushmaydi: 「<ruby>住</ruby>んでいるところです」 «yashayotgan payt» emas,
«yashaydigan joy» boʻlib oʻqiladi. Bu dars uni alohida koʻrsatadi.

⚠️ Kursda hech qachon berilmagan ikki shakl bu batchda ham yoʻq:
意向形 (行こう / 〜ようと思う) va 〜んです. Gate ikkalasini ham
mexanik tekshiradi. 〜たほうがいい ham yoʻq — u toc da umuman
berilmagan, shuning uchun PJ-82 uni tanish deb olmaydi.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_82_84.py --author=prime
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
        "title": "PJ-82: 〜べきです va 〜なければならない — burch",
        "category": "japanese",
        "order": 82,
        "summary": (
            "Oʻzbekchadagi bitta «kerak» yapon tilida ikkiga boʻlinadi: "
            "なければならない — iloj yoʻq, qoida shunday; べきだ — hech kim "
            "majburlamayapti, lekin bu toʻgʻri ish. Va ularning inkori, "
            "oʻtgan zamoni, chegarasi."
        ),
        "stories": ["さいふの ひ"],
        "content": """
<h2>PJ-82: 〜べきです va 〜なければならない — burch</h2>

<p>パリ yaponiyalik doʻstiga xat yozyapti va ikki gap orasida
toʻxtab qoldi:</p>

<p><ruby>約束<rt>やくそく</rt></ruby>を<ruby>守<rt>まも</rt></ruby>らなければなりません。</p>

<p><ruby>約束<rt>やくそく</rt></ruby>を<ruby>守<rt>まも</rt></ruby>るべきです。</p>

<p>Oʻzbekchada ikkalasi ham bitta gap — «vada ustidan chiqish kerak».
Lekin yapon quloq ularni bir xil eshitmaydi. Birinchisida
<em>iloj yoʻq</em>: qoida shunday, qonun shunday, boshqa yoʻl
qolmagan. Ikkinchisida hech kim majburlamayapti — shunchaki
<em>bu toʻgʻri ish</em>.</p>

<p>Oʻzbek tilining bitta «kerak» soʻzi yapon tilida ikkiga boʻlinadi.
Shu chegarani chizish — butun darsning ishi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>〜なければならない</b> ni oddiy shaklda ishlatasiz</li>
    <li><b>〜べきだ</b> ni feʼlga toʻgʻri ulaysiz</li>
    <li>«qoida» va «toʻgʻri ish» degan ikki xil kerakni ajratasiz</li>
    <li><b>べきではない</b> va <b>べきだった</b> bilan taqiq va afsusni aytasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻgʻri ish</span>
  <span class="pe-chip pe-chip--v"><ruby>辞書形<rt>じしょけい</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">べきだ</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">shunday qilish toʻgʻri</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Iloj yoʻq</span>
  <span class="pe-chip pe-chip--neg">ない-shakli</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">なければならない</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">boshqa yoʻl qolmagan</span>
</div>

<h3>1. Nega bitta «kerak» kam</h3>

<p>Oʻzbekcha «kerak» juda mehnatkash soʻz. U hamma narsani koʻtaradi:
«pasport kerak», «uxlashim kerak», «uzr soʻrashing kerak»,
«bu kitobni oʻqish kerak». Toʻrt gapda toʻrt xil kuch bor, lekin soʻz
bitta, shuning uchun biz farqni sezmaymiz.</p>

<p>Yapon tili sezadi. U bitta savol soʻraydi: <b>kim majburlayapti —
tashqaridagi qoidami yoki ichkaridagi vijdonmi?</b> Javob qaysi
qolipni tanlashni hal qiladi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">〜なければならない — tashqarida</p>
    <p><ruby>空港<rt>くうこう</rt></ruby>でパスポートを<ruby>見<rt>み</rt></ruby>せなければなりません。</p>
    <p>Aeroportda pasportni koʻrsatish kerak. Qoida shunday.
    Sizning fikringiz soʻralmaydi, iloj ham yoʻq.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">〜べきだ — ichkarida</p>
    <p><ruby>悪<rt>わる</rt></ruby>いことをしたら、<ruby>謝<rt>あやま</rt></ruby>るべきです。</p>
    <p>Yomon ish qilsangiz, uzr soʻrash kerak. Hech qanday qonun
    majburlamaydi — lekin bu toʻgʻri.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu chegara koʻrinmaydi, va aynan shuning uchun
  xato tugʻiladi.</b> Biz «kerak» deymiz va gapni tugatamiz. Yapon
  tilida esa tanlov majburiy — gapni tuzayotganda <em>qaysi</em>
  kerak ekanini aytib qoʻyish shart. Shuning uchun tarjima qilishdan
  oldin oʻzingizdan bitta savol soʻrang: <em>«Agar qilmasam, nima
  boʻladi?»</em> Javob «jarima», «poyezdga kech qolaman»,
  «imtihonga kirmayman» boʻlsa — <b>なければならない</b>. Javob
  «hech nima, lekin oʻzimni yomon his qilaman» boʻlsa —
  <b>べきだ</b>. Bu savol deyarli hech qachon adashtirmaydi.</p>
</div>

<h3>2. 〜なければならない — tanish qolipning oddiy shakli</h3>

<p>Buni siz PJ-33 da <b>〜なければなりません</b> koʻrinishida
koʻrgansiz. PJ-45 dan keyin uning oddiy shakli ham kerak boʻladi,
chunki yozma matn <ruby>普通体<rt>ふつうたい</rt></ruby> da yuradi:
<b>なりません → ならない</b>. Boshqa hech narsa oʻzgarmaydi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>ない-shakli</th><th>Almashtiramiz</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>行<rt>い</rt></ruby>く</td><td class="pj-stem"><ruby>行<rt>い</rt></ruby>かない</td>
      <td class="pj-end">ない → なければ</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>かなければならない</td>
      <td class="pj-uz">borishim kerak</td></tr>
  <tr><td><ruby>食<rt>た</rt></ruby>べる</td><td class="pj-stem"><ruby>食<rt>た</rt></ruby>べない</td>
      <td class="pj-end">ない → なければ</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べなければならない</td>
      <td class="pj-uz">yeyishim kerak</td></tr>
  <tr><td>する</td><td class="pj-stem">しない</td>
      <td class="pj-end">ない → なければ</td>
      <td class="pj-res">しなければならない</td>
      <td class="pj-uz">qilishim kerak</td></tr>
  <tr><td><ruby>来<rt>く</rt></ruby>る</td><td class="pj-stem"><ruby>来<rt>こ</rt></ruby>ない</td>
      <td class="pj-end">ない → なければ</td>
      <td class="pj-res"><ruby>来<rt>こ</rt></ruby>なければならない</td>
      <td class="pj-uz">kelishi kerak</td></tr>
  <tr><td><ruby>安<rt>やす</rt></ruby>い</td><td class="pj-stem"><ruby>安<rt>やす</rt></ruby>くない</td>
      <td class="pj-end">ない → なければ</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>くなければならない</td>
      <td class="pj-uz">arzon boʻlishi kerak</td></tr>
  <tr><td><ruby>学生<rt>がくせい</rt></ruby></td><td class="pj-stem"><ruby>学生<rt>がくせい</rt></ruby>ではない</td>
      <td class="pj-end">ない → なければ</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>でなければならない</td>
      <td class="pj-uz">talaba boʻlishi kerak</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Qoida bitta, uch qadamdan iborat.</b> Feʼlni
  <b>ない-shakliga</b> qoʻying (PJ-34), oxiridagi <b>ない</b> ni
  <b>なければ</b> ga almashtiring, keyin <b>ならない</b> qoʻshing.
  Sifat va otlar ham xuddi shu yoʻldan yuradi — ularning inkori
  ham ない bilan tugagani uchun.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>明日<rt>あした</rt></ruby>までに<span class="pe-hl pe-hl--o">レポートを<ruby>出<rt>だ</rt></ruby>さなければならない</span>。</p>
  <p class="pe-ex__uz">Ertagacha hisobotni topshirishim kerak.</p>
  <p class="pe-ex__why">Muddat belgilangan, uni kim qoʻygani muhim emas — tashqi majburiyat. <b>べき</b> bu yerga tushmaydi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Ikkita qardosh shakl.</b> <b>〜なくてはならない</b> —
  aynan shu maʼno, faqat biroz yumshoqroq. <b>〜なければいけない</b>
  esa umumiy qoidani emas, <em>aynan shu holatni</em> koʻrsatadi:
  «hozir, bu safar shunday qilish kerak». Suhbatda esa bularning
  hammasi qisqaradi —
  <b><ruby>行<rt>い</rt></ruby>かなきゃ</b>,
  <b><ruby>行<rt>い</rt></ruby>かなくちゃ</b>. Yozmang, lekin
  eshitsangiz taniyalang: bu oʻsha なければならない ning tirik nutqdagi
  kiyimi.</p>
</div>

<h3>3. べき — feʼlga qanday ulanadi</h3>

<p>Ulanish oson: <b>lugʻat shakli + べき</b>. Guruh muhim emas,
tovush oʻzgarishi yoʻq.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>本<rt>ほん</rt></ruby></span>
  <span class="pj-joshi__p">を<small>TOʻLDIRUVCHI</small></span>
  <span class="pj-joshi__n"><ruby>返<rt>かえ</rt></ruby>す<b>べき</b></span>
  <span class="pj-joshi__v">です</span>
  <span class="pj-joshi__uz">Kitobni qaytarish kerak. — べき feʼldan keyin, kesimdan oldin.</span>
</div>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>Nima ulanadi</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">feʼl</td><td class="pj-end"><ruby>辞書形<rt>じしょけい</rt></ruby> + べき</td>
      <td class="pj-res"><ruby>読<rt>よ</rt></ruby>むべきだ</td>
      <td class="pj-uz">oʻqish kerak</td></tr>
  <tr><td class="pj-stem">する</td><td class="pj-end">するべき / すべき</td>
      <td class="pj-res"><ruby>注意<rt>ちゅうい</rt></ruby>するべきだ</td>
      <td class="pj-uz">ehtiyot boʻlish kerak</td></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end">である + べき</td>
      <td class="pj-res"><ruby>平等<rt>びょうどう</rt></ruby>であるべきだ</td>
      <td class="pj-uz">teng boʻlishi kerak</td></tr>
  <tr><td class="pj-stem">い-sifat</td><td class="pj-end">ulanmaydi</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>くなければならない</td>
      <td class="pj-uz">arzon boʻlishi kerak</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>Uchta nuqta shu jadvalda yashiringan.</b> Birinchisi:
  する ning ikkita shakli bor — <b>するべき</b> (kundalik) va
  <b>すべき</b> (kitobiy, gazetada shu turadi). Ikkalasi ham
  toʻgʻri. Ikkinchisi: ot yalangʻoch ulanmaydi, oldiga
  <b>である</b> kerak. Uchinchisi va eng muhimi:
  <b>い-sifat べき olmaydi</b>. «Arzon boʻlishi kerak» degani
  uchun なければならない ga oʻting.</p>
</div>

<h3>4. Toʻrtta aʼzo</h3>

<p>べき ning oʻzi ot kabi ishlaydi, shuning uchun oxiriga だ, です,
ではない, だった qoʻshiladi — ularning har biri gapga boshqa
maʼno beradi.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h">べきだ / べきです</p>
    <p><ruby>毎日<rt>まいにち</rt></ruby><ruby>復習<rt>ふくしゅう</rt></ruby>するべきです。</p>
    <p>Har kuni takrorlash kerak. — maslahat emas, baho: shunday
    qilish toʻgʻri.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">べきではない</p>
    <p><ruby>人<rt>ひと</rt></ruby>の<ruby>日記<rt>にっき</rt></ruby>を<ruby>読<rt>よ</rt></ruby>むべきではない。</p>
    <p>Birovning kundaligini oʻqish kerak emas. — taqiq emas,
    axloqiy rad.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">べきだった</p>
    <p>もっと<ruby>早<rt>はや</rt></ruby>く<ruby>謝<rt>あやま</rt></ruby>るべきだった。</p>
    <p>Ertaroq uzr soʻrashim kerak edi. — qilmadim, va afsusdaman.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">べき + ot</p>
    <p><ruby>今<rt>いま</rt></ruby><ruby>読<rt>よ</rt></ruby>むべき<ruby>本<rt>ほん</rt></ruby></p>
    <p>Hozir oʻqilishi kerak boʻlgan kitob. — otdan oldin だ tushib
    qoladi.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>子供<rt>こども</rt></ruby>にそんなことを<span class="pe-hl pe-hl--neg"><ruby>言<rt>い</rt></ruby>うべきではありません</span>。</p>
  <p class="pe-ex__uz">Bolaga bunday gapni aytish kerak emas.</p>
  <p class="pe-ex__why">Hurmatli shakli — <b>べきではありません</b>. Suhbatda <b>べきじゃない</b> ham eshitiladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>先<rt>さき</rt></ruby>に<span class="pe-hl pe-hl--v"><ruby>電話<rt>でんわ</rt></ruby>するべきだった</span>が、<ruby>忘<rt>わす</rt></ruby>れてしまった。</p>
  <p class="pe-ex__uz">Avval qoʻngʻiroq qilishim kerak edi, lekin unutib qoʻydim.</p>
  <p class="pe-ex__why">べきだった har doim afsus bilan keladi: ish qilinmagan. Shuning uchun undan keyin が yoki けど juda tabiiy.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>べきだった ni oʻzbekchada ikki xil aytamiz, va ikkalasi ham
  toʻgʻri.</b> «Aytishim <em>kerak edi</em>» va «aytishim
  <em>kerak ekan</em>» — birinchisi rejani, ikkinchisi keyin
  tushunilgan afsusni bildiradi. Yaponcha <b>べきだった</b> aynan
  ikkinchisiga yaqin: voqea oʻtib boʻlgan, endi orqaga qarab
  baho berilyapti. Shuning uchun uni «kerak edi» deb
  tarjima qilganda ham, ichida doim <em>«lekin qilmadim»</em>
  degan davomi bor deb bilib turing.</p>
</div>

<h3>5. Kuchning shkalasi</h3>

<p>Bu darsgacha siz ruxsat, taqiq va majburiyatni alohida
oʻrgangansiz. Endi ularni bitta jadvalga terib qoʻysak, べき oʻz
oʻrnini topadi — u <em>eng kuchli</em> emas, u <em>boshqa
turdagi</em> kuch.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Kuchi</th><th>Kim majbur qilyapti</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pj-stem">〜なければならない</td><td class="pj-end">majburiyat</td>
      <td class="pj-res">qoida, vaziyat</td><td class="pj-uz">qilmasam boʻlmaydi</td></tr>
  <tr><td class="pj-stem">〜べきだ</td><td class="pj-end">burch</td>
      <td class="pj-res">vijdon, adolat</td><td class="pj-uz">qilish toʻgʻri</td></tr>
  <tr><td class="pj-stem">〜てもいい</td><td class="pj-end">ruxsat</td>
      <td class="pj-res">hech kim</td><td class="pj-uz">qilsa boʻladi</td></tr>
  <tr><td class="pj-stem">〜なくてもいい</td><td class="pj-end">erkinlik</td>
      <td class="pj-res">hech kim</td><td class="pj-uz">qilmasa ham boʻladi</td></tr>
  <tr><td class="pj-stem">〜べきではない</td><td class="pj-end">axloqiy rad</td>
      <td class="pj-res">vijdon</td><td class="pj-uz">qilmaslik toʻgʻri</td></tr>
  <tr><td class="pj-stem">〜てはいけない</td><td class="pj-end">taqiq</td>
      <td class="pj-res">qoida, kattalar</td><td class="pj-uz">mumkin emas</td></tr>
</table></div>

<h3>6. べき qayerda ishlamaydi</h3>

<p>Ikkita chegara bor va ikkalasi ham darsliklarda kam yoziladi.</p>

<div class="pe-steps">
  <ol>
    <li><b>Tabiat hodisasiga べき tushmaydi.</b> Yomgʻir yogʻishi
    «toʻgʻri» yoki «notoʻgʻri» boʻlmaydi — u shunchaki yogʻadi.
    Bunday gapda PJ-62 dagi <b>でしょう</b> yoki PJ-81 dagi
    <b>に<ruby>違<rt>ちが</rt></ruby>いない</b> turadi.</li>
    <li><b>Ustozga, mijozga, katta yoshlilarga べき aytilmaydi.</b>
    U baho beradigan soʻz, va yuqoridagi odamga baho berish
    yapon tilida qoʻpol. Uning oʻrnida PJ-69 dagi hurmat shakli
    yoki oddiy iltimos ishlatiladi.</li>
  </ol>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>先生<rt>せんせい</rt></ruby>、もっと<span class="pe-hl pe-hl--v">お<ruby>休<rt>やす</rt></ruby>みになってください</span>。</p>
  <p class="pe-ex__uz">Ustoz, koʻproq dam oling.</p>
  <p class="pe-ex__why">「<ruby>先生<rt>せんせい</rt></ruby>は<ruby>休<rt>やす</rt></ruby>むべきです」 grammatik jihatdan toʻgʻri, lekin ustozga aytilsa qoʻpol eshitiladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu yerda oʻzbek tili sizni qutqaradi.</b> Oʻzbekchada ham
  ustozga «dam olishingiz kerak» deyish gʻalati —
  «dam olsangiz yaxshi boʻlardi», «dam oling» deymiz. Yaponchada
  ham xuddi shu odob ishlaydi, faqat u grammatikaga yozib
  qoʻyilgan: hurmat kerak boʻlgan joyda baho beruvchi soʻz
  emas, <ruby>尊敬語<rt>そんけいご</rt></ruby> turadi.
  Demak, べき ni ishlatishdan oldin bitta savol: <em>«Men bu
  odamga baho bera olamanmi?»</em> Javob «yoʻq» boʻlsa, gapni
  iltimosga aylantiring.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">義</span>
    <span class="pj-kanji__uz">adolat, burch</span>
    <span class="pj-kanji__on">オン: ギ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">義務 (ぎむ) — burch · 意義 (いぎ) — maʼno, ahamiyat</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">務</span>
    <span class="pj-kanji__uz">vazifa, xizmat</span>
    <span class="pj-kanji__on">オン: ム</span>
    <span class="pj-kanji__kun">KUN: つと(める)</span>
    <span class="pj-kanji__note">事務所 (じむしょ) — idora · 公務員 (こうむいん) — davlat xizmatchisi</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">守</span>
    <span class="pj-kanji__uz">saqlamoq, rioya qilmoq</span>
    <span class="pj-kanji__on">オン: シュ</span>
    <span class="pj-kanji__kun">KUN: まも(る)</span>
    <span class="pj-kanji__note">約束を守る — vadada turmoq · 留守 (るす) — uyda yoʻq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>学生<rt>がくせい</rt></ruby>べきだ</p>
  <p class="pe-fix__good">✓ <ruby>学生<rt>がくせい</rt></ruby><b>である</b>べきだ — ot べき oldida である ni oladi, yalangʻoch ulanmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>値段<rt>ねだん</rt></ruby>は<ruby>安<rt>やす</rt></ruby>いべきだ</p>
  <p class="pe-fix__good">✓ <ruby>値段<rt>ねだん</rt></ruby>は<ruby>安<rt>やす</rt></ruby>く<b>なければならない</b> — い-sifat べき olmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>行<rt>い</rt></ruby>かないなければならない</p>
  <p class="pe-fix__good">✓ <ruby>行<rt>い</rt></ruby>か<b>なければ</b>ならない — ない ni olib tashlamang, uni なければ ga <em>almashtiring</em>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>謝<rt>あやま</rt></ruby>るべきじゃないだった</p>
  <p class="pe-fix__good">✓ <ruby>謝<rt>あやま</rt></ruby>るべき<b>ではなかった</b> — oʻtgan zamon べき ning oʻzidan keyin yasaladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>明日<rt>あした</rt></ruby>は<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>るべきだ</p>
  <p class="pe-fix__good">✓ <ruby>明日<rt>あした</rt></ruby>は<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby><b>るでしょう</b> — tabiat hodisasi «toʻgʻri» boʻlmaydi, べき unga tushmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Aeroportda pasportni koʻrsatish kerak» — qaysi qolip?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>見<rt>み</rt></ruby>せなければなりません</b>. Qoida tashqarida turibdi va iloj yoʻq. べき bu yerda notoʻgʻri boʻlardi — u vijdonning soʻzi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Boʻsh joyni toʻldiring: <ruby>先生<rt>せんせい</rt></ruby>は<ruby>公平<rt>こうへい</rt></ruby>___あるべきです。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>で</b> — <ruby>公平<rt>こうへい</rt></ruby> な-sifat, べき oldida <b>である</b> kerak: <ruby>公平<rt>こうへい</rt></ruby>であるべきです («ustoz odil boʻlishi kerak»).</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Ertaroq aytishim kerak edi, lekin aytmadim» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>もっと<ruby>早<rt>はや</rt></ruby>く<ruby>言<rt>い</rt></ruby>うべきだった</b>. べきだった ichida doim «lekin qilmadim» degan davomi bor, shuning uchun uni alohida aytish ham shart emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>安<rt>やす</rt></ruby>い bilan べき ishlatsa boʻladimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> い-sifat べき olmaydi. «Arzon boʻlishi kerak» degani uchun <ruby>安<rt>やす</rt></ruby>くなければならない deyiladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. Ustozga «koʻproq dam oling» deyish uchun べき ishlatsa boʻladimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> べき baho beradi, baho esa yuqoridagi odamga aytilmaydi. Oʻrniga <ruby>尊敬語<rt>そんけいご</rt></ruby>: <ruby>先生<rt>せんせい</rt></ruby>、もっとお<ruby>休<rt>やす</rt></ruby>みになってください。</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜べきだ</b> — … kerak (toʻgʻri ish)</li>
  <li><b>〜べきではない</b> — … kerak emas (axloqiy rad)</li>
  <li><b>〜べきだった</b> — … kerak edi (afsus)</li>
  <li><b>〜なければならない</b> — … majbur, iloji yoʻq</li>
  <li><b>〜なくてもいい</b> — … shart emas</li>
  <li><b><ruby>義務<rt>ぎむ</rt></ruby></b> — burch, majburiyat</li>
  <li><b><ruby>規則<rt>きそく</rt></ruby></b> — qoida, tartib</li>
  <li><b><ruby>守<rt>まも</rt></ruby>る</b> — rioya qilmoq, saqlamoq</li>
  <li><b><ruby>謝<rt>あやま</rt></ruby>る</b> — uzr soʻramoq</li>
  <li><b><ruby>必<rt>かなら</rt></ruby>ず</b> — albatta, soʻzsiz</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>なければならない</b> — qoida majburlaydi; <b>べきだ</b> — vijdon.</li>
    <li>べき <ruby>辞書形<rt>じしょけい</rt></ruby> ga ulanadi; ot <b>である</b> oladi, い-sifat esa umuman ulanmaydi.</li>
    <li><b>べきだった</b> = «kerak edi, lekin qilmadim». Yuqoridagi odamga べき aytilmaydi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-83: 〜ばかり va 〜たばかり — «endigina» va «faqat»",
        "category": "japanese",
        "order": 83,
        "summary": (
            "Bitta soʻz — ばかり — uch xil ulanadi va uch xil maʼno beradi: "
            "ot bilan «faqat shu», て-shakli bilan «faqat shu ish», "
            "た-shakli bilan «endigina». Ulanishni koʻrsangiz, maʼnoni "
            "bilasiz."
        ),
        "stories": ["ついたばかりの メール"],
        "content": """
<h2>PJ-83: 〜ばかり va 〜たばかり — «endigina» va «faqat»</h2>

<p>Bir kunda, bitta uyda, ikkita gap:</p>

<p>お<ruby>母<rt>かあ</rt></ruby>さん: イムロンはゲーム<b>ばかり</b>している。</p>

<p>イムロン: <ruby>宿題<rt>しゅくだい</rt></ruby>が<ruby>終<rt>お</rt></ruby>わった<b>ばかり</b>だよ。</p>

<p>Bitta soʻz — ばかり — ikki gapda turibdi, lekin maʼnosi umuman
boshqa. Onasi «faqat oʻyin, boshqa hech narsa» deyapti. Imron
esa «uy vazifasi <em>endigina</em> tugadi» deyapti. Tanbeh va
uzr bitta soʻz bilan.</p>

<p>Maʼnoni ばかり ning oʻzi emas, <b>undan oldin turgan shakl</b>
hal qiladi. Shuni koʻrishni oʻrgansangiz, bu dars tugadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>ot + ばかり</b> bilan «faqat shu, haddan tashqari koʻp» deysiz</li>
    <li><b>て-shakli + ばかりいる</b> bilan takrorlanadigan ishni tanqid qilasiz</li>
    <li><b>た-shakli + ばかり</b> bilan «endigina» deysiz</li>
    <li>ばかり va <b>だけ</b> orasidagi ohang farqini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ulanish maʼnoni hal qiladi</span>
  <span class="pe-chip pe-chip--o">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">ばかり</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">faqat shu</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ulanish maʼnoni hal qiladi</span>
  <span class="pe-chip pe-chip--v">た-shakli</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">ばかり</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">endigina qildi</span>
</div>

<h3>1. ot + ばかり — «faqat shu, boshqasi yoʻq»</h3>

<p>Birinchi maʼnosi eng sodda: otdan keyin kelib, «faqat shu narsa»
deydi. Lekin unda yashirin bir ohang bor —
<b>«koʻp, juda koʻp, meningcha ortiqcha»</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>弟<rt>おとうと</rt></ruby>は<span class="pe-hl pe-hl--o"><ruby>肉<rt>にく</rt></ruby>ばかり</span><ruby>食<rt>た</rt></ruby>べている。</p>
  <p class="pe-ex__uz">Ukam faqat goʻsht yeyapti.</p>
  <p class="pe-ex__why">Gapiruvchi shunchaki xabar bermayapti — u buni yoqtirmaydi. «Sabzavot ham yesa boʻlardi» degan davomi eshitilib turibdi.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Qoʻshimchaga eʼtibor bering.</b> ばかり <b>を</b> va
  <b>が</b> ni siqib chiqaradi:
  <ruby>肉<rt>にく</rt></ruby>を<ruby>食<rt>た</rt></ruby>べる →
  <ruby>肉<rt>にく</rt></ruby><b>ばかり</b><ruby>食<rt>た</rt></ruby>べる.
  Qolgan qoʻshimchalar esa joyida qoladi va ばかり ulardan
  <em>keyin</em> keladi:
  <ruby>公園<rt>こうえん</rt></ruby>で<b>ばかり</b><ruby>遊<rt>あそ</rt></ruby>ぶ,
  <ruby>友<rt>とも</rt></ruby>だちと<b>ばかり</b><ruby>話<rt>はな</rt></ruby>す.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>店<rt>みせ</rt></ruby>には<span class="pe-hl pe-hl--s"><ruby>高<rt>たか</rt></ruby>い<ruby>物<rt>もの</rt></ruby>ばかり</span>ある。</p>
  <p class="pe-ex__uz">Bu doʻkonda faqat qimmat narsalar bor.</p>
  <p class="pe-ex__why">Sifat bilan otga ham ulanadi. Ohang yana oʻsha — «arzoni yoʻqmi?» degan norozilik eshitiladi.</p>
</div>

<h3>2. て-shakli + ばかりいる — «faqat shu ishni qiladi»</h3>

<p>Ot emas, <em>harakat</em> takrorlanayotganini aytmoqchi
boʻlsangiz, feʼlni て-shakliga qoʻyib (PJ-29, PJ-30) ばかりいる
qoʻshasiz.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Feʼl</th><th>て-shakli</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td><ruby>遊<rt>あそ</rt></ruby>ぶ</td><td class="pj-stem"><ruby>遊<rt>あそ</rt></ruby>んで</td>
      <td class="pj-res"><ruby>遊<rt>あそ</rt></ruby>んでばかりいる</td>
      <td class="pj-uz">faqat oʻynaydi</td></tr>
  <tr><td><ruby>泣<rt>な</rt></ruby>く</td><td class="pj-stem"><ruby>泣<rt>な</rt></ruby>いて</td>
      <td class="pj-res"><ruby>泣<rt>な</rt></ruby>いてばかりいた</td>
      <td class="pj-uz">faqat yigʻlardi</td></tr>
  <tr><td><ruby>寝<rt>ね</rt></ruby>る</td><td class="pj-stem"><ruby>寝<rt>ね</rt></ruby>て</td>
      <td class="pj-res"><ruby>寝<rt>ね</rt></ruby>てばかりいる</td>
      <td class="pj-uz">faqat uxlaydi</td></tr>
  <tr><td>する</td><td class="pj-stem">して</td>
      <td class="pj-res">してばかりいる</td>
      <td class="pj-uz">faqat shuni qiladi</td></tr>
</table></div>

<div class="pe-call pe-warn">
  <p><b>いる ni tashlab ketmang.</b> <ruby>遊<rt>あそ</rt></ruby>んで<b>ばかり</b>
  oʻzi yarim gap. Toʻliq shakli — <b>ばかりいる</b> yoki
  <b>ばかりいます</b>. Bu PJ-31 dagi 〜ている ning ichiga ばかり
  kirib olgani: <ruby>遊<rt>あそ</rt></ruby>んでいる →
  <ruby>遊<rt>あそ</rt></ruby>んで<b>ばかり</b>いる.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>彼<rt>かれ</rt></ruby>は<span class="pe-hl pe-hl--v"><ruby>文句<rt>もんく</rt></ruby>を<ruby>言<rt>い</rt></ruby>ってばかりいて</span>、<ruby>何<rt>なに</rt></ruby>もしない。</p>
  <p class="pe-ex__uz">U faqat noliydi, hech nima qilmaydi.</p>
  <p class="pe-ex__why">Bu qolipning ohangi deyarli doim tanqid. Oʻzingiz haqingizda ishlatsangiz, uzr yoki hazil boʻlib eshitiladi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida bu ohangni qoʻshimcha koʻtaradi.</b>
  «Oʻyna<em>b yuradi</em>», «gapir<em>averadi</em>»,
  «uxla<em>b yotibdi</em>» — uchalasi ham shunchaki
  «oʻynaydi, gapiradi, uxlaydi» emas. Ularda takror ham, norozilik
  ham bor, va aynan shu <b>〜てばかりいる</b> ning ishi. Shuning
  uchun bu qolipni «faqat oʻynaydi» deb quruq tarjima
  qilmang — ichingizda «oʻynab yuradi» deb eshiting, keyin yaponcha
  gapning ovozi ham toʻgʻri chiqadi. Aksincha ham ishlaydi: oʻzbekcha
  «-averadi» ni koʻrsangiz, yaponchada て-shakli va ばかりいる ni
  qidiring.</p>
</div>

<h3>3. た-shakli + ばかり — «endigina»</h3>

<p>Uchinchi maʼnosi birinchi ikkitasiga umuman oʻxshamaydi, va
u N4 imtihonida eng koʻp soʻraladigani. <b>た-shakli + ばかり</b>
— ish <em>hozirgina</em> tugagan.</p>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>日本<rt>にほん</rt></ruby></span>
  <span class="pj-joshi__p">に<small>YOʻNALISH</small></span>
  <span class="pj-joshi__n"><ruby>来<rt>き</rt></ruby>た<b>ばかり</b></span>
  <span class="pj-joshi__v">です</span>
  <span class="pj-joshi__uz">Yaponiyaga endigina keldim.</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--v"><ruby>食<rt>た</rt></ruby>べたばかり</span>だから、おなかがすいていない。</p>
  <p class="pe-ex__uz">Endigina ovqatlandim, shuning uchun qornim och emas.</p>
  <p class="pe-ex__why">«Endigina» — sabab. Shuning uchun bu qolipdan keyin PJ-53 dagi <b>から</b> va <b>ので</b> juda tez-tez keladi.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Otdan oldin の kerak.</b> たばかり ot emas, shuning uchun
  otni aniqlashda oradan <b>の</b> tushadi:
  <ruby>買<rt>か</rt></ruby>ったばかり<b>の</b><ruby>時計<rt>とけい</rt></ruby>
  («endigina sotib olingan soat»),
  <ruby>生<rt>う</rt></ruby>まれたばかり<b>の</b><ruby>赤<rt>あか</rt></ruby>ちゃん
  («endigina tugʻilgan chaqaloq»). の siz gap buziladi.</p>
</div>

<h3>4. «Endigina» — soatda emas, koʻngilda</h3>

<p>Bu qolipning eng chiroyli tomoni shu: <b>たばかり soatga
qaramaydi</b>. U gapiruvchining hissini koʻrsatadi — ish unga
<em>yaqin</em> tuyulsa, ばかり ishlaydi.</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">Bir necha daqiqa</p>
    <p><ruby>今<rt>いま</rt></ruby><ruby>起<rt>お</rt></ruby>きたばかりです。</p>
    <p>Endigina uygʻondim. Soat boʻyicha ham yangi.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">Bir yil</p>
    <p><ruby>去年<rt>きょねん</rt></ruby><ruby>結婚<rt>けっこん</rt></ruby>したばかりです。</p>
    <p>Oʻtgan yili endigina turmush qurdik. Bir yil oʻtgan, lekin
    gapiruvchi uchun bu hali «yaqinda».</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «endigina» ham aynan shunday ishlaydi.</b>
  «Endigina uygʻondim» — besh daqiqa. «Bu shaharga endigina
  koʻchib kelganmiz» — bir yil boʻlgan boʻlishi ham mumkin.
  Ikkala gapda ham soat emas, <em>his</em> gapiryapti: ish hali
  «yangi», hali oʻrganib ketilmagan. Shuning uchun たばかり ni
  tarjima qilganda lugʻatga emas, oʻzingizning «endigina»
  soʻzingizga ishoning — u yapon tilidagisi bilan bir xil
  choʻzilib, bir xil qisqaradi.</p>
</div>

<h3>5. ばかり va だけ</h3>

<p>Ikkalasi ham oʻzbekchada «faqat» deb tarjima qilinadi, lekin
ular bir xil emas. <b>だけ</b> — sovuq oʻlchov.
<b>ばかり</b> — baho.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Gap</th><th>Nimani aytyapti</th><th>Ohangi</th></tr>
  <tr><td class="pj-stem"><ruby>一人<rt>ひとり</rt></ruby>だけ<ruby>来<rt>き</rt></ruby>た</td>
      <td class="pj-uz">faqat bitta odam keldi</td>
      <td class="pj-res">fakt, bahosiz</td></tr>
  <tr><td class="pj-stem"><ruby>男<rt>おとこ</rt></ruby>ばかりだ</td>
      <td class="pj-uz">hammasi erkak</td>
      <td class="pj-res">koʻp, va bu koʻzga tashlanyapti</td></tr>
  <tr><td class="pj-stem"><ruby>水<rt>みず</rt></ruby>だけ<ruby>飲<rt>の</rt></ruby>む</td>
      <td class="pj-uz">faqat suv ichaman</td>
      <td class="pj-res">tanlov, xotirjam</td></tr>
  <tr><td class="pj-stem"><ruby>水<rt>みず</rt></ruby>ばかり<ruby>飲<rt>の</rt></ruby>む</td>
      <td class="pj-uz">faqat suv ichaveradi</td>
      <td class="pj-res">takror, gʻalati yoki ortiqcha</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Bitta oson sinov.</b> Gapni ichingizda «...ning oʻzi»
  deb tugatib koʻring. «Faqat suv<em>ning oʻzi</em>ni ichaman» —
  chegara, demak <b>だけ</b>. Endi «...dan boshqa hech narsa
  yoʻq, juda koʻp» deb tugatib koʻring: «Suv ichaveradi-yey» —
  baho, demak <b>ばかり</b>. Ikkinchisida ovoz ham oʻzgaradi, va
  yaponchada ham xuddi shunday.</p>
</div>

<h3>6. Uchtasi bitta jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Oldida nima turibdi</th><th>Qolip</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">ot</td><td class="pj-end">ot + ばかり</td>
      <td class="pj-res">ゲームばかりする</td>
      <td class="pj-uz">faqat oʻyin oʻynaydi</td></tr>
  <tr><td class="pj-stem">て-shakli</td><td class="pj-end">〜てばかりいる</td>
      <td class="pj-res"><ruby>遊<rt>あそ</rt></ruby>んでばかりいる</td>
      <td class="pj-uz">faqat oʻynab yuradi</td></tr>
  <tr><td class="pj-stem">た-shakli</td><td class="pj-end">〜たばかりだ</td>
      <td class="pj-res"><ruby>来<rt>き</rt></ruby>たばかりだ</td>
      <td class="pj-uz">endigina keldi</td></tr>
  <tr><td class="pj-stem">た-shakli + ot</td><td class="pj-end">〜たばかりの + ot</td>
      <td class="pj-res"><ruby>買<rt>か</rt></ruby>ったばかりの<ruby>靴<rt>くつ</rt></ruby></td>
      <td class="pj-uz">endigina olingan poyabzal</td></tr>
</table></div>

<div class="pe-call pe-uz">
  <p><b>Bu jadval — darsning butun mazmuni.</b> Yapon tilida
  koʻp soʻz shunday ishlaydi: soʻzning oʻzi bitta, lekin
  <em>oldiga nima ulangani</em> maʼnoni oʻzgartiradi. Oʻzbek
  tilida ham shunga oʻxshash narsa bor —
  «kel<b>gan</b>», «kel<b>ganda</b>», «kel<b>ganicha</b>»
  bittagina «kel» oʻzagidan chiqadi, lekin uchtasi uch xil
  gap. Shuning uchun yangi qolipni koʻrganda birinchi savol
  «bu nima degani?» emas, <b>«bu nimaga ulangan?»</b> boʻlsin.
  ばかり — bu odatni mustahkamlaydigan eng yaxshi mashq.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">遊</span>
    <span class="pj-kanji__uz">oʻynamoq, sayr qilmoq</span>
    <span class="pj-kanji__on">オン: ユウ</span>
    <span class="pj-kanji__kun">KUN: あそ(ぶ)</span>
    <span class="pj-kanji__note">遊園地 (ゆうえんち) — istirohat bogʻi · 遊ぶ — oʻynamoq</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">済</span>
    <span class="pj-kanji__uz">tugamoq, hal boʻlmoq</span>
    <span class="pj-kanji__on">オン: サイ</span>
    <span class="pj-kanji__kun">KUN: す(む)</span>
    <span class="pj-kanji__note">経済 (けいざい) — iqtisod · 済んだばかり — endigina tugadi</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">文</span>
    <span class="pj-kanji__uz">yozuv, gap, madaniyat</span>
    <span class="pj-kanji__on">オン: ブン・モン</span>
    <span class="pj-kanji__kun">KUN: ふみ</span>
    <span class="pj-kanji__note">文句 (もんく) — nolish, eʼtiroz · 文化 (ぶんか) — madaniyat</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>肉<rt>にく</rt></ruby><b>を</b>ばかり<ruby>食<rt>た</rt></ruby>べる</p>
  <p class="pe-fix__good">✓ <ruby>肉<rt>にく</rt></ruby>ばかり<ruby>食<rt>た</rt></ruby>べる — ばかり を va が ni siqib chiqaradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>遊<rt>あそ</rt></ruby>んでばかり<b>ある</b></p>
  <p class="pe-fix__good">✓ <ruby>遊<rt>あそ</rt></ruby>んでばかり<b>いる</b> — bu 〜ている ning ichi, odam esa いる bilan keladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>買<rt>か</rt></ruby>ったばかり<ruby>靴<rt>くつ</rt></ruby></p>
  <p class="pe-fix__good">✓ <ruby>買<rt>か</rt></ruby>ったばかり<b>の</b><ruby>靴<rt>くつ</rt></ruby> — otdan oldin の shart.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>来<rt>く</rt></ruby>るばかりです («endigina keldim» maʼnosida)</p>
  <p class="pe-fix__good">✓ <ruby>来<rt>き</rt></ruby>たばかりです — «endigina» uchun た-shakli kerak, lugʻat shakli emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>一人<rt>ひとり</rt></ruby>ばかり<ruby>来<rt>き</rt></ruby>ました («faqat bir kishi keldi» maʼnosida)</p>
  <p class="pe-fix__good">✓ <ruby>一人<rt>ひとり</rt></ruby>だけ<ruby>来<rt>き</rt></ruby>ました — quruq chegara uchun だけ turadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Ukam faqat goʻsht yeydi» — qoʻshimchani qoʻying: <ruby>弟<rt>おとうと</rt></ruby>は<ruby>肉<rt>にく</rt></ruby>___<ruby>食<rt>た</rt></ruby>べる。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ばかり</b>. を tushib ketadi: <ruby>肉<rt>にく</rt></ruby>ばかり<ruby>食<rt>た</rt></ruby>べる. Gapda «bu menga yoqmaydi» degan ohang bor.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>遊<rt>あそ</rt></ruby>んでばかり___ — boʻsh joyga nima tushadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>いる</b>. Toʻliq shakli <ruby>遊<rt>あそ</rt></ruby>んでばかりいる. Bu 〜ている ning ichiga ばかり kirgani, shuning uchun ある emas, いる.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Endigina sotib olingan soat» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>買<rt>か</rt></ruby>ったばかりの<ruby>時計<rt>とけい</rt></ruby></b>. Otni aniqlaganda oradan <b>の</b> tushishini unutmang.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>去年<rt>きょねん</rt></ruby><ruby>結婚<rt>けっこん</rt></ruby>したばかりです — bir yil oʻtgan boʻlsa ham shunday deyish mumkinmi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Mumkin.</b> たばかり soatni emas, gapiruvchining hissini koʻrsatadi. Ish unga hali «yangi» tuyulsa, bir yil ham «endigina» boʻladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Faqat suv ichaman» degan xotirjam gapda だけ yoki ばかり?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>だけ</b> — <ruby>水<rt>みず</rt></ruby>だけ<ruby>飲<rt>の</rt></ruby>みます. Bu tanlov va chegara. ばかり qoʻysangiz, gap «suv ichaveradi-yey» degan bahoga aylanadi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ot + ばかり</b> — faqat shu (ortiqcha koʻp)</li>
  <li><b>〜てばかりいる</b> — faqat shu ishni qiladi</li>
  <li><b>〜たばかりだ</b> — endigina qildi</li>
  <li><b>〜たばかりの + ot</b> — endigina …qilingan …</li>
  <li><b>〜だけ</b> — faqat (quruq chegara)</li>
  <li><b><ruby>文句<rt>もんく</rt></ruby>を<ruby>言<rt>い</rt></ruby>う</b> — nolimoq, eʼtiroz bildirmoq</li>
  <li><b><ruby>済<rt>す</rt></ruby>む</b> — tugamoq, hal boʻlmoq</li>
  <li><b><ruby>生<rt>う</rt></ruby>まれる</b> — tugʻilmoq</li>
  <li><b><ruby>結婚<rt>けっこん</rt></ruby>する</b> — turmush qurmoq</li>
  <li><b>おなかがすく</b> — qorni ochmoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li>Maʼnoni ばかり emas, <b>oldidagi shakl</b> hal qiladi: ot, て yoki た.</li>
    <li><b>〜たばかりの</b> — otdan oldin の shart; ばかり を va が ni siqib chiqaradi.</li>
    <li><b>だけ</b> oʻlchaydi, <b>ばかり</b> baho beradi.</li>
  </ul>
</div>
""",
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-84: 〜ところ (〜るところ, 〜ているところ, 〜たところ)",
        "category": "japanese",
        "order": 84,
        "summary": (
            "«Joy» degan ot vaqt oʻqiga koʻchadi: 辞書形 + ところ — hali "
            "boshlanmagan, 〜ているところ — aynan hozir, 〜たところ — "
            "hozirgina tugagan. Va たところ bilan たばかり orasidagi farq."
        ),
        "stories": ["あと いっぷん"],
        "content": """
<h2>PJ-84: 〜ところ (〜るところ, 〜ているところ, 〜たところ)</h2>

<p>ラノ telefonda. Doʻsti soʻraydi:</p>

<p>ムニラ: <ruby>今<rt>いま</rt></ruby>、どこ。</p>

<p>ラノ: <ruby>今<rt>いま</rt></ruby>、<ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>る<b>ところ</b>。</p>

<p>Savol joy haqida edi, javobda esa ところ turibdi — va bu «joy»
degani emas. «Hozir uydan chiqayotgan <em>paytim</em>» degani.
Rano hali koʻchaga chiqmagan: bir oyogʻi ostonada.</p>

<p><ruby>所<rt>ところ</rt></ruby> aslida «joy» degan ot. Lekin yapon
tili uni <b>vaqt oʻqiga koʻchirgan</b>: xaritadagi nuqta oʻrniga
soatdagi nuqta. Bu darsda siz oʻsha nuqtani uch joyga qoʻyishni
oʻrganasiz — ish boshlanishidan oldin, oʻrtasida va tugaganidan
keyin.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b><ruby>辞書形<rt>じしょけい</rt></ruby> + ところだ</b> bilan «endi qilaman» deysiz</li>
    <li><b>〜ているところだ</b> bilan «aynan hozir qilyapman» deysiz</li>
    <li><b>〜たところだ</b> bilan «hozirgina tugatdim» deysiz</li>
    <li><b>たところ</b> va PJ-83 dagi <b>たばかり</b> ni ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta ish, uchta nuqta</span>
  <span class="pe-chip pe-chip--opt"><ruby>食<rt>た</rt></ruby>べるところ</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v"><ruby>食<rt>た</rt></ruby>べているところ</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s"><ruby>食<rt>た</rt></ruby>べたところ</span>
</div>

<h3>1. Joydan vaqtga</h3>

<p><ruby>所<rt>ところ</rt></ruby> ni siz allaqachon bilasiz:
<ruby>静<rt>しず</rt></ruby>かな<ruby>所<rt>ところ</rt></ruby> — tinch
joy, <ruby>台所<rt>だいどころ</rt></ruby> — oshxona. Bu darsda esa u
gapning oxiriga chiqib, <b>ish qaysi bosqichda ekanini</b>
koʻrsatadi. Yozilishi ham oʻzgaradi: vaqt maʼnosida odatda
hiragana bilan <b>ところ</b> deb yoziladi.</p>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham joy soʻzlari vaqtga koʻchadi.</b>
  «Ishning <em>oxirida</em>», «gapning <em>oʻrtasida</em>»,
  «yoʻlning <em>boshida</em>» — bularning hammasi aslida joy
  soʻzlari, lekin biz ular bilan vaqtni oʻlchaymiz. Yapon tili
  ham xuddi shuni qiladi, faqat bitta soʻz bilan:
  <b>ところ</b> ish oʻqidagi nuqtani koʻrsatadi. Shuning uchun
  uni «payt», «arafa», «hozirgina» deb tarjima qilamiz — lekin
  ichida hamon oʻsha «joy» turadi. Buni bilib turgan odam
  qolipni yodlashi shart emas.</p>
</div>

<h3>2. <ruby>辞書形<rt>じしょけい</rt></ruby> + ところだ — arafa</h3>

<p>Ish <b>hali boshlanmagan</b>. Bir daqiqadan keyin
boshlanadi — ammo hozircha yoʻq.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">これから<span class="pe-hl pe-hl--aux"><ruby>昼<rt>ひる</rt></ruby>ごはんを<ruby>食<rt>た</rt></ruby>べるところ</span>です。</p>
  <p class="pe-ex__uz">Hozir tushlik qilaman (endi oʻtiraman).</p>
  <p class="pe-ex__why">Hali bir luqma ham yemagan. Shuning uchun bu qolip bilan <b>これから</b>, <b><ruby>今<rt>いま</rt></ruby>から</b>, <b>もうすぐ</b> juda tabiiy juftlashadi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha bu «arafa» nima deb aytiladi?</b> «Endi chiqaman
  deganimda», «chiqay deb turganimda», «chiqmoqchi edim» — uchalasi
  ham bitta narsani aytadi: <em>ish hali boshlanmagan, lekin bir
  qadam qolgan</em>. Yaponchada shu holat uchun alohida qolip bor,
  va u kutilmagan joyda turadi — lugʻat shaklidan keyin. Shuning
  uchun <ruby>出<rt>で</rt></ruby>るところ ni «chiqaman» deb emas,
  <b>«chiqay deb turibman»</b> deb tarjima qiling: oʻzbekchada ham
  feʼl kelasi zamonda, lekin maʼno hozirgi daqiqada.</p>
</div>

<h3>3. 〜ているところだ — aynan hozir</h3>

<p>Ish <b>boshlangan va hali tugamagan</b>. PJ-31 dagi
〜ている ga ところ qoʻshilsa, «aynan shu daqiqada, boshqa hech
narsa bilan emas» degan urgʻu paydo boʻladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>今<rt>いま</rt></ruby>、<span class="pe-hl pe-hl--v"><ruby>宿題<rt>しゅくだい</rt></ruby>をしているところ</span>だから、<ruby>後<rt>あと</rt></ruby>で<ruby>電話<rt>でんわ</rt></ruby>する。</p>
  <p class="pe-ex__uz">Hozir uy vazifasini qilyapman, keyinroq qoʻngʻiroq qilaman.</p>
  <p class="pe-ex__why">Oddiy 〜ている ham toʻgʻri boʻlardi. ところ qoʻshilishi «shu topda bandman» degan maʼnoni kuchaytiradi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Bu darsning eng nozik joyi.</b> 〜ているところ
  <em>harakat</em>ga tushadi, <em>holat</em>ga emas. Shuning uchun
  「<ruby>東京<rt>とうきょう</rt></ruby>に<ruby>住<rt>す</rt></ruby>んでいるところです」
  degan gap «hozir yashayapman» degani emas — u
  «<ruby>住<rt>す</rt></ruby>んでいる<ruby>所<rt>ところ</rt></ruby>»,
  yaʼni <b>yashaydigan joy</b> boʻlib oʻqiladi. Yashash, bilish,
  egalik qilish kabi feʼllar bilan ところ ishlatilmaydi:
  <ruby>東京<rt>とうきょう</rt></ruby>に<ruby>住<rt>す</rt></ruby>んでいます
  deng, xolos.</p>
</div>

<h3>4. 〜たところだ — hozirgina</h3>

<p>Ish <b>shu daqiqada tugadi</b>. Chiqqan buguning nafasi hali
sovumagan.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>今<rt>いま</rt></ruby>、<ruby>駅<rt>えき</rt></ruby>に<span class="pe-hl pe-hl--s"><ruby>着<rt>つ</rt></ruby>いたところ</span>です。</p>
  <p class="pe-ex__uz">Hozirgina bekatga yetib keldim.</p>
  <p class="pe-ex__why">Bir-ikki daqiqa oldin. Shuning uchun bu qolip bilan <b><ruby>今<rt>いま</rt></ruby></b> va <b>ちょうど</b> doim yonma-yon yuradi.</p>
</div>

<h3>5. Uchtasi bitta jadvalda</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qolip</th><th>Ish qayerda</th><th>Misol</th><th>Hamrohi</th></tr>
  <tr><td class="pj-stem"><ruby>辞書形<rt>じしょけい</rt></ruby> + ところ</td>
      <td class="pj-uz">hali boshlanmagan</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べるところだ</td>
      <td class="pj-end">これから · もうすぐ</td></tr>
  <tr><td class="pj-stem">〜ている + ところ</td>
      <td class="pj-uz">oʻrtasida</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べているところだ</td>
      <td class="pj-end"><ruby>今<rt>いま</rt></ruby> · ちょうど</td></tr>
  <tr><td class="pj-stem">た-shakli + ところ</td>
      <td class="pj-uz">hozirgina tugadi</td>
      <td class="pj-res"><ruby>食<rt>た</rt></ruby>べたところだ</td>
      <td class="pj-end"><ruby>今<rt>いま</rt></ruby> · ちょうど</td></tr>
</table></div>

<div class="pe-call pe-tip">
  <p><b>Uchtasini eslab qolishning oson yoʻli — kino kadri.</b>
  <ruby>食<rt>た</rt></ruby>べるところ: qoshiq qoʻlda, ogʻiz hali
  yopiq. <ruby>食<rt>た</rt></ruby>べているところ: ogʻiz toʻla,
  yonoq qimirlayapti. <ruby>食<rt>た</rt></ruby>べたところ: qoshiq
  yana likopchada, lab hali artilmagan. Uchala kadr ham
  <b>bir necha soniya</b> ichida — ところ har doim shunday tor
  oynadan qaraydi. Eʼtibor bering: uchalasida ham feʼl
  <em>davom etadigan</em> ish — shuning uchun oʻrtadagi kadr
  umuman boʻlishi mumkin.</p>
</div>

<h3>6. たところ va たばかり — oʻxshaydi, lekin bir xil emas</h3>

<p>PJ-83 da <b>〜たばかり</b> ni koʻrgansiz, va u ham «endigina»
deb tarjima qilinadi. Farq bitta soʻz bilan aytiladi:
<b>たところ soatga qaraydi, たばかり koʻngilga.</b></p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">〜たところ — soat</p>
    <p><ruby>今<rt>いま</rt></ruby><ruby>着<rt>つ</rt></ruby>いたところです。</p>
    <p>Bir-ikki daqiqa oldin. Uzoqroq vaqt bilan ishlatilmaydi:
    <ruby>先月<rt>せんげつ</rt></ruby><ruby>着<rt>つ</rt></ruby>いたところです
    — notoʻgʻri.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">〜たばかり — his</p>
    <p><ruby>先月<rt>せんげつ</rt></ruby><ruby>着<rt>つ</rt></ruby>いたばかりです。</p>
    <p>Bir oy oʻtgan, lekin gapiruvchi uchun hali «yangi».
    Qisqa vaqt bilan ham ishlaydi:
    <ruby>今<rt>いま</rt></ruby><ruby>着<rt>つ</rt></ruby>いたばかりです
    — toʻgʻri.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekcha «hozirgina» va «endigina» aynan shu ikkiga
  boʻlinadi.</b> «Hozirgina yetib keldim» — soat boʻyicha hozir,
  besh daqiqa oldin ham desa boʻlmaydi. «Endigina koʻchib
  kelganmiz» — bir yil boʻlgandir, lekin his hali yangi. Ikkala
  soʻz ham bizda bor, faqat biz ularni oʻylab tanlamaymiz.
  Yaponcha esa tanlashga majbur qiladi:
  <b><ruby>今<rt>いま</rt></ruby>〜たところ</b> — hozirgina,
  <b>〜たばかり</b> — endigina. Tarjima qilishdan oldin oʻzbekcha
  qaysi soʻzni aytganingizni eshiting, keyin oʻshanisini
  qoʻying — adashmaysiz.</p>
</div>

<h3>7. ところ + qoʻshimcha: ish uzilganda</h3>

<p>ところ ot boʻlgani uchun undan keyin qoʻshimcha ham kelishi
mumkin. Va u kelganda gap doim bitta narsani aytadi:
<b>ish aynan shu paytda uzildi</b>.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Qoʻshimcha</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">ところに / ところへ</td>
      <td class="pj-res"><ruby>出<rt>で</rt></ruby>かけるところに<ruby>電話<rt>でんわ</rt></ruby>が<ruby>来<rt>き</rt></ruby>た</td>
      <td class="pj-uz">chiqayotganimda telefon keldi</td></tr>
  <tr><td class="pj-stem">ところを</td>
      <td class="pj-res"><ruby>寝<rt>ね</rt></ruby>ているところを<ruby>見<rt>み</rt></ruby>られた</td>
      <td class="pj-uz">uxlayotganimda koʻrib qolishdi</td></tr>
  <tr><td class="pj-stem">ところで</td>
      <td class="pj-res"><ruby>話<rt>はな</rt></ruby>が<ruby>終<rt>お</rt></ruby>わったところで<ruby>帰<rt>かえ</rt></ruby>った</td>
      <td class="pj-uz">gap tugagan payt qaytdim</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--aux"><ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>るところ</span>に<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した。</p>
  <p class="pe-ex__uz">Uydan chiqayotganimda yomgʻir yogʻa boshladi.</p>
  <p class="pe-ex__why">ところに — «aynan oʻsha paytda» degan urgʻu beradi. PJ-49 dagi <b>とき</b> kengroq oynadan qaraydi, ところに esa bitta daqiqani koʻrsatadi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">所</span>
    <span class="pj-kanji__uz">joy</span>
    <span class="pj-kanji__on">オン: ショ</span>
    <span class="pj-kanji__kun">KUN: ところ</span>
    <span class="pj-kanji__note">台所 (だいどころ) — oshxona · 近所 (きんじょ) — qoʻshnichilik · 場所 (ばしょ) — joy</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">場</span>
    <span class="pj-kanji__uz">maydon, joy</span>
    <span class="pj-kanji__on">オン: ジョウ</span>
    <span class="pj-kanji__kun">KUN: ば</span>
    <span class="pj-kanji__note">場合 (ばあい) — holat · 会場 (かいじょう) — zal, maydon</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">着</span>
    <span class="pj-kanji__uz">yetib kelmoq; kiymoq</span>
    <span class="pj-kanji__on">オン: チャク</span>
    <span class="pj-kanji__kun">KUN: つ(く)・き(る)</span>
    <span class="pj-kanji__note">到着 (とうちゃく) — yetib kelish · 着物 (きもの) — kimono</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>今<rt>いま</rt></ruby>、<ruby>食<rt>た</rt></ruby>べるところです («hozir ovqatlanyapman» maʼnosida)</p>
  <p class="pe-fix__good">✓ <ruby>今<rt>いま</rt></ruby>、<ruby>食<rt>た</rt></ruby>べて<b>いる</b>ところです — «oʻrtasida» uchun 〜ている kerak; <ruby>辞書形<rt>じしょけい</rt></ruby> esa hali boshlanmaganini bildiradi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>東京<rt>とうきょう</rt></ruby>に<ruby>住<rt>す</rt></ruby>んでいるところです («hozir yashayapman» maʼnosida)</p>
  <p class="pe-fix__good">✓ <ruby>東京<rt>とうきょう</rt></ruby>に<ruby>住<rt>す</rt></ruby>んでいます — ところ holat feʼliga tushmaydi, aks holda «yashaydigan joy» boʻlib oʻqiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>先月<rt>せんげつ</rt></ruby><ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>たところです</p>
  <p class="pe-fix__good">✓ <ruby>先月<rt>せんげつ</rt></ruby><ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>た<b>ばかり</b>です — uzoqroq vaqt uchun ばかり, たところ faqat bir necha daqiqa.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>出<rt>で</rt></ruby>かけるところ<ruby>電話<rt>でんわ</rt></ruby>が<ruby>来<rt>き</rt></ruby>た</p>
  <p class="pe-fix__good">✓ <ruby>出<rt>で</rt></ruby>かけるところ<b>に</b><ruby>電話<rt>でんわ</rt></ruby>が<ruby>来<rt>き</rt></ruby>た — ところ ot, shuning uchun qoʻshimchasiz qolmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ちょうど<ruby>今<rt>いま</rt></ruby>、<ruby>出<rt>で</rt></ruby>るところです («hozirgina chiqdim» maʼnosida)</p>
  <p class="pe-fix__good">✓ ちょうど<ruby>今<rt>いま</rt></ruby>、<ruby>出<rt>で</rt></ruby><b>た</b>ところです — ちょうど<ruby>今<rt>いま</rt></ruby> «hozirgina» degani, unga た-shakli kerak; lugʻat shakli esa hali chiqmaganini bildiradi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Hozir uydan chiqmoqchiman, hali chiqmadim» — qaysi shakl?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>家<rt>いえ</rt></ruby>を<ruby>出<rt>で</rt></ruby>るところです</b>. <ruby>辞書形<rt>じしょけい</rt></ruby> ish hali boshlanmaganini koʻrsatadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. Boʻsh joyni toʻldiring: <ruby>今<rt>いま</rt></ruby>、ごはんを<ruby>作<rt>つく</rt></ruby>___ところです。 (aynan hozir pishiryapman)</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>って いる</b> — toʻliq gap: <ruby>今<rt>いま</rt></ruby>、ごはんを<ruby>作<rt>つく</rt></ruby>っているところです。 て-shakli + いる + ところ.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. <ruby>東京<rt>とうきょう</rt></ruby>に<ruby>住<rt>す</rt></ruby>んでいるところです — nega bu gap gʻalati?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Chunki ところ holat feʼliga tushmaydi: gap «Tokioda yashayotgan paytim» emas, <b>«yashaydigan joyim»</b> boʻlib oʻqiladi. Toʻgʻrisi — <ruby>東京<rt>とうきょう</rt></ruby>に<ruby>住<rt>す</rt></ruby>んでいます.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>先月<rt>せんげつ</rt></ruby><ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>ました — «endigina keldim» deyish uchun ところ yoki ばかり?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ばかり</b>: <ruby>先月<rt>せんげつ</rt></ruby><ruby>日本<rt>にほん</rt></ruby>に<ruby>来<rt>き</rt></ruby>たばかりです. たところ faqat bir necha daqiqaga toʻgʻri keladi, bir oyga emas.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. «Chiqayotganimda telefon keldi» — boʻsh joyga qaysi qoʻshimcha? <ruby>出<rt>で</rt></ruby>かけるところ___<ruby>電話<rt>でんわ</rt></ruby>が<ruby>来<rt>き</rt></ruby>た。</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>に</b> — ところに «aynan oʻsha paytda uzildi» degan maʼnoni beradi. ところへ ham boʻladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b><ruby>辞書形<rt>じしょけい</rt></ruby> + ところだ</b> — endi qiladi, hali boshlamagan</li>
  <li><b>〜ているところだ</b> — aynan hozir qilyapti</li>
  <li><b>〜たところだ</b> — hozirgina tugatdi</li>
  <li><b>〜ところに / 〜ところへ</b> — aynan oʻsha paytda</li>
  <li><b>ちょうど</b> — roppa-rosa, aynan</li>
  <li><b>これから</b> — bundan keyin, endi</li>
  <li><b><ruby>着<rt>つ</rt></ruby>く</b> — yetib kelmoq</li>
  <li><b><ruby>出<rt>で</rt></ruby>かける</b> — koʻchaga chiqmoq</li>
  <li><b><ruby>場所<rt>ばしょ</rt></ruby></b> — joy</li>
  <li><b><ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>す</b> — yogʻa boshlamoq</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><ruby>辞書形<rt>じしょけい</rt></ruby> — arafa, <b>ている</b> — oʻrtasi, <b>た</b> — hozirgina.</li>
    <li>ところ <b>holat</b> feʼliga tushmaydi — <ruby>住<rt>す</rt></ruby>んでいるところ «yashaydigan joy» boʻlib oʻqiladi.</li>
    <li><b>たところ</b> soatga, <b>たばかり</b> koʻngilga qaraydi.</li>
  </ul>
</div>
""",
    },
]
