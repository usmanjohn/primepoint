# -*- coding: utf-8 -*-
"""Prime Russian — Block G yakuni: soʻz yasalishi (86–88).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Uchta dars bitta gʻoyaning uchta qismi: rus soʻzlari tasodifiy emas,
ular QURILGAN. Shuning uchun oʻquvchi hech qachon koʻrmagan soʻzni ham
oʻqiy oladi — bu kursning eng katta amaliy sovgʻasi.

PR-86 — toʻrtta gʻisht: приставка + корень + суффикс + окончание.
Oʻzbekcha lever: oʻzbek tili ham aynan shunday ishlaydi (ish+chi+lar+
imiz+ga), farqi bitta — oʻzbekchada PREFIKS yoʻq, hamma narsa oʻzakdan
keyin keladi. Ikkinchi muhim farq: ruschada суффикс YANGI SOʻZ yasaydi,
окончание esa faqat shaklni oʻzgartiradi.
PR-87 — suffikslar xaritasi. Darsning gavhari: suffiks nafaqat maʼnoni,
balki JINSNI ham aytadi (-тель м.р., -ость ж.р., -ение/-ство ср.р.).
Oʻzbekcha lever ikkita va ikkalasi ham toza: -тель/-щик/-ник ↔ «-chi»,
-ость/-ство ↔ «-lik», -ение ↔ «-(i)sh».
PR-88 — kichraytirish va erkalash. Oʻzbekchada bu ikki maʼno IKKI xil
qoʻshimchada (-cha kichraytiradi, -jon erkalaydi), ruschada esa bitta
shaklda. Aynan shu joyda oʻzbek oʻquvchi «домик» ni har doim «kichik
uy» deb tarjima qilib xato qiladi.

⚠️ Oʻqish matnlarida URGʻU BELGISI YOʻQ (2026-08-24) — darsliklar saqlaydi.

Mashqlar:        practice/management/commands/_practice_pr_86_88.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_86_88.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_86_88.py --author=prime
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
        "title": "PR-86: Soʻz yasalishi: приставка + корень + суффикс + окончание",
        "category": "russian",
        "order": 86,
        "summary": (
            "Rus soʻzlari toʻrtta gʻishtdan qurilgan. Shu toʻrttasini ajratishni "
            "bilsangiz, lugʻatsiz ham notanish soʻzning maʼnosini topa olasiz."
        ),
        "stories": ["Один корень — сорок слов"],
        "content": """
<h2>PR-86: Soʻz yasalishi: приставка + корень + суффикс + окончание</h2>

<p>Tasavvur qiling: matnda <b>переписа́ть</b> degan soʻzni koʻrdingiz va
uni hech qachon uchratmagansiz. Lugʻat yoʻq. Lekin siz
<b>писа́ть</b> ni bilasiz, <b>пере-</b> ni esa PR-57 da olgansiz — u
«qayta, boshqatdan» degani.</p>

<p>Demak, javob oʻzingizda: <b>qayta yozmoq</b>. Lugʻat kerak
boʻlmadi.</p>

<p>Rus tilining eng katta sovgʻasi shu. Uning soʻzlari tasodifiy emas —
ular <b>qurilgan</b>. Bu darsda biz qurilishni ochamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Soʻzni <b>toʻrtta gʻishtga</b> ajratasiz: приста́вка · ко́рень · су́ффикс · оконча́ние</li>
    <li><b>Oʻzakni</b> topishning ishonchli usulini oʻrganasiz</li>
    <li><b>Су́ффикс</b> va <b>оконча́ние</b> ni bir-biridan ajratasiz — bu ikkisi bir xil narsa emas</li>
    <li>Oʻzak nega oʻzgarishini bilasiz: <b>чередова́ние</b></li>
    <li>Notanish soʻzni <b>taxmin qilishni</b> mashq qilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--adv">приста́вка</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">ко́рень</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">су́ффикс</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">оконча́ние</span>
</div>

<h3>1. Toʻrtta gʻisht</h3>

<p>Har bir gʻishtning oʻz vazifasi bor. Ular oʻrin almashmaydi va
tartibi hech qachon buzilmaydi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gʻisht</th><th>Qayerda</th><th>Nima qiladi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">приста́вка</td><td class="pr-uz">oʻzakdan <b>oldin</b></td>
      <td class="pr-end">maʼnoni burdi</td><td class="pr-res"><b>пере</b>писа́ть</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">ко́рень</td><td class="pr-uz">oʻrtada</td>
      <td class="pr-end">asosiy maʼno</td><td class="pr-res">пере<b>пис</b>а́ть</td></tr>
  <tr><td class="pr-stem">су́ффикс</td><td class="pr-uz">oʻzakdan <b>keyin</b></td>
      <td class="pr-end">yangi soʻz yasadi</td><td class="pr-res">писа́<b>тель</b></td></tr>
  <tr><td class="pr-stem">оконча́ние</td><td class="pr-uz">eng oxirida</td>
      <td class="pr-end">grammatik shakl</td><td class="pr-res">писа́тел<b>я</b></td></tr>
</table></div>

<p>Toʻrttasi ham bir soʻzda uchraganiga qarang:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Приста́вка</th><th>Ко́рень</th><th>Су́ффикс</th><th>Оконча́ние</th></tr>
  <tr><td class="pr-res">перепи́сывать</td><td class="pr-stem">пере</td>
      <td class="pr-end">пис</td><td class="pr-stem">ыва</td><td class="pr-end">ть</td></tr>
  <tr><td class="pr-res">пришко́льный</td><td class="pr-stem">при</td>
      <td class="pr-end">школь</td><td class="pr-stem">н</td><td class="pr-end">ый</td></tr>
  <tr><td class="pr-res">подсне́жник</td><td class="pr-stem">под</td>
      <td class="pr-end">снеж</td><td class="pr-stem">ник</td><td class="pr-end">—</td></tr>
  <tr><td class="pr-res">учи́тельница</td><td class="pr-stem">—</td>
      <td class="pr-end">уч</td><td class="pr-stem">и + тель + ниц</td><td class="pr-end">а</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Подсне́жник — bitta soʻzda butun rasm</span>
<b>под</b> (tagida) + <b>снеж</b> (qor) + <b>ник</b> (narsa) =
«qor tagidagi narsa». Bu — <b>boychechak</b>.<br><br>
Oʻzbekcha nomi ham xuddi shunday tuzilgan: <em>boy</em> + <em>chechak</em>.
Ikkala til ham gulni tasvirlab nom qoʻygan, faqat boshqa tomonidan.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbek tili ham aynan shunday ishlaydi</span>
Oʻzbekcha soʻzni ham gʻishtlarga ajratish mumkin, va siz buni maktabdan
beri qilasiz:<br><br>
<b>ish</b> + <b>chi</b> + <b>lar</b> + <b>imiz</b> + <b>ga</b><br>
oʻzak &nbsp;·&nbsp; suffiks &nbsp;·&nbsp; qoʻshimchalar<br><br>
Ruscha ham xuddi shunday: <b>пис</b> + <b>а</b> + <b>тел</b> +
<b>ям</b> — «yozuvchilarga».<br><br>
<b>Bitta farq bor, va u muhim:</b> oʻzbek tilida <b>prefiks yoʻq</b>.
Oʻzbekchada hamma narsa oʻzakdan <b>keyin</b> yopishadi. Ruschada esa
oldindan ham qoʻshiladi — <em>пере-, при-, вы-, под-, без-</em>.
Shuning uchun oʻzbek oʻquvchi odatda soʻzning oxirini yaxshi koʻradi va
boshini eʼtiborsiz oʻqiydi. Rus tilida esa soʻzning <b>boshi</b>
koʻpincha eng muhim qismi.</div>

<h3>2. Ко́рень — soʻzning yuragi</h3>

