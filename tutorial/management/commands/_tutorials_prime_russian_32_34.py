# -*- coding: utf-8 -*-
"""Prime Russian — Block D davomi (32–34).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-32 — Вини́тельный toʻldiruvchi sifatida (oʻzbekcha -NI): butun blokdagi
eng toʻgʻri kelgan moslik. Yagona yangi tushuncha — jonli/jonsiz farqi.
PR-33 — oʻsha kelishik, ikkinchi ishi: yoʻnalish. Bu yerda PR-30 bilan
qarama-qarshilik ochiladi: в шко́ле ↔ в шко́лу.
PR-34 — Роди́тельный boshlanadi: egalik va yoʻqlik. Egalik soʻz tartibi
oʻzbekchaning TESKARISI (кни́га бра́та), va bu darsning eng katta xatosi.

Mashqlar:        practice/management/commands/_practice_pr_32_34.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_32_34.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_32_34.py --author=prime
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
        "title": "PR-32: Винительный 1: кого? что? — jonli va jonsiz farqi",
        "category": "russian",
        "order": 32,
        "summary": (
            "Toʻldiruvchi kelishigi — oʻzbekcha -NI ning aynan oʻzi. Yagona yangi "
            "narsa: erkak jinsida ot JONLI yoki JONSIZ ekaniga qarab boshqacha "
            "oʻzgaradi."
        ),
        "stories": ["Кто кого ждёт?"],
        "content": """
<h2>PR-32: Винительный 1: кого? что? — jonli va jonsiz farqi</h2>

<p>Bugungi kelishik butun blokdagi <b>eng tanish</b> kelishik. Oʻzbekchada
<em>kitob<b>ni</b> oʻqiyman</em> deysiz — ruschada <em>чита́ю кни́г<b>у</b></em>.
Bir xil ish, bir xil joyda. Sizga faqat qoʻshimchani almashtirish qoladi. Va
bitta yangi narsa bor, u oʻzbekchada yoʻq: rus tili <b>jonli</b> va
<b>jonsiz</b> otni ajratadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Toʻldiruvchini yasaysiz: <b>кни́га → кни́гу</b></li>
    <li>Oʻrta jins umuman oʻzgarmasligini bilasiz</li>
    <li>Erkak jinsida <b>jonli/jonsiz</b> farqini oʻrganasiz</li>
    <li>Olmoshlarni yodlaysiz: <b>меня́, тебя́, его́, её</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻldiruvchi</span>
  <span class="pe-chip pe-chip--s">Я чита́ю</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">кни́г<b>у</b></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">kitob<b>ni</b> oʻqiyman</span>
</div>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Savoli</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__q">кто? что?</td>
      <td class="pr-case__word">кни́га</td><td class="pr-case__uz">bosh kelishik — kitob</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Вини́тельный</td>
      <td class="pr-case__q">кого́? что?</td>
      <td class="pr-case__word">кни́г<span class="pr-end">у</span></td>
      <td class="pr-case__uz">tushum kelishigi — kitob<b>ni</b></td></tr>
</table></div>

<h3>1. Uchta jins, uchta xatti-harakat</h3>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">jonli/jonsizga qarab</p>
    <p>Jonsiz: <b>oʻzgarmaydi</b> — <em>стол → стол</em>.<br>
       Jonli: <b>-а / -я</b> oladi — <em>брат → бра́та</em>.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">-а → <span class="pr-end">у</span></p>
    <p>Har doim, jonli boʻlsa ham: <em>кни́га → кни́гу</em>,
       <em>Афсо́на → Афсо́ну</em>. <em>-я → -ю</em>: <em>Ка́тя → Ка́тю</em>.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">oʻzgarmaydi</p>
    <p>Hech qachon, hech qanday holatda: <em>окно́ → окно́</em>,
       <em>письмо́ → письмо́</em>, <em>мо́ре → мо́ре</em>.</p>
  </div>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Jadvalni teskari tomondan oʻqing va u ancha yengil boʻlib qoladi:
<b>uchta holatdan ikkitasida hech narsa qilmaysiz</b>. Oʻrta jins —
oʻzgarmaydi. Jonsiz erkak — oʻzgarmaydi. Yaʼni ishlash kerak boʻlgan joy
faqat ikkita: <b>ayol jinsi</b> (har doim <em>-у/-ю</em>) va <b>jonli
erkak</b> (<em>-а/-я</em>).</div>

<h3>2. Ayol jinsi — eng oddiy qism</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Bosh shakl</th><th>Toʻldiruvchi</th><th>Gapda</th></tr>
  <tr><td class="pr-res">кни́га</td><td class="pr-end">кни́гу</td>
      <td class="pr-uz">Я чита́ю кни́гу.</td></tr>
  <tr><td class="pr-res">му́зыка</td><td class="pr-end">му́зыку</td>
      <td class="pr-uz">Мы слу́шаем му́зыку.</td></tr>
  <tr><td class="pr-res">ма́ма</td><td class="pr-end">ма́му</td>
      <td class="pr-uz">Я люблю́ ма́му.</td></tr>
  <tr><td class="pr-res">Афсо́на</td><td class="pr-end">Афсо́ну</td>
      <td class="pr-uz">Жасу́р ждёт Афсо́ну.</td></tr>
  <tr><td class="pr-res">Ка́тя</td><td class="pr-end">Ка́тю</td>
      <td class="pr-uz">Я ви́жу Ка́тю.</td></tr>
  <tr><td class="pr-res">неде́ля</td><td class="pr-end">неде́лю</td>
      <td class="pr-uz">Я ждал неде́лю.</td></tr>
</table></div>

<p>Eʼtibor bering: <em>ма́ма</em> va <em>Афсо́на</em> — jonli, <em>кни́га</em>
va <em>му́зыка</em> — jonsiz, lekin qoʻshimcha <b>bir xil</b>. Ayol jinsida
jonli/jonsiz farqi <b>umuman ishlamaydi</b>.</p>

