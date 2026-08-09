# -*- coding: utf-8 -*-
"""Prime Russian — Block B, darslar 12–14.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Har bir dars uchta boʻlakdan biri: dars + mashq + oʻqish matni.
Mashqlar:        practice/management/commands/_practice_pr_12_14.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_12_14.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_12_14.py --author=prime
"""

PLAYLIST = {
    "title": "Prime Russian",
    "category": "russian",
    "description": (
        "Rus tili noldan ishonchli B2 gacha — 100 ta dars. Kirill alifbosi, kelishiklar, "
        "feʼl turlari, oʻzbekcha tushuntirish va oʻzingiz tekshiradigan mashqlar."
    ),
}

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-12: Sifat otga moslashadi — новый, новая, новое, новые",
        "category": "russian",
        "order": 12,
        "summary": (
            "Oʻzbekchada “yangi” hech qachon oʻzgarmaydi. Ruschada esa sifat otning "
            "jinsi va soniga qarab toʻrt xil shakl oladi — va bu shakllarni siz "
            "allaqachon koʻrgansiz."
        ),
        "stories": ["Но́вая шко́ла"],
        "content": """
<h2>PR-12: Sifat otga moslashadi — новый, новая, новое, новые</h2>

<p>Oʻzbekchada bitta soʻz hamma joyga yetadi: <em>yangi uy, yangi kitob, yangi deraza,
yangi kitoblar</em> — <b>yangi</b> qimirlamaydi. Ruschada esa u toʻrt marta shakl
oʻzgartiradi: <b>но́вый дом, но́вая кни́га, но́вое окно́, но́вые кни́ги</b>. Bu koʻp
ishga oʻxshaydi, lekin bitta yaxshi xabar bor — siz bu toʻrtlikni allaqachon
bilasiz. U PR-8 dagi <em>он/она́/оно́/они́</em> va PR-10 dagi <em>мой/моя́/моё/мои́</em>
bilan aynan bir xil naqsh. Uchinchi marta koʻryapsiz, demak bu safar oson boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Sifatning toʻrtta shaklini otga moslaysiz</li>
    <li>Uchta oxir turini ajratasiz: <b>-ый</b>, <b>-о́й</b>, <b>-ий</b></li>
    <li><b>Како́й? Кака́я? Како́е? Каки́е?</b> deb soʻraysiz</li>
    <li>Sifat otdan oldin turishini — oʻzbekchadagidek — tasdiqlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta sifat, toʻrtta shakl</span>
  <span class="pe-chip pe-chip--s">но́в<b>ый</b> дом</span>
  <span class="pe-chip pe-chip--o">но́в<b>ая</b> кни́га</span>
  <span class="pe-chip pe-chip--v">но́в<b>ое</b> окно́</span>
  <span class="pe-chip pe-chip--adv">но́в<b>ые</b> кни́ги</span>
</div>

<h3>1. Toʻrtta shakl</h3>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">но́в<span class="pr-end">ый</span> дом</p>
    <p>ста́р<b>ый</b> го́род<br>интере́сн<b>ый</b> фильм</p>
    <p>Savoli: <b>Како́й?</b></p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">но́в<span class="pr-end">ая</span> кни́га</p>
    <p>ста́р<b>ая</b> шко́ла<br>интере́сн<b>ая</b> исто́рия</p>
    <p>Savoli: <b>Кака́я?</b></p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">но́в<span class="pr-end">ое</span> окно́</p>
    <p>ста́р<b>ое</b> ме́сто<br>интере́сн<b>ое</b> сло́во</p>
    <p>Savoli: <b>Како́е?</b></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Э́то <span class="pe-hl pe-hl--o">но́вые</span> кни́ги.</p>
  <p class="pe-ex__uz">Bu — yangi kitoblar.</p>
  <p class="pe-ex__why">Koʻplikda jins yana yoʻqoladi (PR-9 dagidek): hamma jins
     uchun bitta shakl — <b>но́вые</b>.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Uchta jadvalni yonma-yon qoʻying va bir xil naqshni koʻring:<br>
<b>он — она́ — оно́ — они́</b><br>
<b>мой — моя́ — моё — мои́</b><br>
<b>но́вый — но́вая — но́вое — но́вые</b><br>
Rus tili sizdan yangi narsa oʻrganishni soʻramayapti — u bitta naqshni qayta-qayta
ishlatyapti. Har safar uni tanisangiz, kurs qisqarib boradi.</div>

<h3>2. Uchta oxir turi</h3>

<p>Erkak jinsining oxiri uch xil boʻlishi mumkin, va bu qolgan shakllarga ham
taʼsir qiladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Turi</th><th>м.</th><th>ж.</th><th>с.</th><th>мн.</th></tr>
  <tr><td class="pr-uz"><b>1. Oddiy</b> — urgʻu oʻzakda</td>
      <td class="pr-res">но́в<span class="pr-end">ый</span></td>
      <td class="pr-res">но́в<span class="pr-end">ая</span></td>
      <td class="pr-res">но́в<span class="pr-end">ое</span></td>
      <td class="pr-res">но́в<span class="pr-end">ые</span></td></tr>
  <tr><td class="pr-uz"><b>2. Urgʻuli oxir</b> — <b>-о́й</b></td>
      <td class="pr-res">больш<span class="pr-end">о́й</span></td>
      <td class="pr-res">больш<span class="pr-end">а́я</span></td>
      <td class="pr-res">больш<span class="pr-end">о́е</span></td>
      <td class="pr-res">больш<span class="pr-end">и́е</span></td></tr>
  <tr><td class="pr-uz"><b>3. Yumshoq</b> — <b>-ний</b></td>
      <td class="pr-res">си́н<span class="pr-end">ий</span></td>
      <td class="pr-res">си́н<span class="pr-end">яя</span></td>
      <td class="pr-res">си́н<span class="pr-end">ее</span></td>
      <td class="pr-res">си́н<span class="pr-end">ие</span></td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>-ый</b> va <b>-о́й</b> — bir xil tur, farqi faqat urgʻuda. Urgʻu oxirga tushsa,
<b>-ый</b> avtomatik <b>-о́й</b> boʻlib chiqadi: <em>молодо́й, плохо́й, дорого́й,
больш<b>о́й</b></em>. Yaʼni bu yangi qoida emas — bu talaffuzning imloga taʼsiri.</div>

<h3>3. Yettita harf yana ishlaydi</h3>

<p>PR-9 dagi <b>Г К Х Ж Ч Ш Щ</b> roʻyxati bu yerda ham chiqadi. Ulardan keyin
<b>-ый</b> emas, <b>-ий</b> yoziladi:</p>

<div class="pr-say">
  <span class="pr-say__from">ру́сск + ый</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">ру́сск<b>ий</b></span>
  <span class="pr-say__why">К dan keyin -ы boʻlmaydi</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">ма́леньк + ый</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">ма́леньк<b>ий</b></span>
  <span class="pr-say__why">shu qoida</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">хоро́ш + ый</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">хоро́ш<b>ий</b></span>
  <span class="pr-say__why">Ш dan keyin ham</span>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Ж Ч Ш Щ</b> dan keyin urgʻusiz <b>о</b> ham <b>е</b> ga aylanadi. Shuning uchun
oʻrta jinsda: <b>хоро́шее</b>, <em>хоро́шое</em> emas. Lekin urgʻu oxirga tushsa,
<b>о</b> oʻz joyida qoladi: <b>большо́е</b>. Ikkita soʻzni yonma-yon yodlang —
<em>хоро́шее / большо́е</em> — va bu qoidani hech qachon adashtirmaysiz.</div>

<h3>4. Sifat qayerda turadi</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">Э́то <span class="pe-hl pe-hl--adv">но́вая</span>
     <span class="pe-hl pe-hl--o">шко́ла</span>.</p>
  <p class="pe-ex__uz">Bu — yangi maktab.</p>
  <p class="pe-ex__why">Sifat otdan <b>oldin</b> turadi — xuddi oʻzbekchadagidek.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu yerda ikkita xabar bor, biri yaxshi, biri qiyin. <b>Yaxshisi:</b> soʻz tartibi
bir xil — <em>yangi maktab</em> = <b>но́вая шко́ла</b>, sifat oldinda. Ingliz yoki
fransuz tilidan farqli oʻlaroq, siz bu yerda hech narsani oʻzgartirmaysiz.
<b>Qiyini:</b> oʻzbek sifati hech qachon oʻzgarmaydi, rus sifati esa har safar
otga qaraydi. Yaʼni siz <em>joyni</em> emas, <em>oxirini</em> oʻrganyapsiz.</div>

<p>Sifat kesim boʻlib, otdan <b>keyin</b> ham turishi mumkin — bu PR-11 dagi
tiresiz gap:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">Шко́ла <span class="pe-hl pe-hl--v">но́вая</span>.<br>
     Дом <span class="pe-hl pe-hl--v">большо́й</span>.</p>
  <p class="pe-ex__uz">Maktab yangi. Uy katta.</p>
  <p class="pe-ex__why">Bu yerda tire <b>qoʻyilmaydi</b> — kesim sifat (PR-11).
     Maʼnosi ham biroz boshqa: <em>но́вая шко́ла</em> = “yangi maktab” (nomlash),
     <em>шко́ла но́вая</em> = “maktab yangi” (xabar berish).</p>
</div>

<h3>5. Како́й? — “qanday?”</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--s">Кака́я</span> э́то шко́ла?<br>
     — Э́то <span class="pe-hl pe-hl--o">больша́я</span> и
     <span class="pe-hl pe-hl--o">но́вая</span> шко́ла.</p>
  <p class="pe-ex__uz">— Bu qanday maktab?<br>— Bu katta va yangi maktab.</p>
  <p class="pe-ex__why">Savol soʻzi ham otga moslashadi — xuddi <b>чей/чья</b>
     kabi (PR-10). Va ikkita sifatni <b>и</b> bilan bogʻlash mumkin.</p>
</div>

<h3>6. Ishlatishga tayyor sifatlar</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Juftlik bilan</p>
    <p>но́вый — ста́рый (yangi — eski)<br>
       большо́й — ма́ленький (katta — kichik)<br>
       хоро́ший — плохо́й (yaxshi — yomon)<br>
       дорого́й — дешёвый (qimmat — arzon)</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Odam haqida</p>
    <p>у́мный (aqlli) · до́брый (mehribon)<br>
       весёлый (quvnoq) · молодо́й (yosh)<br>
       краси́вый (chiroyli)</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Narsa haqida</p>
    <p>интере́сный (qiziqarli)<br>
       тру́дный (qiyin) · лёгкий (oson)<br>
       вку́сный (mazali) · ру́сский (ruscha)</p></div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>но́вый кни́га</s></p>
  <p class="pe-good">но́в<b>ая</b> кни́га — <em>кни́га</em> ayol jinsi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>ру́сскый язы́к</s></p>
  <p class="pe-good">ру́сск<b>ий</b> язы́к — К dan keyin <b>-ий</b>, hech qachon <b>-ый</b> emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>хоро́шое окно́</s></p>
  <p class="pe-good">хоро́ш<b>ее</b> окно́ — Ш dan keyin urgʻusiz <b>о</b> → <b>е</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Дом — большо́й.</s></p>
  <p class="pe-good">Дом большо́й. — kesim sifat boʻlsa, tire qoʻyilmaydi (PR-11)</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>___ шко́ла</b> (yangi)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>но́вая шко́ла</strong>. <em>Шко́ла</em> ayol
    jinsi (-а), demak sifat ham ayol shaklida: <b>-ая</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>___ окно́</b> (katta)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>большо́е окно́</strong>. <em>Окно́</em> oʻrta
    jins. Diqqat: <b>большо́е</b>, chunki urgʻu oxirda — <em>большое</em> emas,
    <b>больш<u>о́</u>е</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega <b>ру́сский</b>, <b>ру́сскый</b> emas?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki oʻzak <b>К</b> bilan tugaydi, u esa yettita
    harf roʻyxatida (<strong>Г К Х Ж Ч Ш Щ</strong>). Ulardan keyin
    <strong>-ы</strong> hech qachon yozilmaydi. Xuddi shu qoida PR-9 da
    <em>кни́ги</em> ni ham tushuntirgan edi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Savolni tuzing: <b>___ э́то кни́ги?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Каки́е э́то кни́ги?</strong> —
    <em>кни́ги</em> koʻplikda, demak <b>каки́е</b>. Birlikda boʻlsa edi:
    <em>Кака́я э́то кни́га?</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi birikma notoʻgʻri?<br>
     а) но́вое сло́во &nbsp; б) больша́я шко́ла<br>
     в) хоро́шое окно́ &nbsp; г) ста́рый го́род</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi
    <b>хоро́шее окно́</b>: <b>Ш</b> dan keyin urgʻusiz <b>о</b> <b>е</b> ga aylanadi.
    Solishtiring: <em>большо́е</em> da urgʻu oxirda, shuning uchun u yerda
    <b>о</b> qoladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>но́вый / ста́рый</b><span>yangi / eski</span></li>
  <li><b>большо́й / ма́ленький</b><span>katta / kichik</span></li>
  <li><b>хоро́ший / плохо́й</b><span>yaxshi / yomon</span></li>
  <li><b>краси́вый</b><span>chiroyli</span></li>
  <li><b>интере́сный</b><span>qiziqarli</span></li>
  <li><b>тру́дный / лёгкий</b><span>qiyin / oson</span></li>
  <li><b>вку́сный</b><span>mazali</span></li>
  <li><b>ру́сский</b><span>ruscha, rus</span></li>
  <li><b>си́ний</b><span>koʻk</span></li>
  <li><b>како́й?</b><span>qanday?</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Sifat otning <b>jinsi va soniga</b> moslashadi:
        <b>но́вый / но́вая / но́вое / но́вые</b>.</li>
    <li>Bu naqsh siz uchun uchinchi marta: <em>он/она́/оно́/они́</em>,
        <em>мой/моя́/моё/мои́</em>, endi sifat.</li>
    <li>Uch tur: <b>-ый</b> (oddiy), <b>-о́й</b> (urgʻu oxirda), <b>-ий</b> (yumshoq).</li>
    <li><b>Г К Х Ж Ч Ш Щ</b> dan keyin — <b>-ий</b>: ру́сский, ма́ленький, хоро́ший.</li>
    <li>Ж Ч Ш Щ dan keyin urgʻusiz <b>о → е</b>: <b>хоро́шее</b>, lekin <b>большо́е</b>.</li>
    <li>Sifat otdan <b>oldin</b> turadi — oʻzbekchadagidek. Kesim boʻlsa keyin turadi
        va tire qoʻyilmaydi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-13: Sonlar 0–100 va «сколько?»",
        "category": "russian",
        "order": 13,
        "summary": (
            "Noldan yuzgacha sanashni oʻrganasiz. Ikkita sonning oʻziga xosligi bor: "
            "оди́н jinsga qarab oʻzgaradi, два esa ayol jinsi uchun две shaklini oladi."
        ),
        "stories": ["Ско́лько сто́ит?"],
        "content": """
