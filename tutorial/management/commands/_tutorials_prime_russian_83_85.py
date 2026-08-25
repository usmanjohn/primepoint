# -*- coding: utf-8 -*-
"""Prime Russian — Block G yakuni va Block H boshlanishi (83–85).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-83 — predloglar xaritasi 2. Darsning gavhari: НЕСМОТРЯ НА ning
oʻzbekcha juftligi soʻzma-soʻz mos tushadi. «Не + смотря» = «qara + may»
— ikkala til ham «yomgʻirga qaramay» deb aytadi. Bunday toza kalka
kursda kam uchraydi.
PR-84 — yuklamalar. Bular maʼno qoʻshmaydi, MUNOSABAT qoʻshadi — nutqni
jonlantiradigan narsa shu. «Же» ↔ oʻzbekcha «-ku» («Aytdim-ku!»),
«неужели» ↔ «nahotki» — ikkalasi ham aynan.
PR-85 — jonli soʻzlashuv. Kitobdagi rus tili bilan koʻchadagi rus tili
orasidagi farq. Qisqarishlar (щас, здрасьте) oʻzbekchadagi «kevotti»
bilan bir xil hodisa — buni aytish oʻquvchini tinchlantiradi.

⚠️ Oʻqish matnlarida URGʻU BELGISI YOʻQ (2026-08-24) — darsliklar saqlaydi.

Mashqlar:        practice/management/commands/_practice_pr_83_85.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_83_85.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_83_85.py --author=prime
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
        "title": "PR-83: Predlog xaritasi 2: по, за, из-за, благодаря, вместо, кроме, несмотря на",
        "category": "russian",
        "order": 83,
        "summary": (
            "Ikkinchi predlog xaritasi. Gavhari — «несмотря́ на»: u oʻzbekcha "
            "«qaramay» ning soʻzma-soʻz nusxasi, chunki ikkalasi ham «qaramay» degani."
        ),
        "stories": ["Благодаря одному письму"],
        "content": """
<h2>PR-83: Predlog xaritasi 2: по, за, из-за, благодаря, вместо, кроме, несмотря на</h2>

<p>PR-48 da predloglarning birinchi xaritasini olgansiz. Endi
<b>qiyinlari</b> navbati keldi — bittasi oltita maʼnoga ega, boshqasi
esa oʻzbekcha soʻzning aynan nusxasi. Aynan shu ikkinchisidan
boshlaymiz, chunki u sizga bepul beriladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Несмотря́ на</b> ni bir daqiqada oʻrganasiz — u oʻzbekcha «qaramay»</li>
    <li><b>По</b> ning oltita maʼnosini ajratasiz</li>
    <li><b>За</b> ning ikki kelishikdagi farqini koʻrasiz</li>
    <li><b>Вме́сто</b>, <b>кро́ме</b> va ularning kelishiklarini olasiz</li>
    <li>PR-66 dagi <b>из-за / благодаря́</b> ni mustahkamlaysiz</li>
  </ul>
</div>

<h3>1. Несмотря́ на — sovgʻa</h3>

<div class="pe-call pe-uz"><span class="pe-call__t">Soʻzma-soʻz bir xil</span>
Ruscha <b>несмотря́</b> ni boʻlaklarga ajrating:
<em>не</em> + <em>смотря́</em> = «<b>qaramay</b>».<br><br>
Endi oʻzbekchasiga qarang: <em>qara</em> + <em>-may</em> =
«<b>qaramay</b>».<br><br>
Ikkala til ham bir xil obrazni ishlatadi — «yomgʻirga
<b>qaramay</b>»:<br>
<em>yomgʻir<b>ga qaramay</b> bordik</em><br>
→ <b>несмотря́ на</b> дождь, мы пошли́<br><br>
Bunday toza moslik butun kursda bir necha marta uchraydi.
Yodlash kerak boʻlgani atigi bitta: <b>несмотря́ на</b>
<b>Вини́тельный</b> oladi — <em>на дождь</em>, <s>на дождя́</s>
emas.</div>

<div class="pe-ex">
  <p class="pe-ex__t">Ikki qurilish</p>
  <p class="pe-ex__ru"><b>Несмотря́ на</b> дождь, матч не отмени́ли.</p>
  <p class="pe-ex__uz">Yomgʻirga qaramay, oʻyin bekor qilinmadi. — ot bilan.</p>
  <p class="pe-ex__ru"><b>Несмотря́ на то, что</b> шёл дождь, матч не отмени́ли.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻayotganiga qaramay… — butun gap bilan.</p>
  <p class="pe-ex__why">Gap bilan kelganda <em>на то, что</em>
     qoʻshiladi — xuddi PR-66 dagi <em>из-за того́ что</em> kabi.</p>
</div>

<h3>2. По — oltita vazifa, bitta soʻz</h3>

<p><b>По</b> deyarli har doim <b>Да́тельный</b> oladi. Qiyinligi
kelishikda emas — <b>maʼnolarining koʻpligida</b>.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Maʼnosi</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">boʻylab, ustidan</td><td class="pr-res">идти́ <b>по</b> у́лице</td>
      <td class="pr-end">koʻcha boʻylab yurmoq</td></tr>
  <tr><td class="pr-stem">vosita bilan</td><td class="pr-res">говори́ть <b>по</b> телефо́ну</td>
      <td class="pr-end">telefon orqali gapirmoq</td></tr>
  <tr><td class="pr-stem">…ga koʻra</td><td class="pr-res"><b>по</b> расписа́нию</td>
      <td class="pr-end">jadvalga koʻra</td></tr>
  <tr><td class="pr-stem">soha, fan</td><td class="pr-res">уче́бник <b>по</b> исто́рии</td>
      <td class="pr-end">tarixdan darslik</td></tr>
  <tr><td class="pr-stem">taqsimlash</td><td class="pr-res"><b>по</b> одному́ я́блоку</td>
      <td class="pr-end">bittadan olma</td></tr>
  <tr><td class="pr-stem">sabab (rasmiy)</td><td class="pr-res"><b>по</b> оши́бке</td>
      <td class="pr-end">xato bilan</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bitta ruscha soʻz — toʻrtta oʻzbekcha</span>
