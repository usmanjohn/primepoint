# -*- coding: utf-8 -*-
"""Prime Russian — Block H: maqol, juftlik va tinish belgisi (95–97).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-95 — maqollar. PR-94 iboralar haqida edi (gap ICHIDAGI birikma),
bu dars maqollar haqida (BUTUN gap + saboq). Darsning gavhari —
«Язы́к до Ки́ева доведёт» ↔ «Soʻrab-soʻrab Makkani topibdi»: ikkala
maqol ham uzoq muqaddas shaharni tilga oladi va ikkalasi ham
«soʻrasang yetasan» deydi. «Семь раз отмерь» ↔ «Yetti oʻlchab, bir
kes» esa raqamigacha bir xil.
PR-96 — adashtiriladigan juftlar. Eng katta lever shu yerda:
НАДЕ́ТЬ / ОДЕ́ТЬ farqi oʻzbekchada KIYMOQ / KIYDIRMOQ bilan aynan
beriladi — oʻzbek tilidagi orttirma nisbat (-dir) rus tilidagi ikki
alohida feʼlning oʻrnini bosadi. Oʻzbek oʻquvchi bu farqni ingliz
tilida soʻzlashuvchidan koʻra osonroq tushunadi.
PR-97 — punktuatsiya. Oʻzbek tinish belgilari tizimi rus tilidan
olingan, shuning uchun qoidalarning koʻpi ustma-ust tushadi: tire
(«Toshkent — poytaxt» / «Москва́ — столи́ца»), undalma va kirish
soʻzlardagi vergul. Bu darsni oson qiladi va buni aytish kerak.
Asosiy yangi qoida: ergash gap oldidan vergul RUS TILIDA HAR DOIM
qoʻyiladi — который, что, чтобы, потому что oldida istisno yoʻq.

⚠️ Oʻqish matnlarida URGʻU BELGISI YOʻQ (2026-08-24) — darsliklar saqlaydi.

Mashqlar:        practice/management/commands/_practice_pr_95_97.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_95_97.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_95_97.py --author=prime
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
        "title": "PR-95: Maqollar va matallar, oʻzbekcha muqobillari bilan",
        "category": "russian",
        "order": 95,
        "summary": (
            "«Yetti oʻlchab, bir kes» ruschada ham yetti marta oʻlchaydi. "
            "Maqollar, ularning oʻzbekcha juftlari va yarmini aytish odati."
        ),
        "stories": ["Письмо из кишлака"],
        "content": """
<h2>PR-95: Maqollar va matallar, oʻzbekcha muqobillari bilan</h2>

<p>Rus tilida <b>«Язы́к до Ки́ева доведёт»</b> degan maqol bor —
«til Kiyevgacha yetkazadi», yaʼni soʻrab-soʻrab istagan joyingizga
borasiz.</p>

<p>Endi oʻzbekcha maqolni eslang: <b>«Soʻrab-soʻrab Makkani
topibdi.»</b></p>

<p>Ikkala maqol ham bitta narsani aytadi va ikkalasi ham buni
<b>uzoqdagi muqaddas shahar</b> orqali aytadi. Faqat shahar boshqa.</p>

<p>Bu darsda ana shunday juftlarni yigʻamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Посло́вица</b> va <b>погово́рка</b> ni ajratasiz</li>
    <li>Oʻzbekchaga <b>aynan</b> tushadigan maqollarni olasiz</li>
    <li>Obraz boshqa, maʼno bir xil boʻlgan juftlarni koʻrasiz</li>
    <li>Maqolning <b>yarmini aytish</b> odatini oʻrganasiz</li>
    <li>Maqolni <b>qayerda ishlatmaslik</b> kerakligini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Farqi</span>
  <span class="pe-chip pe-chip--s">посло́вица = butun gap + saboq</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">погово́рка = gapning boʻlagi</span>
</div>

<h3>1. Uch xil turgʻun birikma</h3>

<p>PR-94 da <b>iboralar</b> bilan tanishdik. Endi ularning yoniga ikki
qoʻshni qoʻyamiz:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Nima</th><th>Qanday</th><th>Misol</th></tr>
  <tr><td class="pr-stem">фразеологи́зм</td><td class="pr-uz">gap <b>ichidagi</b> birikma</td>
      <td class="pr-res">бить баклу́ши</td></tr>
  <tr><td class="pr-stem">погово́рка</td><td class="pr-uz">tugallanmagan obraz, saboqsiz</td>
      <td class="pr-res">ни ры́ба ни мя́со</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">посло́вица</td>
      <td class="pr-uz"><b>butun gap</b>, ichida saboq bor</td>
      <td class="pr-res">Семь раз отме́рь, оди́н раз отре́жь.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Oson tekshiruv</span>
Birikmani <b>alohida</b> yozib koʻring.<br><br>
Toʻliq gap chiqdimi va undan <b>maslahat</b> oʻqilyaptimi — bu
<b>посло́вица</b>.<br>
Gapga qoʻshib ishlatish kerakmi — bu <b>погово́рка</b> yoki
<b>фразеологи́зм</b>.<br><br>
<em>Семь раз отме́рь, оди́н раз отре́жь</em> — oʻzi turadi, maslahat
beradi → посло́вица.<br>
<em>Бить баклу́ши</em> — oʻzi turmaydi, gapga kerak → фразеологи́зм.</div>

<h3>2. Aynan mos tushadiganlar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Oʻzbekcha</th><th>Maʼnosi</th></tr>
  <tr class="pr-case__on"><td class="pr-res">Семь раз отме́рь, оди́н раз отре́жь.</td>
      <td class="pr-end">Yetti oʻlchab, bir kes.</td>
      <td class="pr-uz">Qilishdan oldin oʻylab koʻr.</td></tr>
  <tr class="pr-case__on"><td class="pr-res">Что посе́ешь, то и пожнёшь.</td>
      <td class="pr-end">Nima eksang, shuni oʻrasan.</td>
      <td class="pr-uz">Qilmishingga yarasha topasan.</td></tr>
  <tr class="pr-case__on"><td class="pr-res">Не всё то зо́лото, что блести́т.</td>
      <td class="pr-end">Yaltiragan hamma narsa oltin emas.</td>
      <td class="pr-uz">Tashqi koʻrinishga ishonma.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">«Yetti» ikkala tilda ham yetti</span>
