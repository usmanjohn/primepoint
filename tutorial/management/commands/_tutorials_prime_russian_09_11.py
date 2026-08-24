# -*- coding: utf-8 -*-
"""Prime Russian — Block B, darslar 9–11.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Har bir dars uchta boʻlakdan biri: dars + mashq + oʻqish matni.
Mashqlar:        practice/management/commands/_practice_pr_09_11.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_09_11.py
(Prime Russian oʻqish matnlarida AUDIO yoʻq — 2026-08-09 dagi qaror.)

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_09_11.py --author=prime
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
        "title": "PR-9: Koʻplik (множественное число) — -ы, -и, -а va istisnolar",
        "category": "russian",
        "order": 9,
        "summary": (
            "Rus tilida koʻplik qoʻshimchasi otning jinsiga va oxirgi harfiga qarab "
            "tanlanadi. Asosan ikkita qoʻshimcha bor — -ы/-и va -а/-я — plus bitta "
            "imlo qoidasi va qisqa istisnolar roʻyxati."
        ),
        "stories": ["Рынок в субботу"],
        "content": """
<h2>PR-9: Koʻplik (множественное число) — -ы, -и, -а va istisnolar</h2>

<p>Oʻzbek tilida koʻplik dunyodagi eng oson ish: nima boʻlsa ham <b>-lar</b> qoʻshasiz.
<em>Kitob → kitoblar. Uy → uylar. Odam → odamlar.</em> Istisno yoʻq, jins yoʻq,
oʻylash yoʻq. Rus tilida esa qoʻshimcha otning jinsiga qarab tanlanadi. Bu birinchi
qarashda yomon xabarga oʻxshaydi — lekin aslida qoʻshimchalar atigi <b>ikkita</b>:
<b>-ы/-и</b> va <b>-а/-я</b>. Birinchisi — deyarli hamma narsa. Ikkinchisi — oʻrta
jins va yodlanadigan qisqa roʻyxat. Bugun ikkalasini ham hal qilamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uch jinsning koʻplik qoʻshimchasini bilasiz</li>
    <li><b>г к х ж ч ш щ</b> imlo qoidasini — nega <em>кни́ги</em>, <em>кни́гы</em> emas</li>
    <li>Koʻplikda urgʻu koʻchishini payqaysiz</li>
    <li>Eng koʻp uchraydigan istisnolarni taniysiz: <b>друзья́, лю́ди, де́ти</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikkita qoʻshimcha</span>
  <span class="pe-chip pe-chip--s">-ы / -и</span>
  <span class="pe-op">= erkak va ayol jinsi</span>
  <span class="pe-chip pe-chip--v">-а / -я</span>
  <span class="pe-op">= oʻrta jins (+ qisqa roʻyxat)</span>
</div>

<h3>1. Jinsga qarab qoʻshimcha</h3>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">+ <span class="pr-end">ы</span></p>
    <p>стол → сто<b>лы́</b><br>
       студе́нт → студе́нт<b>ы</b><br>
       журна́л → журна́л<b>ы</b></p>
    <p><b>-й</b> va <b>-ь</b> boʻlsa → <b>-и</b>:<br>
       музе́й → музе́<b>и</b> · слова́рь → словар<b>и́</b></p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">-а → <span class="pr-end">ы</span></p>
    <p>шко́ла → шко́л<b>ы</b><br>
       ко́мната → ко́мнат<b>ы</b><br>
       газе́та → газе́т<b>ы</b></p>
    <p><b>-я</b> va <b>-ь</b> boʻlsa → <b>-и</b>:<br>
       неде́ля → неде́л<b>и</b> · дверь → две́р<b>и</b></p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">-о → <span class="pr-end">а</span></p>
    <p>окно́ → о́кн<b>а</b><br>
       сло́во → слов<b>а́</b><br>
       ме́сто → мест<b>а́</b></p>
    <p><b>-е</b> boʻlsa → <b>-я</b>:<br>
       мо́ре → мор<b>я́</b> · зда́ние → зда́ни<b>я</b></p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu jadval qoʻrqinchli koʻrinadi, lekin unga boshqacha qarang. Oʻzbekchada bitta
qoʻshimcha bor — <b>-lar</b>. Ruschada esa aslida ham bitta asosiy qoʻshimcha bor:
<b>-ы/-и</b>. U erkak jinsining ham, ayol jinsining ham koʻpligini yasaydi, yaʼni
otlarning katta koʻpchiligini. <b>-а/-я</b> esa faqat oʻrta jins va bir hovuch
maxsus soʻz uchun. Yaʼni siz <em>ikkita</em> narsani oʻrganyapsiz, oʻn ikkitani
emas.</div>

<h3>2. Yettita harf qoidasi — nega кни́ги, кни́гы emas</h3>

<p>Bitta imlo qoidasi bor va u koʻplikda doim ishlaydi. <b>Г, К, Х, Ж, Ч, Ш, Щ</b>
dan keyin <b>-ы</b> hech qachon yozilmaydi — uning oʻrniga <b>-и</b> keladi.</p>

<div class="pr-say">
  <span class="pr-say__from">кни́га</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">кни́г<b>и</b></span>
  <span class="pr-say__why">Г dan keyin -ы boʻlmaydi</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">ру́чка</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">ру́чк<b>и</b></span>
  <span class="pr-say__why">К dan keyin -ы boʻlmaydi</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">врач</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">врач<b>и́</b></span>
  <span class="pr-say__why">Ч dan keyin -ы boʻlmaydi</span>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Г К Х Ж Ч Ш Щ</b> dan keyin — har doim <b>И</b>. Bu yettita harf rus imlosining
