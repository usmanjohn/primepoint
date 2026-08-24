# -*- coding: utf-8 -*-
"""Prime Russian — Block B yakuni (18) va Block C boshi (19–20).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-19 dan feʼl tizimi ochiladi — oʻqish matnlaridagi "narrative frame"
istisnosi shu yerdan keyin keraksiz boʻladi.

Mashqlar:        practice/management/commands/_practice_pr_18_20.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_18_20.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_18_20.py --author=prime
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
        "title": "PR-18: Ravishlar va тоже / также / ещё / уже",
        "category": "russian",
        "order": 18,
        "summary": (
            "Oʻn ikki darsdan keyin nihoyat hech nimaga moslashmaydigan soʻz turkumi: "
            "ravish. Sifatdan ravish yasashni va тоже / также / ещё / уже ni "
            "ajratishni oʻrganasiz."
        ),
        "stories": ["Мы тоже!"],
        "content": """
<h2>PR-18: Ravishlar va тоже / также / ещё / уже</h2>

<p>Oʻn ikki dars davomida siz bitta narsani qayta-qayta qildingiz: soʻzni otga
moslashtirdingiz. Sifat moslashdi, egalik moslashdi, <em>э́тот</em> moslashdi,
hatto savol soʻzi ham moslashdi. Bugun dam olasiz. <b>Ravish</b> (наречие) —
rus tilidagi eng bemalol soʻz turkumi: u <b>hech qachon, hech nimaga
moslashmaydi</b>. Bitta shakl, hamma joyda. Va yaxshi xabar davom etadi:
ravishni sifatdan yasash uchun bitta harfni almashtirish kifoya.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Sifatdan ravish yasaysiz: <b>-ый → -о</b></li>
    <li>Eng koʻp ishlatiladigan ravishlarni bilasiz</li>
    <li><b>Тоже</b> va <b>также</b> ni ajratasiz</li>
    <li><b>Ещё</b> va <b>уже́</b> ni — va ularning inkor shakllarini — oʻrganasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ravish yasash</span>
  <span class="pe-chip pe-chip--s">хоро́ш<b>ий</b></span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--adv">хорош<b>о́</b></span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">бы́стр<b>ый</b></span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--adv">бы́стр<b>о</b></span>
</div>

<h3>1. Sifatdan ravishga — bitta harf</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Sifat (otga)</th><th>Ravish (harakatga)</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">хоро́ший</td><td class="pr-end">хорошо́</td>
      <td class="pr-uz">yaxshi</td><td class="pr-uz">Здесь хорошо́.</td></tr>
  <tr><td class="pr-stem">плохо́й</td><td class="pr-end">пло́хо</td>
      <td class="pr-uz">yomon</td><td class="pr-uz">Там пло́хо.</td></tr>
  <tr><td class="pr-stem">бы́стрый</td><td class="pr-end">бы́стро</td>
      <td class="pr-uz">tez</td><td class="pr-uz">О́чень бы́стро.</td></tr>
  <tr><td class="pr-stem">ме́дленный</td><td class="pr-end">ме́дленно</td>
      <td class="pr-uz">sekin</td><td class="pr-uz">Ме́дленно, пожа́луйста.</td></tr>
  <tr><td class="pr-stem">ти́хий</td><td class="pr-end">ти́хо</td>
      <td class="pr-uz">jimgina</td><td class="pr-uz">До́ма ти́хо.</td></tr>
  <tr><td class="pr-stem">интере́сный</td><td class="pr-end">интере́сно</td>
      <td class="pr-uz">qiziqarli</td><td class="pr-uz">Э́то интере́сно!</td></tr>
  <tr><td class="pr-stem">тру́дный</td><td class="pr-end">тру́дно</td>
      <td class="pr-uz">qiyin</td><td class="pr-uz">Ру́сский — не тру́дно.</td></tr>
  <tr><td class="pr-stem">лёгкий</td><td class="pr-end">легко́</td>
      <td class="pr-uz">oson</td><td class="pr-uz">Э́то легко́. <em>(istisno)</em></td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Ravish oʻrta jinsdagi sifat bilan <b>bir xil koʻrinadi</b>: <em>хорош<b>о́</b></em>.
Chalkashmaslik oson — ular <b>boshqa narsaga</b> qaraydi. Sifat <b>otni</b>
taʼriflaydi, ravish esa <b>holatni yoki harakatni</b>:<br>
<em>Э́то хоро́шее окно́.</em> — sifat, <em>окно́</em> ga qaraydi.<br>
<em>Здесь хорошо́.</em> — ravish, hech qanday ot yoʻq.</div>

<h3>2. Kerakli ravishlar roʻyxati</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Qanday?</p>
    <p>хорошо́ · пло́хо · бы́стро · ме́дленно<br>
       ти́хо · гро́мко · краси́во · пра́вильно</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Qachon?</p>
    <p>сейча́с (hozir) · сего́дня · вчера́ · за́втра<br>
       ра́но (erta) · по́здно (kech)<br>
       всегда́ (doim) · ча́сто (tez-tez) · ре́дко (kamdan-kam)</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Qancha?</p>
    <p>о́чень (juda) · мно́го (koʻp) · ма́ло (oz)<br>
       то́лько (faqat) · то́же (ham)</p></div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu yerda bitta chinakam farq bor va uni bilmaslik xatoga olib keladi. Oʻzbek tilida