Mana bu joyda yoʻnalish teskari: oʻzbekchada <b>toʻrtta</b> alohida
soʻz bor, ruschada esa hammasi <b>bitta</b> <em>по</em> ga
yigʻilgan:<br><br>
<em>boʻylab</em> · <em>orqali</em> · <em>koʻra</em> ·
<em>bilan</em> &nbsp;→&nbsp; hammasi <b>по</b><br><br>
Shuning uchun ruschadan oʻzbekchaga tarjima qilish qiyin, teskarisi
esa oson. Yodda tuting: agar oʻzbekcha gapda shu toʻrt soʻzdan
biri boʻlsa — ruschada katta ehtimol bilan <b>по + Да́тельный</b>
kerak.</div>

<h3>3. За — kelishikka qarab ikki maʼno</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">ЗА + Твори́тельный</p>
    <p><em>Кот сиди́т <b>за до́мом</b>.</em><br>Mushuk uy orqasida oʻtiribdi.</p>
    <p><b>Joy</b> — harakat yoʻq.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ЗА + Вини́тельный</p>
    <p><em>Кот побежа́л <b>за дом</b>.</em><br>Mushuk uy orqasiga yugurdi.</p>
    <p><b>Yoʻnalish</b> — harakat bor.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Maʼnosi</th><th>Kelishik</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">evaziga, uchun</td><td class="pr-uz">В.п.</td>
      <td class="pr-res">спаси́бо <b>за по́мощь</b></td><td class="pr-end">yordam uchun rahmat</td></tr>
  <tr><td class="pr-stem">toʻlash</td><td class="pr-uz">В.п.</td>
      <td class="pr-res">заплати́ть <b>за биле́т</b></td><td class="pr-end">chipta uchun toʻlamoq</td></tr>
  <tr><td class="pr-stem">vaqt ichida (PR-80)</td><td class="pr-uz">В.п.</td>
      <td class="pr-res">сде́лать <b>за час</b></td><td class="pr-end">bir soatda qilmoq</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">olib kelgani</td><td class="pr-uz">Т.п.</td>
      <td class="pr-res">идти́ <b>за хле́бом</b></td><td class="pr-end">non olgani bormoq</td></tr>
  <tr><td class="pr-stem">stol atrofida</td><td class="pr-uz">Т.п.</td>
      <td class="pr-res">сиде́ть <b>за столо́м</b></td><td class="pr-end">stolda oʻtirmoq</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">«За хле́бом» — juda kerakli qurilish</span>
Oʻzbekcha «<b>non olgani</b> bormoq» ruschada
<b>идти́ за хле́бом</b> boʻladi — Твори́тельный bilan, hech
qanday feʼlsiz:<br><br>
<em>Я иду́ <b>за молоко́м</b>.</em> — Sut olgani ketyapman.<br>
<em>Он пошёл <b>за врачо́м</b>.</em> — Shifokor chaqirgani ketdi.<br><br>
<s>Идти́ за хлеб</s> deyilsa, «nonning orqasiga bormoq» degan
kulgili maʼno chiqadi.</div>

<h3>4. Вме́сто va кро́ме — ikkalasi Роди́тельный</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Вме́сто — oʻrniga</p>
  <p class="pe-ex__ru">Он вы́пил ко́фе <b>вме́сто ча́я</b>.</p>
  <p class="pe-ex__uz">Choy oʻrniga qahva ichdi.</p>
  <p class="pe-ex__ru"><b>Вме́сто меня́</b> пойдёт Бекзо́д.</p>
  <p class="pe-ex__uz">Mening oʻrnimga Bekzod boradi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">Кро́ме — ikki maʼno</p>
  <p class="pe-ex__ru">Пришли́ все, <b>кро́ме</b> Дилно́зы.</p>
  <p class="pe-ex__uz">Dilnozadan tashqari hamma keldi. — <b>istisno</b>.</p>
  <p class="pe-ex__ru"><b>Кро́ме</b> ру́сского, он зна́ет коре́йский.</p>
  <p class="pe-ex__uz">Ruschadan tashqari koreyschani ham biladi. — <b>qoʻshimcha</b>.</p>
  <p class="pe-ex__why">Ikkinchi maʼnoda koʻpincha <em>ещё</em>
     qoʻshiladi: <em>кро́ме того́</em> — «bundan tashqari».</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">«…dan tashqari» ham ikki maʼnoli</span>
Oʻzbekchada ham aynan shu ikkilik bor va u ham bir xil soʻz bilan
beriladi:<br><br>
<em>Dilnoza<b>dan tashqari</b> hamma keldi</em> — istisno<br>
<em>rus tili<b>dan tashqari</b> koreyschani ham biladi</em> — qoʻshimcha<br><br>
Yaʼni <b>кро́ме</b> = <b>«…dan tashqari»</b>, ikkala maʼnosi
bilan birga. Qaysi maʼno ekanini gapning oʻzi koʻrsatadi:
inkor bor boʻlsa — istisno, <em>ещё / то́же</em> bor boʻlsa —
qoʻshimcha.</div>

<h3>5. Из-за va благодаря́ — qisqacha takror</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Predlog</th><th>Kelishik</th><th>Natija</th><th>Misol</th></tr>
  <tr><td class="pr-stem">из-за</td><td class="pr-uz">Роди́тельный</td>
      <td class="pr-end">yomon</td><td class="pr-res">из-за дождя́ мы не пошли́</td></tr>
  <tr><td class="pr-stem">благодаря́</td><td class="pr-uz">Да́тельный</td>
      <td class="pr-end">yaxshi</td><td class="pr-res">благодаря́ дру́гу я нашёл рабо́ту</td></tr>
  <tr><td class="pr-stem">несмотря́ на</td><td class="pr-uz">Вини́тельный</td>
      <td class="pr-end">to'siqqa qaramay</td><td class="pr-res">несмотря́ на дождь, мы пошли́</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Uchtasini bir jadvalda yodlang</span>
