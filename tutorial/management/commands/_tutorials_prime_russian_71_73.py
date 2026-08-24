# -*- coding: utf-8 -*-
"""Prime Russian — Block F yakuni (71–73).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Uchala dars bir zanjir: PR-71 qisqa shaklni (постро́ен) olib keladi,
PR-73 esa oʻsha qisqa shaklni sifatlarga yoyadi (прав, до́лжен, ну́жен).
PR-72 oʻrtada turadi va PR-70/71 bilan qarama-qarshi qoʻyiladi:
причастие — sifat, деепричастие — ravish.

PR-71 — страдательные причастия. Oʻzbekcha tayanch kuchli: bizda ham
majhul qoʻshimcha bor (-il-, -in-), va PR-62 dagi -ся bilan bir oila.
Ustiga «Толстой TOMONIDAN yozilgan» ↔ «напи́санная Толсты́м».
PR-72 — деепричастие. Oʻzbekcha -ib va -gach ning aynan oʻzi. Darsning
yuragi — EGA BIRXILLIGI qoidasi, va u oʻzbekchada ham bor: oʻquvchining
quloqi allaqachon toʻgʻri eshitadi, faqat unga ishonish kerak.
PR-73 — qisqa sifat. Bu yerda oʻzbek tili yordam bermaydi (bizda bitta
shakl bor), lekin рад / до́лжен / ну́жен / гото́в / прав toʻplami
oʻzbekcha xursand / kerak / rozi / haq ga bir-bir tushadi.

Mashqlar:        practice/management/commands/_practice_pr_71_73.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_71_73.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_71_73.py --author=prime
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
        "title": "PR-71: Причастие 2: страдательные — прочитанный, написан, сделан",
        "category": "russian",
        "order": 71,
        "summary": (
            "Ot ishni oʻzi qilmaydi — ish uning ustida qilinadi. Oʻzbekcha -il-/-in- "
            "majhul qoʻshimchasi kabi. Toʻliq shaklda -нн-, qisqasida -н-."
        ),
        "stories": ["Кни́га, напи́санная в тюрьме́"],
        "content": """
<h2>PR-71: Причастие 2: страдательные — прочитанный, написан, сделан</h2>

<p>Oʻtgan darsda <em>студе́нт, <b>прочита́вший</b> кни́гу</em> — talaba
oʻqidi. Endi teskarisiga oʻgiramiz: <em>кни́га, <b>прочи́танная</b>
студе́нтом</em> — kitob oʻqildi. Ish bir xil, lekin gapning markazida
endi <b>ishni qilgan</b> emas, <b>ish qilingan</b> narsa turibdi.
Oʻzbekchada buni <b>-il-</b> qoʻshimchasi qiladi: <em>oʻqi<b>l</b>gan
kitob</em>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Действительное</b> bilan <b>страдательное</b> ni ajratasiz</li>
    <li>Toʻliq shaklni yasaysiz: <b>-нн- / -енн- / -т-</b></li>
    <li>Qisqa shaklni yasaysiz va <b>bitta Н</b> qoidasini eslab qolasiz</li>
    <li>Ishni kim qilganini <b>Твори́тельный</b> bilan aytasiz</li>
    <li>PR-61 dagi <em>дом постро́ен</em> qayerdan kelganini nihoyat koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻliq</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">нн / енн / т</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">ый / ая / ое / ые</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qisqa</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--neg">н / ен / т</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">— / а / о / ы</span>
</div>

<h3>1. Kim qiladi, kimga qilinadi</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">ДЕЙСТВИ́ТЕЛЬНОЕ (PR-70)</p>
    <p><em>студе́нт, <b>прочита́вший</b> кни́гу</em><br>
       kitobni oʻqi<b>gan</b> talaba</p>
    <p>Ot <b>oʻzi</b> ish qiladi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">СТРАДА́ТЕЛЬНОЕ (bu dars)</p>
    <p><em>кни́га, <b>прочи́танная</b> студе́нтом</em><br>
       talaba tomonidan oʻqi<b>l</b>gan kitob</p>
    <p>Ish ot <b>ustida</b> bajariladi.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha — bu sizda bor</span>
Oʻzbekchada majhul nisbat <b>-il- / -in-</b> qoʻshimchasi bilan
yasaladi, va u sifatdoshga ham qoʻshiladi:<br><br>
<em>yoz<b>gan</b> odam</em> &nbsp;→&nbsp; <b>написа́вший</b> челове́к<br>
<em>yoz<b>il</b>gan xat</em> &nbsp;→&nbsp; <b>напи́санное</b> письмо́<br>
<em>qur<b>il</b>gan uy</em> &nbsp;→&nbsp; <b>постро́енный</b> дом<br><br>
Bu PR-62 dagi <b>-ся</b> bilan bir oila: <em>дом стро́ится</em> —
jarayon, <em>дом постро́ен</em> — natija. Ikkalasi ham oʻzbekcha
<em>-il-</em> ga tushadi.</div>

<h3>2. Toʻliq shakl: -нн- / -енн- / -т-</h3>

<p>Qaysi qoʻshimcha kelishi feʼlning tugashiga bogʻliq:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Feʼl tugashi</th><th>Qoʻshimcha</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-uz">-ать / -ять</td><td class="pr-end">-анн- / -янн-</td>
      <td class="pr-res">прочита́ть → прочи́танный</td><td class="pr-stem">oʻqilgan</td></tr>
  <tr><td class="pr-uz">-ать</td><td class="pr-end">-анн-</td>
      <td class="pr-res">написа́ть → напи́санный</td><td class="pr-stem">yozilgan</td></tr>
  <tr><td class="pr-uz">-ать</td><td class="pr-end">-анн-</td>
      <td class="pr-res">сде́лать → сде́ланный</td><td class="pr-stem">qilingan</td></tr>
  <tr><td class="pr-uz">-ить</td><td class="pr-end">-енн-</td>
      <td class="pr-res">постро́ить → постро́енный</td><td class="pr-stem">qurilgan</td></tr>
  <tr><td class="pr-uz">-ить (urgʻu oxirida)</td><td class="pr-end">-ённ-</td>
      <td class="pr-res">реши́ть → решённый</td><td class="pr-stem">hal qilingan</td></tr>
  <tr><td class="pr-uz">-ти</td><td class="pr-end">-ённ-</td>
      <td class="pr-res">перевести́ → переведённый</td><td class="pr-stem">tarjima qilingan</td></tr>
  <tr><td class="pr-uz">-ыть / -ять / -нуть</td><td class="pr-end">-т-</td>
      <td class="pr-res">закры́ть → закры́тый</td><td class="pr-stem">yopilgan</td></tr>
  <tr><td class="pr-uz">bir boʻgʻinli</td><td class="pr-end">-т-</td>
      <td class="pr-res">взять → взя́тый</td><td class="pr-stem">olingan</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Urgʻu orqaga siljiydi</span>
