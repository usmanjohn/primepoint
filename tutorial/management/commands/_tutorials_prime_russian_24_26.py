# -*- coding: utf-8 -*-
"""Prime Russian — Block C yakuni (24–26).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-24 kelasi zamonni beradi (shu bilan uchala zamon yigʻiladi), PR-25
qaytim feʼllarni, PR-26 esa «-a olmoq» ning ikki turini.

Urgʻu siyosati: faqat YANGI va urgʻusi KOʻCHADIGAN soʻzlarga belgi.

Mashqlar:        practice/management/commands/_practice_pr_24_26.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_24_26.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_24_26.py --author=prime
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
        "title": "PR-24: Kelasi zamon: буду + infinitiv",
        "category": "russian",
        "order": 24,
        "summary": (
            "Kelasi zamon ikki soʻzdan yasaladi: бу́ду + infinitiv. Shu dars bilan "
            "uchala zamon — kecha, bugun, ertaga — qoʻlingizda boʻladi."
        ),
        "stories": ["Завтра экзамен"],
        "content": """
<h2>PR-24: Kelasi zamon: буду + infinitiv</h2>

<p>Kecha siz «kecha» ni ochdingiz. Bugun «ertaga» ni ochasiz — va shundan keyin
rus tilida <b>istalgan vaqt haqida</b> gapira olasiz. Yana bir yaxshi xabar:
kelasi zamonda ham yangi qoʻshimchalar yoʻq. Bor-yoʻgʻi <b>bitta yordamchi
feʼl</b> va uning yonida oʻzgarmagan infinitiv.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Быть</b> feʼlining kelasi zamonini tuslaysiz: бу́ду, бу́дешь, бу́дет…</li>
    <li><b>Бу́ду + infinitiv</b> qolipini oʻrganasiz</li>
    <li>Yolgʻiz <b>бу́ду</b> ni ishlatasiz: «Я бу́ду до́ма»</li>
    <li>Uchala zamonni bir jadvalda koʻrasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kelasi zamon</span>
  <span class="pe-chip pe-chip--v">бу́ду</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">чита́ть</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">oʻqiyman (ertaga)</span>
</div>

<h3>1. Бу́ду — «boʻlmoq» ning kelasi zamoni</h3>

<p>PR-11 da siz bir gʻalati qoidani oʻrgandingiz: hozirgi zamonda
<em>быть</em> aytilmaydi. PR-23 da u oʻtgan zamonda qaytib keldi
(<em>был, была́</em>). Kelasi zamonda esa u <b>toʻliq tuslanadi</b>, va oddiy
I tuslanish qoʻshimchalari bilan:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th><th>Maʼnosi</th></tr>
  <tr><td>я</td><td class="pr-stem">бу́д</td><td class="pr-end">у</td>
      <td class="pr-res">бу́ду</td><td class="pr-uz">boʻlaman</td></tr>
  <tr><td>ты</td><td class="pr-stem">бу́д</td><td class="pr-end">ешь</td>
      <td class="pr-res">бу́дешь</td><td class="pr-uz">boʻlasan</td></tr>
  <tr><td>он / она́</td><td class="pr-stem">бу́д</td><td class="pr-end">ет</td>
      <td class="pr-res">бу́дет</td><td class="pr-uz">boʻladi</td></tr>
  <tr><td>мы</td><td class="pr-stem">бу́д</td><td class="pr-end">ем</td>
      <td class="pr-res">бу́дем</td><td class="pr-uz">boʻlamiz</td></tr>
  <tr><td>вы</td><td class="pr-stem">бу́д</td><td class="pr-end">ете</td>
      <td class="pr-res">бу́дете</td><td class="pr-uz">boʻlasiz</td></tr>
  <tr><td>они́</td><td class="pr-stem">бу́д</td><td class="pr-end">ут</td>
      <td class="pr-res">бу́дут</td><td class="pr-uz">boʻladilar</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Jadvalga diqqat bilan qarang — bu <b>aynan PR-22 dagi <em>идти́</em> naqshi</b>:
<em>иду́, идёшь, идёт, идём, идёте, иду́т</em> — <em>бу́ду, бу́дешь, бу́дет,
бу́дем, бу́дете, бу́дут</em>. Farqi faqat urgʻuda: <em>идти́</em> da u
qoʻshimchada (shuning uchun Ё), <em>быть</em> da esa oʻzakda (shuning uchun Е).
Yangi narsa yoʻq — siz buni allaqachon bilasiz.</div>

<h3>2. Бу́ду + infinitiv — ikki soʻzdan bitta zamon</h3>

<p>Endi butun qolip. <b>Birinchi soʻz tuslanadi, ikkinchisi tegilmaydi</b>:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Yordamchi</th><th>Infinitiv</th><th>Maʼnosi</th></tr>
  <tr><td>я</td><td class="pr-res">бу́ду</td><td class="pr-end">чита́ть</td>
      <td class="pr-uz">oʻqiyman (keyin)</td></tr>
  <tr><td>ты</td><td class="pr-res">бу́дешь</td><td class="pr-end">рабо́тать</td>
      <td class="pr-uz">ishlaysan</td></tr>
  <tr><td>он</td><td class="pr-res">бу́дет</td><td class="pr-end">говори́ть</td>
      <td class="pr-uz">gapiradi</td></tr>
  <tr><td>мы</td><td class="pr-res">бу́дем</td><td class="pr-end">смотре́ть</td>
      <td class="pr-uz">koʻramiz</td></tr>
  <tr><td>вы</td><td class="pr-res">бу́дете</td><td class="pr-end">жить</td>
      <td class="pr-uz">yashaysiz</td></tr>
  <tr><td>они́</td><td class="pr-res">бу́дут</td><td class="pr-end">есть</td>
      <td class="pr-uz">yeydilar</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Infinitiv <b>hech qachon</b> oʻzgarmaydi. Bu — PR-19 dagi qoidaning oʻsha oʻzi:
gapda faqat <b>birinchi</b> feʼl tuslanadi. <em>Я бу́ду чита́ть</em> —
<em>чита́ть</em> oʻz holida. <em>Я бу́ду чита́ю</em> degan gap yoʻq.</div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">За́втра</span> я
     <span class="pe-hl pe-hl--v">бу́ду рабо́тать</span>, а Дилно́за
     <span class="pe-hl pe-hl--v">бу́дет</span>
     <span class="pe-hl pe-hl--v">чита́ть</span>.</p>
  <p class="pe-ex__uz">Ertaga men ishlayman, Dilnoza esa kitob oʻqiydi.</p>
  <p class="pe-ex__why">Ikkita ega, ikkita yordamchi shakl — lekin infinitivlar
     qimirlamaydi.</p>
</div>

<h3>3. Yolgʻiz бу́ду — «boʻlaman»</h3>

<p>Agar gapda boshqa feʼl boʻlmasa, <em>бу́ду</em> oʻzi kesim boʻlib qoladi.
Bu <b>juda koʻp</b> ishlatiladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kecha</th><th>Bugun</th><th>Ertaga</th></tr>
  <tr><td class="pr-res">Я был до́ма.</td><td class="pr-end">Я до́ма.</td>
      <td class="pr-uz">Я <b>бу́ду</b> до́ма.</td></tr>
  <tr><td class="pr-res">Э́то бы́ло тру́дно.</td><td class="pr-end">Э́то тру́дно.</td>
      <td class="pr-uz">Э́то <b>бу́дет</b> тру́дно.</td></tr>
  <tr><td class="pr-res">Вчера́ был дождь.</td><td class="pr-end">Сего́дня дождь.</td>
      <td class="pr-uz">За́втра <b>бу́дет</b> дождь.</td></tr>
</table></div>

<p>Oʻrtadagi ustunga qarang — u <b>boʻsh</b>. Hozirgi zamonda feʼl yoʻq. Chapda
va oʻngda esa bor. Rus tilining bu «teshigi»ni bir marta koʻrsangiz, uni hech
qachon unutmaysiz.</p>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbek tilida kelasi zamon <b>bitta soʻz</b>: <em>oʻqiy<b>man</b></em>,
<em>oʻqi<b>moqchi</b>man</em>, <em>bora<b>jak</b>man</em>. Rus tilida esa
<b>ikkita</b>. Bu — mexanik farq, uni oʻrganish oson.<br><br>
Lekin bittasi qiyinroq: oʻzbekchada <em>oʻqiyman</em> ham «hozir oʻqiyman»,
ham «ertaga oʻqiyman» degani — bitta shakl ikkala vaqtga xizmat qiladi. Rus
tilida bunday emas: <em>Я чита́ю</em> — faqat <b>hozir</b>. Ertaga uchun
<em>бу́ду</em> ni <b>aytish shart</b>. Shuning uchun oʻzbek oʻquvchi «Завтра я
читаю» deb yozib yuboradi — ruscha quloqqa bu tugallanmagan gap boʻlib
tuyuladi.</div>

<h3>4. Inkor va savol</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">За́втра я <span class="pe-hl pe-hl--neg">не</span>
     <span class="pe-hl pe-hl--v">бу́ду</span> рабо́тать.</p>
  <p class="pe-ex__uz">Ertaga ishlamayman.</p>
  <p class="pe-ex__why"><b>Не</b> — <em>бу́ду</em> ning oldida, infinitivning
     emas. Inkor har doim <b>tuslanadigan</b> feʼlga tegadi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Ты <span class="pe-hl pe-hl--v">бу́дешь</span> чай?<br>
     — Да, бу́ду. Спаси́бо.</p>
  <p class="pe-ex__uz">— Choy ichasanmi?<br>— Ha, ichaman. Rahmat.</p>
  <p class="pe-ex__why">Kundalik nutqda <em>бу́дешь</em> yolgʻiz ham «olasanmi,
     ichasanmi» maʼnosini beradi — infinitiv tushib qoladi, chunki u
     tushunarli. Qisqa javob ham shu shaklda: <b>«Да, бу́ду»</b>.</p>
</div>

<h3>5. Uchala zamon bir jadvalda</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Feʼl</th><th>Kecha (он)</th><th>Bugun (он)</th><th>Ertaga (он)</th></tr>
  <tr><td class="pr-res">чита́ть</td><td class="pr-end">чита́л</td>
      <td class="pr-end">чита́ет</td><td class="pr-end">бу́дет чита́ть</td></tr>
  <tr><td class="pr-res">говори́ть</td><td class="pr-end">говори́л</td>
      <td class="pr-end">говори́т</td><td class="pr-end">бу́дет говори́ть</td></tr>
  <tr><td class="pr-res">жить</td><td class="pr-end">жил</td>
      <td class="pr-end">живёт</td><td class="pr-end">бу́дет жить</td></tr>
  <tr><td class="pr-res">есть</td><td class="pr-end">ел</td>
      <td class="pr-end">ест</td><td class="pr-end">бу́дет есть</td></tr>
  <tr><td class="pr-res">быть</td><td class="pr-end">был</td>
      <td class="pr-end">— (yoʻq)</td><td class="pr-end">бу́дет</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Rus tilida kelasi zamonning <b>ikkinchi turi</b> ham bor —