Bu uchta predlog bir-biriga yaqin, lekin <b>uch xil kelishik</b>
oladi — va aynan shu adashtiriladi:<br><br>
<b>из-за</b> + Р.п. &nbsp;·&nbsp; <b>благодаря́</b> + Д.п.
&nbsp;·&nbsp; <b>несмотря́ на</b> + В.п.<br><br>
Yordamchi fikr: <em>благодаря́</em> ichida «rahmat aytmoq» bor,
rahmat esa <b>kimga</b> aytiladi → Да́тельный.
<em>Несмотря́ на</em> ichida <em>на</em> bor, <em>на</em> esa
yoʻnalish uchun <b>Вини́тельный</b> oladi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Несмотря́ на дождя́, мы пошли́.</s></p>
  <p class="pe-good">Несмотря́ на <b>дождь</b> — Вини́тельный, chunki <em>на</em> bor</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ за хлеб.</s></p>
  <p class="pe-good">Я иду́ <b>за хле́бом</b> — «olib kelgani» maʼnosida Твори́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Спаси́бо для по́мощи.</s></p>
  <p class="pe-good">Спаси́бо <b>за по́мощь</b> — «uchun» maʼnosida <em>за</em> + В.п.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он вы́пил ко́фе вме́сто чай.</s></p>
  <p class="pe-good">…вме́сто <b>ча́я</b> — <em>вме́сто</em> Роди́тельный oladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Несмотря́ на ___, мы вы́шли
     на у́лицу.</b> (моро́з)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>моро́з</strong> —
    Вини́тельный, shakl oʻzgarmaydi (jonsiz ot). <s>Моро́за</s>
    deyilsa, <em>из-за</em> ning kelishigi qoʻyilgan boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>За хле́бом</b> yoki <b>за хлеб</b>? &nbsp;
     <b>Ма́ма посла́ла меня́ ___ .</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>за хле́бом</strong> —
    Твори́тельный, «non olib kelgani». <em>За хлеб</em> «non
    orqasiga» degan maʼno berardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>По</b> ning qaysi maʼnosi? &nbsp; <b>Мы получи́ли по два
     биле́та.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Taqsimlash</strong> —
    «ikkitadan chipta oldik», yaʼni har birimizga ikkitadan.
    Oʻzbekcha <em>-tadan</em> qoʻshimchasi shuni bildiradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Uchtasini toʻgʻri kelishikka qoʻying.<br>
     <b>из-за (дождь) · благодаря́ (учи́тель) · несмотря́ на (боле́знь)</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>из-за дождя́</strong> (Р.п.)
    · <strong>благодаря́ учи́телю</strong> (Д.п.) ·
    <strong>несмотря́ на боле́знь</strong> (В.п.). Uch predlog —
    uch kelishik.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Kasalligiga qaramay, u mendan tashqari hammaga xat yozdi.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Несмотря́ на боле́знь, он
    написа́л всем, кро́ме меня́.</strong> «Qaramay» →
    <em>несмотря́ на</em> + В.п.; «dan tashqari» → <em>кро́ме</em>
    + Р.п.; «hammaga» → <em>всем</em> (Д.п.).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>несмотря́ на</b> + В.п.<span>…ga qaramay</span></li>
  <li><b>по</b> + Д.п.<span>boʻylab; orqali; koʻra</span></li>
  <li><b>за</b> + В.п.<span>uchun, evaziga</span></li>
  <li><b>за</b> + Т.п.<span>orqasida; olib kelgani</span></li>
  <li><b>из-за</b> + Р.п.<span>tufayli (yomon)</span></li>
  <li><b>благодаря́</b> + Д.п.<span>tufayli (yaxshi)</span></li>
  <li><b>вме́сто</b> + Р.п.<span>oʻrniga</span></li>
  <li><b>кро́ме</b> + Р.п.<span>…dan tashqari</span></li>
  <li><b>кро́ме того́</b><span>bundan tashqari</span></li>
  <li><b>по оши́бке</b><span>xato bilan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Несмотря́ на</b> = oʻzbekcha <b>«qaramay»</b>, soʻzma-soʻz.
        Kelishigi — <b>Вини́тельный</b>.</li>
    <li><b>По</b> + Д.п. — oʻzbekcha <em>boʻylab / orqali / koʻra /
        bilan</em> ning hammasi.</li>
    <li><b>За</b> + Т.п. = orqasida yoki <b>olib kelgani</b>;
        <b>за</b> + В.п. = uchun, evaziga, vaqt ichida.</li>
    <li><b>Вме́сто</b> va <b>кро́ме</b> — ikkalasi
        <b>Роди́тельный</b>.</li>
    <li><b>Кро́ме</b> ikki maʼnoli — xuddi oʻzbekcha «…dan
        tashqari» kabi.</li>
    <li>Uchlikni yodlang: <b>из-за</b> Р.п. · <b>благодаря́</b> Д.п. ·
        <b>несмотря́ на</b> В.п.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-84: Yuklamalar (частицы): же, ведь, ну, вот, разве, неужели, -то",
        "category": "russian",
        "order": 84,
        "summary": (
            "Yuklamalar maʼno qoʻshmaydi — munosabat qoʻshadi. «Же» oʻzbekcha "
            "«-ku», «неужели» esa «nahotki» ning aynan oʻzi."
        ),
        "stories": ["Ну и что же?"],
        "content": """
<h2>PR-84: Yuklamalar (частицы): же, ведь, ну, вот, разве, неужели, -то</h2>

<p>Ikki gap: <em>«Я говори́л»</em> va <em>«Я <b>же</b> говори́л!»</em>.
Grammatik jihatdan ikkalasi ham toʻgʻri, maʼnosi ham bir xil.
Lekin ikkinchisida <b>ovoz</b> bor: «men-<b>ku</b> aytdim!». Mana shu
kichkina soʻzlar — <b>yuklamalar</b> — rus nutqini jonlantiradi. Ularsiz
gap toʻgʻri, lekin quruq boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Же</b> ni oʻzbekcha <b>«-ku»</b> ga bogʻlaysiz</li>
    <li><b>Ведь</b> bilan umumiy bilimga murojaat qilasiz</li>
    <li><b>Ра́зве</b> va <b>неуже́ли</b> bilan hayratni bildirasiz</li>
    <li><b>Ну</b> va <b>вот</b> ni jonli nutqda ishlatasiz</li>
    <li>Yuklama <b>-то</b> ni PR-78 dagi <em>-то</em> dan ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--v">yuklama</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">taʼkidlanayotgan soʻzdan keyin</span>
</div>

<h3>1. Же — «-ku»</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Uch xil ish</p>
  <p class="pe-ex__ru">Я <b>же</b> говори́л!</p>
  <p class="pe-ex__uz">Aytdim-ku! — eslatish, biroz norozilik.</p>
  <p class="pe-ex__ru">Что <b>же</b> де́лать?</p>
  <p class="pe-ex__uz">Nima qilish kerak axir? — chorasizlik.</p>
  <p class="pe-ex__ru">Э́то тот <b>же</b> са́мый челове́к.</p>
  <p class="pe-ex__uz">Bu oʻsha odamning oʻzi. — aynanlik.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Же = -ku</span>
Oʻzbekchada bu vazifani <b>-ku</b> qoʻshimchasi va <b>axir</b>
soʻzi bajaradi, va mosligi juda toza:<br><br>
<em>Ayt<b>dim-ku</b>!</em> &nbsp;→&nbsp; Я <b>же</b> говори́л!<br>
<em>Sen<b>-ku</b> bilasan.</em> &nbsp;→&nbsp; Ты <b>же</b> зна́ешь.<br>
<em><b>Axir</b> u kelmadi.</em> &nbsp;→&nbsp; Он <b>же</b> не пришёл.<br><br>
Oʻrni ham bir xil: oʻzbekcha <em>-ku</em> qaysi soʻzga yopishsa,
ruscha <em>же</em> ham oʻsha soʻzdan <b>keyin</b> turadi.<br><br>
<s>Я говори́л же</s> — notoʻgʻri tartib. <em>Же</em> gap oxirida
turmaydi.</div>

<h3>2. Ведь — «axir, oʻzing bilasan»</h3>

<p><b>Ведь</b> tinglovchining <b>allaqachon biladigan</b> narsasiga
murojaat qiladi. U <em>же</em> ga yaqin, lekin yumshoqroq.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Umumiy bilimga tayanish</p>
  <p class="pe-ex__ru">Ты <b>ведь</b> зна́ешь его́, пра́вда?</p>
  <p class="pe-ex__uz">Sen-ku uni bilasan, shundaymi?</p>
  <p class="pe-ex__ru">Не спеши́, <b>ведь</b> вре́мени мно́го.</p>
  <p class="pe-ex__uz">Shoshilma, axir vaqt koʻp.</p>
  <p class="pe-ex__why"><em>Ведь</em> gap boshida ham tura oladi,
     <em>же</em> esa yoʻq.</p>
</div>

<h3>3. Ра́зве va неуже́ли — hayrat</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">РА́ЗВЕ — «rostdanmi?»</p>
    <p><em><b>Ра́зве</b> он уе́хал?</em><br>U ketdimi, rostdanmi?</p>
    <p>Men boshqacha deb oʻylagandim.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">НЕУЖЕ́ЛИ — «nahotki?»</p>
    <p><em><b>Неуже́ли</b> пра́вда?</em><br>Nahotki rost boʻlsa?</p>
    <p>Ishonishim qiyin, hayratdaman.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Неуже́ли = nahotki</span>
Bu ikkinchi toza moslik. Oʻzbekcha <b>«nahotki»</b> ruscha
<b>«неуже́ли»</b> ning aynan oʻzi — ikkalasi ham
<b>ishonmaslik</b>ni bildiradi va ikkalasi ham gap
<b>boshida</b> turadi:<br><br>
<em><b>Nahotki</b> u buni qilgan boʻlsa?</em><br>
→ <b>Неуже́ли</b> он э́то сде́лал?<br><br>
<b>Ра́зве</b> esa biroz yumshoqroq — «rostdanmi?», «shunaqami?».
U kutilgan narsa bilan haqiqat mos kelmaganda ishlatiladi.</div>

<h3>4. Ну va вот — jonli nutqning tayanchi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Qachon</th></tr>
  <tr><td class="pr-stem">Ну…</td><td class="pr-uz">Xoʻsh…</td>
      <td class="pr-res">javobni boshlashdan oldin</td></tr>
  <tr><td class="pr-stem">Ну и что?</td><td class="pr-uz">Nima boʻpti?</td>
      <td class="pr-res">eʼtiroz</td></tr>
  <tr><td class="pr-stem">Ну ла́дно.</td><td class="pr-uz">Mayli boʻlmasa.</td>
      <td class="pr-res">rozilik, biroz istaksiz</td></tr>
  <tr><td class="pr-stem">Вот!</td><td class="pr-uz">Mana!</td>
      <td class="pr-res">koʻrsatish yoki tasdiq</td></tr>
  <tr><td class="pr-stem">Вот и всё.</td><td class="pr-uz">Mana, hammasi.</td>
      <td class="pr-res">yakunlash</td></tr>
  <tr><td class="pr-stem">Ну вот…</td><td class="pr-uz">Mana koʻrdingmi…</td>
      <td class="pr-res">«men aytgandim» maʼnosida</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__t">Jonli suhbatda</p>
  <p class="pe-ex__ru">— <b>Ну</b> что, идём? — <b>Ну</b> ла́дно, идём.</p>
  <p class="pe-ex__uz">— Xoʻsh, ketdikmi? — Mayli boʻlmasa, ketdik.</p>
  <p class="pe-ex__ru">— Я забы́л ключи́. — <b>Ну вот</b>… Я <b>же</b> тебе́ говори́л.</p>
  <p class="pe-ex__uz">— Kalitni unutibman. — Mana koʻrdingmi… Aytdim-ku senga.</p>
  <p class="pe-ex__ru">— <b>Вот и всё</b>, зако́нчили.</p>
  <p class="pe-ex__uz">— Mana, hammasi, tugatdik.</p>
</div>

<h3>5. Boshqa kerakli yuklamalar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Yuklama</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">да́же</td><td class="pr-uz">hatto</td>
      <td class="pr-res">Да́же он не знал.</td></tr>
  <tr><td class="pr-stem">то́лько</td><td class="pr-uz">faqat</td>
      <td class="pr-res">То́лько не сего́дня.</td></tr>
  <tr><td class="pr-stem">лишь</td><td class="pr-uz">faqat (kitobiy)</td>
      <td class="pr-res">Лишь оди́н раз.</td></tr>
  <tr><td class="pr-stem">ещё</td><td class="pr-uz">hali; yana</td>
      <td class="pr-res">Он ещё не гото́в.</td></tr>
  <tr><td class="pr-stem">уж</td><td class="pr-uz">allaqachon (taʼkid)</td>
      <td class="pr-res">Уж я-то зна́ю.</td></tr>
  <tr><td class="pr-stem">про́сто</td><td class="pr-uz">shunchaki</td>
      <td class="pr-res">Я про́сто уста́л.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bu dars — asosan lugʻat</span>
Oʻzbek tili yuklamalarga <b>juda boy</b>, shuning uchun bu darsda
yangi <b>fikr</b> yoʻq — faqat yangi soʻzlar. Deyarli hammasi
bir-bir tushadi:<br><br>
<em>-ku, axir</em> &nbsp;→&nbsp; <b>же · ведь</b><br>
<em>nahotki</em> &nbsp;→&nbsp; <b>неуже́ли</b><br>
<em>hatto</em> &nbsp;→&nbsp; <b>да́же</b><br>
<em>faqat</em> &nbsp;→&nbsp; <b>то́лько · лишь</b><br>
<em>shunchaki</em> &nbsp;→&nbsp; <b>про́сто</b><br>
<em>xoʻsh</em> &nbsp;→&nbsp; <b>ну</b><br>
<em>mana</em> &nbsp;→&nbsp; <b>вот</b><br><br>
Yagona eʼtibor beriladigan narsa — <b>oʻrni</b>. Oʻzbekcha
qoʻshimchalar (<em>-ku, -chi</em>) soʻzga yopishadi, ruscha
yuklamalar esa <b>alohida</b> yoziladi — lekin baribir oʻsha
soʻzning yonida turadi.</div>

<h3>6. Yuklama -то — PR-78 dagi emas</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">-ТО noaniqlik (PR-78)</p>
    <p><em><b>Кто́-то</b> звони́л.</em><br>Kimdir qoʻngʻiroq qildi.</p>
    <p>Savol soʻziga yopishadi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">-ТО taʼkid (bu dars)</p>
    <p><em><b>Я-то</b> зна́ю.</em><br>Men-ku bilaman.</p>
    <p>Oddiy soʻzga yopishadi va uni ajratib koʻrsatadi.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Qanday ajratish</span>
Qaraysiz: <em>-то</em> <b>savol soʻziga</b> yopishganmi
(<em>кто, что, где, когда́</em>)? Unda bu <b>noaniqlik</b>.<br><br>
Oddiy soʻzga yopishganmi (<em>я, он, кни́га, сего́дня</em>)? Unda
bu <b>taʼkid</b>:<br>
<em><b>Кни́гу-то</b> ты прочита́л?</em> — Kitobni-chi, oʻqidingmi?</div>

<h3>7. Meʼyor</h3>

<div class="pe-call pe-warn"><span class="pe-call__t">Koʻp qoʻysangiz — gʻalati</span>
Yuklamalar tuz kabi: ozi taomni ochadi, koʻpi buzadi.<br><br>
<s>Ну вот я же ведь про́сто уж говори́л же!</s> — bunday
gapirilmaydi.<br>
<b>Я же говори́л!</b> — yetarli.<br><br>
Bitta gapda odatda <b>bitta</b> yuklama boʻladi, kamdan-kam
ikkita.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я говори́л же!</s></p>
  <p class="pe-good">Я <b>же</b> говори́л! — <em>же</em> taʼkidlanayotgan soʻzdan keyin</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Неуже́ли он придёт ли?</s></p>
  <p class="pe-good">Неуже́ли он придёт? — <em>ли</em> (PR-68) bilan birga ishlatilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Же ты зна́ешь.</s></p>
  <p class="pe-good">Ты <b>же</b> зна́ешь — <em>же</em> gapni boshlamaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кто́-то зна́ю.</s> <em>(«men-ku bilaman»)</em></p>
  <p class="pe-good"><b>Я-то</b> зна́ю — taʼkid uchun <em>-то</em> oddiy soʻzga qoʻshiladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu gapni ruschaga oʻgiring. &nbsp; <b>Aytdim-ku!</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я же говори́л!</strong>
    Oʻzbekcha <em>-ku</em> = ruscha <em>же</em>, va u
    taʼkidlanayotgan soʻzdan keyin turadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>Ра́зве</b> yoki <b>неуже́ли</b>? &nbsp;
     <b>___ он сдал экза́мен без подгото́вки?!</b> (juda hayronman)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Неуже́ли</strong> — kuchli
    hayrat, «nahotki». <em>Ра́зве</em> yumshoqroq boʻlardi:
    «rostdanmi?».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapdagi <b>-то</b> bir xilmi?<br>
     <b>Кто́-то звони́л. · Я-то зна́ю.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Yoʻq.</strong> Birinchisi —
    <b>noaniqlik</b> (PR-78), savol soʻziga yopishgan.
    Ikkinchisi — <b>taʼkid</b>, oddiy olmoshga yopishgan:
    «men-ku bilaman».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Javob bering. &nbsp; <b>— Он опозда́л на де́сять мину́т.</b>
     (sizga farqi yoʻq)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>— Ну и что?</strong> —
    «Nima boʻpti?». Yumshoqroq variant: <em>Ну ла́дно</em> —
    «mayli boʻlmasa».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Axir sen uni bilasan-ku. Hatto men ham bilaman.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ты же его́ зна́ешь. Да́же я
    зна́ю.</strong> Yoki <em>Ты ведь его́ зна́ешь</em>. «Hatto» —
    <em>да́же</em>, va u taʼkidlanayotgan soʻzdan
    <b>oldin</b> turadi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>же</b><span>-ku, axir</span></li>
  <li><b>ведь</b><span>axir, oʻzing bilasan</span></li>
  <li><b>ра́зве</b><span>rostdanmi?</span></li>
  <li><b>неуже́ли</b><span>nahotki</span></li>
  <li><b>да́же</b><span>hatto</span></li>
  <li><b>то́лько / лишь</b><span>faqat</span></li>
  <li><b>про́сто</b><span>shunchaki</span></li>
  <li><b>Ну и что?</b><span>Nima boʻpti?</span></li>
  <li><b>Ну ла́дно.</b><span>Mayli boʻlmasa.</span></li>
  <li><b>Вот и всё.</b><span>Mana, hammasi.</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Yuklamalar <b>maʼno emas, munosabat</b> qoʻshadi.</li>
    <li><b>Же = oʻzbekcha «-ku»</b>, va u taʼkidlanayotgan soʻzdan
        <b>keyin</b> turadi. Gapni boshlamaydi.</li>
    <li><b>Ведь</b> — «axir, oʻzing bilasan»; gap boshida ham tura
        oladi.</li>
    <li><b>Неуже́ли = nahotki</b> (kuchli hayrat),
        <b>ра́зве</b> = «rostdanmi?» (yumshoqroq).</li>
    <li>Yuklama <b>-то</b> oddiy soʻzga yopishadi va uni ajratadi:
        <em>я-то зна́ю</em>. PR-78 dagisi savol soʻziga
        yopishadi.</li>
    <li>Bitta gapda <b>bitta</b> yuklama yetarli.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-85: Undov soʻzlar va jonli soʻzlashuv nutqi",
        "category": "russian",
        "order": 85,
        "summary": (
            "Kitobdagi rus tili bilan koʻchadagi rus tili orasidagi farq: "
            "«здра́вствуйте» → [здра́сьте], «сейча́с» → [щас]. Bizda ham shunday."
        ),
        "stories": ["Разговор в такси"],
        "content": """