<em>-анн-</em> guruhida urgʻu koʻpincha bir boʻgʻin orqaga
qaytadi:<br><br>
прочит<b>а́</b>ть → проч<b>и́</b>танный &nbsp;·&nbsp;
напис<b>а́</b>ть → нап<b>и́</b>санный &nbsp;·&nbsp;
потер<b>я́</b>ть → пот<b>е́</b>рянный<br><br>
Bir nechta feʼlda oʻzak ham oʻzgaradi:
<em>куп<b>и́</b>ть → к<b>у́</b>пленный</em> (п → пл).</div>

<h3>3. Qisqa shakl — bitta Н</h3>

<p>Bu darsning eng amaliy qismi. Qisqa shakl <b>kesim</b> boʻlib
xizmat qiladi — yaʼni gapning oʻzagida turadi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Toʻliq (2 Н)</th><th>Erkak</th><th>Ayol</th><th>Oʻrta</th><th>Koʻplik</th></tr>
  <tr><td class="pr-stem">прочи́та<b>нн</b>ый</td><td class="pr-res">прочи́та<b>н</b></td>
      <td class="pr-res">прочи́тана</td><td class="pr-res">прочи́тано</td>
      <td class="pr-res">прочи́таны</td></tr>
  <tr><td class="pr-stem">постро́е<b>нн</b>ый</td><td class="pr-res">постро́е<b>н</b></td>
      <td class="pr-res">постро́ена</td><td class="pr-res">постро́ено</td>
      <td class="pr-res">постро́ены</td></tr>
  <tr><td class="pr-stem">напи́са<b>нн</b>ый</td><td class="pr-res">напи́са<b>н</b></td>
      <td class="pr-res">напи́сана</td><td class="pr-res">напи́сано</td>
      <td class="pr-res">напи́саны</td></tr>
  <tr><td class="pr-stem">решё<b>нн</b>ый</td><td class="pr-res">решё<b>н</b></td>
      <td class="pr-res">решена́</td><td class="pr-res">решено́</td>
      <td class="pr-res">решены́</td></tr>
  <tr><td class="pr-stem">закры́<b>т</b>ый</td><td class="pr-res">закры́<b>т</b></td>
      <td class="pr-res">закры́та</td><td class="pr-res">закры́то</td>
      <td class="pr-res">закры́ты</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Yodlab oling</span>
<b>Toʻliq shaklda — ikkita Н. Qisqa shaklda — bitta Н.</b><br><br>
<em>прочи́та<b>нн</b>ая кни́га</em> &nbsp;→&nbsp;
<em>кни́га прочи́та<b>н</b>а</em><br>
<em>напи́са<b>нн</b>ые пи́сьма</em> &nbsp;→&nbsp;
<em>пи́сьма напи́са<b>н</b>ы</em><br><br>
Bu rus imlosidagi eng koʻp tekshiriladigan qoidalardan biri.</div>

<h3>4. Toʻliq yoki qisqa?</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">TOʻLIQ — aniqlovchi</p>
    <p><em><b>Закры́тая</b> дверь.</em><br>Yopiq eshik.</p>
    <p>Otni aniqlaydi. Savol: <b>qanday?</b></p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">QISQA — kesim</p>
    <p><em>Дверь <b>закры́та</b>.</em><br>Eshik yopilgan.</p>
    <p>Gapning kesimi. Savol: <b>nima boʻldi?</b></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">Qisqa shakl amalda</p>
  <p class="pe-ex__ru">Магази́н <b>закры́т</b> до девяти́.</p>
  <p class="pe-ex__uz">Doʻkon toqqizgacha yopiq.</p>
  <p class="pe-ex__ru">Дом <b>постро́ен</b> в 1980 году́.</p>
  <p class="pe-ex__uz">Uy 1980-yilda qurilgan.</p>
  <p class="pe-ex__ru">Все зада́чи <b>решены́</b>.</p>
  <p class="pe-ex__uz">Barcha masalalar yechilgan.</p>
  <p class="pe-ex__why">Bu — PR-61 dagi <b>majhul nisbat</b>. Endi
     bilasiz: <em>постро́ен</em> — bu qisqa sifatdosh.</p>
</div>

<h3>5. Kim qildi? — Твори́тельный</h3>

<p>Ishni kim bajarganini aytish kerak boʻlsa, u
<b>Твори́тельный</b> kelishigida turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Кем?</p>
  <p class="pe-ex__ru">Кни́га, напи́санная <b>Толсты́м</b>.</p>
  <p class="pe-ex__uz">Tolstoy tomonidan yozilgan kitob.</p>
  <p class="pe-ex__ru">Дом, постро́енный <b>де́дом</b>.</p>
  <p class="pe-ex__uz">Bobom tomonidan qurilgan uy.</p>
  <p class="pe-ex__ru">Э́та карти́на напи́сана <b>молоды́м худо́жником</b>.</p>
  <p class="pe-ex__uz">Bu surat yosh rassom tomonidan chizilgan.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha «tomonidan»</span>
Oʻzbekcha <b>«tomonidan»</b> soʻzi aynan shu vazifani bajaradi, va
mosligi juda toza:<br><br>
<em>Tolstoy <b>tomonidan</b> yozilgan</em> &nbsp;→&nbsp;
<b>напи́санный Толсты́м</b> (Т.п.)<br>
<em>bobom <b>tomonidan</b> qurilgan</em> &nbsp;→&nbsp;
<b>постро́енный де́дом</b> (Т.п.)<br><br>
Yaʼni «tomonidan» ni koʻrsangiz — <b>Твори́тельный</b> qoʻying,
predlogsiz. Rus tilida bu yerda hech qanday predlog ishlatilmaydi.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Nega bu ikki shakl bizda yoʻq</span>
Oʻzbekchada <b>bitta</b> shakl ikkala vazifani ham bajaradi:<br><br>
<em><b>yopilgan</b> eshik</em> — aniqlovchi<br>
<em>eshik <b>yopilgan</b></em> — kesim<br><br>
Soʻz oʻzgarmadi, faqat oʻrni oʻzgardi. Ruschada esa <b>soʻzning
oʻzi</b> oʻzgaradi: <em>закры́т<b>ая</b> дверь</em> ↔ <em>дверь
закры́т<b>а</b></em>.<br><br>
Shuning uchun har safar oʻzingizga bitta savol bering: <b>bu soʻz
otni aniqlayaptimi yoki gapning kesimimi?</b> Aniqlovchi boʻlsa —
toʻliq shakl. Kesim boʻlsa — qisqa shakl. Keyingi darsda (PR-73)
xuddi shu bosqichni oddiy sifatlar bilan ham takrorlaymiz.</div>

<h3>6. Vergul — PR-70 dagi qoidaning oʻzi</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Oʻrin va vergul</p>
  <p class="pe-ex__ru">Кни́га<b>,</b> напи́санная в тюрьме́<b>,</b> ста́ла знамени́той.</p>
  <p class="pe-ex__ru">Напи́санная в тюрьме́ кни́га ста́ла знамени́той.</p>
  <p class="pe-ex__uz">Qamoqda yozilgan kitob mashhur boʻlib ketdi.</p>
  <p class="pe-ex__why">Otdan <b>keyin</b> → ikki tomondan vergul.
     Otdan <b>oldin</b> (oʻzbekcha tartib) → vergulsiz.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Hamma feʼlda ham boʻlavermaydi</span>
