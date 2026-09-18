# -*- coding: utf-8 -*-
"""Prime Japanese — PJ-94, PJ-95, PJ-96: rad etish, vaqt aniqligi va yozma uslub.

Blok F ning oxirgi uchdan biri boshlanadi.
    PJ-94 — どころか va ばかりか: ikkalasi ham ikkita narsani
            bogʻlaydi, lekin biri kutilganni RAD ETADI, ikkinchisi
            ustiga QOʻSHADI. Oʻzbekchada «u yoqda tursin» va
            «ustiga-ustak» — ikkovi ham tayyor jufti bor.
    PJ-95 — たとたん, 次第, か〜ないかのうちに: uchala qolip ham
            «…ishi bilan» deb tarjima qilinadi, lekin yaponchada
            ularni ZAMON ajratadi — たとたん faqat oʻtgan, 次第
            faqat kelasi zamon bilan keladi.
    PJ-96 — だ・である体: kursning birinchi USLUB darsi. Grammatika
            emas, registr. Bu yerdan keyin oʻquvchi gazeta, insho va
            maqola yaponchasini tanib oladi.

⚠️ PJ-94 ning eng katta tuzogʻi — どころか ni «…dan tashqari» deb
tarjima qilish. U aynan TESKARISI: «…dan tashqari» qoʻshadi,
どころか esa rad etadi. Qoʻshadigani — ばかりか.

⚠️ PJ-95 da uchala qolipning ulanishi boshqa-boshqa:
た-shakli + とたん · ます-oʻzagi (yoki ot) + 次第 ·
lugʻat shakli + か + ない-shakli + かのうちに.
Va 次第 dan keyin OʻTGAN ZAMON boʻlmaydi — bu darsning yarmi shu.

⚠️ PJ-96 uslub darsi, shuning uchun unda «toʻgʻri/notoʻgʻri» emas,
«qayerda» degan savol bor. Lekin bitta qatʼiy qoida bor: bitta matn
ichida registr aralashmaydi.

⚠️ Kursda hali berilmagan narsalar bu batchda ham yoʻq:
拝啓・敬具 va rasmiy xat qoliplari (PJ-97), 四字熟語 (PJ-98),
和語・漢語・外来語 atamalari (PJ-99).

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_japanese_94_96.py --author=prime
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
        "title": "PJ-94: 〜どころか va 〜ばかりか",
        "category": "japanese",
        "order": 94,
        "summary": (
            "Ikkita qolip, ikkita teskari ish: どころか kutilganni rad "
            "etadi («oson u yoqda tursin»), ばかりか esa ustiga qoʻshadi "
            "(«ustiga-ustak»). Va どころではない — «hozir buning payti emas»."
        ),
        "stories": ["にがてどころか"],
        "content": """
<h2>PJ-94: 〜どころか va 〜ばかりか</h2>

<p>Doʻstingiz soʻradi: «Imtihon oson boʻldimi?» Siz javob bermoqchisiz:
«Oson? <em>Oson u yoqda tursin</em> — birinchi savolni ham tushunmadim».
Yaponchada bu butun ohang bitta qoʻshimchaga sigʻadi: <b>どころか</b>.</p>

<p>Uning yonida esa teskarisi turadi. «Yomgʻir yogʻdi, <em>ustiga-ustak</em>
shamol ham kuchaydi» — bu <b>ばかりか</b>. Ikkala qolip ham ikkita narsani
bogʻlaydi, lekin biri kutilganni <b>rad etadi</b>, ikkinchisi ustiga
<b>qoʻshadi</b>. Shuning uchun ular bitta darsda.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>〜どころか</b> bilan «… u yoqda tursin» deysiz</li>
    <li>Uning ikkinchi ishini — «aksincha» maʼnosini ajratasiz</li>
    <li><b>〜どころではない</b> bilan «hozir buning payti emas» deysiz</li>
    <li><b>〜ばかりか</b> bilan kutilmagan qoʻshimchani aytasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Rad etish</span>
  <span class="pe-chip pe-chip--s">A</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">どころか</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--neg">B — kutilganning aksi</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qoʻshish</span>
  <span class="pe-chip pe-chip--s">A</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">ばかりか</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">B + も — ustiga-ustak</span>
</div>

<h3>1. 〜どころか — «… u yoqda tursin»</h3>

<p>Birinchi ishi eng koʻp uchraydi: <b>A ni aytish ham ortiqcha, chunki
undan ham pastroq/yuqoriroq narsa haqiqat</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><span class="pe-hl pe-hl--s"><ruby>漢字<rt>かんじ</rt></ruby>どころか</span>、ひらがな<span class="pe-hl pe-hl--neg">も</span><ruby>読<rt>よ</rt></ruby>めない。</p>
  <p class="pe-ex__uz">Kanji u yoqda tursin, hiraganani ham oʻqiy olmaydi.</p>
  <p class="pe-ex__why">Kanji — qiyinrogʻi. «Uni qoʻying» deb, undan osonrogʻiga oʻtyapmiz. Ikkinchi qismda deyarli doim <b>も</b> turadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>一<rt>いち</rt></ruby><ruby>時間<rt>じかん</rt></ruby>どころか、<ruby>三<rt>さん</rt></ruby><ruby>時間<rt>じかん</rt></ruby>も<ruby>待<rt>ま</rt></ruby>った。</p>
  <p class="pe-ex__uz">Bir soat u yoqda tursin, uch soat kutdim.</p>
  <p class="pe-ex__why">Bu yerda yoʻnalish teskari — kichikdan kattaga. どころか ikkala tomonga ham ishlaydi; muhimi, ikkinchi qism <b>kuchliroq</b> boʻlsin.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu qolipning tayyor jufti bor va u aynan shu
  joyda turadi.</b> «Kanji <em>u yoqda tursin</em>, hiraganani ham
  oʻqiy olmaydi» — qarang, «u yoqda tursin» oʻzbekchada ham otdan
  <em>keyin</em> keladi, xuddi どころか kabi. Ikki tilda bir xil
  slotda turgan ibora kam uchraydi, shuning uchun buni yodda
  tuting: <b>どころか = «u yoqda tursin»</b>. Tarjima qilganingizda
  soʻz tartibini oʻzgartirishingiz ham shart emas.</p>
</div>

<h3>2. Ikkinchi ishi — «aksincha»</h3>

<p>Sifat yoki feʼldan keyin kelsa, どころか koʻpincha butun gapni
<b>teskarisiga oʻgiradi</b>: «kutilgani A edi, aslida esa B».</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>人<rt>ひと</rt></ruby>が<span class="pe-hl pe-hl--v"><ruby>減<rt>へ</rt></ruby>るどころか</span>、<ruby>去年<rt>きょねん</rt></ruby>より<span class="pe-hl pe-hl--s"><ruby>増<rt>ふ</rt></ruby>えている</span>。</p>
  <p class="pe-ex__uz">Odam kamayish u yoqda tursin, oʻtgan yilgidan koʻra koʻpaymoqda.</p>
  <p class="pe-ex__why">Kutilgan narsa — kamayish. Haqiqat — koʻpayish. どころか shu ikki qarama-qarshilikni bir gapda ushlab turadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja">その<ruby>店<rt>みせ</rt></ruby>は<ruby>安<rt>やす</rt></ruby>いどころか、とても<ruby>高<rt>たか</rt></ruby>かった。</p>
  <p class="pe-ex__uz">U doʻkon arzon boʻlish u yoqda tursin, juda qimmat edi.</p>
  <p class="pe-ex__why">い-sifat oʻz shaklida turadi: <b><ruby>安<rt>やす</rt></ruby>い</b> + どころか. Hech narsa tushmaydi.</p>
</div>

<h3>3. Ulanish jadvali</h3>

<p>Ikkala qolip ham sodda shaklga ulanadi, lekin <b>な</b>-sifat va
<b>ot</b>da ular bir-biridan farq qiladi. Buni bir marta koʻrib
qoʻying:</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Soʻz turi</th><th>〜どころか</th><th>〜ばかりか</th><th>Izoh</th></tr>
  <tr><td class="pj-stem">ot</td>
      <td class="pj-res"><ruby>漢字<rt>かんじ</rt></ruby>どころか</td>
      <td class="pj-res"><ruby>英語<rt>えいご</rt></ruby>ばかりか</td>
      <td class="pj-uz">ikkalasi ham otga toʻgʻridan-toʻgʻri</td></tr>
  <tr><td class="pj-stem">い-sifat</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>いどころか</td>
      <td class="pj-res"><ruby>安<rt>やす</rt></ruby>いばかりか</td>
      <td class="pj-uz">い oʻz joyida qoladi</td></tr>
  <tr><td class="pj-stem">な-sifat</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かどころか</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>か<b>な</b>ばかりか</td>
      <td class="pj-uz">bu yerda farq bor — ばかりか <b>な</b> talab qiladi</td></tr>
  <tr><td class="pj-stem">feʼl</td>
      <td class="pj-res"><ruby>減<rt>へ</rt></ruby>るどころか</td>
      <td class="pj-res"><ruby>降<rt>ふ</rt></ruby>ったばかりか</td>
      <td class="pj-uz">sodda shakl; zamon erkin</td></tr>