sifat va ravish koʻpincha <b>bir xil soʻz</b>: <em>yaxshi kitob</em> — <em>yaxshi
oʻqiydi</em>, <em>tez mashina</em> — <em>tez yuradi</em>. Soʻz oʻzgarmaydi. Rus
tilida esa u <b>oʻzgaradi</b>: <em>хоро́ш<b>ий</b> — хорош<b>о́</b></em>,
<em>бы́стр<b>ый</b> — бы́стр<b>о</b></em>. Har safar “yaxshi” yoki “tez” deb
oʻylaganingizda oʻzingizdan soʻrang: <b>otni</b> taʼriflayapmanmi yoki
<b>harakatni</b>? Ot boʻlsa — <b>-ый</b>, harakat boʻlsa — <b>-о</b>.</div>

<h3>3. Тоже va также</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Тоже — “men ham”</p>
    <p>Yangi <b>ega</b> qoʻshadi: kimdir yana shuni qilyapti.</p>
    <p>— Я студе́нт.<br>— Я <b>то́же</b>.</p>
    <p>Афсо́на здесь. Жасу́р <b>то́же</b> здесь.</p>
    <p>Kundalik nutqda — deyarli har doim <b>тоже</b>.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Также — “bundan tashqari”</p>
    <p>Yangi <b>narsa</b> qoʻshadi, roʻyxatga davom.</p>
    <p>Здесь шко́ла, а <b>та́кже</b> библиоте́ка.</p>
    <p>Kitobiy va rasmiyroq. Yozuvda koʻproq uchraydi.</p>
    <p>Ikkilansangiz — <b>тоже</b> deng.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekcha <b>ham</b> ikkala vazifani bajaradi: <em>men <b>ham</b></em> va
<em>bundan tashqari</em>. Rus tili ularni ikkiga ajratgan. Amaliy maslahat:
<em>“men ham”, “u ham”</em> degan joyda — <b>то́же</b>. Roʻyxatga narsa
qoʻshayotgan joyda — <b>та́кже</b>. Va <b>то́же</b> ni tanlab hech qachon
qoʻpol xato qilmaysiz.</div>

<h3>4. Ещё va уже́ — va ularning inkori</h3>

<p>Bu ikkisi juftlik boʻlib yashaydi, va ularning inkor shakllari ham juftlik:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shakl</th><th>Maʼnosi</th><th>Misol</th><th>Oʻzbekchada</th></tr>
  <tr><td class="pr-res">ещё</td><td class="pr-uz">hali, yana</td>
      <td class="pr-stem">Он ещё здесь.</td><td class="pr-end">U hali shu yerda.</td></tr>
  <tr><td class="pr-res">уже́</td><td class="pr-uz">allaqachon</td>
      <td class="pr-stem">Он уже́ здесь.</td><td class="pr-end">U allaqachon shu yerda.</td></tr>
  <tr><td class="pr-res">ещё не</td><td class="pr-uz">hali … emas</td>
      <td class="pr-stem">Он ещё не здесь.</td><td class="pr-end">U hali kelmagan.</td></tr>
  <tr><td class="pr-res">уже́ не</td><td class="pr-uz">endi … emas</td>
      <td class="pr-stem">Он уже́ не здесь.</td><td class="pr-end">U endi bu yerda emas.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Bu toʻrtlikni <b>vaqt chizigʻi</b> sifatida tasavvur qiling. <em>Ещё не</em> —
hali boshlanmagan. <em>Уже́</em> — boshlangan. <em>Ещё</em> — davom etyapti.
<em>Уже́ не</em> — tugagan. Toʻrt nuqta, bitta chiziq. Bir marta shunday
koʻrsangiz, ularni boshqa adashtirmaysiz.</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Жасу́р <span class="pe-hl pe-hl--adv">уже́</span> здесь?<br>
     — Нет, <span class="pe-hl pe-hl--adv">ещё не</span> здесь. Но Афсо́на
     <span class="pe-hl pe-hl--adv">уже́</span> здесь.</p>
  <p class="pe-ex__uz">— Jasur allaqachon keldimi?<br>
     — Yoʻq, hali kelmadi. Lekin Afsona allaqachon shu yerda.</p>
  <p class="pe-ex__why">Bitta suhbatda <b>уже́</b> ikki marta va <b>ещё не</b>
     bir marta. Bu toʻrtlik kundalik nutqda juda tez-tez uchraydi.</p>
</div>

<p><b>Ещё</b> ning yana ikkita foydali ishlatilishi bor:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">Ещё раз, пожа́луйста.<br>Ещё чай?</p>
  <p class="pe-ex__uz">Yana bir marta, iltimos.<br>Yana choy?</p>
  <p class="pe-ex__why">“Yana, koʻproq” maʼnosida — dasturxonda va darsda har kuni
     eshitasiz.</p>
</div>