<p>Oʻzakni topish uchun bitta ishonchli usul bor: <b>qarindosh
soʻzlarni yigʻing</b> va ularda takrorlanayotgan qismni oling.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Qarindosh soʻzlar — однокоренны́е слова́</p>
  <p class="pe-ex__ru">писа́ть · написа́ть · пи́сьменный · писа́тель ·
     письмо́ · за́пись · по́дпись · опи́сывать</p>
  <p class="pe-ex__uz">Hammasida <b>пис / пись</b> bor. Demak, oʻzak — <b>-пис-</b>.</p>
  <p class="pe-ex__why">Maʼnosi ham bitta oilaga tegishli: yozish,
     yozuv, yozgan odam, yozilgan narsa.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Oʻxshash koʻrinish — qarindoshlik emas</span>
<b>Вода́</b> (suv) va <b>води́ть</b> (boshqarmoq) bir-biriga oʻxshaydi,
lekin qarindosh emas: birinchisining oʻzagi <em>-вод-</em> «suv»,
ikkinchisiniki <em>-вод-</em> «yetaklamoq». Faqat shaklga qarab emas,
<b>maʼnoga ham</b> qarang.</div>

<h3>3. Приста́вка — maʼnoni burovchi</h3>

<p>Prefikslarni PR-57 va PR-58 da feʼllar bilan koʻrgansiz. Lekin
ular faqat feʼlga qoʻshilmaydi — ot va sifatga ham qoʻshiladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Приста́вка</th><th>Maʼnosi</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">не-</td><td class="pr-uz">inkor</td>
      <td class="pr-res"><b>не</b>возмо́жный</td><td class="pr-end">imkonsiz</td></tr>
  <tr><td class="pr-stem">без- / бес-</td><td class="pr-uz">…siz</td>
      <td class="pr-res"><b>без</b>рабо́тный</td><td class="pr-end">ishsiz</td></tr>
  <tr><td class="pr-stem">пере-</td><td class="pr-uz">qayta; ustidan</td>
      <td class="pr-res"><b>пере</b>писа́ть</td><td class="pr-end">qayta yozmoq</td></tr>
  <tr><td class="pr-stem">при-</td><td class="pr-uz">yaqin, yonidagi</td>
      <td class="pr-res"><b>при</b>шко́льный</td><td class="pr-end">maktab yonidagi</td></tr>
  <tr><td class="pr-stem">под-</td><td class="pr-uz">tagida</td>
      <td class="pr-res"><b>под</b>во́дный</td><td class="pr-end">suv ostidagi</td></tr>
  <tr><td class="pr-stem">со-</td><td class="pr-uz">birga</td>
      <td class="pr-res"><b>со</b>рабо́тник</td><td class="pr-end">hamkasb</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">З yoki С — quloqqa qarab</span>
<b>без-</b>, <b>из-</b>, <b>раз-</b> kabi prefikslar <b>jarangsiz</b>
undosh oldida <b>с</b> ga aylanadi. Sababi oddiy — shunday aytish
oson:<br><br>
без + рабо́тный → <b>без</b>рабо́тный (р jarangli)<br>
без + поле́зный → <b>бес</b>поле́зный (п jarangsiz)<br>
без + коне́чный → <b>бес</b>коне́чный<br>
раз + сказа́ть → <b>рас</b>сказа́ть<br>
из + по́ртить → <b>ис</b>по́ртить<br><br>
Bu — PR-4 dagi <b>оглуше́ние</b> ning yozuvdagi koʻrinishi. Boshqa
joyda rus tili jarangsizlanishni yozmaydi (<em>хлеб</em>,
<s>хлеп</s> emas), lekin bu uch prefiksda <b>yozadi</b>.</div>

<h3>4. Су́ффикс — yangi soʻz yasovchi</h3>

<p>Suffiks soʻzning shaklini emas, <b>oʻzini</b> oʻzgartiradi: undan
lugʻatda alohida turadigan yangi soʻz chiqadi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Bitta oʻzak, toʻrtta soʻz</p>
  <p class="pe-ex__ru">учи́ть → учи́<b>тель</b> → уче́б<b>ник</b> → уч<b>ени́к</b></p>
  <p class="pe-ex__uz">oʻrgatmoq → oʻqituvchi → darslik → oʻquvchi</p>
  <p class="pe-ex__why">Toʻrttasi ham lugʻatda alohida soʻz. Keyingi
     dars — PR-87 — butunlay shu suffikslarga bagʻishlangan.</p>
</div>

<h3>5. Оконча́ние — grammatika, xolos</h3>

<p>Mana bu farqni tushunsangiz, dars oʻz haqini oqlaydi. Suffiks
<b>yangi soʻz</b> yasaydi; окончание esa <b>oʻsha soʻzning</b>
boshqa shakli.</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">СУ́ФФИКС — ikki xil soʻz</p>
    <p><em>учи́ть</em> va <em>учи́тель</em></p>
    <p>Biri — feʼl, ikkinchisi — odam. Lugʻatda <b>ikki</b> maqola.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ОКОНЧА́НИЕ — bitta soʻz</p>
    <p><em>учи́тель</em> va <em>учи́теля</em></p>
    <p>Bitta odam, ikki kelishik. Lugʻatda <b>bitta</b> maqola.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekchada ham shu ikkilik bor</span>
Siz buni allaqachon his qilasiz, faqat nomini bilmaysiz:<br><br>
<em>ish → ish<b>chi</b></em> — yangi soʻz, lugʻatda alohida turadi.
Bu <b>suffiks</b>.<br>
<em>ishchi → ishchi<b>ga</b></em> — oʻsha odam, boshqa kelishikda.
Bu <b>окончание</b>.<br><br>
Ruschada ham aynan shunday: <em>уч → учи́<b>тель</b></em> (yangi
soʻz), <em>учи́тель → учи́тел<b>ю</b></em> (oʻsha odam, Да́тельный).</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Оконча́ние yoʻq boʻlishi ham mumkin</span>
<b>Дом</b>, <b>стол</b>, <b>подсне́жник</b> — bularning okonchaniyesi
<b>boʻsh</b> (jadvalda «—» deb yozdik). Bu «yoʻq» degani emas:
kelishik oʻzgarishi bilanoq u paydo boʻladi — <em>до́м<b>а</b>,
до́м<b>у</b>, до́м<b>ом</b></em>.</div>

<h3>6. Чередова́ние — oʻzak nega oʻzgaradi</h3>

<p>Baʼzan qarindosh soʻzlarda oʻzak biroz boshqacha koʻrinadi. Bu
boshqa oʻzak emas — bu <b>чередова́ние</b>, yaʼni tovushlarning
almashinuvi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Almashinuv</th><th>Birinchi shakl</th><th>Ikkinchi shakl</th><th>Izoh</th></tr>
  <tr><td class="pr-stem">с / ш</td><td class="pr-res">писа́ть</td>
      <td class="pr-res">пишу́</td><td class="pr-uz">PR-22 da uchragan</td></tr>
  <tr><td class="pr-stem">д / ж</td><td class="pr-res">ходи́ть</td>
      <td class="pr-res">хожу́</td><td class="pr-uz">I shaxs birlikda</td></tr>
  <tr><td class="pr-stem">к / ч</td><td class="pr-res">рука́</td>
      <td class="pr-res">ру́чка</td><td class="pr-uz">suffiks oldida</td></tr>
  <tr><td class="pr-stem">г / ж</td><td class="pr-res">кни́га</td>
      <td class="pr-res">кни́жка</td><td class="pr-uz">suffiks oldida</td></tr>
  <tr><td class="pr-stem">е / —</td><td class="pr-res">день</td>
      <td class="pr-res">дня</td><td class="pr-uz">«qochoq» unli</td></tr>
  <tr><td class="pr-stem">о / —</td><td class="pr-res">оте́ц</td>
      <td class="pr-res">отца́</td><td class="pr-uz">«qochoq» unli</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekchada ham «qochoq unli» bor</span>