Birinchi qatorga diqqat bilan qarang. Ikkala maqol ham:<br><br>
— <b>oʻlchash</b> va <b>kesish</b> haqida gapiradi,<br>
— <b>yetti</b> raqamini ishlatadi,<br>
— <b>bir</b> marta kesishni aytadi.<br><br>
Yaʼni bu shunchaki maʼnodosh maqol emas — ular <b>bir xil</b>.
Bunday moslik tasodif emas: har ikkala xalq ham asrlar davomida
mato va yogʻoch kesgan, va xato qilish ikkalasiga ham bir xil
qimmatga tushgan.<br><br>
Bunday maqolni <b>tarjima qilish shart emas</b> — juftini aytsangiz
kifoya.</div>

<h3>3. Obraz boshqa, maʼno bir xil</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Soʻzma-soʻz</th><th>Oʻzbekcha jufti</th></tr>
  <tr><td class="pr-res">Язы́к до Ки́ева доведёт.</td>
      <td class="pr-stem">til Kiyevgacha yetkazadi</td>
      <td class="pr-end">Soʻrab-soʻrab Makkani topibdi.</td></tr>
  <tr><td class="pr-res">Не име́й сто рубле́й, а име́й сто друзе́й.</td>
      <td class="pr-stem">yuz rubling emas, yuz doʻsting boʻlsin</td>
      <td class="pr-end">Yuz soʻming boʻlguncha, yuz doʻsting boʻlsin.</td></tr>
  <tr><td class="pr-res">В гостя́х хорошо́, а до́ма лу́чше.</td>
      <td class="pr-stem">mehmonda yaxshi, uyda yaxshiroq</td>
      <td class="pr-end">Oʻz uying — oʻlan toʻshaging.</td></tr>
  <tr><td class="pr-res">Терпе́ние и труд всё перетру́т.</td>
      <td class="pr-stem">sabr va mehnat hammasini yengadi</td>
      <td class="pr-end">Sabrning tagi sariq oltin.</td></tr>
  <tr><td class="pr-res">Друг познаётся в беде́.</td>
      <td class="pr-stem">doʻst kulfatda bilinadi</td>
      <td class="pr-end">Doʻst kulfatda bilinadi.</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida: tarjima qilmang, juftini toping</span>
Bu — PR-94 dagi qoidaning oʻzi, faqat maqollarga
tegishlisi.<br><br>
<em>Язы́к до Ки́ева доведёт</em> ni «til Kiyevgacha olib boradi» deb
tarjima qilsangiz, oʻzbek quloqqa hech narsa aytmaydi. Lekin
«Soʻrab-soʻrab Makkani topibdi» desangiz — hamma darrov
tushunadi.<br><br>
Shuning uchun maqollarni <b>juft-juft</b> yodlang: chapda ruschasi,
oʻngda oʻzbekchasi.</div>

<h3>4. Yana beshta kerakli maqol</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Maqol</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Без труда́ не вы́тащишь и ры́бку из пруда́.</td>
      <td class="pr-uz">Mehnatsiz baliqni ham tutolmaysan — mehnatning tagi rohat.</td></tr>
  <tr><td class="pr-res">Ти́ше е́дешь — да́льше бу́дешь.</td>
      <td class="pr-uz">Sekin borsang, uzoqqa borasan — shoshilma.</td></tr>
  <tr><td class="pr-res">Ум хорошо́, а два лу́чше.</td>
      <td class="pr-uz">Bir aql yaxshi, ikkitasi yaxshiroq — maslahatlash.</td></tr>
  <tr><td class="pr-res">Век живи́ — век учи́сь.</td>
      <td class="pr-uz">Umr boʻyi yasha — umr boʻyi oʻrgan.</td></tr>
  <tr><td class="pr-res">Пе́рвый блин ко́мом.</td>
      <td class="pr-uz">Birinchi urinish har doim ham chiqmaydi.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ikkitasida tire turibdi</span>
<em>Ти́ше е́дешь <b>—</b> да́льше бу́дешь</em> va
<em>Век живи́ <b>—</b> век учи́сь</em> da <b>тире́</b> bor.<br><br>
Bu tasodif emas: maqollarda gap qismlari bogʻlovchisiz turadi, va
oʻsha yerga tire qoʻyiladi. Keyingi darsdan bittasi — PR-97 —
butunlay shu belgiga bagʻishlangan.</div>

<h3>5. Yarmini aytish odati</h3>

<p>Rus nutqida maqol koʻpincha <b>toʻliq aytilmaydi</b>. Gapiruvchi
birinchi yarmini aytadi va <b>toʻxtaydi</b> — tinglovchi qolganini
oʻzi biladi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Yarim maqol — toʻliq maʼno</p>
  <p class="pe-ex__ru">— Он купи́л маши́ну о́чень дёшево.<br>
     — Ну, зна́ешь… <b>не всё то зо́лото…</b></p>
  <p class="pe-ex__uz">— Mashinani juda arzonga oldi. — Hm, bilasanmi…
     yaltiragan hamma narsa oltin emas-da.</p>
  <p class="pe-ex__why">Ikkinchi qismi (<em>что блести́т</em>) aytilmadi,
     lekin hamma eshitdi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekchada ham shunday qilinadi</span>
Bu odat sizga tanish: oʻzbekchada ham
<em>«Yetti oʻlchab…»</em> deb toʻxtash mumkin — davomi
aytilmasa ham tushuniladi.<br><br>
Lekin bir shart bor: maqolni <b>toʻliq bilish</b> kerak.
Yarmini aytish uchun avval butunini yodlang — aks holda notoʻgʻri
joyda toʻxtab qolasiz.</div>