<h2>PR-13: Sonlar 0–100 va «сколько?»</h2>

<p>Sonlar — tilning eng amaliy qismi. Ular bilan narx soʻraysiz, vaqt aytasiz,
telefon raqamini beryapsiz, yoshingizni aytasiz. Rus sonlari oʻzbekcha sonlarga
oʻxshab tuzilgan — <em>oʻn bir</em>, <em>yigirma besh</em> — lekin ikkita joyda
oʻziga xoslik bor: <b>оди́н</b> jinsga qarab oʻzgaradi, va <b>два</b> ning ayol
jinsi uchun alohida shakli bor. Qolgani oddiy yodlash.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>0 dan 100 gacha sanaysiz</li>
    <li><b>оди́н / одна́ / одно́</b> ni otga moslaysiz</li>
    <li><b>два</b> va <b>две</b> ni ajratasiz</li>
    <li><b>Ско́лько?</b> deb soʻraysiz va son bilan otni bogʻlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki oʻziga xoslik</span>
  <span class="pe-chip pe-chip--s">оди́н · одна́ · одно́</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">два (м./с.) · две (ж.)</span>
</div>

<h3>1. Nol dan oʻngacha</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Son</th><th>Ruscha</th><th>Son</th><th>Ruscha</th></tr>
  <tr><td class="pr-res">0</td><td class="pr-stem">ноль</td>
      <td class="pr-res">6</td><td class="pr-stem">шесть</td></tr>
  <tr><td class="pr-res">1</td><td class="pr-stem">оди́н</td>
      <td class="pr-res">7</td><td class="pr-stem">семь</td></tr>
  <tr><td class="pr-res">2</td><td class="pr-stem">два</td>
      <td class="pr-res">8</td><td class="pr-stem">во́семь</td></tr>
  <tr><td class="pr-res">3</td><td class="pr-stem">три</td>
      <td class="pr-res">9</td><td class="pr-stem">де́вять</td></tr>
  <tr><td class="pr-res">4</td><td class="pr-stem">четы́ре</td>
      <td class="pr-res">10</td><td class="pr-stem">де́сять</td></tr>
  <tr><td class="pr-res">5</td><td class="pr-stem">пять</td>
      <td class="pr-res">&nbsp;</td><td class="pr-stem">&nbsp;</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Uchta sonda urgʻu <b>birinchi</b> boʻgʻinda va oʻquvchilar buni doim adashtiradi:
