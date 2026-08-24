# -*- coding: utf-8 -*-
"""Prime Russian — Block E davomi (56–58): harakat feʼllari.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-56 — qolgan harakat juftliklari. Mantiq PR-55 dagining oʻzi, faqat
juftliklar sakkizta. Yangi narsa: НЕСТИ/НОСИТЬ turkumi (nimadir olib
yurish) va носи́ть ning ikkinchi maʼnosi — «kiymoq».
PR-57 — prefikslar. Bu yerda kursning eng chiroyli tizimli fakti ochiladi:
prefiks + ИДТИ = СВ, prefiks + ХОДИТЬ = НСВ. Yaʼni PR-52 (vid) va PR-55
(harakat) bitta joyda birlashadi.
PR-58 — maʼnoni oʻzgartiradigan prefikslar, va ular orasida НАЙТИ =
на + идти. Bu oʻquvchiga tizimning ichki mantiqini koʻrsatadi.

Mashqlar:        practice/management/commands/_practice_pr_56_58.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_56_58.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_56_58.py --author=prime
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
        "title": "PR-56: Harakat feʼllari 2: ехать/ездить, бежать/бегать, лететь/летать, нести/носить",
        "category": "russian",
        "order": 56,
        "summary": (
            "Kecha bitta juftlikni oʻrgandingiz. Aslida ular sakkizta — lekin "
            "mantiq bitta va u oʻzgarmaydi: bir tomonga yoki muntazam."
        ),
        "stories": ["Транссиб: семь дней в поезде"],
        "content": """
<h2>PR-56: Harakat feʼllari 2: ехать/ездить, бежать/бегать, лететь/летать, нести/носить</h2>

<p>PR-55 da siz <em>идти́ ↔ ходи́ть</em> juftligini oʻrgandingiz. Endi yaxshi
xabar: rus tilida bunday juftliklar <b>sakkizta</b>, va ularning
<b>hammasi bir xil mantiqda</b> ishlaydi. Yaʼni siz qoidani bir marta
oʻrgandingiz — bugun uni yettita yangi soʻzga qoʻllaysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Sakkizta juftlikni bir jadvalda koʻrasiz</li>
    <li><b>Е́хать ↔ е́здить</b> ni ishlatasiz — eng koʻp kerak boʻladigan juftlik</li>
    <li><b>Нести́ ↔ носи́ть</b> turkumini oʻrganasiz</li>
    <li><b>Носи́ть</b> ning ikkinchi maʼnosini bilasiz: «kiymoq»</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Bitta mantiq</span>
  <span class="pe-chip pe-chip--v">bir tomonga, hozir</span>
  <span class="pe-op">↔</span>
  <span class="pe-chip pe-chip--o">muntazam / borib-kelish</span>
</div>

<h3>1. Sakkizta juftlik</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Bir tomonga</th><th>Muntazam</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">идти́</td><td class="pr-end">ходи́ть</td>
      <td class="pr-uz">piyoda yurmoq</td></tr>
  <tr><td class="pr-res">е́хать</td><td class="pr-end">е́здить</td>
      <td class="pr-uz">transportda ketmoq</td></tr>
  <tr><td class="pr-res">бежа́ть</td><td class="pr-end">бе́гать</td>
      <td class="pr-uz">yugurmoq</td></tr>
  <tr><td class="pr-res">лете́ть</td><td class="pr-end">лета́ть</td>
      <td class="pr-uz">uchmoq</td></tr>
  <tr><td class="pr-res">плыть</td><td class="pr-end">пла́вать</td>
      <td class="pr-uz">suzmoq</td></tr>
  <tr><td class="pr-res">нести́</td><td class="pr-end">носи́ть</td>
      <td class="pr-uz">olib yurmoq (qoʻlda)</td></tr>
  <tr><td class="pr-res">везти́</td><td class="pr-end">вози́ть</td>
      <td class="pr-uz">olib yurmoq (transportda)</td></tr>
  <tr><td class="pr-res">вести́</td><td class="pr-end">води́ть</td>
      <td class="pr-uz">boshlab bormoq; haydamoq</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Jadvaldagi naqshni payqang: chap ustunda soʻzlar <b>qisqaroq</b> va
koʻpincha <b>-ти</b> yoki <b>-ть</b> ga tugaydi; oʻng ustunda ular
<b>uzunroq</b> va <b>-ить / -ать</b> oladi.<br><br>
Va ikkalasi ham <b>НСВ</b> — bu vid emas, yoʻnalish. Buni unutmang:
<em>ходи́л</em> tugagan safarni bildirsa ham, u <b>СВ emas</b>.</div>