<h3>3. Erkak jinsi — jonli mi, jonsizmi?</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Jonsiz — hech narsa qilinmaydi</p>
    <p><em>Я ви́жу <b>стол</b>.</em> — Stolni koʻryapman.<br>
       <em>Я чита́ю <b>журна́л</b>.</em><br>
       <em>Мы ждём <b>авто́бус</b>.</em></p>
    <p>Shakl <b>bosh kelishik bilan bir xil</b>.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Jonli — <b>-а / -я</b> qoʻshiladi</p>
    <p><em>Я ви́жу <b>бра́та</b>.</em> — Akamni koʻryapman.<br>
       <em>Я жду <b>Жасу́ра</b>.</em><br>
       <em>Мы зна́ем <b>учи́теля</b>.</em></p>
    <p>Shakl <b>Роди́тельный bilan bir xil</b> (PR-34).</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Bosh shakl</th><th>Jonlimi?</th><th>Toʻldiruvchi</th><th>Gapda</th></tr>
  <tr><td class="pr-res">стол</td><td class="pr-uz">yoʻq</td>
      <td class="pr-end">стол</td><td class="pr-uz">Я ви́жу стол.</td></tr>
  <tr><td class="pr-res">дом</td><td class="pr-uz">yoʻq</td>
      <td class="pr-end">дом</td><td class="pr-uz">Я ви́жу дом.</td></tr>
  <tr><td class="pr-res">по́езд</td><td class="pr-uz">yoʻq</td>
      <td class="pr-end">по́езд</td><td class="pr-uz">Оле́г ждёт по́езд.</td></tr>
  <tr><td class="pr-res">брат</td><td class="pr-uz">ha</td>
      <td class="pr-end">бра́та</td><td class="pr-uz">Я жду бра́та.</td></tr>
  <tr><td class="pr-res">Жасу́р</td><td class="pr-uz">ha</td>
      <td class="pr-end">Жасу́ра</td><td class="pr-uz">Бекзо́д ждёт Жасу́ра.</td></tr>
  <tr><td class="pr-res">учи́тель</td><td class="pr-uz">ha</td>
      <td class="pr-end">учи́теля</td><td class="pr-uz">Мы зна́ем учи́теля.</td></tr>
  <tr><td class="pr-res">оте́ц</td><td class="pr-uz">ha</td>
      <td class="pr-end">отца́</td><td class="pr-uz">Я ви́жу отца́. <em>(Е tushib qoladi)</em></td></tr>
  <tr><td class="pr-res">кот</td><td class="pr-uz">ha</td>
      <td class="pr-end">кота́</td><td class="pr-uz">Я люблю́ кота́.</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Jonli</b> (одушевлённое) = odam yoki hayvon. Boshqa hamma narsa —
<b>jonsiz</b> (неодушевлённое). Chegara sof grammatik: <em>кот</em>,
<em>соба́ка</em>, <em>ры́ба</em> — jonli. <em>Наро́д</em> (xalq),
<em>класс</em> (sinf) — odamlardan iborat, lekin grammatik jihatdan
<b>jonsiz</b>, chunki ular guruhni bildiradi.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu kelishik oʻzbekcha <b>-NI</b> ning aynan oʻzi, va bu blokdagi eng aniq
moslik. Lekin ikkita farq bor.<br><br>
<b>Birinchi:</b> oʻzbekcha <em>-ni</em> hamma soʻz uchun bitta.
<em>Kitob<b>ni</b>, aka<b>ni</b>, deraza<b>ni</b></em> — farq yoʻq. Ruschada esa
jins va jonlilik shaklni tanlaydi.<br><br>
<b>Ikkinchi va ancha muhimi:</b> oʻzbekchada <em>-ni</em> ni <b>tushirib
qoldirish mumkin</b>. <em>Kitob oʻqiyapman</em> — toʻgʻri gap (aniq boʻlmagan
kitob). <em>Kitobni oʻqiyapman</em> — aniq kitob. Rus tilida bunday tanlov
<b>yoʻq</b>: toʻldiruvchi har doim kelishikka kiradi.
<em>«Я чита́ю кни́га»</em> — hech qanday holatda toʻgʻri emas. Oʻzbek oʻquvchi
aynan shu odat tufayli qoʻshimchani unutadi.</div>

<h3>4. Olmoshlar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Olmosh</th><th>Toʻldiruvchi</th><th>Gapda</th><th>Oʻzbekcha</th></tr>
  <tr><td>я</td><td class="pr-res">меня́</td>
      <td class="pr-end">Он зна́ет меня́.</td><td class="pr-uz">meni</td></tr>
  <tr><td>ты</td><td class="pr-res">тебя́</td>
      <td class="pr-end">Я жду тебя́.</td><td class="pr-uz">seni</td></tr>
  <tr><td>он / оно́</td><td class="pr-res">его́</td>
      <td class="pr-end">Мы ви́дим его́.</td><td class="pr-uz">uni (erkak)</td></tr>
  <tr><td>она́</td><td class="pr-res">её</td>
      <td class="pr-end">Я люблю́ её.</td><td class="pr-uz">uni (ayol)</td></tr>
  <tr><td>мы</td><td class="pr-res">нас</td>
      <td class="pr-end">Они́ ждут нас.</td><td class="pr-uz">bizni</td></tr>
  <tr><td>вы</td><td class="pr-res">вас</td>
      <td class="pr-end">Я слу́шаю вас.</td><td class="pr-uz">sizni</td></tr>
  <tr><td>они́</td><td class="pr-res">их</td>
      <td class="pr-end">Ты зна́ешь их?</td><td class="pr-uz">ularni</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<em>Его́</em> soʻzi <b>[йиво́]</b> deb oʻqiladi — <b>Г</b> harfi bu yerda