Страдательное причастие faqat <b>obyekt oladigan</b> feʼllardan
yasaladi — yaʼni «kimni? nimani?» degan savolga javob beradiganidan.
<em>Идти́, спать, жить, сиде́ть</em> kabi feʼllarda obyekt yoʻq,
demak <s>идённый</s>, <s>спа́нный</s> degan soʻzlar ham yoʻq.<br><br>
Va koʻpincha faqat <b>СВ</b> feʼllardan:
<em>прочита́ть → прочи́танный</em>. НСВ dan koʻproq
<em>-мый</em> shakli chiqadi (<em>люби́мый</em> — sevimli), lekin
u alohida mavzu.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Дом постро́енный в 1980 году́.</s></p>
  <p class="pe-good">Дом <b>постро́ен</b> в 1980 году́ — kesim kerak, demak qisqa shakl</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Пи́сьма напи́санны.</s></p>
  <p class="pe-good">Пи́сьма <b>напи́саны</b> — qisqa shaklda har doim <b>bitta Н</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кни́га, напи́санная Толсто́го.</s></p>
  <p class="pe-good">…напи́санная <b>Толсты́м</b> — «kim tomonidan» Твори́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ви́дел дверь, закры́тый на ключ.</s></p>
  <p class="pe-good">…дверь, <b>закры́тую</b> на ключ — sifatdosh otga moslashadi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Toʻliq shaklni yasang. &nbsp; <b>постро́ить</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>постро́енный</strong>.
    <em>-ить</em> bilan tugagani uchun <b>-енн-</b> qoʻshiladi.
    Qisqa shakli — <em>постро́ен</em>, bitta Н bilan.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Qisqa shaklni qoʻying. &nbsp; <b>Все зада́чи ___.</b> (реши́ть)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>решены́</strong>.
    <em>Зада́чи</em> — koʻplik, demak <em>-ы</em>. Toʻliq shakli
    <em>решённые</em> boʻlardi, lekin bu yerda <b>kesim</b> kerak.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nechta Н? &nbsp; <b>Пи́сьма уже́ напи́са__ы.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Bitta: напи́саны.</strong>
    Bu qisqa shakl (kesim). Toʻliq shaklda esa ikkita boʻlardi:
    <em>напи́са<b>нн</b>ые пи́сьма</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Э́та пе́сня напи́сана ___.</b>
     (молодо́й компози́тор)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>молоды́м
    компози́тором</strong> — Твори́тельный. Oʻzbekcha «yosh
    bastakor <b>tomonidan</b>». Rus tilida predlog
    qoʻyilmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Qamoqda yozilgan kitob koʻp tillarga tarjima qilingan.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Кни́га, напи́санная в
    тюрьме́, переведена́ на мно́гие языки́.</strong> Birinchisi —
    toʻliq shakl (aniqlovchi, vergul bilan), ikkinchisi — qisqa
    shakl (kesim, bitta Н... aniqrogʻi <em>-на</em>).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>страда́тельное прича́стие</b><span>majhul sifatdosh</span></li>
  <li><b>прочи́танный</b><span>oʻqilgan</span></li>
  <li><b>напи́санный</b><span>yozilgan</span></li>
  <li><b>постро́енный</b><span>qurilgan</span></li>
  <li><b>переведённый</b><span>tarjima qilingan</span></li>
  <li><b>закры́тый</b><span>yopilgan, yopiq</span></li>
  <li><b>реши́ть → решён</b><span>hal qilmoq → hal qilingan</span></li>
  <li><b>тюрьма́</b><span>qamoq</span></li>
  <li><b>знамени́тый</b><span>mashhur</span></li>
  <li><b>худо́жник</b><span>rassom</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Действительное</b> — ot ish qiladi. <b>Страдательное</b> —
        ish ot ustida qilinadi (oʻzbekcha <b>-il-</b>).</li>
    <li>Toʻliq: <b>-нн- / -енн- / -т-</b>. <em>-ать</em> → -анн-,
        <em>-ить</em> → -енн-, <em>-ыть / bir boʻgʻinli</em> → -т-.</li>
    <li><b>Toʻliqda ikkita Н, qisqada bitta Н</b>:
        <em>прочи́танная → прочи́тана</em>.</li>
    <li>Toʻliq = <b>aniqlovchi</b>, qisqa = <b>kesim</b>:
        <em>закры́тая дверь</em> ↔ <em>дверь закры́та</em>.</li>
    <li>«Kim tomonidan» — <b>Твори́тельный</b>, predlogsiz:
        <em>напи́сана Толсты́м</em>.</li>
    <li>Vergul PR-70 dagidek: oborot <b>otdan keyin</b> tursa —
        ikki tomondan.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-72: Деепричастие: читая, прочитав — bir vaqtda va undan oldin",
        "category": "russian",
        "order": 72,
        "summary": (
            "Oʻzbekcha «-ib» va «-gach» ning aynan oʻzi. Bitta qoida hammasini hal "
            "qiladi: ravishdosh bilan asosiy feʼlning egasi BIR XIL boʻlishi shart."
        ),
        "stories": ["Возвраща́ясь домо́й"],
        "content": """
<h2>PR-72: Деепричастие: читая, прочитав — bir vaqtda va undan oldin</h2>

<p>Oʻzbekchada siz buni kuniga oʻn marta aytasiz: <em>«Uyga
qayt<b>ib</b>, ovqat yedim»</em>, <em>«Xatni oʻqi<b>gach</b>,
hammasini tushundim»</em>. Feʼl ikkinchi feʼlga <b>yordamchi</b>
boʻlib qoʻshiladi va qachon yoki qanday boʻlganini aytadi. Rus tilida
bu <b>деепричастие</b> — <b>ravishdosh</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Чита́я</b> (bir vaqtda) va <b>прочита́в</b> (undan oldin) ni ajratasiz</li>
    <li>Ikkala shaklni ham yasaysiz</li>
    <li>Darsning yagona qatʼiy qoidasini oʻrganasiz: <b>ega bir xil boʻlishi shart</b></li>
    <li>Vergul qoidasini olasiz — u <b>причастие</b> nikidan osonroq</li>
    <li>Ravishdoshi yoʻq feʼllarni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">НСВ — bir vaqtda</span>
  <span class="pe-chip pe-chip--s">они́ shakli</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">-я / -а</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">чита́я</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">СВ — undan oldin</span>
  <span class="pe-chip pe-chip--s">он shakli − л</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">-в / -вшись</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">прочита́в</span>
</div>

<h3>1. Причастие emas — bu boshqa narsa</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">ПРИЧА́СТИЕ — sifat</p>
    <p><em>ма́льчик, <b>чита́ющий</b> кни́гу</em></p>
    <p>Savol: <b>qanday?</b> Otni aniqlaydi va unga
       <b>moslashadi</b>: чита́ющий, чита́ющая, чита́ющего…</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ДЕЕПРИЧА́СТИЕ — ravish</p>
    <p><em><b>Чита́я</b>, он забы́л про вре́мя.</em></p>
    <p>Savol: <b>qachon? qanday qilib?</b> Feʼlni aniqlaydi va
       <b>hech qachon oʻzgarmaydi</b>.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha — deyarli bepul</span>
Ikkala shakl ham oʻzbekchada bor va ular kundalik nutqning
oʻzagida turadi:<br><br>
<em>oʻqi<b>b</b></em> (bir vaqtda) &nbsp;→&nbsp; <b>чита́я</b><br>
<em>oʻqi<b>gach</b></em>, <em>oʻqi<b>b boʻlgach</b></em> (avval)
&nbsp;→&nbsp; <b>прочита́в</b><br><br>
<em>Uyga qayt<b>ib</b>, ovqat yedim.</em> →
<b>Верну́вшись</b> домо́й, я поу́жинал.<br>
<em>Xatni oʻqi<b>gach</b>, tushundim.</em> →
<b>Прочита́в</b> письмо́, я по́нял.<br><br>
Yaʼni siz bu qurilishni allaqachon bilasiz. Yangi narsa —
shakllarning oʻzi, xolos.</div>

<h3>2. НСВ: -я / -а — bir vaqtda</h3>

<p>Yasalish yana <b>они́</b> shaklidan (PR-59, PR-70 dagi kabi):
qoʻshimcha olib tashlanadi, <b>-я</b> qoʻshiladi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>Они́</th><th>Ravishdosh</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">чита́ть</td><td class="pr-uz">чита́ют</td>
      <td class="pr-res">чита́я</td><td class="pr-end">oʻqib (oʻqiyotib)</td></tr>
  <tr><td class="pr-stem">рабо́тать</td><td class="pr-uz">рабо́тают</td>
      <td class="pr-res">рабо́тая</td><td class="pr-end">ishlab</td></tr>
  <tr><td class="pr-stem">говори́ть</td><td class="pr-uz">говоря́т</td>
      <td class="pr-res">говоря́</td><td class="pr-end">gapirib</td></tr>
  <tr><td class="pr-stem">возвраща́ться</td><td class="pr-uz">возвраща́ются</td>
      <td class="pr-res">возвраща́ясь</td><td class="pr-end">qaytayotib</td></tr>
  <tr><td class="pr-stem">улыба́ться</td><td class="pr-uz">улыба́ются</td>
      <td class="pr-res">улыба́ясь</td><td class="pr-end">jilmayib</td></tr>
  <tr><td class="pr-stem">держа́ть</td><td class="pr-uz">де́ржат</td>
      <td class="pr-res">держа́</td><td class="pr-end">ushlab</td></tr>
  <tr><td class="pr-stem">быть</td><td class="pr-uz">—</td>
      <td class="pr-res">бу́дучи</td><td class="pr-end">boʻlib (kitobiy)</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ravishdoshi yoʻq feʼllar</span>
Baʼzi keng ishlatiladigan НСВ feʼllarning <b>-я</b> shakli yoʻq —
yasab qoʻysangiz, gʻalati eshitiladi:<br><br>
<b>писа́ть, пить, бить, петь, ждать, спать, есть, бежа́ть, мочь,
хоте́ть.</b><br><br>
Ular oʻrniga oddiy gap ishlatiladi: <s>«пиша́ письмо́»</s> emas,
<b>«когда́ я писа́л письмо́»</b>.</div>

<h3>3. СВ: -в / -вшись — avval bu, keyin u</h3>

<p>Tayanch — oʻtgan zamonning <b>он</b> shakli, <b>-л</b> olib
tashlanadi va <b>-в</b> qoʻshiladi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>Он shakli</th><th>Ravishdosh</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">прочита́ть</td><td class="pr-uz">прочита́л</td>
      <td class="pr-res">прочита́в</td><td class="pr-end">oʻqib boʻlgach</td></tr>
  <tr><td class="pr-stem">уви́деть</td><td class="pr-uz">уви́дел</td>
      <td class="pr-res">уви́дев</td><td class="pr-end">koʻrgach</td></tr>
  <tr><td class="pr-stem">купи́ть</td><td class="pr-uz">купи́л</td>
      <td class="pr-res">купи́в</td><td class="pr-end">sotib olgach</td></tr>
  <tr><td class="pr-stem">верну́ться</td><td class="pr-uz">верну́лся</td>
      <td class="pr-res">верну́вшись</td><td class="pr-end">qaytgach</td></tr>
  <tr><td class="pr-stem">останови́ться</td><td class="pr-uz">останови́лся</td>
      <td class="pr-res">останови́вшись</td><td class="pr-end">toʻxtagach</td></tr>
  <tr><td class="pr-stem">вы́йти</td><td class="pr-uz">вы́шел</td>
      <td class="pr-res">вы́йдя</td><td class="pr-end">chiqqach</td></tr>
  <tr><td class="pr-stem">прийти́</td><td class="pr-uz">пришёл</td>
      <td class="pr-res">придя́</td><td class="pr-end">kelgach</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Uchta kichik qoida</span>
1. <b>-ся feʼllari → -вшись</b>: <em>верну́лся →
   верну́<b>вшись</b></em>. Bu yerda <em>-сь</em> boʻladi,
   <em>причастие</em> dagidan farqli.<br>
2. <b>-вши</b> shakli eskirgan: <s>прочита́вши</s> emas,
   <b>прочита́в</b>.<br>
3. Harakat feʼllarining bir qismi <b>-я</b> oladi:
   <em>вы́йти → вы́йдя</em>, <em>прийти́ → придя́</em>,
   <em>принести́ → принеся́</em>. Bularni yodlang.</div>

<div class="pe-ex">
  <p class="pe-ex__t">Ikkisi yonma-yon</p>
  <p class="pe-ex__ru"><b>Чита́я</b> письмо́, он улыба́лся.</p>
  <p class="pe-ex__uz">Xatni oʻqiyotib jilmayardi. — Ikkala ish <b>bir vaqtda</b>.</p>
  <p class="pe-ex__ru"><b>Прочита́в</b> письмо́, он улыбну́лся.</p>
  <p class="pe-ex__uz">Xatni oʻqib boʻlgach jilmaydi. — Avval oʻqidi, <b>keyin</b> jilmaydi.</p>
  <p class="pe-ex__why">Bitta harf farq — <em>-я</em> yoki <em>-в</em> — va
     butun manzara oʻzgaradi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha «-ib» ikki ishni bajaradi</span>
Mana shu joyda ehtiyot boʻling. Oʻzbekcha <b>-ib</b> ikkala maʼnoni
ham bera oladi:<br><br>
<em>Xatni oʻqi<b>b</b> jilmayardi</em> — bir vaqtda<br>
<em>Xatni oʻqi<b>b</b>, chiqib ketdi</em> — avval oʻqidi, keyin chiqdi<br><br>
Rus tilida esa <b>tanlash majburiy</b>: bir vaqtda boʻlsa —
<b>НСВ + -я</b> (<em>чита́я</em>), ketma-ket boʻlsa — <b>СВ + -в</b>
(<em>прочита́в</em>).<br><br>
Shuning uchun oʻzbekchadan tarjima qilayotganda <em>-ib</em> ni
koʻrishingiz yetarli emas. Bitta savol bering: <b>«bu ikki ish bir
paytda ketyaptimi yoki biri tugab, keyin ikkinchisi
boshlandimi?»</b></div>

<h3>4. Darsning yagona qatʼiy qoidasi: EGA BIR XIL</h3>

<p>Bu — rus tilidagi eng mashhur xatolardan biri, va uni bir marta
tushunsangiz, boshqa qilmaysiz.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--v">ravishdoshning egasi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">asosiy feʼlning egasi</span>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Возвраща́ясь домо́й, начался́ дождь.</s></p>
  <p class="pe-good">Возвраща́ясь домо́й, <b>я попа́л</b> под дождь</p>
</div>

<p>Nega birinchisi kulgili? Chunki unda <b>yomgʻir uyga qaytib
kelyapti</b>. Ravishdosh <em>возвраща́ясь</em> ning egasi asosiy
gapdagi ega bilan bir xil boʻlishi kerak edi — lekin u yerda
<em>дождь</em> turibdi.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Qulogʻingizga ishoning</span>
Bu qoida <b>oʻzbekchada ham bor</b>, va siz uni buzmaysiz:<br><br>
<em>Uyga qaytib, yomgʻirga tushdim.</em> ✓ — men qaytdim, men
tushdim<br>
<s>Uyga qaytib, yomgʻir boshlandi.</s> ✗ — yomgʻir uyga
qaytmaydi<br><br>
Yaʼni oʻzbekcha qulogʻingiz bu xatoni allaqachon eshitadi.
Ruschada yozayotganda faqat <b>bitta savol</b> bering:
<em>«bu ishni kim qildi?»</em> — javob ikkala qismda ham bir xil
boʻlishi shart.</div>

<h3>5. Vergul — bu safar oson</h3>

<p><b>Ravishdosh oborot har doim, har qanday oʻrinda vergul bilan
ajratiladi.</b> Причастие dan farqli oʻlaroq, oʻrni hech narsani
oʻzgartirmaydi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Uchta oʻrin, uchta vergul</p>
  <p class="pe-ex__ru"><b>Прочита́в письмо́,</b> он позвони́л сестре́.</p>
  <p class="pe-ex__ru">Он<b>, прочита́в письмо́,</b> позвони́л сестре́.</p>
  <p class="pe-ex__ru">Он позвони́л сестре́<b>, прочита́в письмо́</b>.</p>
  <p class="pe-ex__uz">Xatni oʻqigach, u singlisiga qoʻngʻiroq qildi.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ravishga aylanib qolganlari</span>
Baʼzi ravishdoshlar shu qadar koʻp ishlatilganki, endi oddiy
ravish boʻlib qolgan — <b>ular vergul olmaydi</b>:<br><br>
<em>Он рабо́тал <b>не спеша́</b>.</em> — Shoshilmasdan ishladi.<br>
<em>Он сиде́л <b>мо́лча</b>.</em> — Jim oʻtirdi.<br>
<em>Она́ слу́шала <b>не дыша́</b>.</em> — Nafas olmay tingladi.</div>

<h3>6. Inkor</h3>

<p>Inkor <em>не</em> ravishdoshdan <b>alohida</b> yoziladi:
<em><b>не зна́я</b></em>, <em><b>не поду́мав</b></em>,
<em><b>не попроща́вшись</b></em>.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Inkor bilan</p>
  <p class="pe-ex__ru"><b>Не зна́я</b> а́дреса, он до́лго иска́л дом.</p>
  <p class="pe-ex__uz">Manzilni bilmagani uchun uyni uzoq qidirdi.</p>
  <p class="pe-ex__ru">Он вы́шел, <b>не попроща́вшись</b>.</p>
  <p class="pe-ex__uz">U xayrlashmasdan chiqib ketdi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Чита́я кни́гу, мне ста́ло гру́стно.</s></p>
  <p class="pe-good">Чита́я кни́гу, <b>я загрусти́л</b> — egasi bir xil boʻlishi shart</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Прочита́вши письмо́, он позвони́л.</s></p>
  <p class="pe-good"><b>Прочита́в</b> письмо́ — <em>-вши</em> shakli eskirgan</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Верну́вши домо́й, я поу́жинал.</s></p>
  <p class="pe-good"><b>Верну́вшись</b> домо́й — <em>-ся</em> feʼli <b>-вшись</b> oladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он ушёл не попроща́вшись.</s></p>
  <p class="pe-good">Он ушёл<b>,</b> не попроща́вшись — oborot har doim vergul bilan</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Ravishdosh yasang. &nbsp; <b>рабо́тать</b> (НСВ)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>рабо́тая</strong>. «Они́»
    shakli — <em>рабо́таю[т]</em>, qoʻshimcha olib tashlanadi va
    <b>-я</b> qoʻshiladi. Maʼnosi «ishlab, ishlayotib».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Ravishdosh yasang. &nbsp; <b>верну́ться</b> (СВ)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>верну́вшись</strong>.
    <em>-ся</em> feʼllari <b>-вшись</b> oladi. <s>Верну́вши</s>
    yoki <s>верну́в</s> — notoʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Xatoni toping va tuzating.<br>
     <b>Подходя́ к до́му, у меня́ зазвони́л телефо́н.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Telefon uyga yaqinlashmaydi!
    Toʻgʻrisi: <strong>Подходя́ к до́му, я услы́шал звоно́к.</strong>
    Yoki ravishdoshdan voz keching: <em>Когда́ я подходи́л к до́му,
    у меня́ зазвони́л телефо́н.</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>Чита́я</b> yoki <b>прочита́в</b>? &nbsp;
     <b>___ письмо́, он сра́зу позвони́л сестре́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Прочита́в</strong>. Avval
    xat oʻqib boʻlindi, <b>keyin</b> qoʻngʻiroq qildi — bu
    ketma-ketlik, demak СВ. <em>Чита́я</em> «oʻqiyotib qoʻngʻiroq
    qildi» degan boshqa manzara berardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Uyga qaytayotib, men eski doʻstimni uchratdim.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Возвраща́ясь домо́й, я
    встре́тил ста́рого дру́га.</strong> «Qaytayotib» — davom
    etayotgan ish, demak <b>НСВ</b> va <em>-ясь</em>. Ikkala
    qismda ham ega <em>я</em> — qoida bajarildi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>дееприча́стие</b><span>ravishdosh</span></li>
  <li><b>чита́я</b><span>oʻqib, oʻqiyotib</span></li>
  <li><b>прочита́в</b><span>oʻqib boʻlgach</span></li>
  <li><b>возвраща́ясь</b><span>qaytayotib</span></li>
  <li><b>верну́вшись</b><span>qaytgach</span></li>
  <li><b>уви́дев</b><span>koʻrgach</span></li>
  <li><b>не спеша́</b><span>shoshilmasdan</span></li>
  <li><b>мо́лча</b><span>jim, indamay</span></li>
  <li><b>попроща́ться</b><span>xayrlashmoq</span></li>
  <li><b>грусти́ть</b><span>gʻamgin boʻlmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Причастие</b> — sifat (qanday?). <b>Деепричастие</b> —
        ravish (qachon? qanday qilib?) va <b>hech qachon
        oʻzgarmaydi</b>.</li>
    <li><b>НСВ → -я</b> (bir vaqtda) = oʻzbekcha <b>-ib</b>.
        <b>СВ → -в</b> (avval) = oʻzbekcha <b>-gach</b>.</li>
    <li><b>-ся feʼllari → -вшись</b>: <em>верну́вшись</em>.</li>
    <li><b>EGA BIR XIL BOʻLISHI SHART.</b> Ishonchingiz komil
        boʻlmasa — <em>когда́</em> li gap yozing.</li>
    <li>Oborot <b>har doim vergul</b> bilan, oʻrni muhim emas.</li>
    <li><b>Не</b> alohida yoziladi: <em>не зна́я</em>,
        <em>не попроща́вшись</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-73: Sifatning qisqa shakli: красив, готов, должен, рад",
        "category": "russian",
        "order": 73,
        "summary": (
            "Rus sifatining ikkinchi shakli — faqat kesim boʻlib keladi. Bu yerda "
            "рад, до́лжен, ну́жен, гото́в, прав yashaydi — kundalik nutqning oʻzagi."
        ),
        "stories": ["Он был прав"],
        "content": """