</table></div>

<div class="pe-call pe-rule">
  <p><b>Bitta qatorni yodlang: <ruby>静<rt>しず</rt></ruby>か<b>どころか</b> lekin
  <ruby>静<rt>しず</rt></ruby>か<b>な</b>ばかりか.</b> どころか な ni
  tushiradi, ばかりか esa saqlaydi. Qolgan hamma joyda ikkalasi bir xil
  ulanadi, shuning uchun imtihonda な-sifat koʻrsangiz darrov shu
  qatorni eslang.</p>
</div>

<h3>4. 〜どころではない — «hozir buning payti emas»</h3>

<p>どころ ning uchinchi ishi alohida qolip boʻlib qotgan:
<b>どころではない</b> (yumshogʻi — <b>どころじゃない</b>). Maʼnosi:
<em>«vaziyat shunday ogʻirki, bu haqda gapirish ham mumkin emas»</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>来週<rt>らいしゅう</rt></ruby><ruby>試験<rt>しけん</rt></ruby>があるから、<span class="pe-hl pe-hl--neg"><ruby>旅行<rt>りょこう</rt></ruby>どころではない</span>。</p>
  <p class="pe-ex__uz">Keyingi hafta imtihon bor, sayohat qayoqda.</p>
  <p class="pe-ex__why">Bu yerda «sayohat yomon» deyilmayapti — «hozir uning payti emas» deyilyapti. Farqi shu.</p>
</div>

<div class="pj-joshi">
  <span class="pj-joshi__n"><ruby>今<rt>いま</rt></ruby></span>
  <span class="pj-joshi__p">は<small>MAVZU</small></span>
  <span class="pj-joshi__n"><ruby>昼<rt>ひる</rt></ruby>ごはん</span>
  <span class="pj-joshi__v">どころではない</span>
  <span class="pj-joshi__uz">Hozir tushlik qayoqda. (shunchalik bandmiz)</span>
</div>

<div class="pe-call pe-tip">
  <p><b>どころではない ni ikkita oʻzbekcha ibora aniq ushlaydi:</b>
  «… qayoqda» va «… ning payti emas». «Dam olish qayoqda»,
  «hozir kinoning payti emas» — ikkovi ham shu qolip. Oddiy
  inkordan farqini his qiling: <b>ではない</b> «bu emas» deydi,
  <b>どころではない</b> esa «bu haqda soʻrashning oʻzi ortiqcha»
  deydi.</p>
</div>

<h3>5. 〜ばかりか — «ustiga-ustak»</h3>

<p>ばかりか A ni rad etmaydi — A haqiqat, va ustiga <b>kutilmagan B
ham</b> qoʻshiladi. Ikkinchi qismda deyarli doim <b>も</b> turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">パリさんは<span class="pe-hl pe-hl--s"><ruby>英語<rt>えいご</rt></ruby>ばかりか</span>、<ruby>日本語<rt>にほんご</rt></ruby><span class="pe-hl pe-hl--v">も</span><ruby>話<rt>はな</rt></ruby>せる。</p>
  <p class="pe-ex__uz">Pari ingliz tilidan tashqari, yapon tilida ham gapira oladi.</p>
  <p class="pe-ex__why">Diqqat: bu yerda ingliz tili <b>inkor qilinmayapti</b>. U bor, va ustiga yana bittasi bor. どころか boʻlsa maʼno teskari boʻlib ketardi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>ったばかりか、<ruby>風<rt>かぜ</rt></ruby>も<ruby>強<rt>つよ</rt></ruby>くなった。</p>
  <p class="pe-ex__uz">Yomgʻir yogʻdi, ustiga-ustak shamol ham kuchaydi.</p>
  <p class="pe-ex__why">Yomon narsa ustiga yana yomonroq. ばかりか koʻpincha shunday — qoʻshimcha B kutilmagan va kuchliroq boʻladi.</p>
</div>

<h3>6. ばかりか va だけでなく</h3>

