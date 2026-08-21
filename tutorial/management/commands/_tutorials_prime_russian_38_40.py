# -*- coding: utf-8 -*-
"""Prime Russian — Block D davomi (38–40).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-38 — Да́тельный yakuni: shaxssiz qurilishlar (мне хо́лодно), yosh, va
ikkita predlog — К va ПО. Bu yerda oʻzbekcha -GA ning CHEGARASI koʻrsatiladi:
«maktabga» = в шко́лу (В.п.), lekin «akamga» = к бра́ту (Д.п.).
PR-39 — Твори́тельный boshlanadi. Bu kursdagi YAGONA kelishik, uning
oʻzbekchada juftligi yoʻq. Butun dars bitta farq ustiga qurilgan: oʻzbekcha
«bilan» ruschada ikkiga boʻlinadi — vosita (predlogsiz) va hamrohlik (С).
PR-40 — Твори́тельный yakuni: кем рабо́тать / стать, va joy predloglari.

Mashqlar:        practice/management/commands/_practice_pr_38_40.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_38_40.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_38_40.py --author=prime
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
        "title": "PR-38: Дательный 2: мне холодно, ему нравится, по улице, к другу",
        "category": "russian",
        "order": 38,
        "summary": (
            "Da'telniy padejining qolgan ishlari: holat (мне хо́лодно), yosh (мне "
            "два́дцать лет) va ikkita predlog — К va ПО. Bu yerda oʻzbekcha -GA "
            "ning chegarasi ochiladi."
        ),
        "stories": ["Пе́рвая зима́"],
        "content": """
<h2>PR-38: Дательный 2: мне холодно, ему нравится, по улице, к другу</h2>

<p>Kecha siz Да́тельный'ni feʼllar bilan koʻrdingiz — <em>дать бра́ту</em>,
<em>помога́ть ма́ме</em>. Bugun uning qolgan ishlarini olamiz, va ular
orasida siz allaqachon <b>har kuni ishlatadigan</b> ikkitasi bor:
<em>мне хо́лодно</em> va <em>мне два́дцать лет</em>. Oxirida esa bir
narsani aniqlaymiz: oʻzbekcha <b>-GA</b> ruschada har doim ham Да́тельный
boʻlavermaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Holat bildirasiz: <b>мне хо́лодно, ему́ гру́стно</b></li>
    <li>Yoshni aytasiz: <b>мне два́дцать оди́н год</b></li>
    <li><b>К</b> predlogini oʻrganasiz: <b>к бра́ту, к врачу́</b></li>
    <li><b>ПО</b> predlogini oʻrganasiz: <b>по у́лице, по телефо́ну</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Holat</span>
  <span class="pe-chip pe-chip--o">Мне</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">хо́лодно</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">menga sovuq</span>
</div>

<h3>1. Holat — ega yoʻq gaplar</h3>

<p>PR-28 da bu qurilishni koʻrgan edingiz. Endi uning nomi bor: bu
<b>shaxssiz gap</b> va undagi olmosh <b>Да́тельный</b>'da turadi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Oʻzbekcha</th><th>Ruscha</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">Мне хо́лодно.</td><td class="pr-uz">Menga sovuq.</td>
      <td class="pr-res">Мне гру́стно.</td><td class="pr-uz">Menga gʻamgin.</td></tr>
  <tr><td class="pr-res">Мне жа́рко.</td><td class="pr-uz">Menga issiq.</td>
      <td class="pr-res">Мне ве́село.</td><td class="pr-uz">Menga quvnoq.</td></tr>
  <tr><td class="pr-res">Мне интере́сно.</td><td class="pr-uz">Menga qiziq.</td>
      <td class="pr-res">Ему́ тру́дно.</td><td class="pr-uz">Unga qiyin.</td></tr>
  <tr><td class="pr-res">Мне ску́чно.</td><td class="pr-uz">Menga zerikarli.</td>
      <td class="pr-res">Ей легко́.</td><td class="pr-uz">Unga oson.</td></tr>
</table></div>

<p>Zamonlar PR-27 dagidek ishlaydi — har doim <b>oʻrta jinsda</b>:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kecha</th><th>Bugun</th><th>Ertaga</th></tr>
  <tr><td class="pr-res">Мне <b>бы́ло</b> хо́лодно.</td>
      <td class="pr-end">Мне хо́лодно.</td>
      <td class="pr-uz">Мне <b>бу́дет</b> хо́лодно.</td></tr>
</table></div>

<h3>2. Yosh — bu ham Да́тельный</h3>

<p>PR-36 da siz <em>Мне два́дцать оди́н год</em> deb aytgan edingiz. Nega
<em>мне</em>? Chunki rus tilida yosh <b>Да́тельный</b> bilan aytiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--v">Ско́лько</span>
     <span class="pe-hl pe-hl--o">тебе́</span> лет?<br>
     — <span class="pe-hl pe-hl--o">Мне</span> два́дцать оди́н год. А
     <span class="pe-hl pe-hl--o">Бекзо́ду</span> де́сять.</p>
  <p class="pe-ex__uz">— Necha yoshdasan?<br>— Yigirma bir yoshdaman. Bekzod
     esa oʻn yoshda.</p>
  <p class="pe-ex__why">Otlarda ham xuddi shunday: <em>Бекзо́д<b>у</b>
     де́сять лет</em>. Soʻzma-soʻz: «Bekzodga oʻn yil».</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Yosh haqidagi gap ikkala tilda ham gʻalati, lekin <b>boshqa-boshqa</b>