Oxirgi ikki qator sizga tanish tuyulishi kerak. Oʻzbekchada ham
qoʻshimcha qoʻshilganda unli tushib qoladi:<br><br>
<em>ogʻiz → ogʻ<b>z</b>im</em> &nbsp;·&nbsp;
<em>burun → bur<b>n</b>i</em> &nbsp;·&nbsp;
<em>shahar → shah<b>r</b>i</em><br><br>
Ruschada ham xuddi shunday: <em>день → дня</em>,
<em>оте́ц → отца́</em>, <em>у́гол → угла́</em>.<br><br>
Yaʼni bu hodisa siz uchun yangi emas — faqat nomi yangi.</div>

<h3>7. Bitta oʻzak — qirq soʻz</h3>

<p>Endi kuchni koʻring. Mana <b>-ход-</b> oʻzagi («yurish»), va undan
oʻsib chiqqan soʻzlar:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Qanday qurilgan</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">вход</td><td class="pr-stem">в + ход</td>
      <td class="pr-end">kirish (joy)</td></tr>
  <tr><td class="pr-res">вы́ход</td><td class="pr-stem">вы + ход</td>
      <td class="pr-end">chiqish (joy)</td></tr>
  <tr><td class="pr-res">перехо́д</td><td class="pr-stem">пере + ход</td>
      <td class="pr-end">oʻtish joyi</td></tr>
  <tr><td class="pr-res">похо́дка</td><td class="pr-stem">по + ход + ка</td>
      <td class="pr-end">yurish tarzi</td></tr>
  <tr><td class="pr-res">пешехо́д</td><td class="pr-stem">пеш + е + ход</td>
      <td class="pr-end">piyoda</td></tr>
  <tr><td class="pr-res">парохо́д</td><td class="pr-stem">пар + о + ход</td>
      <td class="pr-end">paroxod</td></tr>
  <tr><td class="pr-res">вездехо́д</td><td class="pr-stem">везде + ход</td>
      <td class="pr-end">har joyda yuruvchi mashina</td></tr>
  <tr><td class="pr-res">дохо́д</td><td class="pr-stem">до + ход</td>
      <td class="pr-end">daromad</td></tr>
  <tr><td class="pr-res">расхо́д</td><td class="pr-stem">рас + ход</td>
      <td class="pr-end">xarajat</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ikki oʻzak, oʻrtada «o» yoki «e»</span>
<em>пар<b>о</b>хо́д</em>, <em>пеш<b>е</b>хо́д</em>,
<em>сам<b>о</b>лёт</em>, <em>вод<b>о</b>па́д</em> —
ruschada ikkita oʻzakni bitta soʻzga qoʻshish uchun oʻrtaga
<b>о</b> yoki <b>е</b> qoʻyiladi.<br><br>
Oʻzbekchada bunday soʻzlar ham bor, faqat ular ulanmay yoziladi:
<em>suv quvuri</em>, <em>oʻt oʻchiruvchi</em>. Ruschada esa hammasi
<b>bitta soʻz</b> boʻlib yopishadi.</div>