<b>[в]</b> tovushini beradi. Bu rus tilining eski qoidasi va u
<em>его́, сего́дня, ничего́</em> soʻzlarida saqlanib qolgan. Yozilishi
<b>Г</b>, oʻqilishi <b>[в]</b>.</div>

<div class="pr-say">
  <span class="pr-say__from">его́</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[йиво́]</span>
  <span class="pr-say__why">Г → [в] — eski qoidaning qoldigʻi</span>
</div>

<h3>5. Qaysi feʼllar toʻldiruvchi oladi</h3>

<p>Aksariyat feʼllar. Ular oʻzbekchada ham <em>-ni</em> bilan ishlaydi,
shuning uchun tekshirish oson:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Koʻrish va bilish</p>
    <p><em>ви́деть</em> · <em>знать</em> · <em>по́мнить</em> · <em>слу́шать</em><br>
       <em>Я ви́жу Афсо́ну. Я по́мню э́то.</em></p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Qilish</p>
    <p><em>чита́ть</em> · <em>писа́ть</em> · <em>де́лать</em> · <em>учи́ть</em><br>
       <em>Он пи́шет письмо́. Я учу́ ру́сский язы́к.</em></p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>His-tuygʻu</p>
    <p><em>люби́ть</em> · <em>ждать</em> · <em>слы́шать</em><br>
       <em>Я люблю́ ма́му. Мы ждём авто́бус.</em></p></div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я чита́ю кни́га.</s></p>
  <p class="pe-good">Я чита́ю <b>кни́гу</b> — toʻldiruvchi har doim kelishikka kiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ви́жу Жасу́р.</s></p>
  <p class="pe-good">Я ви́жу <b>Жасу́ра</b> — jonli erkak, demak <b>-а</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ви́жу стола́.</s></p>
  <p class="pe-good">Я ви́жу <b>стол</b> — jonsiz, demak hech narsa qoʻshilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я жду ты.</s></p>
  <p class="pe-good">Я жду <b>тебя́</b> — olmosh ham kelishikka kiradi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он пи́шет письма́.</s> <em>(bitta xat maʼnosida)</em></p>
  <p class="pe-good">Он пи́шет <b>письмо́</b> — oʻrta jins umuman oʻzgarmaydi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Мы слу́шаем ___.</b> (му́зыка)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>му́зыку</strong>. Ayol jinsi, demak
    <b>-а → -у</b>. Jonli/jonsiz bu yerda ahamiyatsiz — ayol jinsida u
    umuman ishlamaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Бекзо́д ждёт ___.</b> (Жасу́р)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Жасу́ра</strong>. Jasur — odam,
    demak jonli erkak, demak <b>-а</b>. Agar avtobus kutayotgan boʻlsa,
    hech narsa qoʻshilmasdi: <em>ждёт авто́бус</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapdan qaysi biri oʻzgardi, qaysi biri yoʻq?<br>
     <b>Я ви́жу стол. · Я ви́жу бра́та.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><em>Стол</em> — <strong>oʻzgarmadi</strong>
    (jonsiz). <em>Брат → бра́та</em> — <strong>oʻzgardi</strong> (jonli).
    Ikkalasi ham erkak jinsida; farqni faqat jonlilik hal qildi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni ruschaga oʻgiring: <b>Men seni kutyapman.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я жду тебя́.</strong> Olmoshlar ham
    kelishikka kiradi: <em>меня́, тебя́, его́, её, нас, вас, их</em>.
    <em>«Я жду ты»</em> — xato.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Я чита́ю письмо́. &nbsp; б) Она́ лю́бит кота́.<br>
     в) Мы ждём по́езда. &nbsp; г) Он зна́ет Ка́тю.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Мы ждём по́езд</b>. Poyezd jonsiz, demak shakl oʻzgarmaydi. Qolgan
    uchtasi toʻgʻri: <em>письмо́</em> (oʻrta jins), <em>кота́</em> (jonli
    hayvon), <em>Ка́тю</em> (ayol jinsi).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>кого́? что?</b><span>kimni? nimani?</span></li>
  <li><b>одушевлённый</b><span>jonli</span></li>
  <li><b>неодушевлённый</b><span>jonsiz</span></li>
  <li><b>ждать</b><span>kutmoq</span></li>
  <li><b>ви́деть</b><span>koʻrmoq</span></li>
  <li><b>по́езд</b><span>poyezd</span></li>
  <li><b>вокза́л</b><span>vokzal</span></li>
  <li><b>учи́тель</b><span>oʻqituvchi</span></li>
  <li><b>оте́ц</b><span>ota</span></li>
  <li><b>ве́щь</b><span>narsa, buyum</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Вини́тельный = toʻldiruvchi = oʻzbekcha <b>-NI</b>.</li>
    <li><b>Oʻrta jins</b> hech qachon oʻzgarmaydi: <em>окно́, письмо́,
        мо́ре</em>.</li>
    <li><b>Ayol jinsi</b> har doim <b>-у / -ю</b>: <em>кни́гу, Афсо́ну,
        Ка́тю</em>.</li>
    <li><b>Erkak jinsi</b> jonlilikka qaraydi: jonsiz — oʻzgarmaydi
        (<em>стол</em>), jonli — <b>-а / -я</b> (<em>бра́та</em>).</li>
    <li>Jonli = odam yoki hayvon. Boshqa hammasi jonsiz.</li>
    <li>Olmoshlar: <b>меня́, тебя́, его́, её, нас, вас, их</b>.
        <em>Его́</em> = [йиво́].</li>
    <li>Oʻzbekchada <em>-ni</em> ni tushirib qoldirish mumkin, ruschada
        <b>hech qachon</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-33: Винительный 2: yoʻnalish — в школу, на работу, куда?",
        "category": "russian",
        "order": 33,
        "summary": (
            "Oʻsha kelishik, ikkinchi ishi: harakatning manzili. Bu dars PR-30 bilan "
            "yonma-yon turadi va rus tilidagi eng chiroyli juftlikni ochadi: "
            "в шко́ле ↔ в шко́лу."
        ),
        "stories": ["Куда идёт этот автобус?"],
        "content": """
<h2>PR-33: Винительный 2: yoʻnalish — в школу, на работу, куда?</h2>

<p>PR-29 da bir gap aytilgan edi: «bitta predlog ikkita kelishik bilan
ishlashi mumkin». Bugun oʻsha gap toʻliq ochiladi. <em>В шко́л<b>е</b></em> —
maktabda<b>man</b>. <em>В шко́л<b>у</b></em> — maktab<b>ga</b> ketyapman.
Predlog bir xil, feʼl boshqa, va <b>butun maʼnoni bitta harf hal
qiladi</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>«Qayerga?» degan savolga javob berasiz: <b>в шко́лу, на рабо́ту</b></li>
    <li><b>Где?</b> va <b>куда́?</b> ni ajratasiz</li>
    <li>Predlog PR-30 dagidek qolishini bilasiz — bu katta yengillik</li>
    <li>Ravishlarni juftlaysiz: <b>до́ма ↔ домо́й</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qayerga?</span>
  <span class="pe-chip pe-chip--v">в / на</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">шко́л</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">у</span>
</div>

<h3>1. Butun dars bitta jadvalda</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Bosh shakl</th><th>Где? (PR-30)</th><th>Куда́? (bugun)</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">шко́ла</td><td class="pr-uz">в шко́л<b>е</b></td>
      <td class="pr-end">в шко́л<b>у</b></td><td class="pr-uz">maktabda / maktabga</td></tr>
  <tr><td class="pr-res">рабо́та</td><td class="pr-uz">на рабо́т<b>е</b></td>
      <td class="pr-end">на рабо́т<b>у</b></td><td class="pr-uz">ishda / ishga</td></tr>
  <tr><td class="pr-res">Москва́</td><td class="pr-uz">в Москв<b>е́</b></td>
      <td class="pr-end">в Москв<b>у́</b></td><td class="pr-uz">Moskvada / Moskvaga</td></tr>
  <tr><td class="pr-res">дере́вня</td><td class="pr-uz">в дере́вн<b>е</b></td>
      <td class="pr-end">в дере́вн<b>ю</b></td><td class="pr-uz">qishloqda / qishloqqa</td></tr>
  <tr><td class="pr-res">магази́н</td><td class="pr-uz">в магази́н<b>е</b></td>
      <td class="pr-end">в магази́н</td><td class="pr-uz">doʻkonda / doʻkonga</td></tr>
  <tr><td class="pr-res">ры́нок</td><td class="pr-uz">на ры́нк<b>е</b></td>
      <td class="pr-end">на ры́нок</td><td class="pr-uz">bozorda / bozorga</td></tr>
  <tr><td class="pr-res">уро́к</td><td class="pr-uz">на уро́к<b>е</b></td>
      <td class="pr-end">на уро́к</td><td class="pr-uz">darsda / darsga</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Jadvalning pastki uch qatoriga qarang: <em>магази́н, ры́нок, уро́к</em> —
«qayerga?» ustunida ular <b>umuman oʻzgarmagan</b>. Sababi PR-32 dan:
bular <b>jonsiz erkak</b> otlar, va ularning Вини́тельный shakli bosh
kelishik bilan bir xil. Yaʼni sizga faqat predlogni qoʻyish qoladi:
<em>иду́ <b>в</b> магази́н</em>.</div>

<h3>2. Predlog oʻzgarmaydi — bu eng yaxshi xabar</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Agar soʻz «qayerda?» da <b>на</b> olsa, u «qayerga?» da ham <b>на</b> oladi.
Agar <b>в</b> olsa — har doim <b>в</b>.<br>
<em>на рабо́т<b>е</b> → на рабо́т<b>у</b></em><br>
<em>в шко́л<b>е</b> → в шко́л<b>у</b></em><br>
Yaʼni PR-30 da yodlagan НА-roʻyxatingiz <b>oʻzgarishsiz ishlaydi</b>. Yangi
roʻyxat yodlash kerak emas — faqat qoʻshimchani almashtirasiz.</div>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Где? — <b>Предло́жный</b></p>
    <p>Feʼl: <em>быть, жить, рабо́тать, учи́ться</em></p>
    <p><em>Я <b>в шко́ле</b>.</em><br>
       <em>Ма́ма <b>на рабо́те</b>.</em><br>
       <em>Мы <b>в Москве́</b>.</em></p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Куда́? — <b>Вини́тельный</b></p>
    <p>Feʼl: <em>идти́, е́хать, ходи́ть</em></p>
    <p><em>Я иду́ <b>в шко́лу</b>.</em><br>
       <em>Ма́ма е́дет <b>на рабо́ту</b>.</em><br>
       <em>Мы е́дем <b>в Москву́</b>.</em></p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu dars siz oʻylagandan ancha tanish, faqat uni toʻgʻri koʻrish kerak.
Oʻzbekchada ham bu farq <b>otning oxirida</b> koʻrsatiladi:<br>
<em>maktab<b>DA</b></em> (qayerda) &nbsp;↔&nbsp; <em>maktab<b>GA</b></em> (qayerga)<br>
<em>в шко́л<b>Е</b></em> &nbsp;↔&nbsp; <em>в шко́л<b>У</b></em><br><br>
Ikkala tilda ham <b>qoʻshimcha</b> ishlaydi. Ruschadagi predlog esa —
qoʻshimcha shovqin: u ikkala holatda ham bir xil va hech narsani hal
qilmaydi. Shuning uchun ruscha gapni tuzayotganda <b>predlogga emas,
oxiriga qarang</b>: aynan u «da» mi yoki «ga» mi ekanini aytadi.</div>

<h3>3. Ravishlar — uchlik</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Где?</th><th>Куда́?</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">до́ма</td><td class="pr-end">домо́й</td>
      <td class="pr-uz">uyda / uyga</td></tr>
  <tr><td class="pr-res">здесь</td><td class="pr-end">сюда́</td>
      <td class="pr-uz">bu yerda / bu yerga</td></tr>
  <tr><td class="pr-res">там</td><td class="pr-end">туда́</td>
      <td class="pr-uz">u yerda / u yerga</td></tr>
  <tr><td class="pr-res">где?</td><td class="pr-end">куда́?</td>
      <td class="pr-uz">qayerda? / qayerga?</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ru">— <span class="pe-hl pe-hl--v">Куда́</span> ты идёшь?<br>
     — <span class="pe-hl pe-hl--adv">Домо́й</span>. А ты?<br>
     — Я <span class="pe-hl pe-hl--adv">до́ма</span>. Уже́.</p>
  <p class="pe-ex__uz">— Qayerga ketyapsan?<br>— Uyga. Sen-chi?<br>— Men
     uydaman. Allaqachon.</p>
  <p class="pe-ex__why">Ikkita soʻz, bitta ildiz, ikki xil ish. Rus tilida bu
     juftlik hech qachon aralashmaydi.</p>
</div>

<h3>4. Bonus: «в» + Вини́тельный = vaqt</h3>

<p>Xuddi shu qurilish <b>vaqt</b> uchun ham ishlatiladi — va siz uni
PR-9 dan beri ishlatib kelyapsiz, bilmasdan:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Bosh shakl</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">в суббо́ту</td><td class="pr-uz">суббо́та</td>
      <td class="pr-uz">shanba kuni</td></tr>
  <tr><td class="pr-res">в сре́ду</td><td class="pr-uz">среда́</td>
      <td class="pr-uz">chorshanba kuni</td></tr>
  <tr><td class="pr-res">в понеде́льник</td><td class="pr-uz">понеде́льник</td>
      <td class="pr-uz">dushanba kuni</td></tr>
  <tr><td class="pr-res">в два часа́</td><td class="pr-uz">два часа́</td>
      <td class="pr-uz">soat ikkida</td></tr>
</table></div>

<p><em>Понеде́льник</em> — jonsiz erkak, shuning uchun oʻzgarmadi.
<em>Суббо́та</em> — ayol jinsi, shuning uchun <em>суббо́т<b>у</b></em>. Yaʼni
yangi qoida yoʻq, oʻsha kelishikning yana bir ishi.</p>

<h3>5. Gaplarda</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">У́тром Жасу́р <span class="pe-hl pe-hl--v">идёт</span>
     <span class="pe-hl pe-hl--o">в шко́лу</span>, а ве́чером он
     <span class="pe-hl pe-hl--v">рабо́тает</span>
     <span class="pe-hl pe-hl--adv">в магази́не</span>.</p>
  <p class="pe-ex__uz">Ertalab Jasur maktabga boradi, kechqurun esa doʻkonda
     ishlaydi.</p>
  <p class="pe-ex__why">Bitta gapda ikkala kelishik ham bor. Feʼllarga
     qarang: <em>идёт</em> — harakat, demak «qayerga»; <em>рабо́тает</em> —
     harakat emas, demak «qayerda».</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--adv">В суббо́ту</span> мы
     <span class="pe-hl pe-hl--v">е́дем</span>
     <span class="pe-hl pe-hl--o">в дере́вню</span>.</p>
  <p class="pe-ex__uz">Shanba kuni qishloqqa boramiz.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ в шко́ле.</s></p>
  <p class="pe-good">Я иду́ <b>в шко́лу</b> — harakat bor, demak «qayerga»</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я рабо́таю на рабо́ту.</s></p>
  <p class="pe-good">Я рабо́таю <b>на рабо́те</b> — harakat yoʻq, demak «qayerda»</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я иду́ до́ма.</s></p>
  <p class="pe-good">Я иду́ <b>домо́й</b> — «qayerga» uchun boshqa ravish</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы е́дем в рабо́ту.</s></p>
  <p class="pe-good">Мы е́дем <b>на рабо́ту</b> — predlog PR-30 dagidek qoladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он идёт в магази́на.</s></p>
  <p class="pe-good">Он идёт <b>в магази́н</b> — jonsiz erkak oʻzgarmaydi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Ма́ма е́дет ___ (рабо́та).</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>на рабо́ту</strong>. Feʼl
    <em>е́дет</em> — harakat, demak «qayerga». Predlog PR-30 dagidek
    <b>на</b>, qoʻshimcha esa <b>-у</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Он идёт ___ (ры́нок).</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>на ры́нок</strong> — soʻz
    <b>oʻzgarmaydi</b>! <em>Ры́нок</em> jonsiz erkak ot, uning Вини́тельный
    shakli bosh kelishik bilan bir xil. Solishtiring: <em>на ры́нк<b>е</b></em>
    (qayerda).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapni tarjima qiling.<br>
     <b>Я в Москве́. · Я е́ду в Москву́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Moskvadaman</strong> ·
    <strong>Moskvaga ketyapman</strong>. Predlog bir xil, feʼl boshqa, va
    butun maʼnoni oxirgi harf hal qildi: <b>-е</b> = joy, <b>-у</b> =
    manzil.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>до́ма</b> yoki <b>домо́й</b>? &nbsp; <b>По́здно. Я иду́ ___.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>домо́й</strong>. Feʼl
    <em>иду́</em> — harakat, demak «qayerga» kerak. <em>До́ма</em> esa
    «qayerda»: <em>Я до́ма</em> — uydaman.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) В суббо́ту мы е́дем в дере́вню. &nbsp; б) Он рабо́тает в магази́не.<br>
     в) Я иду́ на уро́ке. &nbsp; г) Ба́бушка живёт в дере́вне.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Я иду́ на уро́к</b>. Feʼl <em>иду́</em> harakatni bildiradi, demak
    «qayerga» kerak; <em>уро́к</em> esa jonsiz erkak, shuning uchun shakl
    oʻzgarmaydi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>куда́?</b><span>qayerga?</span></li>
  <li><b>домо́й</b><span>uyga</span></li>
  <li><b>сюда́</b><span>bu yerga</span></li>
  <li><b>туда́</b><span>u yerga</span></li>
  <li><b>в шко́лу</b><span>maktabga</span></li>
  <li><b>на рабо́ту</b><span>ishga</span></li>
  <li><b>води́тель</b><span>haydovchi</span></li>
  <li><b>остано́вка</b><span>bekat</span></li>
  <li><b>в суббо́ту</b><span>shanba kuni</span></li>
  <li><b>непра́вильно</b><span>notoʻgʻri</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Oʻsha Вини́тельный, ikkinchi ishi: <b>manzil</b>.</li>
    <li><b>Где?</b> → Предло́жный (<em>-е</em>) · <b>Куда́?</b> →
        Вини́тельный (<em>-у</em>).</li>
    <li><b>Predlog oʻzgarmaydi</b>: <em>на рабо́те → на рабо́ту</em>. PR-30
        dagi roʻyxat oʻz kuchida.</li>
    <li>Jonsiz erkak otlar manzilda ham <b>oʻzgarmaydi</b>:
        <em>в магази́н, на ры́нок, на уро́к</em>.</li>
    <li>Ravishlar juftligi: <b>до́ма ↔ домо́й</b>, <b>здесь ↔ сюда́</b>,
        <b>там ↔ туда́</b>.</li>
    <li>Vaqt ham shu qurilish bilan: <b>в суббо́ту, в понеде́льник</b>.</li>
    <li>Feʼlga qarang: harakat bormi? Bor — «qayerga». Yoʻq —
        «qayerda».</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-34: Родительный 1: egalik va yoʻqlik — книга брата, нет времени",
        "category": "russian",
        "order": 34,
        "summary": (
            "Rus tilidagi eng koʻp ishlatiladigan kelishik boshlanadi. Ikki asosiy "
            "ishi: «kimniki?» va «yoʻq». Egalikda soʻz tartibi oʻzbekchaning "
            "teskarisi — bu darsning eng katta xatosi."
        ),
        "stories": ["Дом моего деда"],
        "content": """