<p>Ikkalasi ham «faqat … emas, … ham» deb tarjima qilinadi. Farq
ohangda:</p>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">だけでなく — quruq qoʻshish</p>
    <p><ruby>英語<rt>えいご</rt></ruby>だけでなく、<ruby>日本語<rt>にほんご</rt></ruby>も<ruby>話<rt>はな</rt></ruby>せる。</p>
    <p>Ikkita fakt. Hayron boʻlish yoʻq, baho yoʻq. Rasmiy matnda ham, gapda ham erkin.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">ばかりか — hayratli qoʻshish</p>
    <p><ruby>英語<rt>えいご</rt></ruby>ばかりか、<ruby>日本語<rt>にほんご</rt></ruby>も<ruby>話<rt>はな</rt></ruby>せる。</p>
    <p>«Buni ham deysizmi!» Gapiruvchi taajjublanmoqda. Koʻproq yozma tilda.</p></div>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada bu farqni ikkita ibora koʻtaradi.</b>
  «Nafaqat ingliz tilida, balki yapon tilida <em>ham</em>» —
  bu <b>だけでなく</b>: xotirjam, rasmiy, hisobotga yaraydi.
  «Ingliz tilida gapiradi, <em>ustiga-ustak</em> yaponchani ham
  biladi» — bu <b>ばかりか</b>: bu yerda gapiruvchining hayrati
  eshitilib turibdi. Yozayotganda oʻzingizdan soʻrang:
  <em>«men bu yerda hayron boʻlyapmanmi yoki shunchaki
  sanayapmanmi?»</em> Hayron boʻlsangiz — ばかりか. Sanasangiz —
  だけでなく.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">増</span>
    <span class="pj-kanji__uz">koʻpaymoq, ortmoq</span>
    <span class="pj-kanji__on">オン: ゾウ</span>
    <span class="pj-kanji__kun">KUN: ふ(える)・ま(す)</span>
    <span class="pj-kanji__note">増える (ふえる) — koʻpaymoq · 増加 (ぞうか) — oʻsish</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">減</span>
    <span class="pj-kanji__uz">kamaymoq, qisqarmoq</span>
    <span class="pj-kanji__on">オン: ゲン</span>
    <span class="pj-kanji__kun">KUN: へ(る)・へ(らす)</span>
    <span class="pj-kanji__note">減る (へる) — kamaymoq · 減少 (げんしょう) — kamayish</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">逆</span>
    <span class="pj-kanji__uz">teskari, aks</span>
    <span class="pj-kanji__on">オン: ギャク</span>
    <span class="pj-kanji__kun">KUN: さか(さ)</span>
    <span class="pj-kanji__note">逆 (ぎゃく) — teskarisi · 逆に (ぎゃくに) — aksincha</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <p><b>Bir tuzoq: どころか ni «…dan tashqari» deb tarjima qilmang.</b>
  Bu ikkovi bir-birining <em>aynan teskarisi</em>. «Kanjidan tashqari
  hiraganani ham oʻqiydi» — bu ikkalasini ham biladi degani, va u
  yaponchada <b>ばかりか</b>. «Kanji u yoqda tursin, hiraganani ham
  oʻqiy olmaydi» — bu ikkalasini ham bilmaydi degani, va u
  <b>どころか</b>. Oʻzbek oʻquvchisi koʻpincha どころ ni «joy, oʻrin»
  degan otdan chiqarib «… oʻrniga» deb oʻqiydi va maʼnoni teskari
  tushunadi. Tekshirish usuli oddiy: ikkinchi qismga qarang. U
  birinchisidan <b>kuchliroq va kutilmaganroq</b> boʻlsa —
  どころか.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>漢字<rt>かんじ</rt></ruby>どころか、ひらがな<b>が</b><ruby>読<rt>よ</rt></ruby>めない</p>
  <p class="pe-fix__good">✓ <ruby>漢字<rt>かんじ</rt></ruby>どころか、ひらがな<b>も</b><ruby>読<rt>よ</rt></ruby>めない — ikkinchi qismda <b>も</b> boʻlishi deyarli shart.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>静<rt>しず</rt></ruby>か<b>な</b>どころか、うるさかった</p>
  <p class="pe-fix__good">✓ <ruby>静<rt>しず</rt></ruby>かどころか — どころか <b>な</b> ni tushiradi. ばかりか esa aksincha, uni saqlaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>英語<rt>えいご</rt></ruby>どころか、<ruby>日本語<rt>にほんご</rt></ruby>も<ruby>話<rt>はな</rt></ruby>せる (ikkalasini ham biladi demoqchi edik)</p>
  <p class="pe-fix__good">✓ <ruby>英語<rt>えいご</rt></ruby><b>ばかりか</b> — qoʻshish kerak boʻlsa ばかりか. どころか rad etadi, shuning uchun bu gap kulgili chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>今<rt>いま</rt></ruby>は<ruby>旅行<rt>りょこう</rt></ruby>どころ<b>じゃありません</b>でした</p>
  <p class="pe-fix__good">✓ <ruby>旅行<rt>りょこう</rt></ruby>どころ<b>ではありませんでした</b> — qolip <b>どころではない</b>; oʻtgan zamon uning oxiriga qoʻyiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>る<b>ばかり</b>、<ruby>風<rt>かぜ</rt></ruby>も<ruby>強<rt>つよ</rt></ruby>くなった</p>
  <p class="pe-fix__good">✓ <ruby>降<rt>ふ</rt></ruby>った<b>ばかりか</b> — <b>か</b> siz bu PJ-83 dagi boshqa qolip boʻlib qoladi («endigina yogʻdi»).</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Kanji u yoqda tursin, hiraganani ham oʻqiy olmaydi» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>漢字<rt>かんじ</rt></ruby>どころか、ひらがなも<ruby>読<rt>よ</rt></ruby>めない</b>. Ikkinchi qismdagi <b>も</b> — qolipning bir boʻlagi, uni tushirib qoldirmang.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>静<rt>しず</rt></ruby>か___どころか va <ruby>静<rt>しず</rt></ruby>か___ばかりか — boʻsh joylarga nima tushadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p>Birinchisida <b>hech narsa</b>, ikkinchisida <b>な</b>: <ruby>静<rt>しず</rt></ruby>かどころか / <ruby>静<rt>しず</rt></ruby>か<b>な</b>ばかりか. Bu ikkovining yagona ulanish farqi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Pari ingliz tilidan tashqari yapon tilida ham gapiradi» — どころか yoki ばかりか?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ばかりか</b>: パリさんは<ruby>英語<rt>えいご</rt></ruby>ばかりか、<ruby>日本語<rt>にほんご</rt></ruby>も<ruby>話<rt>はな</rt></ruby>せる。Bu yerda ingliz tili <b>rad etilmayapti</b>, ustiga yana bittasi qoʻshilyapti.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. «Keyingi hafta imtihon bor, sayohat qayoqda» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>来週<rt>らいしゅう</rt></ruby><ruby>試験<rt>しけん</rt></ruby>があるから、<ruby>旅行<rt>りょこう</rt></ruby>どころではない</b>. «Sayohat yomon» emas — «hozir uning payti emas».</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>人<rt>ひと</rt></ruby>が<ruby>減<rt>へ</rt></ruby>るどころか、___ — davomida nima kelishi mantiqan toʻgʻri?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>増<rt>ふ</rt></ruby>えている</b> kabi <b>teskari</b> natija. どころか dan keyin kutilganning aksi keladi; «<ruby>少<rt>すこ</rt></ruby>し<ruby>減<rt>へ</rt></ruby>った» desangiz qolip buziladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. だけでなく va ばかりか — qaysi biri hisobotga, qaysi biri hayratli gapga toʻgʻri keladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>だけでなく</b> — hisobot, quruq sanash. <b>ばかりか</b> — hayrat, «ustiga-ustak». Maʼno bir xil, ohang boshqa.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜どころか</b> — … u yoqda tursin; aksincha</li>
  <li><b>〜どころではない</b> — … qayoqda, uning payti emas</li>
  <li><b>〜ばかりか</b> — ustiga-ustak, … ham</li>
  <li><b>〜だけでなく</b> — nafaqat …, balki … ham</li>
  <li><b><ruby>増<rt>ふ</rt></ruby>える</b> — koʻpaymoq</li>
  <li><b><ruby>減<rt>へ</rt></ruby>る</b> — kamaymoq</li>
  <li><b><ruby>逆<rt>ぎゃく</rt></ruby>に</b> — aksincha</li>
  <li><b><ruby>旅行<rt>りょこう</rt></ruby></b> — sayohat</li>
  <li><b><ruby>強<rt>つよ</rt></ruby>くなる</b> — kuchaymoq</li>
  <li><b>とても</b> — juda</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>どころか</b> rad etadi («u yoqda tursin»), <b>ばかりか</b> qoʻshadi («ustiga-ustak»).</li>
    <li>Ikkinchi qismda <b>も</b> — ikkala qolipning ham odati.</li>
    <li><ruby>静<rt>しず</rt></ruby>か<b>どころか</b> lekin <ruby>静<rt>しず</rt></ruby>か<b>な</b>ばかりか.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-95: 〜たとたん, 〜次第, 〜か〜ないかのうちに — vaqt aniqligi",
        "category": "japanese",
        "order": 95,
        "summary": (
            "Uchala qolip ham «…ishi bilan» deb tarjima qilinadi, lekin "
            "yaponchada ularni zamon ajratadi: たとたん — faqat oʻtgan va "
            "kutilmagan, 次第 — faqat kelasi va rejali, か〜ないかのうちに "
            "— «…ar-etmas»."
        ),
        "stories": ["ホイッスルが なったとたん"],
        "content": """
<h2>PJ-95: 〜たとたん, 〜<ruby>次第<rt>しだい</rt></ruby>, 〜か〜ないかのうちに — vaqt aniqligi</h2>

<p>Oʻzbekchada bitta qoʻshimcha uchchalasining ham ishini bajaradi:
<em>«…ishi bilan»</em>. «Eshikni ochishim bilan mushuk otilib chiqdi»,
«Vokzalga yetishim bilan qoʻngʻiroq qilaman» — bir xil ibora, ikki xil
vaziyat. Yapon tili esa bu ikkovini <b>ikkita boshqa-boshqa qolipga</b>
ajratadi, va ajratishning oʻlchovi — <b>zamon</b>.</p>

<p>Shuning uchun bu darsda savol «qaysi qolip toʻgʻri?» emas. Savol —
<em>«gapning oxiri oʻtgan zamondami yoki kelasi zamondami?»</em>
Javobni topsangiz, qolip oʻzi kelib turadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>〜たとたん</b> bilan kutilmagan, oʻtgan voqeani aytasiz</li>
    <li><b>〜<ruby>次第<rt>しだい</rt></ruby></b> bilan rejali, kelasi ishni aytasiz</li>
    <li><b>〜か〜ないかのうちに</b> bilan «…ar-etmas» deysiz</li>
    <li>Uchalasini <b>zamon</b> boʻyicha bir soniyada ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kutilmagan, oʻtgan</span>
  <span class="pe-chip pe-chip--v">feʼl た-shakli</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">とたん(に)</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">natija — OʻTGAN zamon</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Rejali, kelasi</span>
  <span class="pe-chip pe-chip--v">ます-oʻzagi</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux"><ruby>次第<rt>しだい</rt></ruby></span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">niyat, iltimos — KELASI zamon</span>
</div>

<h3>1. 〜たとたん — «…ishi bilanoq» (oʻtgan, kutilmagan)</h3>

<p>Feʼlning <b>た-shakli</b> ustiga <b>とたん</b> qoʻyiladi. Ikki voqea
orasida vaqt deyarli yoʻq, va ikkinchisi <b>kutilmagan</b> boʻladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">ドアを<span class="pe-hl pe-hl--v"><ruby>開<rt>あ</rt></ruby>けたとたん</span>、<ruby>猫<rt>ねこ</rt></ruby>が<span class="pe-hl pe-hl--s"><ruby>飛<rt>と</rt></ruby>び<ruby>出<rt>だ</rt></ruby>した</span>。</p>
  <p class="pe-ex__uz">Eshikni ochishim bilanoq mushuk otilib chiqdi.</p>
  <p class="pe-ex__why">Ikkinchi qism <b>oʻtgan zamonda</b> va <b>kutilmagan</b>. Ikkalasi ham shart.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>立<rt>た</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>がったとたん、<ruby>目<rt>め</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>が<ruby>暗<rt>くら</rt></ruby>くなった。</p>
  <p class="pe-ex__uz">Oʻrnimdan turishim bilanoq koʻz oldim qorongʻilashdi.</p>
  <p class="pe-ex__why">Bu ham kutilmagan va gapiruvchining ixtiyorida emas — とたん uchun ideal gap.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>とたん ning uchta taqiqi bor, va ular imtihonning oʻzi.</b>
  Undan keyin <b>buyruq</b> («… <ruby>行<rt>い</rt></ruby>け»),
  <b>iltimos</b> («…てください»), <b>niyat</b> («…ましょう», «…つもりだ»)
  kela olmaydi. Sababi bitta: とたん <em>kutilmagan</em> voqeani
  aytadi, buyruq va niyat esa — <em>rejalashtirilgan</em>. Bir gapda
  ikkovi sigʻmaydi. Shuning uchun «<ruby>着<rt>つ</rt></ruby>いたとたん、
  <ruby>電話<rt>でんわ</rt></ruby>してください» — xato. Bunda <ruby>次第<rt>しだい</rt></ruby>
  kerak.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchadagi jufti — «…ishi bilanoq» va «…gani hamono».</b>
  Eʼtibor bering: biz ham bu iborani deyarli har doim <em>oʻtgan
  zamon</em> voqeasi haqida ishlatamiz. «Eshikni ochishi bilanoq
  mushuk otilib chiqdi» — tabiiy. «Eshikni ochishi bilanoq
  qoʻngʻiroq qiling» — oʻzbekchada ham gʻalati eshitiladi, toʻgʻrimi?
  Demak, qoidani yodlash shart emas: <em>oʻzbekcha tarjimasi
  gʻalati boʻlsa, yaponchasi ham xato</em>. Bu ikki tilning kamdan
  kam tasodifiy mos kelgan joylaridan biri — foydalaning.</p>
</div>

<h3>2. 〜<ruby>次第<rt>しだい</rt></ruby> — «…ishim bilan, … qilaman» (kelasi, rejali)</h3>

<p>Ulanishi boshqa: <b>ます-oʻzagi</b> (yaʼni <ruby>着<rt>つ</rt></ruby>きます →
<ruby>着<rt>つ</rt></ruby>き) yoki <b>ot</b> + <ruby>次第<rt>しだい</rt></ruby>. Va gapning oxiri
<b>hech qachon oʻtgan zamonda boʻlmaydi</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>駅<rt>えき</rt></ruby>に<span class="pe-hl pe-hl--v"><ruby>着<rt>つ</rt></ruby>き<ruby>次第<rt>しだい</rt></ruby></span>、<ruby>電話<rt>でんわ</rt></ruby>します。</p>
  <p class="pe-ex__uz">Vokzalga yetishim bilan qoʻngʻiroq qilaman.</p>
  <p class="pe-ex__why"><ruby>着<rt>つ</rt></ruby>きます ning ます qismi tushadi, oʻzak qoladi: <b><ruby>着<rt>つ</rt></ruby>き</b> + <ruby>次第<rt>しだい</rt></ruby>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>詳<rt>くわ</rt></ruby>しいことが<span class="pe-hl pe-hl--s">わかり<ruby>次第<rt>しだい</rt></ruby></span>、お<ruby>知<rt>し</rt></ruby>らせします。</p>
  <p class="pe-ex__uz">Tafsilotlar maʼlum boʻlishi bilan xabar beramiz.</p>
  <p class="pe-ex__why">Bu — <ruby>次第<rt>しだい</rt></ruby> ning oʻz uyi: rasmiy eʼlon, ish yozishmasi, xizmat xabari. お<ruby>知<rt>し</rt></ruby>らせします — PJ-70 dagi <ruby>謙譲語<rt>けんじょうご</rt></ruby>.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Ot bilan ham ishlaydi, va bu shakl eʼlonlarda juda koʻp:</b>
  <ruby>到着<rt>とうちゃく</rt></ruby><ruby>次第<rt>しだい</rt></ruby>
  («yetib kelishi bilan»),
  <ruby>連絡<rt>れんらく</rt></ruby><ruby>次第<rt>しだい</rt></ruby>
  («aloqa boʻlishi bilan»). Qoida sodda: <b>する</b> bilan feʼl
  boʻladigan otlarga <ruby>次第<rt>しだい</rt></ruby> toʻgʻridan-toʻgʻri yopishadi, oraga
  hech narsa qoʻyilmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Nega bu dars oʻzbek oʻquvchisi uchun qiyin — sababi ochiq.</b>
  Bizda «…ishi bilan» <em>ikkala</em> vaziyatga ham toʻgʻri keladi:
  «Vokzalga yetishi bilan yomgʻir yogʻdi» ham, «Vokzalga yetishingiz
  bilan qoʻngʻiroq qiling» ham tabiiy gaplar. Oʻzbekchada ularni
  <b>feʼlning zamoni</b> ajratadi, alohida qoʻshimcha emas.
  Yapon tili esa teskari yoʻldan borgan: u <em>zamonni qolipning
  ichiga solib qoʻygan</em>. Shuning uchun tarjima qilayotganda
  oʻzbekcha iborangizga emas, <b>gapning oxiriga</b> qarang.
  «…qildi» bilan tugasa — とたん. «…qilaman», «…qiling» bilan
  tugasa — <ruby>次第<rt>しだい</rt></ruby>. Boshqa savol yoʻq.</p>
</div>

<h3>3. Ikkovini bir jadvalda koʻring</h3>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>&nbsp;</th><th>〜たとたん</th><th>〜<ruby>次第<rt>しだい</rt></ruby></th></tr>
  <tr><td class="pj-stem">Ulanishi</td>
      <td class="pj-res">た-shakli</td>
      <td class="pj-res">ます-oʻzagi / ot</td></tr>
  <tr><td class="pj-stem">Gap oxiri</td>
      <td class="pj-res">faqat OʻTGAN zamon</td>
      <td class="pj-res">faqat KELASI zamon</td></tr>
  <tr><td class="pj-stem">Ohang</td>
      <td class="pj-res">kutilmagan, ixtiyorsiz</td>
      <td class="pj-res">rejali, ixtiyoriy</td></tr>
  <tr><td class="pj-stem">Buyruq/iltimos</td>
      <td class="pj-res">mumkin emas</td>
      <td class="pj-res">aynan shuning uchun bor</td></tr>
  <tr><td class="pj-stem">Qayerda</td>
      <td class="pj-res">hikoya, kundalik</td>
      <td class="pj-res">rasmiy xabar, ish yozishmasi</td></tr>
</table></div>

<div class="pe-vs">
  <div class="pe-vs__card"><p class="pe-vs__h">✓ <ruby>着<rt>つ</rt></ruby>いたとたん、<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した</p>
    <p>Yetib kelishim bilanoq yomgʻir yogʻa boshladi. Kutilmagan, oʻtgan — とたん.</p></div>
  <div class="pe-vs__card pe-vs__card--alt"><p class="pe-vs__h">✓ <ruby>着<rt>つ</rt></ruby>き<ruby>次第<rt>しだい</rt></ruby>、<ruby>電話<rt>でんわ</rt></ruby>してください</p>
    <p>Yetib kelishingiz bilan qoʻngʻiroq qiling. Rejali, kelasi — <ruby>次第<rt>しだい</rt></ruby>.</p></div>
</div>

<h3>4. 〜か〜ないかのうちに — «…ar-etmas»</h3>

<p>Uchinchisi eng uzun, lekin tuzilishi mexanik:
<b>lugʻat shakli + か + ない-shakli + かのうちに</b>. Bitta feʼl
ikki marta yoziladi — biri tasdiqda, biri inkorda.</p>

<div class="pe-ex">
  <p class="pe-ex__ja">ベルが<span class="pe-hl pe-hl--v"><ruby>鳴<rt>な</rt></ruby>るか<ruby>鳴<rt>な</rt></ruby>らないかのうちに</span>、みんな<ruby>教室<rt>きょうしつ</rt></ruby>を<ruby>出<rt>で</rt></ruby>た。</p>
  <p class="pe-ex__uz">Qoʻngʻiroq chalinar-chalinmas hamma sinfdan chiqdi.</p>
  <p class="pe-ex__why">Ikki voqea <b>ustma-ust tushgan</b>: birinchisi tugamasidan ikkinchisi boshlangan. とたん dan ham tigʻizroq.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Bu qolipning oʻzbekchasi shu qadar aniqki, uni tushuntirishning
  hojati ham yoʻq.</b> Biz «chalin<b>ar</b>-chalin<b>mas</b>»,
  «yot<b>ar</b>-yot<b>mas</b>», «kel<b>ar</b>-kel<b>mas</b>» deymiz —
  <em>bitta feʼl ikki marta, biri tasdiq, biri inkor</em>. Yaponcha
  <ruby>鳴<rt>な</rt></ruby>る<b>か</b><ruby>鳴<rt>な</rt></ruby>らない<b>か</b>
  ham aynan shu: «chalindimi, chalinmadimi — bilinmadi». Ikki til
  bir xil fikrga bir xil yoʻldan kelgan. Yodlash uchun bittagina
  narsa qoladi: yaponchada oxirida <b>のうちに</b> ham boʻladi.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Bu qolip yozma tilga tegishli</b> — hikoyada, insho va
  maqolada uchraydi, doʻstingizga yozgan xabarda emas. Kundalik
  gapda odamlar oddiygina «<ruby>鳴<rt>な</rt></ruby>ってすぐ» yoki
  «<ruby>鳴<rt>な</rt></ruby>ったとたん» deyishadi. Siz uni
  <b>tanib olishingiz</b> kerak; yozishda esa tanlov sizda.</p>
</div>

<h3>5. Uchalasini yonma-yon</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h">〜てすぐ</p>
    <p><ruby>着<rt>つ</rt></ruby>いてすぐ<ruby>電話<rt>でんわ</rt></ruby>した。</p>
    <p>Eng bemalol. «Darrov» degani, boshqa hech qanday shart yoʻq.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">〜たとたん</p>
    <p><ruby>着<rt>つ</rt></ruby>いたとたん、<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した。</p>
    <p>Kutilmagan. Oʻtgan zamon. Gapiruvchining ixtiyorida emas.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">〜<ruby>次第<rt>しだい</rt></ruby></p>
    <p><ruby>着<rt>つ</rt></ruby>き<ruby>次第<rt>しだい</rt></ruby>、<ruby>電話<rt>でんわ</rt></ruby>します。</p>
    <p>Rejali. Kelasi zamon. Rasmiy ohang.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h">〜か〜ないかのうちに</p>
    <p><ruby>着<rt>つ</rt></ruby>くか<ruby>着<rt>つ</rt></ruby>かないかのうちに、<ruby>雨<rt>あめ</rt></ruby>が<ruby>降<rt>ふ</rt></ruby>り<ruby>出<rt>だ</rt></ruby>した。</p>
    <p>Eng tigʻiz. Ikkovi ustma-ust tushgan. Yozma til.</p>
  </div>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">次</span>
    <span class="pj-kanji__uz">keyingi, navbatdagi</span>
    <span class="pj-kanji__on">オン: ジ・シ</span>
    <span class="pj-kanji__kun">KUN: つぎ・つ(ぐ)</span>
    <span class="pj-kanji__note">次 (つぎ) — keyingi · 次第 (しだい) — …ishi bilan</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">第</span>
    <span class="pj-kanji__uz">tartib, daraja</span>
    <span class="pj-kanji__on">オン: ダイ</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">第一 (だいいち) — birinchi · 次第 (しだい)</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">途</span>
    <span class="pj-kanji__uz">yoʻl, orada</span>
    <span class="pj-kanji__on">オン: ト</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">途中 (とちゅう) — yoʻlda · 途端 (とたん)</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <p><b>とたん ning kanjisi bor —
  <ruby>途端<rt>とたん</rt></ruby></b> — lekin grammatik qolip
  sifatida u koʻpincha <b>hiraganada</b> yoziladi. Ikkalasini ham
  koʻrasiz, ikkalasi ham toʻgʻri. Shu qoida yaponchada keng
  tarqalgan: soʻz <em>maʼnoli</em> boʻlsa kanji, <em>grammatik</em>
  boʻlsa kana.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>駅<rt>えき</rt></ruby>に<ruby>着<rt>つ</rt></ruby>いたとたん、<ruby>電話<rt>でんわ</rt></ruby>してください</p>
  <p class="pe-fix__good">✓ <ruby>着<rt>つ</rt></ruby>き<b><ruby>次第<rt>しだい</rt></ruby></b>、<ruby>電話<rt>でんわ</rt></ruby>してください — iltimos boʻlsa, とたん emas, <ruby>次第<rt>しだい</rt></ruby>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>着<rt>つ</rt></ruby>く<ruby>次第<rt>しだい</rt></ruby>、<ruby>電話<rt>でんわ</rt></ruby>します</p>
  <p class="pe-fix__good">✓ <ruby>着<rt>つ</rt></ruby>き<ruby>次第<rt>しだい</rt></ruby> — <ruby>次第<rt>しだい</rt></ruby> lugʻat shakliga emas, <b>ます-oʻzagiga</b> ulanadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>着<rt>つ</rt></ruby>き<ruby>次第<rt>しだい</rt></ruby>、<ruby>電話<rt>でんわ</rt></ruby>しました</p>
  <p class="pe-fix__good">✓ <ruby>着<rt>つ</rt></ruby>いたとたん、<ruby>電話<rt>でんわ</rt></ruby>が<ruby>鳴<rt>な</rt></ruby>った — <ruby>次第<rt>しだい</rt></ruby> dan keyin <b>oʻtgan zamon boʻlmaydi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ ベルが<ruby>鳴<rt>な</rt></ruby>るか<ruby>鳴<rt>な</rt></ruby>らない<b>うちに</b></p>
  <p class="pe-fix__good">✓ <ruby>鳴<rt>な</rt></ruby>るか<ruby>鳴<rt>な</rt></ruby>らない<b>かの</b>うちに — ikkinchi <b>か</b> va <b>の</b> tushib qolmasin.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>立<rt>た</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>がるとたん、<ruby>目<rt>め</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>が<ruby>暗<rt>くら</rt></ruby>くなった</p>
  <p class="pe-fix__good">✓ <ruby>立<rt>た</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>が<b>った</b>とたん — とたん faqat <b>た-shakliga</b> ulanadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. «Yetib kelishingiz bilan qoʻngʻiroq qiling» — qaysi qolip?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>着<rt>つ</rt></ruby>き<ruby>次第<rt>しだい</rt></ruby>、<ruby>電話<rt>でんわ</rt></ruby>してください</b>. Iltimos — kelasi zamon, demak <ruby>次第<rt>しだい</rt></ruby>. とたん dan keyin iltimos kela olmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>着<rt>つ</rt></ruby>___<ruby>次第<rt>しだい</rt></ruby> — boʻsh joyga nima tushadi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>き</b>: <ruby>着<rt>つ</rt></ruby>き<ruby>次第<rt>しだい</rt></ruby>. Bu <ruby>着<rt>つ</rt></ruby>きます ning ます-oʻzagi. Lugʻat shakli (<ruby>着<rt>つ</rt></ruby>く) ham, た-shakli ham bu yerga tushmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. «Qoʻngʻiroq chalinar-chalinmas hamma chiqdi» — yaponchada?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ベルが<ruby>鳴<rt>な</rt></ruby>るか<ruby>鳴<rt>な</rt></ruby>らないかのうちに、みんな<ruby>出<rt>で</rt></ruby>た</b>. Bitta feʼl ikki marta — biri lugʻat shaklida, biri ない-shaklida.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. Nega «<ruby>立<rt>た</rt></ruby>ったとたん、<ruby>座<rt>すわ</rt></ruby>りましょう» xato?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>ましょう — niyat</b>, とたん esa <b>kutilmagan</b> voqeani aytadi. Bir gapda «rejalashtirdim» va «kutmagandim» sigʻmaydi. とたん dan keyin faqat oʻtgan zamondagi xabar keladi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. <ruby>連絡<rt>れんらく</rt></ruby> (aloqa) soʻziga <ruby>次第<rt>しだい</rt></ruby> ni ulang.</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>連絡<rt>れんらく</rt></ruby><ruby>次第<rt>しだい</rt></ruby></b>. する bilan feʼl boʻladigan otlarga <ruby>次第<rt>しだい</rt></ruby> toʻgʻridan-toʻgʻri yopishadi — oraga <b>の</b> ham, <b>し</b> ham qoʻyilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. とたん va <ruby>次第<rt>しだい</rt></ruby> ni ajratish uchun gapning qayeriga qaraysiz?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Oxiriga.</b> Oʻtgan zamonda tugasa — とたん. Kelasi zamon, iltimos yoki niyat bilan tugasa — <ruby>次第<rt>しだい</rt></ruby>. Boshiga qarash kerak emas.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>〜たとたん(に)</b> — …ishi bilanoq (oʻtgan, kutilmagan)</li>
  <li><b>〜<ruby>次第<rt>しだい</rt></ruby></b> — …ishi bilan (kelasi, rejali)</li>
  <li><b>〜か〜ないかのうちに</b> — …ar-etmas</li>
  <li><b>〜てすぐ</b> — …ib darrov</li>
  <li><b><ruby>飛<rt>と</rt></ruby>び<ruby>出<rt>だ</rt></ruby>す</b> — otilib chiqmoq</li>
  <li><b><ruby>立<rt>た</rt></ruby>ち<ruby>上<rt>あ</rt></ruby>がる</b> — oʻrnidan turmoq</li>
  <li><b><ruby>鳴<rt>な</rt></ruby>る</b> — jiringlamoq, chalinmoq</li>
  <li><b><ruby>到着<rt>とうちゃく</rt></ruby></b> — yetib kelish</li>
  <li><b><ruby>連絡<rt>れんらく</rt></ruby></b> — aloqa, xabar</li>
  <li><b><ruby>詳<rt>くわ</rt></ruby>しい</b> — batafsil</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>とたん</b> — た-shakli, oxiri <b>oʻtgan</b> zamon, kutilmagan.</li>
    <li><b><ruby>次第<rt>しだい</rt></ruby></b> — ます-oʻzagi yoki ot, oxiri <b>kelasi</b> zamon, rejali.</li>
    <li><b>か〜ないかのうちに</b> — bitta feʼl ikki marta: tasdiq, keyin inkor.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PJ-96: Yozma uslub: だ・である体 va gazeta yaponchasi",
        "category": "japanese",
        "order": 96,
        "summary": (
            "Kursning birinchi USLUB darsi. です・ます体, だ体 va である体 "
            "— uchta registr, uchta boshqa dunyo. Insho, maqola va gazeta "
            "yaponchasini tanib olasiz va oʻzingiz yoza boshlaysiz."
        ),
        "stories": ["こうこうせいが つくった ちず"],
        "content": """