<h3>6. Qayerda ishlatiladi</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">✓ MUMKIN</p>
    <p>Ogʻzaki suhbat · maktub · insho xulosasi · maʼruza ·
       hikoya · maslahat</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">✗ MUMKIN EMAS</p>
    <p>Ariza · rasmiy xat · hujjat · ilmiy matn · rezyume ·
       yangilik xabari</p>
  </div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Insho uchun foydali</span>
Rus tilida insho yozganda maqol <b>xulosani</b> mustahkamlash uchun
juda qulay:<br><br>
<em>…Поэ́тому не сто́ит спеши́ть с реше́нием. Неда́ром говоря́т:
<b>семь раз отме́рь, оди́н раз отре́жь</b>.</em><br><br>
<b>Неда́ром говоря́т…</b> va <b>Как говори́тся…</b> — maqolni
kiritadigan ikki tayyor qolip. Ularni yodlab qoʻying.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Язы́к до Ки́ева доведёт</s> — «til Kiyevgacha olib
     boradi» deb tarjima qilish</p>
  <p class="pe-good">Juftini ayting: <b>Soʻrab-soʻrab Makkani topibdi</b>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Семь раз отме́рить, оди́н раз отре́зать.</s></p>
  <p class="pe-good">Семь раз <b>отме́рь</b>, оди́н раз <b>отре́жь</b> —
     maqol shakli qotib qolgan (buyruq mayli, PR-59).</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Прошу́ рассмотре́ть моё заявле́ние. Как говори́тся,
     семь раз отме́рь.</s></p>
  <p class="pe-good">Arizada maqol boʻlmaydi — rasmiy hujjatda uslub
     buziladi (PR-91).</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>«Бить баклу́ши» — bu посло́вица.</s></p>
  <p class="pe-good">Bu <b>фразеологи́зм</b>: oʻzi turmaydi va saboq
     bermaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>«Семь раз отме́рь, оди́н раз отре́жь»</b> ning oʻzbekcha jufti
     nima va nimasi bilan gʻalati?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>«Yetti oʻlchab, bir
    kes.»</strong> Gʻalati tomoni — ikkala maqol ham <b>oʻsha
    raqamlarni</b> ishlatadi: yetti va bir. Bu maʼnodosh maqol emas,
    bu <b>bir xil</b> maqol.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu ikkitasidan qaysi biri <b>посло́вица</b>, qaysi biri
     <b>фразеологи́зм</b>?<br>
     <b>ни ры́ба ни мя́со</b> · <b>Век живи́ — век учи́сь.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><em>Ни ры́ба ни мя́со</em> —
    <strong>погово́рка</strong>: oʻzi turmaydi, saboq bermaydi
    («na u, na bu»). <em>Век живи́ — век учи́сь</em> —
    <strong>посло́вица</strong>: toʻliq gap va maslahat.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Maqolni toʻldiring va oʻzbekchasini ayting.<br>
     <b>Не име́й сто рубле́й, а ___ .</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>…а име́й сто
    друзе́й.</strong> Oʻzbekchasi: <b>«Yuz soʻming boʻlguncha, yuz
    doʻsting boʻlsin.»</b> Obraz deyarli bir xil — faqat pul
    birligi boshqa.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Suhbatdosh dedi: <b>«Ну, пе́рвый блин…»</b> U nima demoqchi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Toʻliq maqol —
    <strong>«Пе́рвый блин ко́мом»</strong>, yaʼni «birinchi urinish
    chiqmasligi normal». U <b>yarmini</b> aytdi va toʻxtadi —
    bu rus nutqining odatiy usuli. Maʼno esa toʻliq
    yetkazildi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Insho xulosasini maqol bilan tugating.<br>
     <b>Fikr: shoshilib qaror qabul qilmaslik kerak.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Masalan: <strong>Поэ́тому не
    сто́ит спеши́ть. Неда́ром говоря́т: семь раз отме́рь, оди́н раз
    отре́жь.</strong><br><em>Ти́ше е́дешь — да́льше бу́дешь</em> ham
    toʻgʻri kelardi. Kiritish qoliplari: <b>Неда́ром говоря́т…</b> ·
    <b>Как говори́тся…</b></p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>посло́вица</b><span>maqol — toʻliq gap, saboq bilan</span></li>
  <li><b>погово́рка</b><span>matal — tugallanmagan obraz</span></li>
  <li><b>Как говори́тся…</b><span>aytishlaricha…</span></li>
  <li><b>Неда́ром говоря́т…</b><span>bejizga aytishmagan…</span></li>
  <li><b>Семь раз отме́рь…</b><span>Yetti oʻlchab, bir kes</span></li>
  <li><b>Что посе́ешь, то и пожнёшь.</b><span>Nima eksang, shuni oʻrasan</span></li>
  <li><b>Язы́к до Ки́ева доведёт.</b><span>Soʻrab-soʻrab Makkani topibdi</span></li>
  <li><b>Друг познаётся в беде́.</b><span>Doʻst kulfatda bilinadi</span></li>
  <li><b>Ти́ше е́дешь — да́льше бу́дешь.</b><span>Shoshilma</span></li>
  <li><b>Пе́рвый блин ко́мом.</b><span>Birinchi urinish chiqmasligi mumkin</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Посло́вица</b> — butun gap va saboq; <b>погово́рка</b> —
        gapning boʻlagi; <b>фразеологи́зм</b> — gap ichidagi birikma.</li>
    <li>Uchtasi oʻzbekchaga <b>aynan</b> tushadi: <em>Yetti oʻlchab
        bir kes</em>, <em>Nima eksang shuni oʻrasan</em>,
        <em>Yaltiragan hamma narsa oltin emas</em>.</li>
    <li><b>Язы́к до Ки́ева</b> ↔ <b>Soʻrab-soʻrab Makkani topibdi</b> —
        obraz boshqa, mantiq bir xil.</li>
    <li>Maqolni <b>tarjima qilmang — juftini toping</b>.</li>
    <li>Rus nutqida maqolning <b>yarmi</b> aytiladi. Buning uchun
        butunini bilish shart.</li>
    <li>Inshoda <b>Неда́ром говоря́т…</b> bilan kiriting. Arizada va
        hujjatda — <b>hech qachon</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-96: Tez-tez adashtiriladigan juftlar: одеть/надеть, тоже/то же, в течение/в течении",
        "category": "russian",
        "order": 96,
        "summary": (
            "Наде́ть = kiymoq, оде́ть = kiydirmoq — oʻzbekcha «-dir» qoʻshimchasi "
            "farqni aynan beradi. Va «ложить» degan feʼl umuman mavjud emas."
        ),
        "stories": ["Одеть или надеть?"],
        "content": """
<h2>PR-96: Tez-tez adashtiriladigan juftlar: одеть/надеть, тоже/то же, в течение/в течении</h2>

<p>Bu darsdagi xatolarni <b>ruslarning oʻzi</b> ham qiladi. Ular
maktabda tuzatiladi, imtihonda soʻraladi va internetda ular haqida
bahslashishadi.</p>

<p>Yaxshi xabar sizda: birinchi juftlikni oʻzbek tili sizga
<b>bepul</b> beradi. Boshlaymiz oʻshandan.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Наде́ть</b> va <b>оде́ть</b> ni bir umrga ajratasiz</li>
    <li><b>Класть / положи́ть</b> ni toʻgʻri ishlatasiz — va «ложи́ть» yoʻqligini bilasiz</li>
    <li><b>То́же</b> va <b>то же</b> ni bir soʻzda tekshirasiz</li>
    <li><b>В тече́ние</b> va <b>в тече́нии</b> ni farqlaysiz</li>
    <li><b>Что́бы</b> va <b>что бы</b> ni ajratasiz</li>
    <li>Yana ikkita mashhur xatoni tuzatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">наде́ть — что?</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">оде́ть — кого́?</span>
</div>

<h3>1. Наде́ть va оде́ть — oʻzbekcha kalit</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">НАДЕ́ТЬ — что?</p>
    <p><em>Я <b>наде́л</b> пальто́.</em></p>
    <p>Narsani <b>oʻzingizga</b> kiyasiz. Savoli — <b>что?</b></p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ОДЕ́ТЬ — кого́?</p>
    <p><em>Я <b>оде́л</b> ребёнка.</em></p>
    <p>Boshqa <b>odamni</b> kiyintirasiz. Savoli — <b>кого́?</b></p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha «-dir» qoʻshimchasi butun farqni beradi</span>
Oʻzbek tilida bu ikki maʼno <b>bitta oʻzakdan</b> yasaladi:<br><br>
<b>kiymoq</b> — oʻzingga &nbsp;→&nbsp; <b>наде́ть</b><br>
<b>kiy<span class="pr-end">dir</span>moq</b> — boshqaga &nbsp;→&nbsp; <b>оде́ть</b><br><br>
<em>Men palto <b>kiydim</b>.</em> → Я <b>наде́л</b> пальто́.<br>
<em>Men bolani <b>kiydirdim</b>.</em> → Я <b>оде́л</b> ребёнка.<br><br>
Yaʼni oʻzbekchadagi <b>orttirma nisbat</b> (-dir) ruschada
<b>alohida feʼl</b> bilan beriladi. Farq siz uchun yangi emas —
faqat u boshqa joyda turibdi.<br><br>
Shuning uchun tarjima qilishdan oldin oʻzbekcha gapga qarang:
«kiydim» boʻlsa — <b>наде́л</b>, «kiydirdim» boʻlsa —
<b>оде́л</b>.</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ruslarning oʻz eslatmasi</span>
Rus maktablarida bu qoida bitta jumla bilan yodlanadi:<br><br>
<b>«Надева́ют оде́жду, одева́ют Наде́жду.»</b><br><br>
<em>Оде́жда</em> — kiyim (narsa), <em>Наде́жда</em> — ayol ismi
(odam). Yaʼni: <b>narsani</b> — надева́ют, <b>odamni</b> —
одева́ют.<br><br>
Qiziq tomoni: soʻzlar joyini almashtirgan — <em>наде-</em>
<em>оде́жда</em> bilan, <em>оде-</em> esa <em>Наде́жда</em> bilan
ketadi. Aynan shu esda qoladi.</div>

<h3>2. Класть / положи́ть — «ложи́ть» degan feʼl yoʻq</h3>

<p>Bu — rus tilidagi eng mashhur xato. Qoida esa juda oddiy:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Tur</th><th>Toʻgʻri</th><th>Xato</th><th>Qoida</th></tr>
  <tr><td class="pr-stem">НСВ</td><td class="pr-res">класть · кладу́ · клал</td>
      <td class="pr-end">ложи́ть</td><td class="pr-uz"><b>prefikssiz</b></td></tr>
  <tr><td class="pr-stem">СВ</td><td class="pr-res">положи́ть · положу́ · положи́л</td>
      <td class="pr-end">покла́сть</td><td class="pr-uz"><b>prefiks bilan</b></td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Bitta jumlada</span>
<b>Prefikssiz — faqat КЛАСТЬ. Prefiks bilan — faqat -ЛОЖИТЬ.</b><br><br>
✓ <em>Я <b>кладу́</b> кни́гу на стол.</em> (НСВ, prefikssiz)<br>
✓ <em>Я <b>положи́л</b> кни́гу на стол.</em> (СВ, <em>по-</em> bilan)<br>
✓ <em>Он <b>сложи́л</b> ве́щи.</em> · <em>Она́ <b>вложи́ла</b>
письмо́.</em><br><br>
✗ <s>Я ложу́ кни́гу</s> — bunday feʼl adabiy tilda <b>mavjud
emas</b>.<br>
✗ <s>Я покла́л кни́гу</s> — bu ham yoʻq.<br><br>
Koʻchada <em>ложи́ть</em> ni eshitishingiz mumkin, lekin yozuvda
va imtihonda bu <b>xato</b> hisoblanadi.</div>

<h3>3. То́же va то же</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">ТО́ЖЕ — birga</p>
    <p><em>Я <b>то́же</b> пойду́.</em></p>
    <p>«Ham, shuningdek». <em>Та́кже</em> bilan almashtirsa boʻladi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ТО ЖЕ — alohida</p>
    <p><em>Он сказа́л <b>то же</b> са́мое.</em></p>
    <p>«Oʻsha narsa». <em>Са́мое</em> ni qoʻshsa boʻladi.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ikki soniyalik test</span>
<b>«Са́мое» ni qoʻshib koʻring.</b><br><br>
Qoʻshilsa — <b>alohida</b> yoziladi: <em>то же (са́мое)</em>.<br>
Qoʻshilmasa — <b>birga</b>: <em>то́же</em>.<br><br>
<em>Он сказа́л то же <b>са́мое</b>.</em> ✓ → alohida<br>
<s>Я то́же <b>са́мое</b> пойду́.</s> ✗ → demak birga: <em>то́же</em><br><br>
Xuddi shu test <b>та́кже / так же</b> uchun ham ishlaydi.</div>

<h3>4. В тече́ние va в тече́нии</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shakl</th><th>Nima haqida</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr class="pr-case__on"><td class="pr-res">в тече́ни<b>е</b></td>
      <td class="pr-uz"><b>vaqt</b> — predlog</td>
      <td class="pr-stem">в тече́ние неде́ли</td><td class="pr-end">bir hafta davomida</td></tr>
  <tr><td class="pr-res">в тече́ни<b>и</b></td><td class="pr-uz"><b>oqim</b> — haqiqiy ot</td>
      <td class="pr-stem">в тече́нии реки́</td><td class="pr-end">daryoning oqimida</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Daryo bormi?</span>
Savol bitta: gapda <b>haqiqiy oqim</b> bormi?<br><br>
Daryo, suv, oqim haqida gap ketyaptimi → <b>-и</b>:
<em>в тече́ни<b>и</b> реки́</em>.<br>
Vaqt haqidami → <b>-е</b>: <em>в тече́ни<b>е</b> го́да, в
тече́ни<b>е</b> ча́са</em>.<br><br>
Amalda 99 foiz holatda <b>vaqt</b> nazarda tutiladi, demak
deyarli har doim <b>-е</b>. Xuddi shunday: <em>в продолже́ние</em>,
<em>вследствие</em>.</div>

<h3>5. Что́бы va что бы</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Ikki xil «чтобы»</p>
  <p class="pe-ex__ru">Я пришёл, <b>что́бы</b> помо́чь.</p>
  <p class="pe-ex__uz">Yordam berish uchun keldim. — maqsad, birga yoziladi.</p>
  <p class="pe-ex__ru"><b>Что бы</b> ты сде́лал на моём ме́сте?</p>
  <p class="pe-ex__uz">Mening oʻrnimda nima qilarding? — «nima» + «бы», alohida.</p>
  <p class="pe-ex__why">Test: <b>бы</b> ni tashlab koʻring. Gap
     saqlanib qolsa — <b>alohida</b> (<em>Что ты сде́лал?</em>).
     Buzilsa — <b>birga</b>.</p>
</div>

<h3>6. Yana ikkita mashhur xato</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Он мне зво́нит ка́ждый день.</s></p>
  <p class="pe-good">Он мне <b>звони́т</b> — urgʻu <b>oxirgi boʻgʻinda</b>:
     звони́т, звоня́т, позвони́шь. Bu eng koʻp tekshiriladigan urgʻu.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Вообщем, я согла́сен.</s></p>
  <p class="pe-good"><b>В о́бщем</b>, я согла́сен. — <em>вообщем</em> degan
     soʻz yoʻq. Bor soʻzlar: <b>в о́бщем</b> (alohida) va
     <b>вообще́</b> (birga).</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Оде́нь пальто́, на у́лице хо́лодно.</s></p>
  <p class="pe-good"><b>Наде́нь</b> пальто́ — palto narsa, demak
     <em>наде́ть</em>. Oʻzbekcha «kiy», «kiydir» emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Не ложи́ телефо́н на стол.</s></p>
  <p class="pe-good">Не <b>клади́</b> телефо́н на стол — prefikssiz faqat
     <em>класть</em>.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я то́же са́мое ду́маю.</s></p>
  <p class="pe-good">Я думаю <b>то же са́мое</b> — <em>са́мое</em> qoʻshilyapti,
     demak alohida yoziladi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я всё сде́лаю в тече́нии неде́ли.</s></p>
  <p class="pe-good">…в тече́ни<b>е</b> неде́ли — vaqt haqida, daryo emas.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Toʻgʻri feʼlni qoʻying.<br>
     <b>Ма́ма ___ Афсо́ну и ___ ша́пку.</b> (оде́ть / наде́ть)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ма́ма оде́ла Афсо́ну и
    наде́ла ша́пку.</strong> Afsona — <b>odam</b> (кого́?) →
    <em>оде́ла</em>; shapka — <b>narsa</b> (что?) →
    <em>наде́ла</em>. Oʻzbekcha: «Afsonani <b>kiydirdi</b>» va
    «shapka <b>kiydi</b>».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Toʻgʻri shaklni tanlang.<br>
     <b>Я ___ докуме́нты в па́пку ка́ждое у́тро.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>кладу́</strong> —
    НСВ, prefikssiz. <s>Ложу́</s> degan feʼl adabiy tilda mavjud
    emas. СВ kerak boʻlsa: <em>положи́л</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Birgami yoki alohidami?<br>
     <b>Он сказа́л то(же) са́мое, что и вчера́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>то же</strong> — alohida.
    Tekshiruv: <em>са́мое</em> qoʻshilyapti, demak bu «oʻsha narsa».
    <em>То́же</em> boʻlganda <em>са́мое</em> qoʻshib
    boʻlmasdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>-е</b> yoki <b>-и</b>?<br>
     <b>В тече́ни_ ме́сяца · в тече́ни_ реки́</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в тече́ние ме́сяца</strong>
    (vaqt → -е) · <strong>в тече́нии реки́</strong> (haqiqiy oqim →
    -и). Amalda deyarli har doim vaqt nazarda tutiladi, demak
    <b>-е</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapda uchta xato bor. Toping.<br>
     <b>Вообщем, оде́нь ша́пку и не ложи́ её на стол.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>В о́бщем, наде́нь ша́пку и
    не клади́ её на стол.</strong><br>
    1. <s>Вообщем</s> → <b>в о́бщем</b> (bunday soʻz yoʻq).<br>
    2. <s>Оде́нь</s> → <b>наде́нь</b> (shapka — narsa).<br>
    3. <s>Ложи́</s> → <b>клади́</b> (prefikssiz faqat
    <em>класть</em>).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>наде́ть что?</b><span>kiymoq (oʻziga)</span></li>
  <li><b>оде́ть кого́?</b><span>kiydirmoq (boshqaga)</span></li>
  <li><b>класть · кладу́</b><span>qoʻymoq (НСВ, prefikssiz)</span></li>
  <li><b>положи́ть · положу́</b><span>qoʻymoq (СВ, prefiks bilan)</span></li>
  <li><b>то́же</b><span>ham, shuningdek</span></li>
  <li><b>то же са́мое</b><span>oʻsha narsa</span></li>
  <li><b>в тече́ние</b> + Р.п.<span>…davomida (vaqt)</span></li>
  <li><b>что́бы</b><span>…uchun (maqsad)</span></li>
  <li><b>в о́бщем</b><span>umuman olganda</span></li>
  <li><b>звони́т</b><span>qoʻngʻiroq qiladi (urgʻu oxirda)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Наде́ть — что?</b> (narsa), <b>оде́ть — кого́?</b> (odam).
        Oʻzbekcha: <b>kiymoq / kiydirmoq</b>.</li>
    <li>Ruslarning eslatmasi: <b>«Надева́ют оде́жду, одева́ют
        Наде́жду.»</b></li>
    <li><b>Prefikssiz — класть, prefiks bilan — положи́ть.</b>
        <em>Ложи́ть</em> degan feʼl <b>yoʻq</b>.</li>
    <li><b>Са́мое</b> qoʻshilsa — <b>то же</b> alohida; qoʻshilmasa —
        <b>то́же</b> birga.</li>
    <li><b>В тече́ние</b> — vaqt; <b>в тече́нии</b> — daryo oqimi.</li>
    <li><b>Бы</b> ni tashlab koʻring: gap saqlansa — <b>что бы</b>
        alohida.</li>
    <li>Urgʻu: <b>звони́т</b>, <s>зво́нит</s> emas. Va
        <b>в о́бщем</b>, <s>вообщем</s> emas.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-97: Punktuatsiya: vergul qoidalari va tire",
        "category": "russian",
        "order": 97,
        "summary": (
            "«Казни́ть нельзя́ поми́ловать» — vergul qayerda tursa, odam shunga "
            "yarasha yashaydi. Vergul, tire va oʻzbekcha bilan mos qoidalar."
        ),
        "stories": ["Запятая на доске"],
        "content": """