<h3>5. О́чень — va u nimaga qoʻshiladi</h3>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--adv">О́чень</span> хорошо́.
     <span class="pe-hl pe-hl--adv">О́чень</span> большо́й дом.</p>
  <p class="pe-ex__uz">Juda yaxshi. Juda katta uy.</p>
  <p class="pe-ex__why"><b>О́чень</b> sifat va ravishga qoʻshiladi. U hech qachon
     oʻzgarmaydi — <em>о́чень большо́й</em>, <em>о́чень больша́я</em>,
     <em>о́чень больши́е</em>.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Здесь хоро́ший.</s> (joy haqida)</p>
  <p class="pe-good">Здесь <b>хорошо́</b>. — bu holat, ot emas: ravish kerak</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Э́то хорошо́ окно́.</s></p>
  <p class="pe-good">Э́то <b>хоро́шее</b> окно́. — ot bor, demak sifat kerak</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я также.</s> (“men ham”)</p>
  <p class="pe-good">Я <b>то́же</b>. — yangi ega qoʻshilganda <b>тоже</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он не ещё здесь.</s></p>
  <p class="pe-good">Он <b>ещё не</b> здесь. — tartib qatʼiy: <b>ещё не</b>, <b>уже́ не</b></p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>бы́стрый</b> dan ravish yasang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>бы́стро</strong>. Qoida oddiy:
    <b>-ый → -о</b>. Xuddi shunday <em>ти́хий → ти́хо</em>,
    <em>краси́вый → краси́во</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Sifatmi yoki ravish? <b>Здесь ___.</b> (yaxshi)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>хорошо́</strong> — ravish. Gapda ot yoʻq,
    demak taʼriflanadigan narsa ham yoʻq: bu <em>holat</em>. Ot boʻlganda sifat
    kerak boʻlardi: <em>хоро́шее ме́сто</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>Он ещё не здесь</b> va <b>Он уже́ не здесь</b> — farqi nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ещё не</strong> — hali kelmagan (keladi).
    <strong>Уже́ не</strong> — endi yoʻq (kelgan edi, ketdi). Vaqt chizigʻining
    ikki uchi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Boʻsh joyga: <b>— Я студе́нт. — Я ___.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>то́же</strong>. Yangi ega qoʻshilyapti —
    “men ham”. <em>Также</em> bu yerda kitobiy va gʻalati eshitiladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gapda xato bor?<br>
     а) Э́то о́чень интере́сно. &nbsp; б) Здесь ти́хо.<br>
     в) Э́то хорошо́ кни́га. &nbsp; г) Он уже́ до́ма.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Ot bor
    (<em>кни́га</em>), demak sifat kerak: <b>хоро́шая кни́га</b>. Ravish
    (<em>хорошо́</em>) otni taʼriflay olmaydi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>наре́чие</b><span>ravish</span></li>
  <li><b>то́же</b><span>ham (yangi ega)</span></li>
  <li><b>та́кже</b><span>bundan tashqari</span></li>
  <li><b>ещё</b><span>hali, yana</span></li>
  <li><b>уже́</b><span>allaqachon</span></li>
  <li><b>о́чень</b><span>juda</span></li>
  <li><b>всегда́ / ча́сто / ре́дко</b><span>doim / tez-tez / kamdan-kam</span></li>
  <li><b>сейча́с</b><span>hozir</span></li>
  <li><b>ра́но / по́здно</b><span>erta / kech</span></li>
  <li><b>то́лько</b><span>faqat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Ravish <b>hech qachon oʻzgarmaydi</b> — oʻn ikki darsdan keyin birinchi
        bunday soʻz turkumi.</li>
    <li>Sifatdan ravish: <b>-ый → -о</b>. <em>хоро́ший → хорошо́</em>.</li>
    <li>Sifat <b>otni</b>, ravish <b>holat yoki harakatni</b> taʼriflaydi.
        Oʻzbekchada bu bitta soʻz — ruschada ikkita.</li>
    <li><b>Тоже</b> = “men ham” (yangi ega). <b>Также</b> = “bundan tashqari”
        (yangi narsa, kitobiy).</li>
    <li>Vaqt chizigʻi: <b>ещё не → уже́ → ещё → уже́ не</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-19: Feʼl nima? Infinitiv va ikkita tuslanish (спряжение)",
        "category": "russian",
        "order": 19,
        "summary": (
            "Kursning yarmi shu darsdan boshlanadi: gaplar harakatga keladi. Infinitiv "
            "nima, oltita shaxs qanday ishlaydi va rus feʼllari nega ikki guruhga "
            "boʻlingan."
        ),
        "stories": ["Анкета"],
        "content": """
<h2>PR-19: Feʼl nima? Infinitiv va ikkita tuslanish (спряжение)</h2>

<p>Shu paytgacha tuzgan gaplaringizning hammasi <b>qimirlamas</b> edi:
<em>Э́то дом. Дом большо́й. У меня́ есть брат.</em> Ular narsalarni nomlaydi va
taʼriflaydi, lekin hech nima <em>sodir boʻlmaydi</em>. Bugundan boshlab odamlar
oʻqiydi, ishlaydi, gapiradi, yuradi. Bu — kursning eng katta eshigi, va u
ortida atigi ikkita jadval turadi. Bugun eshikni ochamiz: feʼl nima, uning
lugʻat shakli qanday, va nega rus feʼllari ikki guruhga boʻlingan.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Infinitivni — feʼlning lugʻat shaklini — taniysiz</li>
    <li>Oltita shaxsni bilasiz va ular nima uchun kerakligini tushunasiz</li>
    <li>I va II tuslanishni bir qarashda ajratasiz</li>
    <li>Rus va oʻzbek feʼllari orasidagi asosiy farqni bilib olasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Feʼl qanday ishlaydi</span>
  <span class="pe-chip pe-chip--s">oʻzak</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">shaxs qoʻshimchasi</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">чита́-ю</span>
</div>

<h3>1. Infinitiv — feʼlning lugʻat shakli</h3>

<p>PR-4 da bir gap aytgan edik: <em>“-ть bilan tugagan soʻz — deyarli har doim
feʼl”</em>. Endi u toʻliq maʼnoga ega boʻladi. <b>Infinitiv</b> — bu feʼlning
lugʻatdagi shakli, oʻzbekchadagi <b>-moq</b> ga toʻgʻri keladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Oxiri</th><th>Misol</th><th>Maʼnosi</th><th>Izoh</th></tr>
  <tr><td class="pr-end">-ть</td><td class="pr-res">чита́ть · рабо́тать · говори́ть</td>
      <td class="pr-uz">oʻqimoq · ishlamoq · gapirmoq</td>
      <td class="pr-uz">Feʼllarning katta koʻpchiligi</td></tr>
  <tr><td class="pr-end">-ти</td><td class="pr-res">идти́ · нести́</td>
      <td class="pr-uz">yurmoq · koʻtarib bormoq</td>
      <td class="pr-uz">Oz sonli, lekin juda koʻp ishlatiladi</td></tr>
  <tr><td class="pr-end">-чь</td><td class="pr-res">мочь · помо́чь</td>
      <td class="pr-uz">-a olmoq · yordam bermoq</td>
      <td class="pr-uz">Juda oz sonli</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu tuzilma sizga tanish: oʻzbek lugʻatida ham feʼl <b>-moq</b> bilan beriladi —
<em>oʻqi<b>moq</b>, ishla<b>moq</b>, gapir<b>moq</b></em>. Rus lugʻatida esa
<b>-ть</b> bilan. Ikkala tilda ham bu shakl <b>hech kimga tegishli emas</b>:
u shunchaki harakatning nomi. Gapirish uchun uni oʻzgartirish kerak.</div>

<h3>2. Oltita shaxs</h3>

<p>Feʼl <b>kim</b> harakat qilayotganiga qarab shakl oladi. Rus tilida oltita
shakl bor — PR-10 dagi olmoshlarning har biri uchun bittadan:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Olmosh</th><th>чита́ть</th><th>Oʻzbekchada</th></tr>
  <tr><td class="pr-res">1-shaxs birlik</td><td class="pr-stem">я</td>
      <td class="pr-end">чита́ю</td><td class="pr-uz">oʻqiyman</td></tr>
  <tr><td class="pr-res">2-shaxs birlik</td><td class="pr-stem">ты</td>
      <td class="pr-end">чита́ешь</td><td class="pr-uz">oʻqiysan</td></tr>
  <tr><td class="pr-res">3-shaxs birlik</td><td class="pr-stem">он / она́ / оно́</td>
      <td class="pr-end">чита́ет</td><td class="pr-uz">oʻqiydi</td></tr>
  <tr><td class="pr-res">1-shaxs koʻplik</td><td class="pr-stem">мы</td>
      <td class="pr-end">чита́ем</td><td class="pr-uz">oʻqiymiz</td></tr>
  <tr><td class="pr-res">2-shaxs koʻplik</td><td class="pr-stem">вы</td>
      <td class="pr-end">чита́ете</td><td class="pr-uz">oʻqiysiz</td></tr>
  <tr><td class="pr-res">3-shaxs koʻplik</td><td class="pr-stem">они́</td>
      <td class="pr-end">чита́ют</td><td class="pr-uz">oʻqiydilar</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻng ustunga qarang — bu <b>aynan oʻzbekcha tizim</b>. Oʻzbekchada ham
<em>oʻqi-y-<b>man</b>, oʻqi-y-<b>san</b>, oʻqi-y-<b>di</b></em>: oʻzak
oʻzgarmaydi, oxiriga shaxs qoʻshimchasi qoʻshiladi. Ruschada ham
<em>чита́-<b>ю</b>, чита́-<b>ешь</b>, чита́-<b>ет</b></em>. Yaʼni <b>g‘oya bir
xil</b> — siz faqat yangi qoʻshimchalarni yodlaysiz, yangi tushunchani emas.
Ingliz tilida bunday tizim yoʻq (<em>I read, you read, we read</em>), shuning
uchun bu joyda siz ingliz tilini oʻrgangan oʻquvchidan oldindasiz.</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Mana bu esa <b>haqiqiy farq</b>, va u butun kurs davomida sizni chalgʻitib
turadi: <b>soʻz tartibi</b>. Oʻzbek gapida feʼl <b>oxirida</b> turadi, rus gapida
esa <b>oʻrtada</b>:<br>
<em>Men kitob <b>oʻqiyman</b>.</em> — ega, toʻldiruvchi, <b>feʼl</b>.<br>
<b>Я <span class="pr-stem">чита́ю</span> кни́гу.</b> — ega, <b>feʼl</b>,
toʻldiruvchi.<br>
Koreys yoki yapon tilini oʻrganayotgan oʻzbek bolaga soʻz tartibi sovgʻa
boʻladi; rus tilida esa u <b>oʻrganilishi kerak</b>. Har bir gap tuzganingizda
feʼlni oldinga suring.</div>

<h3>3. Ikkita tuslanish — va ularni qanday ajratish</h3>

<p>Rus feʼllari <b>ikki guruhga</b> boʻlinadi. Guruh qoʻshimchalar toʻplamini hal
qiladi, shuning uchun har bir yangi feʼlda qaysi guruhdaligini bilish kerak:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">I tuslanish (пе́рвое)</p>
    <p>Infinitiv koʻpincha <b>-ать</b>, <b>-ять</b>, <b>-еть</b>.</p>
    <p style="font-size:1.05rem">-ю · -<b>е</b>шь · -<b>е</b>т<br>
       -<b>е</b>м · -<b>е</b>те · -<b>ю</b>т</p>
    <p>чита́ть · рабо́тать · знать · де́лать · гуля́ть</p>
    <p>Belgisi: <b>Е</b> harfi.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">II tuslanish (второ́е)</p>
    <p>Infinitiv koʻpincha <b>-ить</b>.</p>
    <p style="font-size:1.05rem">-ю · -<b>и</b>шь · -<b>и</b>т<br>
       -<b>и</b>м · -<b>и</b>те · -<b>я</b>т</p>
    <p>говори́ть · люби́ть · учи́ть · смотре́ть</p>
    <p>Belgisi: <b>И</b> harfi.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Guruhni aniqlashning eng tez yoʻli — <b>ты</b> shakliga qarash:<br>
<b>-ешь</b> koʻrsangiz → I tuslanish (чита́<b>ешь</b>).<br>
<b>-ишь</b> koʻrsangiz → II tuslanish (говор<b>и́шь</b>).<br>
Shuning uchun lugʻatda yangi feʼlni koʻrganingizda <b>ikkita shaklni</b> yozib
oling: infinitiv va <b>ты</b> shakli. Qolgan beshtasi oʻz-oʻzidan kelib
chiqadi.</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Infinitiv oxiri <b>maslahat beradi, lekin kafolat bermaydi</b>: <em>-ить</em>
odatda II, <em>-ать</em> odatda I. Lekin istisnolar bor — masalan
<b>смотре́ть</b> <em>-еть</em> bilan tugaydi, lekin II tuslanishda
(<em>смотр<b>и́шь</b></em>). Shuning uchun ishonchli belgi — infinitiv emas,
<b>ты</b> shakli. Yodlashning eng arzon yoʻli shu.</div>

<h3>4. Feʼl bilan birinchi gaplar</h3>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Я</span>
     <span class="pe-hl pe-hl--v">чита́ю</span>.
     <span class="pe-hl pe-hl--s">Ты</span>
     <span class="pe-hl pe-hl--v">чита́ешь</span>.
     <span class="pe-hl pe-hl--s">Мы</span>
     <span class="pe-hl pe-hl--v">чита́ем</span>.</p>
  <p class="pe-ex__uz">Men oʻqiyman. Sen oʻqiysan. Biz oʻqiymiz.</p>
  <p class="pe-ex__why">Toʻldiruvchisiz ham gap toʻliq. Toʻldiruvchi
     qoʻshilganda u <b>feʼldan keyin</b> keladi va shaklini oʻzgartiradi
     (<em>кни́гу</em>) — buni PR-32 da koʻramiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Афсо́на <span class="pe-hl pe-hl--v">рабо́тает</span>.
     Жасу́р <span class="pe-hl pe-hl--neg">не</span>
     <span class="pe-hl pe-hl--v">рабо́тает</span>.</p>
  <p class="pe-ex__uz">Afsona ishlaydi. Jasur ishlamaydi.</p>
  <p class="pe-ex__why">PR-17 dagi <b>не</b> nihoyat feʼl bilan ishlayapti:
     u har doim feʼlning <b>oldida</b> turadi.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Oʻzbekchada olmoshni tushirib qoldirish odatiy hol: <em>“Oʻqiyman”</em> —
“men” aytilmaydi, chunki <b>-man</b> allaqachon aytib turibdi. Rus tilida ham
qoʻshimcha shaxsni koʻrsatadi, lekin <b>olmosh odatda saqlanadi</b>:
<em>Я чита́ю</em>, <em>Чита́ю</em> emas. Uni tushirish mumkin, lekin bu
soʻzlashuv uslubi — boshida har doim olmosh bilan gapiring.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я чита́ть кни́гу.</s></p>
  <p class="pe-good">Я <b>чита́ю</b> кни́гу. — infinitiv gapda kesim boʻla olmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я кни́гу чита́ю.</s> (oʻzbekcha tartib)</p>
  <p class="pe-good">Я <b>чита́ю</b> кни́гу. — ruschada feʼl oʻrtada turadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>говори́ешь</s></p>
  <p class="pe-good">говор<b>и́шь</b> — <em>говори́ть</em> II tuslanishda, demak <b>-ишь</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он чита́ю.</s></p>
  <p class="pe-good">Он <b>чита́ет</b> — qoʻshimcha shaxsga mos boʻlishi kerak</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>рабо́тать</b> soʻzining qaysi qismi infinitiv belgisi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>-ть</strong>. Oʻzak — <b>рабо́та-</b>,
    infinitiv belgisi — <b>-ть</b>. Oʻzbekchadagi <em>-moq</em> ga toʻgʻri
    keladi: <em>ishla<b>moq</b></em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>говори́шь</b> — qaysi tuslanish?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>II tuslanish</strong> — chunki
    <b>ты</b> shaklida <b>-ишь</b> turibdi. I tuslanishda <b>-ешь</b> boʻlardi:
    <em>чита́ешь</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Oʻzbekcha va ruscha feʼl tizimining <b>asosiy farqi</b> nima?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Soʻz tartibi.</strong> Qoʻshimcha tizimi
    ikkala tilda ham bir xil ishlaydi (oʻzak + shaxs qoʻshimchasi), lekin oʻzbek
    gapida feʼl <b>oxirida</b>, rus gapida <b>oʻrtada</b> turadi:
    <em>Men kitob oʻqiyman</em> → <em>Я чита́ю кни́гу</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Yangi feʼlni lugʻatdan koʻchirayotganda <b>nechta shaklni</b> yozish kerak?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ikkitani: infinitiv va «ты» shakli.</strong>
    <em>Ты</em> shakli tuslanishni aytib beradi (<b>-ешь</b> = I, <b>-ишь</b> = II),
    va undan qolgan beshta shakl oʻz-oʻzidan kelib chiqadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap toʻgʻri?<br>
     а) Я чита́ть кни́гу. &nbsp; б) Я кни́гу чита́ю.<br>
     в) Я чита́ю кни́гу. &nbsp; г) Чита́ть я кни́гу.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. а) da infinitiv kesim
    boʻlolmaydi; б) — oʻzbekcha tartib (grammatik jihatdan mumkin, lekin taʼkidli
    va gʻalati); г) umuman notoʻgʻri. Rus gapining odatiy tartibi:
    <b>ega → feʼl → toʻldiruvchi</b>.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>глаго́л</b><span>feʼl</span></li>
  <li><b>инфинити́в</b><span>infinitiv, lugʻat shakli</span></li>
  <li><b>спряже́ние</b><span>tuslanish</span></li>
  <li><b>чита́ть</b><span>oʻqimoq</span></li>
  <li><b>рабо́тать</b><span>ishlamoq</span></li>
  <li><b>знать</b><span>bilmoq</span></li>
  <li><b>де́лать</b><span>qilmoq</span></li>
  <li><b>говори́ть</b><span>gapirmoq</span></li>
  <li><b>жить</b><span>yashamoq</span></li>
  <li><b>по́мнить</b><span>eslamoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Infinitiv</b> — lugʻat shakli, <b>-ть</b> (kamroq <b>-ти</b>, <b>-чь</b>).
        Oʻzbekcha <em>-moq</em>.</li>
    <li>Feʼl <b>oltita shaxs</b> boʻyicha oʻzgaradi: oʻzak + shaxs qoʻshimchasi —
        xuddi oʻzbekchadagidek.</li>
    <li>Ikki tuslanish: <b>I → Е</b> (чита́<b>ешь</b>), <b>II → И</b>
        (говор<b>и́шь</b>).</li>
    <li>Ishonchli belgi infinitiv emas, <b>«ты» shakli</b>. Yangi feʼlni ikkala
        shaklda yodlang.</li>
    <li><b>Eng katta farq:</b> oʻzbek feʼli gap <b>oxirida</b>, rus feʼli
        <b>oʻrtada</b>. <em>Я чита́ю кни́гу.</em></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-20: I tuslanish: читать, работать, знать (-ю, -ешь, -ет, -ем, -ете, -ют)",
        "category": "russian",
        "order": 20,
        "summary": (
            "Birinchi tuslanishning oltita qoʻshimchasi va ular bilan ishlaydigan "
            "oʻnlab feʼl. Bu darsdan keyin siz kundalik hayotingiz haqida gapira "
            "olasiz."
        ),
        "stories": ["Один день Жасура"],
        "content": """
