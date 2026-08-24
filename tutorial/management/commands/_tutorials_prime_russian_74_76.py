# -*- coding: utf-8 -*-
"""Prime Russian — Block F yakuni va Block G boshlanishi (74–76).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-74 — sifat darajalari. Blok F ni yopadi. Oʻzbekcha tayanch juda toza:
«Toshkent<b>dan</b> katta» ↔ «бо́льше Ташке́нт<b>а</b>» — ikkala tilda ham
solishtiriladigan narsa QOʻSHIMCHA oladi (bizda -dan, ularda Р.п.).
«Eng» esa aynan «са́мый».
PR-75 — свой. Blok G ochiladi. Bu kursning eng katta sovgʻalaridan biri:
oʻzbekchada «oʻz» bor, ingliz tilida esa umuman yoʻq. Oʻzbek oʻquvchisi
«U OʻZ kitobini oldi» bilan «U UNING kitobini oldi» ni bir zumda ajratadi.
PR-76 — себя va сам. Yana «oʻz» oilasidan, lekin bu safar oʻzbekcha bitta
soʻz (oʻzim / oʻzini) rus tilida IKKIGA boʻlinadi: себя́ — toʻldiruvchi,
сам — taʼkid. Butun dars shu chiziqni chizishga qaratilgan.

Mashqlar:        practice/management/commands/_practice_pr_74_76.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_74_76.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_74_76.py --author=prime
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
        "title": "PR-74: Sifat darajalari: больше, самый, лучше, наиболее, чем",
        "category": "russian",
        "order": 74,
        "summary": (
            "Oʻzbekcha «-dan katta» ruschada «бо́льше + Роди́тельный» boʻladi, «eng» "
            "esa «са́мый». Qolgani — soʻzning oʻzi oʻzgarishi."
        ),
        "stories": ["Са́мая дли́нная река́"],
        "content": """
<h2>PR-74: Sifat darajalari: больше, самый, лучше, наиболее, чем</h2>

<p>Oʻzbekchada solishtirish juda oson: sifat <b>oʻzgarmaydi</b>,
faqat solishtiriladigan narsaga <b>-dan</b> qoʻshiladi —
<em>«Toshkent<b>dan</b> katta»</em>. Rus tilida esa <b>sifatning
oʻzi</b> oʻzgaradi: <em>большо́й → <b>бо́льше</b></em>. Mana shu
oʻzgarish bu darsning asosiy ishi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Qiyosiy darajani yasaysiz: <b>интере́сный → интере́снее</b></li>
    <li>Undosh almashinadigan guruhni oʻrganasiz: <b>дорого́й → доро́же</b></li>
    <li>Beshta notoʻgʻri shaklni yodlaysiz: <b>лу́чше, ху́же, бо́льше, ме́ньше, ста́рше</b></li>
    <li>Ikki xil solishtirish yoʻlini bilasiz: <b>чем</b> va <b>Роди́тельный</b></li>
    <li>Orttirma darajani qoʻyasiz: <b>са́мый</b>, <b>всех</b>, <b>всего́</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qiyosiy</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">-ее</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">интере́снее</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Orttirma</span>
  <span class="pe-chip pe-chip--s">са́мый</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">toʻliq sifat</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">са́мый большо́й</span>
</div>

<h3>1. Qiyosiy daraja: -ее</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Sifat</th><th>Qiyosiy</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">интере́сный</td><td class="pr-res">интере́снее</td>
      <td class="pr-end">qiziqarliroq</td></tr>
  <tr><td class="pr-stem">краси́вый</td><td class="pr-res">краси́вее</td>
      <td class="pr-end">chiroyliroq</td></tr>
  <tr><td class="pr-stem">тру́дный</td><td class="pr-res">трудне́е</td>
      <td class="pr-end">qiyinroq</td></tr>
  <tr><td class="pr-stem">бы́стрый</td><td class="pr-res">быстре́е</td>
      <td class="pr-end">tezroq</td></tr>
  <tr><td class="pr-stem">у́мный</td><td class="pr-res">умне́е</td>
      <td class="pr-end">aqlliroq</td></tr>
  <tr><td class="pr-stem">дли́нный</td><td class="pr-res">длинне́е</td>
      <td class="pr-end">uzunroq</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Urgʻu</span>
Ikki boʻgʻinli qisqa sifatlarda urgʻu <b>-е́е</b> ga koʻchadi:
<em>трудн<b>е́</b>е, быстр<b>е́</b>е, умн<b>е́</b>е,
сильн<b>е́</b>е</em>.<br><br>
Uzunroq sifatlarda esa oʻz joyida qoladi:
<em>крас<b>и́</b>вее, интер<b>е́</b>снее</em>.</div>

<h3>2. Undosh almashadigan guruh: -е</h3>

<p>Oʻzak <b>г, к, х, д, т, ст</b> bilan tugasa, qoʻshimcha <b>-е</b>
boʻladi va oxirgi undosh <b>almashadi</b>. Bu guruh kichik, lekin
undagi soʻzlar juda koʻp ishlatiladi — yodlash kerak.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Sifat</th><th>Qiyosiy</th><th>Maʼnosi</th><th>Sifat</th><th>Qiyosiy</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">дорого́й</td><td class="pr-res">доро́же</td><td class="pr-end">qimmatroq</td>
      <td class="pr-stem">молодо́й</td><td class="pr-res">моло́же</td><td class="pr-end">yoshroq</td></tr>
  <tr><td class="pr-stem">высо́кий</td><td class="pr-res">вы́ше</td><td class="pr-end">balandroq</td>
      <td class="pr-stem">ни́зкий</td><td class="pr-res">ни́же</td><td class="pr-end">pastroq</td></tr>
  <tr><td class="pr-stem">бли́зкий</td><td class="pr-res">бли́же</td><td class="pr-end">yaqinroq</td>
      <td class="pr-stem">далёкий</td><td class="pr-res">да́льше</td><td class="pr-end">uzoqroq</td></tr>
  <tr><td class="pr-stem">широ́кий</td><td class="pr-res">ши́ре</td><td class="pr-end">kengroq</td>
      <td class="pr-stem">у́зкий</td><td class="pr-res">у́же</td><td class="pr-end">torroq</td></tr>
  <tr><td class="pr-stem">глубо́кий</td><td class="pr-res">глу́бже</td><td class="pr-end">chuqurroq</td>
      <td class="pr-stem">коро́ткий</td><td class="pr-res">коро́че</td><td class="pr-end">qisqaroq</td></tr>
  <tr><td class="pr-stem">лёгкий</td><td class="pr-res">ле́гче</td><td class="pr-end">yengilroq</td>
      <td class="pr-stem">кре́пкий</td><td class="pr-res">кре́пче</td><td class="pr-end">mustahkamroq</td></tr>
  <tr><td class="pr-stem">ти́хий</td><td class="pr-res">ти́ше</td><td class="pr-end">jimroq</td>
      <td class="pr-stem">бога́тый</td><td class="pr-res">бога́че</td><td class="pr-end">boyroq</td></tr>
  <tr><td class="pr-stem">ча́стый</td><td class="pr-res">ча́ще</td><td class="pr-end">tez-tezroq</td>
      <td class="pr-stem">ре́дкий</td><td class="pr-res">ре́же</td><td class="pr-end">kamroq</td></tr>