boshqa joylarida ham xuddi shunday ishlaydi (PR-4 dagi <em>жи-ши</em> ni eslang).
Ularni bir marta yodlasangiz, butun kurs davomida foyda beradi. Talaffuzda esa
<b>ж, ш, ц</b> dan keyin bu <b>и</b> baribir <b>[ы]</b> boʻlib oʻqiladi.</div>

<h3>3. Urgʻu koʻchadi — quloq soling</h3>

<p>PR-5 da urgʻu koʻchishini koʻrgan edik. Koʻplik — u eng koʻp koʻchadigan joy:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Birlik</th><th>Koʻplik</th><th>Urgʻu</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">стол</td><td class="pr-res">столы́</td>
      <td class="pr-end">oxirga koʻchdi</td><td class="pr-uz">stol → stollar</td></tr>
  <tr><td class="pr-res">окно́</td><td class="pr-res">о́кна</td>
      <td class="pr-end">boshga koʻchdi</td><td class="pr-uz">deraza → derazalar</td></tr>
  <tr><td class="pr-res">рука́</td><td class="pr-res">ру́ки</td>
      <td class="pr-end">boshga koʻchdi</td><td class="pr-uz">qoʻl → qoʻllar</td></tr>
  <tr><td class="pr-res">сло́во</td><td class="pr-res">слова́</td>
      <td class="pr-end">oxirga koʻchdi</td><td class="pr-uz">soʻz → soʻzlar</td></tr>
  <tr><td class="pr-res">кни́га</td><td class="pr-res">кни́ги</td>
      <td class="pr-end">joyida qoldi</td><td class="pr-uz">kitob → kitoblar</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Urgʻu qayerga koʻchishini bashorat qiladigan ishonchli qoida <b>yoʻq</b> — buni
ochiq aytish halolroq. Shuning uchun yangi otni <b>ikkita shaklda</b> yodlang:
<em>окно́ — о́кна</em>, <em>стол — столы́</em>. Bu ikki barobar ish emas; bu
bitta soʻzni <em>toʻliq</em> oʻrganish.</div>

<h3>4. Erkak jinsining -а koʻpligi — yodlanadigan roʻyxat</h3>

<p>Bir guruh erkak jinsdagi ot <b>-ы</b> emas, <b>-а́</b> qabul qiladi, va bu <b>-а́</b>
har doim urgʻuli boʻladi. Bu soʻzlar juda koʻp uchraydi, shuning uchun ularni
alohida yodlash arziydi:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Joy va narsa</p>
    <p>дом → дома́<br>го́род → города́<br>по́езд → поезда́<br>па́спорт → паспорта́</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Odam</p>
    <p>учи́тель → учителя́<br>до́ктор → доктора́<br>профе́ссор → профессора́</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Boshqa</p>
    <p>глаз → глаза́<br>ве́чер → вечера́<br>а́дрес → адреса́</p></div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>дома́</b> (uylar) va <b>до́ма</b> (uyda) — bir xil harflar, ikki xil soʻz.
Faqat urgʻu ajratadi. <em>Здесь дома́</em> — “bu yerda uylar”. <em>Я до́ма</em> —
“men uydaman”. PR-5 dagi <em>за́мок / замо́к</em> juftligini eslang: rus tilida
urgʻu maʼno tashiydi.</div>

<h3>5. Haqiqiy istisnolar — oltitasi yetadi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Birlik</th><th>Koʻplik</th><th>Maʼnosi</th><th>Izoh</th></tr>
  <tr><td class="pr-res">друг</td><td class="pr-end">друзья́</td><td class="pr-uz">doʻst</td>
      <td class="pr-uz">-ья guruhi</td></tr>
  <tr><td class="pr-res">брат</td><td class="pr-end">бра́тья</td><td class="pr-uz">aka</td>
      <td class="pr-uz">-ья guruhi</td></tr>
  <tr><td class="pr-res">сын</td><td class="pr-end">сыновья́</td><td class="pr-uz">oʻgʻil</td>
      <td class="pr-uz">-ья guruhi</td></tr>
  <tr><td class="pr-res">стул</td><td class="pr-end">сту́лья</td><td class="pr-uz">stul</td>
      <td class="pr-uz">-ья guruhi</td></tr>
  <tr><td class="pr-res">челове́к</td><td class="pr-end">лю́ди</td><td class="pr-uz">odam</td>
      <td class="pr-uz">butunlay boshqa soʻz</td></tr>
  <tr><td class="pr-res">ребёнок</td><td class="pr-end">де́ти</td><td class="pr-uz">bola</td>
      <td class="pr-uz">butunlay boshqa soʻz</td></tr>
</table></div>

<p>Va bir nechta ot <b>faqat koʻplikda</b> yashaydi — ularning birligi umuman yoʻq:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">де́ньги · часы́ · очки́ · роди́тели · кани́кулы · но́жницы</p>
  <p class="pe-ex__uz">pul · soat · koʻzoynak · ota-ona · taʼtil · qaychi</p>
  <p class="pe-ex__why">Oʻzbekchada bularning koʻpi birlikda: “pul”, “soat”.
     Ruschada esa ular doim koʻplik — <em>де́ньги здесь</em>, “pullar shu yerda”
     emas, oddiygina “pul shu yerda”.</p>