<em>прочита́ю, напишу́, позвоню́</em> kabi bir soʻzli shakllar. Ular
<b>tugallangan</b> ishni bildiradi va ularni <b>feʼl turi (вид)</b> bilan
birga, PR-51 da oʻrganamiz. Bugun ular haqida oʻylamang: hozircha kelasi
zamon = <b>бу́ду + infinitiv</b>, va bu shakl har doim toʻgʻri va
tushunarli.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я бу́ду чита́ю кни́гу.</s></p>
  <p class="pe-good">Я бу́ду <b>чита́ть</b> кни́гу — ikkinchi feʼl infinitivda</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы бу́дет до́ма.</s></p>
  <p class="pe-good">Мы <b>бу́дем</b> до́ма — yordamchi feʼl egaga moslashadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>За́втра я бу́ду быть до́ма.</s></p>
  <p class="pe-good">За́втра я <b>бу́ду</b> до́ма — <em>бу́ду</em> ning oʻzi «boʻlaman»</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я бу́ду не рабо́тать.</s></p>
  <p class="pe-good">Я <b>не бу́ду</b> рабо́тать — <em>не</em> tuslanadigan feʼl oldida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>За́втра он рабо́тает в магази́не.</s> <em>(«ertaga» maʼnosida)</em></p>
  <p class="pe-good">За́втра он <b>бу́дет рабо́тать</b> — hozirgi zamon kelasi zamon oʻrniga ishlamaydi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>За́втра мы ___ смотре́ть фильм.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>бу́дем</strong>. «Мы» uchun yordamchi
    shakl <b>бу́дем</b>, infinitiv esa oʻz holida qoladi:
    <em>бу́дем смотре́ть</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Bu gapni kelasi zamonga oʻtkazing: <b>Вчера́ был дождь.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>За́втра бу́дет дождь.</strong>
    <em>Дождь</em> — uchinchi shaxs birligi, demak <b>бу́дет</b>. Bu yerda
    infinitiv kerak emas — <em>бу́дет</em> ning oʻzi «boʻladi» degani.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu gapni inkor qiling: <b>Я бу́ду рабо́тать в суббо́ту.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я не бу́ду рабо́тать в
    суббо́ту.</strong> <b>Не</b> <em>бу́ду</em> ning oldiga tushadi, chunki
    inkor har doim tuslanadigan feʼlga tegadi. <em>«Я бу́ду не рабо́тать»</em>
    — xato.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni ruschaga oʻgiring: <b>Ertaga uyda boʻlamiz va choy ichamiz.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>За́втра мы бу́дем до́ма и бу́дем пить
    чай.</strong> Birinchi qismda infinitiv yoʻq (<em>бу́дем до́ма</em>),
    ikkinchisida bor (<em>бу́дем пить</em>). Ikkinchi <em>бу́дем</em> ni
    tushirib qoldirish ham mumkin: <em>…и пить чай</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Они́ бу́дут жить в Москве́. &nbsp; б) Ты бу́дешь есть?<br>
     в) Я бу́ду быть до́ма. &nbsp; г) Э́то бу́дет тру́дно.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Я бу́ду до́ма</b>. <em>Бу́ду</em> ning oʻzi allaqachon «boʻlaman»
    degani, shuning uchun yoniga yana <em>быть</em> qoʻyilmaydi. Qolgan
    uchtasi toʻgʻri.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>бу́ду</b><span>boʻlaman; (yordamchi feʼl)</span></li>
  <li><b>за́втра</b><span>ertaga</span></li>
  <li><b>ско́ро</b><span>tez orada</span></li>
  <li><b>экза́мен</b><span>imtihon</span></li>
  <li><b>обеща́ть</b><span>vaʼda bermoq</span></li>
  <li><b>план</b><span>reja</span></li>
  <li><b>ле́том</b><span>yozda</span></li>
  <li><b>зимо́й</b><span>qishda</span></li>
  <li><b>наде́яться</b><span>umid qilmoq</span></li>
  <li><b>обяза́тельно</b><span>albatta</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Kelasi zamon = <b>бу́ду + infinitiv</b>. Ikki soʻz, bitta zamon.</li>
    <li><b>Бу́ду, бу́дешь, бу́дет, бу́дем, бу́дете, бу́дут</b> — aynan
        <em>идти́</em> naqshi, faqat urgʻu oʻzakda.</li>
    <li>Infinitiv <b>hech qachon</b> oʻzgarmaydi.</li>
    <li>Yolgʻiz <em>бу́ду</em> = «boʻlaman»: <em>Я бу́ду до́ма</em>. Yoniga
        <em>быть</em> qoʻshilmaydi.</li>
    <li>Inkor: <b>не бу́ду</b> — <em>не</em> yordamchi feʼl oldida.</li>
    <li>Oʻzbekcha «oʻqiyman» ikkala vaqtga xizmat qiladi, ruscha
        <em>чита́ю</em> esa faqat <b>hozir</b>. Ertaga uchun <em>бу́ду</em> ni
        aytish shart.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-25: Qaytim feʼllar -ся / -сь: учиться, находиться, нравиться",
        "category": "russian",
        "order": 25,
        "summary": (
            "Feʼlning oxiriga qoʻshiladigan kichkina -ся uning maʼnosini butunlay "
            "oʻzgartirishi mumkin. Oʻzbek tilida ham xuddi shunday qoʻshimcha bor — "
            "shuning uchun bu dars siz oʻylagandan osonroq."
        ),
        "stories": ["Как я учился плавать"],
        "content": """
<h2>PR-25: Qaytim feʼllar -ся / -сь: учиться, находиться, нравиться</h2>

<p>Rus tilidagi matnni ochsangiz, oxiri <b>-ся</b> ga tugagan feʼllarni darrov
koʻrasiz: <em>учи́ться, смея́ться, находи́ться, нра́виться</em>. Bu — alohida
feʼllar emas, balki siz bilgan feʼllarga qoʻshilgan <b>bitta qoʻshimcha</b>. Va
u har doim <b>eng oxirida</b>, hatto shaxs qoʻshimchasidan ham keyin turadi.
Yaxshi xabar: oʻzbek tilida ham aynan shunday narsa bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>-ся</b> va <b>-сь</b> ni qachon ishlatishni bilasiz</li>
    <li>Qaytim feʼlni toʻliq tuslaysiz: учу́сь, у́чишься, у́чится…</li>
    <li>Oʻtgan zamonda yasaysiz: учи́лся, учи́лась, учи́лись</li>
    <li><b>Учи́ть</b> va <b>учи́ться</b> ni ajratasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qaytim feʼl</span>
  <span class="pe-chip pe-chip--v">учу́</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">сь</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--s">учу́сь — oʻqiyman (oʻzim)</span>
</div>

<h3>1. Qachon -ся, qachon -сь</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Qoida bitta jumlaga sigʻadi:<br>
Feʼl <b>unli</b> bilan tugasa → <b>-сь</b>.<br>
Feʼl <b>undosh</b> (yoki <b>-ь</b>) bilan tugasa → <b>-ся</b>.<br>
Bu talaffuz uchun qilingan: <em>учу́-сь</em> aytish oson, <em>учу́-ся</em> esa
ogʻirroq.</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Asosiy shakl</th><th>Oxiri</th><th>Qoʻshimcha</th><th>Natija</th></tr>
  <tr><td>я</td><td class="pr-stem">учу́</td><td class="pr-uz">unli</td>
      <td class="pr-end">сь</td><td class="pr-res">учу́сь</td></tr>
  <tr><td>ты</td><td class="pr-stem">у́чишь</td><td class="pr-uz">ь</td>
      <td class="pr-end">ся</td><td class="pr-res">у́чишься</td></tr>
  <tr><td>он / она́</td><td class="pr-stem">у́чит</td><td class="pr-uz">undosh</td>
      <td class="pr-end">ся</td><td class="pr-res">у́чится</td></tr>
  <tr><td>мы</td><td class="pr-stem">у́чим</td><td class="pr-uz">undosh</td>
      <td class="pr-end">ся</td><td class="pr-res">у́чимся</td></tr>
  <tr><td>вы</td><td class="pr-stem">у́чите</td><td class="pr-uz">unli</td>
      <td class="pr-end">сь</td><td class="pr-res">у́читесь</td></tr>
  <tr><td>они́</td><td class="pr-stem">у́чат</td><td class="pr-uz">undosh</td>
      <td class="pr-end">ся</td><td class="pr-res">у́чатся</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Yodlash uchun: <b>faqat ikkita shaklda -сь</b> boʻladi — <b>«я»</b> va
<b>«вы»</b>. Qolgan toʻrttasida <b>-ся</b>. Yaʼni <em>учу́<b>сь</b></em> va
<em>у́чите<b>сь</b></em>, boshqa hamma joyda <em>-ся</em>. Shu ikkitani eslab
qolsangiz, qoidani har safar boshdan oʻylashingiz shart emas.</div>

<div class="pr-say">
  <span class="pr-say__from">у́чится</span>
  <span class="pr-say__arrow">→</span>
  <span class="pr-say__to">[у́чица]</span>
  <span class="pr-say__why">-тся va -ться har doim [ца] boʻlib oʻqiladi</span>
</div>

<h3>2. Oʻtgan zamonda</h3>

<p>Bu yerda ham qoida oʻsha: qoʻshimcha eng oxiriga tushadi va oldingi harfga
qarab tanlanadi.</p>

<div class="pr-gender">
  <div class="pr-gender__side">
    <p class="pr-gender__h">Мужско́й — erkak</p>
    <p class="pr-gender__form">учи́л<span class="pr-end">ся</span></p>
    <p>Oxirida <b>Л</b> — undosh, demak <b>-ся</b>.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--f">
    <p class="pr-gender__h">Же́нский — ayol</p>
    <p class="pr-gender__form">учи́ла<span class="pr-end">сь</span></p>
    <p>Oxirida <b>А</b> — unli, demak <b>-сь</b>.</p>
  </div>
  <div class="pr-gender__side pr-gender__side--n">
    <p class="pr-gender__h">Koʻplik</p>
    <p class="pr-gender__form">учи́ли<span class="pr-end">сь</span></p>
    <p>Oxirida <b>И</b> — unli, demak <b>-сь</b>.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Жасу́р</span>
     <span class="pe-hl pe-hl--v">учи́лся</span> в Ташке́нте, а
     <span class="pe-hl pe-hl--s">Афсо́на</span>
     <span class="pe-hl pe-hl--v">учи́лась</span> в Самарка́нде.</p>
  <p class="pe-ex__uz">Jasur Toshkentda oʻqidi, Afsona esa Samarqandda.</p>
  <p class="pe-ex__why">Bitta feʼl, ikki xil oxir — chunki jins boshqa
     (PR-23), va shundan keyin qoʻshimcha ham boshqa.</p>
</div>

<h3>3. Toʻrtta maʼno guruhi</h3>

<p><b>-ся</b> nima qiladi? Har doim bitta ish emas. Toʻrtta guruhga
boʻlinadi va ularni bir marta koʻrib chiqish kifoya:</p>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Oʻziga qaytadi</p>
    <p>Harakat <b>oʻz egasiga</b> qaytadi:<br>
       <em>умыва́ться</em> — yuvinmoq<br>
       <em>одева́ться</em> — kiyinmoq<br>
       <em>гото́виться</em> — tayyorlanmoq</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Bir-birini</p>
    <p>Ikki tomon <b>bir-biriga</b> qiladi:<br>
       <em>встреча́ться</em> — uchrashmoq<br>
       <em>знако́миться</em> — tanishmoq<br>
       <em>обнима́ться</em> — quchoqlashmoq</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Faqat -ся bilan</p>
    <p>Bu feʼllar <b>-ся siz umuman yoʻq</b>:<br>
       <em>смея́ться</em> — kulmoq<br>
       <em>боя́ться</em> — qoʻrqmoq<br>
       <em>стара́ться</em> — harakat qilmoq<br>
       <em>находи́ться</em> — joylashgan boʻlmoq</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">4</span>Maʼno oʻzgaradi</p>
    <p>Feʼl bor, lekin <b>maʼnosi boshqa</b>:<br>
       <em>учи́ть</em> — oʻrgatmoq / yodlamoq<br>
       <em>учи́ться</em> — oʻqimoq (talaba boʻlmoq)<br>
       <em>начина́ть</em> — boshlamoq<br>
       <em>начина́ться</em> — boshlanmoq</p></div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu — kursdagi kam uchraydigan holat: <b>oʻzbek tili sizga yordam beradi</b>.
Oʻzbekchada ham xuddi shunday qoʻshimcha bor — <b>-(i)n-</b>:<br>
<em>yuv-moq → yuv<b>in</b>-moq</em> &nbsp;=&nbsp; <em>мыть → мы́ться</em><br>
<em>kiy-moq → kiy<b>in</b>-moq</em> &nbsp;=&nbsp; <em>надева́ть → одева́ться</em><br>
<em>tara-moq → tara<b>n</b>-moq</em> — sochini taramoq.<br>
Yaʼni tushuncha siz uchun yangi emas: <b>harakat oʻz egasiga qaytadi</b>. Faqat
rus tilida bu qoʻshimcha <b>eng oxirida</b> turadi, oʻzbekchada esa oʻrtada
(<em>yuv-in-a-man</em> — <em>умыва́-ю-сь</em>). Va rus tilida u koʻproq ish
bajaradi: yuqoridagi 2, 3 va 4-guruhlar oʻzbekchada bu qoʻshimcha bilan
yasalmaydi.</div>

<h3>4. Учи́ть va учи́ться — eng koʻp adashtiriladigan juftlik</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">учи́ть — <b>nimani?</b></p>
    <p><em>Я <b>учу́</b> ру́сский язы́к.</em><br>Rus tilini oʻrganaman
       (yodlayman).</p>
    <p>Yoniga <b>albatta narsa kerak</b>: nimani oʻrganyapsiz? Bu feʼl
       yolgʻiz turolmaydi.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">учи́ться — <b>qayerda?</b></p>
    <p><em>Я <b>учу́сь</b> в шко́ле.</em><br>Maktabda oʻqiyman.</p>
    <p>Yoniga narsa <b>kerak emas</b> — bu «talaba boʻlmoq» degani. Joy yoki
       usul aytiladi.</p>
  </div>
</div>

<p>Shuning uchun <em>«Я учу́ в шко́ле»</em> — xato: «maktabda <b>nimani</b>
yodlayapsiz?» degan savol javobsiz qoladi. Va <em>«Я учу́сь ру́сский язы́к»</em>
ham xato: <em>учи́ться</em> yoniga narsa olmaydi.</p>

<h3>5. Faqat -ся bilan yashaydigan feʼllar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>я</th><th>он / она́</th><th>они́</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">смея́ться</td><td class="pr-end">смею́сь</td>
      <td class="pr-end">смеётся</td><td class="pr-end">смею́тся</td>
      <td class="pr-uz">kulmoq</td></tr>
  <tr><td class="pr-res">боя́ться</td><td class="pr-end">бою́сь</td>
      <td class="pr-end">бои́тся</td><td class="pr-end">боя́тся</td>
      <td class="pr-uz">qoʻrqmoq</td></tr>
  <tr><td class="pr-res">стара́ться</td><td class="pr-end">стара́юсь</td>
      <td class="pr-end">стара́ется</td><td class="pr-end">стара́ются</td>
      <td class="pr-uz">harakat qilmoq</td></tr>
  <tr><td class="pr-res">находи́ться</td><td class="pr-end">нахожу́сь</td>
      <td class="pr-end">нахо́дится</td><td class="pr-end">нахо́дятся</td>
      <td class="pr-uz">joylashgan boʻlmoq</td></tr>
  <tr><td class="pr-res">занима́ться</td><td class="pr-end">занима́юсь</td>
      <td class="pr-end">занима́ется</td><td class="pr-end">занима́ются</td>
      <td class="pr-uz">shugʻullanmoq</td></tr>
</table></div>

<p><em>Находи́ться</em> ni alohida eslab qoling — u savolda juda koʻp
uchraydi: <em>Где <b>нахо́дится</b> шко́ла?</em> — «Maktab qayerda?». Va
<em>нра́виться</em> ni ham koʻrasiz (<em>мне нра́вится</em> — «menga
yoqadi»); u teskari qurilishda ishlaydi va unga <b>butun boshli dars</b>
ajratilgan — PR-28.</p>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я учу́ся в шко́ле.</s></p>
  <p class="pe-good">Я <b>учу́сь</b> в шко́ле — unlidan keyin <b>-сь</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Афсо́на учи́лся в Москве́.</s></p>
  <p class="pe-good">Афсо́на <b>учи́лась</b> — ayol jinsi, demak <b>-ла + сь</b></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я учу́ в университе́те.</s></p>
  <p class="pe-good">Я <b>учу́сь</b> в университе́те — <em>учи́ть</em> yoniga narsa talab qiladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он смеёт гро́мко.</s></p>
  <p class="pe-good">Он <b>смеётся</b> гро́мко — <em>смея́ться</em> <b>-ся</b> siz mavjud emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы встреча́ем ка́ждый день.</s> <em>(«uchrashamiz» maʼnosida)</em></p>
  <p class="pe-good">Мы <b>встреча́емся</b> ка́ждый день — bir-birimiz bilan</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>-ся</b> yoki <b>-сь</b>? &nbsp; <b>Вы у́чите___ в шко́ле?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>-сь</strong>: <em>у́читесь</em>.
    <em>У́чите</em> unli (<b>Е</b>) bilan tugaydi. «Вы» — <b>-сь</b> oladigan
    ikkita shakldan biri; ikkinchisi «я».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Дилно́за ___ пла́вать.</b> (учи́ться, oʻtgan zamon)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>учи́лась</strong>. Ikki qadam: avval
    oʻtgan zamon va jins (<em>учи́ла-</em>, chunki Dilnoza qiz), keyin
    qoʻshimcha (<b>-сь</b>, chunki oxirida unli <b>А</b>).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>учи́ть</b> yoki <b>учи́ться</b>? &nbsp; <b>Я ___ но́вые слова́
     ка́ждый день.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>учу́</strong> (<em>учи́ть</em>).
    Gapda «nimani?» degan savolga javob bor — <em>но́вые слова́</em>. Demak
    qaytim shakli kerak emas. <em>Учу́сь</em> yoniga narsa olmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>у́чится</b> qanday oʻqiladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>[у́чица]</strong>. <b>-тся</b> va
    <b>-ться</b> birikmalari har doim <b>[ца]</b> boʻlib oʻqiladi. Shuning
    uchun <em>у́чится</em> va <em>учи́ться</em> deyarli bir xil eshitiladi —
    farqni faqat gapdan bilib olasiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Он бои́тся. &nbsp; б) Мы встреча́емся в суббо́ту.<br>
     в) Они́ смею́т гро́мко. &nbsp; г) Шко́ла нахо́дится здесь.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Они́ смею́тся</b>. <em>Смея́ться</em> uchinchi guruhdan: u <b>-ся</b>
    siz umuman mavjud emas, xuddi <em>боя́ться</em>, <em>стара́ться</em>,
    <em>находи́ться</em> kabi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>учи́ться</b><span>oʻqimoq (talaba boʻlmoq)</span></li>
  <li><b>смея́ться</b><span>kulmoq</span></li>
  <li><b>боя́ться</b><span>qoʻrqmoq</span></li>
  <li><b>стара́ться</b><span>harakat qilmoq</span></li>
  <li><b>находи́ться</b><span>joylashgan boʻlmoq</span></li>
  <li><b>занима́ться</b><span>shugʻullanmoq</span></li>
  <li><b>встреча́ться</b><span>uchrashmoq</span></li>
  <li><b>улыба́ться</b><span>jilmaymoq</span></li>
  <li><b>начина́ться</b><span>boshlanmoq</span></li>
  <li><b>гото́виться</b><span>tayyorlanmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Qoʻshimcha <b>eng oxirida</b>, shaxs qoʻshimchasidan ham keyin.</li>
    <li>Unlidan keyin <b>-сь</b>, undoshdan keyin <b>-ся</b>. Faqat
        <b>«я»</b> va <b>«вы»</b> shakllarida <b>-сь</b>.</li>
    <li>Oʻtgan zamonda: <em>учи́л<b>ся</b></em> (undosh Л) —
        <em>учи́ла<b>сь</b></em>, <em>учи́ли<b>сь</b></em> (unli).</li>
    <li>Toʻrt guruh: oʻziga qaytadi · bir-birini · faqat -ся bilan · maʼnosi
        oʻzgaradi.</li>
    <li><b>Учи́ть</b> yoniga narsa oladi, <b>учи́ться</b> olmaydi.</li>
    <li>Talaffuz: <b>-тся / -ться → [ца]</b>.</li>
    <li>Oʻzbekchadagi <b>-(i)n-</b> (yuv<b>in</b>moq) — shu tushunchaning
        oʻzi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-26: Мочь va уметь — «-a olmoq» ning ikki xil turi",
        "category": "russian",
        "order": 26,
        "summary": (
            "Oʻzbekcha «-a olmoq» rus tilida ikkiga boʻlinadi: уме́ть — oʻrganib "
            "olingan mahorat, мочь — shu ondagi imkoniyat. Farqni bilmaslik gapni "
            "butunlay boshqa maʼnoga burib yuboradi."
        ),
        "stories": ["Бабушка умеет всё"],
        "content": """