<h2>PR-85: Undov soʻzlar va jonli soʻzlashuv nutqi</h2>

<p>Siz sakson toʻrtta dars oʻqidingiz va endi ruscha yozilgan matnni
tushunasiz. Lekin birinchi marta Moskvada avtobusga chiqsangiz,
qandaydir <em>«щас паеду»</em> degan narsani eshitasiz va hech narsa
tushunmaysiz. Bu boshqa til emas — bu <b>oʻsha til, tez
gapirilgani</b>. Bu darsda ana shu farqni koʻramiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Ogʻzaki qisqarishlarni tanib olasiz: <b>щас, здра́сьте, што</b></li>
    <li>Suhbat toʻldiruvchilarini olasiz: <b>коро́че, в о́бщем, слу́шай</b></li>
    <li>Tabiiy javob berasiz: <b>Да ла́дно! Ничего́ себе́! Я́сно.</b></li>
    <li>Norasmiy xayrlashuvni oʻrganasiz — <b>«Дава́й!»</b></li>
    <li>Qaysi soʻzni <b>tanish</b>-u, qaysinisini <b>ishlatmaslik</b> kerakligini bilasiz</li>
  </ul>
</div>

<h3>1. Yozilishi ↔ aytilishi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Yoziladi</th><th>Aytiladi</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">здра́вствуйте</td><td class="pr-res">[здра́сьте]</td>
      <td class="pr-uz">assalomu alaykum</td></tr>
  <tr><td class="pr-stem">сейча́с</td><td class="pr-res">[щас]</td>
      <td class="pr-uz">hozir</td></tr>
  <tr><td class="pr-stem">что</td><td class="pr-res">[што]</td>
      <td class="pr-uz">nima</td></tr>
  <tr><td class="pr-stem">коне́чно</td><td class="pr-res">[коне́шно]</td>
      <td class="pr-uz">albatta</td></tr>
  <tr><td class="pr-stem">ты́сяча</td><td class="pr-res">[ты́ща]</td>
      <td class="pr-uz">ming</td></tr>
  <tr><td class="pr-stem">когда́ / тогда́</td><td class="pr-res">[кагда́ / тагда́]</td>
      <td class="pr-uz">qachon / oʻshanda</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bizda ham xuddi shunday</span>
