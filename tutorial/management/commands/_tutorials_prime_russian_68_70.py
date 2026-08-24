# -*- coding: utf-8 -*-
"""Prime Russian — Block F davomi (68–70).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-68 — ли. Bu darsning oʻzbekcha tayanchi kursdagi eng kuchlilaridan biri:
ruscha «ли» = oʻzbekcha «-mi», va ikkalasi ham SOʻRALAYOTGAN SOʻZGA
yopishadi («Bugunmi kelasan?» ↔ «За́втра ли он придёт?»). Shu bitta
moslik butun darsni ochadi.
PR-69 — тот, кто / то, что. PR-63 (который) ning davomi: который otga
yopishadi, bu yerda esa ot yoʻq — shuning uchun rus tili oʻzi ot qoʻyadi.
Ikki qism ikki xil kelishikda turadi, xuddi который dagidek.
PR-70 — действительные причастия. Oʻzbek oʻquvchisida bu allaqachon bor:
-ayotgan / -gan / -adigan. Farq faqat oʻrnida (oʻzbekchada otdan oldin,
ruschada koʻpincha keyin) va vergulda.

Mashqlar:        practice/management/commands/_practice_pr_68_70.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_68_70.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_68_70.py --author=prime
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
        "title": "PR-68: Ли va bilvosita savol: «Не знаю, придёт ли он»",
        "category": "russian",
        "order": 68,
        "summary": (
            "Ruscha «ли» — oʻzbekcha «-mi» ning aynan oʻzi, va u ham soʻralayotgan "
            "soʻzga yopishadi. Shu bilan bilvosita savol quriladi."
        ),
        "stories": ["Никто не знал, придёт ли он"],
        "content": """
<h2>PR-68: Ли va bilvosita savol: «Не знаю, придёт ли он»</h2>

<p>Oʻzbekchada savolni bitta harf yasaydi: <em>«Kel<b>di</b>»</em> —
xabar, <em>«Kel<b>dimi</b>?»</em> — savol. Rus tilida ham xuddi shunday
zarracha bor: <b>ли</b>. U <em>-mi</em> ning aynan oʻzi, va eng qizigʻi
— <b>u ham xuddi shunday ishlaydi</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Ли</b> ni oʻzbekcha <b>-mi</b> ga bogʻlaysiz</li>
    <li>Bilvosita savol qurasiz: <em>Не зна́ю, придёт ли он</em></li>
    <li>Soʻz tartibi maʼnoni qanday oʻzgartirishini koʻrasiz</li>
    <li>Eng katta xatodan qutulasiz: <s>«Я не зна́ю, е́сли он придёт»</s></li>
    <li><b>Вряд ли</b> va boshqa tayyor iboralarni olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--v">soʻralayotgan soʻz</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">ли</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">qolgan gap</span>
</div>

<h3>1. Ли — bu «-mi»</h3>

<p>Ogʻzaki nutqda oddiy savol faqat ohang bilan beriladi:
<em>Он придёт?</em> Lekin yozma nutqda, rasmiy savolda va
<b>taʼkidda</b> rus tili <em>ли</em> ni qoʻyadi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Toʻgʻridan-toʻgʻri savol</p>
  <p class="pe-ex__ru">Придёт <b>ли</b> он?</p>
  <p class="pe-ex__uz">U kela<b>di</b><b>mi</b>?</p>
  <p class="pe-ex__why">Feʼl birinchi oʻringa chiqdi, <em>ли</em> undan
     keyin turdi. Oʻzbekchada ham <em>-mi</em> feʼlga yopishdi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha — darsning kaliti</span>
Oʻzbekcha <b>-mi</b> qaysi soʻzga yopishsa, savol <b>oʻsha soʻz
haqida</b> boʻladi. Ruscha <b>ли</b> ham xuddi shunday: u
soʻralayotgan soʻzning <b>orqasiga</b> turadi.<br><br>
<em>U <b>keladimi</b>?</em> &nbsp;→&nbsp; <b>Придёт ли</b> он?<br>
<em><b>Umi</b> keladi?</em> &nbsp;→&nbsp; <b>Он ли</b> придёт?<br>
<em><b>Ertagami</b> keladi?</em> &nbsp;→&nbsp; <b>За́втра ли</b> он придёт?<br><br>
Yaʼni siz bu qoidani bilasiz. Faqat oʻzbekchada zarracha soʻzga
<b>qoʻshilib</b> yoziladi, ruschada esa <b>alohida</b> turadi.</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Nima soʻralyapti</th><th>Ruscha</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-uz">kelish faktimi?</td>
      <td class="pr-res"><b>Придёт</b> ли он за́втра?</td>
      <td class="pr-end">U ertaga <b>keladimi</b>?</td></tr>
  <tr><td class="pr-uz">aynan umi?</td>
      <td class="pr-res"><b>Он</b> ли придёт за́втра?</td>
      <td class="pr-end"><b>Umi</b> ertaga keladi?</td></tr>
  <tr><td class="pr-uz">aynan ertagami?</td>
      <td class="pr-res"><b>За́втра</b> ли он придёт?</td>
      <td class="pr-end"><b>Ertagami</b> u keladi?</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qatʼiy qoida</span>
<b>Ли hech qachon birinchi soʻz boʻlmaydi.</b> Undan oldin har doim
soʻralayotgan soʻz turadi.<br><br>
<s>Ли он придёт?</s> &nbsp;→&nbsp; <b>Придёт ли он?</b></div>

<h3>2. Bilvosita savol — ли ning asosiy ishi</h3>

<p>Endi eng muhim qismi. Savolni boshqa gapning ichiga solganda
(<em>«bilmayman…», «soʻradi…», «qiziq…»</em>) rus tili
<b>majburan</b> <em>ли</em> ishlatadi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Bilvosita savol</p>
  <p class="pe-ex__ru">Я не зна́ю, <b>придёт ли</b> он.</p>
  <p class="pe-ex__uz">U keladimi, bilmayman.</p>
  <p class="pe-ex__ru">Он спроси́л, <b>есть ли</b> у меня́ вре́мя.</p>
  <p class="pe-ex__uz">Vaqtim bormi, deb soʻradi.</p>
  <p class="pe-ex__ru">Интере́сно, <b>рабо́тает ли</b> ещё э́тот магази́н.</p>
  <p class="pe-ex__uz">Qiziq, bu doʻkon hali ishlayaptimikan.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Kursdagi eng mashhur xato</span>