<h3>8. Notanish soʻzni yechish — uch qadam</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Mashq: водопрово́д</p>
  <p class="pe-ex__ru">1. Oʻzaklarni toping: <b>вод</b> (suv) va <b>провод</b> (oʻtkazgich).</p>
  <p class="pe-ex__ru">2. Bogʻlovchi unlini koʻring: <b>о</b>.</p>
  <p class="pe-ex__ru">3. Qoʻshing: «suv oʻtkazuvchi».</p>
  <p class="pe-ex__uz">Javob: <b>vodoprovod</b>, yaʼni suv quvuri. Lugʻatsiz topildi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>«Переписа́ть» ning oʻzagi — «переп».</s></p>
  <p class="pe-good">Oʻzagi <b>пис</b>; <em>пере-</em> — приста́вка. Qarindosh
     soʻzlarni yigʻing: <em>писа́ть, письмо́, писа́тель</em>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>«Учи́тель» va «учи́теля» — ikki xil soʻz.</s></p>
  <p class="pe-good">Bitta soʻz, ikki shakl — farq faqat <b>окончание</b> da.
     Yangi soʻz suffiks orqali chiqadi: <em>учи́ть → учи́тель</em>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>«Пишу́» va «писа́ть» — turli oʻzak: пиш va пис.</s></p>
  <p class="pe-good">Oʻzak bitta. <b>с/ш</b> — чередова́ние, tovush almashinuvi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>безполе́зный</s></p>
  <p class="pe-good"><b>бес</b>поле́зный — jarangsiz <em>п</em> oldida
     <em>без-</em> → <em>бес-</em>.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>Подсне́жник</b> soʻzini gʻishtlarga ajrating va maʼnosini toping.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>под + снеж + ник</strong>,
    окончание boʻsh. «Qor tagidan chiquvchi» — <b>boychechak</b>.
    Oʻzak <em>-снеж-</em>, чередование bilan <em>снег</em> dan
    chiqqan (г/ж).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu soʻzlarning umumiy oʻzagi qaysi?<br>
     <b>учи́тель · учени́к · уче́бник · изуча́ть · учёный</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>-уч-</strong>. Beshtasi ham
    bitta oilaga tegishli: oʻrgatuvchi, oʻrganuvchi, oʻrganish
    kitobi, oʻrganmoq, olim.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>Перехо́д</b> va <b>перехо́да</b> — bu ikki soʻzmi yoki bitta?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Bitta soʻz</strong>, ikki
    shakl: И.п. va Р.п. Farq <b>окончание</b> da, demak yangi soʻz
    yasalmagan. <em>Перехо́д</em> va <em>перехо́дный</em> esa —
    ikki soʻz, chunki <em>-н-</em> suffiksi qoʻshilgan.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Toʻgʻri yozing: <b>без + поле́зный</b> · <b>раз + сказа́ть</b> ·
     <b>без + рабо́тный</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>бесполе́зный</strong>
    (п jarangsiz → с) ·
    <strong>рассказа́ть</strong> (с jarangsiz → с, ikkita с yonma-yon) ·
    <strong>безрабо́тный</strong> (р jarangli → з saqlanadi).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Siz bu soʻzni hech qachon koʻrmagansiz. Maʼnosini toping:<br>
     <b>снегохо́д</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>снег</strong> (qor) +
    <b>о</b> + <strong>ход</strong> (yurish) = <b>qorda yuradigan
    mashina</b>, snegoxod. Xuddi <em>парохо́д</em> va
    <em>вездехо́д</em> kabi qurilgan — lugʻat kerak boʻlmadi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>морфе́ма</b><span>soʻzning eng kichik maʼnoli boʻlagi</span></li>
  <li><b>ко́рень</b><span>oʻzak</span></li>
  <li><b>приста́вка</b><span>prefiks, oʻzakdan oldingi qism</span></li>
  <li><b>су́ффикс</b><span>oʻzakdan keyingi soʻz yasovchi qism</span></li>
  <li><b>оконча́ние</b><span>grammatik qoʻshimcha</span></li>
  <li><b>осно́ва</b><span>negiz — okonchaniyesiz qism</span></li>
  <li><b>однокоренны́е слова́</b><span>bir oʻzakli, qarindosh soʻzlar</span></li>
  <li><b>чередова́ние</b><span>tovush almashinuvi</span></li>
  <li><b>бе́глая гла́сная</b><span>«qochoq» unli: день → дня</span></li>
  <li><b>словообразова́ние</b><span>soʻz yasalishi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Rus soʻzi toʻrtta gʻishtdan: <b>приста́вка + ко́рень +
        су́ффикс + оконча́ние</b>.</li>
    <li>Oʻzakni topish uchun <b>qarindosh soʻzlarni yigʻing</b> va
        takrorlanayotgan qismni oling.</li>
    <li><b>Су́ффикс yangi soʻz yasaydi</b> (учи́ть → учи́тель),
        <b>окончание esa faqat shaklni</b> (учи́тель → учи́теля).</li>
    <li>Oʻzbekchada prefiks yoʻq — shuning uchun rus soʻzining
        <b>boshiga</b> alohida eʼtibor bering.</li>
    <li><b>Без- / из- / раз-</b> jarangsiz undosh oldida
        <b>бес- / ис- / рас-</b> boʻladi.</li>
    <li>Oʻzak oʻzgarsa — bu boshqa oʻzak emas, <b>чередова́ние</b>:
        писа́ть/пишу́, рука́/ру́чка, день/дня.</li>
    <li>Qurilishni bilsangiz, <b>notanish soʻzni lugʻatsiz</b> yechasiz.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-87: Suffikslar xaritasi: -ость, -ение, -тель, -ник, -щик, -ка, -ство",
        "category": "russian",
        "order": 87,
        "summary": (
            "Suffiks sizga ikki narsani birdan aytadi: soʻz nimani anglatishini "
            "va qaysi jinsda ekanini. -тель erkak, -ость ayol, -ение oʻrta."
        ),
        "stories": ["Профессии на -тель и -щик"],
        "content": """
<h2>PR-87: Suffikslar xaritasi: -ость, -ение, -тель, -ник, -щик, -ка, -ство</h2>

<p>PR-86 da soʻzni gʻishtlarga ajratdik. Endi eng foydali gʻishtni
alohida olamiz — <b>су́ффикс</b>.</p>

<p>Sababi bor. Soʻzning oxirgi uch-toʻrt harfi sizga <b>ikki</b> narsani
birdan aytadi: bu soʻz <b>nima haqida</b> (odammi, harakatmi,
xususiyatmi) va u <b>qaysi jinsda</b>. Ikkinchisi ayniqsa qimmatli —
PR-8 dan beri jins bilan kurashib kelyapsiz, va mana bu yerda u bepul
beriladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Yetti asosiy suffiksni <b>maʼnosi bilan</b> olasiz</li>
    <li>Suffiksga qarab <b>jinsni</b> aniqlaysiz — oʻylab oʻtirmasdan</li>
    <li><b>-тель / -щик / -ник</b> ni oʻzbekcha <b>«-chi»</b> ga bogʻlaysiz</li>
    <li><b>-ость / -ство</b> ni oʻzbekcha <b>«-lik»</b> ga bogʻlaysiz</li>
    <li><b>-ение</b> ni oʻzbekcha <b>«-(i)sh»</b> ga bogʻlaysiz</li>
    <li>Bir oʻzakdan butun soʻz oilasini yasashni mashq qilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--v">су́ффикс</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--s">maʼno</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">род</span>
</div>

<h3>1. Suffiks jinsni aytadi</h3>

<p>Bu darsning eng amaliy jumlasi. Yodlab qoʻying:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Suffiks</th><th>Jinsi</th><th>Misol</th><th>Tekshiruv</th></tr>
  <tr><td class="pr-stem">-тель</td><td class="pr-uz">мужско́й</td>
      <td class="pr-res">учи́тель</td><td class="pr-end">но́вый учи́тель</td></tr>
  <tr><td class="pr-stem">-ник</td><td class="pr-uz">мужско́й</td>
      <td class="pr-res">рабо́тник</td><td class="pr-end">но́вый рабо́тник</td></tr>
  <tr><td class="pr-stem">-щик / -чик</td><td class="pr-uz">мужско́й</td>
      <td class="pr-res">перево́дчик</td><td class="pr-end">но́вый перево́дчик</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">-ость</td><td class="pr-uz">же́нский</td>
      <td class="pr-res">но́вость</td><td class="pr-end">но́вая но́вость</td></tr>
  <tr><td class="pr-stem">-ка / -ница</td><td class="pr-uz">же́нский</td>
      <td class="pr-res">остано́вка</td><td class="pr-end">но́вая остано́вка</td></tr>
  <tr><td class="pr-stem">-ение / -ание</td><td class="pr-uz">сре́дний</td>
      <td class="pr-res">реше́ние</td><td class="pr-end">но́вое реше́ние</td></tr>
  <tr><td class="pr-stem">-ство</td><td class="pr-uz">сре́дний</td>
      <td class="pr-res">ка́чество</td><td class="pr-end">но́вое ка́чество</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">-ость — istisnosiz ayol jinsi</span>
Bu qoidada <b>bitta ham istisno yoʻq</b>, va bu kamdan-kam uchraydigan
baxt. <em>-ость</em> ga tugagan har qanday soʻz — <b>же́нский род</b>,
va <b>дверь</b> kabi <b>uchinchi turlanish</b>ga kiradi:<br><br>
но́вость → но́вост<b>и</b> (Р.п.) · о но́вост<b>и</b> (П.п.)<br>
ско́рость → ско́рост<b>и</b> · возмо́жность → возмо́жност<b>и</b><br><br>
Yumshoq belgiga aldanmang: <em>-ость</em> koʻrsangiz — ayol jinsi,
tamom. Shuning uchun <s>но́вый но́вость</s> emas, <b>но́вая
но́вость</b>.</div>

<h3>2. Odam yasovchilar: -тель · -щик · -ник</h3>

<div class="pe-call pe-uz"><span class="pe-call__t">Uchtasi ham oʻzbekcha «-chi»</span>
Oʻzbek tilida kasb yasash uchun bitta qoʻshimcha bor:
<b>-chi / -uvchi</b>.<br><br>
<em>ish → ish<b>chi</b></em> · <em>sot → sot<b>uvchi</b></em> ·
<em>oʻqit → oʻqit<b>uvchi</b></em> · <em>tarjima → tarjimon</em><br><br>
Ruschada bu bitta vazifa <b>uchta</b> suffiksga boʻlingan:<br><br>
<b>-тель</b> — koʻproq «yuqori» va kitobiy kasblar:
<em>учи́тель, писа́тель, води́тель, строи́тель</em><br>
<b>-щик / -чик</b> — koʻproq qoʻl mehnati va aniq ish:
<em>ка́менщик, сва́рщик, перево́дчик, лётчик</em><br>
<b>-ник</b> — ish bilan bogʻliq odam yoki narsa:
<em>учени́к, рабо́тник, помо́щник</em><br><br>
Qaysi soʻzga qaysi suffiks kelishi <b>yodlanadi</b> — qoidasi yoʻq.
Lekin uchtasini koʻrganingizda «bu odam» ekanini darrov bilasiz, va
amalda kerak boʻlgani shu.</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Qayerdan</th><th>Erkak</th><th>Ayol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">учи́ть</td><td class="pr-res">учи́тель</td>
      <td class="pr-res">учи́тельница</td><td class="pr-end">oʻqituvchi</td></tr>
  <tr><td class="pr-stem">писа́ть</td><td class="pr-res">писа́тель</td>
      <td class="pr-res">писа́тельница</td><td class="pr-end">yozuvchi</td></tr>
  <tr><td class="pr-stem">води́ть</td><td class="pr-res">води́тель</td>
      <td class="pr-res">—</td><td class="pr-end">haydovchi</td></tr>
  <tr><td class="pr-stem">стро́ить</td><td class="pr-res">строи́тель</td>
      <td class="pr-res">—</td><td class="pr-end">quruvchi</td></tr>
  <tr><td class="pr-stem">переводи́ть</td><td class="pr-res">перево́дчик</td>
      <td class="pr-res">перево́дчица</td><td class="pr-end">tarjimon</td></tr>
  <tr><td class="pr-stem">ка́мень</td><td class="pr-res">ка́менщик</td>
      <td class="pr-res">—</td><td class="pr-end">gʻishtchi, banno</td></tr>
  <tr><td class="pr-stem">помога́ть</td><td class="pr-res">помо́щник</td>
      <td class="pr-res">помо́щница</td><td class="pr-end">yordamchi</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">-щик yoki -чик? Oldingi harfga qarang</span>
Qoida bor va u qisqa. Oʻzak <b>д · т · з · с · ж</b> bilan tugasa —
<b>-чик</b>; boshqa hollarda — <b>-щик</b>:<br><br>
перево<b>д</b> → перево́д<b>чик</b> &nbsp;·&nbsp;
лё<b>т</b> → лёт<b>чик</b> &nbsp;·&nbsp;
расска<b>з</b> → расска́з<b>чик</b><br>
ка́мен<b>ь</b> → ка́мен<b>щик</b> &nbsp;·&nbsp;
свар<b>к</b>а → сва́р<b>щик</b> &nbsp;·&nbsp;
убор<b>к</b>а → убо́р<b>щик</b><br><br>
Shuning uchun <s>перево́дщик</s> — xato, <b>перево́дчик</b> toʻgʻri.
Talaffuzda ikkalasi deyarli bir xil eshitiladi, farq faqat yozuvda —
va imtihonda aynan shu soʻraladi.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ayol kasbining ikki yoʻli</span>
Rasmiy nutqda ayol haqida ham <b>erkak shakli</b> ishlatiladi:
<em>Мари́на Петро́вна — на́ш<b>а</b> но́в<b>ый</b> дире́ктор</em> —
ot erkak jinsida qoladi, lekin feʼl ayol jinsida boʻladi:
<em>дире́ктор сказа́л<b>а</b></em>.<br><br>
Kundalik nutqda esa <em>-ница / -ка / -чица</em> ishlatiladi:
<em>учи́тельница, перево́дчица, студе́нтка</em>. Ikkalasi ham
toʻgʻri; birinchisi rasmiyroq.</div>

<h3>3. -ость — sifatdan xususiyat</h3>

<div class="pe-call pe-uz"><span class="pe-call__t">-ость = oʻzbekcha «-lik»</span>
Bu — kursdagi eng toza mosliklardan biri. Ikkala til ham
<b>sifatdan</b> mavhum ot yasaydi va ikkalasi ham buni <b>bitta</b>
qoʻshimcha bilan qiladi:<br><br>
<em>yangi → yangi<b>lik</b></em> &nbsp;→&nbsp; но́вый → но́в<b>ость</b><br>
<em>yosh → yosh<b>lik</b></em> &nbsp;→&nbsp; молодо́й → мо́лод<b>ость</b><br>
<em>halol → halol<b>lik</b></em> &nbsp;→&nbsp; че́стный → че́стн<b>ость</b><br>
<em>qiyin → qiyin<b>chilik</b></em> &nbsp;→&nbsp; тру́дный → тру́дн<b>ость</b><br><br>
Yaʼni oʻzbekcha gapda «-lik» koʻrsangiz, ruschada katta ehtimol bilan
<b>-ость</b> kerak boʻladi.</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Sifat</th><th>Ot</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">но́вый</td><td class="pr-res">но́вость</td>
      <td class="pr-end">yangilik (xabar)</td></tr>
  <tr><td class="pr-stem">молодо́й</td><td class="pr-res">мо́лодость</td>
      <td class="pr-end">yoshlik</td></tr>
  <tr><td class="pr-stem">ско́рый</td><td class="pr-res">ско́рость</td>
      <td class="pr-end">tezlik</td></tr>
  <tr><td class="pr-stem">возмо́жный</td><td class="pr-res">возмо́жность</td>
      <td class="pr-end">imkoniyat</td></tr>
  <tr><td class="pr-stem">ва́жный</td><td class="pr-res">ва́жность</td>
      <td class="pr-end">muhimlik</td></tr>
  <tr><td class="pr-stem">сме́лый</td><td class="pr-res">сме́лость</td>
      <td class="pr-end">jasorat</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Но́вость — maʼnosi siljigan</span>
Soʻzma-soʻz <em>но́вость</em> «yangilik» degani, lekin bugun u koʻproq
<b>xabar</b> maʼnosida ishlatiladi:<br><br>
<em>У меня́ хоро́шая <b>но́вость</b>.</em> — Menda yaxshi xabar bor.<br>
<em>Я смотрю́ <b>но́вости</b>.</em> — Men yangiliklar koʻryapman.<br><br>
Oʻzbekchada ham xuddi shunday siljish boʻlgan: «yangiliklar» —
televizordagi xabarlar.</div>

<h3>4. -ение / -ание — feʼldan harakat</h3>

<div class="pe-call pe-uz"><span class="pe-call__t">-ение = oʻzbekcha «-(i)sh»</span>
Oʻzbekchada feʼldan ot yasash uchun <b>-(i)sh</b> qoʻshiladi:
<em>oʻqi → oʻqi<b>sh</b></em>, <em>bil → bili<b>sh</b></em>,
<em>yech → yechi<b>sh</b></em>.<br><br>
Ruschada bu vazifani <b>-ение / -ание</b> bajaradi:<br><br>
<em>чита́ть → чте́ние</em> — oʻqish<br>
<em>знать → зна́ние</em> — bilish, bilim<br>
<em>реши́ть → реше́ние</em> — yechish, yechim<br>
<em>дви́гаться → движе́ние</em> — harakat<br><br>
Hammasi <b>сре́дний род</b>, va urgʻu deyarli har doim
<b>-е́ние</b> ga tushadi.</div>

<div class="pe-ex">
  <p class="pe-ex__t">Gapda</p>
  <p class="pe-ex__ru">Э́то бы́л<span class="pr-end">о</span> пра́вильн<span class="pr-end">ое</span> реше́ние.</p>
  <p class="pe-ex__uz">Bu toʻgʻri qaror edi.</p>
  <p class="pe-ex__why">Uchala soʻz ham <b>сре́дний род</b> ga
     moslashgan, chunki <em>-ение</em> shuni talab qiladi.
     <s>Реше́ние был пра́вильный</s> — koʻp uchraydigan xato.</p>
</div>

<h3>5. -ство — jamlovchi va mavhum</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Qayerdan</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">де́тство</td><td class="pr-stem">де́ти</td>
      <td class="pr-end">bolalik</td></tr>
  <tr><td class="pr-res">бога́тство</td><td class="pr-stem">бога́тый</td>
      <td class="pr-end">boylik</td></tr>
  <tr><td class="pr-res">знако́мство</td><td class="pr-stem">знако́мый</td>
      <td class="pr-end">tanishuv</td></tr>
  <tr><td class="pr-res">ка́чество</td><td class="pr-stem">како́й</td>
      <td class="pr-end">sifat</td></tr>
  <tr><td class="pr-res">госуда́рство</td><td class="pr-stem">госуда́рь</td>
      <td class="pr-end">davlat</td></tr>
  <tr><td class="pr-res">большинство́</td><td class="pr-stem">бо́льший</td>
      <td class="pr-end">koʻpchilik</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">-ость va -ство ikkalasi ham «-lik»</span>
Oʻzbekcha «-lik» ruschada ikkiga boʻlingan:<br><br>
<b>-ость</b> — <em>sifatdan</em> xususiyat: <em>сме́лость</em>
(jasorat), <em>че́стность</em> (halollik)<br>
<b>-ство</b> — <em>holat yoki jamoa</em>: <em>де́тство</em>
(bolalik), <em>бога́тство</em> (boylik)<br><br>
Chegara doim ham aniq emas, shuning uchun bunday soʻzlarni juft-juft
yodlang: <em>бога́тый → бога́тство</em>, <em>сме́лый → сме́лость</em>.
Jinsi esa oʻz-oʻzidan chiqadi: <b>-ость</b> ayol,
<b>-ство</b> oʻrta.</div>

<h3>6. -ка — uch xil ish</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Vazifasi</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">ayol shakli</td><td class="pr-res">студе́нтка</td>
      <td class="pr-end">talaba qiz</td></tr>
  <tr><td class="pr-stem">harakat / natija</td><td class="pr-res">остано́вка</td>
      <td class="pr-end">bekat, toʻxtash</td></tr>
  <tr><td class="pr-stem">harakat / natija</td><td class="pr-res">оши́бка</td>
      <td class="pr-end">xato</td></tr>
  <tr><td class="pr-stem">narsa</td><td class="pr-res">откры́тка</td>
      <td class="pr-end">otkritka</td></tr>
  <tr><td class="pr-stem">kichraytirish</td><td class="pr-res">кни́жка</td>
      <td class="pr-end">kitobcha (PR-88)</td></tr>
</table></div>

<p><b>-ка</b> ning kichraytiruvchi vazifasi keyingi darsning butun
mavzusi. Hozircha bitta narsani bilib qoʻying: <em>-ка</em> har doim
<b>же́нский род</b>.</p>

<h3>7. Bir oʻzak — butun oila</h3>

<p>Endi PR-86 dagi oʻzakni bu darsdagi suffikslar bilan birlashtiring
va soʻz oilasi oʻzi qurilib chiqadi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Oʻzak</th><th>Odam</th><th>Harakat / xususiyat</th><th>Narsa</th></tr>
  <tr><td class="pr-stem">-уч-</td><td class="pr-res">учи́тель · учени́к</td>
      <td class="pr-end">обуче́ние</td><td class="pr-res">уче́бник</td></tr>
  <tr><td class="pr-stem">-пис-</td><td class="pr-res">писа́тель</td>
      <td class="pr-end">описа́ние</td><td class="pr-res">по́дпись</td></tr>
  <tr><td class="pr-stem">-строй-</td><td class="pr-res">строи́тель</td>
      <td class="pr-end">строи́тельство</td><td class="pr-res">стро́йка</td></tr>
  <tr><td class="pr-stem">-вод-</td><td class="pr-res">води́тель</td>
      <td class="pr-end">вожде́ние</td><td class="pr-res">про́вод</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>У меня́ хоро́ший но́вость.</s></p>
  <p class="pe-good">У меня́ хоро́ш<b>ая</b> но́вость — <em>-ость</em> har doim
     <b>же́нский род</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он рабо́тает перево́дщиком.</s></p>
  <p class="pe-good">…перево́д<b>чик</b>ом — oʻzak <em>д</em> bilan tugagan,
     demak <b>-чик</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Реше́ние был о́чень тру́дный.</s></p>
  <p class="pe-good">Реше́ни<b>е</b> бы́л<b>о</b> о́чень тру́дн<b>ым</b> —
     <em>-ение</em> <b>сре́дний род</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Моя́ учи́телька — Мари́на Петро́вна.</s></p>
  <p class="pe-good">Моя́ учи́тель<b>ница</b> — ayol shakli
     <em>-ница</em> bilan yasaladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>Ско́рость</b> qaysi jinsda? Sifatni qoʻying:
     <b>больш___ ско́рость</b>.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>больша́я ско́рость</strong> —
    <em>-ость</em> istisnosiz <b>же́нский род</b>. Р.п. da esa
    <em>большо́й ско́рости</em> boʻladi, chunki u <b>дверь</b> kabi
    uchinchi turlanishga kiradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Kasb yasang: <b>переводи́ть</b> · <b>стро́ить</b> · <b>убира́ть</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>перево́дчик</strong>
    (oʻzak <em>д</em> bilan → -чик) · <strong>строи́тель</strong> ·
    <strong>убо́рщик</strong> (oʻzak <em>д т з с ж</em> bilan
    tugamagan → -щик). Uchtasi ham oʻzbekchada bitta qoʻshimcha
    bilan: tarjimon, quruvchi, farrosh.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Sifatdan ot yasang: <b>возмо́жный</b> · <b>сме́лый</b> · <b>бога́тый</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>возмо́жность</strong>
    (imkoniyat, ж.р.) · <strong>сме́лость</strong> (jasorat, ж.р.) ·
    <strong>бога́тство</strong> (boylik, ср.р.). Uchtasi ham
    oʻzbekchada <em>-lik</em> bilan tugardi — ruschada esa ikki
    xil suffiks va ikki xil jins.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Feʼldan ot yasang va jinsini ayting:
     <b>реши́ть</b> · <b>знать</b> · <b>объясни́ть</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>реше́ние · зна́ние ·
    объясне́ние</strong> — uchtasi ham <b>сре́дний род</b>, chunki
    <em>-ение</em>. Sifat ham shunga moslashadi:
    <em>пра́вильн<b>ое</b> реше́ние</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Siz bu soʻzni koʻrmagansiz. Maʼnosini va jinsini toping:
     <b>гото́вность</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Oʻzak <em>гото́в-</em> («tayyor»,
    PR-73 dagi qisqa sifat) + <em>-ость</em>. Demak
    <strong>гото́вность</strong> = <b>tayyorlik</b>, va jinsi —
    <b>же́нский</b>. Suffiks ikkala javobni ham bergani shu.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>учи́тельница</b><span>oʻqituvchi ayol</span></li>
  <li><b>води́тель</b><span>haydovchi</span></li>
  <li><b>строи́тель</b><span>quruvchi</span></li>
  <li><b>перево́дчик</b><span>tarjimon</span></li>
  <li><b>ка́менщик</b><span>gʻishtchi, banno</span></li>
  <li><b>но́вость</b><span>yangilik, xabar</span></li>
  <li><b>возмо́жность</b><span>imkoniyat</span></li>
  <li><b>ско́рость</b><span>tezlik</span></li>
  <li><b>реше́ние</b><span>qaror, yechim</span></li>
  <li><b>бога́тство</b><span>boylik</span></li>
  <li><b>ка́чество</b><span>sifat</span></li>
  <li><b>остано́вка</b><span>bekat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Suffiks ikki narsani aytadi: <b>maʼno</b> va <b>jins</b>.</li>
    <li><b>-тель · -ник · -щик/-чик</b> → <b>м.р.</b>, odam.
        Oʻzbekcha «-chi».</li>
    <li><b>-ость</b> → <b>ж.р.</b>, istisnosiz, <em>дверь</em> kabi
        turlanadi. Oʻzbekcha «-lik».</li>
    <li><b>-ение / -ание</b> → <b>ср.р.</b>, feʼldan harakat.
        Oʻzbekcha «-(i)sh».</li>
    <li><b>-ство</b> → <b>ср.р.</b>, holat yoki jamoa. Bu ham «-lik».</li>
    <li><b>-ка / -ница</b> → <b>ж.р.</b></li>
    <li><b>-чик</b> — oʻzak <b>д т з с ж</b> bilan tugasa;
        boshqa hollarda <b>-щик</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-88: Kichraytiruvchi va erkalash shakllari: домик, сынок, Машенька, водичка",
        "category": "russian",
        "order": 88,
        "summary": (
            "«До́мик» kichik uy, lekin «ма́мочка» kichik ona emas. Ruschada "
            "kichraytirish va erkalash bitta shaklda — oʻzbekchada esa ikkita."
        ),
        "stories": ["Бабушкины слова"],
        "content": """