<h3>2. Е́хать ↔ е́здить</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>е́хать</th><th>е́здить</th></tr>
  <tr><td>я</td><td class="pr-res">е́ду</td><td class="pr-end">е́зжу</td></tr>
  <tr><td>ты</td><td class="pr-res">е́дешь</td><td class="pr-end">е́здишь</td></tr>
  <tr><td>он / она́</td><td class="pr-res">е́дет</td><td class="pr-end">е́здит</td></tr>
  <tr><td>они́</td><td class="pr-res">е́дут</td><td class="pr-end">е́здят</td></tr>
  <tr><td class="pr-uz">oʻtgan zamon</td><td class="pr-res">е́хал</td>
      <td class="pr-end">е́здил</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ru">Сейча́с я <span class="pe-hl pe-hl--v">е́ду</span> на
     рабо́ту. Я <span class="pe-hl pe-hl--o">е́зжу</span> на рабо́ту на
     метро́ ка́ждый день.</p>
  <p class="pe-ex__uz">Hozir ishga ketyapman. Har kuni ishga metroda borib
     turaman.</p>
  <p class="pe-ex__why">Bir gapda ikkalasi ham: <em>е́ду</em> — hozir
     yoʻldaman; <em>е́зжу</em> — muntazam odat.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Ле́том я
     <span class="pe-hl pe-hl--o">е́здил</span> в Самарка́нд.</p>
  <p class="pe-ex__uz">Yozda Samarqandga borib keldim.</p>
  <p class="pe-ex__why">Oʻtgan zamonda <em>е́здил</em> — <b>borib-kelish</b>,
     xuddi <em>ходи́л</em> kabi. Agar <em>е́хал</em> boʻlsa, gap yoʻl haqida
     boʻlardi: «ketayotgan edim».</p>
</div>

<h3>3. Нести́ ↔ носи́ть — nimadir olib yurish</h3>

<p>Bu turkum biroz boshqacha: unda <b>obyekt</b> bor — nimanidir olib
yuriladi. Lekin mantiq oʻsha:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gap</th><th>Maʼnosi</th><th>Nima uchun</th></tr>
  <tr><td class="pr-res">Я несу́ кни́ги.</td><td class="pr-end">Kitoblarni olib ketyapman.</td>
      <td class="pr-uz">hozir, bir tomonga</td></tr>
  <tr><td class="pr-res">Я ношу́ кни́ги в шко́лу.</td><td class="pr-end">Kitoblarni maktabga olib borib turaman.</td>
      <td class="pr-uz">har kuni</td></tr>
  <tr><td class="pr-res">Он вёз хлеб на ры́нок.</td><td class="pr-end">Nonni bozorga olib ketayotgan edi.</td>
      <td class="pr-uz">transportda, bir tomonga</td></tr>
  <tr><td class="pr-res">Он во́зит хлеб ка́ждое у́тро.</td><td class="pr-end">Har kuni ertalab non tashiydi.</td>
      <td class="pr-uz">muntazam</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Носи́ть</b> ning ikkinchi, juda koʻp ishlatiladigan maʼnosi bor —
<b>«kiymoq»</b>:<br>
<em>Она́ <b>но́сит</b> очки́.</em> — U koʻzoynak taqadi.<br>
<em>Зимо́й я <b>ношу́</b> ша́пку.</em> — Qishda qalpoq kiyaman.<br>
Bu mantiqan tushunarli: kiyim — bu doim oʻzing bilan olib yurgan narsa.
Faqat <em>носи́ть</em> shu maʼnoda; <em>нести́</em> emas.<br><br>
Va yana bir tuzoq: <b>вожу́</b> ikki feʼlga tegishli —
<em>вози́ть</em> (tashimoq) va <em>води́ть</em> (haydamoq). Farqni gap
koʻrsatadi: <em>вожу́ дете́й в шко́лу</em> (tashiyman) va <em>вожу́
маши́ну</em> (mashina haydayman).</div>

<h3>4. Лете́ть ↔ лета́ть, бежа́ть ↔ бе́гать</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gap</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Самолёт лети́т в Москву́.</td>
      <td class="pr-end">Samolyot Moskvaga uchyapti (hozir).</td></tr>
  <tr><td class="pr-res">Он лета́ет в Москву́ ча́сто.</td>
      <td class="pr-end">U Moskvaga tez-tez uchib turadi.</td></tr>
  <tr><td class="pr-res">Ребёнок бежи́т к ма́ме.</td>
      <td class="pr-end">Bola onasiga qarab yugurib kelyapti.</td></tr>
  <tr><td class="pr-res">Он бе́гает ка́ждое у́тро.</td>
      <td class="pr-end">U har kuni ertalab yuguradi (sport).</td></tr>
</table></div>