<h2>PR-20: I tuslanish: читать, работать, знать (-ю, -ешь, -ет, -ем, -ете, -ют)</h2>

<p>Kechagi dars xarita edi — bugun yoʻlga chiqamiz. Birinchi tuslanish rus tilidagi
feʼllarning katta koʻpchiligini oʻz ichiga oladi, va uning qoʻshimchalari
<b>bittagina naqsh</b>dan iborat. Bugun oʻsha naqshni oʻrganasiz va u bilan
darrov <em>oʻnlab</em> feʼlni ishlata boshlaysiz — chunki naqsh <b>har birida
bir xil</b> ishlaydi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>I tuslanishning oltita qoʻshimchasini yodlaysiz</li>
    <li>Infinitivdan oʻzakni ajratib olasiz</li>
    <li>Oʻnga yaqin kundalik feʼlni toʻliq tuslay olasiz</li>
    <li>Feʼlni inkor qilasiz va savol berasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">I tuslanish</span>
  <span class="pe-chip pe-chip--s">чита́</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">ю · ешь · ет · ем · ете · ют</span>
</div>

<h3>1. Oʻzakni topish — ikki qadam</h3>

<ol class="pe-steps">
  <li>Infinitivni oling: <b>чита́ть</b>.</li>
  <li><b>-ть</b> ni olib tashlang: <b>чита́-</b>. Bu — oʻzak.</li>
  <li>Oʻzakka oltita qoʻshimchani navbat bilan qoʻshing.</li>