Rus tilida «…mi» maʼnosidagi <b>«если» YOʻQ</b>. Boshqa tillardan
kelib qolgan bu xato juda keng tarqalgan:<br><br>
<s>Я не зна́ю, <b>е́сли</b> он придёт.</s><br>
<b>Я не зна́ю, придёт <b>ли</b> он.</b><br><br>
Yodda tuting: <em>е́сли</em> — <b>shart</b> (PR-65), <em>ли</em> —
<b>savol</b>. Oʻzbekchada ham «agar» bilan «-mi» hech qachon
aralashmaydi.</div>

<h3>3. Savol soʻzi bor boʻlsa — ли kerak emas</h3>

<p>Bu farqni bir marta tushunsangiz, boshqa adashmaysiz.</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Savol soʻzi YOʻQ → ли</p>
    <p><em>Я не зна́ю, <b>придёт ли</b> он.</em><br>
       U keladi<b>mi</b>, bilmayman.</p>
    <p>Javobi: ha yoki yoʻq.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Savol soʻzi BOR → ли yoʻq</p>
    <p><em>Я не зна́ю, <b>когда́</b> он придёт.</em><br>
       U <b>qachon</b> keladi, bilmayman.</p>
    <p>Javobi: aniq maʼlumot.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada ham xuddi shu qoida ishlaydi — faqat siz buni
oʻylamasdan bajarasiz:<br><br>
<em>U kela<b>dimi</b>, bilmayman.</em> — savol soʻzi yoʻq, <b>-mi</b> bor<br>
<em><b>Qachon</b> keladi, bilmayman.</em> — savol soʻzi bor, <b>-mi</b> yoʻq<br><br>
Hech kim <s>«qachon keladimi, bilmayman»</s> demaydi. Ruschada ham
xuddi shunday: <s>когда́ ли</s> boʻlmaydi.</div>

<h3>4. Ли va vergul</h3>

<p>Bilvosita savol — ergash gap, demak undan oldin <b>vergul
majburiy</b>: <em>Я не зна́ю<b>,</b> придёт ли он.</em></p>

<p>Ikki variantni sanaganda <em>и́ли</em> qoʻshiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__t">Ли … или</p>
  <p class="pe-ex__ru">Я не зна́ю, придёт <b>ли</b> он <b>и́ли</b> нет.</p>
  <p class="pe-ex__uz">U keladimi yoki yoʻqmi, bilmayman.</p>
  <p class="pe-ex__ru">Реши́, идёшь <b>ли</b> ты с на́ми <b>и́ли</b> остаёшься.</p>
  <p class="pe-ex__uz">Biz bilan borasanmi yoki qolasanmi — hal qil.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Ikki variantni sanaganda oʻzbekcha <b>-mi</b> ikki marta takrorlanadi:
<em>«kela<b>dimi</b> yoki yoʻq<b>mi</b>»</em>. Ruschada esa
<em>ли</em> <b>bir marta</b> qoʻyiladi, ikkinchi qismda faqat
<em>и́ли</em> qoladi:<br><br>
<em>U keladi<b>mi</b> yoki yoʻq<b>mi</b>?</em><br>
→ Придёт <b>ли</b> он <b>и́ли</b> нет? &nbsp;
(<s>придёт ли он и́ли ли нет</s> — bunday boʻlmaydi)<br><br>
Shu bitta farqni yodda tutsangiz, bu qurilishda hech qachon
adashmaysiz.</div>

<h3>5. Qaysi soʻzlar ли talab qiladi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">не знать</td><td class="pr-uz">bilmaslik</td>
      <td class="pr-res">Не зна́ю, до́ма ли он.</td></tr>
  <tr><td class="pr-stem">спроси́ть</td><td class="pr-uz">soʻramoq</td>
      <td class="pr-res">Спроси́, рабо́тает ли по́чта.</td></tr>
  <tr><td class="pr-stem">узна́ть</td><td class="pr-uz">bilib olmoq</td>
      <td class="pr-res">Узна́й, есть ли биле́ты.</td></tr>
  <tr><td class="pr-stem">прове́рить</td><td class="pr-uz">tekshirmoq</td>
      <td class="pr-res">Прове́рь, рабо́тает ли интерне́т.</td></tr>
  <tr><td class="pr-stem">интере́сно</td><td class="pr-uz">qiziq</td>
      <td class="pr-res">Интере́сно, ско́лько э́то сто́ит.</td></tr>
  <tr><td class="pr-stem">сомнева́ться</td><td class="pr-uz">shubhalanmoq</td>
      <td class="pr-res">Я сомнева́юсь, пра́вда ли э́то.</td></tr>
  <tr><td class="pr-stem">по́мнить</td><td class="pr-uz">eslamoq</td>
      <td class="pr-res">Не по́мню, закры́л ли я дверь.</td></tr>
</table></div>

<h3>6. Tayyor iboralar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">вряд ли</td><td class="pr-uz">dargumon, gumon</td>
      <td class="pr-res">Вряд ли он придёт.</td></tr>
  <tr><td class="pr-stem">едва́ ли</td><td class="pr-uz">deyarli mumkin emas</td>
      <td class="pr-res">Едва́ ли мы успе́ем.</td></tr>
  <tr><td class="pr-stem">не так ли?</td><td class="pr-uz">shunday emasmi?</td>
      <td class="pr-res">Вы из Ташке́нта, не так ли?</td></tr>
  <tr><td class="pr-stem">то ли … то ли</td><td class="pr-uz">yo … yo (aniq emas)</td>
      <td class="pr-res">То ли дождь, то ли снег.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Вряд ли — yodlab oling</span>