<h2>PR-73: Sifatning qisqa shakli: красив, готов, должен, рад</h2>

<p>Oʻtgan darsda <em>дверь закры́т<b>а</b></em> ni koʻrdingiz — qisqa
sifatdosh. Endi maʼlum boʻladiki, <b>oddiy sifatlarda ham</b> shunday
ikkinchi shakl bor. Va eng qizigʻi: rus tilining eng koʻp
ishlatiladigan soʻzlaridan bir nechtasi — <em>рад, до́лжен, ну́жен,
гото́в, прав</em> — kundalik nutqda <b>faqat shu shaklda</b>
yashaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Qisqa shaklni yasaysiz: <b>краси́вый → краси́в</b></li>
    <li>Ichidan chiqadigan unlini bilib olasiz: <b>у́мный → умён</b></li>
    <li><b>Мне ну́жен / нужна́ / ну́жно / нужны́</b> ni toʻgʻri qoʻyasiz</li>
    <li><b>До́лжен</b> ni shaxsga moslashtirasiz</li>
    <li>Toʻliq va qisqa shakl maʼnosidagi nozik farqni koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">— / а / о / ы</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">faqat kesim</span>
</div>

<h3>1. Toʻliq va qisqa</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">TOʻLIQ — aniqlovchi</p>
    <p><em><b>краси́вый</b> дом</em><br>chiroyli uy</p>
    <p>Otdan oldin turadi va uni aniqlaydi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">QISQA — kesim</p>
    <p><em>дом <b>краси́в</b></em><br>uy chiroyli</p>
    <p>Gapning kesimi. Otdan oldin <b>hech qachon</b> turmaydi.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Toʻliq</th><th>Erkak</th><th>Ayol</th><th>Oʻrta</th><th>Koʻplik</th></tr>
  <tr><td class="pr-stem">краси́вый</td><td class="pr-res">краси́в</td>
      <td class="pr-res">краси́ва</td><td class="pr-res">краси́во</td>
      <td class="pr-res">краси́вы</td></tr>
  <tr><td class="pr-stem">гото́вый</td><td class="pr-res">гото́в</td>
      <td class="pr-res">гото́ва</td><td class="pr-res">гото́во</td>
      <td class="pr-res">гото́вы</td></tr>
  <tr><td class="pr-stem">за́нятый</td><td class="pr-res">за́нят</td>
      <td class="pr-res">занята́</td><td class="pr-res">за́нято</td>
      <td class="pr-res">за́няты</td></tr>
  <tr><td class="pr-stem">похо́жий</td><td class="pr-res">похо́ж</td>
      <td class="pr-res">похо́жа</td><td class="pr-res">похо́же</td>
      <td class="pr-res">похо́жи</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bu yerda oʻzbekcha yordam bermaydi</span>