gʻalati:<br>
Oʻzbekcha: <em>Men yigirma yosh<b>da</b>man</em> — «men» ega, «yoshda» —
oʻrin.<br>
Ruscha: <em><b>Мне</b> два́дцать лет</em> — ega <b>yoʻq</b>, «менга» —
joʻnalish.<br>
Yaʼni ruschada gap soʻzma-soʻz «menga yigirma yil» deyapti. Bu qurilishni
oʻylab oʻtirmang — uni butun ibora sifatida yodlang, xuddi
<em>мне хо́лодно</em> kabi.</div>

<h3>3. К — odam tomon</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Jufti (PR-35)</th></tr>
  <tr><td class="pr-res">к бра́ту</td><td class="pr-uz">akamning oldiga</td>
      <td class="pr-end">от бра́та — akamdan</td></tr>
  <tr><td class="pr-res">к врачу́</td><td class="pr-uz">shifokorga</td>
      <td class="pr-end">от врача́ — shifokordan</td></tr>
  <tr><td class="pr-res">к ба́бушке</td><td class="pr-uz">buvimning oldiga</td>
      <td class="pr-end">от ба́бушки</td></tr>
  <tr><td class="pr-res">к окну́</td><td class="pr-uz">deraza tomon</td>
      <td class="pr-end">от окна́</td></tr>
  <tr><td class="pr-res">ко мне</td><td class="pr-uz">mening oldimga</td>
      <td class="pr-end">от меня́</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana bu darsning eng muhim joyi. Oʻzbekcha <b>-GA</b> ruschada
<b>ikkiga boʻlinadi</b>, va tanlov <b>manzil odammi yoki joymi</b> degan
savolga qarab qilinadi:<br><br>
<em>maktab<b>ga</b> boraman</em> → <b>в шко́лу</b> (В.п., PR-33)<br>
<em>ish<b>ga</b> boraman</em> → <b>на рабо́ту</b> (В.п.)<br>
<em>aka<b>mga</b> boraman</em> → <b>к бра́ту</b> (Д.п., bugun)<br>
<em>shifokor<b>ga</b> boraman</em> → <b>к врачу́</b> (Д.п.)<br><br>
Qoida oddiy: <b>joy</b> boʻlsa — <em>в</em> yoki <em>на</em> +
Вини́тельный. <b>Odam</b> boʻlsa — <em>к</em> + Да́тельный.
<em>«Я иду́ к шко́ле»</em> ham mumkin, lekin u boshqa maʼno beradi:
«maktab <b>tomon</b> ketyapman» — binoning yoniga, ichiga emas.</div>

<h3>4. ПО — boʻylab</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Izoh</th></tr>
  <tr><td class="pr-res">по у́лице</td><td class="pr-uz">koʻcha boʻylab</td>
      <td class="pr-uz">harakat yoʻnalishi emas, yuza</td></tr>
  <tr><td class="pr-res">по го́роду</td><td class="pr-uz">shahar boʻylab</td>
      <td class="pr-uz">гуля́ть по го́роду — sayr qilmoq</td></tr>
  <tr><td class="pr-res">по телефо́ну</td><td class="pr-uz">telefon orqali</td>
      <td class="pr-uz">говори́ть по телефо́ну</td></tr>
  <tr><td class="pr-res">по ра́дио</td><td class="pr-uz">radio orqali</td>
      <td class="pr-uz">слу́шать по ра́дио</td></tr>
  <tr><td class="pr-res">по суббо́там</td><td class="pr-uz">shanba kunlari</td>
      <td class="pr-uz">takrorlanadigan vaqt</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ru">Мы гуля́ем <span class="pe-hl pe-hl--adv">по го́роду</span>
     и говори́м <span class="pe-hl pe-hl--adv">по телефо́ну</span>
     <span class="pe-hl pe-hl--o">с ма́мой</span>.</p>
  <p class="pe-ex__uz">Shahar boʻylab sayr qilyapmiz va telefonda onam bilan
     gaplashyapmiz.</p>
  <p class="pe-ex__why">Ikkita <em>по</em>, ikki xil maʼno: birinchisi joy
     boʻylab, ikkinchisi vosita orqali. <em>С ма́мой</em> esa keyingi
     darsning mavzusi.</p>
</div>

<h3>5. Olmoshlar predlog bilan</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Olmosh</th><th>Predlogsiz</th><th>К bilan</th><th>ПО bilan</th></tr>
  <tr><td>я</td><td class="pr-res">мне</td><td class="pr-end">ко мне</td>
      <td class="pr-uz">по мне</td></tr>
  <tr><td>ты</td><td class="pr-res">тебе́</td><td class="pr-end">к тебе́</td>
      <td class="pr-uz">по тебе́</td></tr>
  <tr><td>он</td><td class="pr-res">ему́</td><td class="pr-end">к <b>н</b>ему́</td>
      <td class="pr-uz">по <b>н</b>ему́</td></tr>
  <tr><td>она́</td><td class="pr-res">ей</td><td class="pr-end">к <b>н</b>ей</td>
      <td class="pr-uz">по <b>н</b>ей</td></tr>
  <tr><td>они́</td><td class="pr-res">им</td><td class="pr-end">к <b>н</b>им</td>
      <td class="pr-uz">по <b>н</b>им</td></tr>