</table></div>

<h3>3. Beshta notoʻgʻri shakl</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Sifat</th><th>Qiyosiy</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">хоро́ший</td><td class="pr-res">лу́чше</td><td class="pr-end">yaxshiroq</td></tr>
  <tr><td class="pr-stem">плохо́й</td><td class="pr-res">ху́же</td><td class="pr-end">yomonroq</td></tr>
  <tr><td class="pr-stem">большо́й</td><td class="pr-res">бо́льше</td><td class="pr-end">kattaroq, koʻproq</td></tr>
  <tr><td class="pr-stem">ма́ленький</td><td class="pr-res">ме́ньше</td><td class="pr-end">kichikroq, kamroq</td></tr>
  <tr><td class="pr-stem">ста́рый</td><td class="pr-res">ста́рше</td><td class="pr-end">kattaroq (yoshda)</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Ста́рше yoki старе́е?</span>
<b>Ста́рше</b> — <b>odam</b> haqida: <em>Он ста́рше меня́</em> —
mendan katta.<br>
<b>Старе́е</b> — <b>narsa</b> haqida: <em>Э́тот дом старе́е</em> —
bu uy eskiroq.<br><br>
Oʻzbekchada ham shunday: odam «katta», narsa «eski».</div>

<h3>4. Ikki xil solishtirish</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">ЧЕМ + Имени́тельный</p>
    <p><em>Москва́ бо́льше<b>,</b> чем Ташке́нт.</em></p>
    <p>Vergul <b>majburiy</b>. Har doim ishlaydi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Роди́тельный, чем siz</p>
    <p><em>Москва́ бо́льше Ташке́нт<b>а</b>.</em></p>
    <p>Qisqaroq va tabiiyroq. Faqat bitta ot bilan.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha — toza moslik</span>
Ikkinchi yoʻl oʻzbekchaning <b>aynan oʻzi</b>. Ikkala tilda ham
solishtiriladigan narsa <b>qoʻshimcha oladi</b>:<br><br>
<em>Toshkent<b>dan</b> katta</em> &nbsp;→&nbsp; <b>бо́льше
Ташке́нт<b>а</b></b> (Роди́тельный)<br>
<em>men<b>dan</b> yosh</em> &nbsp;→&nbsp; <b>моло́же мен<b>я́</b></b><br>
<em>bu kitob<b>dan</b> qiziqarli</em> &nbsp;→&nbsp; <b>интере́снее
э́т<b>ой</b> кни́г<b>и</b></b><br><br>
Yaʼni oʻzbekcha <b>-dan</b> = ruscha <b>Роди́тельный</b>. Bu
mosligni bir marta koʻrsangiz, boshqa unutmaysiz.<br><br>
<b>Чем</b> esa oʻzbekcha «<em>…ga qaraganda</em>», «<em>…dan
koʻra</em>» ga toʻgʻri keladi va undan keyin ot
<b>oʻzgarmaydi</b>.</div>

<h3>5. На + Вини́тельный — qancha farq bilan</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Farqni aytish</p>
  <p class="pe-ex__ru">Он <b>на два го́да</b> ста́рше меня́.</p>
  <p class="pe-ex__uz">U mendan ikki yosh katta.</p>
  <p class="pe-ex__ru">Э́та су́мка <b>на ты́сячу</b> доро́же.</p>
  <p class="pe-ex__uz">Bu sumka ming soʻm qimmatroq.</p>
  <p class="pe-ex__why">Oʻzbekchada hech qanday belgi yoʻq — «ikki
     yosh katta». Ruschada esa <b>на</b> qoʻyilishi shart.</p>
</div>

<h3>6. Бо́лее + toʻliq sifat</h3>

<p>Bu joyni koʻpchilik bilmaydi. Oddiy qiyosiy shakl
(<em>интере́снее</em>) <b>faqat kesim</b> boʻla oladi — otdan oldin
turolmaydi. Otni aniqlash kerak boʻlsa, <b>бо́лее</b> + toʻliq sifat
ishlatiladi.</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Kesim — oddiy shakl</p>
    <p><em>Э́та кни́га <b>интере́снее</b>.</em><br>Bu kitob qiziqarliroq.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Aniqlovchi — бо́лее</p>
    <p><em>Дай мне <b>бо́лее интере́сную</b> кни́гу.</em><br>Menga qiziqarliroq kitob ber.</p>
    <p><s>интере́снее кни́гу</s> — bunday boʻlmaydi.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">Bir fikr, uch xil aytilishi</p>
  <p class="pe-ex__ru">Э́тот путь <b>коро́че</b>.</p>
  <p class="pe-ex__uz">Bu yoʻl qisqaroq. — kesim, oddiy shakl.</p>
  <p class="pe-ex__ru">Э́тот путь <b>коро́че</b> того́.</p>
  <p class="pe-ex__uz">Bu yoʻl undan qisqaroq. — Роди́тельный bilan.</p>
  <p class="pe-ex__ru">Мы вы́брали <b>бо́лее коро́ткий</b> путь.</p>
  <p class="pe-ex__uz">Biz qisqaroq yoʻlni tanladik. — aniqlovchi, demak бо́лее.</p>
</div>

<h3>7. Orttirma daraja</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shakl</th><th>Uslub</th><th>Misol</th></tr>
  <tr><td class="pr-stem">са́мый + sifat</td><td class="pr-uz">hamma joyda</td>
      <td class="pr-res">са́мый большо́й го́род</td></tr>
  <tr><td class="pr-stem">наибо́лее + sifat</td><td class="pr-uz">rasmiy, ilmiy</td>
      <td class="pr-res">наибо́лее ва́жный вопро́с</td></tr>
  <tr><td class="pr-stem">-е́йший / -а́йший</td><td class="pr-uz">kitobiy</td>
      <td class="pr-res">интере́снейший, велича́йший</td></tr>
  <tr><td class="pr-stem">qiyosiy + всех</td><td class="pr-uz">ogʻzaki</td>
      <td class="pr-res">Он бе́гает быстре́е всех.</td></tr>
  <tr><td class="pr-stem">qiyosiy + всего́</td><td class="pr-uz">ogʻzaki</td>
      <td class="pr-res">Бо́льше всего́ я люблю́ ле́то.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Всех yoki всего́?</span>