<h2>PJ-96: Yozma uslub: だ・である<ruby>体<rt>たい</rt></ruby> va gazeta yaponchasi</h2>

<p>Bir kun yapon gazetasini ochasiz va hayron qolasiz: siz bilgan
<b>です</b> ham, <b>ます</b> ham yoʻq. Gaplar
<b>である</b> bilan tugaydi, sarlavhalarda esa qoʻshimchalar
umuman tushib qolgan. Xato emas — bu <b>boshqa registr</b>.</p>

<p>Bu dars yangi grammatika bermaydi. U sizga
<em>bir xil fikrni uch xil kiyimda</em> koʻrsatadi va qaysi
kiyim qayerga toʻgʻri kelishini oʻrgatadi. Shundan keyin siz
maqola, insho va xabar yaponchasini tanib olasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchta registrni — です・ます, だ, である — ajratasiz</li>
    <li><b>である<ruby>体<rt>たい</rt></ruby></b> shakllarini yasaysiz</li>
    <li>Yozma bogʻlovchilarni (しかし, また, なお…) ishlatasiz</li>
    <li>Gazeta sarlavhasini oʻqiy olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch kiyim, bir fikr</span>
  <span class="pe-chip pe-chip--s"><ruby>学生<rt>がくせい</rt></ruby>です</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v"><ruby>学生<rt>がくせい</rt></ruby>だ</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux"><ruby>学生<rt>がくせい</rt></ruby>である</span>