<h2>PR-88: Kichraytiruvchi va erkalash shakllari: домик, сынок, Машенька, водичка</h2>

<p>Rus doʻstingiz sizga <b>«Ко́фейку?»</b> deydi. Lugʻatni ochasiz —
bunday soʻz yoʻq. Bor narsa <b>ко́фе</b>, va unga qoʻshilgan bir
narsa: <b>iliqlik</b>.</p>

<p>Rus tili bu ishni juda koʻp qiladi. Kundalik nutqda deyarli har
uchinchi ot kichraytirilgan shaklda keladi. Buni bilmasangiz, matnni
tushunasiz-u, <b>ohangni</b> tushunmaysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Asosiy kichraytiruvchi suffikslarni olasiz: <b>-ик · -ок · -чик · -очка · -ушка</b></li>
    <li><b>Kichraytirish</b> va <b>erkalash</b> ni bir-biridan ajratasiz</li>
    <li>Rus ismlarining <b>uch pogʻonasini</b> bilib olasiz: Мари́я → Ма́ша → Ма́шенька</li>
    <li><b>-ище</b> bilan kattalashtirasiz: до́мик ↔ доми́ще</li>
    <li>«Одну́ мину́точку!» kabi <b>muloyimlik</b> qurilishlarini ishlatasiz</li>
    <li>Bu shakllarni <b>qayerda ishlatmaslik</b> kerakligini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">ot</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">-ик / -ок / -очка / -ушка</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">kichik <b>yoki</b> qadrli</span>