</table></div>

<p><b>Ко мне</b> — <em>к</em> emas, <b>ко</b>. Bu <em>обо мне</em> (PR-31) va
<em>со мной</em> (PR-39) bilan bir xil hodisa: talaffuzni yengillashtirish
uchun predlogga unli qoʻshiladi.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я хо́лодно.</s></p>
  <p class="pe-good"><b>Мне</b> хо́лодно — bu holat, ega emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я два́дцать лет.</s></p>
  <p class="pe-good"><b>Мне</b> два́дцать лет — yosh Да́тельный bilan aytiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ к шко́лу.</s></p>
  <p class="pe-good">Я иду́ <b>в шко́лу</b> — joy uchun В + Вини́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ в бра́та.</s></p>
  <p class="pe-good">Я иду́ <b>к бра́ту</b> — odam uchun К + Да́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я говорю́ по телефо́н.</s></p>
  <p class="pe-good">Я говорю́ <b>по телефо́ну</b> — ПО ham Да́тельный oladi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu gapni ruschaga oʻgiring: <b>Menga sovuq edi.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Мне бы́ло хо́лодно.</strong>
    Shaxssiz gap, shuning uchun <em>быть</em> oʻrta jinsda — <b>бы́ло</b>,
    gapirayotgan odamning jinsidan qatʼi nazar.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>___ де́сять лет.</b> (Бекзо́д)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Бекзо́ду</strong>. Yosh Да́тельный
    bilan aytiladi — otlarda ham: erkak jins <b>-у</b> oladi. Soʻzma-soʻz:
    «Bekzodga oʻn yil».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>в</b> yoki <b>к</b>? &nbsp; <b>Я иду́ ___ шко́лу, а пото́м ___
     врачу́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в</strong> шко́лу (joy →
    Вини́тельный), <strong>к</strong> врачу́ (odam → Да́тельный). Oʻzbekcha
    ikkalasida ham <em>-ga</em>, lekin ruschada tanlov bor.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>Мы гуля́ем по ___.</b> (го́род)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>го́роду</strong>. <em>ПО</em>
    Да́тельный oladi, erkak jins esa <b>-у</b>. Maʼnosi: «shahar
    boʻylab».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Ей ску́чно. &nbsp; б) Мне два́дцать три го́да.<br>
     в) Я иду́ в бра́та. &nbsp; г) Мы говори́м по телефо́ну.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Я иду́ к бра́ту</b>. Manzil <b>odam</b> boʻlsa, <em>к</em> +
    Да́тельный ishlatiladi. <em>В</em> faqat joy uchun.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>мне хо́лодно</b><span>menga sovuq</span></li>
  <li><b>мне гру́стно</b><span>menga gʻamgin</span></li>
  <li><b>ве́село</b><span>quvnoq</span></li>
  <li><b>к бра́ту</b><span>akamning oldiga</span></li>
  <li><b>ко мне</b><span>mening oldimga</span></li>
  <li><b>по у́лице</b><span>koʻcha boʻylab</span></li>
  <li><b>по телефо́ну</b><span>telefonda</span></li>
  <li><b>врач</b><span>shifokor</span></li>
  <li><b>зима́</b><span>qish</span></li>
  <li><b>ша́рф</b><span>sharf</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Holat: <b>мне хо́лодно, ему́ гру́стно</b> — ega yoʻq, olmosh
        Да́тельный'da.</li>
    <li>Zamon: <b>мне бы́ло / мне бу́дет</b> — har doim oʻrta jinsda.</li>
    <li>Yosh ham Да́тельный: <b>мне два́дцать лет</b>, <b>Бекзо́ду
        де́сять</b>.</li>
    <li><b>К</b> + Да́тельный = odam tomon. Jufti — <b>от</b> (PR-35).</li>
    <li><b>ПО</b> + Да́тельный = boʻylab, orqali:
        <em>по у́лице, по телефо́ну</em>.</li>
    <li>Oʻzbekcha <b>-GA</b> ikkiga boʻlinadi: <b>joy</b> → в/на +
        Вини́тельный · <b>odam</b> → к + Да́тельный.</li>
    <li><b>Ко мне</b> — <em>обо мне</em>, <em>со мной</em> bilan bir xil
        hodisa.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-39: Творительный 1: чем? — vosita va «с кем?» birgalik",
        "category": "russian",
        "order": 39,
        "summary": (
            "Kursdagi yagona kelishik, uning oʻzbekchada juftligi yoʻq. Butun dars "
            "bitta farq ustiga qurilgan: oʻzbekcha «bilan» ruschada ikkiga "
            "boʻlinadi — asbob (predlogsiz) va hamroh (С bilan)."
        ),
        "stories": ["Как де́лают самсу́"],
        "content": """
<h2>PR-39: Творительный 1: чем? — vosita va «с кем?» birgalik</h2>

<p>PR-29 dagi xaritada bitta qator boʻsh qolgan edi — <b>Твори́тельный</b>.
Uning oʻzbekchada aniq juftligi yoʻq, va aynan shuning uchun u eng oxirida
oʻrgatiladi. Lekin qoʻrqmang: uning <b>maʼnosi</b> siz uchun mutlaqo tanish.
Oʻzbekcha <em>«bilan»</em> soʻzi aynan shu ishni qiladi. Butun qiyinchilik
bitta joyda: rus tili <em>«bilan»</em> ni <b>ikkiga</b> boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Qoʻshimchalarni oʻrganasiz: <b>-ом/-ем</b> va <b>-ой/-ей</b></li>
    <li>Asbobni aytasiz — <b>predlogsiz</b>: <b>писа́ть ру́чкой</b></li>
    <li>Hamrohni aytasiz — <b>С bilan</b>: <b>идти́ с бра́том</b></li>
    <li>Olmoshlarni bilasiz: <b>со мной, с тобо́й, с ним</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikkita «bilan»</span>
  <span class="pe-chip pe-chip--v">ножо́м</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">pichoq bilan (asbob)</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">с бра́том</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">akam bilan (hamroh)</span>
</div>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Savoli</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__q">что?</td>
      <td class="pr-case__word">нож</td><td class="pr-case__uz">bosh kelishik — pichoq</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Твори́тельный</td>
      <td class="pr-case__q">чем? с кем?</td>
      <td class="pr-case__word">нож<span class="pr-end">о́м</span></td>
      <td class="pr-case__uz">pichoq <b>bilan</b></td></tr>
</table></div>

<h3>1. Qoʻshimchalar</h3>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">-<span class="pr-end">ом</span> / -<span class="pr-end">ем</span></p>
    <p><em>стол → столо́м</em><br><em>брат → бра́том</em><br>
       <em>учи́тель → учи́телем</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">-<span class="pr-end">ом</span> / -<span class="pr-end">ем</span></p>
    <p><em>окно́ → окно́м</em><br><em>письмо́ → письмо́м</em><br>
       <em>мо́ре → мо́рем</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">-<span class="pr-end">ой</span> / -<span class="pr-end">ей</span></p>
    <p><em>кни́га → кни́гой</em><br><em>ма́ма → ма́мой</em><br>
       <em>Ка́тя → Ка́тей</em></p>
  </div>
</div>

<p>Erkak va oʻrta jins yana bir xil — bu blok davomida toʻrtinchi marta.
Yaʼni amalda ikkita naqsh: <b>-ом/-ем</b> va <b>-ой/-ей</b>.</p>

<h3>2. Asbob — predlogsiz</h3>

<p>«Nima bilan qilding?» degan savolga javob. Rus tilida bu yerda
<b>hech qanday predlog qoʻyilmaydi</b> — faqat qoʻshimcha:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">писа́ть ру́чкой</td><td class="pr-uz">ruchka bilan yozmoq</td></tr>
  <tr><td class="pr-res">ре́зать ножо́м</td><td class="pr-uz">pichoq bilan kesmoq</td></tr>
  <tr><td class="pr-res">есть ло́жкой</td><td class="pr-uz">qoshiq bilan yemoq</td></tr>
  <tr><td class="pr-res">де́лать рука́ми</td><td class="pr-uz">qoʻl bilan qilmoq</td></tr>
  <tr><td class="pr-res">смотре́ть глаза́ми</td><td class="pr-uz">koʻz bilan koʻrmoq</td></tr>
  <tr><td class="pr-res">е́хать авто́бусом</td><td class="pr-uz">avtobusda ketmoq</td></tr>
</table></div>

<h3>3. Hamroh — С bilan</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">идти́ с бра́том</td><td class="pr-uz">akam bilan bormoq</td></tr>
  <tr><td class="pr-res">говори́ть с ма́мой</td><td class="pr-uz">onam bilan gaplashmoq</td></tr>
  <tr><td class="pr-res">чай с са́харом</td><td class="pr-uz">shakarli choy</td></tr>
  <tr><td class="pr-res">хлеб с сы́ром</td><td class="pr-uz">pishloqli non</td></tr>
  <tr><td class="pr-res">с удово́льствием</td><td class="pr-uz">mamnuniyat bilan</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana bu darsning butun mazmuni, va uni bir marta yaxshilab oʻqing.<br><br>
Oʻzbekchada <b>bitta</b> soʻz — <em>bilan</em> — ikkala ishni ham
bajaradi:<br>
<em>pichoq <b>bilan</b> kesaman</em> · <em>akam <b>bilan</b>
boraman</em><br><br>
Ruschada esa <b>ikkita</b> qurilish bor:<br>
<em>ре́жу нож<b>о́м</b></em> — predlog <b>YOʻQ</b><br>
<em>иду́ <b>с</b> бра́т<b>ом</b></em> — predlog <b>С</b> bor<br><br>
Shuning uchun oʻzbek oʻquvchi <em>«Я пишу́ <s>с</s> ру́чкой»</em> deb
yozib yuboradi — chunki oʻzbekchada «ruchka <b>bilan</b>» deydi. Ruscha
quloqqa bu «ruchka bilan birga yozyapman, ikkalamiz» boʻlib
eshitiladi.<br><br>
<b>Tekshiruv:</b> oʻzingizdan soʻrang — bu <b>asbob</b>mi (qoʻlimda tutib
ishlatyapmanmi?) yoki <b>hamroh</b>mi (u ham men bilan birga
qilyaptimi?). Asbob — predlogsiz. Hamroh — <em>с</em> bilan.</div>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Asbob — predlogsiz</p>
    <p><em>Я ре́жу <b>ножо́м</b>.</em><br>Pichoq bilan kesaman.</p>
    <p>Pichoq — qoʻlimda. U hech narsa qilmayapti, men ishlatyapman.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Hamroh — С bilan</p>
    <p><em>Я иду́ <b>с бра́том</b>.</em><br>Akam bilan ketyapman.</p>
    <p>Akam — yonimda. U ham ketyapti, ikkalamiz birga.</p>
  </div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<em>Нож</em> bilan ikkala qurilish ham mumkin, lekin maʼnolari
butunlay boshqa:<br>
<em>Я ре́жу хлеб <b>ножо́м</b>.</em> — Nonni pichoq bilan kesyapman.
<b>(asbob)</b><br>
<em>Он пришёл <b>с ножо́м</b>.</em> — U pichoq <b>koʻtarib</b> keldi.
<b>(yonida olib)</b><br>
Ikkinchi gap ancha tashvishli eshitiladi. Predlog maʼnoni
oʻzgartiradi.</div>

<h3>4. Olmoshlar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Olmosh</th><th>Tworitelniy</th><th>С bilan</th><th>Oʻzbekcha</th></tr>
  <tr><td>я</td><td class="pr-res">мной</td><td class="pr-end">со мной</td>
      <td class="pr-uz">men bilan</td></tr>
  <tr><td>ты</td><td class="pr-res">тобо́й</td><td class="pr-end">с тобо́й</td>
      <td class="pr-uz">sen bilan</td></tr>
  <tr><td>он / оно́</td><td class="pr-res">им</td><td class="pr-end">с <b>н</b>им</td>
      <td class="pr-uz">u bilan (erkak)</td></tr>
  <tr><td>она́</td><td class="pr-res">ей</td><td class="pr-end">с <b>н</b>ей</td>
      <td class="pr-uz">u bilan (ayol)</td></tr>
  <tr><td>мы</td><td class="pr-res">на́ми</td><td class="pr-end">с на́ми</td>
      <td class="pr-uz">biz bilan</td></tr>
  <tr><td>вы</td><td class="pr-res">ва́ми</td><td class="pr-end">с ва́ми</td>
      <td class="pr-uz">siz bilan</td></tr>
  <tr><td>они́</td><td class="pr-res">и́ми</td><td class="pr-end">с <b>н</b>и́ми</td>
      <td class="pr-uz">ular bilan</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>Со мной</b> — <em>с</em> emas, <b>со</b>. Bu uchinchi marta uchrayapti:
<em><b>обо</b> мне</em> (PR-31), <em><b>ко</b> мне</em> (PR-38),
<em><b>со</b> мной</em> (bugun). Qoida bitta: <em>мне/мной</em> dan oldin
predlogga unli qoʻshiladi. Uchtasini birga yodlang — ular har doim birga
keladi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я пишу́ с ру́чкой.</s></p>
  <p class="pe-good">Я пишу́ <b>ру́чкой</b> — asbob, predlogsiz</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ бра́том.</s></p>
  <p class="pe-good">Я иду́ <b>с бра́том</b> — hamroh, С bilan</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я говорю́ с ма́ма.</s></p>
  <p class="pe-good">Я говорю́ <b>с ма́мой</b> — predlogdan keyin ham qoʻshimcha kerak</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Пойдём с я.</s></p>
  <p class="pe-good">Пойдём <b>со мной</b> — olmoshning alohida shakli bor</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ем с ло́жкой.</s></p>
  <p class="pe-good">Я ем <b>ло́жкой</b> — qoshiq asbob, hamroh emas</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>с</b> kerakmi? &nbsp; <b>Я ре́жу хлеб ___ (нож).</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ножо́м</strong> — <em>с</em>
    <b>kerak emas</b>. Pichoq — asbob, u mening qoʻlimda. Tekshiruv savoli:
    «u ham men bilan birga kesyaptimi?» — yoʻq.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>с</b> kerakmi? &nbsp; <b>Я иду́ ___ (Афсо́на).</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>с Афсо́ной</strong> — <em>с</em>
    <b>kerak</b>. Afsona — hamroh, u ham ketyapti. Ayol jinsi qoʻshimchasi
    <b>-ой</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Пойдём ___.</b> («men bilan» maʼnosida)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>со мной</strong>. Ikkita narsa:
    olmoshning alohida shakli (<em>мной</em>) va predlogga qoʻshiladigan
    unli (<em>со</em>) — xuddi <em>обо мне</em> va <em>ко мне</em>
    kabi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu ikki gapni tarjima qiling.<br>
     <b>Он ре́жет ножо́м. · Он пришёл с ножо́м.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Pichoq bilan kesyapti</strong> ·
    <strong>Pichoq koʻtarib keldi</strong>. Bitta soʻz, bitta kelishik —
    lekin predlog butun maʼnoni oʻzgartiradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Мы говори́м с учи́телем. &nbsp; б) Я пишу́ с ру́чкой.<br>
     в) Чай с са́харом. &nbsp; г) Он е́дет авто́бусом.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong>. Toʻgʻrisi —
    <b>Я пишу́ ру́чкой</b>. Ruchka — asbob, demak predlogsiz. Qolgan uchtasi
    toʻgʻri: <em>с учи́телем</em> (hamroh), <em>с са́харом</em> (qoʻshimcha
    narsa), <em>авто́бусом</em> (vosita).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>чем? с кем?</b><span>nima bilan? kim bilan?</span></li>
  <li><b>нож</b><span>pichoq</span></li>
  <li><b>ло́жка</b><span>qoshiq</span></li>
  <li><b>ру́ки → рука́ми</b><span>qoʻllar bilan</span></li>
  <li><b>ре́зать</b><span>kesmoq</span></li>
  <li><b>соль</b><span>tuz</span></li>
  <li><b>пе́рец</b><span>qalampir</span></li>
  <li><b>те́сто</b><span>xamir</span></li>
  <li><b>мука́</b><span>un</span></li>
  <li><b>с удово́льствием</b><span>mamnuniyat bilan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Erkak va oʻrta: <b>-ом / -ем</b>. Ayol: <b>-ой / -ей</b>.</li>
    <li><b>Asbob</b> — predlogsiz: <em>писа́ть ру́чкой, ре́зать
        ножо́м</em>.</li>
    <li><b>Hamroh</b> — <b>С</b> bilan: <em>идти́ с бра́том, чай с
        са́харом</em>.</li>
    <li>Oʻzbekcha <b>«bilan»</b> ikkala ishni ham qiladi — shuning uchun
        har safar oʻzingizdan soʻrang: <b>asbobmi yoki hamrohmi?</b></li>
    <li>Olmoshlar: <b>со мной, с тобо́й, с ним, с ней, с на́ми, с ва́ми,
        с ни́ми</b>.</li>
    <li><b>Со мной</b> — <em>обо мне</em> va <em>ко мне</em> bilan bir xil
        hodisa.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-40: Творительный 2: быть/стать/работать + Т.п., над, под, за, перед, между",
        "category": "russian",
        "order": 40,
        "summary": (
            "Kim boʻlib ishlaysiz, kim boʻlmoqchisiz — bu ham Tvoritelniy. Va "
            "joyni koʻrsatadigan beshta predlog. Shu dars bilan oltita kelishik "
            "toʻliq yigʻiladi."
        ),
        "stories": ["Кем ты хо́чешь стать?"],
        "content": """