Oʻzbekchada sifat <b>bitta</b> shaklda yashaydi va oʻrni oʻzgarsa
ham oʻzgarmaydi:<br><br>
<em><b>chiroyli</b> uy</em> — aniqlovchi<br>
<em>uy <b>chiroyli</b></em> — kesim<br><br>
Ruschada esa gapning kesimi boʻlgan sifat <b>boshqa shaklga</b>
oʻtishi mumkin. Shuning uchun bu dars — kursdagi kam sonli
«oʻzbekchada bunday narsa yoʻq» darslaridan biri. Uni yodlash
kerak, chiqarib olib boʻlmaydi.<br><br>
Xushxabar ham bor: <b>ogʻzaki nutqda</b> ruslar koʻpincha toʻliq
shaklni ishlatadi — <em>дом краси́вый</em>. Qisqa shakl kitobiy.
Lekin 3-boʻlimdagi toʻplam bundan mustasno — u har kuni
kerak.</div>

<h3>2. Ichidan chiqadigan unli: умный → умён</h3>

<p>Oʻzak ikkita undosh bilan tugasa, erkak shaklida ular orasiga
<b>-е-</b> yoki <b>-о-</b> qoʻshiladi. Boshqa shakllarda u yoʻqoladi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Toʻliq</th><th>Erkak</th><th>Ayol</th><th>Koʻplik</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">у́мный</td><td class="pr-res">ум<b>ё</b>н</td>
      <td class="pr-uz">умна́</td><td class="pr-uz">умны́</td><td class="pr-end">aqlli</td></tr>
  <tr><td class="pr-stem">си́льный</td><td class="pr-res">сил<b>ё</b>н</td>
      <td class="pr-uz">сильна́</td><td class="pr-uz">сильны́</td><td class="pr-end">kuchli</td></tr>
  <tr><td class="pr-stem">ну́жный</td><td class="pr-res">ну́ж<b>е</b>н</td>
      <td class="pr-uz">нужна́</td><td class="pr-uz">нужны́</td><td class="pr-end">kerak</td></tr>
  <tr><td class="pr-stem">до́лжный</td><td class="pr-res">до́лж<b>е</b>н</td>
      <td class="pr-uz">должна́</td><td class="pr-uz">должны́</td><td class="pr-end">majbur, kerak</td></tr>
  <tr><td class="pr-stem">свобо́дный</td><td class="pr-res">свобо́д<b>е</b>н</td>
      <td class="pr-uz">свобо́дна</td><td class="pr-uz">свобо́дны</td><td class="pr-end">boʻsh, ozod</td></tr>
  <tr><td class="pr-stem">больно́й</td><td class="pr-res">б<b>о́</b>лен</td>
      <td class="pr-uz">больна́</td><td class="pr-uz">больны́</td><td class="pr-end">kasal</td></tr>
  <tr><td class="pr-stem">интере́сный</td><td class="pr-res">интере́с<b>е</b>н</td>
      <td class="pr-uz">интере́сна</td><td class="pr-uz">интере́сны</td><td class="pr-end">qiziqarli</td></tr>