<b>Всех</b> — <b>odamlar</b> yoki sanaladigan narsalar bilan
solishtirganda: <em>Он бе́гает быстре́е <b>всех</b></em> —
hammadan tez yuguradi.<br><br>
<b>Всего́</b> — <b>ish yoki umuman narsalar</b> bilan:
<em>Бо́льше <b>всего́</b> я люблю́ ле́то</em> — hammadan koʻproq
yozni yaxshi koʻraman.<br><br>
Sinov: «hamma<b>dan</b>» → всех. «hamma narsa<b>dan</b>» →
всего́.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">«Eng» = са́мый</span>
Orttirma daraja oʻzbek oʻquvchisi uchun deyarli bepul:
oʻzbekcha <b>«eng»</b> ruscha <b>«са́мый»</b> ga bir-bir
tushadi.<br><br>
<em><b>eng</b> katta shahar</em> → <b>са́мый</b> большо́й го́род<br>
<em><b>eng</b> chiroyli</em> → <b>са́мая</b> краси́вая<br><br>
Bitta farq bor: oʻzbekcha «eng» oʻzgarmaydi, ruscha
<em>са́мый</em> esa <b>sifat kabi turlanadi</b> — jinsda, sonda,
kelishikda: <em>в са́мом большо́м го́роде</em>, <em>о са́мой
дли́нной реке́</em>.</div>

<h3>8. Kuchaytiruvchi soʻzlar</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Qanchalik farq</p>
  <p class="pe-ex__ru">Здесь <b>гора́здо</b> ти́ше. · Здесь <b>намно́го</b> ти́ше.</p>
  <p class="pe-ex__uz">Bu yerda ancha jimroq.</p>
  <p class="pe-ex__ru">Стань <b>чуть</b> бли́же. · Так <b>ещё</b> лу́чше.</p>
  <p class="pe-ex__uz">Biroz yaqinroq tur. · Bunisi yanayam yaxshi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Nima yangi, nima yoʻq</span>