</div>

<h3>1. Bitta shakl — ikki maʼno</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">KICHRAYTIRISH — oʻlcham</p>
    <p><em>дом → до́мик</em></p>
    <p>Haqiqatan ham kichik uy. Oʻlcham haqida gap ketyapti.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ERKALASH — munosabat</p>
    <p><em>ма́ма → ма́мочка</em></p>
    <p>Ona kichraymaydi. Bu — mehr, «onajon».</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekchada bu ikki maʼno ikki xil qoʻshimchada</span>
Mana bu joyda oʻzbek oʻquvchi eng koʻp adashadi, chunki oʻzbek tili bu
ikki ishni <b>ajratib</b> qiladi:<br><br>
<b>-cha</b> — kichraytiradi: <em>uy<b>cha</b>, kitob<b>cha</b>,
qoshiq<b>cha</b></em><br>
<b>-jon / -xon</b> — erkalaydi: <em>ona<b>jon</b>, aka<b>jon</b>,
Dilnoza<b>xon</b></em><br><br>
Ruschada esa <b>bitta</b> shakl ikkala vazifani ham bajaradi:<br><br>
<em>до́мик</em> = uy<b>cha</b> (kichik uy)<br>
<em>ма́мочка</em> = ona<b>jon</b> (mehr, kichiklik emas)<br>
<em>сыно́к</em> = oʻgʻl<b>im</b> (yosh muhim emas — ellik yoshli
odamga ham aytiladi)<br><br>
Qaysi maʼno ekanini <b>faqat kontekst</b> koʻrsatadi. Shuning uchun
<em>ма́мочка</em> ni «kichkina ona» deb tarjima qilmang — bu xato
emas, bu kulgili.</div>