</table></div>

<h3>3. Har kuni kerak boʻladigan toʻplam</h3>

<p>Bu boʻlim darsning yuragi. Quyidagi soʻzlar kundalik nutqda
<b>deyarli har doim qisqa shaklda</b> keladi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">рад</td><td class="pr-uz">xursand</td>
      <td class="pr-res">Я рад вас ви́деть.</td></tr>
  <tr><td class="pr-stem">до́лжен</td><td class="pr-uz">majbur, …ishi kerak</td>
      <td class="pr-res">Я до́лжен идти́.</td></tr>
  <tr><td class="pr-stem">ну́жен</td><td class="pr-uz">kerak</td>
      <td class="pr-res">Мне ну́жен слова́рь.</td></tr>
  <tr><td class="pr-stem">гото́в</td><td class="pr-uz">tayyor</td>
      <td class="pr-res">Обе́д гото́в.</td></tr>
  <tr><td class="pr-stem">прав</td><td class="pr-uz">haq</td>
      <td class="pr-res">Ты был прав.</td></tr>
  <tr><td class="pr-stem">винова́т</td><td class="pr-uz">aybdor</td>
      <td class="pr-res">Я винова́т.</td></tr>
  <tr><td class="pr-stem">согла́сен</td><td class="pr-uz">rozi</td>
      <td class="pr-res">Я согла́сен с тобо́й.</td></tr>
  <tr><td class="pr-stem">за́нят</td><td class="pr-uz">band</td>
      <td class="pr-res">Извини́, я за́нят.</td></tr>
  <tr><td class="pr-stem">свобо́ден</td><td class="pr-uz">boʻsh</td>
      <td class="pr-res">Ты свобо́ден в суббо́ту?</td></tr>
  <tr><td class="pr-stem">бо́лен</td><td class="pr-uz">kasal</td>
      <td class="pr-res">Он бо́лен уже́ неде́лю.</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__t">Kundalik nutqda</p>
  <p class="pe-ex__ru">— Ты <b>свобо́ден</b> в суббо́ту? — Нет, я <b>за́нят</b>.</p>
  <p class="pe-ex__uz">— Shanba kuni boʻshmisan? — Yoʻq, bandman.</p>
  <p class="pe-ex__ru">— Я <b>согла́сен</b>, ты был <b>прав</b>. Извини́, я <b>винова́т</b>.</p>
  <p class="pe-ex__uz">— Roziman, sen haq eding. Kechir, aybdorman.</p>
  <p class="pe-ex__why">Beshta soʻz, beshtasi ham qisqa shaklda. Bu
     gaplarda toʻliq shakl umuman ishlatilmaydi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Sovgʻa: toʻplam bir-bir tushadi</span>