<h2>PR-40: Творительный 2: быть/стать/работать + Т.п., над, под, за, перед, между</h2>

<p>Bugun oltita kelishikning oxirgisi yopiladi. Ikkita yangi ish bor va
ikkalasi ham juda koʻp ishlatiladi: <b>«kim boʻlib?»</b> —
<em>рабо́тать врачо́м</em> — va <b>joy predloglari</b> —
<em>под столо́м, за до́мом</em>. Shundan keyin PR-29 dagi xaritada boʻsh
joy qolmaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Рабо́тать кем</b> qurilishini oʻrganasiz</li>
    <li><b>Стать кем</b> bilan kelajak haqida gapirasiz</li>
    <li><b>Быть</b> ning zamonga qarab oʻzgarishini koʻrasiz</li>
    <li>Beshta joy predlogini bilasiz: <b>над, под, за, пе́ред, ме́жду</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kim boʻlib?</span>
  <span class="pe-chip pe-chip--s">Он рабо́тает</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">учи́тел<b>ем</b></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">oʻqituvchi boʻlib ishlaydi</span>
</div>

<h3>1. Рабо́тать кем — kasb haqida</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kasb</th><th>Tworitelniy</th><th>Gapda</th></tr>
  <tr><td class="pr-res">учи́тель</td><td class="pr-end">учи́телем</td>
      <td class="pr-uz">Она́ рабо́тает учи́телем.</td></tr>
  <tr><td class="pr-res">врач</td><td class="pr-end">врачо́м</td>
      <td class="pr-uz">Ма́ма рабо́тает врачо́м.</td></tr>
  <tr><td class="pr-res">инжене́р</td><td class="pr-end">инжене́ром</td>
      <td class="pr-uz">Оте́ц рабо́тает инжене́ром.</td></tr>
  <tr><td class="pr-res">води́тель</td><td class="pr-end">води́телем</td>
      <td class="pr-uz">Он рабо́тает води́телем.</td></tr>
  <tr><td class="pr-res">стро́итель</td><td class="pr-end">стро́ителем</td>
      <td class="pr-uz">Дед был стро́ителем.</td></tr>
  <tr><td class="pr-res">программи́ст</td><td class="pr-end">программи́стом</td>
      <td class="pr-uz">Брат рабо́тает программи́стом.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada bu maʼno <b>«boʻlib»</b> soʻzi bilan beriladi:<br>