<p><em>Бежа́ть</em> ni alohida eslang — u <b>aralash tuslanadi</b>:
<em>бегу́, бежи́шь, бежи́т, бежи́м, бежи́те, <b>бегу́т</b></em>. Yaʼni
birinchi va oxirgi shaklda <b>Г</b>, oʻrtada <b>Ж</b> — xuddi
<em>мочь</em> kabi (PR-26).</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
PR-55 dagi solishtiruv bu yerda ham toʻliq ishlaydi — faqat endi u
<b>sakkizta juftlikka</b> qoʻllanadi:<br><br>
<em>ket<b>yapman</b></em> → <b>е́ду</b> · <em>bor<b>ib turaman</b></em> →
<b>е́зжу</b> · <em>bor<b>ib keldim</b></em> → <b>е́здил</b><br>
<em>uch<b>yapti</b></em> → <b>лети́т</b> · <em>uch<b>ib turadi</b></em> →
<b>лета́ет</b><br>
<em>olib ket<b>yapman</b></em> → <b>несу́</b> · <em>olib bor<b>ib
turaman</b></em> → <b>ношу́</b><br><br>
Yaʼni oʻzbekcha bu farqni <b>qoʻshimcha feʼl</b> bilan koʻrsatadi
(<em>turmoq, kelmoq</em>), ruscha esa <b>alohida soʻz</b> bilan. Ikkala
tilda ham farq bor — faqat vosita boshqa.<br><br>
Va <em>носи́ть</em> ning «kiymoq» maʼnosi ham tanish: oʻzbekchada ham
«koʻzoynak <b>taqib yuradi</b>» deyiladi — «yuradi» soʻzi bilan.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Ка́ждый день я е́ду на рабо́ту.</s></p>
  <p class="pe-good">Ка́ждый день я <b>е́зжу</b> — takror koʻp yoʻnalish</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ле́том я е́хал в Самарка́нд и верну́лся.</s></p>
  <p class="pe-good">Ле́том я <b>е́здил</b> в Самарка́нд — borib-kelish</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Она́ несёт очки́.</s> <em>(«taqadi» maʼnosida)</em></p>
  <p class="pe-good">Она́ <b>но́сит</b> очки́ — kiyim uchun faqat <em>носи́ть</em></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Они́ бежа́т в парк ка́ждое у́тро.</s></p>
  <p class="pe-good">Они́ <b>бе́гают</b> ка́ждое у́тро — takror; va shakl <em>бегу́т</em></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>е́ду</b> yoki <b>е́зжу</b>? &nbsp; <b>Ка́ждый день я ___ на рабо́ту
     на метро́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>е́зжу</strong>. «Ка́ждый день» —
    takror, demak koʻp yoʻnalish. Oʻzbekcha: «borib turaman».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>е́хал</b> yoki <b>е́здил</b>? &nbsp; <b>Ле́том я ___ в дере́вню к
     ба́бушке.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>е́здил</strong> — bordim va
    qaytdim. <em>Е́хал</em> boʻlsa, gap yoʻl haqida boʻlardi:
    «ketayotgan edim».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Зимо́й я ___ ша́пку.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ношу́</strong>. Kiyim uchun har
    doim <em>носи́ть</em> — bu uning ikkinchi maʼnosi. <em>Несу́</em>
    «qoʻlimda olib ketyapman» degan boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>вожу́</b> ikki feʼlga tegishli. Qaysilarga?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>вози́ть</strong> (tashimoq) va
    <strong>води́ть</strong> (haydamoq). Farqni gap koʻrsatadi:
    <em>вожу́ дете́й в шко́лу</em> va <em>вожу́ маши́ну</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Самолёт лети́т в Москву́. &nbsp; б) Он лета́ет ча́сто.<br>
     в) Ка́ждый день я е́ду на рабо́ту. &nbsp; г) Он бе́гает по утра́м.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>я е́зжу на рабо́ту</b>. «Ка́ждый день» takrorni bildiradi, demak
    koʻp yoʻnalish kerak.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>е́хать → е́ду, е́хал</b><span>ketmoq (hozir, transportda)</span></li>
  <li><b>е́здить → е́зжу, е́здил</b><span>borib turmoq; borib kelmoq</span></li>
  <li><b>лете́ть / лета́ть</b><span>uchmoq</span></li>
  <li><b>бежа́ть / бе́гать</b><span>yugurmoq</span></li>
  <li><b>плыть / пла́вать</b><span>suzmoq</span></li>
  <li><b>нести́ / носи́ть</b><span>olib yurmoq; kiymoq</span></li>
  <li><b>везти́ / вози́ть</b><span>tashimoq</span></li>
  <li><b>по́езд</b><span>poyezd</span></li>
  <li><b>ваго́н</b><span>vagon</span></li>
  <li><b>проводни́к</b><span>vagon xodimi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Sakkizta juftlik, <b>bitta mantiq</b>: bir tomonga ↔ muntazam.</li>
    <li>Ikkala shakl ham <b>НСВ</b> — bu vid emas, yoʻnalish.</li>
    <li><b>Е́хал</b> = yoʻlda edim · <b>е́здил</b> = borib keldim.</li>
    <li><b>Носи́ть</b> = kiymoq ham: <em>но́сит очки́</em>.</li>
    <li><b>Вожу́</b> ikki feʼldan: <em>вози́ть</em> (tashimoq) va
        <em>води́ть</em> (haydamoq).</li>
    <li><b>Бежа́ть</b> aralash tuslanadi: <em>бегу́ … бежи́шь …
        бегу́т</em>.</li>
    <li>Oʻzbekcha farqni qoʻshimcha feʼl bilan, ruscha alohida soʻz bilan
        koʻrsatadi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-57: Harakat feʼllarining prefikslari: при-, у-, вы-, в-, до-, пере-, под-, от-",
        "category": "russian",
        "order": 57,
        "summary": (
            "Bitta feʼl va sakkizta prefiks — oʻn oltita yangi soʻz. Va bu yerda "
            "kursning eng chiroyli fakti ochiladi: prefiks + ИДТИ = СВ, prefiks + "
            "ХОДИТЬ = НСВ."
        ),
        "stories": ["Один глагол, десять дверей"],
        "content": """
<h2>PR-57: Harakat feʼllarining prefikslari: при-, у-, вы-, в-, до-, пере-, под-, от-</h2>

<p>Bugun rus tilining eng tejamkor tomoni ochiladi. Bitta feʼl —
<em>идти́</em> — va sakkizta prefiks. Natijada <b>oʻn oltita yangi
soʻz</b>. Va ular tasodifiy emas: har bir prefiks aniq bir <b>yoʻnalish</b>
bildiradi, va bu maʼnolar boshqa feʼllarda ham xuddi shunday
ishlaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Sakkizta prefiksning maʼnosini oʻrganasiz</li>
    <li>Vid qoidasini bilasiz: <b>идти́ → СВ</b>, <b>ходи́ть → НСВ</b></li>
    <li>Oʻsha prefikslarni <b>е́хать</b> bilan ishlatasiz</li>
    <li><b>Вы́-</b> ning urgʻu xususiyatini eslab qolasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Tizim</span>
  <span class="pe-chip pe-chip--v">prefiks + идти́ = СВ</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">prefiks + ходи́ть = НСВ</span>
</div>

<h3>1. Sakkizta prefiks</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Prefiks</th><th>Maʼnosi</th><th>СВ (идти́)</th><th>НСВ (ходи́ть)</th></tr>
  <tr><td class="pr-res">при-</td><td class="pr-uz">kelmoq (yetib kelish)</td>
      <td class="pr-end">прийти́</td><td class="pr-end">приходи́ть</td></tr>
  <tr><td class="pr-res">у-</td><td class="pr-uz">ketmoq (uzoqlashish)</td>
      <td class="pr-end">уйти́</td><td class="pr-end">уходи́ть</td></tr>
  <tr><td class="pr-res">в- / во-</td><td class="pr-uz">kirmoq</td>
      <td class="pr-end">войти́</td><td class="pr-end">входи́ть</td></tr>
  <tr><td class="pr-res">вы-</td><td class="pr-uz">chiqmoq</td>
      <td class="pr-end">вы́йти</td><td class="pr-end">выходи́ть</td></tr>
  <tr><td class="pr-res">до-</td><td class="pr-uz">yetib bormoq</td>
      <td class="pr-end">дойти́</td><td class="pr-end">доходи́ть</td></tr>
  <tr><td class="pr-res">пере-</td><td class="pr-uz">kesib oʻtmoq</td>
      <td class="pr-end">перейти́</td><td class="pr-end">переходи́ть</td></tr>
  <tr><td class="pr-res">под-</td><td class="pr-uz">yaqinlashmoq</td>
      <td class="pr-end">подойти́</td><td class="pr-end">подходи́ть</td></tr>
  <tr><td class="pr-res">от-</td><td class="pr-uz">uzoqlashmoq (bir oz)</td>
      <td class="pr-end">отойти́</td><td class="pr-end">отходи́ть</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Mana bugungi darsning eng muhim fakti, va u butun tizimni bogʻlaydi:<br>
Prefiks <b>идти́</b> ga qoʻshilsa — <b>СВ</b> chiqadi (<em>прийти́,
уйти́, войти́</em>).<br>
Oʻsha prefiks <b>ходи́ть</b> ga qoʻshilsa — <b>НСВ</b> chiqadi
(<em>приходи́ть, уходи́ть, входи́ть</em>).<br><br>
Yaʼni PR-52 (vid juftliklari) va PR-55 (harakat feʼllari) shu yerda
<b>birlashadi</b>. Bitta prefiks — bitta vid jufti. Sakkizta prefiks —
sakkizta juftlik.</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Он <span class="pe-hl pe-hl--v">прихо́дит</span>
     ка́ждый день в во́семь. Сего́дня он
     <span class="pe-hl pe-hl--o">пришёл</span> в де́вять.</p>
  <p class="pe-ex__uz">U har kuni soat sakkizda keladi. Bugun toʻqqizda
     keldi.</p>
  <p class="pe-ex__why">Birinchisi — takror (<b>НСВ</b>, <em>ходи́ть</em>
     dan), ikkinchisi — bir marta tugagan ish (<b>СВ</b>, <em>идти́</em>
     dan).</p>
</div>

<h3>2. Ular qanday ishlaydi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gap</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Он пришёл домо́й.</td><td class="pr-end">Uyga keldi.</td></tr>
  <tr><td class="pr-res">Он ушёл домо́й.</td><td class="pr-end">Uyga ketdi (bu yerdan).</td></tr>
  <tr><td class="pr-res">Он вошёл в дом.</td><td class="pr-end">Uyga kirdi.</td></tr>
  <tr><td class="pr-res">Он вы́шел из до́ма.</td><td class="pr-end">Uydan chiqdi.</td></tr>
  <tr><td class="pr-res">Он дошёл до шко́лы.</td><td class="pr-end">Maktabgacha yetib bordi.</td></tr>
  <tr><td class="pr-res">Он перешёл у́лицу.</td><td class="pr-end">Koʻchani kesib oʻtdi.</td></tr>
  <tr><td class="pr-res">Он подошёл к окну́.</td><td class="pr-end">Deraza oldiga keldi.</td></tr>
  <tr><td class="pr-res">Он отошёл от окна́.</td><td class="pr-end">Derazadan uzoqlashdi.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Prefikslar <b>predloglar bilan juftlashadi</b>, va bu tasodif emas —
koʻpincha ular bir xil soʻz:<br>
<em><b>в</b>ойти́ <b>в</b> дом</em> · <em><b>вы</b>йти <b>из</b> до́ма</em>
· <em><b>до</b>йти́ <b>до</b> шко́лы</em> · <em><b>под</b>ойти́
<b>к</b> окну́</em> · <em><b>от</b>ойти́ <b>от</b> окна́</em><br><br>
Yaʼni prefiksni bilsangiz, predlogni ham deyarli bilasiz. Ularni
<b>juftlab</b> yodlang.</div>

<h3>3. Вы- ning urgʻu xususiyati</h3>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Вы-</b> prefiksi СВ feʼllarda <b>doim urgʻuli</b> boʻladi:<br>
<em><b>вы́</b>йти, <b>вы́</b>шел, <b>вы́</b>йду</em> — urgʻu boshida.<br>
Lekin НСВ shaklda urgʻu odatdagi joyda: <em>выход<b>и́</b>ть,
выхож<b>у́</b></em>.<br><br>
Bu qoida boshqa СВ feʼllarga ham tegishli: <em><b>вы́</b>учить</em>,
<em><b>вы́</b>брать</em>, <em><b>вы́</b>пить</em>. Agar soʻzda
<em>вы-</em> boʻlsa va u СВ boʻlsa — urgʻu deyarli har doim shu
yerda.</div>

<h3>4. Oʻsha prefikslar е́хать bilan</h3>

<p>Prefikslar <b>hamma harakat feʼliga</b> qoʻshiladi — maʼnosi
oʻzgarmaydi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Prefiks</th><th>СВ (е́хать)</th><th>НСВ (е́здить)</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">при-</td><td class="pr-end">прие́хать</td>
      <td class="pr-end">приезжа́ть</td><td class="pr-uz">yetib kelmoq</td></tr>
  <tr><td class="pr-res">у-</td><td class="pr-end">уе́хать</td>
      <td class="pr-end">уезжа́ть</td><td class="pr-uz">ketib qolmoq</td></tr>
  <tr><td class="pr-res">вы-</td><td class="pr-end">вы́ехать</td>
      <td class="pr-end">выезжа́ть</td><td class="pr-uz">chiqib ketmoq</td></tr>
  <tr><td class="pr-res">до-</td><td class="pr-end">дое́хать</td>
      <td class="pr-end">доезжа́ть</td><td class="pr-uz">yetib bormoq</td></tr>
  <tr><td class="pr-res">пере-</td><td class="pr-end">перее́хать</td>
      <td class="pr-end">переезжа́ть</td><td class="pr-uz">koʻchib oʻtmoq</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
НСВ shakl <em>е́здить</em> dan emas, <b>-езжа́ть</b> dan yasaladi:
<em>приезжа́ть</em>, <em>уезжа́ть</em> — <em>«приездить»</em> emas. Bu
kichkina, lekin muhim tafsilot.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu yerda ikki til <b>butunlay boshqa yoʻldan boradi</b> — va buni koʻrish
foydali.<br><br>
Oʻzbek tilida bu maʼnolar uchun <b>alohida feʼllar</b> bor:<br>
<em>kelmoq</em> · <em>ketmoq</em> · <em>kirmoq</em> · <em>chiqmoq</em> ·
<em>oʻtmoq</em> · <em>yaqinlashmoq</em> · <em>yetib bormoq</em><br>
Yettita boshqa-boshqa oʻzak. Ularning bir-biri bilan aloqasi yoʻq.<br><br>
Rus tilida esa <b>bitta oʻzak</b> va sakkizta prefiks:
<em>-йти</em> → <em>прийти́, уйти́, войти́, вы́йти, дойти́, перейти́,
подойти́, отойти́</em>.<br><br>
Bu boshda qiyinroq (prefikslarni yodlash kerak), lekin keyin
<b>ancha osonroq</b>: prefikslarni bir marta oʻrgansangiz, ular
<b>hamma</b> harakat feʼlida ishlaydi. <em>При-</em> ni bilsangiz,
<em>прийти́, прие́хать, прилете́ть, принести́</em> — hammasi
tushunarli.<br><br>
Oʻzbekchada esa har bir yangi harakat uchun yangi soʻz yodlash kerak edi.
Yaʼni ruscha tizim <b>tejamkorroq</b> — faqat uni ochish uchun bir oz
vaqt ketadi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Он приходи́л вчера́ в во́семь.</s> <em>(bir marta maʼnosida)</em></p>
  <p class="pe-good">Он <b>пришёл</b> вчера́ в во́семь — bir marta, tugagan ish</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он пришёл ка́ждый день.</s></p>
  <p class="pe-good">Он <b>приходи́л</b> ка́ждый день — takror НСВ talab qiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он вы́шел в до́ма.</s></p>
  <p class="pe-good">Он вы́шел <b>из</b> до́ма — <em>вы-</em> prefiksi <em>из</em> bilan juftlashadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы приезди́м за́втра.</s></p>
  <p class="pe-good">Мы <b>приезжа́ем</b> за́втра — НСВ <em>-езжа́ть</em> dan yasaladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он вышёл из до́ма.</s></p>
  <p class="pe-good">Он <b>вы́шел</b> — <em>вы-</em> СВ da har doim urgʻuli</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>прийти́</b> va <b>приходи́ть</b> — qaysi biri СВ?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Прийти́</strong> — u
    <em>идти́</em> dan yasalgan. <em>Приходи́ть</em> esa <em>ходи́ть</em>
    dan, demak НСВ. Qoida: <b>идти́ → СВ, ходи́ть → НСВ</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Он ___ ка́ждый день в во́семь.</b>
     (прийти́ / приходи́ть)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>прихо́дит</strong>. «Ка́ждый
    день» — takror, demak НСВ. Bir marta boʻlsa: <em>пришёл</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu prefikslarga qaysi predloglar juftlashadi?<br>
     <b>вы- · до- · под-</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>из · до · к</strong>:
    <em>вы́йти <b>из</b> до́ма</em>, <em>дойти́ <b>до</b> шко́лы</em>,
    <em>подойти́ <b>к</b> окну́</em>. Prefiks va predlog koʻpincha bir xil
    maʼnoni takrorlaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>вы́йти</b> soʻzida urgʻu qayerda?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Вы-</strong> da:
    <em>вы́йти, вы́шел, вы́йду</em>. СВ feʼllarda <em>вы-</em> har doim
    urgʻuli. НСВ da esa oddiy: <em>выходи́ть</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Он вошёл в дом. &nbsp; б) Он вы́шел из до́ма.<br>
     в) Мы приезди́м за́втра. &nbsp; г) Он подошёл к окну́.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Мы приезжа́ем за́втра</b>. <em>Е́здить</em> ning prefiksli НСВ
    shakli <em>-езжа́ть</em> dan yasaladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>прийти́ / приходи́ть</b><span>kelmoq</span></li>
  <li><b>уйти́ / уходи́ть</b><span>ketmoq</span></li>
  <li><b>войти́ / входи́ть</b><span>kirmoq</span></li>
  <li><b>вы́йти / выходи́ть</b><span>chiqmoq</span></li>
  <li><b>дойти́ / доходи́ть</b><span>yetib bormoq</span></li>
  <li><b>перейти́ / переходи́ть</b><span>kesib oʻtmoq</span></li>
  <li><b>подойти́ / подходи́ть</b><span>yaqinlashmoq</span></li>
  <li><b>отойти́ / отходи́ть</b><span>uzoqlashmoq</span></li>
  <li><b>приста́вка</b><span>prefiks</span></li>
  <li><b>дверь</b><span>eshik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Prefiks + идти́ = СВ</b>, <b>prefiks + ходи́ть = НСВ</b>. Bu
        qoida butun tizimni bogʻlaydi.</li>
    <li>Sakkizta prefiks: <b>при-, у-, в-, вы-, до-, пере-, под-,
        от-</b>.</li>
    <li>Prefiks va predlog juftlashadi: <em>вы́йти из</em>, <em>дойти́
        до</em>, <em>подойти́ к</em>.</li>
    <li><b>Вы-</b> СВ da har doim urgʻuli: <em>вы́шел</em>.</li>
    <li>Е́хать bilan НСВ <b>-езжа́ть</b> dan yasaladi:
        <em>приезжа́ть</em>.</li>
    <li>Oʻzbekchada bular <b>alohida feʼllar</b>, ruschada esa bitta oʻzak
        va prefikslar — tejamkorroq tizim.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-58: Prefikslar maʼnoni qanday oʻzgartiradi: по-, за-, про-, раз-, с-, на-",
        "category": "russian",
        "order": 58,
        "summary": (
            "Baʼzi prefikslar yoʻnalish emas, boshqa narsa qoʻshadi: boshlanish, "
            "qisqa toʻxtash, oʻtib ketish. Va ular orasida bitta ajoyibi bor — "
            "НАЙТИ aslida «на + идти»."
        ),
        "stories": ["Кот ушёл и пришёл"],
        "content": """