<h2>PR-34: Родительный 1: egalik va yoʻqlik — книга брата, нет времени</h2>

<p>Rus tilidagi <b>eng koʻp ishlatiladigan</b> kelishik shu. Uning ishlari
juda koʻp, shuning uchun unga uchta dars ajratilgan. Bugun ikkitasini
olamiz — va ular ikkalasi ham oʻzbekchada bor: <b>«kimniki?»</b> va
<b>«yoʻq»</b>. Bitta narsani oldindan aytib qoʻyaman: egalikda rus tili
soʻzlarni <b>oʻzbekchaning teskarisiga</b> qoʻyadi. Aynan shu yerda eng koʻp
xato boʻladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Qoʻshimchalarni oʻrganasiz: <b>-а/-я</b> va <b>-ы/-и</b></li>
    <li>Egalikni yasaysiz: <b>кни́га бра́та</b> — akaning kitobi</li>
    <li><b>Нет</b> bilan yoʻqlikni aytasiz: <b>нет вре́мени</b></li>
    <li>Uchala zamonda ishlatasiz: <b>нет · не́ было · не бу́дет</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Egalik</span>
  <span class="pe-chip pe-chip--s">кни́га</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">бра́т<b>а</b></span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">aka<b>ning</b> kitobi</span>
</div>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Savoli</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-case__name">Имени́тельный</td><td class="pr-case__q">кто? что?</td>
      <td class="pr-case__word">брат</td><td class="pr-case__uz">bosh kelishik — aka</td></tr>
  <tr class="pr-case__on"><td class="pr-case__name">Роди́тельный</td>
      <td class="pr-case__q">кого́? чего́?</td>
      <td class="pr-case__word">бра́т<span class="pr-end">а</span></td>
      <td class="pr-case__uz">qaratqich — aka<b>ning</b></td></tr>