</div>

<h3>6. Они́ — koʻplikning olmoshi</h3>

<p>Bitta yaxshi xabar bilan tugatamiz. PR-8 da uchta olmosh bor edi: он, она́, оно́.
Koʻplikda esa <b>bitta</b> shakl — <b>они́</b>, jinsdan qatʼi nazar:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">— Где столы́? — <span class="pe-hl pe-hl--s">Они́</span> здесь.<br>
     — Где кни́ги? — <span class="pe-hl pe-hl--s">Они́</span> здесь.<br>
     — Где о́кна? — <span class="pe-hl pe-hl--s">Они́</span> здесь.</p>
  <p class="pe-ex__uz">— Stollar/kitoblar/derazalar qayerda? — Ular shu yerda.</p>
  <p class="pe-ex__why">Koʻplikda jins yoʻqoladi. Rus tilida bu tez-tez uchraydigan
     yengillik: koʻplik koʻp narsani soddalashtiradi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>кни́гы</s></p>
  <p class="pe-good">кни́г<b>и</b> — Г К Х Ж Ч Ш Щ dan keyin har doim <b>-и</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>челове́ки</s></p>
  <p class="pe-good"><b>лю́ди</b> — bu istisno, butunlay boshqa soʻz</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Где кни́ги? — Она́ здесь.</s></p>
  <p class="pe-good">Где кни́ги? — <b>Они́</b> здесь. — koʻplikda har doim <b>они́</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>окны</s></p>
  <p class="pe-good"><b>о́кна</b> — oʻrta jins <b>-о</b> ni <b>-а</b> ga almashtiradi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>шко́ла</b> ning koʻpligi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>шко́лы</strong>. Ayol jinsi, <b>-а</b> bilan
    tugagan → <b>-ы</b>. Oxiridagi <b>л</b> yettita harf roʻyxatida yoʻq, shuning uchun
    imlo qoidasi bu yerda ishlamaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Nega <b>ру́чка</b> → <b>ру́чки</b>, <b>ру́чкы</b> emas?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki oxirgi undosh <b>К</b> — u yettita harf
    (<strong>Г К Х Ж Ч Ш Щ</strong>) roʻyxatida. Ulardan keyin <b>-ы</b> hech qachon
    yozilmaydi, faqat <b>-и</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>окно́</b> ning koʻpligini urgʻusi bilan ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>о́кна</strong> — urgʻu <b>oxirdan boshga
    koʻchdi</b>. Birlikda окн<b>о́</b>, koʻplikda <b>о́</b>кна. Aynan shuning uchun
    yangi otni ikkala shaklda yodlash kerak.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>Здесь дома́</b> va <b>Я до́ма</b> — farqi nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Faqat urgʻu, lekin maʼno butunlay boshqa.
    <strong>дома́</strong> — “uylar” (<em>дом</em> ning koʻpligi).
    <strong>до́ма</strong> — “uyda”. <em>Здесь дома́</em> = bu yerda uylar bor;
    <em>Я до́ма</em> = men uydaman.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi qatorda hamma koʻplik shakli toʻgʻri?<br>
     а) столы́, кни́гы, о́кна &nbsp; б) столы́, кни́ги, о́кна<br>
     в) столы, кни́ги, окны &nbsp; г) стола́, кни́ги, о́кна</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong>. а) da <em>кни́гы</em> — Г dan
    keyin -ы boʻlmaydi. в) da <em>окны</em> — oʻrta jins <b>-а</b> oladi. г) da
    <em>стола́</em> — <em>стол</em> maxsus roʻyxatda yoʻq, u oddiy <b>столы́</b>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>мно́жественное число́</b><span>koʻplik</span></li>
  <li><b>друзья́</b><span>doʻstlar</span></li>
  <li><b>лю́ди</b><span>odamlar</span></li>
  <li><b>де́ти</b><span>bolalar</span></li>
  <li><b>они́</b><span>ular</span></li>
  <li><b>де́ньги</b><span>pul (doim koʻplik)</span></li>
  <li><b>роди́тели</b><span>ota-ona</span></li>
  <li><b>врачи́</b><span>shifokorlar</span></li>
  <li><b>города́</b><span>shaharlar</span></li>
  <li><b>ру́чка / ру́чки</b><span>ruchka / ruchkalar</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Asosiy qoʻshimcha — <b>-ы/-и</b> (erkak va ayol jinsi). Oʻrta jins —
        <b>-а/-я</b>.</li>
    <li><b>Г К Х Ж Ч Ш Щ</b> dan keyin har doim <b>-и</b>: кни́ги, ру́чки, врачи́.</li>
    <li>Urgʻu koʻpincha <b>koʻchadi</b> — otni ikkala shaklda yodlang:
        <em>окно́ — о́кна</em>.</li>
    <li>Erkak jinsining urgʻuli <b>-а́</b> roʻyxati: дома́, города́, учителя́,
        доктора́, глаза́.</li>
    <li>Istisnolar: <b>друзья́, бра́тья, сту́лья, лю́ди, де́ти</b>. Faqat koʻplik:
        <b>де́ньги, часы́, очки́</b>.</li>
    <li>Koʻplikning olmoshi bitta — <b>они́</b>, jinsdan qatʼi nazar.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-10: Shaxs olmoshlari va egalik: мой, твой, наш, ваш",
        "category": "russian",
        "order": 10,
        "summary": (
            "Sakkizta shaxs olmoshi va egalik soʻzlari. Eng muhim gʻoya: ruschada "
            "egalik soʻzi egaga emas, EGALIK QILINGAN narsaning jinsiga qarab oʻzgaradi."
        ),
        "stories": ["Чей это телефон?"],
        "content": """
<h2>PR-10: Shaxs olmoshlari va egalik: мой, твой, наш, ваш</h2>

<p>Oʻzbek tilida “mening kitobim” deganda oʻzgaradigan narsa — <b>kitob</b>:
kitob<b>im</b>, kitob<b>ing</b>, kitob<b>i</b>. Qoʻshimcha <em>egani</em> koʻrsatadi.
Rus tilida esa hammasi teskari: “mening” alohida soʻz boʻlib oldinda turadi, va u
<em>egaga</em> emas, <b>egalik qilingan narsaning jinsiga</b> qarab oʻzgaradi.
<b>Мой брат</b>, lekin <b>моя́ сестра́</b> — “men” oʻzgarmadim, oʻzgargani aka va
opa. Shu bitta flipni tushunsangiz, dars tugadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Sakkizta shaxs olmoshini bilasiz: я, ты, он, она́, оно́, мы, вы, они́</li>
    <li><b>мой / твой / наш / ваш</b> ni otning jinsiga moslaysiz</li>
    <li><b>его́, её, их</b> nega hech qachon oʻzgarmasligini bilib olasiz</li>
    <li><b>Чей? Чья? Чьё? Чьи?</b> deb soʻraysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Egalik otga moslashadi</span>
  <span class="pe-chip pe-chip--s">мой брат</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">моя́ сестра́</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">моё окно́</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--adv">мои́ друзья́</span>
</div>

<h3>1. Sakkizta shaxs olmoshi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Birlik</th><th>Maʼnosi</th><th>Koʻplik</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">я</td><td class="pr-uz">men</td>
      <td class="pr-res">мы</td><td class="pr-uz">biz</td></tr>
  <tr><td class="pr-res">ты</td><td class="pr-uz">sen</td>
      <td class="pr-res">вы</td><td class="pr-uz">siz / sizlar</td></tr>
  <tr><td class="pr-res">он</td><td class="pr-uz">u (erkak jinsi)</td>
      <td class="pr-res">они́</td><td class="pr-uz">ular (hamma jins)</td></tr>
  <tr><td class="pr-res">она́</td><td class="pr-uz">u (ayol jinsi)</td>
      <td class="pr-res">—</td><td class="pr-uz">&nbsp;</td></tr>
  <tr><td class="pr-res">оно́</td><td class="pr-uz">u (oʻrta jins)</td>
      <td class="pr-res">—</td><td class="pr-uz">&nbsp;</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu jadval oʻzbekcha bilan deyarli bir xil: <em>men, sen, u, biz, siz, ular</em>.
Yagona farq — uchinchi shaxs birlikda ruschada uchta shakl bor (он/она́/оно́),
oʻzbekchada esa bitta (<em>u</em>). Buni PR-8 da koʻrgan edik. <b>Вы</b> esa PR-7
dagidek ikki vazifada: hurmat va koʻplik.</div>

<h3>2. Egalik soʻzlari — otga moslashadi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kimning</th><th>м. (дом)</th><th>ж. (кни́га)</th><th>с. (окно́)</th>
      <th>мн. (друзья́)</th></tr>
  <tr><td class="pr-res">я → mening</td><td class="pr-stem">мой</td>
      <td class="pr-stem">моя́</td><td class="pr-stem">моё</td>
      <td class="pr-stem">мои́</td></tr>
  <tr><td class="pr-res">ты → sening</td><td class="pr-stem">твой</td>
      <td class="pr-stem">твоя́</td><td class="pr-stem">твоё</td>
      <td class="pr-stem">твои́</td></tr>
  <tr><td class="pr-res">мы → bizning</td><td class="pr-stem">наш</td>
      <td class="pr-stem">на́ша</td><td class="pr-stem">на́ше</td>
      <td class="pr-stem">на́ши</td></tr>
  <tr><td class="pr-res">вы → sizning</td><td class="pr-stem">ваш</td>
      <td class="pr-stem">ва́ша</td><td class="pr-stem">ва́ше</td>
      <td class="pr-stem">ва́ши</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Мой</span> брат —
     <span class="pe-hl pe-hl--s">моя́</span> сестра́ —
     <span class="pe-hl pe-hl--s">моё</span> окно́ —
     <span class="pe-hl pe-hl--s">мои́</span> друзья́.</p>
  <p class="pe-ex__uz">Mening akam — mening opam — mening derazam — mening doʻstlarim.</p>
  <p class="pe-ex__why">Toʻrt marta “mening”, toʻrt xil shakl. Oʻzgargani —
     <b>ot</b>, “men” emas.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana bu darsning eng muhim jumlasi. Oʻzbek tilida qoʻshimcha <b>egani</b>
koʻrsatadi: <em>kitob<b>im</b></em> (meniki), <em>kitob<b>ing</b></em> (seniki).
Ot esa oʻzgarmaydi. Rus tilida <b>teskarisi</b>: “men” har doim <b>м-</b> boʻlib
qolaveradi, oʻzgaradigan qism esa <b>oxiri</b> — va u <em>otning</em> jinsiga
qaraydi. Shuning uchun “mening akam” va “mening opam” ruschada boshqa-boshqa
soʻz bilan boshlanadi: <b>мой</b> брат, <b>моя́</b> сестра́.</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Jadvalni yodlamang — <b>naqshni</b> koʻring. Oxirlari PR-8 dagi uchlik bilan
bir xil: <b>-й / -я / -ё / -и</b> va <b>— / -а / -е / -и</b>. Xuddi
<em>но́вый / но́вая / но́вое / но́вые</em> kabi. Rus tilida bir xil oxirlar
qayta-qayta takrorlanadi; siz bitta naqshni oʻrganib, uni koʻp joyda
ishlatasiz.</div>

<h3>3. Его́, её, их — hech qachon oʻzgarmaydi</h3>

<p>Endi darsning eng oson qismi. “Uning” va “ularning” <b>umuman oʻzgarmaydi</b>:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shakl</th><th>Maʼnosi</th><th>Misol</th><th>Izoh</th></tr>
  <tr><td class="pr-res">его́</td><td class="pr-uz">uning (erkak egasi)</td>
      <td class="pr-stem">его́ дом · его́ кни́га · его́ окно́</td>
      <td class="pr-uz">hech qachon oʻzgarmaydi</td></tr>
  <tr><td class="pr-res">её</td><td class="pr-uz">uning (ayol egasi)</td>
      <td class="pr-stem">её дом · её кни́га · её окно́</td>
      <td class="pr-uz">hech qachon oʻzgarmaydi</td></tr>
  <tr><td class="pr-res">их</td><td class="pr-uz">ularning</td>
      <td class="pr-stem">их дом · их кни́га · их о́кна</td>
      <td class="pr-uz">hech qachon oʻzgarmaydi</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Его́</b> yozilishi bilan oʻqilishi mos kelmaydi — bu rus tilidagi eng koʻp
uchraydigan “aldov”lardan biri:</div>

<div class="pr-say">
  <span class="pr-say__from">его́</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[йиво́]</span>
  <span class="pr-say__why">-го oxiri [во] boʻlib oʻqiladi</span>
</div>

<div class="pr-say">
  <span class="pr-say__from">сего́дня</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[с'иво́дн'ъ]</span>
  <span class="pr-say__why">shu qoida: bugun</span>
</div>

<p>Bu qoida keyinchalik <b>hamma</b> <em>-ого/-его</em> oxirida ishlaydi
(PR-43 da koʻramiz). Hozircha shuni bilib qoʻying: <b>-го</b> koʻrsangiz, <b>[во]</b>
deng.</p>

<h3>4. Чей? — “kimning?”</h3>

<p>Savol soʻzi ham xuddi egalik kabi otga moslashadi:</p>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">м. — Чей?</p>
    <p class="pr-gender__form">Чей э́то дом?</p>
    <p>— Э́то мой дом.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">ж. — Чья?</p>
    <p class="pr-gender__form">Чья э́то кни́га?</p>
    <p>— Э́то её кни́га.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">с. — Чьё? · мн. — Чьи?</p>
    <p class="pr-gender__form">Чьё э́то окно́?<br>Чьи э́то кни́ги?</p>
    <p>— Э́то на́ше окно́.<br>— Э́то их кни́ги.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--s">Чей</span> э́то телефо́н?<br>
     — Э́то не <span class="pe-hl pe-hl--s">мой</span> телефо́н.
     Мо́жет, <span class="pe-hl pe-hl--s">его́</span>?</p>
  <p class="pe-ex__uz">— Bu kimning telefoni?<br>
     — Bu mening telefonim emas. Balki uningdir?</p>
  <p class="pe-ex__why"><b>Телефо́н</b> — erkak jinsi, shuning uchun <b>чей</b> va
     <b>мой</b>. <b>Его́</b> esa baribir oʻzgarmadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>мой сестра́</s></p>
  <p class="pe-good"><b>моя́</b> сестра́ — <em>сестра́</em> ayol jinsi, egalik unga moslashadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>его́ кни́га → “егоя кни́га”</s></p>
  <p class="pe-good"><b>его́ кни́га</b> — <em>его́, её, их</em> hech qachon oʻzgarmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>его́ → [эго́]</s></p>
  <p class="pe-good">его́ → <b>[йиво́]</b> — <b>-го</b> oxiri [во] boʻlib oʻqiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Чей э́то кни́га?</s></p>
  <p class="pe-good"><b>Чья</b> э́то кни́га? — savol soʻzi ham otga moslashadi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>___ шко́ла</b> (bizning)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>на́ша шко́ла</strong>. <em>Шко́ла</em> ayol
    jinsi (-а), demak <b>на́ша</b>. Erkak jinsi boʻlsa <em>наш</em>, oʻrta jins
    boʻlsa <em>на́ше</em>, koʻplik boʻlsa <em>на́ши</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>его́</b> qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[йиво́]</strong>. <b>-го</b> oxiri
    <b>[во]</b> boʻlib oʻqiladi, birinchi <b>е</b> esa urgʻusiz boʻlgani uchun
    [и] ga qisqaradi (иканье, PR-5). Xuddi shunday: <em>сего́дня</em>
    [с'иво́дн'ъ].</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Savolni tuzing: <b>___ э́то тетра́ди?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Чьи</strong> э́то тетра́ди? —
    <em>тетра́ди</em> koʻplikda, demak <b>чьи</b>. Birlikda boʻlsa edi:
    <em>Чья э́то тетра́дь?</em> (ayol jinsi).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Nima uchun <b>мой брат</b>, lekin <b>моя́ сестра́</b>? “Men” oʻzgardimi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Yoʻq — men oʻzgarmadim.</strong> Oʻzgargani
    <b>ot</b>: <em>брат</em> erkak jinsi, <em>сестра́</em> ayol jinsi. Ruschada
    egalik soʻzi <b>egalik qilingan narsaga</b> moslashadi, egaga emas — bu
    oʻzbekchaning teskarisi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap toʻgʻri?<br>
     а) Э́то её дом. &nbsp; б) Э́то ея́ дом. &nbsp;
     в) Э́то ей дом. &nbsp; г) Э́то её́я дом.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>а)</strong>. <b>Её</b> hech qachon
    oʻzgarmaydi — <em>её дом, её кни́га, её окно́, её друзья́</em>. Bu darsning eng
    oson qismi: uchta soʻz (его́, её, их) hech qanday shaklga ega emas.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>мой / моя́ / моё / мои́</b><span>mening</span></li>
  <li><b>твой / твоя́ / твоё / твои́</b><span>sening</span></li>
  <li><b>наш / на́ша / на́ше / на́ши</b><span>bizning</span></li>
  <li><b>ваш / ва́ша / ва́ше / ва́ши</b><span>sizning</span></li>
  <li><b>его́</b><span>uning (erkak)</span></li>
  <li><b>её</b><span>uning (ayol)</span></li>
  <li><b>их</b><span>ularning</span></li>
  <li><b>чей / чья / чьё / чьи</b><span>kimning</span></li>
  <li><b>телефо́н</b><span>telefon</span></li>
  <li><b>мо́жет</b><span>balki</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Sakkiz olmosh: <b>я, ты, он, она́, оно́, мы, вы, они́</b>.</li>
    <li>Egalik soʻzi <b>egalik qilingan narsaning jinsiga</b> moslashadi, egaga emas.
        Oʻzbekchaning teskarisi.</li>
    <li><b>мой / моя́ / моё / мои́</b> — bir xil naqsh твой, наш, ваш uchun ham.</li>
    <li><b>его́, её, их</b> — hech qachon oʻzgarmaydi. Darsning eng oson qismi.</li>
    <li><b>его́</b> = <b>[йиво́]</b>. <b>-го</b> koʻrsangiz, <b>[во]</b> deng.</li>
    <li>Savol ham moslashadi: <b>Чей? Чья? Чьё? Чьи?</b></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-11: «Быть» yoʻq gaplar: Я студент. Кофе горячий. Tire qachon qoʻyiladi?",
        "category": "russian",
        "order": 11,
        "summary": (
            "Hozirgi zamonda “boʻlmoq” feʼli yoʻqligini butun gapga tarqatamiz — va "
            "tire (—) qachon qoʻyilishini aniq bilib olasiz. Oʻtgan va kelasi zamonda "
            "esa u qaytib keladi: был va бу́дет."
        ),
        "stories": ["Мой город — Ташкент"],
        "content": """