Bu hodisadan qoʻrqmang — oʻzbek tilida ham aynan shu narsa
boʻladi:<br><br>
<em>ke<b>layapti</b></em> → [ke<b>votti</b>]<br>
<em>nima qi<b>lyapsan</b></em> → [nima qi<b>vossan</b>]<br>
<em>bo<b>ryapman</b></em> → [bo<b>voman</b>]<br><br>
Hech kim buni yozmaydi, lekin hamma shunday gapiradi. Ruschada
ham xuddi shunday: <b>[щас]</b> deb aytiladi, lekin
<b>«сейча́с»</b> deb yoziladi.<br><br>
Sizga vazifa bitta: bularni <b>tanib olish</b>. Ishlatishingiz
shart emas — sekin va toʻliq gapirsangiz, hech kim gʻalati deb
oʻylamaydi.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Yozmang</span>
Bu shakllar faqat <b>ogʻzaki</b>. Xat, xabar yoki ishdagi
yozishmada <s>щас</s> deb yozish — savodsizlik belgisi.<br><br>
Yagona istisno: badiiy matnda <b>dialog</b> ichida —
yozuvchi qahramonning ovozini koʻrsatish uchun shunday
yozishi mumkin.</div>

<h3>2. Suhbat toʻldiruvchilari</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Maʼnosi</th><th>Qachon ishlatiladi</th></tr>
  <tr><td class="pr-stem">коро́че</td><td class="pr-uz">qisqasi</td>
      <td class="pr-res">uzun hikoyani yakunlashda</td></tr>
  <tr><td class="pr-stem">в о́бщем</td><td class="pr-uz">umuman olganda</td>
      <td class="pr-res">xulosa qilishda</td></tr>
  <tr><td class="pr-stem">слу́шай</td><td class="pr-uz">eshit, qara</td>
      <td class="pr-res">yangi mavzu boshlashda</td></tr>
  <tr><td class="pr-stem">зна́ешь</td><td class="pr-uz">bilasanmi</td>
      <td class="pr-res">fikrni yumshatishda</td></tr>
  <tr><td class="pr-stem">зна́чит</td><td class="pr-uz">demak</td>
      <td class="pr-res">tushuntirishni boshlashda</td></tr>
  <tr><td class="pr-stem">как бы</td><td class="pr-uz">qandaydir</td>
      <td class="pr-res">aniq aytolmaganda</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Коро́че — eng koʻp eshitiladigani</span>