<b>Вряд ли</b> kundalik nutqda juda koʻp ishlatiladi va oʻzbekcha
«<b>dargumon</b>», «<b>qayoqda</b>» degan maʼnoni beradi:<br><br>
— Он позвони́т?<br>
— <b>Вряд ли.</b> — Dargumon.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я не зна́ю, е́сли он придёт.</s></p>
  <p class="pe-good">Я не зна́ю, придёт <b>ли</b> он — <em>е́сли</em> shart, savol emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я не зна́ю, ли он придёт.</s></p>
  <p class="pe-good">…придёт <b>ли</b> он — <em>ли</em> birinchi soʻz boʻlmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я не зна́ю, когда́ ли он придёт.</s></p>
  <p class="pe-good">Я не зна́ю, <b>когда́</b> он придёт — savol soʻzi bor, <em>ли</em> keraksiz</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Спроси́ до́ма ли он.</s></p>
  <p class="pe-good">Спроси́<b>,</b> до́ма ли он — ergash gapdan oldin vergul</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Xatoni tuzating. &nbsp; <b>Я не зна́ю, е́сли она́ до́ма.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я не зна́ю, до́ма ли
    она́.</strong> Bu savol («uydami?»), shart emas. Soʻralayotgan
    soʻz — <em>до́ма</em> — oldinga chiqadi, <em>ли</em> undan keyin
    turadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu ikki gapning farqi nima?<br>
     <b>Придёт ли Жасу́р? · Жасу́р ли придёт?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi: <b>Jasur keladimi?</b>
    — kelish-kelmaslik soʻralyapti. Ikkinchisi: <b>Jasurmi
    keladi?</b> — kimdir keladi, lekin aynan Jasurmi? <em>Ли</em>
    oʻzidan oldingi soʻzni soʻroq ostiga oladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>Ли</b> kerakmi? &nbsp; <b>Я не по́мню, где ___ я оста́вил
     ключи́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Kerak emas.</strong>
    <em>Я не по́мню, где я оста́вил ключи́.</em> Gapda savol soʻzi
    (<em>где</em>) bor, demak <em>ли</em> ortiqcha.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Doʻkon ishlayaptimi, tekshir.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Прове́рь, рабо́тает ли
    магази́н.</strong> Oʻzbekcha <em>-mi</em> feʼlga yopishgan,
    demak ruschada ham <em>ли</em> feʼldan keyin turadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Javobni bitta ibora bilan bering.<br>
     <b>— Ты ду́маешь, он сда́ст экза́мен без подгото́вки?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>— Вряд ли.</strong>
    «Dargumon». Bu ibora ichida ham <em>ли</em> turibdi, lekin u
    qotib qolgan — alohida tahlil qilinmaydi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ли</b><span>-mi (savol zarrachasi)</span></li>
  <li><b>вряд ли</b><span>dargumon</span></li>
  <li><b>едва́ ли</b><span>deyarli mumkin emas</span></li>
  <li><b>не так ли?</b><span>shunday emasmi?</span></li>
  <li><b>то ли … то ли</b><span>yo … yo (aniq emas)</span></li>
  <li><b>узна́ть</b><span>bilib olmoq</span></li>
  <li><b>прове́рить</b><span>tekshirmoq</span></li>
  <li><b>сомнева́ться</b><span>shubhalanmoq</span></li>
  <li><b>успе́ть</b><span>ulgurmoq</span></li>
  <li><b>подгото́вка</b><span>tayyorgarlik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Ли = -mi.</b> Ikkalasi ham soʻralayotgan soʻzning orqasida
        turadi.</li>
    <li><b>Ли hech qachon birinchi soʻz emas.</b></li>
    <li>Bilvosita savolda <b>majburiy</b>: <em>Не зна́ю, придёт ли
        он.</em></li>
    <li><s>«Не зна́ю, е́сли он придёт»</s> — <b>xato</b>. <em>Е́сли</em>
        shart, <em>ли</em> savol.</li>
    <li>Gapda <b>savol soʻzi</b> (где, когда́, кто…) boʻlsa —
        <em>ли</em> qoʻyilmaydi.</li>
    <li>Ergash gapdan oldin <b>vergul</b>. Ikki variant boʻlsa —
        <b>ли … и́ли</b>.</li>
    <li><b>Вряд ли</b> = dargumon. Kundalik nutqning eng kerakli
        iboralaridan biri.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-69: Тот, кто… / то, что… — koʻrsatish va bogʻlash",
        "category": "russian",
        "order": 69,
        "summary": (
            "Который otga yopishadi. Ot boʻlmasa nima qilamiz? Rus tili otning "
            "oʻrniga «тот» yoki «то» qoʻyadi — oʻzbekcha «kim… oʻsha» kabi."
        ),
        "stories": ["Тот, кто сажает деревья"],
        "content": """
<h2>PR-69: Тот, кто… / то, что… — koʻrsatish va bogʻlash</h2>

<p>PR-63 da <b>кото́рый</b> ni oʻrgangansiz: <em>челове́к,
<b>кото́рый</b> мно́го чита́ет</em>. Lekin <em>кото́рый</em> ga har
doim <b>ot</b> kerak — u otga yopishadi. Xoʻsh, ot boʻlmasa-chi?
«Koʻp oʻqi<b>gan odam</b>» emas, shunchaki «koʻp oʻqi<b>gan</b>»
demoqchi boʻlsangiz? Rus tili juda oddiy yoʻl tutadi: <b>otning
oʻrniga oʻzi bir soʻz qoʻyadi</b> — <em>тот</em> yoki <em>то</em>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Тот, кто</b> (odam) va <b>то, что</b> (narsa) ni ajratasiz</li>
    <li>Ikki qism <b>ikki xil kelishikda</b> turishini oʻrganasiz</li>
    <li>Predlogdan keyin <b>то</b> majburiy ekanini bilasiz</li>
    <li><b>Все, кто</b> dan keyin feʼl birlikda turishini eslab qolasiz</li>
    <li><b>Де́ло в том, что…</b> — kundalik nutqning eng kerakli iborasini olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Odam</span>
  <span class="pe-chip pe-chip--s">тот</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">кто + gap</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Narsa</span>
  <span class="pe-chip pe-chip--o">то</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">что + gap</span>
</div>

<h3>1. Кото́рый bilan farqi</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">КОТО́РЫЙ — ot bor</p>
    <p><em><b>Челове́к</b>, кото́рый мно́го чита́ет, хорошо́ пи́шет.</em><br>
       Koʻp oʻqiydigan <b>odam</b> yaxshi yozadi.</p>
    <p>Gapda ot turibdi — <em>кото́рый</em> unga yopishadi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ТОТ, КТО — ot yoʻq</p>
    <p><em><b>Тот</b>, кто мно́го чита́ет, хорошо́ пи́шет.</em><br>
       Koʻp oʻqiydigan yaxshi yozadi.</p>
    <p>Ot yoʻq, shuning uchun <em>тот</em> uning oʻrnida turibdi.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada bu qurilish bor va u ham <b>juft</b>:<br><br>
<em><b>Kim</b> koʻp oʻqisa, <b>oʻsha</b> yaxshi yozadi.</em><br>
→ <b>Тот</b>, <b>кто</b> мно́го чита́ет, хорошо́ пи́шет.<br><br>
<em><b>Nima</b> deding, men <b>oʻsha</b>ni tushunmadim.</em><br>
→ Я не по́нял <b>то</b>, <b>что</b> ты сказа́л.<br><br>
Yaʼni oʻzbekchadagi <b>«oʻsha»</b> — bu ruscha <b>тот / то</b>.
Faqat oʻzbekchada u ikkinchi oʻrinda turadi, ruschada esa
<b>birinchi</b>.</div>

<div class="pe-ex">
  <p class="pe-ex__t">Odam ↔ narsa</p>
  <p class="pe-ex__ru"><b>Тот</b>, кто и́щет, нахо́дит.</p>
  <p class="pe-ex__uz">Qidirgan topadi. — <b>Odam</b> haqida: тот, кто.</p>
  <p class="pe-ex__ru">Я не по́нял <b>то</b>, что ты сказа́л.</p>
  <p class="pe-ex__uz">Aytganingni tushunmadim. — <b>Narsa</b> haqida: то, что.</p>
  <p class="pe-ex__why">Odamga — <em>тот, кто</em>. Narsaga, gapga,
     butun bir fikrga — <em>то, что</em>.</p>
</div>

<h3>2. Ikki qism, ikki kelishik</h3>

<p>Bu darsning yuragi. Qoida <em>кото́рый</em> nikiga aynan
oʻxshaydi (PR-63):</p>

<div class="pe-formula">
  <span class="pe-formula__label">Qoida</span>
  <span class="pe-chip pe-chip--s">тот — asosiy gapdan</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">кто — oʻz gapidan</span>
</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gap</th><th>тот nega shunday</th><th>кто nega shunday</th></tr>
  <tr><td class="pr-res">Я помога́ю <b>тому́</b>, <b>кто</b> про́сит.</td>
      <td class="pr-uz">помога́ть кому́? — Д.п.</td>
      <td class="pr-end">кто про́сит — ega, И.п.</td></tr>
  <tr><td class="pr-res"><b>Тот</b>, <b>кого́</b> мы жда́ли, не пришёл.</td>
      <td class="pr-uz">тот — ega, И.п.</td>
      <td class="pr-end">ждать кого́? — В.п.</td></tr>
  <tr><td class="pr-res">Я ду́маю о <b>том</b>, <b>что</b> ты сказа́л.</td>
      <td class="pr-uz">ду́мать о чём? — П.п.</td>
      <td class="pr-end">сказа́ть что? — В.п.</td></tr>
  <tr><td class="pr-res">Спаси́бо за <b>то</b>, <b>что</b> вы пришли́.</td>
      <td class="pr-uz">спаси́бо за что? — В.п.</td>
      <td class="pr-end">что вы пришли́ — butun gap</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Nega bu qiyin</span>
Oʻzbekchada <em>«oʻsha»</em> soʻzi ham turlanadi
(<em>oʻshaga, oʻshani</em>), lekin ergash gapdagi soʻz turlanmaydi.
Ruschada esa <b>ikkalasi ham</b> turlanadi va ular <b>bir-biriga
qaramaydi</b>.<br><br>
Har safar ikkita alohida savol bering:<br>
1. <b>Asosiy gapda</b> bu soʻz qanday vazifada? → <em>тот</em> ning
   kelishigi.<br>
2. <b>Ergash gapda</b> u qanday vazifada? → <em>кто / что</em> ning
   kelishigi.<br><br>
Xuddi PR-63 dagi <em>кото́рый</em> kabi — bir xil mantiq.</div>

<h3>3. Predlogdan keyin «то» tushib qolmaydi</h3>

<p>Agar asosiy gapdagi feʼl <b>predlog</b> talab qilsa, predlogdan
keyin <b>albatta</b> <em>том / то</em> turadi. Uni tashlab
ketish — koʻp uchraydigan xato.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Predlog bilan</p>
  <p class="pe-ex__ru">Я ду́маю <b>о том</b>, что ты сказа́л.</p>
  <p class="pe-ex__uz">Aytganing haqida oʻylayapman.</p>
  <p class="pe-ex__ru">Я не сомнева́юсь <b>в том</b>, что он придёт.</p>
  <p class="pe-ex__uz">Uning kelishiga shubham yoʻq.</p>
  <p class="pe-ex__ru">Спаси́бо <b>за то</b>, что помогли́.</p>
  <p class="pe-ex__uz">Yordam berganingiz uchun rahmat.</p>
  <p class="pe-ex__why">Predlog otsiz turolmaydi — <em>то</em> aynan
     oʻsha otning oʻrnini bosadi.</p>
</div>

<h3>4. Все, кто — feʼl birlikda</h3>

<p>Bir nozik joy: <em>кто</em> dan keyingi feʼl <b>har doim
birlikda</b> turadi, hatto <em>все</em> bilan ham.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Все, кто</p>
  <p class="pe-ex__ru">Все, кто <b>пришёл</b>, получи́ли кни́гу.</p>
  <p class="pe-ex__uz">Kelganlarning hammasi kitob oldi.</p>
  <p class="pe-ex__why"><em>Пришёл</em> — birlikda, chunki u
     <em>кто</em> ga tegishli. Asosiy gapdagi <em>получи́ли</em> esa
     <em>все</em> ga tegishli, shuning uchun koʻplikda.</p>
</div>

<h3>5. То, что — tayyor iboralar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">де́ло в том, что…</td><td class="pr-uz">gap shundaki…</td>
      <td class="pr-res">Де́ло в том, что вре́мени ма́ло.</td></tr>
  <tr><td class="pr-stem">то, что ну́жно</td><td class="pr-uz">aynan kerakli narsa</td>
      <td class="pr-res">Э́то то, что ну́жно.</td></tr>
  <tr><td class="pr-stem">де́ло не в том…</td><td class="pr-uz">gap bunda emas…</td>
      <td class="pr-res">Де́ло не в том, что до́рого.</td></tr>
  <tr><td class="pr-stem">речь идёт о том…</td><td class="pr-uz">gap … haqida ketyapti</td>
      <td class="pr-res">Речь идёт о том, как нам успе́ть.</td></tr>
  <tr><td class="pr-stem">тот, кто…</td><td class="pr-uz">kim … oʻsha</td>
      <td class="pr-res">Тот, кто и́щет, нахо́дит.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Sovgʻa</span>
<b>Де́ло в том, что…</b> — bu oʻzbekcha <b>«Gap shundaki…»</b>
iborasining aynan oʻzi, soʻzma-soʻz. Ikkala tilda ham u
tushuntirishni boshlaydi:<br><br>
<em>Gap shundaki, mening vaqtim yoʻq.</em><br>
→ <b>Де́ло в том, что</b> у меня́ нет вре́мени.<br><br>
Shu bitta iborani yodlab olsangiz, tushuntirish boshlash uchun
har doim tayyor jumlangiz boʻladi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Тот, кто мно́го чита́ет, хорошо́ пи́шут.</s></p>
  <p class="pe-good">…хорошо́ <b>пи́шет</b> — <em>тот</em> birlikda, feʼl ham birlikda</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я помога́ю тот, кто про́сит.</s></p>
  <p class="pe-good">Я помога́ю <b>тому́</b>, кто про́сит — помога́ть Д.п. talab qiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ду́маю о что ты сказа́л.</s></p>
  <p class="pe-good">Я ду́маю <b>о том</b>, что ты сказа́л — predlogdan keyin <em>то</em></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Все, кто пришли́, получи́ли кни́гу.</s></p>
  <p class="pe-good">Все, кто <b>пришёл</b>, получи́ли кни́гу — <em>кто</em> dan keyin birlik</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Я ве́рю ___, кто говори́т
     пра́вду.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>тому́</strong>.
    <em>Ве́рить</em> <b>кому́?</b> — Да́тельный. <em>Кто</em> esa oʻz
    gapida ega, shuning uchun И.п. da qoladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyni toʻldiring. &nbsp; <b>Спаси́бо ___, что вы
     пришли́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>за то</strong>.
    <em>Спаси́бо за что?</em> — Вини́тельный, demak <em>за
    то</em>. Predlogsiz <s>«спаси́бо, что»</s> ogʻzaki nutqda
    uchraydi, lekin toʻgʻri shakl — <em>спаси́бо за то,
    что</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Xatoni toping. &nbsp; <b>Все, кто хоте́ли, оста́лись.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Все, кто хоте́л,
    оста́лись.</strong> <em>Кто</em> dan keyingi feʼl birlikda
    turadi. Asosiy gapdagi <em>оста́лись</em> esa <em>все</em> ga
    tegishli — u koʻplikda toʻgʻri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>Кото́рый</b> yoki <b>тот, кто</b>? &nbsp;
     <b>___ мно́го рабо́тает, тот мно́го зна́ет.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Кто</strong> —
    <em>Кто мно́го рабо́тает, тот мно́го зна́ет.</em> Gapda ot yoʻq,
    demak <em>кото́рый</em> ishlamaydi. Maqollarda tartib
    teskari boʻlishi mumkin: avval <em>кто</em>, keyin
    <em>тот</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Gap shundaki, men aytganingni tushunmadim.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Де́ло в том, что я не
    по́нял то, что ты сказа́л.</strong> Bitta gapda ikkita
    <em>то, что</em>: birinchisi ibora ichida
    (<em>де́ло в том, что</em>), ikkinchisi esa <em>поня́ть</em>
    ning obyekti — В.п., shuning uchun <em>то</em>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>тот, кто</b><span>kim … oʻsha (odam haqida)</span></li>
  <li><b>то, что</b><span>nima … oʻsha (narsa haqida)</span></li>
  <li><b>де́ло в том, что</b><span>gap shundaki</span></li>
  <li><b>речь идёт о том</b><span>gap … haqida ketyapti</span></li>
  <li><b>ве́рить</b> + Д.п.<span>ishonmoq</span></li>
  <li><b>сомнева́ться</b> в чём<span>shubhalanmoq</span></li>
  <li><b>иска́ть</b><span>qidirmoq</span></li>
  <li><b>находи́ть</b><span>topmoq</span></li>
  <li><b>получи́ть</b><span>olmoq (qoʻlga kiritmoq)</span></li>
  <li><b>оста́ться</b><span>qolmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Ot bor → <b>кото́рый</b>. Ot yoʻq → <b>тот, кто</b> /
        <b>то, что</b>.</li>
    <li>Oʻzbekcha <b>«kim… oʻsha»</b> — bu aynan
        <em>тот, кто</em>.</li>
    <li><b>Тот</b> asosiy gapdan kelishik oladi, <b>кто/что</b> esa
        oʻz gapidan. Ikkita alohida savol bering.</li>
    <li>Predlogdan keyin <b>то majburiy</b>: <em>о том, что</em> ·
        <em>за то, что</em> · <em>в том, что</em>.</li>
    <li><b>Кто</b> dan keyingi feʼl <b>birlikda</b>: <em>все, кто
        пришёл</em>.</li>
    <li><b>Де́ло в том, что…</b> = «Gap shundaki…». Yodlab
        qoʻying.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-70: Причастие 1: действительные — читающий, прочитавший",
        "category": "russian",
        "order": 70,
        "summary": (
            "Sifatdosh — feʼlning sifat kiyimidagi shakli. Oʻzbek oʻquvchisida bu "
            "allaqachon bor: -ayotgan, -gan, -adigan. Farq faqat oʻrni va vergulda."
        ),
        "stories": ["Люди, живущие на Севере"],
        "content": """