<h2>PR-58: Prefikslar maʼnoni qanday oʻzgartiradi: по-, за-, про-, раз-, с-, на-</h2>

<p>Kecha sakkizta prefiks yoʻnalish bildirardi: qayerga, qayerdan.
Bugungi prefikslar boshqacha ishlaydi — ular <b>yoʻnalish emas, harakatning
xarakterini</b> oʻzgartiradi: boshlanishmi, qisqa tashrifmi, oʻtib
ketishmi. Va ular orasida bitta soʻz bor, uni koʻrgach rus tili
sizga boshqacha koʻrinadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>По-</b> bilan harakat boshlanishini bildirasiz</li>
    <li><b>За-</b> bilan «yoʻl-yoʻlakay kirish» ni aytasiz</li>
    <li><b>Про-</b>, <b>с-</b>, <b>раз-</b> maʼnolarini bilasiz</li>
    <li><b>Найти́</b> qayerdan kelganini koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Boshqa turdagi prefikslar</span>
  <span class="pe-chip pe-chip--v">пойти́ = yoʻlga chiqmoq</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">зайти́ = kirib oʻtmoq</span>
</div>

<h3>1. По- — harakatning boshlanishi</h3>

<p>Bu eng koʻp ishlatiladigan prefiks. U «yoʻlga chiqdi» degan maʼnoni
beradi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Gap</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Он пошёл в шко́лу.</td>
      <td class="pr-end">Maktabga joʻnadi (yoʻlga chiqdi).</td></tr>
  <tr><td class="pr-res">Я пошёл!</td>
      <td class="pr-end">Men ketdim! (xayrlashuv)</td></tr>
  <tr><td class="pr-res">Пое́хали!</td>
      <td class="pr-end">Ketdik!</td></tr>
  <tr><td class="pr-res">По́сле уро́ка мы пойдём домо́й.</td>
      <td class="pr-end">Darsdan keyin uyga ketamiz.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<b>Пойти́</b> — bu <em>идти́</em> ning eng koʻp ishlatiladigan СВ jufti.