<h2>PR-11: «Быть» yoʻq gaplar: Я студент. Кофе горячий. Tire qachon qoʻyiladi?</h2>

<p>PR-6 da <b>Э́то дом</b> deb oʻrgangan edik va “oʻrtada feʼl yoʻq” degan edik.
Endi shu gʻoyani butun tilga tarqatamiz: <b>hozirgi zamonda rus tilida “boʻlmoq”
feʼli hech qachon qoʻyilmaydi</b>. Faqat <em>это</em> bilan emas — <b>hamma</b>
gapda. <em>Я студе́нт. Он врач. Мы до́ма. Ко́фе горя́чий.</em> Ammo bitta yangi
narsa bor: yozuvda baʼzan feʼl oʻrniga <b>tire (—)</b> qoʻyiladi, baʼzan esa
qoʻyilmaydi. Bugun qaysi holatda qaysi biri ekanini aniq bilib olasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Feʼlsiz gapni har qanday ega bilan tuzasiz</li>
    <li>Tire (—) qachon qoʻyilishini uchta qoida bilan hal qilasiz</li>
    <li>Oʻtgan zamonda <b>был / была́ / бы́ло / бы́ли</b> ni ishlatasiz</li>
    <li>Kelasi zamonda <b>бу́дет / бу́дут</b> ni ishlatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Uch zamon</span>
  <span class="pe-chip pe-chip--o">был</span>
  <span class="pe-op">←</span>
  <span class="pe-chip pe-chip--opt">(hech nima)</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">бу́дет</span>