<h3>2. Asosiy suffikslar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Suffiks</th><th>Asl soʻz</th><th>Shakl</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">-ик</td><td class="pr-res">дом</td>
      <td class="pr-res">до́мик</td><td class="pr-end">kichik uy</td></tr>
  <tr><td class="pr-stem">-ик</td><td class="pr-res">нос</td>
      <td class="pr-res">но́сик</td><td class="pr-end">kichkina burun</td></tr>
  <tr><td class="pr-stem">-ок / -ёк</td><td class="pr-res">сын</td>
      <td class="pr-res">сыно́к</td><td class="pr-end">oʻgʻlim (mehr)</td></tr>
  <tr><td class="pr-stem">-ок / -ёк</td><td class="pr-res">чай</td>
      <td class="pr-res">чаёк</td><td class="pr-end">choygina</td></tr>
  <tr><td class="pr-stem">-чик</td><td class="pr-res">стака́н</td>
      <td class="pr-res">стака́нчик</td><td class="pr-end">stakancha</td></tr>
  <tr><td class="pr-stem">-очка / -ечка</td><td class="pr-res">ма́ма</td>
      <td class="pr-res">ма́мочка</td><td class="pr-end">onajon</td></tr>
  <tr><td class="pr-stem">-очка / -ечка</td><td class="pr-res">мину́та</td>
      <td class="pr-res">мину́точка</td><td class="pr-end">daqiqagina</td></tr>
  <tr><td class="pr-stem">-ушка / -юшка</td><td class="pr-res">хлеб</td>
      <td class="pr-res">хле́бушек</td><td class="pr-end">nongina (mehr)</td></tr>
  <tr><td class="pr-stem">-ышко</td><td class="pr-res">со́лнце</td>
      <td class="pr-res">со́лнышко</td><td class="pr-end">quyoshginam</td></tr>
  <tr><td class="pr-stem">-ичка / -ка</td><td class="pr-res">вода́</td>
      <td class="pr-res">води́чка</td><td class="pr-end">suvcha</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">PR-86 dagi чередова́ние qaytib keldi</span>
Suffiks qoʻshilganda oʻzakning oxirgi undoshi almashadi — bu oʻsha
qoida:<br><br>
<em>ру<b>к</b>а → ру́<b>ч</b>ка</em> (к/ч) &nbsp;·&nbsp;
<em>но<b>г</b>а → но́<b>ж</b>ка</em> (г/ж)<br>
<em>кни<b>г</b>а → кни́<b>ж</b>ка</em> (г/ж) &nbsp;·&nbsp;
<em>сне<b>г</b> → сне́<b>ж</b>ок</em> (г/ж)<br><br>
Yaʼni <em>кни́жка</em> da <b>ж</b> paydo boʻlgani tasodif emas.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Baʼzilari mustaqil soʻzga aylangan</span>
Ayrim kichraytirilgan shakllar oʻz maʼnosini olib, lugʻatda alohida
soʻz boʻlib qolgan:<br><br>
<b>ру́чка</b> — «kichik qoʻl» emas, <b>ruchka</b> yoki
<b>eshik dastasi</b><br>
<b>кни́жка</b> — koʻpincha shunchaki «kitob», norasmiy ohangda<br>
<b>ба́бушка</b> — buvi (bu <em>ба́ба</em> ning kichraytirilgani
edi, endi asosiy soʻz)<br>
<b>де́вочка</b> — qizcha; <b>ма́льчик</b> — oʻgʻil bola<br><br>
Bularni endi kichraytirilgan deb hisoblamang — ular oddiy soʻz.</div>

<h3>3. Ismlar — uch pogʻona</h3>

<p>Rus ismi kamdan-kam toʻliq shaklda ishlatiladi. Har bir ismning
kamida uch bosqichi bor:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Toʻliq — rasmiy</th><th>Qisqa — kundalik</th><th>Erkalash — yaqin</th><th>Familyar</th></tr>
  <tr><td class="pr-stem">Мари́я</td><td class="pr-res">Ма́ша</td>
      <td class="pr-end">Ма́шенька</td><td class="pr-uz">Ма́шка</td></tr>
  <tr><td class="pr-stem">Алекса́ндр(а)</td><td class="pr-res">Са́ша</td>
      <td class="pr-end">Са́шенька</td><td class="pr-uz">Са́шка</td></tr>
  <tr><td class="pr-stem">Дми́трий</td><td class="pr-res">Ди́ма</td>
      <td class="pr-end">Ди́мочка</td><td class="pr-uz">Ди́мка</td></tr>
  <tr><td class="pr-stem">Ива́н</td><td class="pr-res">Ва́ня</td>
      <td class="pr-end">Ва́нечка</td><td class="pr-uz">Ва́нька</td></tr>
  <tr><td class="pr-stem">Екатери́на</td><td class="pr-res">Ка́тя</td>
      <td class="pr-end">Ка́тенька</td><td class="pr-uz">Ка́тька</td></tr>
  <tr><td class="pr-stem">Серге́й</td><td class="pr-res">Серёжа</td>
      <td class="pr-end">Серёженька</td><td class="pr-uz">Серёжка</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">-ка ismda — ehtiyot boʻling</span>
<b>Ма́шка</b>, <b>Ва́нька</b>, <b>Ди́мка</b> — bu shakllar juda yaqin
doʻstlar orasida yoki bolalarga nisbatan normal, lekin
<b>notanish odamga</b> yoki <b>kattaga</b> aytilsa <b>qoʻpol</b>
eshitiladi.<br><br>
Xavfsiz yoʻl: <b>qisqa shakl</b>ni ishlating (Ма́ша, Ди́ма) yoki
odam oʻzini qanday tanishtirgan boʻlsa, shunday chaqiring. Rasmiy
holatda esa — <b>ism + otasining ismi</b>: <em>Мари́я
Петро́вна</em>.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekchada ham shu tizim bor</span>
Bu sizga notanish emas. Oʻzbek tilida ham ism qisqaradi va
erkalanadi:<br><br>
<em>Dilnoza → Dilya → Dilnoza<b>xon</b></em><br>
<em>Jasur → Jasur<b>bek</b> → Jasur<b>jon</b></em><br>
<em>Sherbek → Sher → Sher<b>jon</b></em><br><br>
Ruschada <em>-енька / -очка</em> aynan shu <em>-jon</em> ning
oʻrnida turadi. Va oʻzbekchada ham qaysi shaklni kimga aytish
mumkinligini his qilasiz — ruschada ham xuddi shu his kerak.</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Са́ша — ikki jins uchun bitta ism</span>
<b>Алекса́ндр</b> (erkak) va <b>Алекса́ндра</b> (ayol) — ikkalasining
qisqa shakli <b>Са́ша</b>. Shuning uchun «Са́ша пришёл» va «Са́ша
пришла́» — ikkalasi ham toʻgʻri, feʼl kimligini koʻrsatadi.<br><br>
Xuddi shunday: <b>Ва́ля</b> (Валенти́н / Валенти́на),
<b>Же́ня</b> (Евге́ний / Евге́ния).</div>