<h2>PR-97: Punktuatsiya: vergul qoidalari va tire</h2>

<p>Rus maktablarida bitta jumla bor. Unda uchta soʻz va bitta
vergul:</p>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">Казни́ть, нельзя́ поми́ловать.</span>
    <span class="pr-pair__uz">Qatl qiling, kechirib boʻlmaydi.</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">Казни́ть нельзя́, поми́ловать.</span>
    <span class="pr-pair__uz">Qatl qilib boʻlmaydi, kechiring.</span>
  </div>
</div>

<p>Uchta soʻz oʻzgarmadi. <b>Vergul</b> bir soʻz oʻngga
koʻchdi — va odam tirik qoldi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Ega bilan kesim orasiga <b>tire</b> qoʻyasiz</li>
    <li>Ergash gap oldiga <b>har doim</b> vergul qoʻyasiz</li>
    <li><b>И</b> oldida vergul kerakmi-yoʻqligini aniqlaysiz</li>
    <li><b>Kirish soʻzlarni</b> vergul bilan ajratasiz</li>
    <li><b>Undalmani</b> vergul bilan ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--s">ikki ega bor</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">vergul kerak</span>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Yaxshi xabar: bu tizim sizga tanish</span>
Oʻzbek tinish belgilari tizimi <b>rus tilidan olingan</b>. Shuning
uchun bu darsdagi qoidalarning koʻpi oʻzbekchada ham
<b>xuddi shunday</b> ishlaydi:<br><br>
— undalma vergul bilan ajratiladi: <em>Jasur, bu yoqqa kel.</em><br>
— kirish soʻz vergul bilan ajratiladi: <em>Albatta, men boraman.</em><br>
— ega bilan kesim orasiga tire qoʻyiladi:
<em>Toshkent — Oʻzbekiston poytaxti.</em><br><br>
Yaʼni siz noldan boshlamayapsiz. Faqat <b>bitta</b> qoida yangi
boʻladi — ergash gap oldidagi vergul. Uni alohida koʻramiz.</div>