</div>

<h3>1. Hozirgi zamon — boʻshliq</h3>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Я</span>
     <span class="pe-hl pe-hl--o">студе́нт</span>.<br>
     <span class="pe-hl pe-hl--s">Он</span>
     <span class="pe-hl pe-hl--o">врач</span>.<br>
     <span class="pe-hl pe-hl--s">Мы</span>
     <span class="pe-hl pe-hl--adv">до́ма</span>.</p>
  <p class="pe-ex__rom">[йа студэ́нт · он врач · мы до́мъ]</p>
  <p class="pe-ex__uz">Men talabaman. U shifokor. Biz uydamiz.</p>
  <p class="pe-ex__why">Uch gap, uchalasida ham feʼl yoʻq — va uchalasi ham toʻliq,
     tabiiy rus gapi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekcha tarjimaga qarang: <em>Men talaba<b>man</b></em>. Bizda kesim
qoʻshimchasi bor — <b>-man, -san, -miz</b>. Rus tilida esa <b>hech narsa</b>
qoʻyilmaydi: <em>Я студе́нт</em>, <em>Ты студе́нт</em>, <em>Мы студе́нты</em> —
faqat olmosh oʻzgaradi. Bu oʻzbek oʻquvchisi uchun yoqimli xabar: oʻrganadigan
qoʻshimcha yoʻq, unutadigan narsa ham yoʻq.</div>