<h2>PR-26: Мочь va уметь — «-a olmoq» ning ikki xil turi</h2>

<p>«Men suza olaman» — buni ruschaga oʻgiring. Ikkita toʻgʻri javob bor, va
ular <b>boshqa-boshqa narsani</b> anglatadi. <em>Я уме́ю пла́вать</em> —
«suzishni bilaman, oʻrganganman». <em>Я могу́ пла́вать</em> — «hozir suzishimga
hech narsa xalaqit bermaydi». Oʻzbekchada bitta ibora, rus tilida ikkita feʼl.
Bugun ularni ajratamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Мочь</b> ni tuslaysiz — г va ж almashinuvi bilan</li>
    <li><b>Уме́ть</b> ni tuslaysiz — u butunlay oddiy</li>
    <li>Qaysi biri qachon kerakligini bilasiz</li>
    <li>Ikkalasining oʻtgan va kelasi zamonini yasaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ikki xil «-a olmoq»</span>
  <span class="pe-chip pe-chip--s">уме́ю</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">bilaman, oʻrganganman</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">могу́</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--adv">hozir imkonim bor</span>
</div>

<h3>1. Мочь — г va ж almashinuvi</h3>

<p>Bu feʼl PR-22 dagi notoʻgʻrilar oilasidan, lekin uning naqshi chiroyli:
<b>birinchi va oxirgi shaklda Г, oʻrtadagi toʻrttasida Ж</b>.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Shakl</th><th>Oʻzak</th><th>Maʼnosi</th></tr>
  <tr><td>я</td><td class="pr-res">могу́</td><td class="pr-uz">мог-</td>
      <td class="pr-uz">imkonim bor</td></tr>
  <tr><td>ты</td><td class="pr-res">мо́жешь</td><td class="pr-uz">мож-</td>
      <td class="pr-uz">imkoning bor</td></tr>
  <tr><td>он / она́</td><td class="pr-res">мо́жет</td><td class="pr-uz">мож-</td>
      <td class="pr-uz">imkoni bor</td></tr>
  <tr><td>мы</td><td class="pr-res">мо́жем</td><td class="pr-uz">мож-</td>
      <td class="pr-uz">imkonimiz bor</td></tr>
  <tr><td>вы</td><td class="pr-res">мо́жете</td><td class="pr-uz">мож-</td>
      <td class="pr-uz">imkoningiz bor</td></tr>
  <tr><td>они́</td><td class="pr-res">мо́гут</td><td class="pr-uz">мог-</td>
      <td class="pr-uz">imkonlari bor</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Naqshni bitta jumla qilib eslang: «<b>Г — ikki chetda, Ж — oʻrtada</b>».