<h2>PR-70: Причастие 1: действительные — читающий, прочитавший</h2>

<p>Oʻzbekchada siz buni har kuni ishlatasiz: <em>oʻqi<b>yotgan</b>
bola</em>, <em>oʻqi<b>gan</b> bola</em>, <em>oʻqi<b>ydigan</b>
bola</em>. Feʼl sifatga aylanadi va otni aniqlaydi. Rus tilida bu
<b>причастие</b> deyiladi va u sizda allaqachon bor — faqat
ruschasini olishingiz kerak.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Причастие</b> nima ekanini va oʻzbekcha <b>-gan / -ayotgan</b> ga qanday tushishini koʻrasiz</li>
    <li>Hozirgi zamon shaklini yasaysiz: <b>чита́ют → чита́ющий</b></li>
    <li>Oʻtgan zamon shaklini yasaysiz: <b>чита́л → чита́вший</b></li>
    <li>Vergul qoidasini oʻrganasiz — u <b>oʻrniga</b> bogʻliq</li>
    <li>Har qanday sifatdoshni <b>кото́рый</b> li gapga yoyib tushunasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Hozirgi</span>
  <span class="pe-chip pe-chip--s">они́ shakli − т</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">щ</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">ий / ая / ее / ие</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Oʻtgan</span>
  <span class="pe-chip pe-chip--s">он shakli − л</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">вш</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">ий / ая / ее / ие</span>