<h3>2. Tire qachon qoʻyiladi — uchta qoida</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">✅ TIRE QOʻYILADI</p>
    <p><b>Ikkala tomon ham OT boʻlsa.</b></p>
    <p>Москва́ — столи́ца.<br>
       Мой брат — врач.<br>
       Ташке́нт — го́род.<br>
       Мой го́род — Ташке́нт.</p>
    <p>Bu yerda tire <em>yoʻq boʻlgan feʼlning oʻrnini</em> bildiradi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">❌ TIRE QOʻYILMAYDI</p>
    <p><b>1. Ega — olmosh boʻlsa:</b><br>
       Я студе́нт. Он врач. Мы дру́зья.</p>
    <p><b>2. Kesim — sifat boʻlsa:</b><br>
       Ко́фе горя́чий. Дом большо́й.</p>
    <p><b>3. Kesim — ravish boʻlsa:</b><br>
       Мы до́ма. Здесь хорошо́.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Eng qisqa shakli: <b>ot + ot = tire</b>. Boshqa hamma holatda tire yoʻq.
Yodlash uchun bitta juftlikni eslab qoling:<br>
<em>Мой брат — врач.</em> (ot + ot → tire bor)<br>
<em>Он врач.</em> (olmosh + ot → tire yoʻq)</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Olmoshdan keyin ham tire qoʻyish <b>mumkin</b> — lekin faqat <em>kuchli
taʼkid</em> uchun: <em>«Я — учи́тель!»</em> degani “aynan men oʻqituvchiman”.
Bu kamdan-kam ishlatiladi. Oddiy gapda <em>Я учи́тель</em> deng va xato
qilmaysiz.</div>