<em>Мо<b>г</b>у́ … мо́<b>ж</b>ешь, мо́<b>ж</b>ет, мо́<b>ж</b>ем,
мо́<b>ж</b>ете … мо́<b>г</b>ут</em>. Va urgʻuga eʼtibor bering: faqat
<em>могу́</em> da u oxirida, qolgan hamma joyda oʻzakda.</div>

<h3>2. Уме́ть — hech qanday hiyla yoʻq</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Shaxs</th><th>Oʻzak</th><th>Qoʻshimcha</th><th>Natija</th></tr>
  <tr><td>я</td><td class="pr-stem">уме́</td><td class="pr-end">ю</td>
      <td class="pr-res">уме́ю</td></tr>
  <tr><td>ты</td><td class="pr-stem">уме́</td><td class="pr-end">ешь</td>
      <td class="pr-res">уме́ешь</td></tr>
  <tr><td>он / она́</td><td class="pr-stem">уме́</td><td class="pr-end">ет</td>
      <td class="pr-res">уме́ет</td></tr>
  <tr><td>мы</td><td class="pr-stem">уме́</td><td class="pr-end">ем</td>
      <td class="pr-res">уме́ем</td></tr>
  <tr><td>вы</td><td class="pr-stem">уме́</td><td class="pr-end">ете</td>
      <td class="pr-res">уме́ете</td></tr>
  <tr><td>они́</td><td class="pr-stem">уме́</td><td class="pr-end">ют</td>
      <td class="pr-res">уме́ют</td></tr>