</div>

<h3>1. Bu nima va nega kerak</h3>

<p><b>Действительное причастие</b> — ot <b>oʻzi</b> ish qilayotganini
bildiradi. (Ot ish <b>koʻrayotgan</b> tomon boʻlsa, u
<em>страда́тельное</em> boʻladi — PR-71 da.)</p>

<div class="pe-ex">
  <p class="pe-ex__t">Bir xil maʼno, ikki shakl</p>
  <p class="pe-ex__ru">Ма́льчик, <b>кото́рый чита́ет</b> кни́гу, — мой брат.</p>
  <p class="pe-ex__ru">Ма́льчик, <b>чита́ющий</b> кни́гу, — мой брат.</p>
  <p class="pe-ex__uz">Kitob oʻqiyotgan bola — mening akam.</p>
  <p class="pe-ex__why">Ikkala gap ham toʻgʻri. Birinchisi —
     <b>ogʻzaki</b>, ikkinchisi — <b>yozma</b> uslub.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha — bu sizda bor</span>
Bu darsning butun mazmuni bitta jadvalga sigʻadi:<br><br>
<em>oʻqi<b>yotgan</b> bola</em> &nbsp;→&nbsp; <b>чита́ющий</b> ма́льчик<br>
<em>oʻqi<b>gan</b> bola</em> &nbsp;→&nbsp; <b>чита́вший</b> ма́льчик<br>
<em>oʻqi<b>b chiqqan</b> bola</em> &nbsp;→&nbsp; <b>прочита́вший</b> ма́льчик<br><br>
Yagona jiddiy farq — <b>oʻrni</b>. Oʻzbekchada sifatdosh <b>har doim
otdan oldin</b> turadi. Ruschada esa u koʻpincha <b>otdan
keyin</b> keladi, va aynan shundan vergul qoidasi kelib chiqadi
(4-boʻlim).</div>