Bu darsning shakllari yangi boʻlsa ham, <b>maʼnolari</b> sizga
tanish. Oʻzbekchada bu soʻzlar ham alohida turkum boʻlib turadi —
ular sifat ham emas, feʼl ham emas:<br><br>
<em>xursand</em> &nbsp;→&nbsp; <b>рад</b><br>
<em>kerak</em> &nbsp;→&nbsp; <b>ну́жен</b><br>
<em>…ishi kerak, majbur</em> &nbsp;→&nbsp; <b>до́лжен</b><br>
<em>rozi</em> &nbsp;→&nbsp; <b>согла́сен</b><br>
<em>tayyor</em> &nbsp;→&nbsp; <b>гото́в</b><br>
<em>haq</em> &nbsp;→&nbsp; <b>прав</b><br>
<em>aybdor</em> &nbsp;→&nbsp; <b>винова́т</b><br><br>
Yaʼni yodlash kerak boʻlgani — <b>qoʻshimchalar</b>, maʼnolar
emas. Shu yettitasini shakllari bilan yodlab olsangiz, kundalik
suhbatning katta qismi yopiladi.</div>

<div class="pe-call pe-rule"><span class="pe-call__t">«Ра́дый» degan soʻz yoʻq</span>
<b>Рад</b> ning toʻliq shakli umuman mavjud emas — u har doim
qisqa:<br><br>
<s>Я ра́дый вас ви́деть.</s> &nbsp;→&nbsp; <b>Я рад вас
ви́деть.</b><br>
<em>Она́ ра́да. Мы ра́ды.</em><br><br>
Bu <em>смея́ться</em> (PR-62) kabi: soʻzning bitta shakli bor,
ikkinchisi yoʻq.</div>

<h3>4. Мне ну́жен — narsaga moslashadi</h3>

<p>Bu joy oʻzbek oʻquvchisi uchun eng katta tuzoq. <em>Ну́жен</em>
<b>kerak boʻlgan narsaga</b> moslashadi, odamga emas.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kerak narsa</th><th>Shakl</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-uz">erkak</td><td class="pr-end">ну́жен</td>
      <td class="pr-res">Мне ну́жен слова́рь.</td><td class="pr-stem">Menga lugʻat kerak.</td></tr>
  <tr><td class="pr-uz">ayol</td><td class="pr-end">нужна́</td>
      <td class="pr-res">Мне нужна́ по́мощь.</td><td class="pr-stem">Menga yordam kerak.</td></tr>
  <tr><td class="pr-uz">oʻrta</td><td class="pr-end">ну́жно</td>
      <td class="pr-res">Мне ну́жно вре́мя.</td><td class="pr-stem">Menga vaqt kerak.</td></tr>
  <tr><td class="pr-uz">koʻplik</td><td class="pr-end">нужны́</td>
      <td class="pr-res">Мне нужны́ де́ньги.</td><td class="pr-stem">Menga pul kerak.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Ikki soʻz, ikki tomon</span>
Oʻzbekchada <em>kerak</em> hech qachon oʻzgarmaydi: <em>menga
lugʻat kerak</em>, <em>menga pul kerak</em> — bir xil soʻz.
Ruschada esa moslashish bor, va u <b>ikki xil tomonga</b>
qaraydi:<br><br>
<b>Ну́жен</b> — <b>narsa</b>ga qaraydi:
<em>Мне <b>нужна́</b> кни́га</em> (kitob ayol jinsida).<br>
<b>До́лжен</b> — <b>odam</b>ga qaraydi:
<em>Она́ <b>должна́</b> рабо́тать</em> (u ayol).<br><br>
Oʻzbekchada ham shaxs bir joyda belgilanadi:
<em>bor<b>ishim</b> kerak</em> ↔ <em>bor<b>ishi</b> kerak</em>.
Faqat bizda u feʼlga, ruschada esa <em>до́лжен</em> ga
qoʻshiladi.</div>