Uni alohida yodlang, chunki u har kuni kerak: <em>Я пошёл</em>,
<em>пойдём</em>, <em>пойдёшь?</em>, <em>пое́хали</em>.<br><br>
Farqni sezing: <em>Я <b>иду́</b> в шко́лу</em> — hozir yoʻldaman.
<em>Я <b>пошёл</b> в шко́лу</em> — endi yoʻlga chiqdim, ketdim.</div>

<h3>2. За- — yoʻl-yoʻlakay kirish</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">По доро́ге домо́й я
     <span class="pe-hl pe-hl--v">зашёл</span> в магази́н.</p>
  <p class="pe-ex__uz">Uyga ketayotib doʻkonga kirib oʻtdim.</p>
  <p class="pe-ex__why"><b>За-</b> — asosiy yoʻlni buzmasdan, qisqa vaqtga
     kirish. Bu <em>войти́</em> dan farq qiladi: <em>войти́</em> shunchaki
     «kirmoq», <em>зайти́</em> esa «kirib chiqmoq».</p>
</div>

<p>Xuddi shu maʼnoda: <em>Заходи́!</em> — «kir!» (mehmonni chaqirish),
<em>Я зайду́ ве́чером</em> — «kechqurun kirib oʻtaman».</p>

<h3>3. Про-, с-, раз-</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Prefiks</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-res">про-</td><td class="pr-uz">oʻtib ketmoq; bosib oʻtmoq</td>
      <td class="pr-end">Он прошёл ми́мо. · Мы прошли́ два киломе́тра.</td></tr>
  <tr><td class="pr-res">с-</td><td class="pr-uz">pastga tushmoq</td>
      <td class="pr-end">Он сошёл с ле́стницы.</td></tr>
  <tr><td class="pr-res">с- + -ся</td><td class="pr-uz">yigʻilmoq</td>
      <td class="pr-end">Все сошли́сь у две́ри.</td></tr>
  <tr><td class="pr-res">раз- + -ся</td><td class="pr-uz">tarqalmoq</td>
      <td class="pr-end">По́сле уро́ка все разошли́сь.</td></tr>