<em>oʻqituvchi <b>boʻlib</b> ishlaydi</em> → <em>рабо́тает
учи́тел<b>ем</b></em><br>
<em>shifokor <b>boʻlmoqchiman</b></em> → <em>хочу́ стать
врач<b>о́м</b></em><br>
Yaʼni ikkala til ham bu yerda <b>maxsus belgi</b> qoʻyadi — oʻzbekcha
alohida soʻz bilan, ruscha esa qoʻshimcha bilan. Tushuncha bir xil:
«bu — mening doimiy holatim emas, bu — mening rolim».</div>

<h3>2. Быть — zamonga qarab oʻzgaradi</h3>

<p>Mana rus tilining chiroyli joylaridan biri. <em>Быть</em> feʼli
<b>hozirgi zamonda yoʻq</b> (PR-11), shuning uchun kasb bosh kelishikda
qoladi. Oʻtgan va kelasi zamonda esa feʼl paydo boʻladi — va u bilan birga
<b>Твори́тельный</b> ham keladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Zamon</th><th>Gap</th><th>Kasbning shakli</th></tr>
  <tr><td class="pr-uz">Hozir</td><td class="pr-res">Он учи́тель.</td>
      <td class="pr-end">bosh kelishik</td></tr>
  <tr><td class="pr-uz">Kecha</td><td class="pr-res">Он был учи́телем.</td>
      <td class="pr-end">Твори́тельный</td></tr>
  <tr><td class="pr-uz">Ertaga</td><td class="pr-res">Он бу́дет учи́телем.</td>
      <td class="pr-end">Твори́тельный</td></tr>
  <tr><td class="pr-uz">Xohish</td><td class="pr-res">Он хо́чет стать учи́телем.</td>
      <td class="pr-end">Твори́тельный</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Qoidani bir jumlada eslang: <b>feʼl bor boʻlsa — Твори́тельный, feʼl yoʻq