</div>

<h3>1. Uchta registr</h3>

<div class="pj-level">
  <div class="pj-level__row pj-level__row--3">
    <span class="pj-level__name"><ruby>丁寧体<rt>ていねいたい</rt></ruby></span>
    <span class="pj-level__ja"><ruby>学生<rt>がくせい</rt></ruby>です</span>
    <span class="pj-level__who">gap, xat, xabar, bu sayt — odamga murojaat</span>
  </div>
  <div class="pj-level__row pj-level__row--2">
    <span class="pj-level__name"><ruby>普通体<rt>ふつうたい</rt></ruby> (だ<ruby>体<rt>たい</rt></ruby>)</span>
    <span class="pj-level__ja"><ruby>学生<rt>がくせい</rt></ruby>だ</span>
    <span class="pj-level__who">kundalik, roman, blog, doʻstga xabar</span>
  </div>
  <div class="pj-level__row pj-level__row--1">
    <span class="pj-level__name">である<ruby>体<rt>たい</rt></ruby></span>
    <span class="pj-level__ja"><ruby>学生<rt>がくせい</rt></ruby>である</span>
    <span class="pj-level__who">insho, maqola, ilmiy ish, gazeta, hisobot</span>
  </div>
</div>

<p>Eʼtibor bering: <b>である</b> — «eng hurmatli» emas. U
<em>hurmat oʻqini tark etgan</em>: unda oʻquvchi ham, tinglovchi
ham yoʻq. Bor-yoʻgʻi <b>fikr</b> bor. Shuning uchun u ilmiy va
rasmiy matnning tili.</p>