<h3>2. Hozirgi zamon: -ущ- / -ющ- / -ащ- / -ящ-</h3>

<p>Yasalish PR-59 dagi buyruq mayli bilan bir xil joydan boshlanadi —
<b>они́</b> shaklidan.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>Они́ shakli</th><th>−т + щ</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">чита́ть</td><td class="pr-uz">чита́ю<b>т</b></td>
      <td class="pr-end">чита́ю + щ</td><td class="pr-res">чита́ющий</td>
      <td class="pr-uz">oʻqiyotgan</td></tr>
  <tr><td class="pr-stem">рабо́тать</td><td class="pr-uz">рабо́таю<b>т</b></td>
      <td class="pr-end">рабо́таю + щ</td><td class="pr-res">рабо́тающий</td>
      <td class="pr-uz">ishlayotgan</td></tr>
  <tr><td class="pr-stem">идти́</td><td class="pr-uz">иду́<b>т</b></td>
      <td class="pr-end">иду + щ</td><td class="pr-res">иду́щий</td>
      <td class="pr-uz">ketayotgan</td></tr>
  <tr><td class="pr-stem">жить</td><td class="pr-uz">живу́<b>т</b></td>
      <td class="pr-end">живу + щ</td><td class="pr-res">живу́щий</td>
      <td class="pr-uz">yashayotgan</td></tr>
  <tr><td class="pr-stem">говори́ть</td><td class="pr-uz">говоря́<b>т</b></td>
      <td class="pr-end">говоря + щ</td><td class="pr-res">говоря́щий</td>
      <td class="pr-uz">gapirayotgan</td></tr>
  <tr><td class="pr-stem">люби́ть</td><td class="pr-uz">лю́бя<b>т</b></td>
      <td class="pr-end">люб я + щ</td><td class="pr-res">лю́бящий</td>
      <td class="pr-uz">sevadigan</td></tr>
  <tr><td class="pr-stem">учи́ться</td><td class="pr-uz">у́ча<b>т</b>ся</td>
      <td class="pr-end">уча + щ + ся</td><td class="pr-res">уча́щийся</td>
      <td class="pr-uz">oʻqiyotgan (oʻquvchi)</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Muhim cheklov</span>
<b>СВ feʼllarining hozirgi zamon sifatdoshi YOʻQ.</b> Sabab oddiy:
СВ feʼlida hozirgi zamon umuman yoʻq (PR-51).<br><br>
<s>прочита́ющий</s> — bunday soʻz mavjud emas.<br>
<b>прочита́вший</b> — oʻtgan zamon shakli, mana bu bor.<br><br>
Yaʼni: <b>НСВ</b> → hozirgi ham, oʻtgan ham. <b>СВ</b> → faqat
oʻtgan.</div>

<h3>3. Oʻtgan zamon: -вш- / -ш-</h3>