Bu darsda oʻzbek oʻquvchisi uchun <b>yangi narsa bittagina</b>:
sifatning oʻzi oʻzgarishi.<br><br>
Oʻzbekchada <em>katta</em> soʻzi hech qachon oʻzgarmaydi —
<em>katta</em>, <em>kattaroq</em>, <em>eng katta</em> da ham oʻzagi
bitta. Ruschada esa <em>большо́й</em> solishtirilganda butunlay
boshqa soʻzga aylanadi — <b>бо́льше</b>.<br><br>
Shuning uchun 2- va 3-boʻlimdagi jadvallarni yodlash kerak. Qolgan
hamma narsa — <em>-dan</em> ↔ Роди́тельный, <em>eng</em> ↔
<em>са́мый</em> — sizda allaqachon bor.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Москва́ бо́льше чем Ташке́нт.</s></p>
  <p class="pe-good">Москва́ бо́льше<b>,</b> чем Ташке́нт — <em>чем</em> dan oldin vergul</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Москва́ бо́льше Ташке́нт.</s></p>
  <p class="pe-good">Москва́ бо́льше <b>Ташке́нта</b> — <em>чем</em> siz Роди́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он бо́лее ста́рше меня́.</s></p>
  <p class="pe-good">Он <b>ста́рше</b> меня́ — ikki marta qiyosiy daraja qoʻyilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Дай мне интере́снее кни́гу.</s></p>
  <p class="pe-good">Дай мне <b>бо́лее интере́сную</b> кни́гу — otdan oldin бо́лее kerak</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Qiyosiy shaklni yasang. &nbsp; <b>дорого́й</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>доро́же</strong>. Oʻzak
    <b>-г</b> bilan tugagan, demak <b>-е</b> qoʻshimchasi va
    undosh almashinadi: <em>г → ж</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Ikki xil yoʻl bilan ayting. &nbsp; <b>Amudaryo Zarafshondan
     uzun.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Амударья́ длинне́е
    Зеравша́на.</strong> (Роди́тельный) yoki <strong>Амударья́
    длинне́е, чем Зеравша́н.</strong> (чем + И.п., vergul
    bilan). Ikkalasi ham toʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>Всех</b> yoki <b>всего́</b>? &nbsp;
     <b>Бо́льше ___ я люблю́ чита́ть.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>всего́</strong>. Bu yerda
    ish (<em>чита́ть</em>) boshqa ishlar bilan solishtirilyapti,
    odamlar bilan emas. Odamlar boʻlsa — <em>лу́чше
    всех</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Xatoni toping. &nbsp; <b>Я купи́л бо́лее дешёвее биле́т.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я купи́л бо́лее дешёвый
    биле́т.</strong> <em>Бо́лее</em> dan keyin <b>toʻliq
    sifat</b> keladi, qiyosiy shakl emas. Ikki marta daraja
    qoʻyilmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Akam mendan uch yosh katta.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Брат на три го́да ста́рше
    меня́.</strong> Odam haqida — <em>ста́рше</em>. Farq
    <b>на</b> + Вини́тельный bilan beriladi, «mendan» esa
    Роди́тельный — <em>меня́</em>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>лу́чше</b><span>yaxshiroq</span></li>
  <li><b>ху́же</b><span>yomonroq</span></li>
  <li><b>бо́льше / ме́ньше</b><span>kattaroq / kichikroq</span></li>
  <li><b>ста́рше / моло́же</b><span>kattaroq / yoshroq (yoshda)</span></li>
  <li><b>доро́же / деше́вле</b><span>qimmatroq / arzonroq</span></li>
  <li><b>чем</b><span>…ga qaraganda</span></li>
  <li><b>са́мый</b><span>eng</span></li>
  <li><b>гора́здо / намно́го</b><span>ancha</span></li>
  <li><b>чуть</b><span>biroz</span></li>
  <li><b>наибо́лее</b><span>eng (rasmiy)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Qiyosiy: <b>-ее</b> (<em>интере́снее</em>) yoki undosh
        almashib <b>-е</b> (<em>доро́же</em>).</li>
    <li>Yodlang: <b>лу́чше, ху́же, бо́льше, ме́ньше, ста́рше</b>.</li>
    <li>Ikki yoʻl: <b>чем + И.п.</b> (vergul bilan) yoki
        <b>Роди́тельный</b> — bu oʻzbekcha <b>-dan</b> ning oʻzi.</li>
    <li>Farq — <b>на</b> + В.п.: <em>на два го́да ста́рше</em>.</li>
    <li>Otdan oldin oddiy qiyosiy shakl turolmaydi — <b>бо́лее</b> +
        toʻliq sifat.</li>
    <li>Orttirma: <b>са́мый</b> (= oʻzbekcha «eng») va u
        <b>turlanadi</b>.</li>
    <li><b>Всех</b> — odamlardan, <b>всего́</b> — hamma narsadan.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-75: Свой — «oʻz» olmoshi va u nega shunchalik muhim",
        "category": "russian",
        "order": 75,
        "summary": (
            "Oʻzbekchada «oʻz» bor — shuning uchun bu dars siz uchun ingliz "
            "tilida oʻqiyotganlarga qaraganda ancha oson. «Свой» = «oʻz»."
        ),
        "stories": ["Свой дом"],
        "content": """
<h2>PR-75: Свой — «oʻz» olmoshi va u nega shunchalik muhim</h2>

<p>Ikki gapga qarang: <em>«Он взял <b>его́</b> кни́гу»</em> va
<em>«Он взял <b>свою́</b> кни́гу»</em>. Birinchisida u
<b>boshqa odamning</b> kitobini oldi. Ikkinchisida — <b>oʻzining</b>.
Ingliz tilida bu ikki gap bir xil aytiladi va farqni faqat kontekstdan
topish kerak. Oʻzbekchada esa farq bor — <b>«oʻz»</b>. Rus tilida ham
bor, va uning nomi <b>свой</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Свой</b> ni oʻzbekcha <b>«oʻz»</b> ga bogʻlaysiz</li>
    <li>Uni <b>мой</b> kabi turlaysiz</li>
    <li>3-shaxsda nega u <b>majburiy</b> ekanini koʻrasiz</li>
    <li>Bitta qatʼiy cheklovni oʻrganasiz: <b>свой ega boʻlolmaydi</b></li>
    <li><b>У меня́ своя́ ко́мната</b> — «oʻzimniki» maʼnosini olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--s">egasi = gapning egasi</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">свой</span>
</div>

<h3>1. Chiziq: свой ↔ его́</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">СВОЙ — oʻzining</p>
    <p><em>Дми́трий взял <b>свою́</b> кни́гу.</em><br>
       Dmitriy <b>oʻz</b> kitobini oldi.</p>
    <p>Kitob <b>Dmitriyniki</b>.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ЕГО́ — boshqaning</p>
    <p><em>Дми́трий взял <b>его́</b> кни́гу.</em><br>
       Dmitriy <b>uning</b> kitobini oldi.</p>
    <p>Kitob <b>boshqa odamniki</b>.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bu — kursning katta sovgʻalaridan biri</span>
Oʻzbekchada aynan shu farq bor va siz uni <b>oʻylamasdan</b>
qilasiz:<br><br>
<em>U <b>oʻz</b> kitobini oldi.</em> &nbsp;→&nbsp; <b>свою́</b><br>
<em>U <b>uning</b> kitobini oldi.</em> &nbsp;→&nbsp; <b>его́</b><br><br>
Yaʼni tarjima qilishda bitta savol yetarli: <b>oʻzbekchada bu
yerda «oʻz» turadimi?</b> Tursa — <em>свой</em>, turmasa —
<em>его́ / её / их</em>.<br><br>
Ingliz tilida bunday soʻz umuman yoʻq, shuning uchun ingliz
tilidan oʻrganayotgan odam bu darsda uzoq qiynaladi. Siz esa
tayyor kelgansiz.</div>

<h3>2. Turlanishi — мой kabi</h3>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Erkak</th><th>Ayol</th><th>Oʻrta</th><th>Koʻplik</th></tr>
  <tr><td class="pr-case__name">И.п.</td><td class="pr-res">свой</td>
      <td class="pr-res">своя́</td><td class="pr-res">своё</td><td class="pr-res">свои́</td></tr>
  <tr><td class="pr-case__name">Р.п.</td><td class="pr-uz">своего́</td>
      <td class="pr-uz">свое́й</td><td class="pr-uz">своего́</td><td class="pr-uz">свои́х</td></tr>
  <tr><td class="pr-case__name">Д.п.</td><td class="pr-uz">своему́</td>
      <td class="pr-uz">свое́й</td><td class="pr-uz">своему́</td><td class="pr-uz">свои́м</td></tr>
  <tr><td class="pr-case__name">В.п.</td><td class="pr-uz">свой / своего́</td>
      <td class="pr-uz">свою́</td><td class="pr-uz">своё</td><td class="pr-uz">свои́ / свои́х</td></tr>
  <tr><td class="pr-case__name">Т.п.</td><td class="pr-uz">свои́м</td>
      <td class="pr-uz">свое́й</td><td class="pr-uz">свои́м</td><td class="pr-uz">свои́ми</td></tr>
  <tr><td class="pr-case__name">П.п.</td><td class="pr-uz">своём</td>
      <td class="pr-uz">свое́й</td><td class="pr-uz">своём</td><td class="pr-uz">свои́х</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__t">Kelishiklarda</p>
  <p class="pe-ex__ru">Он помога́ет <b>свои́м</b> роди́телям. <span class="pr-uz">(Д.п.)</span></p>
  <p class="pe-ex__ru">Она́ говори́т о <b>свое́й</b> рабо́те. <span class="pr-uz">(П.п.)</span></p>
  <p class="pe-ex__ru">Мы горди́мся <b>свои́м</b> го́родом. <span class="pr-uz">(Т.п.)</span></p>
  <p class="pe-ex__uz">U oʻz ota-onasiga yordam beradi. · U oʻz ishi haqida
     gapiryapti. · Biz oʻz shahrimiz bilan faxrlanamiz.</p>
</div>

<h3>3. Qachon majburiy, qachon ixtiyoriy</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Holat</th><th>Misol</th></tr>
  <tr><td class="pr-stem">я / ты / мы / вы</td><td class="pr-uz">ixtiyoriy — ikkalasi toʻgʻri</td>
      <td class="pr-res">Я взял <b>свою́</b> / <b>мою́</b> кни́гу.</td></tr>
  <tr><td class="pr-stem">он / она́ / они́</td><td class="pr-uz"><b>majburiy</b></td>
      <td class="pr-res">Он взял <b>свою́</b> кни́гу. (oʻziniki)</td></tr>
  <tr><td class="pr-stem">он / она́ / они́</td><td class="pr-uz">boshqa odamniki</td>
      <td class="pr-res">Он взял <b>его́</b> кни́гу. (boshqaniki)</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Nega 3-shaxsda majburiy</span>
1- va 2-shaxsda chalkashlik boʻlishi mumkin emas:
<em>«я взял мою́ кни́гу»</em> da <em>мою́</em> baribir menikini
bildiradi.<br><br>
3-shaxsda esa <em>его́ / её / их</em> <b>boshqa odamni</b>
koʻrsatadi. Shuning uchun oʻzining narsasi haqida gapirsangiz,
<b>свой</b> dan boshqa yoʻl yoʻq.</div>

<h3>4. Bitta qatʼiy cheklov</h3>

<p><b>Свой gapning egasi boʻla olmaydi.</b> U har doim boshqa
soʻzga qarab turadi.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>Свой брат прие́хал.</s></p>
  <p class="pe-good"><b>Мой</b> брат прие́хал — ega oʻrnida <em>свой</em> turmaydi</p>
</div>

<p>Sabab oddiy: <em>свой</em> «gapning egasiga tegishli» degani.
Agar uning oʻzi ega boʻlsa, kimga tegishli ekani nomaʼlum boʻlib
qoladi.</p>

<h3>5. «Oʻzimniki» maʼnosi</h3>

<p><em>Свой</em> ning ikkinchi ishi — <b>ijaraga olingan emas,
begona emas</b> degan maʼno. Bu juda koʻp ishlatiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Oʻziniki</p>
  <p class="pe-ex__ru">У них тепе́рь <b>свой</b> дом.</p>
  <p class="pe-ex__uz">Endi ularning oʻz uyi bor. — ijara emas.</p>
  <p class="pe-ex__ru">У меня́ <b>своя́</b> ко́мната.</p>
  <p class="pe-ex__uz">Menda oʻz xonam bor.</p>
  <p class="pe-ex__ru">Он откры́л <b>своё</b> де́ло.</p>
  <p class="pe-ex__uz">U oʻz ishini ochdi.</p>
  <p class="pe-ex__why">Bu gaplarda <em>свой</em> ni <em>мой</em> ga
     almashtirsa boʻladi, lekin «oʻziniki» degan taʼkid
     yoʻqoladi.</p>
</div>

<h3>6. Tayyor iboralar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">в своё вре́мя</td><td class="pr-uz">oʻz vaqtida; bir paytlar</td>
      <td class="pr-res">В своё вре́мя он мно́го чита́л.</td></tr>
  <tr><td class="pr-stem">по-сво́ему</td><td class="pr-uz">oʻzicha</td>
      <td class="pr-res">Он всё де́лает по-сво́ему.</td></tr>
  <tr><td class="pr-stem">свой челове́к</td><td class="pr-uz">oʻz odami</td>
      <td class="pr-res">Здесь он свой челове́к.</td></tr>
  <tr><td class="pr-stem">ка́ждому своё</td><td class="pr-uz">har kimga oʻziniki</td>
      <td class="pr-res">Ка́ждому своё.</td></tr>
  <tr><td class="pr-stem">своё де́ло</td><td class="pr-uz">oʻz biznesi</td>
      <td class="pr-res">Она́ откры́ла своё де́ло.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Iboralar ham bir-bir tushadi</span>
Bu jadvaldagi deyarli hamma narsa oʻzbekchaga <b>soʻzma-soʻz</b>
oʻgiriladi:<br><br>
<em>oʻz vaqtida</em> → <b>в своё вре́мя</b><br>
<em>oʻzicha</em> → <b>по-сво́ему</b><br>
<em>oʻz odami</em> → <b>свой челове́к</b><br>
<em>oʻz ishini ochdi</em> → <b>откры́л своё де́ло</b><br><br>
Bu tasodif emas: ikkala tilda ham «oʻz» tushunchasi bir xil
ishlaydi. Shuning uchun bu iboralarni alohida yodlash ham shart
emas — oʻzbekchadan chiqarib olsangiz kifoya.</div>

<h3>7. Bitta nozik holat: egasi yoʻq gaplar</h3>

<p><em>Свой</em> gapning <b>egasiga</b> qarab turadi. Demak gapda ega
boʻlmasa, u ishlamaydi. Bu ikki qurilishni yonma-yon eslab
qoʻying:</p>

<div class="pe-ex">
  <p class="pe-ex__t">Ishlaydi ↔ ishlamaydi</p>
  <p class="pe-ex__ru">У меня́ <b>своя́</b> ко́мната. ✓</p>
  <p class="pe-ex__uz">Menda oʻz xonam bor. — <em>у меня́</em> qurilishida <em>свой</em> odatiy holat.</p>
  <p class="pe-ex__ru">Мне нра́вится <b>моя́</b> рабо́та. ✓</p>
  <p class="pe-ex__uz">Menga oʻz ishim yoqadi. — bu yerda <s>своя́ рабо́та</s> deyilmaydi.</p>
  <p class="pe-ex__why">Sabab: <em>нра́виться</em> li gapda ega —
     <em>рабо́та</em> ning oʻzi, odam esa Да́тельный da turibdi.
     <em>Свой</em> esa egaga qarashi kerak edi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bu yerda oʻzbekcha adashtiradi</span>
Mana shu bitta joyda oʻzbekcha <b>xato</b> qildiradi. Oʻzbekchada
ikkala gapda ham «oʻz» bemalol turadi:<br><br>
<em>Menda <b>oʻz</b> xonam bor.</em> → У меня́ <b>своя́</b>
ко́мната ✓<br>
<em>Menga <b>oʻz</b> ishim yoqadi.</em> → Мне нра́вится
<b>моя́</b> рабо́та ✓ (<s>своя́</s> emas!)<br><br>
Qoidani shunday tekshiring: gapda <b>Имени́тельный dagi ega</b>
bormi va u narsaning egasimi? Bor boʻlsa — <em>свой</em>.
Odam <em>мне, ему́, ей</em> shaklida tursa — <b>мой, его́,
её</b> qoʻying.<br><br>
Yaxshi xabar: <em>у меня́ / у него́</em> qurilishi bundan
mustasno, u yerda <em>свой</em> tabiiy eshitiladi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Она́ забы́ла её су́мку.</s> <em>(oʻzinikini)</em></p>
  <p class="pe-good">Она́ забы́ла <b>свою́</b> су́мку — oʻzbekcha «oʻz sumkasini»</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он помога́ет свои́ роди́телям.</s></p>
  <p class="pe-good">…<b>свои́м</b> роди́телям — <em>свой</em> ham turlanadi (Д.п.)</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Свои́ друзья́ пришли́ ко мне.</s></p>
  <p class="pe-good"><b>Мои́</b> друзья́ пришли́ ко мне — <em>свой</em> ega boʻlolmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он рассказа́л о его́ рабо́те.</s> <em>(oʻzining ishi haqida)</em></p>
  <p class="pe-good">Он рассказа́л о <b>свое́й</b> рабо́те — aks holda boshqaning ishi chiqadi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>Свой</b> yoki <b>его́</b>? &nbsp; <b>Бекзо́д потеря́л ___
     ключи́.</b> (oʻzinikini)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>свои́</strong>. Kalitlar
    Bekzodniki, u esa gapning egasi. <em>Его́ ключи́</em> deyilsa,
    boshqa odamning kalitlari chiqadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Она́ горди́тся ___
     дочерью.</b> (свой)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>свое́й</strong> —
    Твори́тельный, ayol jinsi. <em>Горди́ться</em> Т.п. talab
    qiladi (PR-40).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu gapda nima notoʻgʻri? &nbsp; <b>Свой сын позвони́л мне
     вчера́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Мой сын позвони́л мне
    вчера́.</strong> <em>Свой</em> gapning egasi boʻla olmaydi —
    u har doim egaga qarab turadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu ikki gapning farqi nima?<br>
     <b>Оле́г взял свою́ маши́ну. · Оле́г взял его́ маши́ну.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisida mashina —
    <b>Olegniki</b>. Ikkinchisida — <b>boshqa odamniki</b>. Bitta
    soʻz butun voqeani oʻzgartiradi: ikkinchi gapda Oleg begona
    mashinani olib ketgan.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Nihoyat ularning oʻz uyi boʻldi.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Наконе́ц у них появи́лся
    свой дом.</strong> Yoki <em>…тепе́рь у них свой дом</em>.
    Bu yerda <em>свой</em> «ijara emas, oʻziniki» degan
    maʼnoni beradi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>свой</b><span>oʻz</span></li>
  <li><b>в своё вре́мя</b><span>oʻz vaqtida; bir paytlar</span></li>
  <li><b>по-сво́ему</b><span>oʻzicha</span></li>
  <li><b>своё де́ло</b><span>oʻz ishi, biznes</span></li>
  <li><b>горди́ться</b> + Т.п.<span>faxrlanmoq</span></li>
  <li><b>потеря́ть</b><span>yoʻqotmoq</span></li>
  <li><b>появи́ться</b><span>paydo boʻlmoq</span></li>
  <li><b>наконе́ц</b><span>nihoyat</span></li>
  <li><b>ключи́</b><span>kalitlar</span></li>
  <li><b>дочь</b><span>qiz (farzand)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Свой = oʻz.</b> Oʻzbekchada «oʻz» tursa — ruschada
        <em>свой</em>.</li>
    <li>U <b>gapning egasiga</b> tegishli narsani bildiradi.</li>
    <li>3-shaxsda <b>majburiy</b>: <em>его́ кни́гу</em> boshqa
        odamning kitobi degani.</li>
    <li><b>Свой ega boʻla olmaydi</b>: <s>свой брат прие́хал</s>.</li>
    <li>U <b>мой</b> kabi turlanadi: <em>свои́м, свое́й,
        своего́</em>.</li>
    <li>Ikkinchi maʼnosi — «<b>oʻziniki</b>, ijara emas»:
        <em>у них свой дом</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-76: Себя va сам — oʻziga qaytish va taʼkid",
        "category": "russian",
        "order": 76,
        "summary": (
            "Oʻzbekcha «oʻzim» ikki ish qiladi — ruschada esa ular ikki soʻzga "
            "boʻlingan: себя́ (toʻldiruvchi) va сам (taʼkid)."
        ),
        "stories": ["Сде́лай сам"],
        "content": """