<div class="pe-call pe-uz">
  <p><b>Oʻzbek tilida ham xuddi shu uch qavat bor, faqat biz ularga
  nom qoʻymaymiz.</b> «Kecha keldim, koʻrdim» — soʻzlashuv.
  «Tadqiqotchi bu masalani oʻrgandi» — oddiy yozma. «Mazkur masala
  tadqiq <em>etilgan</em> boʻlib, natijalar quyidagicha
  <em>hisoblanadi</em>» — ilmiy uslub. Uchinchisida ham kim
  qilganini aytmaymiz, «siz»ga murojaat yoʻq, faqat fikr bor —
  aynan <b>である<ruby>体<rt>たい</rt></ruby></b> ning ishi. Demak
  bu sizga yangi tushuncha emas; faqat yaponchada uning
  <em>grammatik belgisi</em> bor, oʻzbekchada esa yoʻq.</p>
</div>

<h3>2. である<ruby>体<rt>たい</rt></ruby> shakllari</h3>

<p>Yaxshi xabar: <b>feʼl va い-sifat umuman oʻzgarmaydi</b>. Faqat
<b>だ</b> turgan joylar oʻzgaradi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>&nbsp;</th><th>です・ます<ruby>体<rt>たい</rt></ruby></th><th>だ<ruby>体<rt>たい</rt></ruby></th><th>である<ruby>体<rt>たい</rt></ruby></th></tr>
  <tr><td class="pj-stem">ot</td>
      <td class="pj-end"><ruby>学生<rt>がくせい</rt></ruby>です</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>だ</td>
      <td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby><b>である</b></td></tr>
  <tr><td class="pj-stem">ot, inkor</td>
      <td class="pj-end"><ruby>学生<rt>がくせい</rt></ruby>ではありません</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>ではない</td>
      <td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby><b>でない</b></td></tr>
  <tr><td class="pj-stem">ot, oʻtgan</td>
      <td class="pj-end"><ruby>学生<rt>がくせい</rt></ruby>でした</td>
      <td class="pj-res"><ruby>学生<rt>がくせい</rt></ruby>だった</td>
      <td class="pj-uz"><ruby>学生<rt>がくせい</rt></ruby><b>であった</b></td></tr>
  <tr><td class="pj-stem">な-sifat</td>
      <td class="pj-end"><ruby>静<rt>しず</rt></ruby>かです</td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かだ</td>
      <td class="pj-uz"><ruby>静<rt>しず</rt></ruby>か<b>である</b></td></tr>
  <tr><td class="pj-stem">い-sifat</td>
      <td class="pj-end"><ruby>大<rt>おお</rt></ruby>きいです</td>
      <td class="pj-res"><ruby>大<rt>おお</rt></ruby>きい</td>
      <td class="pj-uz"><ruby>大<rt>おお</rt></ruby>きい — <b>oʻzgarmaydi</b></td></tr>
  <tr><td class="pj-stem">feʼl</td>
      <td class="pj-end"><ruby>行<rt>い</rt></ruby>きます</td>
      <td class="pj-res"><ruby>行<rt>い</rt></ruby>く</td>
      <td class="pj-uz"><ruby>行<rt>い</rt></ruby>く — <b>oʻzgarmaydi</b></td></tr>
  <tr><td class="pj-stem">な-sifat + ot</td>
      <td class="pj-end"><ruby>静<rt>しず</rt></ruby>かな<ruby>町<rt>まち</rt></ruby></td>
      <td class="pj-res"><ruby>静<rt>しず</rt></ruby>かな<ruby>町<rt>まち</rt></ruby></td>
      <td class="pj-uz"><ruby>静<rt>しず</rt></ruby>かな<ruby>町<rt>まち</rt></ruby> — <b>oʻzgarmaydi</b></td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja">この<ruby>問題<rt>もんだい</rt></ruby>は<ruby>簡単<rt>かんたん</rt></ruby><span class="pe-hl pe-hl--v">ではない</span>。<ruby>解決<rt>かいけつ</rt></ruby>には<ruby>時間<rt>じかん</rt></ruby>が<ruby>必要<rt>ひつよう</rt></ruby><span class="pe-hl pe-hl--v">である</span>。</p>
  <p class="pe-ex__uz">Bu masala oson emas. Uni hal qilish uchun vaqt zarur.</p>
  <p class="pe-ex__why">Ikkala gap ham である<ruby>体<rt>たい</rt></ruby>da. Diqqat: <b>ではない</b> ham, <b>でない</b> ham bu uslubda uchraydi; <b>でない</b> quruqroq.</p>