</table></div>

<h3>4. На- va bitta chiroyli soʻz</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Найти́</b> — «topmoq» — aslida <b>на + идти́</b>. Soʻzma-soʻz: «yurib
borib, ustiga tushmoq».<br><br>
Yaʼni rus tilida <b>topish — bu yurishning natijasi</b>. Siz qidirasiz
(<em>иска́ть</em>), yurasiz, va bir joyda <b>ustiga chiqasiz</b> —
<em>нашёл</em>.<br><br>
Shuning uchun bu feʼl <em>идти́</em> kabi tuslanadi:
<em>найду́, найдёшь, найдёт</em> — va oʻtgan zamonda <em>нашёл, нашла́,
нашли́</em>, xuddi <em>шёл, шла, шли</em> kabi.</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Он до́лго <span class="pe-hl pe-hl--o">иска́л</span>
     ключи́ и наконе́ц <span class="pe-hl pe-hl--v">нашёл</span> их.</p>
  <p class="pe-ex__uz">U kalitlarni uzoq qidirdi va nihoyat topdi.</p>
  <p class="pe-ex__why">PR-52 dan tanish juftlik — lekin endi siz
     <em>нашёл</em> qayerdan kelganini bilasiz.</p>
</div>

<h3>5. Bitta oʻzak, oʻn ikkita soʻz</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Maʼnosi</th><th>Soʻz</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">прийти́</td><td class="pr-uz">kelmoq</td>
      <td class="pr-res">пойти́</td><td class="pr-uz">joʻnamoq</td></tr>
  <tr><td class="pr-res">уйти́</td><td class="pr-uz">ketmoq</td>
      <td class="pr-res">зайти́</td><td class="pr-uz">kirib oʻtmoq</td></tr>
  <tr><td class="pr-res">войти́</td><td class="pr-uz">kirmoq</td>
      <td class="pr-res">пройти́</td><td class="pr-uz">oʻtib ketmoq</td></tr>
  <tr><td class="pr-res">вы́йти</td><td class="pr-uz">chiqmoq</td>
      <td class="pr-res">сойти́</td><td class="pr-uz">tushmoq</td></tr>
  <tr><td class="pr-res">дойти́</td><td class="pr-uz">yetib bormoq</td>
      <td class="pr-res">найти́</td><td class="pr-uz">topmoq</td></tr>
  <tr><td class="pr-res">перейти́</td><td class="pr-uz">kesib oʻtmoq</td>
      <td class="pr-res">подойти́</td><td class="pr-uz">yaqinlashmoq</td></tr>