<p>Bu yerda tayanch nuqta — <b>oʻtgan zamonning erkak shakli</b>
(<em>он</em> shakli). Undan <b>-л</b> olib tashlanadi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>Он shakli</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">чита́ть</td><td class="pr-uz">чита́<b>л</b></td>
      <td class="pr-res">чита́вший</td><td class="pr-end">oʻqigan (oʻqib yurgan)</td></tr>
  <tr><td class="pr-stem">прочита́ть</td><td class="pr-uz">прочита́<b>л</b></td>
      <td class="pr-res">прочита́вший</td><td class="pr-end">oʻqib chiqqan</td></tr>
  <tr><td class="pr-stem">верну́ться</td><td class="pr-uz">верну́<b>л</b>ся</td>
      <td class="pr-res">верну́вшийся</td><td class="pr-end">qaytgan</td></tr>
  <tr><td class="pr-stem">прийти́</td><td class="pr-uz">пришёл</td>
      <td class="pr-res">прише́дший</td><td class="pr-end">kelgan</td></tr>
  <tr><td class="pr-stem">принести́</td><td class="pr-uz">принёс</td>
      <td class="pr-res">принёсший</td><td class="pr-end">olib kelgan</td></tr>
  <tr><td class="pr-stem">вы́расти</td><td class="pr-uz">вы́рос</td>
      <td class="pr-res">вы́росший</td><td class="pr-end">oʻsgan, ulgʻaygan</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">-вш- yoki -ш-?</span>
Oʻtgan zamonda <b>-л</b> boʻlsa → <b>-вш-</b>:
<em>чита́<b>л</b> → чита́<b>вш</b>ий</em>.<br><br>
<b>-л</b> boʻlmasa (undosh bilan tugasa) → <b>-ш-</b>:
<em>принёс → принёс<b>ш</b>ий</em>, <em>вы́рос → вы́рос<b>ш</b>ий</em>.<br><br>
Va yana bitta qoida: <b>-ся hech qachon -сь boʻlmaydi</b>
sifatdoshda. <em>верну́вший<b>ся</b></em>, <em>улыба́ющий<b>ся</b></em> —
har doim <em>-ся</em>.</div>

<h3>3.5. Sifatdosh otga moslashadi</h3>

<p>Yasab boʻlgach, sifatdosh oddiy sifat kabi ishlaydi: <b>jins, son
va kelishikda</b> oʻzi aniqlayotgan otga moslashadi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Bitta sifatdosh, toʻrt shakl</p>
  <p class="pe-ex__ru">Ма́льчик, <b>чита́ющий</b> кни́гу, — мой брат. <span class="pr-uz">(И.п., erkak)</span></p>
  <p class="pe-ex__ru">Де́вочка, <b>чита́ющая</b> кни́гу, — моя́ сестра́. <span class="pr-uz">(И.п., ayol)</span></p>
  <p class="pe-ex__ru">Я ви́дел ма́льчика, <b>чита́ющего</b> кни́гу. <span class="pr-uz">(В.п.)</span></p>
  <p class="pe-ex__ru">Я подошёл к де́тям, <b>чита́ющим</b> кни́гу. <span class="pr-uz">(Д.п., koʻplik)</span></p>
  <p class="pe-ex__uz">Kitob oʻqiyotgan bola / qiz / bolani / bolalarga.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Mana shu joy qiyin</span>
Oʻzbekchada sifatdosh <b>hech qachon oʻzgarmaydi</b>: <em>oʻqiyotgan
bola</em>, <em>oʻqiyotgan bolani</em>, <em>oʻqiyotgan
bolalarga</em> — soʻz bir xil turaveradi, qoʻshimcha faqat
<b>otga</b> qoʻshiladi.<br><br>
Ruschada esa <b>ikkalasi ham</b> oʻzgaradi:
<em>ма́льчик<b>а</b>, чита́ющ<b>его</b></em>. Oʻzbek oʻquvchisining
eng koʻp uchraydigan xatosi shu — sifatdoshni И.п. da qoldirib
ketish.<br><br>
Tekshirish oson: sifatdosh qaysi otga tegishli boʻlsa, <b>oʻsha
otning qoʻshimchasiga qarang</b>. Bu — PR-12 dagi oddiy sifat
qoidasining oʻzi, faqat soʻz uzunroq.</div>

<h3>4. Vergul — hammasi oʻringa bogʻliq</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Otdan KEYIN → vergul</p>
    <p><em>Ма́льчик<b>,</b> чита́ющий кни́гу<b>,</b> — мой брат.</em></p>
    <p>Sifatdosh oborot ikki tomondan ajratiladi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Otdan OLDIN → vergul yoʻq</p>
    <p><em>Чита́ющий кни́гу ма́льчик — мой брат.</em></p>
    <p>Hech qanday vergul qoʻyilmaydi.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekcha tartib — bu <b>vergulsiz</b> variant:
<em>«kitob oʻqiyotgan bola»</em> = <em>чита́ющий кни́гу
ма́льчик</em>. Vergul kerak emas.<br><br>
Lekin rus tili yozma matnda koʻpincha <b>ikkinchi</b> tartibni
tanlaydi — sifatdoshni otdan keyinga qoʻyadi, chunki shunda gap
ravonroq oʻqiladi. Shuning uchun kitob oʻqiyotganda siz koʻproq
vergulli variantni uchratasiz.<br><br>
Qoidani bitta jumla bilan yodlang: <b>oborot otdan keyin
tursa — ikki tomondan vergul.</b></div>

<h3>5. Sifatdoshni кото́рый ga yoying</h3>

<p>Notanish sifatdoshni uchratsangiz, uni <em>кото́рый</em> li gapga
aylantiring — maʼnosi darrov ochiladi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Причастие</th><th>Кото́рый bilan</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">студе́нт, чита́ющий кни́гу</td>
      <td class="pr-res">студе́нт, кото́рый чита́ет кни́гу</td>
      <td class="pr-end">kitob oʻqiyotgan talaba</td></tr>
  <tr><td class="pr-stem">студе́нт, прочита́вший кни́гу</td>
      <td class="pr-res">студе́нт, кото́рый прочита́л кни́гу</td>
      <td class="pr-end">kitobni oʻqib chiqqan talaba</td></tr>
  <tr><td class="pr-stem">лю́ди, живу́щие на Се́вере</td>
      <td class="pr-res">лю́ди, кото́рые живу́т на Се́вере</td>
      <td class="pr-end">Shimolda yashaydigan odamlar</td></tr>
  <tr><td class="pr-stem">по́езд, прише́дший у́тром</td>
      <td class="pr-res">по́езд, кото́рый пришёл у́тром</td>
      <td class="pr-end">ertalab kelgan poyezd</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Uslub</span>