<h2>PR-76: Себя va сам — oʻziga qaytish va taʼkid</h2>

<p>Oʻzbekchada bitta soʻz ikki ish qiladi: <em>«<b>oʻzimga</b> oldim»</em>
va <em>«<b>oʻzim</b> qildim»</em>. Birinchisida «oʻzim» —
<b>toʻldiruvchi</b>, ikkinchisida — <b>taʼkid</b>. Rus tilida bular
ikki alohida soʻz: <b>себя́</b> va <b>сам</b>. Butun dars mana shu
chiziqni chizishga qaratilgan.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Себя́</b> ni turlaysiz — va uning <b>Имени́тельный</b>i yoʻqligini bilasiz</li>
    <li>Bitta soʻz hamma shaxs uchun ishlashini koʻrasiz — bu <b>osonlik</b></li>
    <li><b>Сам</b> ni shaxsga moslashtirasiz: <b>сам, сама́, са́ми</b></li>
    <li><b>Сам</b> bilan <b>са́мый</b> ni adashtirmaysiz</li>
    <li>Kundalik iboralarni olasiz: <b>чу́вствовать себя́, у себя́, на себя́</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻldiruvchi</span>
  <span class="pe-chip pe-chip--o">себя́ / себе́ / собо́й</span>
  <span class="pe-op">·</span>
  <span class="pe-formula__label">Taʼkid</span>
  <span class="pe-chip pe-chip--s">сам / сама́ / са́ми</span>