<h3>5. До́лжен + infinitiv</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Shaxsga moslashadi</p>
  <p class="pe-ex__ru">Я <b>до́лжен</b> идти́. <span class="pr-uz">(erkak)</span></p>
  <p class="pe-ex__ru">Я <b>должна́</b> идти́. <span class="pr-uz">(ayol)</span></p>
  <p class="pe-ex__ru">Мы <b>должны́</b> помо́чь ему́. <span class="pr-uz">(koʻplik)</span></p>
  <p class="pe-ex__uz">Borishim kerak. · Borishim kerak. · Unga yordam berishimiz kerak.</p>
  <p class="pe-ex__why">Oʻzbekchada erkak va ayol bir xil gapiradi.
     Ruschada esa <b>ayol «должна́» deyishi shart</b>.</p>
</div>

<h3>6. Maʼnodagi nozik farq</h3>

<p>Ikkala shakl ham mumkin boʻlganda, ular biroz boshqa narsa
aytadi:</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">TOʻLIQ — doimiy belgi</p>
    <p><em>Он больно́й.</em><br>U kasalmand odam (doim).</p>
    <p><em>Она́ весёлая.</em><br>U quvnoq tabiatli.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">QISQA — hozirgi holat</p>
    <p><em>Он бо́лен.</em><br>U hozir kasal.</p>
    <p><em>Она́ весела́.</em><br>U bugun kayfiyati chogʻ.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Juda foydali qoʻshimcha maʼno</span>
Oʻlchov haqidagi qisqa shakl «<b>juda ham</b>, <b>keragidan
ortiq</b>» degan maʼnoni beradi:<br><br>
<em>Ту́фли <b>малы́</b>.</em> — Tuflilar (menga) kichkina.<br>
<em>Пальто́ <b>велико́</b>.</em> — Palto katta (kelmaydi).<br>
<em>Ю́бка <b>длинна́</b>.</em> — Yubka uzun.<br><br>
Doʻkonda kiyim oʻlchayotganda bu shakl har doim kerak boʻladi:
<em>ма́ленькие ту́фли</em> — kichik tuflilar, <em>ту́фли малы́</em> —
oyogʻimga kichiklik qilyapti.</div>

<div class="pe-ex">
  <p class="pe-ex__t">Doimiy belgi ↔ hozirgi holat</p>
  <p class="pe-ex__ru">Э́то о́чень <b>весёлый</b> челове́к.</p>
  <p class="pe-ex__uz">Bu juda quvnoq odam. — Tabiati shunday.</p>
  <p class="pe-ex__ru">Сего́дня она́ <b>весела́</b>.</p>
  <p class="pe-ex__uz">Bugun uning kayfiyati chogʻ. — Faqat bugun.</p>
  <p class="pe-ex__why">Oʻzbekchada ikkala gapda ham «quvnoq»
     turadi. Ruschada esa shaklning oʻzi «doimiymi yoki
     hozirmi» degan javobni beradi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ра́дый вас ви́деть.</s></p>
  <p class="pe-good">Я <b>рад</b> вас ви́деть — «ра́дый» degan soʻz yoʻq</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мне ну́жно кни́га.</s></p>
  <p class="pe-good">Мне <b>нужна́</b> кни́га — <em>кни́га</em> ayol jinsida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Дилно́за до́лжен идти́.</s></p>
  <p class="pe-good">Дилно́за <b>должна́</b> идти́ — <em>до́лжен</em> odamga moslashadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Она́ согла́сная со мной.</s></p>
  <p class="pe-good">Она́ <b>согла́сна</b> со мной — kesim, demak qisqa shakl</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Мне ___ по́мощь.</b> (ну́жный)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>нужна́</strong>.
    <em>По́мощь</em> — ayol jinsida (yumshoq belgi bilan tugagan ot),
    <em>ну́жен</em> esa <b>kerak boʻlgan narsaga</b>
    moslashadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Qisqa shaklni yasang. &nbsp; <b>у́мный</b> (erkak)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>умён</strong>. Oʻzak
    <em>умн-</em> ikkita undosh bilan tugagan, shuning uchun ular
    orasiga <b>-ё-</b> chiqadi. Ayol shaklida u yoʻqoladi:
    <em>умна́</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Afsona gapiryapti. Toʻgʻri shaklni tanlang.<br>
     <b>Я ___ верну́ться до восьми́.</b> (до́лжен)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>должна́</strong>. Afsona —
    ayol, <em>до́лжен</em> esa <b>gapirayotgan odamga</b>
    moslashadi. Oʻzbekchada bu farq eshitilmaydi, ruschada esa
    darrov bilinadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu ikki gapning farqi nima?<br>
     <b>Он больно́й. · Он бо́лен.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — <b>doimiy belgi</b>:
    kasalmand odam. Ikkinchisi — <b>hozirgi holat</b>: hozir
    kasal, ertaga tuzaladi. Qisqa shakl vaqtinchalik holatni
    bildiradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Sen haq eding, men esa aybdorman.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ты был прав, а я
    винова́т.</strong> Ikkalasi ham qisqa shakl. <em>А</em>
    ishlatildi, chunki bu solishtirish (PR-67). Ayol
    aytayotgan boʻlsa: <em>Ты был прав, а я винова́та.</em></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>рад / ра́да</b><span>xursand</span></li>
  <li><b>до́лжен / должна́</b><span>majbur, …ishi kerak</span></li>
  <li><b>ну́жен / нужна́</b><span>kerak</span></li>
  <li><b>гото́в / гото́ва</b><span>tayyor</span></li>
  <li><b>прав / права́</b><span>haq</span></li>
  <li><b>винова́т</b><span>aybdor</span></li>
  <li><b>согла́сен / согла́сна</b><span>rozi</span></li>
  <li><b>за́нят / занята́</b><span>band</span></li>
  <li><b>свобо́ден</b><span>boʻsh, ozod</span></li>
  <li><b>умён / умна́</b><span>aqlli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Qisqa sifat — <b>faqat kesim</b>. Otdan oldin hech qachon
        turmaydi.</li>
    <li>Yasalish: oʻzak + <b>— / а / о / ы</b>. Ikki undosh
        boʻlsa, orasidan <b>-е-/-ё-</b> chiqadi:
        <em>у́мный → умён</em>.</li>
    <li><b>Ну́жен narsaga</b> moslashadi: <em>мне нужна́
        кни́га</em>.</li>
    <li><b>До́лжен odamga</b> moslashadi: <em>она́ должна́
        идти́</em>.</li>
    <li>«<b>Ра́дый</b>» degan soʻz <b>yoʻq</b> — faqat
        <em>рад, ра́да, ра́ды</em>.</li>
    <li>Toʻliq = doimiy belgi, qisqa = <b>hozirgi holat</b>:
        <em>он больно́й</em> ↔ <em>он бо́лен</em>.</li>
    <li>Oʻlchovda qisqa shakl «keragidan ortiq» degani:
        <em>ту́фли малы́</em>.</li>
  </ul>
</div>
""",
    },
]