</ol>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>я</td><td class="pr-stem">чита́</td><td class="pr-end">ю</td>
      <td class="pr-res">чита́ю</td><td class="pr-uz">oʻqiyman</td></tr>
  <tr><td>ты</td><td class="pr-stem">чита́</td><td class="pr-end">ешь</td>
      <td class="pr-res">чита́ешь</td><td class="pr-uz">oʻqiysan</td></tr>
  <tr><td>он / она́</td><td class="pr-stem">чита́</td><td class="pr-end">ет</td>
      <td class="pr-res">чита́ет</td><td class="pr-uz">oʻqiydi</td></tr>
  <tr><td>мы</td><td class="pr-stem">чита́</td><td class="pr-end">ем</td>
      <td class="pr-res">чита́ем</td><td class="pr-uz">oʻqiymiz</td></tr>
  <tr><td>вы</td><td class="pr-stem">чита́</td><td class="pr-end">ете</td>
      <td class="pr-res">чита́ете</td><td class="pr-uz">oʻqiysiz</td></tr>
  <tr><td>они́</td><td class="pr-stem">чита́</td><td class="pr-end">ют</td>
      <td class="pr-res">чита́ют</td><td class="pr-uz">oʻqiydilar</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Oltita qoʻshimchani yodlashning eng oson yoʻli — <b>oʻrtadagi toʻrttasiga</b>