boʻlsa — bosh kelishik</b>. Hozirgi zamonda <em>быть</em> aytilmaydi,
demak kelishik ham kerak emas. <em>Был, бу́дет, стать, рабо́тать</em> —
hammasi feʼl, demak hammasi Твори́тельный oladi.</div>

<h3>3. Стать — kim boʻlmoqchisiz</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--v">Кем</span> ты хо́чешь
     <span class="pe-hl pe-hl--v">стать</span>?<br>
     — Я хочу́ стать <span class="pe-hl pe-hl--o">врачо́м</span>.</p>
  <p class="pe-ex__uz">— Kim boʻlmoqchisan?<br>— Shifokor boʻlmoqchiman.</p>
  <p class="pe-ex__why">Savol soʻzining oʻzi ham kelishikda: <em>кто →
     <b>кем</b></em>. Rus maktablarida bu savol har yili beriladi.</p>
</div>

<h3>4. Joy predloglari</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Predlog</th><th>Maʼnosi</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">над</td><td class="pr-uz">ustida (tegmasdan)</td>
      <td class="pr-end">над столо́м</td><td class="pr-uz">stol ustida</td></tr>
  <tr><td class="pr-res">под</td><td class="pr-uz">tagida</td>
      <td class="pr-end">под столо́м</td><td class="pr-uz">stol tagida</td></tr>
  <tr><td class="pr-res">за</td><td class="pr-uz">orqasida</td>
      <td class="pr-end">за до́мом</td><td class="pr-uz">uy orqasida</td></tr>
  <tr><td class="pr-res">пе́ред</td><td class="pr-uz">oldida</td>
      <td class="pr-end">пе́ред шко́лой</td><td class="pr-uz">maktab oldida</td></tr>
  <tr><td class="pr-res">ме́жду</td><td class="pr-uz">orasida</td>
      <td class="pr-end">ме́жду до́мом и шко́лой</td><td class="pr-uz">uy va maktab orasida</td></tr>
  <tr><td class="pr-res">ря́дом с</td><td class="pr-uz">yonida</td>
      <td class="pr-end">ря́дом с окно́м</td><td class="pr-uz">deraza yonida</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>НА</b> va <b>НАД</b> ni chalkashtirmang — ular bitta harf bilan farq