</table></div>

<h3>1. Qoʻshimchalar</h3>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">-<span class="pr-end">а</span> / -<span class="pr-end">я</span></p>
    <p><em>брат → бра́та</em><br><em>стол → стола́</em><br>
       <em>учи́тель → учи́теля</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Сре́дний — oʻrta</p>
    <p class="pr-gender__form">-<span class="pr-end">а</span> / -<span class="pr-end">я</span></p>
    <p><em>окно́ → окна́</em><br><em>письмо́ → письма́</em><br>
       <em>мо́ре → мо́ря</em></p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">-<span class="pr-end">ы</span> / -<span class="pr-end">и</span></p>
    <p><em>шко́ла → шко́лы</em><br><em>кни́га → кни́ги</em><br>
       <em>Ка́тя → Ка́ти</em></p>
  </div>
</div>

<p>Erkak va oʻrta jins <b>bir xil</b> — PR-29 da aytilgan gap tasdiqlanyapti.
Yaʼni amalda ikkita naqsh bor: <b>-а/-я</b> va <b>-ы/-и</b>.</p>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Ayol jinsida <b>-ы</b> mi yoki <b>-и</b> mi — buni imlo qoidasi hal qiladi.
<b>Г, К, Х, Ж, Ш, Щ, Ч</b> dan keyin <b>Ы yozilmaydi</b>, uning oʻrniga
<b>И</b> qoʻyiladi:<br>
<em>кни́г<b>а</b> → кни́г<b>и</b></em> (К dan keyin) ·
<em>ру́чка → ру́чки</em> · <em>Ма́ша → Ма́ши</em><br>
<em>шко́ла → шко́лы</em> (Л dan keyin — oddiy Ы) ·
<em>маши́на → маши́ны</em><br>
Bu PR-4 dagi shivirlovchilar qoidasining oʻsha oʻzi. U kelishiklarda
qayta-qayta uchraydi.</div>