<h3>1. Тире́ — ega va kesim orasida</h3>

<p>Rus tilida hozirgi zamonda <em>«boʻlmoq»</em> feʼli aytilmaydi
(PR-11). Uning oʻrniga <b>tire</b> qoʻyiladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gap</th><th>Nega tire</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">Москва́ — столи́ца Росси́и.</td>
      <td class="pr-uz">ot — ot, ikkalasi И.п.</td>
      <td class="pr-end">Moskva — Rossiya poytaxti.</td></tr>
  <tr><td class="pr-res">Мой брат — врач.</td><td class="pr-uz">ot — ot</td>
      <td class="pr-end">Akam — shifokor.</td></tr>
  <tr><td class="pr-res">Чита́ть — моё люби́мое заня́тие.</td>
      <td class="pr-uz">infinitiv — ot</td>
      <td class="pr-end">Oʻqish — mening sevimli mashgʻulotim.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Uch holatda tire QOʻYILMAYDI</span>
<b>1. Ega olmosh boʻlsa:</b><br>
<em>Он врач.</em> — <s>Он — врач.</s><br><br>
<b>2. «Не» bor boʻlsa:</b><br>
<em>Бе́дность не поро́к.</em> — <s>Бе́дность — не поро́к.</s><br><br>
<b>3. Kesim sifat boʻlsa:</b><br>
<em>Дом большо́й.</em> — <s>Дом — большо́й.</s><br><br>
Yodda tutish oson: tire faqat <b>ot va ot</b> (yoki infinitiv)
orasida turadi.</div>