<h3>3. Kesim sifat boʻlganda</h3>

<p>Sifatlarni PR-12 da toʻliq oʻrganamiz, lekin tire qoidasi uchun ular hozir
kerak. Sifat kesim boʻlsa, tire hech qachon qoʻyilmaydi:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">Ко́фе <span class="pe-hl pe-hl--v">горя́чий</span>.<br>
     Кни́га <span class="pe-hl pe-hl--v">интере́сная</span>.<br>
     Окно́ <span class="pe-hl pe-hl--v">большо́е</span>.</p>
  <p class="pe-ex__uz">Qahva issiq. Kitob qiziqarli. Deraza katta.</p>
  <p class="pe-ex__why">Uchala gapda ham tire yoʻq. Va sifat otning jinsiga
     moslashganini payqang: <b>-ий / -ая / -ое</b> — PR-8 dagi oʻsha uchlik.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Ко́фе</b> — bu darsdagi eng mashhur tuzoq. U <b>-е</b> bilan tugaydi, demak
PR-8 qoidasiga koʻra oʻrta jins boʻlishi kerak edi. Lekin u <b>erkak jinsida</b>:
<em>ко́фе горя́ч<b>ий</b></em>, <em>горя́чее</em> emas. Bu chet tildan kirgan
soʻz va u qoidaga boʻysunmaydi. Xuddi shunday: <em>такси́</em>, <em>метро́</em>,
<em>ра́дио</em> — bular esa oʻrta jinsda va <b>hech qachon oʻzgarmaydi</b>.</div>

<h3>4. Oʻtgan zamon — feʼl qaytadi</h3>

<p>Hozirgi zamonda “boʻlmoq” yoʻqoladi. Oʻtgan zamonda esa u qaytib keladi —
va otning jinsiga qarab shakl oladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Jins</th><th>Shakl</th><th>Misol</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">м.</td><td class="pr-end">был</td>
      <td class="pr-stem">Дом был здесь.</td><td class="pr-uz">Uy shu yerda edi.</td></tr>
  <tr><td class="pr-res">ж.</td><td class="pr-end">была́</td>
      <td class="pr-stem">Шко́ла была́ здесь.</td><td class="pr-uz">Maktab shu yerda edi.</td></tr>
  <tr><td class="pr-res">с.</td><td class="pr-end">бы́ло</td>
      <td class="pr-stem">Окно́ бы́ло здесь.</td><td class="pr-uz">Deraza shu yerda edi.</td></tr>
  <tr><td class="pr-res">мн.</td><td class="pr-end">бы́ли</td>
      <td class="pr-stem">Дома́ бы́ли здесь.</td><td class="pr-uz">Uylar shu yerda edi.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu — deyarli mukammal moslik. Rus <b>был</b> = oʻzbek <b>edi</b>, rus
<b>бу́дет</b> = oʻzbek <b>boʻladi</b>, hozirgi zamonda esa ikkala tilda ham
<b>hech nima</b>. Yagona farq: oʻzbekcha <em>edi</em> jinsga qarab oʻzgarmaydi,
ruscha <em>был</em> esa oʻzgaradi — <b>был / была́ / бы́ло / бы́ли</b>. Bu
PR-8 dagi uchlikning yana bir koʻrinishi.</div>