qiladi, lekin kelishiklari ham, maʼnolari ham boshqa:<br>
<em><b>на</b> стол<b>е́</b></em> (Предло́жный) — stol <b>ustida</b>, unga
tegib turibdi: kitob stolda yotibdi.<br>
<em><b>над</b> стол<b>о́м</b></em> (Твори́тельный) — stol <b>tepasida</b>,
havoda: lampa stol tepasida osilgan.<br>
Oʻzbekchada ikkalasi ham «ustida» boʻlishi mumkin, shuning uchun bu
farqni alohida eslab qolish kerak.</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Ко́шка спит <span class="pe-hl pe-hl--adv">под
     столо́м</span>, а ла́мпа виси́т <span class="pe-hl pe-hl--adv">над
     столо́м</span>.</p>
  <p class="pe-ex__uz">Mushuk stol tagida uxlayapti, lampa esa stol tepasida
     osilgan.</p>
</div>

<h3>5. Oltita kelishik — xarita toʻldi</h3>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Savoli</th><th>кни́га</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__q">кто? что?</td>
      <td class="pr-case__word">кни́га</td><td class="pr-case__uz">kitob</td></tr>
  <tr><td class="pr-case__name">Роди́тельный</td><td class="pr-case__q">чего́?</td>
      <td class="pr-case__word">кни́ги</td><td class="pr-case__uz">kitobning</td></tr>
  <tr><td class="pr-case__name">Да́тельный</td><td class="pr-case__q">чему́?</td>
      <td class="pr-case__word">кни́ге</td><td class="pr-case__uz">kitobga</td></tr>
  <tr><td class="pr-case__name">Вини́тельный</td><td class="pr-case__q">что?</td>
      <td class="pr-case__word">кни́гу</td><td class="pr-case__uz">kitobni</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Твори́тельный</td>
      <td class="pr-case__q">чем?</td>
      <td class="pr-case__word">кни́гой</td><td class="pr-case__uz">kitob bilan</td></tr>
  <tr><td class="pr-case__name">Предло́жный</td><td class="pr-case__q">о чём?</td>
      <td class="pr-case__word">о кни́ге</td><td class="pr-case__uz">kitob haqida</td></tr>