</div>

<h3>1. Себя́ — turlanishi</h3>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Shakl</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-res">—</td>
      <td class="pr-uz">yoʻq!</td><td class="pr-case__uz">—</td></tr>
  <tr><td class="pr-case__name">Роди́тельный</td><td class="pr-res">себя́</td>
      <td class="pr-uz">Он не ждал э́того от себя́.</td>
      <td class="pr-case__uz">oʻzidan</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Да́тельный</td><td class="pr-res">себе́</td>
      <td class="pr-uz">Я купи́л себе́ кни́гу.</td>
      <td class="pr-case__uz">oʻzimga</td></tr>
  <tr><td class="pr-case__name">Вини́тельный</td><td class="pr-res">себя́</td>
      <td class="pr-uz">Он уви́дел себя́ в зе́ркале.</td>
      <td class="pr-case__uz">oʻzini</td></tr>
  <tr><td class="pr-case__name">Твори́тельный</td><td class="pr-res">собо́й</td>
      <td class="pr-uz">Он недово́лен собо́й.</td>
      <td class="pr-case__uz">oʻzidan</td></tr>
  <tr><td class="pr-case__name">Предло́жный</td><td class="pr-res">(о) себе́</td>
      <td class="pr-uz">Расскажи́ о себе́.</td>
      <td class="pr-case__uz">oʻzing haqingda</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Имени́тельный shakli yoʻq</span>
<b>Себя́</b> hech qachon gapning egasi boʻlmaydi — chunki u har
doim <b>egaga qaytadi</b>. Ega boʻlsa, kimga qaytishi
qolmaydi.<br><br>
<s>Себя пришёл.</s> &nbsp;→&nbsp; <b>Он сам пришёл.</b><br><br>
Taʼkid kerak boʻlsa — <em>сам</em>, <em>себя́</em> emas.</div>

<h3>2. Bitta soʻz — hamma shaxs uchun</h3>

<p>Mana bu yerda rus tili oʻzbekchadan <b>osonroq</b>.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Oʻzbekcha</th><th>Ruscha</th></tr>
  <tr><td class="pr-uz">Men <b>oʻzimga</b> kitob oldim.</td>
      <td class="pr-res">Я купи́л <b>себе́</b> кни́гу.</td></tr>
  <tr><td class="pr-uz">Sen <b>oʻzingga</b> kitob olding.</td>
      <td class="pr-res">Ты купи́л <b>себе́</b> кни́гу.</td></tr>
  <tr><td class="pr-uz">U <b>oʻziga</b> kitob oldi.</td>
      <td class="pr-res">Он купи́л <b>себе́</b> кни́гу.</td></tr>
  <tr><td class="pr-uz">Biz <b>oʻzimizga</b> kitob oldik.</td>
      <td class="pr-res">Мы купи́ли <b>себе́</b> кни́гу.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bu safar biz qiyinroq</span>