<h3>2. Egalik — va soʻz tartibi</h3>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Mana bu darsning eng muhim yarim daqiqasi. Ikkala tilda ham qaratqich bor,
lekin ular <b>qarama-qarshi tomonga qaraydi</b>:<br><br>
Oʻzbekcha: <em><b>aka-NING</b> kitob-<b>i</b></em><br>
&nbsp;&nbsp;→ egasi <b>oldinda</b>, va <b>ikkala soʻz</b> ham belgilanadi
(<em>-ning</em> va <em>-i</em>).<br><br>
Ruscha: <em>кни́га <b>бра́т-А</b></em><br>
&nbsp;&nbsp;→ egasi <b>orqada</b>, va faqat <b>bitta soʻz</b> belgilanadi
(<em>кни́га</em> oʻz holida qoladi).<br><br>
Soʻzma-soʻz oʻgirsak, ruscha «kitob akaning» deyapti. Oʻzbek oʻquvchi
avtomatik ravishda <em>«бра́та кни́га»</em> deb yozib yuboradi — bu esa
ruschada notoʻgʻri. <b>Egasi har doim orqada.</b></div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Soʻzma-soʻz</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">кни́га бра́та</td><td class="pr-uz">kitob akaning</td>
      <td class="pr-end">akaning kitobi</td></tr>
  <tr><td class="pr-res">дом отца́</td><td class="pr-uz">uy otaning</td>
      <td class="pr-end">otaning uyi</td></tr>
  <tr><td class="pr-res">маши́на Жасу́ра</td><td class="pr-uz">mashina Jasurning</td>
      <td class="pr-end">Jasurning mashinasi</td></tr>
  <tr><td class="pr-res">окно́ ку́хни</td><td class="pr-uz">deraza oshxonaning</td>
      <td class="pr-end">oshxonaning derazasi</td></tr>
  <tr><td class="pr-res">центр го́рода</td><td class="pr-uz">markaz shaharning</td>
      <td class="pr-end">shahar markazi</td></tr>
  <tr><td class="pr-res">учи́тель Афсо́ны</td><td class="pr-uz">oʻqituvchi Afsonaning</td>
      <td class="pr-end">Afsonaning oʻqituvchisi</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ru">Э́то <span class="pe-hl pe-hl--s">дом</span>
     <span class="pe-hl pe-hl--o">де́да</span>. А э́то
     <span class="pe-hl pe-hl--s">кни́га</span>
     <span class="pe-hl pe-hl--o">ба́бушки</span>.</p>
  <p class="pe-ex__uz">Bu — bobomning uyi. Bu esa buvimning kitobi.</p>
  <p class="pe-ex__why">Ikkala gapda ham egalik bildiruvchi soʻz
     <b>ikkinchi</b> turibdi va aynan u kelishikka kirgan. Birinchi soʻz —
     bosh kelishikda.</p>