<h3>5. Kelasi zamon</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">За́втра <span class="pe-hl pe-hl--v">бу́дет</span> уро́к.<br>
     За́втра <span class="pe-hl pe-hl--v">бу́дут</span> уро́ки.</p>
  <p class="pe-ex__uz">Ertaga dars boʻladi. Ertaga darslar boʻladi.</p>
  <p class="pe-ex__why">Kelasi zamonda faqat ikkita shakl bor: birlik
     <b>бу́дет</b>, koʻplik <b>бу́дут</b>. Jins bu yerda ahamiyatsiz — oʻtgan
     zamondan osonroq.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Вчера́ <span class="pe-hl pe-hl--v">бы́ло</span> хо́лодно.
     Сего́дня хорошо́. За́втра <span class="pe-hl pe-hl--v">бу́дет</span> жа́рко.</p>
  <p class="pe-ex__uz">Kecha sovuq edi. Bugun yaxshi. Ertaga issiq boʻladi.</p>
  <p class="pe-ex__why">Uch zamon bir joyda. Oʻrtadagi gapda feʼl <b>yoʻq</b> —
     chunki u hozirgi zamon. Chapda <b>бы́ло</b>, oʻngda <b>бу́дет</b>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я есть студе́нт.</s></p>
  <p class="pe-good"><b>Я студе́нт.</b> — hozirgi zamonda “boʻlmoq” qoʻyilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я — студе́нт. (oddiy gapda)</s></p>
  <p class="pe-good"><b>Я студе́нт.</b> — ega olmosh boʻlsa, tire qoʻyilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ко́фе — горя́чий.</s></p>
  <p class="pe-good"><b>Ко́фе горя́чий.</b> — kesim sifat boʻlsa, tire qoʻyilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Шко́ла был здесь.</s></p>
  <p class="pe-good">Шко́ла <b>была́</b> здесь. — <em>шко́ла</em> ayol jinsi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Tire kerakmi? <b>Мой брат ___ врач.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ha — «Мой брат — врач».</strong> Ikkala
    tomon ham ot (<em>брат</em> va <em>врач</em>), demak tire qoʻyiladi. Agar
    <em>Он врач</em> boʻlsa edi, tire kerak boʻlmasdi — chunki ega olmosh.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Tire kerakmi? <b>Дом ___ большо́й.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Yoʻq — «Дом большо́й».</strong> Kesim
    sifat (<em>большо́й</em>), ot emas. Sifat kesim boʻlganda tire hech qachon
    qoʻyilmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Oʻtgan zamonga oʻgiring: <b>Шко́ла здесь.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Шко́ла была́ здесь.</strong>
    <em>Шко́ла</em> — ayol jinsi (-а), demak <b>была́</b>. Erkak jinsi boʻlsa
    <em>был</em>, oʻrta jins <em>бы́ло</em>, koʻplik <em>бы́ли</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>ко́фе</b> qaysi jinsda va nega bu gʻalati?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Erkak jinsida</strong> — <em>ко́фе
    горя́чий</em>. Gʻalati, chunki u <b>-е</b> bilan tugaydi va PR-8 qoidasiga koʻra
    oʻrta jins boʻlishi kerak edi. Bu chet tildan kirgan soʻzning istisnosi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gapda xato bor?<br>
     а) Москва́ — столи́ца. &nbsp; б) Я студе́нт.<br>
     в) Окно́ — большо́е. &nbsp; г) За́втра бу́дет уро́к.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong> — tire ortiqcha. Toʻgʻrisi:
    <b>Окно́ большо́е.</b> Kesim sifat, shuning uchun tire qoʻyilmaydi. Qolgan
    uchtasi toʻgʻri: а) ot + ot → tire bor; б) olmosh ega → tire yoʻq;
    г) kelasi zamonda feʼl bor.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>студе́нт</b><span>talaba</span></li>
  <li><b>врач</b><span>shifokor</span></li>
  <li><b>столи́ца</b><span>poytaxt</span></li>
  <li><b>ко́фе</b><span>qahva (erkak j.!)</span></li>
  <li><b>горя́чий</b><span>issiq (ichimlik)</span></li>
  <li><b>большо́й</b><span>katta</span></li>
  <li><b>был / была́ / бы́ло / бы́ли</b><span>edi</span></li>
  <li><b>бу́дет / бу́дут</b><span>boʻladi</span></li>
  <li><b>вчера́ / сего́дня / за́втра</b><span>kecha / bugun / ertaga</span></li>
  <li><b>до́ма</b><span>uyda</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Hozirgi zamonda “boʻlmoq” feʼli <b>hech qachon</b> qoʻyilmaydi — faqat
        <em>это</em> bilan emas, hamma gapda.</li>
    <li><b>Ot + ot = tire.</b> <em>Мой брат — врач.</em></li>
    <li>Ega <b>olmosh</b> boʻlsa yoki kesim <b>sifat/ravish</b> boʻlsa — tire yoʻq.
        <em>Я студе́нт. Ко́фе горя́чий. Мы до́ма.</em></li>
    <li>Oʻtgan zamon: <b>был / была́ / бы́ло / бы́ли</b> — jinsga moslashadi.
        Oʻzbekcha <em>edi</em>.</li>
    <li>Kelasi zamon: <b>бу́дет</b> (birlik) / <b>бу́дут</b> (koʻplik). Jins
        ahamiyatsiz.</li>
    <li><b>Ко́фе</b> — erkak jinsi, <b>-е</b> bilan tugasa ham. Chet soʻz istisnosi.</li>
  </ul>
</div>
""",
    },
]