</table></div>

<p>Oʻn ikki dars oldin bu jadval <b>xarita</b> edi. Endi u — <b>siz
bilgan narsa</b>. Keyingi darslarda oʻsha oltita kelishik boshqa soʻz
turkumlariga qoʻllanadi: olmoshlar (PR-41, PR-42), sifatlar (PR-43,
PR-44) va koʻplik (PR-45, PR-46). Yangi tizim emas — <b>oʻsha tizim</b>.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Он рабо́тает учи́тель.</s></p>
  <p class="pe-good">Он рабо́тает <b>учи́телем</b> — feʼl bor, demak Твори́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он был учи́тель.</s></p>
  <p class="pe-good">Он был <b>учи́телем</b> — oʻtgan zamonda feʼl bor</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он есть учи́телем.</s></p>
  <p class="pe-good">Он <b>учи́тель</b> — hozirgi zamonda feʼl ham, kelishik ham yoʻq</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ко́шка под стол.</s></p>
  <p class="pe-good">Ко́шка <b>под столо́м</b> — joy uchun Твори́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кни́га над столе́.</s></p>
  <p class="pe-good">Кни́га <b>на столе́</b> — tegib tursa НА + Предло́жный</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Ма́ма рабо́тает ___.</b> (врач)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>врачо́м</strong>. <em>Рабо́тать</em>
    — feʼl, demak Твори́тельный. Erkak jins <b>-ом</b> oladi, va Ч dan
    keyin urgʻu ostida <b>-ом</b> yoziladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu ikki gapdan qaysi biri toʻgʻri va nega?<br>
     <b>Он учи́тель. · Он учи́телем.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Он учи́тель.</strong> Hozirgi
    zamonda <em>быть</em> aytilmaydi — feʼl yoʻq, demak kelishik ham kerak
    emas. <em>Учи́телем</em> faqat feʼl bilan keladi: <em>был учи́телем,
    рабо́тает учи́телем</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu gapni ruschaga oʻgiring: <b>Shifokor boʻlmoqchiman.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я хочу́ стать врачо́м.</strong>
    <em>Стать</em> — feʼl, demak Твори́тельный. Savolni ham eslang:
    <em>Кем ты хо́чешь стать?</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>на</b> yoki <b>над</b>? &nbsp; <b>Ла́мпа ___ столо́м, а кни́га ___
     столе́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>над</strong> столо́м,
    <strong>на</strong> столе́. Lampa havoda osilgan — <em>над</em> +
    Твори́тельный. Kitob stolga tegib turibdi — <em>на</em> +
    Предло́жный. Qoʻshimchalar ham buni koʻrsatib turibdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Ко́шка спит под столо́м. &nbsp; б) Дед был стро́ителем.<br>
     в) Он рабо́тает инжене́р. &nbsp; г) Магази́н за до́мом.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Он рабо́тает инжене́ром</b>. <em>Рабо́тать</em> feʼli Твори́тельный
    talab qiladi. Qolgan uchtasi toʻgʻri.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>кем?</b><span>kim boʻlib?</span></li>
  <li><b>стать</b><span>boʻlmoq</span></li>
  <li><b>врач</b><span>shifokor</span></li>
  <li><b>инжене́р</b><span>muhandis</span></li>
  <li><b>стро́итель</b><span>quruvchi</span></li>
  <li><b>над</b><span>ustida (tegmasdan)</span></li>
  <li><b>под</b><span>tagida</span></li>
  <li><b>за</b><span>orqasida</span></li>
  <li><b>пе́ред</b><span>oldida</span></li>
  <li><b>ме́жду</b><span>orasida</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Рабо́тать / стать / быть</b> + Твори́тельный:
        <em>рабо́тает врачо́м</em>.</li>
    <li>Qoida: <b>feʼl bor — Твори́тельный, feʼl yoʻq — bosh
        kelishik</b>. <em>Он учи́тель</em>, lekin <em>Он был
        учи́телем</em>.</li>
    <li>Savol soʻzi ham oʻzgaradi: <b>кто → кем</b>.</li>
    <li>Joy predloglari: <b>над, под, за, пе́ред, ме́жду, ря́дом с</b> —
        hammasi Твори́тельный.</li>
    <li><b>НА</b> (tegib turibdi, Предло́жный) va <b>НАД</b> (havoda,
        Твори́тельный) — bitta harf, boshqa kelishik.</li>
    <li>Oltita kelishik toʻliq yigʻildi. Keyingi darslar — <b>oʻsha
        tizim</b>, boshqa soʻz turkumlarida.</li>
  </ul>
</div>
""",
    },
]