qarash: <b>-ешь, -ет, -ем, -ете</b>. Ularning hammasida <b>Е</b> bor va ular
bir-biriga oʻxshaydi. Faqat birinchi va oxirgisi boshqacha: <b>-ю</b> va
<b>-ют</b>. Yaʼni yodlash kerak boʻlgan narsa — “Е qatori, ikki tomonida
Ю”.</div>

<h3>2. Bitta naqsh, koʻp feʼl</h3>

<p>Endi eng yoqimli qismi. Naqsh <b>oʻzgarmaydi</b> — siz uni bir marta
oʻrganib, hamma feʼlga qoʻllaysiz:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>я</th><th>ты</th><th>он / она́</th><th>они́</th></tr>
  <tr><td class="pr-res">рабо́тать</td><td class="pr-end">рабо́таю</td>
      <td class="pr-end">рабо́таешь</td><td class="pr-end">рабо́тает</td>
      <td class="pr-end">рабо́тают</td></tr>
  <tr><td class="pr-res">знать</td><td class="pr-end">зна́ю</td>
      <td class="pr-end">зна́ешь</td><td class="pr-end">зна́ет</td>
      <td class="pr-end">зна́ют</td></tr>
  <tr><td class="pr-res">де́лать</td><td class="pr-end">де́лаю</td>
      <td class="pr-end">де́лаешь</td><td class="pr-end">де́лает</td>
      <td class="pr-end">де́лают</td></tr>
  <tr><td class="pr-res">ду́мать</td><td class="pr-end">ду́маю</td>
      <td class="pr-end">ду́маешь</td><td class="pr-end">ду́мает</td>
      <td class="pr-end">ду́мают</td></tr>
  <tr><td class="pr-res">понима́ть</td><td class="pr-end">понима́ю</td>
      <td class="pr-end">понима́ешь</td><td class="pr-end">понима́ет</td>
      <td class="pr-end">понима́ют</td></tr>
  <tr><td class="pr-res">слу́шать</td><td class="pr-end">слу́шаю</td>
      <td class="pr-end">слу́шаешь</td><td class="pr-end">слу́шает</td>
      <td class="pr-end">слу́шают</td></tr>
  <tr><td class="pr-res">гуля́ть</td><td class="pr-end">гуля́ю</td>
      <td class="pr-end">гуля́ешь</td><td class="pr-end">гуля́ет</td>
      <td class="pr-end">гуля́ют</td></tr>
  <tr><td class="pr-res">игра́ть</td><td class="pr-end">игра́ю</td>
      <td class="pr-end">игра́ешь</td><td class="pr-end">игра́ет</td>
      <td class="pr-end">игра́ют</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu jadvalni oʻzbekcha bilan yonma-yon qoʻying va bir narsani koʻring:
<em>ishla-<b>y</b>-man / ishla-<b>y</b>-san / ishla-<b>y</b>-di</em> —
<b>рабо́та-ю / рабо́та-ешь / рабо́та-ет</b>. Ikkala tilda ham oʻzak
qimirlamaydi, faqat oxiri almashadi. Shuning uchun bu dars siz uchun <b>yangi
tushuncha emas, yangi qoʻshimchalar roʻyxati</b>. Buni yodda tuting — u sizga
kuch beradi.</div>

<h3>3. Gap tuzamiz</h3>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Жасу́р</span>
     <span class="pe-hl pe-hl--v">рабо́тает</span>
     <span class="pe-hl pe-hl--adv">бы́стро</span>.</p>
  <p class="pe-ex__uz">Jasur tez ishlaydi.</p>
  <p class="pe-ex__why">PR-18 dagi ravish nihoyat oʻz joyini topdi — u
     <b>harakatni</b> taʼriflaydi. Va soʻz tartibiga qarang: feʼl oʻrtada.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Мы</span>
     <span class="pe-hl pe-hl--v">гуля́ем</span>
     <span class="pe-hl pe-hl--adv">ка́ждый день</span>.</p>
  <p class="pe-ex__uz">Biz har kuni sayr qilamiz.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--s">Вы</span>
     <span class="pe-hl pe-hl--v">понима́ете</span>?<br>
     — Да, <span class="pe-hl pe-hl--v">понима́ю</span>. Но
     <span class="pe-hl pe-hl--adv">ме́дленно</span>.</p>
  <p class="pe-ex__uz">— Tushunyapsizmi?<br>— Ha, tushunaman. Lekin sekin.</p>
  <p class="pe-ex__why">Qisqa javobda olmoshni tushirish mumkin — qoʻshimcha
     (<b>-ю</b>) allaqachon “men” ni aytib turibdi.</p>
</div>

<h3>4. Inkor va savol</h3>

<p>Ikkalasi ham siz allaqachon bilgan qoidalar bilan ishlaydi:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">Я <span class="pe-hl pe-hl--neg">не</span>
     <span class="pe-hl pe-hl--v">зна́ю</span>.</p>
  <p class="pe-ex__uz">Bilmayman.</p>
  <p class="pe-ex__why">PR-17: <b>не</b> inkor qilinadigan soʻzning oldida —
     bu yerda feʼlning oldida. Bu ibora rus tilida eng koʻp aytiladigan
     gaplardan biri.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Ты рабо́таешь? &nbsp;·&nbsp; Где ты рабо́таешь?</p>
  <p class="pe-ex__uz">Ishlaysanmi? &nbsp;·&nbsp; Qayerda ishlaysan?</p>
  <p class="pe-ex__why">PR-6: “ha/yoʻq” savolida soʻz tartibi oʻzgarmaydi, faqat
     ohang. PR-15: savol soʻzi oldinga chiqadi. Hech qanday yangi qoida yoʻq.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Barcha <b>-ать</b> feʼllari I tuslanishda emas, va barcha I tuslanish feʼllari