<h3>2. Ergash gap oldida — HAR DOIM vergul</h3>

<p>Mana bu darsning yagona <b>yangi</b> qoidasi, va u eng koʻp xato
qilinadigan joy.</p>

<p>Rus tilida ergash gap <b>istisnosiz</b> vergul bilan ajratiladi.
<b>Который</b>, <b>что</b>, <b>чтобы</b>, <b>потому что</b>,
<b>если</b>, <b>когда</b>, <b>хотя</b> — bularning oldida
<b>har doim</b> vergul turadi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Beshta bogʻlovchi — beshta vergul</p>
  <p class="pe-ex__ru">Э́то кни́га<b>,</b> кото́рую я прочита́л ле́том.</p>
  <p class="pe-ex__ru">Я зна́ю<b>,</b> что он придёт.</p>
  <p class="pe-ex__ru">Я пришёл<b>,</b> что́бы помо́чь.</p>
  <p class="pe-ex__ru">Мы не пошли́<b>,</b> потому́ что шёл дождь.</p>
  <p class="pe-ex__ru">Позвони́<b>,</b> когда́ бу́дешь до́ма.</p>
  <p class="pe-ex__uz">Beshtasida ham vergul majburiy — tanlov yoʻq.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">«Потому что» — vergul qayerda?</span>