Sifatdoshlar — <b>yozma til</b>. Gazeta, ilmiy matn, hujjat, kitob.
Ogʻzaki nutqda ruslar deyarli har doim <em>кото́рый</em> deydi.<br><br>
Sizga maslahat: <b>oʻqiganda taniy oling, yozganda ishlating,
gapirganda кото́рый deng.</b></div>

<h3>6. Sifatga aylanib qolganlari</h3>

<p>Baʼzi sifatdoshlar shu qadar koʻp ishlatilganki, endi oddiy soʻz
boʻlib qolgan:</p>

<div class="pe-ex">
  <p class="pe-ex__t">Endi bular oddiy soʻz</p>
  <p class="pe-ex__ru"><b>бу́дущий</b> год · <b>настоя́щий</b> друг ·
     <b>блестя́щая</b> иде́я · <b>подходя́щий</b> моме́нт</p>
  <p class="pe-ex__uz">kelasi yil · haqiqiy doʻst · ajoyib fikr · mos payt</p>
  <p class="pe-ex__why">Yasalishi sifatdoshniki, lekin hech kim
     ularni feʼl deb oʻylamaydi. Shunchaki yodlab oling.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>чита́ящий</s></p>
  <p class="pe-good"><b>чита́ющий</b> — «они́» shakli <em>чита́ю[т]</em>, demak <b>-ющ-</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>прочита́ющий кни́гу студе́нт</s></p>
  <p class="pe-good"><b>прочита́вший</b> — СВ feʼlida hozirgi zamon sifatdoshi yoʻq</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ма́льчик чита́ющий кни́гу мой брат.</s></p>
  <p class="pe-good">Ма́льчик<b>,</b> чита́ющий кни́гу<b>,</b> — мой брат — otdan keyin, demak vergul</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ви́дел ма́льчика, чита́ющий кни́гу.</s></p>
  <p class="pe-good">…ма́льчика, <b>чита́ющего</b> кни́гу — sifatdosh otga moslashadi (В.п.)</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Sifatdosh yasang. &nbsp; <b>рабо́тать</b> → hozirgi zamon</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>рабо́тающий</strong>.
    «Они́» shakli — <em>рабо́таю<b>т</b></em>. <b>-т</b> ni olib
    tashlaymiz, <b>-щ-</b> va sifat qoʻshimchasini qoʻshamiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Sifatdosh yasang. &nbsp; <b>прийти́</b> → oʻtgan zamon</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>прише́дший</strong>. Oʻtgan
    zamon erkak shakli — <em>пришёл</em>, unda <b>-л</b> yoʻq,
    shuning uchun <b>-ш-</b> qoʻshiladi. Bu soʻzni yodlab qoʻygan
    maʼqul.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Nega bu shakl mavjud emas? &nbsp; <s><b>напи́шущий</b></s></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><em>Написа́ть</em> — <b>СВ</b> feʼl,
    uning hozirgi zamoni yoʻq, demak hozirgi zamon sifatdoshi ham
    yoʻq. Toʻgʻri shakl — <strong>написа́вший</strong> (yozib
    chiqqan).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Vergul kerakmi? &nbsp; <b>Стоя́щий на углу́ челове́к посмотре́л
     на нас.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Kerak emas.</strong> Oborot
    <em>челове́к</em> dan <b>oldin</b> turibdi — bu oʻzbekcha
    tartib, vergulsiz. Agar otdan keyinga koʻchirsak, vergul paydo
    boʻladi: <em>Челове́к, стоя́щий на углу́, посмотре́л на
    нас.</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni <b>кото́рый</b> bilan yozing.<br>
     <b>Лю́ди, живу́щие на Се́вере, привы́кли к хо́лоду.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Лю́ди, кото́рые живу́т на
    Се́вере, привы́кли к хо́лоду.</strong> — «Shimolda yashaydigan
    odamlar sovuqqa oʻrganib qolgan». <em>Живу́щие</em> koʻplikda
    edi, demak <em>кото́рые живу́т</em>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>прича́стие</b><span>sifatdosh</span></li>
  <li><b>чита́ющий</b><span>oʻqiyotgan</span></li>
  <li><b>прочита́вший</b><span>oʻqib chiqqan</span></li>
  <li><b>живу́щий</b><span>yashayotgan</span></li>
  <li><b>прише́дший</b><span>kelgan</span></li>
  <li><b>уча́щийся</b><span>oʻquvchi, talaba</span></li>
  <li><b>бу́дущий</b><span>kelasi, boʻlajak</span></li>
  <li><b>настоя́щий</b><span>haqiqiy</span></li>
  <li><b>подходя́щий</b><span>mos, munosib</span></li>
  <li><b>привы́кнуть</b> к чему́<span>oʻrganib qolmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Причастие — feʼlning sifat kiyimi. Oʻzbekcha
        <b>-ayotgan / -gan / -adigan</b>.</li>
    <li>Hozirgi: <b>они́ shakli − т + щ</b> →
        <em>чита́ю[т] → чита́ющий</em>.</li>
    <li>Oʻtgan: <b>он shakli − л + вш</b> →
        <em>чита́[л] → чита́вший</em>. <b>-л</b> boʻlmasa —
        <b>-ш-</b>: <em>принёсший</em>.</li>
    <li><b>СВ feʼlida hozirgi zamon sifatdoshi yoʻq</b> —
        <s>прочита́ющий</s> degan soʻz mavjud emas.</li>
    <li><b>-ся hech qachon -сь boʻlmaydi</b>: <em>верну́вшийся</em>.</li>
    <li>Oborot <b>otdan keyin → vergul</b>, <b>otdan oldin →
        vergulsiz</b>.</li>
    <li>Tushunmasangiz — <b>кото́рый</b> ga yoying. Gapirganda ham
        <em>кото́рый</em> deng: sifatdosh yozma tilniki.</li>
  </ul>
</div>
""",
    },
]