<b>-ать</b> bilan tugamaydi. Masalan <b>жить</b> (yashamoq) <b>-ить</b> bilan
tugaydi, lekin I tuslanishda — va uning oʻzagi ham oʻzgaradi:
<em>жи<b>в</b>у́, жи<b>в</b>ёшь, жи<b>в</b>ёт</em>. Bunday feʼllarni PR-22 da
alohida koʻramiz. Bugun faqat oʻzagi oʻzgarmaydigan feʼllar bilan
ishlayapmiz.</div>

<h3>5. Urgʻu haqida bir gap</h3>

<p>Bu darsdagi feʼllarning hammasida urgʻu <b>oʻzakda</b> va u qimirlamaydi:
<em>чита́ю, чита́ешь, чита́ет…</em>. Bu qulay. Lekin ba'zi I tuslanish feʼllarida
urgʻu qoʻshimchaga tushadi va koʻchib yuradi — <em>жив<b>у́</b>, жив<b>ёшь</b></em>.
Bunday holatda <b>-ешь</b> oʻrniga <b>-ёшь</b> yoziladi, chunki urgʻuli
<b>ё</b> qoidasi ishlaydi (PR-2).</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Он чита́ю.</s></p>
  <p class="pe-good">Он <b>чита́ет</b> — qoʻshimcha shaxsga mos boʻlishi kerak</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Они́ рабо́тает.</s></p>
  <p class="pe-good">Они́ <b>рабо́тают</b> — koʻplik uchun <b>-ют</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я не зна́ть.</s></p>
  <p class="pe-good">Я не <b>зна́ю</b> — infinitiv kesim boʻla olmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я хорошо́ рабо́тает.</s></p>
  <p class="pe-good">Я хорошо́ <b>рабо́таю</b> — feʼl <b>egaga</b> qaraydi, ravishga emas</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>рабо́тать</b> ni <b>мы</b> uchun tuslang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>рабо́таем</strong>. Oʻzak
    <b>рабо́та-</b> (infinitivdan <b>-ть</b> olib tashlandi), <b>мы</b> uchun
    qoʻshimcha <b>-ем</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Они́ ___ ка́ждый день.</b> (гуля́ть)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>гуля́ют</strong>. <em>Они́</em> —
    3-shaxs koʻplik, demak <b>-ют</b>. Oʻzak <b>гуля́-</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu gapni ruschaga oʻgiring: <b>Bilmayman.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я не зна́ю.</strong> (yoki qisqa:
    <em>Не зна́ю</em>). <b>Не</b> feʼlning oldida turadi — PR-17 dagi qoida.
    Bu rus tilidagi eng koʻp aytiladigan gaplardan biri.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Qaysi soʻz tartibi tabiiy? <b>кни́гу / чита́ю / я</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я чита́ю кни́гу.</strong> Ega → feʼl →
    toʻldiruvchi. Oʻzbekchada feʼl oxirda boʻlardi (<em>Men kitob
    oʻqiyman</em>) — ruschada uni <b>oldinga suring</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi shakl notoʻgʻri?<br>
     а) вы зна́ете &nbsp; б) она́ де́лает<br>
     в) они́ ду́мает &nbsp; г) мы слу́шаем</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. <em>Они́</em> — koʻplik,
    demak <b>ду́мают</b>. <b>-ет</b> faqat <em>он / она́ / оно́</em> uchun.
    Bu eng koʻp uchraydigan xato: 3-shaxs birlik va koʻplikni adashtirish.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>чита́ть</b><span>oʻqimoq</span></li>
  <li><b>рабо́тать</b><span>ishlamoq</span></li>
  <li><b>знать</b><span>bilmoq</span></li>
  <li><b>де́лать</b><span>qilmoq</span></li>
  <li><b>ду́мать</b><span>oʻylamoq</span></li>
  <li><b>понима́ть</b><span>tushunmoq</span></li>
  <li><b>слу́шать</b><span>tinglamoq</span></li>
  <li><b>гуля́ть</b><span>sayr qilmoq</span></li>
  <li><b>игра́ть</b><span>oʻynamoq</span></li>
  <li><b>ка́ждый день</b><span>har kuni</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Oʻzak = infinitiv minus <b>-ть</b>: <em>чита́ть → чита́-</em>.</li>
    <li>Oltita qoʻshimcha: <b>-ю, -ешь, -ет, -ем, -ете, -ют</b>. “Е qatori, ikki
        tomonida Ю”.</li>
    <li>Naqsh <b>oʻzgarmaydi</b> — bir marta oʻrganib, oʻnlab feʼlga qoʻllaysiz.</li>
    <li>Inkor: <b>не</b> feʼlning oldida. <em>Я не зна́ю.</em></li>
    <li>Soʻz tartibi: <b>ega → feʼl → toʻldiruvchi</b>. Feʼlni oldinga suring.</li>
    <li>Oʻzagi oʻzgaradigan feʼllar (<em>жить → живу́</em>) — PR-22 da.</li>
  </ul>
</div>
""",
    },
]