<b>во́семь</b> (8), <b>де́вять</b> (9), <b>де́сять</b> (10). “Vosem<u>ʼ</u>”,
“devyat<u>ʼ</u>” emas — urgʻu boshda. Yana: <b>пять, шесть, семь, во́семь,
де́вять, де́сять</b> — hammasi <b>-ь</b> bilan tugaydi, demak ular ayol jinsidagi
otlarga oʻxshaydi.</div>

<h3>2. Oʻn birdan yigirmagacha</h3>

<p>Bu yerda chiroyli mantiq bor. <b>-надцать</b> — bu qadimgi <em>“на де́сять”</em>,
yaʼni “oʻn ustiga”. Yaʼni <b>оди́ннадцать</b> = “bir oʻn ustiga”:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Son</th><th>Ruscha</th><th>Son</th><th>Ruscha</th></tr>
  <tr><td class="pr-res">11</td><td class="pr-stem">оди́ннадцать</td>
      <td class="pr-res">16</td><td class="pr-stem">шестна́дцать</td></tr>
  <tr><td class="pr-res">12</td><td class="pr-stem">двена́дцать</td>
      <td class="pr-res">17</td><td class="pr-stem">семна́дцать</td></tr>
  <tr><td class="pr-res">13</td><td class="pr-stem">трина́дцать</td>
      <td class="pr-res">18</td><td class="pr-stem">восемна́дцать</td></tr>
  <tr><td class="pr-res">14</td><td class="pr-stem">четы́рнадцать</td>
      <td class="pr-res">19</td><td class="pr-stem">девятна́дцать</td></tr>
  <tr><td class="pr-res">15</td><td class="pr-stem">пятна́дцать</td>
      <td class="pr-res">20</td><td class="pr-stem">два́дцать</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekcha <em>oʻn bir</em> = “oʻn + bir”. Ruscha <b>оди́ннадцать</b> = “bir + oʻn