Oʻzbekchada «oʻz» soʻziga <b>shaxs qoʻshimchasi</b> qoʻshiladi:
<em>oʻz<b>im</b>ga, oʻz<b>ing</b>ga, oʻz<b>i</b>ga,
oʻz<b>imiz</b>ga</em> — toʻrt xil shakl.<br><br>
Ruschada esa <b>bitta soʻz</b> hamma shaxsga xizmat qiladi:
<em>себе́</em>. Kim haqida gapirilayotgani gapning <b>egasidan</b>
maʼlum boʻladi.<br><br>
Yaʼni bu darsda yodlash kerak boʻlgani — atigi <b>beshta shakl</b>:
себя́, себе́, себя́, собо́й, о себе́. Va ular hech qachon
oʻzgarmaydi.</div>

<h3>3. Себя́ va -ся</h3>

<p>PR-62 da <b>-ся</b> ni oʻrgangansiz. Ular yaqin qarindosh, lekin
bir xil emas.</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">-СЯ — odatiy ish</p>
    <p><em>Он <b>мо́ется</b>.</em><br>U yuvinyapti.</p>
    <p>Har kuni boʻladigan oddiy ish. Qoʻshimcha feʼlga
       yopishgan.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">СЕБЯ́ — taʼkid</p>
    <p><em>Он уви́дел <b>себя́</b> в зе́ркале.</em><br>U oynada oʻzini koʻrdi.</p>
    <p>Alohida soʻz, alohida obyekt. Aynan <b>oʻzini</b>.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">-ся ↔ себя́</p>
  <p class="pe-ex__ru">Ка́ждое у́тро он <b>мо́ется</b> и <b>бре́ется</b>.</p>
  <p class="pe-ex__uz">Har kuni ertalab yuvinadi va soqol oladi. — odatiy ish, -ся yetarli.</p>
  <p class="pe-ex__ru">По́сле стрижки он до́лго рассма́тривал <b>себя́</b> в зе́ркале.</p>
  <p class="pe-ex__uz">Sochini oldirgach, oynada oʻzini uzoq koʻzdan kechirdi.</p>
  <p class="pe-ex__why">Ikkinchi gapda «oʻzini» — <b>alohida obyekt</b>,
     shuning uchun alohida soʻz kerak.</p>
</div>

<h3>4. Kundalik iboralar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">чу́вствовать себя́</td><td class="pr-uz">oʻzini his qilmoq</td>
      <td class="pr-res">Как ты себя́ чу́вствуешь?</td></tr>
  <tr><td class="pr-stem">у себя́</td><td class="pr-uz">oʻz xonasida, oʻzida</td>
      <td class="pr-res">Дире́ктор у себя́.</td></tr>
  <tr><td class="pr-stem">про себя́</td><td class="pr-uz">ichida, ovoz chiqarmay</td>
      <td class="pr-res">Чита́й про себя́.</td></tr>
  <tr><td class="pr-stem">к себе́ / от себя́</td><td class="pr-uz">oʻziga tomon / oʻzidan</td>
      <td class="pr-res">На двери́: «К себе́».</td></tr>
  <tr><td class="pr-stem">взять себя́ в ру́ки</td><td class="pr-uz">oʻzini qoʻlga olmoq</td>
      <td class="pr-res">Возьми́ себя́ в ру́ки.</td></tr>
  <tr><td class="pr-stem">вы́йти из себя́</td><td class="pr-uz">jahli chiqmoq</td>
      <td class="pr-res">Он вы́шел из себя́.</td></tr>
  <tr><td class="pr-stem">не по себе́</td><td class="pr-uz">koʻngli gʻash</td>
      <td class="pr-res">Мне ста́ло не по себе́.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Eshikdagi soʻz</span>
Rossiyada har qanday eshikda <b>«К себе́»</b> (oʻzingizga tortib
oching) yoki <b>«От себя́»</b> (itaring) deb yozilgan boʻladi.
Shu ikki soʻzni bilsangiz, hech qachon eshik oldida
qiynalmaysiz.</div>

<div class="pe-ex">
  <p class="pe-ex__t">Iboralar jonli nutqda</p>
  <p class="pe-ex__ru">— Как ты <b>себя́</b> чу́вствуешь? — Уже́ лу́чше, спаси́бо.</p>
  <p class="pe-ex__uz">— Oʻzingni qanday his qilyapsan? — Yaxshiroq, rahmat.</p>
  <p class="pe-ex__ru">— Марина Петро́вна у <b>себя́</b>? — Да, но она́ за́нята.</p>
  <p class="pe-ex__uz">— Marina Petrovna oʻz xonasidami? — Ha, lekin u band.</p>
  <p class="pe-ex__ru">Не кричи́, возьми́ <b>себя́</b> в ру́ки.</p>
  <p class="pe-ex__uz">Baqirma, oʻzingni qoʻlga ol.</p>
</div>

<h3>5. Сам — taʼkid</h3>

<p><b>Сам</b> «boshqa hech kim emas, aynan oʻzi» degani. U
sifat kabi moslashadi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kim</th><th>Shakl</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-uz">erkak</td><td class="pr-end">сам</td>
      <td class="pr-res">Я сам э́то сде́лал.</td><td class="pr-stem">Buni oʻzim qildim.</td></tr>
  <tr><td class="pr-uz">ayol</td><td class="pr-end">сама́</td>
      <td class="pr-res">Она́ сама́ пришла́.</td><td class="pr-stem">U oʻzi keldi.</td></tr>
  <tr><td class="pr-uz">oʻrta</td><td class="pr-end">само́</td>
      <td class="pr-res">Окно́ откры́лось само́.</td><td class="pr-stem">Deraza oʻzi ochildi.</td></tr>
  <tr><td class="pr-uz">koʻplik</td><td class="pr-end">са́ми</td>
      <td class="pr-res">Мы са́ми всё сде́лаем.</td><td class="pr-stem">Hammasini oʻzimiz qilamiz.</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__t">Chiziq aniq koʻrinadi</p>
  <p class="pe-ex__ru">Он купи́л <b>себе́</b> телефо́н.</p>
  <p class="pe-ex__uz">U oʻziga telefon oldi. — <b>kimga?</b> Toʻldiruvchi.</p>
  <p class="pe-ex__ru">Он <b>сам</b> купи́л телефо́н.</p>
  <p class="pe-ex__uz">Telefonni oʻzi oldi. — <b>kim?</b> Taʼkid, hech kim yordam bermadi.</p>
  <p class="pe-ex__ru">Он <b>сам</b> купи́л <b>себе́</b> телефо́н.</p>
  <p class="pe-ex__uz">Oʻziga telefonni oʻzi oldi. — ikkalasi bir gapda.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Sinov savoli</span>