</table></div>

<p>Oddiy I tuslanish — <em>чита́ть</em> bilan bir xil. Yodlash uchun hech
narsa yoʻq.</p>

<h3>3. Farqi — va u qanchalik muhim</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">уме́ть — <b>oʻrganilgan mahorat</b></p>
    <p><em>Я <b>уме́ю</b> пла́вать.</em><br>Suzishni bilaman.</p>
    <p>Bir marta oʻrganilgan va endi doim bor: suzish, mashina haydash,
       gitara chalish, ovqat pishirish. <b>Vaqtga bogʻliq emas.</b></p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">мочь — <b>shu ondagi imkoniyat</b></p>
    <p><em>Я <b>не могу́</b> пла́вать сего́дня.</em><br>Bugun suza olmayman.</p>
    <p>Sharoit, ruxsat, vaqt, kuch. Ertaga boshqacha boʻlishi mumkin.
       <b>Vaziyatga bogʻliq.</b></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">Я <span class="pe-hl pe-hl--v">уме́ю</span> пла́вать,
     но сего́дня я <span class="pe-hl pe-hl--neg">не</span>
     <span class="pe-hl pe-hl--v">могу́</span> — вода́ холо́дная.</p>
  <p class="pe-ex__uz">Suzishni bilaman, lekin bugun suza olmayman — suv sovuq.</p>
  <p class="pe-ex__why">Bitta gapda ikkalasi ham bor, va ular
     <b>qarama-qarshi emas</b>. Mahorat joyida turibdi, imkoniyat esa
     bugun yoʻq. Aynan shu gap farqni eng yaxshi koʻrsatadi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Aslida oʻzbek tilida ham bu farq <b>bor</b> — faqat siz uni sezmaysiz, chunki