</div>

<div class="pe-call pe-rule">
  <p><b>Amalda である を har gapga qoʻyilmaydi.</b> Yapon inshosining
  koʻp gaplari feʼl bilan tugaydi, feʼl esa oʻzgarmaydi — demak
  matnning oʻzi allaqachon である<ruby>体<rt>たい</rt></ruby>da.
  <b>である</b> faqat <em>ot va な-sifat</em> gap oxirida turganda
  koʻrinadi. Shuning uchun butun sahifada uni ikki-uch marta
  uchratsangiz, bu normal.</p>
</div>

<h3>3. Yozma bogʻlovchilar</h3>

<p>Registr faqat gap oxiri emas. Bogʻlovchilar ham oʻzgaradi, va
aynan ular matnni birinchi qarashdayoq yozma qilib koʻrsatadi.</p>

<div class="pe-table-wrap"><table class="pj-conj">
  <tr><th>Gapda</th><th>Yozma matnda</th><th>Maʼnosi</th></tr>
  <tr><td class="pj-stem">でも</td><td class="pj-res">しかし</td><td class="pj-uz">lekin, biroq</td></tr>
  <tr><td class="pj-stem">だから</td><td class="pj-res">したがって</td><td class="pj-uz">shuning uchun, binobarin</td></tr>
  <tr><td class="pj-stem">それから</td><td class="pj-res">また · さらに</td><td class="pj-uz">shuningdek, bundan tashqari</td></tr>
  <tr><td class="pj-stem">でも、〜だけは</td><td class="pj-res">ただし</td><td class="pj-uz">lekin shuni ham aytish kerakki</td></tr>
  <tr><td class="pj-stem">ちなみに</td><td class="pj-res">なお</td><td class="pj-uz">qoʻshimcha qilib aytganda</td></tr>
  <tr><td class="pj-stem">〜のほうは</td><td class="pj-res"><ruby>一方<rt>いっぽう</rt></ruby></td><td class="pj-uz">ikkinchi tomondan</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>調査<rt>ちょうさ</rt></ruby>の<ruby>結果<rt>けっか</rt></ruby>、<ruby>読書<rt>どくしょ</rt></ruby>の<ruby>時間<rt>じかん</rt></ruby>は<ruby>減<rt>へ</rt></ruby>っていた。<span class="pe-hl pe-hl--adv">しかし</span>、<ruby>本<rt>ほん</rt></ruby>を<ruby>買<rt>か</rt></ruby>う<ruby>人<rt>ひと</rt></ruby>は<ruby>増<rt>ふ</rt></ruby>えている。</p>
  <p class="pe-ex__uz">Tadqiqot natijasiga koʻra, kitob oʻqish vaqti kamaygan. Biroq kitob sotib oluvchilar koʻpaymoqda.</p>
  <p class="pe-ex__why">Bu gapni doʻstingizga aytsangiz でも derdingiz. Maqolada <b>しかし</b> turadi — bir xil maʼno, boshqa qavat.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Oʻzbekchada ham xuddi shu juftliklar bor va siz ularni
  allaqachon bilasiz.</b> Gapda «lekin» deymiz, maqolada «biroq»
  yozamiz. Gapda «shuning uchun», ilmiy ishda «binobarin».
  Gapda «yana», matnda «shuningdek». Hech kim sizga bu qoidani
  oʻrgatmagan — siz uni oʻqib yurib olgansiz. Yaponchada ham
  aynan shunday boʻladi, faqat hozircha sizda oʻsha «oʻqib
  yurish» tajribasi yoʻq. Shuning uchun bu jadvalni bir marta
  yodlab qoʻyish — bir yillik oʻqishni tejaydi.</p>
</div>

<h3>4. Gazeta sarlavhasi — eng qisqa yaponcha</h3>

<p>Sarlavhada joy kam, shuning uchun tejashning oʻz qoidalari bor:</p>

<div class="pe-steps">
  <ol>
    <li><b>Qoʻshimchalar tushadi.</b> <ruby>台風<rt>たいふう</rt></ruby>、<ruby>九州<rt>きゅうしゅう</rt></ruby>に<ruby>上陸<rt>じょうりく</rt></ruby> — «は» ham, «が» ham yoʻq. Vergul ularning oʻrnini bosadi.</li>
    <li><b>Gap oxiri tushadi.</b> <ruby>上陸<rt>じょうりく</rt></ruby>した emas, shunchaki <ruby>上陸<rt>じょうりく</rt></ruby> — ot bilan tugaydi.</li>
    <li><b>へ = kelajak reja.</b> <ruby>新<rt>しん</rt></ruby><ruby>駅<rt>えき</rt></ruby>、<ruby>来春<rt>らいしゅん</rt></ruby><ruby>開業<rt>かいぎょう</rt></ruby>へ — «keyingi bahorda ochiladi».</li>
    <li><b>か = aniq emas.</b> <ruby>値上<rt>ねあ</rt></ruby>げか — «narx koʻtarilishi mumkin».</li>
    <li><b>Sonlar raqamda.</b> 3<ruby>人<rt>にん</rt></ruby>, 20<ruby>年<rt>ねん</rt></ruby> — kanji bilan emas.</li>
  </ol>
</div>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>新<rt>しん</rt></ruby><ruby>駅<rt>えき</rt></ruby>、<ruby>来春<rt>らいしゅん</rt></ruby><ruby>開業<rt>かいぎょう</rt></ruby>へ</p>
  <p class="pe-ex__uz">Yangi bekat kelasi bahorda ochiladi.</p>
  <p class="pe-ex__why">Toʻliq gapga aylantirsak: <ruby>新<rt>しん</rt></ruby><ruby>駅<rt>えき</rt></ruby>は<ruby>来春<rt>らいしゅん</rt></ruby><ruby>開業<rt>かいぎょう</rt></ruby>する<ruby>予定<rt>よてい</rt></ruby>である。Sarlavha shuning siqilgan shakli.</p>
</div>

<div class="pe-call pe-tip">
  <p><b>Sarlavhani oʻqish usuli: qoʻshimchalarni oʻzingiz qaytaring.</b>
  Vergulni «は» deb, oxiridagi otni feʼlga aylantirib oʻqing.
  <ruby>台風<rt>たいふう</rt></ruby>、<ruby>九州<rt>きゅうしゅう</rt></ruby>に<ruby>上陸<rt>じょうりく</rt></ruby>
  → <ruby>台風<rt>たいふう</rt></ruby><b>が</b><ruby>九州<rt>きゅうしゅう</rt></ruby>に<ruby>上陸<rt>じょうりく</rt></ruby><b>した</b>.
  Bir hafta mashq qilsangiz, bu avtomatga aylanadi.</p>
</div>

<div class="pe-call pe-uz">
  <p><b>Gazeta sarlavhasi oʻzbekchada ham xuddi shunday siqiladi.</b>
  «Toshkentda yangi bekat — bahorda ochiladi» emas, balki
  «Toshkentda yangi bekat: bahorda» deb yoziladi; «Havo harorati
  pasaymoqda» oʻrniga «Sovuq qaytdi». Qoʻshimchalar tushadi, feʼl
  tushadi, tire va ikki nuqta ularning oʻrnini bosadi. Demak
  yaponcha sarlavha sizga notanish narsa emas — u aynan oʻsha
  tejamkorlik, faqat boshqa belgilar bilan: bizda tire turgan
  joyda ularda <b>、</b> turadi, bizda «…boʻladi» tushirilgan
  joyda ularda <b>へ</b> qoladi. Shuni bilsangiz, sarlavhani
  lugʻatsiz ham chala-yarim tushunasiz.</p>
</div>