Oʻzbekcha «oʻzim» ni koʻrsangiz, bitta savol bering:<br><br>
<b>«Kimga? Kimni?»</b> degan savolga javob berayaptimi →
<b>себя́ / себе́</b><br>
<b>«Kim? Boshqa emas, aynan kim?»</b> degan taʼkidmi →
<b>сам</b><br><br>
<em>Oʻzimga oldim</em> — kimga? → <b>купи́л себе́</b><br>
<em>Oʻzim oldim</em> — kim? → <b>сам купи́л</b></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Nega bu ikkisi bizda bitta</span>
Oʻzbekcha <em>«oʻzim»</em> gapda qayerda turishiga qarab maʼnosini
oʻzgartiradi, soʻzning shakli esa bir xil qolaveradi:<br><br>
<em><b>Oʻzim</b> qildim.</em> — taʼkid → <b>сам</b><br>
<em><b>Oʻzimga</b> oldim.</em> — toʻldiruvchi → <b>себе́</b><br><br>
Yaʼni bizda ishni <b>kelishik qoʻshimchasi</b> bajaradi
(<em>-ga, -ni</em>), ruschada esa <b>ikki boshqa soʻz</b>.<br><br>
Shuning uchun tarjima qilayotganda oʻzbekcha soʻzning
<b>oxiriga</b> qarang: qoʻshimcha bor boʻlsa (<em>oʻzim<b>ga</b>,
oʻzim<b>ni</b>, oʻzim <b>haqimda</b></em>) — <em>себя́</em>
oilasi. Qoʻshimchasiz yalangʻoch <em>«oʻzim»</em> boʻlsa —
<em>сам</em>.</div>

<h3>6. Сам va са́мый — adashtirmang</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">САМ — oʻzi</p>
    <p><em>Дире́ктор <b>сам</b> пришёл.</em><br>Direktorning oʻzi keldi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">СА́МЫЙ — eng (PR-74)</p>
    <p><em>Э́то <b>са́мый</b> большо́й дом.</em><br>Bu eng katta uy.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Сам собо́й</span>
<b>Сам собо́й / само́ собо́й</b> — «oʻz-oʻzidan»:<br><br>
<em>Дверь откры́лась <b>сама́ собо́й</b>.</em> — Eshik oʻz-oʻzidan
ochildi.<br>
<em><b>Само́ собо́й</b> разуме́ется.</em> — Oʻz-oʻzidan
maʼlum.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я купи́л мне кни́гу.</s></p>
  <p class="pe-good">Я купи́л <b>себе́</b> кни́гу — ega bilan bir odam boʻlsa, <em>себе́</em></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Как ты себе́ чу́вствуешь?</s></p>
  <p class="pe-good">Как ты <b>себя́</b> чу́вствуешь? — bu ibora Вини́тельный oladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Она́ сам пришла́.</s></p>
  <p class="pe-good">Она́ <b>сама́</b> пришла́ — <em>сам</em> jinsga moslashadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Себя сде́лал э́то.</s></p>
  <p class="pe-good">Он <b>сам</b> сде́лал э́то — <em>себя́</em> ega boʻlolmaydi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>Себя́</b> yoki <b>сам</b>? &nbsp; <b>Он ___ почини́л
     велосипе́д.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>сам</strong>. «Velosipedni
    oʻzi tuzatdi» — bu <b>taʼkid</b>, hech kim yordam
    bermagan. <em>Себя́</em> «kimni?» savoliga javob
    berardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Расскажи́ немно́го о
     ___.</b> (себя́)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>себе́</strong> —
    Предло́жный. <em>О себе́</em> = «oʻzing haqingda». Bu
    suhbatning eng koʻp uchraydigan iborasi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Eshikda «<b>От себя́</b>» yozilgan. Nima qilasiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Eshikni itarasiz.</strong>
    <em>От себя́</em> — «oʻzingizdan nariga». <em>К себе́</em>
    esa «oʻzingizga tomon», yaʼni tortasiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapda nechta xato bor? &nbsp; <b>Дилно́за сам купи́ла мне
     пода́рок себе́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Ikkita. Toʻgʻrisi: <strong>Дилно́за
    сама́ купи́ла себе́ пода́рок.</strong> Birinchidan,
    <em>сам</em> ayol jinsiga moslashishi kerak —
    <em>сама́</em>. Ikkinchidan, <em>мне</em> va <em>себе́</em>
    bir gapda ziddiyat hosil qilgan: agar sovgʻa oʻziga
    boʻlsa, faqat <em>себе́</em> qoladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Oʻzingizni qoʻlga oling va oʻzingiz hal qiling.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Возьми́те себя́ в ру́ки и
    реши́те са́ми.</strong> Birinchi qismda <em>себя́</em> —
    toʻldiruvchi (kimni?), ikkinchisida <em>са́ми</em> — taʼkid
    (kim?). Bitta gapda ikkala soʻz ham oʻz oʻrnida
    turibdi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>себя́ / себе́ / собо́й</b><span>oʻzini / oʻziga / oʻzi bilan</span></li>
  <li><b>сам / сама́ / са́ми</b><span>oʻzi (taʼkid)</span></li>
  <li><b>чу́вствовать себя́</b><span>oʻzini his qilmoq</span></li>
  <li><b>у себя́</b><span>oʻz xonasida</span></li>
  <li><b>про себя́</b><span>ichida, ovozsiz</span></li>
  <li><b>к себе́ / от себя́</b><span>torting / itaring</span></li>
  <li><b>взять себя́ в ру́ки</b><span>oʻzini qoʻlga olmoq</span></li>
  <li><b>вы́йти из себя́</b><span>jahli chiqmoq</span></li>
  <li><b>сам собо́й</b><span>oʻz-oʻzidan</span></li>
  <li><b>зе́ркало</b><span>oyna</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Себя́</b> — toʻldiruvchi («kimni? kimga?»).
        <b>Сам</b> — taʼkid («kim? oʻzimi?»).</li>
    <li><b>Себя́ ning Имени́тельный shakli yoʻq</b> — u ega boʻla
        olmaydi.</li>
    <li>Bitta shakl <b>hamma shaxs uchun</b>: <em>я / ты / он
        купи́л себе́</em>. Oʻzbekchadan osonroq.</li>
    <li><b>Сам</b> esa moslashadi: <em>сам, сама́, само́,
        са́ми</em>.</li>
    <li><b>Сам ≠ са́мый.</b> <em>Сам дире́ктор</em> — direktorning
        oʻzi. <em>Са́мый большо́й</em> — eng katta.</li>
    <li>Yodlang: <b>чу́вствовать себя́</b>, <b>у себя́</b>,
        <b>про себя́</b>, <b>к себе́ / от себя́</b>.</li>
  </ul>
</div>
""",
    },
]