u odat boʻlib ketgan:<br>
<em>suzish<b>ni bilaman</b></em> &nbsp;→&nbsp; <b>уме́ю</b> пла́вать<br>
<em>suz<b>a olaman</b></em> &nbsp;→&nbsp; <b>могу́</b> пла́вать<br>
Shuning uchun tarjima qilishdan oldin oʻzingizga oʻzbekcha savol bering:
«<b>bilaman</b>mi yoki <b>-a olaman</b>mi?» Agar «bilaman» toʻgʻri kelsa —
<em>уме́ть</em>. Agar «hozir imkonim bor» boʻlsa — <em>мочь</em>. Bu kichkina
tekshiruv sizni deyarli har safar toʻgʻri javobga olib boradi.</div>

<h3>4. Ikkinchi feʼl doim infinitivda</h3>

<p>Bu — PR-19 dan beri oʻzgarmayotgan qoida, va u bu yerda ham ishlaydi:</p>

<div class="pe-ex">
  <p class="pe-ex__ru">Бекзо́д <span class="pe-hl pe-hl--v">уме́ет</span>
     <span class="pe-hl pe-hl--o">бы́стро бе́гать</span>.</p>
  <p class="pe-ex__uz">Bekzod tez yugurishni biladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__ru">— Ты <span class="pe-hl pe-hl--v">мо́жешь</span>
     говори́ть ме́дленно?<br>— Коне́чно, могу́.</p>
  <p class="pe-ex__uz">— Sekinroq gapira olasizmi?<br>— Albatta.</p>
  <p class="pe-ex__why">Bu — rus tilida iltimos qilishning eng muloyim va eng
     koʻp ishlatiladigan yoʻli. Qisqa javobda infinitiv tushib qoladi:
     <em>Могу́</em>.</p>
</div>

<h3>5. Oʻtgan va kelasi zamonda</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Feʼl</th><th>он</th><th>она́</th><th>они́</th><th>Ertaga</th></tr>
  <tr><td class="pr-res">мочь</td><td class="pr-end">мог</td>
      <td class="pr-end">могла́</td><td class="pr-end">могли́</td>
      <td class="pr-uz">смо́жет <em>(PR-51 da)</em></td></tr>
  <tr><td class="pr-res">уме́ть</td><td class="pr-end">уме́л</td>
      <td class="pr-end">уме́ла</td><td class="pr-end">уме́ли</td>
      <td class="pr-uz">бу́дет уме́ть</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<em>Мочь</em> ning oʻtgan zamonida <b>-л yoʻq</b> — erkak shaklida