</table></div>

<p>Oʻn ikkita soʻz. Bitta oʻzak. Va ularning hammasi
<em>шёл — шла — шли</em> naqshida oʻtgan zamon yasaydi:
<em>пришёл, ушёл, вошёл, вы́шел, дошёл, перешёл, подошёл, пошёл, зашёл,
прошёл, сошёл, нашёл</em>.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbek tilida ham shunga oʻxshash narsa bor — faqat u <b>qoʻshma
feʼllar</b> shaklida:<br>
<em>kir<b>ib chiqmoq</b></em> · <em>bor<b>ib kelmoq</b></em> ·
<em>oʻt<b>ib ketmoq</b></em> · <em>yugur<b>ib chiqmoq</b></em><br><br>
Yaʼni oʻzbekcha ham <b>ikki qismdan</b> maʼno quradi. Farq shundaki,
oʻzbekchada ikkinchi qism <b>orqada</b> va u <b>alohida feʼl</b>;
ruschada esa u <b>oldinda</b> va u <b>soʻzning bir qismi</b>.<br><br>
Solishtiring:<br>
<em>kir<b>ib chiqdim</b></em> → <em><b>за</b>шёл</em><br>
<em>oʻt<b>ib ketdi</b></em> → <em><b>про</b>шёл</em><br><br>
Ikkala tilda ham asosiy harakat bitta, qoʻshimcha maʼno esa unga
qoʻshiladi. Shuning uchun bu tizim siz uchun begona emas — u faqat
<b>teskari tomondan</b> quriladi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́! </s><em>(«ketdim, xayr» maʼnosida)</em></p>
  <p class="pe-good">Я <b>пошёл</b>! — <em>по-</em> yoʻlga chiqishni bildiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я вошёл в магази́н на пять мину́т.</s></p>
  <p class="pe-good">Я <b>зашёл</b> в магази́н — qisqa tashrif <em>за-</em> bilan</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он найди́л ключи́.</s></p>
  <p class="pe-good">Он <b>нашёл</b> ключи́ — <em>найти́</em> <em>идти́</em> kabi turlanadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>По́сле уро́ка все ушли́ в ра́зные сто́роны.</s></p>
  <p class="pe-good">По́сле уро́ка все <b>разошли́сь</b> — tarqalish <em>раз- + -ся</em></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>Найти́</b> qaysi ikki qismdan tuzilgan?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>на + идти́</strong>. Soʻzma-soʻz
    «yurib borib ustiga tushmoq». Shuning uchun u <em>идти́</em> kabi
    turlanadi: <em>найду́, нашёл, нашла́</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>войти́</b> yoki <b>зайти́</b>? &nbsp; <b>По доро́ге домо́й я ___ в
     магази́н.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>зашёл</strong>. <em>За-</em> —
    yoʻl-yoʻlakay, qisqa vaqtga kirish. <em>Войти́</em> shunchaki
    «kirmoq» degan boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapning farqi nima?<br>
     <b>Я иду́ в шко́лу. · Я пошёл в шко́лу.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — hozir yoʻldaman (jarayon).
    Ikkinchisi — <b>yoʻlga chiqdim</b>, ketdim (boshlanish). <em>По-</em>
    harakatning boshlanishini bildiradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>По́сле уро́ка все ___.</b> («tarqalishdi» maʼnosida)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>разошли́сь</strong>.
    <em>Раз- + -ся</em> — tarqalish. Uning teskarisi <em>сошли́сь</em> —
    yigʻilish.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu soʻzlarning hammasi bitta oʻzakdan. Oʻtgan zamon naqshini
     ayting.<br>
     <b>прийти́ · уйти́ · пойти́ · найти́</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>-шёл / -шла / -шли</strong>:
    <em>пришёл, ушёл, пошёл, нашёл</em>. Hammasi <em>шёл — шла — шли</em>
    naqshida — chunki ularning oʻzagi bitta.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>пойти́</b><span>joʻnamoq, yoʻlga chiqmoq</span></li>
  <li><b>зайти́</b><span>kirib oʻtmoq</span></li>
  <li><b>пройти́</b><span>oʻtib ketmoq</span></li>
  <li><b>сойти́</b><span>tushmoq</span></li>
  <li><b>найти́</b><span>topmoq (на + идти́)</span></li>
  <li><b>разойти́сь</b><span>tarqalmoq</span></li>
  <li><b>сойти́сь</b><span>yigʻilmoq</span></li>
  <li><b>ми́мо</b><span>yonidan</span></li>
  <li><b>кры́ша</b><span>tom</span></li>
  <li><b>вниз</b><span>pastga</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>По-</b> — harakatning boshlanishi: <em>пошёл, пое́хали</em>.</li>
    <li><b>За-</b> — yoʻl-yoʻlakay qisqa kirish: <em>зашёл в
        магази́н</em>.</li>
    <li><b>Про-</b> — oʻtib ketmoq · <b>с-</b> — tushmoq ·
        <b>раз- + -ся</b> — tarqalmoq.</li>
    <li><b>Найти́ = на + идти́</b> — topish yurishning natijasi.</li>
    <li>Oʻn ikkita soʻz, bitta oʻzak, bitta oʻtgan zamon naqshi:
        <b>-шёл / -шла / -шли</b>.</li>
    <li>Oʻzbekchada bu maʼnolar <b>qoʻshma feʼl</b> bilan quriladi
        (<em>kirib chiqdim</em>) — bir xil gʻoya, teskari tartib.</li>
  </ul>
</div>
""",
    },
]