Odatda <b>butun bogʻlovchidan oldin</b>:<br>
<em>Мы не пошли́<b>,</b> потому́ что шёл дождь.</em><br><br>
Lekin sabab taʼkidlansa, vergul <b>ichkariga</b> koʻchishi
mumkin:<br>
<em>Мы не пошли́ потому́<b>,</b> что шёл дождь.</em> — «aynan
shuning uchun».<br><br>
Ikkalasi ham toʻgʻri. Ishonchingiz komil boʻlmasa —
<b>birinchisini</b> tanlang, u har doim toʻgʻri.</div>

<h3>3. «И» oldida vergul kerakmi?</h3>

<p>Savol bitta: gapda <b>nechta ega</b> bor?</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">BITTA EGA — vergul YOʻQ</p>
    <p><em>Я чита́л и писа́л.</em></p>
    <p>Bitta «я», ikkita feʼl. Vergul kerak emas.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">IKKI EGA — vergul BOR</p>
    <p><em>Я чита́л<b>,</b> и он писа́л.</em></p>
    <p>Ikki gap qoʻshildi — orasiga vergul.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ikki soniyalik test</span>
<b>«И» dan keyingi qismni alohida gap qilib oʻqing.</b><br><br>
Toʻliq gap chiqdimi (oʻz egasi bilan) → <b>vergul qoʻying</b>.<br>
Faqat feʼl chiqdimi → <b>vergul qoʻymang</b>.<br><br>
<em>…и он писа́л</em> → «Он писа́л» toʻliq gap ✓ → vergul<br>
<em>…и писа́л</em> → «Писа́л» ega yoʻq ✗ → vergul yoʻq</div>

<h3>4. Kirish soʻzlar — ikki tomondan vergul</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kirish soʻz</th><th>Oʻzbekcha</th><th>Misol</th></tr>
  <tr><td class="pr-res">коне́чно</td><td class="pr-uz">albatta</td>
      <td class="pr-end"><b>Коне́чно,</b> я помогу́.</td></tr>
  <tr><td class="pr-res">наве́рное</td><td class="pr-uz">ehtimol</td>
      <td class="pr-end">Он<b>,</b> наве́рное<b>,</b> опозда́ет.</td></tr>
  <tr><td class="pr-res">к сожале́нию</td><td class="pr-uz">afsuski</td>
      <td class="pr-end"><b>К сожале́нию,</b> я не смогу́.</td></tr>
  <tr><td class="pr-res">по-мо́ему</td><td class="pr-uz">menimcha</td>
      <td class="pr-end"><b>По-мо́ему,</b> э́то оши́бка.</td></tr>
  <tr><td class="pr-res">во-пе́рвых</td><td class="pr-uz">birinchidan</td>
      <td class="pr-end"><b>Во-пе́рвых,</b> э́то до́рого.</td></tr>
  <tr><td class="pr-res">ка́жется</td><td class="pr-uz">shekilli</td>
      <td class="pr-end">Он<b>,</b> ка́жется<b>,</b> уже́ ушёл.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">«Однако» — ikki xil ishlaydi</span>
Bu — sinovda eng koʻp uchraydigan tuzoq.<br><br>
<b>Gap boshida</b> = «lekin» → vergul <b>QOʻYILMAYDI</b>:<br>
<em><b>Одна́ко</b> он не пришёл.</em><br><br>
<b>Gap oʻrtasida</b> = «shunga qaramay» → vergul bilan
<b>AJRATILADI</b>:<br>
<em>Он<b>,</b> одна́ко<b>,</b> не пришёл.</em><br><br>
Tekshiruv: <em>но</em> bilan almashtirib koʻring. Almashsa —
vergul kerak emas.</div>