</div>

<h3>3. Нет + Роди́тельный — yoʻqlik</h3>

<p>PR-14 da siz <em>У меня́ есть…</em> ni oʻrgangansiz. Uning inkori
<b>«нет» emas, «нет + Роди́тельный»</b>:</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Bor — bosh kelishik</p>
    <p><em>У меня́ есть <b>кни́га</b>.</em><br>Menda kitob bor.</p>
    <p><em>Здесь есть <b>магази́н</b>.</em></p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Yoʻq — Роди́тельный</p>
    <p><em>У меня́ нет <b>кни́ги</b>.</em><br>Menda kitob yoʻq.</p>
    <p><em>Здесь нет <b>магази́на</b>.</em></p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada bu joyda hech narsa oʻzgarmaydi: <em>Menda kitob <b>bor</b></em>
→ <em>Menda kitob <b>yoʻq</b></em>. Ot ikkala gapda ham bir xil.<br>
Ruschada esa <b>oʻzgaradi</b>: <em>есть кни́г<b>а</b></em> →
<em>нет кни́г<b>и</b></em>. Bu mantiqsiz tuyulishi mumkin, lekin qoida
qatʼiy: <b>«нет» dan keyin har doim Роди́тельный</b>. Uni <em>нет</em> bilan
bitta boʻlak qilib yodlang — <em>нет вре́мени</em>, <em>нет де́нег</em>,
<em>нет пробле́м</em> — shunda oʻylab oʻtirmaysiz.</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Bosh shakl</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">нет вре́мени</td><td class="pr-uz">вре́мя</td>
      <td class="pr-uz">vaqt yoʻq</td></tr>
  <tr><td class="pr-res">нет воды́</td><td class="pr-uz">вода́</td>
      <td class="pr-uz">suv yoʻq</td></tr>
  <tr><td class="pr-res">нет рабо́ты</td><td class="pr-uz">рабо́та</td>
      <td class="pr-uz">ish yoʻq</td></tr>
  <tr><td class="pr-res">нет отве́та</td><td class="pr-uz">отве́т</td>
      <td class="pr-uz">javob yoʻq</td></tr>
  <tr><td class="pr-res">нет интерне́та</td><td class="pr-uz">интерне́т</td>
      <td class="pr-uz">internet yoʻq</td></tr>
  <tr><td class="pr-res">нет пробле́мы</td><td class="pr-uz">пробле́ма</td>
      <td class="pr-uz">muammo yoʻq</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