<h3>4. Teskari tomon: -ище va -ишко</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">-ИЩЕ — kattalashtirish</p>
    <p><em>дом → доми́ще</em> · <em>рука́ → ручи́ща</em></p>
    <p>Juda katta, hayratlanish bilan. <em>Каки́е глази́щи!</em> —
       Qanday katta koʻzlar!</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">-ИШКО — kamsitish</p>
    <p><em>дом → доми́шко</em> · <em>го́род → городи́шко</em></p>
    <p>Kichik va ahamiyatsiz. Ohangi <b>salbiy</b> — ehtiyot
       boʻling.</p>
  </div>
</div>

<h3>5. Muloyimlik uchun — eng foydali qismi</h3>

<p>Mana bu yerda kichraytirish grammatikadan chiqib, <b>odob</b>ga
aylanadi. Soʻrov kichraytirilgan shaklda yumshoqroq eshitiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__t">Kundalik hayotda</p>
  <p class="pe-ex__ru">Одну́ <b>мину́точку</b>, пожа́луйста!</p>
  <p class="pe-ex__uz">Bir daqiqagina, iltimos! — «мину́ту» dan muloyimroq.</p>
  <p class="pe-ex__ru"><b>Секу́ндочку</b>, я сейча́с найду́.</p>
  <p class="pe-ex__uz">Bir soniyagina, hozir topaman.</p>
  <p class="pe-ex__ru">Дилно́за, <b>чайку́</b>?</p>
  <p class="pe-ex__uz">Dilnoza, choy ichasizmi? — juda iliq taklif.</p>
  <p class="pe-ex__why">Ohang kichraytirishdan chiqadi:
     «мину́ту» — buyruq, «мину́точку» — iltimos.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Qayerda ishlatilmaydi</span>
Kichraytirish — <b>ogʻzaki va oilaviy</b> nutqning belgisi. Bu
joylarda u <b>butunlay oʻrinsiz</b>:<br><br>
✗ ariza va rasmiy xat — <s>Прошу́ дать о́тпуск на неде́льку</s> →
<b>на неде́лю</b><br>
✗ imtihon javobi va ilmiy matn<br>
✗ ish xati va rezyume<br>
✗ yangilik xabari<br><br>
PR-90 da rasmiy va norasmiy uslubni yonma-yon koʻramiz —
kichraytirish ikki uslubni ajratadigan eng aniq belgilardan biri.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>«Ма́мочка» — bu «kichkina ona».</s></p>
  <p class="pe-good">Bu <b>«onajon»</b>. Shakl kichraytiruvchi, maʼnosi esa
     mehr — oʻlchamga hech qanday aloqasi yoʻq.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Здра́вствуйте, Ма́шка!</s></p>
  <p class="pe-good">Здра́вствуйте, <b>Мари́я Петро́вна</b>! — <em>-ка</em>
     notanish odamga qoʻpol eshitiladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Прошу́ предоста́вить о́тпуск на неде́льку.</s></p>
  <p class="pe-good">…на <b>неде́лю</b> — arizada kichraytirish boʻlmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Дай мне ру́чку — kichik qoʻlingizni bering.</s></p>
  <p class="pe-good"><b>Ру́чка</b> bu yerda <b>ruchka</b> (yozadigan).
     Baʼzi shakllar mustaqil soʻzga aylangan.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Buvi nevarasiga <b>«Сыно́к, иди́ сюда́»</b> dedi. Nevara necha
     yoshda boʻlishi mumkin?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Har qanday yoshda.</strong>
    <em>Сыно́к</em> — «kichik oʻgʻil» emas, <b>iliq murojaat</b>:
    «oʻgʻlim». Ellik yoshli erkakka ham aytilishi mumkin. Xuddi
    oʻzbekcha «bolam» kabi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>Со́лнце</b> dan erkalash shaklini yasang va u odamga nisbatan
     nima anglatishini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>со́лнышко</strong>
    (<em>-ышко</em>). Odamga aytilganda — juda iliq murojaat:
    <em>Со́лнышко моё!</em> «Quyoshginam», «jonginam». Ona bolasiga,
    er xotiniga aytadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>Ма́шенька</b> qaysi ismdan? Oradagi bosqichni ham ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Мари́я → Ма́ша →
    Ма́шенька</strong>. Toʻliq shakl rasmiy, <em>Ма́ша</em>
    kundalik, <em>Ма́шенька</em> yaqin va mehrli.
    <em>Ма́шка</em> esa toʻrtinchi bosqich — faqat juda yaqin
    doʻstlar orasida.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nega <b>кни́га → кни́жка</b> da <b>ж</b> paydo boʻldi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Чередова́ние г/ж</strong> —
    PR-86 dagi qoida. Suffiks oldida oʻzakning oxirgi undoshi
    almashadi: <em>кни́га → кни́жка</em>, <em>нога́ → но́жка</em>,
    <em>рука́ → ру́чка</em> (к/ч).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring — muloyim shaklda.<br>
     <b>Bir daqiqagina kuting, iltimos.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Подожди́те одну́
    мину́точку, пожа́луйста.</strong> <em>Мину́ту</em> ham toʻgʻri,
    lekin <em>мину́точку</em> aynan «daqiqa<b>gina</b>» ohangini
    beradi. <em>Секу́ндочку</em> ham xuddi shunday
    ishlatiladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>уменьши́тельный су́ффикс</b><span>kichraytiruvchi qoʻshimcha</span></li>
  <li><b>ла́сково</b><span>erkalab, mehr bilan</span></li>
  <li><b>до́мик</b><span>uycha</span></li>
  <li><b>сыно́к</b><span>oʻgʻlim (iliq murojaat)</span></li>
  <li><b>ма́мочка</b><span>onajon</span></li>
  <li><b>води́чка</b><span>suvcha</span></li>
  <li><b>со́лнышко</b><span>quyoshginam</span></li>
  <li><b>мину́точку</b><span>bir daqiqagina</span></li>
  <li><b>хле́бушек</b><span>nongina</span></li>
  <li><b>доми́ще</b><span>ulkan uy</span></li>
  <li><b>доми́шко</b><span>xarob uycha (salbiy ohang)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Bitta shakl <b>ikki maʼno</b> beradi: kichiklik yoki mehr.
        Qaysi biri ekanini kontekst aytadi.</li>
    <li>Oʻzbekchada bular ikki xil: <b>-cha</b> kichraytiradi,
        <b>-jon</b> erkalaydi. Ruschada — bitta shakl.</li>
    <li>Asosiy suffikslar: <b>-ик · -ок/-ёк · -чик · -очка/-ечка ·
        -ушка · -ышко</b>.</li>
    <li>Ismlar uch pogʻonali: <b>Мари́я → Ма́ша → Ма́шенька</b>.
        <b>-ка</b> (Ма́шка) faqat juda yaqinlar orasida.</li>
    <li><b>-ище</b> kattalashtiradi, <b>-ишко</b> kamsitadi.</li>
    <li><b>«Одну́ мину́точку!»</b> — kichraytirish bu yerda
        muloyimlik vositasi.</li>
    <li>Rasmiy matnda, arizada va imtihonda — <b>hech qachon</b>.</li>
  </ul>
</div>
""",
    },
]