<h3>5. Bitta qatʼiy qoida: aralashtirmang</h3>

<p>Bu darsda «toʻgʻri/notoʻgʻri» kam, «qayerda» koʻp. Lekin bitta
qoida qatʼiy: <b>bitta matn ichida registr oʻzgarmaydi</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__ja"><ruby>調査<rt>ちょうさ</rt></ruby>の<ruby>結果<rt>けっか</rt></ruby>、<ruby>三<rt>さん</rt></ruby><ruby>割<rt>わり</rt></ruby>が「<ruby>読<rt>よ</rt></ruby>まない」と<ruby>答<rt>こた</rt></ruby>えた。<ruby>理由<rt>りゆう</rt></ruby>は<ruby>時間<rt>じかん</rt></ruby>がないこと<span class="pe-hl pe-hl--v">である</span>。</p>
  <p class="pe-ex__uz">Tadqiqot natijasida uchdan biri «oʻqimayman» deb javob berdi. Sababi — vaqt yoʻqligi.</p>
  <p class="pe-ex__why">Ikkala gap ham bir qavatda. Ikkinchisini «…ことです» deb yozsangiz, matn buziladi.</p>
</div>

<div class="pe-call pe-warn">
  <p><b>Eng koʻp uchraydigan yozma xato — oxirgi gapni
  です bilan yopish.</b> Oʻquvchi butun inshoni である<ruby>体<rt>たい</rt></ruby>da
  yozadi, keyin xulosada birdan «…と<ruby>思<rt>おも</rt></ruby>います»
  deb qoʻyadi, chunki u joyda u <em>oʻqituvchiga</em> gapirayotgandek
  his qiladi. Yaponcha inshoda oʻqituvchi yoʻq —
  «…と<ruby>思<rt>おも</rt></ruby>う» yoki
  «…と<ruby>考<rt>かんが</rt></ruby>える» boʻlishi kerak.
  Bitta gapdagi bu sakrash butun matnning bahosini tushiradi.</p>
</div>

<div class="pj-kanji">
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">論</span>
    <span class="pj-kanji__uz">fikr, muhokama</span>
    <span class="pj-kanji__on">オン: ロン</span>
    <span class="pj-kanji__kun">KUN: —</span>
    <span class="pj-kanji__note">論文 (ろんぶん) — ilmiy maqola · 議論 (ぎろん) — bahs</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">述</span>
    <span class="pj-kanji__uz">bayon qilmoq</span>
    <span class="pj-kanji__on">オン: ジュツ</span>
    <span class="pj-kanji__kun">KUN: の(べる)</span>
    <span class="pj-kanji__note">述べる (のべる) — bayon qilmoq · 記述 (きじゅつ) — tavsif</span>
  </div>
  <div class="pj-kanji__c">
    <span class="pj-kanji__ch">従</span>
    <span class="pj-kanji__uz">ergashmoq, boʻysunmoq</span>
    <span class="pj-kanji__on">オン: ジュウ</span>
    <span class="pj-kanji__kun">KUN: したが(う)</span>
    <span class="pj-kanji__note">従って (したがって) — shuning uchun · 従う — ergashmoq</span>
  </div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>問題<rt>もんだい</rt></ruby>は<ruby>簡単<rt>かんたん</rt></ruby><b>だである</b></p>
  <p class="pe-fix__good">✓ <ruby>簡単<rt>かんたん</rt></ruby><b>である</b> — である <b>だ</b> ning oʻrniga keladi, uning ustiga emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>大<rt>おお</rt></ruby>きい<b>である</b></p>
  <p class="pe-fix__good">✓ <ruby>大<rt>おお</rt></ruby>きい — い-sifat va feʼl bu uslubda <b>umuman oʻzgarmaydi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ <ruby>結果<rt>けっか</rt></ruby>は<ruby>明<rt>あき</rt></ruby>らかである。<b>でも</b>、<ruby>理由<rt>りゆう</rt></ruby>はわからない。</p>
  <p class="pe-fix__good">✓ <b>しかし</b>、<ruby>理由<rt>りゆう</rt></ruby>はわからない — yozma matnda でも emas, <b>しかし</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ (insho oxirida) …と<ruby>思<rt>おも</rt></ruby><b>います</b></p>
  <p class="pe-fix__good">✓ …と<ruby>思<rt>おも</rt></ruby><b>う</b> / …と<ruby>考<rt>かんが</rt></ruby><b>える</b> — matn oxirigacha bir registrda qoladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-fix__bad">✗ (sarlavha) <ruby>台風<rt>たいふう</rt></ruby><b>が</b><ruby>九州<rt>きゅうしゅう</rt></ruby>に<ruby>上陸<rt>じょうりく</rt></ruby>しました</p>
  <p class="pe-fix__good">✓ <ruby>台風<rt>たいふう</rt></ruby>、<ruby>九州<rt>きゅうしゅう</rt></ruby>に<ruby>上陸<rt>じょうりく</rt></ruby> — sarlavhada qoʻshimcha ham, gap oxiri ham tushadi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q">1. <ruby>学生<rt>がくせい</rt></ruby>でした — である<ruby>体<rt>たい</rt></ruby>da qanday boʻladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>学生<rt>がくせい</rt></ruby>であった</b>. だった → であった. Bu shakl asosan maqola va tarixiy matnlarda uchraydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">2. <ruby>大<rt>おお</rt></ruby>きいです — である<ruby>体<rt>たい</rt></ruby>da?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b><ruby>大<rt>おお</rt></ruby>きい</b> — bor-yoʻgʻi です tushadi. い-sifat oʻzgarmaydi, ustiga である qoʻyilmaydi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">3. Maqolada «でも» oʻrniga nima yoziladi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>しかし</b>. Xuddi shunday: だから → <b>したがって</b>, それから → <b>また</b>, ちなみに → <b>なお</b>.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">4. <ruby>新<rt>しん</rt></ruby><ruby>駅<rt>えき</rt></ruby>、<ruby>来春<rt>らいしゅん</rt></ruby><ruby>開業<rt>かいぎょう</rt></ruby>へ — bu sarlavhadagi «へ» nimani bildiradi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Kelajak rejani.</b> Toʻliq gapi: <ruby>開業<rt>かいぎょう</rt></ruby>する<ruby>予定<rt>よてい</rt></ruby>である. Sarlavhada «へ» shu butun iborani bitta belgiga siqadi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">5. である<ruby>体<rt>たい</rt></ruby>dagi insho oxirida «…と<ruby>思<rt>おも</rt></ruby>います» deb yozsa boʻladimi?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>Yoʻq.</b> <b>…と<ruby>思<rt>おも</rt></ruby>う</b> yoki <b>…と<ruby>考<rt>かんが</rt></ruby>える</b>. Registr matn oxirigacha bir xil qoladi — bu darsning yagona qatʼiy qoidasi.</p></details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q">6. Kundalikda qaysi registr tabiiy?</p>
  <details class="pe-reveal"><summary>Javob</summary>
  <p><b>だ<ruby>体<rt>たい</rt></ruby></b> (<ruby>普通体<rt>ふつうたい</rt></ruby>). である — maqola va ilmiy ish uchun; kundalikda u sovuq eshitiladi.</p></details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>である<ruby>体<rt>たい</rt></ruby></b> — yozma-rasmiy uslub</li>
  <li><b><ruby>普通体<rt>ふつうたい</rt></ruby></b> — oddiy shakl, だ uslubi</li>
  <li><b>しかし</b> — biroq (yozma)</li>
  <li><b>したがって</b> — binobarin, shuning uchun</li>
  <li><b>また · さらに</b> — shuningdek, bundan tashqari</li>
  <li><b>なお</b> — qoʻshimcha qilib aytganda</li>
  <li><b><ruby>一方<rt>いっぽう</rt></ruby></b> — ikkinchi tomondan</li>
  <li><b><ruby>述<rt>の</rt></ruby>べる</b> — bayon qilmoq</li>
  <li><b><ruby>調査<rt>ちょうさ</rt></ruby></b> — tadqiqot, soʻrov</li>
  <li><b><ruby>結果<rt>けっか</rt></ruby></b> — natija</li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoladigan uch narsa</p>
  <ul>
    <li><b>である</b> <b>だ</b> ning oʻrniga keladi; feʼl va い-sifat oʻzgarmaydi.</li>
    <li>Yozma matnda でも emas <b>しかし</b>, だから emas <b>したがって</b>.</li>
    <li>Bitta matn — bitta registr. Oxirgi gapni です bilan yopmang.</li>
  </ul>
</div>
""",
    },
]