<b>мог</b>, <em>«мочил»</em> emas. Bu rus tilidagi bir nechta shunday feʼldan
biri. Ayol va koʻplik shakllarida esa Л qaytib keladi:
<em>могла́, могли́</em> — va urgʻu oxirida, xuddi <em>была́</em> kabi
(PR-23).</div>

<div class="pr-pair">
  <div class="pr-pair__c">
    <span class="pr-pair__w">мог</span>
    <span class="pr-pair__uz">erkak — Л yoʻq</span>
  </div>
  <div class="pr-pair__c">
    <span class="pr-pair__w">могла́</span>
    <span class="pr-pair__uz">ayol — Л bor, urgʻu oxirida</span>
  </div>
</div>

<h3>6. Мо́жет быть — kundalik ibora</h3>

<p>Bu ikki soʻz birga <b>«balki»</b> degani va u har kuni ishlatiladi:</p>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--adv">Мо́жет быть</span>,
     за́втра бу́дет дождь.</p>
  <p class="pe-ex__uz">Balki ertaga yomgʻir yogʻar.</p>
  <p class="pe-ex__why">Uni butun ibora sifatida yodlang — bu yerda
     <em>мо́жет</em> ni tuslash kerak emas, u har doim shu shaklda qoladi.
     Qisqartirib <em>мо́жет</em> deb ham aytishadi.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Они́ мо́жут говори́ть по-ру́сски.</s></p>
  <p class="pe-good">Они́ <b>мо́гут</b> — koʻplikda <b>Г</b> qaytadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я мо́гу пла́вать.</s></p>
  <p class="pe-good">Я <b>могу́</b> — «я» shaklida urgʻu oxirida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я уме́ю чита́ю по-ру́сски.</s></p>
  <p class="pe-good">Я уме́ю <b>чита́ть</b> — ikkinchi feʼl infinitivda</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ба́бушка мог гото́вить пло́в.</s></p>
  <p class="pe-good">Ба́бушка <b>могла́</b> — ayol jinsi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я могу́ пла́вать, я учи́лся два го́да.</s></p>
  <p class="pe-good">Я <b>уме́ю</b> пла́вать — oʻrganilgan mahorat haqida gap ketyapti</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Boʻsh joyga: <b>Они́ ___ помога́ть.</b> (мочь)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>мо́гут</strong>. Naqsh: «Г — ikki
    chetda, Ж — oʻrtada». <em>Они́</em> — oxirgi shakl, demak <b>Г</b>:
    <em>мо́гут</em>. <em>Мо́жут</em> — eng koʻp uchraydigan xato.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>уме́ть</b> yoki <b>мочь</b>? &nbsp; <b>Ба́бушка ___ гото́вить пло́в
     о́чень хорошо́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>уме́ет</strong>. Oʻzbekcha tekshiruv:
    «buvim osh pishirish<b>ni biladi</b>» — «bilaman» toʻgʻri kelyapti, demak
    <em>уме́ть</em>. Bu bir marta oʻrganilgan va doim bor boʻlgan
    mahorat.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>уме́ть</b> yoki <b>мочь</b>? &nbsp; <b>Сего́дня я ___ рабо́тать —
     я бо́лен.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>не могу́</strong>. Gapda
    <em>сего́дня</em> va sabab bor — demak bu vaziyatga bogʻliq imkoniyat,
    mahorat emas. <em>«Не уме́ю рабо́тать»</em> butunlay boshqa maʼno berardi:
    «ishlashni bilmayman».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni oʻtgan zamonga oʻtkazing: <b>Она́ не мо́жет говори́ть.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Она́ не могла́ говори́ть.</strong>
    Ayol jinsi — <b>могла́</b>, urgʻu oxirida. Erkak shaklida esa Л umuman
    boʻlmasdi: <em>он не мог</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu ikki gap bir xil narsani anglatadimi?<br>
     <b>Я уме́ю води́ть маши́ну. · Я могу́ води́ть маши́ну.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Yoʻq.</strong> Birinchisi — «mashina
    haydashni bilaman, oʻrganganman». Ikkinchisi — «hozir haydashimga hech
    narsa xalaqit bermaydi» (masalan, kalit menda, charchamaganman, ruxsat
    bor). Bir odam <em>уме́ет</em> boʻlishi, lekin bugun <em>не мо́жет</em>
    boʻlishi mumkin.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>мочь</b><span>-a olmoq (imkoniyat)</span></li>
  <li><b>уме́ть</b><span>-ni bilmoq (mahorat)</span></li>
  <li><b>пла́вать</b><span>suzmoq</span></li>
  <li><b>бе́гать</b><span>yugurmoq</span></li>
  <li><b>води́ть</b><span>haydamoq (mashina)</span></li>
  <li><b>помога́ть</b><span>yordam bermoq</span></li>
  <li><b>шить</b><span>tikmoq</span></li>
  <li><b>мо́жет быть</b><span>balki</span></li>
  <li><b>коне́чно</b><span>albatta</span></li>
  <li><b>бо́лен / больна́</b><span>kasal</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Уме́ть</b> = oʻrganilgan mahorat. <b>Мочь</b> = shu ondagi
        imkoniyat.</li>
    <li>Oʻzbekcha tekshiruv: «<b>bilaman</b>» → уме́ть · «<b>-a olaman</b>»
        → мочь.</li>
    <li><b>Мочь</b>: «Г — ikki chetda, Ж — oʻrtada» — <em>могу́ … мо́жешь,
        мо́жет, мо́жем, мо́жете … мо́гут</em>.</li>
    <li><b>Уме́ть</b> butunlay oddiy: <em>уме́ю, уме́ешь, уме́ет…</em></li>
    <li>Oʻtgan zamon: <b>мог</b> (Л yoʻq!) — <b>могла́, могли́</b>;
        <em>уме́л, уме́ла, уме́ли</em>.</li>
    <li>Ikkinchi feʼl har doim <b>infinitiv</b>da.</li>
    <li><b>Мо́жет быть</b> = «balki» — butun ibora sifatida yodlanadi.</li>
  </ul>
</div>
""",
    },
]