<b>Коро́че</b> soʻzma-soʻz «qisqaroq» degani (PR-74 dagi qiyosiy
daraja), lekin nutqda u <b>«qisqasi»</b> vazifasini
bajaradi:<br><br>
<em>— Ну и что бы́ло да́льше?<br>
— <b>Коро́че</b>, мы опозда́ли.</em><br>
— Xoʻsh, keyin nima boʻldi? — Qisqasi, kechikdik.<br><br>
Yoshlar orasida u shu qadar koʻp ishlatiladiki, baʼzan
maʼnosini butunlay yoʻqotadi.</div>

<div class="pe-ex">
  <p class="pe-ex__t">Toʻldiruvchilar ish ustida</p>
  <p class="pe-ex__ru">— <b>Слу́шай</b>, а ты за́втра свобо́ден?</p>
  <p class="pe-ex__uz">— Eshit, ertaga boʻshmisan?</p>
  <p class="pe-ex__ru">— <b>Зна́чит</b>, так. Снача́ла в банк, пото́м на по́чту.</p>
  <p class="pe-ex__uz">— Demak, shunday. Avval bankka, keyin pochtaga.</p>
  <p class="pe-ex__ru">— <b>Коро́че</b>, мы опозда́ли на по́езд.</p>
  <p class="pe-ex__uz">— Qisqasi, poyezdga kechikdik.</p>