ustiga”. Yaʼni <b>tartib teskari</b>, lekin mantiq bir xil: ikkala tilda ham 11 —
bu “oʻn va bir”. Faqat ruschada bu bitta soʻzga yopishib qolgan. 14 da esa
kichik gʻalatilik bor: <b>четы́рнадцать</b>, <em>четыренадцать</em> emas — bitta
boʻgʻin tushib qolgan.</div>

<h3>3. Oʻnliklar va yuz</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Son</th><th>Ruscha</th><th>Izoh</th><th>Oʻqilishi</th></tr>
  <tr><td class="pr-res">20</td><td class="pr-stem">два́дцать</td>
      <td class="pr-uz">два + дцать</td><td class="pr-end">[два́ццът']</td></tr>
  <tr><td class="pr-res">30</td><td class="pr-stem">три́дцать</td>
      <td class="pr-uz">три + дцать</td><td class="pr-end">[три́ццът']</td></tr>
  <tr><td class="pr-res">40</td><td class="pr-stem">со́рок</td>
      <td class="pr-uz"><b>istisno</b> — naqshga kirmaydi</td><td class="pr-end">[со́рък]</td></tr>
  <tr><td class="pr-res">50</td><td class="pr-stem">пятьдеся́т</td>
      <td class="pr-uz">пять + десят</td><td class="pr-end">[пиид'ис'а́т]</td></tr>
  <tr><td class="pr-res">60</td><td class="pr-stem">шестьдеся́т</td>
      <td class="pr-uz">шесть + десят</td><td class="pr-end">[шыз'д'ис'а́т]</td></tr>
  <tr><td class="pr-res">70</td><td class="pr-stem">се́мьдесят</td>
      <td class="pr-uz">urgʻu <b>boshda</b>!</td><td class="pr-end">[с'э́м'д'ис'ит]</td></tr>
  <tr><td class="pr-res">80</td><td class="pr-stem">во́семьдесят</td>
      <td class="pr-uz">urgʻu <b>boshda</b>!</td><td class="pr-end">[во́с'им'д'ис'ит]</td></tr>
  <tr><td class="pr-res">90</td><td class="pr-stem">девяно́сто</td>
      <td class="pr-uz"><b>istisno</b> — naqshga kirmaydi</td><td class="pr-end">[д'ивано́стъ]</td></tr>
  <tr><td class="pr-res">100</td><td class="pr-stem">сто</td>
      <td class="pr-uz">qisqa va oson</td><td class="pr-end">[сто]</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ikkita sonni alohida yodlang, chunki ular hech qanday naqshga kirmaydi:
<b>со́рок</b> (40) va <b>девяно́сто</b> (90). Qolgan oʻnliklar oddiy:
son + <em>дцать</em> yoki son + <em>десят</em>. Va 70 bilan 80 da urgʻu
<b>boshida</b> — bu eng koʻp qilinadigan talaffuz xatosi.</div>

<p>Qoʻshma sonlar oddiy — soʻzlarni ketma-ket qoʻyasiz:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">21 — два́дцать оди́н<br>
     35 — три́дцать пять<br>
     48 — со́рок во́семь<br>
     99 — девяно́сто де́вять</p>
  <p class="pe-ex__uz">Xuddi oʻzbekchadagidek: yigirma bir, oʻttiz besh…</p>
  <p class="pe-ex__why">Bu yerda hech qanday hiyla yoʻq. Ikkala tilda ham katta
     son avval, kichigi keyin.</p>
</div>

<h3>4. Оди́н — jinsga qarab oʻzgaradi</h3>

<p>Sonlar orasida faqat <b>оди́н</b> sifat kabi ishlaydi:</p>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">м. — оди́н</p>
    <p class="pr-gender__form">оди́н дом</p>
    <p>оди́н брат · оди́н день</p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">ж. — одна́</p>
    <p class="pr-gender__form">одна́ кни́га</p>
    <p>одна́ шко́ла · одна́ сестра́</p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">с. — одно́</p>
    <p class="pr-gender__form">одно́ окно́</p>
    <p>одно́ сло́во · одно́ ме́сто</p>
  </div>
</div>

<h3>5. Два yoki две?</h3>

<p>Faqat <b>ikki</b> sonining ayol jinsi uchun alohida shakli bor. Uch, toʻrt,
besh va qolganlarining hammasi oʻzgarmaydi:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">два — м. va с.</p>
    <p style="font-size:1.15rem">два до́ма · два бра́та<br>два окна́ · два сло́ва</p>
    <p>Erkak va oʻrta jins uchun.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">две — faqat ж.</p>
    <p style="font-size:1.15rem">две кни́ги · две шко́лы<br>две сестры́ · две ру́чки</p>
    <p>Faqat ayol jinsi uchun.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Bu farq <b>faqat 2 da</b> bor — va qoʻshma sonlarda ham saqlanadi:
<b>два́дцать две кни́ги</b>, <b>три́дцать два до́ма</b>. Uch va undan keyingi
sonlarning jinsi umuman yoʻq: <em>три кни́ги</em>, <em>три до́ма</em> — bir xil.</div>

<h3>6. Ско́лько? va sondan keyin ot nima boʻladi</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--s">Ско́лько</span> здесь
     студе́нтов?<br>— Два́дцать оди́н.</p>
  <p class="pe-ex__uz">— Bu yerda nechta talaba bor?<br>— Yigirma bir.</p>
</div>

<p>Endi diqqat qiling: sondan keyingi ot rus tilida <b>shaklini oʻzgartiradi</b>.
Yuqorida allaqachon koʻrdingiz — <em>два до́м<b>а</b></em>, <em>две кни́г<b>и</b></em>.
Buning toʻliq qoidasi <b>родительный падеж</b>ga tegishli va uni PR-36 da
oʻrganamiz. Hozircha shu uchta naqshni tayyor holda yodlab qoʻying:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Son</th><th>Ot qanday boʻladi</th><th>Misol (м.)</th><th>Misol (ж.)</th></tr>
  <tr><td class="pr-res">1</td><td class="pr-uz">oddiy shakl</td>
      <td class="pr-stem">оди́н дом</td><td class="pr-stem">одна́ кни́га</td></tr>
  <tr><td class="pr-res">2, 3, 4</td><td class="pr-uz">bitta shakl</td>
      <td class="pr-stem">два до́ма</td><td class="pr-stem">две кни́ги</td></tr>
  <tr><td class="pr-res">5 … 20</td><td class="pr-uz">boshqa shakl</td>
      <td class="pr-stem">пять домо́в</td><td class="pr-stem">пять книг</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekcha bu yerda ancha sodda: <em>bir kitob, ikki kitob, besh kitob</em> — ot
umuman oʻzgarmaydi, hatto <em>-lar</em> ham qoʻshilmaydi. Rus tilida esa son otning
shaklini boshqaradi. Bu darsda buni <b>yodlashingiz shart emas</b> — shunchaki
payqab qoʻying, chunki PR-36 da bu qoida oʻz oʻrniga tushadi. Hozir sizga
sonlarning oʻzi kerak.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Yoshni aytish uchun ruschada boshqa qurilma kerak: <b>Мне пятна́дцать лет</b> —
“men oʻn besh yoshdaman”, soʻzma-soʻz “menga oʻn besh yil”. Bu <em>дательный
падеж</em> va biz uni PR-38 da oʻrganamiz. Hozircha uni <b>tayyor ibora</b>
sifatida yodlang — u har kuni kerak boʻladi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>оди́н кни́га</s></p>
  <p class="pe-good">одна́ кни́га — <b>оди́н</b> jinsga qarab oʻzgaradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>два кни́ги</s></p>
  <p class="pe-good">две кни́ги — ayol jinsida <b>две</b>, <b>два</b> emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>во́семь → [восе́мь]</s></p>
  <p class="pe-good"><b>во́семь</b> — urgʻu birinchi boʻgʻinda. Xuddi shunday
     <b>де́вять</b>, <b>де́сять</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>четыренадцать</s></p>
  <p class="pe-good"><b>четы́рнадцать</b> — bitta boʻgʻin tushib qolgan</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>40</b> ruschada qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>со́рок</strong>. Bu istisno — u
    <em>четы́редцать</em> ham, <em>четы́рдесят</em> ham emas. <b>90</b> ham
    shunday istisno: <b>девяно́сто</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>___ шко́ла</b> (bitta)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>одна́ шко́ла</strong>. <em>Шко́ла</em> ayol
    jinsi, demak <b>одна́</b>. Sonlar orasida faqat <b>оди́н</b> shunday
    oʻzgaradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>два</b> yoki <b>две</b>? &nbsp; <b>___ сестры́</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>две сестры́</strong>. <em>Сестра́</em> ayol
    jinsi, demak <b>две</b>. Erkak yoki oʻrta jins boʻlsa — <b>два</b>:
    <em>два бра́та, два окна́</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>78</b> ni ruschada ayting va urgʻuni koʻrsating.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>се́мьдесят во́семь</strong>. Ikkala soʻzda
    ham urgʻu <b>birinchi</b> boʻgʻinda — bu 70 va 80 ning oʻziga xosligi.
    Solishtiring: <em>пятьдеся́т</em> (50) da urgʻu oxirda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi birikma toʻgʻri?<br>
     а) два кни́ги &nbsp; б) одна́ окно́ &nbsp;
     в) две ру́чки &nbsp; г) оди́н шко́ла</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в) две ру́чки</strong>. <em>Ру́чка</em> ayol
    jinsi → <b>две</b>. а) da <em>кни́га</em> ayol jinsi, demak <b>две кни́ги</b>.
    б) da <em>окно́</em> oʻrta jins → <b>одно́ окно́</b>. г) da <em>шко́ла</em> ayol
    jinsi → <b>одна́ шко́ла</b>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ноль</b><span>nol</span></li>
  <li><b>оди́н / одна́ / одно́</b><span>bir</span></li>
  <li><b>два / две</b><span>ikki</span></li>
  <li><b>со́рок</b><span>qirq (istisno)</span></li>
  <li><b>девяно́сто</b><span>toʻqson (istisno)</span></li>
  <li><b>сто</b><span>yuz</span></li>
  <li><b>ско́лько?</b><span>nechta? qancha?</span></li>
  <li><b>ско́лько сто́ит?</b><span>qancha turadi?</span></li>
  <li><b>мне … лет</b><span>men … yoshdaman</span></li>
  <li><b>но́мер</b><span>raqam</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>1–10 ni yodlang, urgʻuga diqqat: <b>во́семь, де́вять, де́сять</b>.</li>
    <li>11–20 = son + <b>-надцать</b> (“oʻn ustiga”). 14 da bitta boʻgʻin tushadi:
        <b>четы́рнадцать</b>.</li>
    <li>Ikkita istisno: <b>со́рок</b> (40), <b>девяно́сто</b> (90). 70 va 80 da
        urgʻu boshda.</li>
    <li><b>Оди́н</b> jinsga qarab oʻzgaradi: <b>оди́н / одна́ / одно́</b>.</li>
    <li><b>Два</b> (м., с.) — <b>две</b> (ж.). Faqat 2 da bu farq bor.</li>
    <li>Sondan keyin ot shaklini oʻzgartiradi — toʻliq qoida PR-36 da.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-14: У меня есть — rus tilida egalik",
        "category": "russian",
        "order": 14,
        "summary": (
            "Rus tilida “ega boʻlmoq” feʼli yoʻq. Uning oʻrniga «У меня́ есть …» "
            "qurilmasi ishlatiladi — va u oʻzbekchadagi «Menda … bor» bilan aynan "
            "bir xil ishlaydi."
        ),
        "stories": ["У меня́ есть всё"],
        "content": """
<h2>PR-14: У меня есть — rus tilida egalik</h2>

<p>Ingliz tilida <em>I have a brother</em> deyiladi — “men akaga egaman”. Rus tilida
esa bunday feʼl kundalik nutqda <b>ishlatilmaydi</b>. Uning oʻrniga rus tili
boshqa yoʻldan boradi: <b>У меня́ есть брат</b> — soʻzma-soʻz “menda aka bor”.
Va shu yerda sizga yaxshi xabar bor: oʻzbek tili ham <b>aynan shunday</b> qiladi.
<em>Menda kitob bor. Mening akam bor.</em> Ikkala tilda ham “ega boʻlmoq” feʼli
yoʻq — ikkalasi ham “falon joyda falon narsa <em>bor</em>” deydi. Bu dars sizga
deyarli tekinga keladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>У меня́ есть …</b> qurilmasini tuzasiz</li>
    <li>Yettita shaklni bilasiz: у меня́, у тебя́, у него́, у неё, у нас, у вас, у них</li>
    <li><b>есть</b> qachon tushib qolishini tushunasiz</li>
    <li>PR-6 dagi «Э́то <s>есть</s> дом» taqiqi bilan bu <b>есть</b> ni ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Egalik qolipi</span>
  <span class="pe-chip pe-chip--adv">У</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">меня́ / тебя́ / него́ …</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">есть</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">narsa</span>
</div>

<h3>1. Yettita shakl</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Olmosh</th><th>Egalik shakli</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">я</td><td class="pr-stem">у меня́</td>
      <td class="pr-end">У меня́ есть брат.</td><td class="pr-uz">Mening akam bor.</td></tr>
  <tr><td class="pr-res">ты</td><td class="pr-stem">у тебя́</td>
      <td class="pr-end">У тебя́ есть кот?</td><td class="pr-uz">Sening mushuging bormi?</td></tr>
  <tr><td class="pr-res">он / оно́</td><td class="pr-stem">у него́</td>
      <td class="pr-end">У него́ есть маши́на.</td><td class="pr-uz">Uning mashinasi bor.</td></tr>
  <tr><td class="pr-res">она́</td><td class="pr-stem">у неё</td>
      <td class="pr-end">У неё есть сестра́.</td><td class="pr-uz">Uning singlisi bor.</td></tr>
  <tr><td class="pr-res">мы</td><td class="pr-stem">у нас</td>
      <td class="pr-end">У нас есть уро́к.</td><td class="pr-uz">Bizning darsimiz bor.</td></tr>
  <tr><td class="pr-res">вы</td><td class="pr-stem">у вас</td>
      <td class="pr-end">У вас есть вопро́с?</td><td class="pr-uz">Savolingiz bormi?</td></tr>
  <tr><td class="pr-res">они́</td><td class="pr-stem">у них</td>
      <td class="pr-end">У них есть де́ти.</td><td class="pr-uz">Ularning bolalari bor.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu jadvalni tarjima ustunidan oʻqing va bir narsani payqang: oʻzbekcha
tarjimalarning hammasi <b>bor</b> bilan tugaydi. Rus tilining <b>есть</b> soʻzi —
bu aynan oʻzbekcha <b>bor</b>. Va <b>у меня́</b> — bu <em>menda</em>. Yaʼni
<em>«У меня́ есть брат»</em> = <em>«Menda aka bor»</em>, soʻzma-soʻz, soʻz-soʻzga.
Ingliz tilini oʻrganayotgan bolaga bu qurilmani tushuntirish qiyin; sizga esa
tushuntirish shart emas — siz shunday gapirasiz.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>У него́</b> talaffuzda yana oʻsha tuzoqni beradi — <b>[у н'иво́]</b>. PR-10 dagi
qoida ishlayapti: <b>-го</b> oxiri <b>[во]</b> boʻlib oʻqiladi. Va diqqat qiling:
<em>у него́, у неё, у них</em> da <b>н-</b> harfi paydo boʻlgan (его́ → у <b>н</b>его́).
Bu <b>у</b> predlogi tufayli — shunchaki shu qoʻshimcha “н” ni eslab qoling.</div>

<h3>2. Bu <b>есть</b> — PR-6 dagi taqiqlangan <b>есть</b> emas</h3>

<p>PR-6 da <em>«Э́то <s>есть</s> дом»</em> notoʻgʻri degan edik. Endi <b>есть</b>
paydo boʻldi. Qarama-qarshilik yoʻq — bu ikki xil ish:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">❌ Nomlash — <b>есть</b> KERAK EMAS</p>
    <p style="font-size:1.1rem">Э́то дом.<br>Я студе́нт.<br>Он врач.</p>
    <p>Bu yerda gap <b>nima ekanini</b> aytyapmiz. Hozirgi zamonda “boʻlmoq”
    qoʻyilmaydi (PR-11).</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">✅ Mavjudlik — <b>есть</b> KERAK</p>
    <p style="font-size:1.1rem">У меня́ есть дом.<br>Здесь есть шко́ла.<br>
       У вас есть вопро́с?</p>
    <p>Bu yerda narsa <b>bor yoki yoʻqligini</b> aytyapmiz. Bu butunlay boshqa
    maʼno.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Oʻzbekchaga tarjima qiling va oʻzingizdan soʻrang: gapda <b>“bor”</b> soʻzi
bormi? Bor boʻlsa — ruschada <b>есть</b> kerak. Yoʻq boʻlsa — kerak emas.
<em>“Bu — uy”</em> da “bor” yoʻq → <b>Э́то дом</b>. <em>“Menda uy bor”</em> da
“bor” bor → <b>У меня́ есть дом</b>. Bu tekshiruv deyarli har doim ishlaydi.</div>

<h3>3. Есть qachon tushib qoladi</h3>

<p>Bitta nozik joy bor. Agar gapning maʼnosi “<b>bormi yoki yoʻq</b>” emas, balki
“<b>qanaqa</b>” boʻlsa, <b>есть</b> tushirib qoldiriladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">У меня́ <span class="pe-hl pe-hl--v">есть</span> маши́на.</p>
  <p class="pe-ex__uz">Mening mashinam bor. <em>(umuman bormi — bor)</em></p>
  <p class="pe-ex__why">Diqqat markazi — mashina <b>bor</b>ligida.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">У меня́ <span class="pe-hl pe-hl--o">но́вая</span> маши́на.</p>
  <p class="pe-ex__uz">Mening mashinam yangi. <em>(mashina borligi maʼlum —
     gap uning qanaqaligida)</em></p>
  <p class="pe-ex__why"><b>Есть</b> yoʻq, chunki mashina borligi allaqachon
     maʼlum. Endi diqqat markazi — <b>но́вая</b>.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Boshida bu farqni oʻylab oʻtirmang. <b>Есть</b> ni qoʻyib gapiring — u deyarli
hech qachon xato boʻlmaydi, faqat ba'zan ortiqcha eshitiladi. Bu nozaklikni
quloq oʻzi oʻrganadi: siz rus nutqini eshitgan sari, sifat kelganda <b>есть</b>
tushib qolishini payqay boshlaysiz.</div>

<h3>4. Savol va javob</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">— У тебя́ есть слова́рь?<br>
     — Да, есть.<br>
     — А у него́?<br>
     — У него́ то́же есть.</p>
  <p class="pe-ex__uz">— Sening lugʻating bormi?<br>— Ha, bor.<br>
     — Uniki-chi?<br>— Unda ham bor.</p>
  <p class="pe-ex__why">Qisqa javobda otni takrorlash shart emas: <b>Да, есть</b> —
     “ha, bor”. Xuddi oʻzbekchadagidek.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Inkor shakli — <b>У меня́ нет …</b> — yangi kelishikni (родительный падеж) talab
qiladi, va biz uni PR-34 da oʻrganamiz. Hozircha ikkita eng kerakli iborani
<b>tayyor holda</b> yodlab qoʻying, chunki ular har kuni ishlatiladi:<br>
<b>У меня́ нет вре́мени</b> — vaqtim yoʻq.<br>
<b>У меня́ нет де́нег</b> — pulim yoʻq.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я име́ю брат.</s></p>
  <p class="pe-good">У меня́ есть брат. — kundalik nutqda “ega boʻlmoq” feʼli ishlatilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>У я есть кни́га.</s></p>
  <p class="pe-good">У <b>меня́</b> есть кни́га — <b>у</b> dan keyin olmosh shaklini oʻzgartiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>У его́ есть маши́на.</s></p>
  <p class="pe-good">У <b>него́</b> есть маши́на — <b>у</b> dan keyin <b>н-</b> qoʻshiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то есть мой дом.</s></p>
  <p class="pe-good">Э́то мой дом. — nomlashda <b>есть</b> qoʻyilmaydi (PR-6)</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu gapni ruschaga oʻgiring: <b>Mening singlim bor.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>У меня́ есть сестра́.</strong> Soʻzma-soʻz
    “menda singil bor”. Oʻzbekcha va ruscha qurilma bir xil ishlaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>У ___ есть кот.</b> (uning — ayol kishi)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>У неё есть кот.</strong> Ayol egasi uchun
    <b>у неё</b>. Erkak boʻlsa — <b>у него́</b> [у н'иво́].</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu gapda <b>есть</b> kerakmi? <b>Э́то ___ на́ша шко́ла.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Yoʻq — «Э́то на́ша шко́ла».</strong>
    Oʻzbekchaga oʻgiring: “Bu — bizning maktabimiz”. Bu yerda <b>“bor”</b> soʻzi
    yoʻq, demak <b>есть</b> ham kerak emas. Bu <em>nomlash</em>, mavjudlik
    emas.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega <b>у него́</b>, <b>у его́</b> emas?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki <b>у</b> predlogidan keyin
    <strong>н-</strong> qoʻshiladi: <em>его́ → у <b>н</b>его́</em>,
    <em>её → у <b>н</b>её</em>, <em>их → у <b>н</b>их</em>. Bu faqat predlog
    bilan boʻladi — egalik sifatida esa <em>его́ дом</em> deb qolaveradi
    (PR-10).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gapda <b>есть</b> ortiqcha?<br>
     а) У нас есть уро́к. &nbsp; б) Э́то есть но́вая шко́ла.<br>
     в) У вас есть вопро́с? &nbsp; г) Здесь есть библиоте́ка.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong>. Toʻgʻrisi
    <b>Э́то но́вая шко́ла</b> — bu nomlash, mavjudlik emas. Qolgan uchtasida
    “bor” maʼnosi bor: <em>darsimiz bor, savolingiz bormi, bu yerda kutubxona
    bor</em>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>у меня́ есть</b><span>menda … bor</span></li>
  <li><b>у тебя́ / у вас</b><span>senda / sizda</span></li>
  <li><b>у него́ / у неё</b><span>unda (erkak / ayol)</span></li>
  <li><b>у нас / у них</b><span>bizda / ularda</span></li>
  <li><b>есть</b><span>bor</span></li>
  <li><b>вопро́с</b><span>savol</span></li>
  <li><b>маши́на</b><span>mashina</span></li>
  <li><b>вре́мя</b><span>vaqt</span></li>
  <li><b>у меня́ нет вре́мени</b><span>vaqtim yoʻq</span></li>
  <li><b>у меня́ нет де́нег</b><span>pulim yoʻq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Rus tilida “ega boʻlmoq” feʼli kundalik nutqda <b>ishlatilmaydi</b>.</li>
    <li>Qolip: <b>У + меня́/тебя́/него́/неё/нас/вас/них + есть + narsa</b>.</li>
    <li>Bu oʻzbekchadagi <b>«Menda … bor»</b> bilan aynan bir xil — <b>есть</b> =
        <b>bor</b>.</li>
    <li>Tekshiruv: oʻzbekcha tarjimada <b>“bor”</b> soʻzi bormi? Bor boʻlsa —
        <b>есть</b> kerak.</li>
    <li><b>У</b> dan keyin <b>н-</b> qoʻshiladi: у <b>н</b>его́, у <b>н</b>её,
        у <b>н</b>их. Va <b>у него́</b> = <b>[у н'иво́]</b>.</li>
    <li>Sifat kelganda <b>есть</b> tushib qoladi: <em>У меня́ но́вая маши́на</em>.</li>
  </ul>
</div>
""",
    },
]