<h3>5. Undalma — har doim ajratiladi</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Uch xil oʻrin</p>
  <p class="pe-ex__ru"><b>Жасу́р,</b> иди́ сюда́.</p>
  <p class="pe-ex__ru">Иди́ сюда́<b>,</b> Жасу́р.</p>
  <p class="pe-ex__ru">Скажи́ мне<b>,</b> Жасу́р<b>,</b> где ты был?</p>
  <p class="pe-ex__uz">Boshida, oxirida yoki oʻrtasida — undalma
     har doim vergul bilan ajratiladi. Oʻzbekchada ham xuddi
     shunday.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Xatdagi murojaat</span>
PR-91 dagi qoidani eslang: rasmiy xatda murojaatdan keyin
<b>undov belgisi</b> qoʻyiladi, vergul emas:<br><br>
<b>Уважа́емая Мари́на Петро́вна!</b><br>
Сообща́ю Вам, что…<br><br>
Oddiy xatda esa vergul ham boʻladi:
<em>Приве́т<b>,</b> Ка́тя!</em></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то кни́га кото́рую я прочита́л.</s></p>
  <p class="pe-good">Э́то кни́га<b>,</b> кото́рую я прочита́л — <em>который</em>
     oldida vergul <b>har doim</b> turadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я чита́л, и писа́л.</s></p>
  <p class="pe-good">Я чита́л и писа́л — bitta ega, vergul kerak emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он — врач.</s></p>
  <p class="pe-good">Он врач — ega <b>olmosh</b> boʻlsa, tire qoʻyilmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Одна́ко, он не пришёл.</s></p>
  <p class="pe-good">Одна́ко он не пришёл — gap boshida <em>одна́ко</em>
     «lekin» degani, vergul olmaydi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Vergulni qoʻying va maʼnosini ayting.<br>
     <b>Казни́ть нельзя́ поми́ловать.</b> (odamni qutqaring)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Казни́ть нельзя́,
    поми́ловать.</strong> — «Qatl qilib boʻlmaydi, kechiring».
    Vergul <em>нельзя́</em> dan keyin tursa, odam tirik qoladi;
    <em>казни́ть</em> dan keyin tursa — yoʻq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Tire kerakmi?<br>
     <b>а) Мой оте́ц инжене́р. &nbsp; б) Он инжене́р. &nbsp;
     в) Чита́ть моё люби́мое заня́тие.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>а) Мой оте́ц —
    инжене́р.</strong> (ot — ot) ✓<br>
    <strong>б) Он инжене́р.</strong> — tire <b>yoʻq</b>, ega
    olmosh.<br>
    <strong>в) Чита́ть — моё люби́мое заня́тие.</strong>
    (infinitiv — ot) ✓</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Vergul kerakmi?<br>
     <b>а) Афсо́на пе́ла и танцева́ла. &nbsp;
     б) Афсо́на пе́ла и Бекзо́д танцева́л.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>а)</strong> vergul
    <b>yoʻq</b> — bitta ega (Афсо́на), ikkita feʼl.<br>
    <strong>б) Афсо́на пе́ла, и Бекзо́д танцева́л.</strong> — ikki
    ega, demak ikki gap qoʻshilgan → vergul.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Qaysi biri toʻgʻri?<br>
     <b>а) Одна́ко, он не пришёл. &nbsp; б) Он, одна́ко, не пришёл.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong> toʻgʻri.
    Gap oʻrtasida <em>одна́ко</em> kirish soʻz («shunga qaramay») →
    ikki tomondan vergul. Gap boshida esa u «lekin» degani va
    vergul olmaydi: <em>Одна́ко он не пришёл.</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapga toʻrtta tinish belgisi qoʻying.<br>
     <b>Дилно́за коне́чно я приду́ но то́лько е́сли бу́дет вре́мя</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Дилно́за, коне́чно, я
    приду́, но то́лько е́сли бу́дет вре́мя.</strong><br>
    1–2: <em>Дилно́за</em> — undalma, ajratiladi.<br>
    2–3: <em>коне́чно</em> — kirish soʻz.<br>
    3: <em>но</em> oldida vergul — ikki gap.<br>
    <em>Е́сли</em> oldida bu yerda alohida vergul qoʻyilmaydi,
    chunki u <em>но то́лько</em> ga qoʻshilib ketgan.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>запята́я</b><span>vergul</span></li>
  <li><b>тире́</b><span>tire</span></li>
  <li><b>двоето́чие</b><span>ikki nuqta</span></li>
  <li><b>то́чка</b><span>nuqta</span></li>
  <li><b>восклица́тельный знак</b><span>undov belgisi</span></li>
  <li><b>вво́дное сло́во</b><span>kirish soʻz</span></li>
  <li><b>обраще́ние</b><span>undalma</span></li>
  <li><b>подлежа́щее</b><span>ega</span></li>
  <li><b>сказу́емое</b><span>kesim</span></li>
  <li><b>сло́жное предложе́ние</b><span>qoʻshma gap</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Oʻzbek tinish tizimi rus tilidan olingan — qoidalarning
        koʻpi <b>bir xil</b>.</li>
    <li><b>Тире́</b> — ot bilan ot orasida. Olmosh, <em>не</em> yoki
        sifat boʻlsa — <b>yoʻq</b>.</li>
    <li>Ergash gap oldida — <b>har doim vergul</b>:
        который, что, чтобы, потому что, если, когда.</li>
    <li><b>«И» oldida:</b> ikki ega bormi? Bor → vergul. Yoʻq →
        vergul yoʻq.</li>
    <li><b>Kirish soʻz</b> va <b>undalma</b> — har doim vergul bilan
        ajratiladi.</li>
    <li><b>Одна́ко</b> boshida = «lekin», vergulsiz; oʻrtasida =
        kirish soʻz, vergul bilan.</li>
  </ul>
</div>
""",
    },
]