</div>

<h3>3. Tabiiy javoblar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Ibora</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">Да ла́дно!</td><td class="pr-uz">Qoʻysang-chi!</td>
      <td class="pr-stem">Я́сно.</td><td class="pr-uz">Tushunarli.</td></tr>
  <tr><td class="pr-stem">Ничего́ себе́!</td><td class="pr-uz">Voy-boʻy!</td>
      <td class="pr-stem">Поня́тно.</td><td class="pr-uz">Tushundim.</td></tr>
  <tr><td class="pr-stem">Серьёзно?</td><td class="pr-uz">Jiddiymi?</td>
      <td class="pr-stem">То́чно!</td><td class="pr-uz">Aynan!</td></tr>
  <tr><td class="pr-stem">Коне́чно!</td><td class="pr-uz">Albatta!</td>
      <td class="pr-stem">Вряд ли.</td><td class="pr-uz">Dargumon.</td></tr>
  <tr><td class="pr-stem">Ничего́!</td><td class="pr-uz">Hechqisi yoʻq!</td>
      <td class="pr-stem">Договори́лись.</td><td class="pr-uz">Kelishdik.</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__t">Suhbatda</p>
  <p class="pe-ex__ru">— Я вчера́ ви́дел Ди́му. — <b>Да ла́дно!</b> Он же уе́хал.</p>
  <p class="pe-ex__uz">— Kecha Dimani koʻrdim. — Qoʻysang-chi! U-ku ketgan edi.</p>
  <p class="pe-ex__ru">— Извини́, я опозда́л. — <b>Ничего́!</b></p>
  <p class="pe-ex__uz">— Kechirasiz, kechikdim. — Hechqisi yoʻq!</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Javoblar ham bir-bir tushadi</span>
Bu jadvaldagi iboralarni tarjima qilib oʻtirish shart emas —
oʻzbekchada ularning tayyor juftligi bor:<br><br>
<em>Qoʻysang-chi!</em> &nbsp;→&nbsp; <b>Да ла́дно!</b><br>
<em>Voy-boʻy!</em> &nbsp;→&nbsp; <b>Ничего́ себе́!</b><br>
<em>Tushunarli.</em> &nbsp;→&nbsp; <b>Я́сно.</b><br>
<em>Hechqisi yoʻq!</em> &nbsp;→&nbsp; <b>Ничего́!</b><br>
<em>Kelishdik.</em> &nbsp;→&nbsp; <b>Договори́лись.</b><br><br>
Ularni <b>butun holda</b> yodlang, boʻlaklarga ajratmang.
<em>«Ничего́ себе́»</em> soʻzma-soʻz «oʻziga hech narsa» degani
va bu hech narsani tushuntirmaydi — u shunchaki hayrat
undovi.</div>

<h3>4. Salomlashish va xayrlashuv</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Rasmiy (вы)</p>
    <p><em>Здра́вствуйте · До свида́ния · Всего́ до́брого</em></p>
    <p>Notanish odam, katta yoshli, ish joyi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Norasmiy (ты)</p>
    <p><em>Приве́т · Пока́ · Дава́й · Уви́димся</em></p>
    <p>Doʻst, tengdosh, oila.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">«Дава́й!» — xayr degani</span>
Bu oʻquvchilarni har doim hayron qoldiradi. <em>Дава́й</em>
«ber» degan feʼl, lekin telefon oxirida yoki koʻchada
xayrlashayotganda u <b>«xayr»</b> maʼnosini beradi:<br><br>
<em>— Ну ла́дно, я побежа́л. <b>Дава́й!</b><br>
— <b>Дава́й</b>, пока́!</em><br><br>
Faqat <b>norasmiy</b> — direktorga <em>«Дава́й!»</em> deb
boʻlmaydi.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bu yerda oʻzbekcha yordam bermaydi</span>
Bu darsdagi bir necha narsaning oʻzbekchada <b>juftligi
yoʻq</b> — ularni shunchaki yodlash kerak:<br><br>
<b>«Дава́й!»</b> = xayr. Oʻzbekchada «ber» soʻzi bilan
xayrlashilmaydi, shuning uchun buni mantiq bilan chiqarib
boʻlmaydi.<br><br>
<b>«Коро́че»</b> = qisqasi. Soʻzma-soʻz «qisqaroq» — qiyosiy
daraja (PR-74), lekin nutqda butunlay boshqa vazifada.<br><br>
Va aksincha: oʻzbekchadagi <em>«xoʻp»</em>, <em>«boʻpti»</em>,
<em>«mayli»</em> — uchalasi ham ruschada koʻpincha bitta
<b>«ла́дно»</b> ga tushadi.<br><br>
Yaʼni bu dars — grammatika emas, <b>quloq</b>. Rus filmini
subtitrsiz koʻrishga urinib koʻring: bir haftada shu
soʻzlarning yarmini oʻzingiz ilib olasiz.</div>