<em>Вре́мя</em> — alohida turadigan ot. U <b>-мя</b> ga tugaydigan kichik
guruhdan (<em>вре́мя, и́мя, зна́мя</em>) va Роди́тельный'da
<b>вре́мени</b> boʻladi, <em>«вре́мя»</em> yoki <em>«вре́ма»</em> emas.
<em>Нет вре́мени</em> — rus tilida eng koʻp aytiladigan iboralardan biri,
uni butunligicha yodlang.</div>

<h3>4. Uchala zamonda</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Zamon</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td class="pr-uz">Hozir</td><td class="pr-res">нет</td>
      <td class="pr-end">Сего́дня нет дождя́.</td></tr>
  <tr><td class="pr-uz">Kecha</td><td class="pr-res">не́ было</td>
      <td class="pr-end">Вчера́ не́ было дождя́.</td></tr>
  <tr><td class="pr-uz">Ertaga</td><td class="pr-res">не бу́дет</td>
      <td class="pr-end">За́втра не бу́дет дождя́.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Oʻtgan zamonda har doim <b>не́ было</b> — oʻrta jinsda, jinsdan qatʼi nazar.
<em>Вчера́ не́ было <b>воды́</b></em> (ayol), <em>не́ было
<b>дождя́</b></em> (erkak), <em>не́ было <b>вре́мени</b></em> (oʻrta) —
hammasida <b>бы́ло</b>. Sababi PR-27 dan tanish: bu <b>shaxssiz gap</b>, unda
ega yoʻq. Urgʻuga ham eʼtibor bering: <b>не́ было</b> — urgʻu
<em>не</em> ga tushadi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Бра́та кни́га.</s></p>
  <p class="pe-good"><b>Кни́га бра́та</b> — egasi har doim orqada</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>У меня́ нет кни́га.</s></p>
  <p class="pe-good">У меня́ нет <b>кни́ги</b> — «нет» dan keyin Роди́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>У меня́ нет вре́мя.</s></p>
  <p class="pe-good">У меня́ нет <b>вре́мени</b> — <em>-мя</em> otlari alohida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Вчера́ не́ был дождь.</s></p>
  <p class="pe-good">Вчера́ <b>не́ было дождя́</b> — shaxssiz gap, oʻrta jins + Роди́тельный</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кни́га бра́т.</s></p>
  <p class="pe-good">Кни́га <b>бра́та</b> — egasi kelishikka kiradi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu iborani ruschaga oʻgiring: <b>Afsonaning kitobi.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Кни́га Афсо́ны.</strong> Ikkita
    narsa: soʻz tartibi <b>teskari</b> (kitob oldinda), va egasi
    Роди́тельный'da — <em>Афсо́на → Афсо́ны</em> (ayol jinsi,
    <b>-ы</b>).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>У меня́ нет ___.</b> (маши́на)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>маши́ны</strong>. «Нет» dan keyin
    har doim Роди́тельный. Ayol jinsi, Н dan keyin oddiy <b>-ы</b>.
    Solishtiring: <em>У меня́ есть маши́на</em> — bosh kelishikda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>-ы</b> yoki <b>-и</b>? &nbsp; <b>кни́га → нет ___</b> ·
     <b>шко́ла → нет ___</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>кни́ги</strong> ·
    <strong>шко́лы</strong>. <em>Кни́га</em> ning oʻzagi <b>К</b> ga
    tugaydi, K dan keyin esa Ы yozilmaydi — demak <b>-и</b>.
    <em>Шко́ла</em> ning oʻzagi <b>Л</b> ga tugaydi, demak oddiy
    <b>-ы</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni oʻtgan zamonga oʻtkazing: <b>Сего́дня нет дождя́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Вчера́ не́ было дождя́.</strong>
    Shaxssiz gap, shuning uchun <em>быть</em> har doim oʻrta jinsda —
    <b>не́ было</b>, hatto <em>дождь</em> erkak jinsida boʻlsa ham. Ot esa
    Роди́тельный'da qoladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Э́то дом отца́. &nbsp; б) У нас нет вре́мени.<br>
     в) Бра́та маши́на но́вая. &nbsp; г) Здесь нет магази́на.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Маши́на бра́та но́вая</b>. Egalik bildiruvchi soʻz har doim
    <b>orqada</b> turadi. Oʻzbekcha tartibni («akaning mashinasi») ruschaga
    koʻchirish — bu darsdagi eng koʻp uchraydigan xato.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>кого́? чего́?</b><span>kimning? nimaning?</span></li>
  <li><b>нет + Р.п.</b><span>yoʻq</span></li>
  <li><b>не́ было</b><span>yoʻq edi</span></li>
  <li><b>вре́мя → вре́мени</b><span>vaqt</span></li>
  <li><b>дед</b><span>bobo</span></li>
  <li><b>оте́ц → отца́</b><span>ota</span></li>
  <li><b>центр</b><span>markaz</span></li>
  <li><b>ти́шина</b><span>sukunat</span></li>
  <li><b>за́пах</b><span>hid</span></li>
  <li><b>де́ньги</b><span>pul</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Erkak va oʻrta: <b>-а / -я</b>. Ayol: <b>-ы / -и</b>.</li>
    <li>Г, К, Х, Ж, Ш, Щ, Ч dan keyin <b>-и</b>, <b>-ы</b> emas:
        <em>кни́ги, ру́чки</em>.</li>
    <li>Egalikda egasi <b>orqada</b>: <em>кни́га бра́та</em> — oʻzbekchaning
        <b>teskarisi</b>.</li>
    <li>Faqat <b>bitta</b> soʻz belgilanadi — <em>кни́га</em> oʻz holida
        qoladi.</li>
    <li><b>Нет</b> dan keyin har doim Роди́тельный: <em>нет вре́мени, нет
        воды́</em>.</li>
    <li>Zamonlar: <b>нет · не́ было · не бу́дет</b> — hammasi oʻrta
        jinsda.</li>
    <li><em>Вре́мя → вре́мени</em> — alohida yodlanadi.</li>
  </ul>
</div>
""",
    },
]