<h3>5. Muloyimlik — qisqartirmang</h3>

<p>Jonli nutq qisqa boʻlishi mumkin, lekin <b>iltimos</b>
har doim toʻliq va yumshoq boʻlishi kerak.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Yumshoq soʻrash</p>
  <p class="pe-ex__ru"><b>Извини́те, вы не подска́жете</b>, где метро́?</p>
  <p class="pe-ex__uz">Kechirasiz, metro qayerdaligini aytib yubormaysizmi?</p>
  <p class="pe-ex__ru"><b>Мо́жно</b> вас спроси́ть?</p>
  <p class="pe-ex__uz">Sizdan soʻrasam maylimi?</p>
  <p class="pe-ex__why">Inkor shakli (<em>не подска́жете</em>)
     rus tilida soʻrovni <b>yumshatadi</b> — bu xato emas, bu
     odob.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Taniysiz, lekin ishlatmaysiz</span>
Koʻchada tez-tez eshitiladigan bir soʻz bor —
<b>«блин»</b>. U qoʻpol soʻz emas, lekin madaniyatli nutqda
oʻrni yoʻq: taxminan oʻzbekcha <em>«e, attang»</em> ning
qoʻpolroq varianti.<br><br>
Uni <b>tanib oling</b> — filmda yoki koʻchada eshitasiz. Lekin
oʻzingiz ishlatmang, ayniqsa notanish odam bilan yoki ish
joyida.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Здра́сьте, я хочу́ пода́ть заявле́ние.</s>
     <em>(rasmiy joyda)</em></p>
  <p class="pe-good"><b>Здра́вствуйте</b> — rasmiy holatda toʻliq shakl</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я щас приду́.</s> <em>(xat yoki xabarda)</em></p>
  <p class="pe-good">Я <b>сейча́с</b> приду́ — [щас] faqat ogʻzaki</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Дава́й!</s> <em>(direktorga)</em></p>
  <p class="pe-good"><b>До свида́ния</b> — <em>дава́й</em> faqat doʻstlar bilan</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Где метро́?</s> <em>(notanish odamga)</em></p>
  <p class="pe-good"><b>Извини́те, вы не подска́жете</b>, где метро́? — yumshoqroq</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu qanday yoziladi? &nbsp; <b>[щас]</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>сейча́с</strong>. Ogʻzaki
    nutqda ikki boʻgʻin bittaga siqiladi. Yozganda esa har
    doim toʻliq shakl.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Doʻstingiz telefonda «<b>Ну всё, дава́й!</b>» dedi. Nima
     demoqchi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>«Xoʻp, xayr!»</strong>
    <em>Дава́й</em> bu yerda «ber» emas, norasmiy
    xayrlashuv. Javoban siz ham <em>«Дава́й, пока́!»</em>
    deysiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Javob bering. &nbsp; <b>— Извини́, я разби́л твою́ ча́шку.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>— Ничего́!</strong> yoki
    <strong>— Ничего́ стра́шного.</strong> — «Hechqisi yoʻq»
    (PR-79). Bu eng koʻp eshitiladigan javoblardan
    biri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Koʻchada notanish odamdan yoʻl soʻramoqchisiz. Qaysi biri
     yaxshiroq?<br>
     <b>«Где вокза́л?»</b> yoki <b>«Извини́те, вы не подска́жете,
     где вокза́л?»</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ikkinchisi.</strong>
    Birinchisi grammatik toʻgʻri, lekin quruq eshitiladi.
    <em>Извини́те</em> va inkor shakli
    (<em>не подска́жете</em>) soʻrovni yumshatadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu suhbatni tugating.<br>
     <b>— Я вчера́ встре́тил Афсо́ну в Москве́!<br>— ___</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Masalan: <strong>— Да ла́дно!
    Серьёзно?</strong> yoki <strong>— Ничего́ себе́!</strong> —
    ikkalasi ham hayratni bildiradi va jonli nutqda juda
    tabiiy.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>[щас]</b><span>сейча́с ning ogʻzaki shakli</span></li>
  <li><b>[здра́сьте]</b><span>здра́вствуйте ning ogʻzaki shakli</span></li>
  <li><b>коро́че</b><span>qisqasi</span></li>
  <li><b>в о́бщем</b><span>umuman olganda</span></li>
  <li><b>слу́шай</b><span>eshit, qara</span></li>
  <li><b>Да ла́дно!</b><span>Qoʻysang-chi!</span></li>
  <li><b>Ничего́ себе́!</b><span>Voy-boʻy!</span></li>
  <li><b>Дава́й!</b><span>Xayr! (norasmiy)</span></li>
  <li><b>Договори́лись.</b><span>Kelishdik.</span></li>
  <li><b>не подска́жете</b><span>aytib yubormaysizmi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Ogʻzaki qisqarishlar — <b>tanib oling, lekin yozmang</b>:
        [щас], [здра́сьте], [што].</li>
    <li>Bu hodisa oʻzbekchada ham bor: <em>kelayapti →
        kevotti</em>.</li>
    <li>Toʻldiruvchilar: <b>коро́че, в о́бщем, слу́шай,
        зна́чит</b>.</li>
    <li>Javoblar: <b>Да ла́дно! · Ничего́ себе́! · Я́сно ·
        Ничего́!</b></li>
    <li><b>«Дава́й!»</b> = xayr, faqat doʻstlar bilan.</li>
    <li>Iltimosni <b>qisqartirmang</b>: <em>Извини́те, вы не
        подска́жете…</em> — inkor shakli odobni bildiradi.</li>
  </ul>
</div>
""",
    },
]
