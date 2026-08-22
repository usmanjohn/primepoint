# -*- coding: utf-8 -*-
"""Prime Russian — Block E yakuniga yaqin (59–61).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-59 — buyruq mayli. PR-54 da vaʼda qilingan «inkor buyruqda НСВ» qoidasi
shu yerda toʻliq ochiladi. Oʻzbekcha bu yerda deyarli mukammal mos keladi:
oʻqi! / oʻqing! / oʻqima! — uchta shakl, uchta vazifa.
PR-60 — шартли mayl. Rus tilidagi eng oson qurilishlardan biri: oʻtgan
zamon + БЫ, tuslanish yoʻq, zamon yoʻq.
PR-61 — majhul nisbat. Ikkita shakl: строится (jarayon) va построен
(natija) — yaʼni PR-51 dagi vid farqi majhul nisbatda ham ishlaydi.

Mashqlar:        practice/management/commands/_practice_pr_59_61.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_59_61.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_59_61.py --author=prime
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
        "title": "PR-59: Buyruq mayli: читай! читайте! давай пойдём! не опаздывай!",
        "category": "russian",
        "order": 59,
        "summary": (
            "Buyruq shakli oson yasaladi — «они́» shaklidan. Va oʻzbekcha bu yerda "
            "deyarli mukammal mos keladi: oʻqi! / oʻqing! / oʻqima!"
        ),
        "stories": ["Инстру́кция для но́вого сотру́дника"],
        "content": """
<h2>PR-59: Buyruq mayli: читай! читайте! давай пойдём! не опаздывай!</h2>

<p>Buyruq mayli (повели́тельное наклоне́ние) rus tilida oson yasaladi va
juda koʻp kerak boʻladi — soʻrash, taklif qilish, yoʻriqnoma berish.
Va bu darsda oʻzbekcha deyarli <b>mukammal</b> mos keladi: sizda ham
<em>oʻqi!</em>, <em>oʻqing!</em>, <em>oʻqima!</em> bor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Buyruq shaklini «они́» dan yasaysiz</li>
    <li>Uchta tugashni ajratasiz: <b>-Й, -И, -Ь</b></li>
    <li>Vid tanlovini bilasiz: <b>чита́й</b> ↔ <b>прочита́й</b></li>
    <li><b>Дава́й</b> bilan taklif qilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Yasalishi</span>
  <span class="pe-chip pe-chip--s">чита́<b>ют</b></span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">чита́<b>й</b></span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">чита́<b>йте</b></span>
</div>

<h3>1. Uch qadam</h3>

<ol class="pe-steps">
  <li>Feʼlning <b>«они́»</b> shaklini oling: <em>чита́<b>ют</b></em>,
      <em>говор<b>я́т</b></em>, <em>ста́в<b>ят</b></em>.</li>
  <li>Qoʻshimchani olib tashlang: <em>чита́-</em>, <em>говор-</em>,
      <em>став-</em>.</li>
  <li>Oxiriga <b>-Й</b>, <b>-И</b> yoki <b>-Ь</b> qoʻshing — qaysi
      biri, quyida.</li>
</ol>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Oʻzak qanday tugaydi</th><th>Qoʻshimcha</th><th>Misol</th></tr>
  <tr><td class="pr-uz">unli bilan</td><td class="pr-res">-Й / -ЙТЕ</td>
      <td class="pr-end">чита́ю<b>т</b> → чита́й · де́лай · слу́шай</td></tr>
  <tr><td class="pr-uz">undosh + urgʻu qoʻshimchada</td><td class="pr-res">-И / -ИТЕ</td>
      <td class="pr-end">говоря́т → говори́ · пиши́ · смотри́</td></tr>
  <tr><td class="pr-uz">undosh + urgʻu oʻzakda</td><td class="pr-res">-Ь / -ЬТЕ</td>
      <td class="pr-end">гото́вят → готовь · отве́ть · будь</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ustoz maslahati</span>
Ikkinchi qatorni tekshirishning oson yoʻli — <b>«я» shakliga qarash</b>.
Agar unda urgʻu qoʻshimchada boʻlsa (<em>пиш<b>у́</b>, говор<b>ю́</b>,
смотр<b>ю́</b></em>), buyruqda <b>-И</b> boʻladi. Agar oʻzakda boʻlsa
(<em>гот<b>о́</b>влю, отв<b>е́</b>чу</em>), <b>-Ь</b> boʻladi.<br><br>
Amalda birinchi guruh eng katta: <em>-ать</em> ga tugaydigan feʼllarning
deyarli hammasi <b>-Й</b> oladi.</div>

<h3>2. Ты va вы</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ты</th><th>Вы (yoki koʻplik)</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">чита́й</td><td class="pr-end">чита́йте</td>
      <td class="pr-uz">oʻqi / oʻqing</td></tr>
  <tr><td class="pr-res">иди́</td><td class="pr-end">иди́те</td>
      <td class="pr-uz">bor / boring</td></tr>
  <tr><td class="pr-res">скажи́</td><td class="pr-end">скажи́те</td>
      <td class="pr-uz">ayt / ayting</td></tr>
  <tr><td class="pr-res">будь</td><td class="pr-end">бу́дьте</td>
      <td class="pr-uz">boʻl / boʻling</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu dars siz uchun eng oson darslardan biri boʻlishi kerak, chunki
oʻzbekchada <b>aynan shu tizim</b> bor:<br><br>
<em>oʻqi<b>!</b></em> → <b>чита́й!</b> &nbsp;(sen)<br>
<em>oʻqi<b>ng</b>!</em> → <b>чита́йте!</b> &nbsp;(siz, hurmat)<br>
<em>oʻqi<b>ma</b>!</em> → <b>не чита́й!</b> &nbsp;(inkor)<br><br>
Ikkala tilda ham buyruq feʼlning eng qisqa shakli, va ikkalasida ham
<b>hurmat shakli</b> alohida. Farq faqat yasalishda: oʻzbekchada
qoʻshimcha (<em>-ng</em>), ruschada esa <em>-те</em>.<br><br>
Va yana bir moslik: oʻzbekcha <em>Kelinglar, boshlaymiz!</em> —
ruschada <em>Дава́йте начнём!</em> Ikkalasi ham «birga qilaylik» degan
taklif.</div>

<h3>3. Vid: чита́й yoki прочита́й?</h3>

<p>PR-54 da bu masala qisqa koʻrilgan edi. Endi toʻliq:</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">НСВ — umumiy taklif</p>
    <p><em><b>Чита́й</b> ка́ждый день.</em><br>Har kuni oʻqi.</p>
    <p><em><b>Заходи́!</b></em> — Kiraver! (taklif, xushmuomalalik)</p>
    <p>Takror, odat, umumiy maslahat.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">СВ — aniq vazifa</p>
    <p><em><b>Прочита́й</b> э́ту страни́цу.</em><br>Bu sahifani oʻqib chiq.</p>
    <p><em><b>Скажи́</b> мне пра́вду.</em> — Menga rostini ayt.</p>
    <p>Bir marta, aniq natija.</p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Inkor buyruqda deyarli har doim НСВ</b>:<br>
<em>Не чита́й! Не де́лай! Не опа́здывай! Не говори́!</em><br><br>
СВ bilan inkor buyruq boshqa maʼno beradi — bu <b>ogohlantirish</b>:<br>
<em>Не упади́!</em> — Yiqilib qolma! (ehtiyot boʻl)<br>
<em>Не забу́дь!</em> — Unutib qoʻyma!<br>
Yaʼni <em>не де́лай</em> — «qilma», <em>не сде́лай</em> — «qilib
qoʻyma». Birinchisi taqiq, ikkinchisi ogohlantirish.</div>

<h3>4. Дава́й / дава́йте — «kelinglar»</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-res">Дава́й пойдём!</td><td class="pr-end">Kel, ketaylik!</td></tr>
  <tr><td class="pr-res">Дава́йте начнём.</td><td class="pr-end">Boshlaylik.</td></tr>
  <tr><td class="pr-res">Дава́й чита́ть вме́сте.</td><td class="pr-end">Birga oʻqiylik.</td></tr>
  <tr><td class="pr-res">Пойдём!</td><td class="pr-end">Ketdik!</td></tr>
</table></div>

<p>СВ bilan <em>дава́й</em> + kelasi zamon (<em>дава́й пойдём</em>), НСВ
bilan <em>дава́й</em> + infinitiv (<em>дава́й чита́ть</em>).</p>

<h3>5. Notoʻgʻri shakllar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Infinitiv</th><th>Buyruq</th><th>Izoh</th></tr>
  <tr><td class="pr-res">быть</td><td class="pr-end">будь · бу́дьте</td>
      <td class="pr-uz">«бу́дьте добры́» — muloyim soʻrov</td></tr>
  <tr><td class="pr-res">дать</td><td class="pr-end">дай · да́йте</td>
      <td class="pr-uz">«да́йте, пожа́луйста»</td></tr>
  <tr><td class="pr-res">есть</td><td class="pr-end">ешь · е́шьте</td>
      <td class="pr-uz">dasturxonda</td></tr>
  <tr><td class="pr-res">пить</td><td class="pr-end">пей · пе́йте</td>
      <td class="pr-uz">—</td></tr>
  <tr><td class="pr-res">е́хать</td><td class="pr-end">поезжа́й · поезжа́йте</td>
      <td class="pr-uz">«е́хай» degan shakl <b>yoʻq</b></td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Е́хай в Москву́!</s></p>
  <p class="pe-good"><b>Поезжа́й</b> в Москву́ — <em>е́хать</em> ning buyrugʻi alohida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Не прочита́й э́ту кни́гу!</s></p>
  <p class="pe-good">Не <b>чита́й</b> э́ту кни́гу — inkor buyruqda НСВ</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Чита́ть э́ту страни́цу!</s></p>
  <p class="pe-good"><b>Прочита́й</b> э́ту страни́цу — infinitiv buyruq emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Говори́те мне пра́вду сейча́с.</s></p>
  <p class="pe-good"><b>Скажи́те</b> мне пра́вду — aniq vazifa, demak СВ</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>де́лать</b> feʼlining buyruq shakli qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>де́лай · де́лайте</strong>.
    «Они́» shakli <em>де́лают</em>, oʻzak <em>де́ла-</em> unli bilan
    tugaydi — demak <b>-Й</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>писа́ть</b> feʼlining buyruq shakli qanday?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>пиши́ · пиши́те</strong>. «Они́»
    shakli <em>пи́шут</em>, oʻzak <em>пиш-</em> undosh bilan; «я» shaklida
    urgʻu qoʻshimchada (<em>пишу́</em>) — demak <b>-И</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     <b>чита́й</b> yoki <b>прочита́й</b>? &nbsp;
     <b>___ э́ту страни́цу и скажи́ мне.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Прочита́й</strong>. Aniq vazifa,
    bir marta, natija kutilyapti — demak СВ. <em>Чита́й</em> umumiy
    maslahat boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu ikki gapning farqi nima?<br>
     <b>Не де́лай э́то! · Не сде́лай оши́бку!</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — <b>taqiq</b>: «buni qilma».
    Ikkinchisi — <b>ogohlantirish</b>: «xato qilib qoʻyma, ehtiyot boʻl».
    Inkor buyruqda НСВ taqiq, СВ esa ogohlantirish beradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Иди́те пря́мо. &nbsp; б) Е́хай в Москву́!<br>
     в) Дава́йте начнём. &nbsp; г) Не опа́здывай.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>б)</strong>. Toʻgʻrisi —
    <b>Поезжа́й в Москву́</b>. <em>Е́хать</em> ning buyruq shakli alohida
    va u <em>-езжа́й</em> dan yasaladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>чита́й / чита́йте</b><span>oʻqi / oʻqing</span></li>
  <li><b>скажи́ / скажи́те</b><span>ayt / ayting</span></li>
  <li><b>иди́ / иди́те</b><span>bor / boring</span></li>
  <li><b>поезжа́й</b><span>bor (transportda)</span></li>
  <li><b>будь / бу́дьте</b><span>boʻl / boʻling</span></li>
  <li><b>дава́й / дава́йте</b><span>kel / kelinglar</span></li>
  <li><b>не опа́здывай</b><span>kechikma</span></li>
  <li><b>сотру́дник</b><span>xodim</span></li>
  <li><b>па́мятка</b><span>eslatma varaqasi</span></li>
  <li><b>ошиба́ться</b><span>xato qilmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Yasalish: <b>«они́» shakli</b> minus qoʻshimcha, plus
        <b>-Й / -И / -Ь</b>.</li>
    <li>Unli bilan tugasa <b>-Й</b>; undosh + urgʻu qoʻshimchada
        <b>-И</b>; undosh + urgʻu oʻzakda <b>-Ь</b>.</li>
    <li><b>Вы</b> shakli <b>-те</b> qoʻshadi: <em>чита́йте</em>.</li>
    <li>Vid: <b>НСВ</b> umumiy taklif, <b>СВ</b> aniq vazifa.</li>
    <li><b>Inkor buyruq → НСВ</b>: <em>не чита́й</em>. СВ bilan bu
        <b>ogohlantirish</b> boʻladi: <em>не упади́!</em></li>
    <li><b>Дава́й / дава́йте</b> — «kelinglar, qilaylik».</li>
    <li>Yodlang: <b>поезжа́й</b> (<em>«е́хай»</em> yoʻq).</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-60: Shartli mayl — бы: если бы, я хотел бы, на твоём месте я бы…",
        "category": "russian",
        "order": 60,
        "summary": (
            "Rus tilidagi eng oson qurilishlardan biri: oʻtgan zamon + БЫ. "
            "Tuslanish yoʻq, zamon yoʻq, istisno yoʻq — bitta soʻz butun mayl "
            "yasaydi."
        ),
        "stories": ["Е́сли бы я знал ра́ньше"],
        "content": """
<h2>PR-60: Shartli mayl — бы: если бы, я хотел бы, на твоём месте я бы…</h2>

<p>Bu dars — dam olish. Rus tilidagi shartli mayl (усло́вное наклоне́ние)
<b>bitta soʻz</b> bilan yasaladi: <b>бы</b>. Va u qoʻshiladigan shakl —
oddiy <b>oʻtgan zamon</b>. Tuslanish yoʻq. Zamon yoʻq. Istisno yoʻq.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Oʻtgan zamon + бы</b> qolipini oʻrganasiz</li>
    <li><b>Е́сли бы…, … бы</b> qurilishini yasaysiz</li>
    <li>Muloyim soʻrov aytasiz: <b>я хоте́л бы</b></li>
    <li>Maslahat berasiz: <b>на твоём ме́сте я бы…</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Butun qoida</span>
  <span class="pe-chip pe-chip--s">oʻtgan zamon</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">бы</span>
</div>

<h3>1. Yasalishi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Oʻtgan zamon</th><th>Shartli mayl</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">я чита́л</td><td class="pr-end">я чита́л бы</td>
      <td class="pr-uz">oʻqirdim</td></tr>
  <tr><td class="pr-res">она́ сказа́ла</td><td class="pr-end">она́ сказа́ла бы</td>
      <td class="pr-uz">aytardi</td></tr>
  <tr><td class="pr-res">мы пошли́</td><td class="pr-end">мы пошли́ бы</td>
      <td class="pr-uz">borardik</td></tr>
  <tr><td class="pr-res">я хоте́л</td><td class="pr-end">я хоте́л бы</td>
      <td class="pr-uz">xohlardim</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
Shakl <b>jinsga qaraydi</b> (chunki u oʻtgan zamon), lekin <b>zamonga
qaramaydi</b>. <em>Я сказа́л бы</em> — «aytardim» yoki «aytgan boʻlardim»,
ikkalasi ham. Kontekst hal qiladi.<br><br>
<b>Бы</b> ning joyi erkin: <em>Я <b>бы</b> сказа́л</em> va <em>Я сказа́л
<b>бы</b></em> — ikkalasi ham toʻgʻri. Odatda u feʼldan keyin yoki
gapning birinchi urgʻuli soʻzidan keyin turadi.</div>

<h3>2. Е́сли бы… , … бы</h3>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--v">Е́сли бы</span> я знал,
     я <span class="pe-hl pe-hl--v">бы</span> сказа́л.</p>
  <p class="pe-ex__uz">Bilganimda aytardim.</p>
  <p class="pe-ex__why">Diqqat: <b>бы</b> <em>ikkala</em> qismda ham bor.
     Birinchisida <em>е́сли бы</em>, ikkinchisida yolgʻiz <em>бы</em>.</p>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
<b>Е́сли</b> va <b>е́сли бы</b> — bu ikki xil gap:<br>
<em><b>Е́сли</b> я узна́ю, я скажу́.</em> — Bilsam, aytaman. <b>Haqiqiy
shart</b>: hali boʻlishi mumkin.<br>
<em><b>Е́сли бы</b> я знал, я бы сказа́л.</em> — Bilganimda aytardim.
<b>Noreal shart</b>: bilmadim, aytmadim.<br><br>
Birinchisida oddiy zamonlar ishlatiladi, ikkinchisida — oʻtgan zamon +
бы. Buni chalkashtirmang.</div>

<h3>3. Muloyim soʻrov</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Toʻgʻridan-toʻgʻri</th><th>Muloyimroq</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Я хочу́ ко́фе.</td><td class="pr-end">Я хоте́л бы ко́фе.</td>
      <td class="pr-uz">Kofe xohlardim.</td></tr>
  <tr><td class="pr-res">Мо́жно спроси́ть?</td><td class="pr-end">Мо́жно бы́ло бы спроси́ть?</td>
      <td class="pr-uz">Soʻrasam boʻladimi?</td></tr>
  <tr><td class="pr-res">Вы помо́жете?</td><td class="pr-end">Вы не помогли́ бы?</td>
      <td class="pr-uz">Yordam bermasmidingiz?</td></tr>
</table></div>

<p><b>Я хоте́л бы</b> — restoran, doʻkon va rasmiy suhbatda eng koʻp
ishlatiladigan ibora. Uni butunligicha yodlang: ayol kishi
<em>я хоте́ла бы</em> deydi.</p>

<h3>4. Maslahat: на твоём ме́сте</h3>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--adv">На твоём ме́сте</span>
     я <span class="pe-hl pe-hl--v">бы</span> не пошёл.</p>
  <p class="pe-ex__uz">Sening oʻrningda boʻlsam, bormasdim.</p>
  <p class="pe-ex__why">Bu maslahat berishning eng muloyim yoʻli — chunki
     u buyruq emas. Rasmiy shakli: <em>на ва́шем ме́сте</em>.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbek tilida shart mayli bor va u ancha boy — <em>-sa</em>,
<em>-ganda</em>, <em>-sa edi</em>, <em>-ardi</em>. Ruscha esa bularning
hammasini <b>bitta</b> qurilish bilan qoplaydi.<br><br>
<em>bil<b>ganimda</b> ayt<b>ardim</b></em> → <em>е́сли <b>бы</b> я знал,
я <b>бы</b> сказа́л</em><br>
<em>xohl<b>ardim</b></em> → <em>я хоте́л <b>бы</b></em><br>
<em>sening oʻrningda boʻl<b>sam</b>, bormas<b>dim</b></em> → <em>на твоём
ме́сте я <b>бы</b> не пошёл</em><br><br>
Yaʼni oʻzbekchada bir necha shakl bor, ruschada bittasi. <b>Bu safar
ruscha osonroq.</b><br><br>
Faqat bitta narsani eslab qoling: oʻzbekchada shart <b>birinchi</b>
qismda belgilanadi (<em>bilganimda</em>), ruschada esa <b>ikkala</b>
qismda ham <em>бы</em> qoʻyiladi.</div>

<h3>5. Yana bir necha ishlatilishi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Что бы ты сде́лал?</td><td class="pr-end">Sen nima qilarding?</td></tr>
  <tr><td class="pr-res">Я бы не сказа́л.</td><td class="pr-end">Men aytmasdim.</td></tr>
  <tr><td class="pr-res">Хорошо́ бы отдохну́ть.</td><td class="pr-end">Dam olsak yaxshi boʻlardi.</td></tr>
  <tr><td class="pr-res">Он мог бы помо́чь.</td><td class="pr-end">U yordam bera olardi.</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Е́сли бы я зна́ю, я бы сказа́л.</s></p>
  <p class="pe-good">Е́сли бы я <b>знал</b> — <em>бы</em> faqat oʻtgan zamon bilan</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Е́сли бы я знал, я сказа́л.</s></p>
  <p class="pe-good">…я <b>бы</b> сказа́л — <em>бы</em> ikkala qismda ham kerak</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я бы хочу́ ко́фе.</s></p>
  <p class="pe-good">Я <b>хоте́л бы</b> ко́фе — oʻtgan zamon shakli</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Е́сли бы за́втра бу́дет дождь…</s></p>
  <p class="pe-good"><b>Е́сли</b> за́втра бу́дет дождь… — haqiqiy shart, <em>бы</em> siz</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Shartli mayl qanday yasaladi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Oʻtgan zamon + бы</strong>. Boshqa
    hech narsa: tuslanish yoʻq, zamon yoʻq. Shakl faqat jinsga qaraydi,
    chunki u oʻtgan zamon.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Е́сли бы я ___, я бы сказа́л.</b> (знать)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>знал</strong>. <em>Бы</em> faqat
    oʻtgan zamon bilan ishlaydi. <em>«Е́сли бы я зна́ю»</em> — xato.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapning farqi nima?<br>
     <b>Е́сли я узна́ю, я скажу́. · Е́сли бы я знал, я бы сказа́л.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — <b>haqiqiy shart</b>: hali
    boʻlishi mumkin («bilsam, aytaman»). Ikkinchisi — <b>noreal</b>:
    bilmadim, aytmadim («bilganimda aytardim»).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni muloyimroq qiling: <b>Я хочу́ ко́фе.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Я хоте́л бы ко́фе</strong> (ayol
    kishi: <em>я хоте́ла бы</em>). Bu restoran va doʻkonda eng koʻp
    ishlatiladigan ibora.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Я бы не сказа́л. &nbsp; б) Е́сли бы я знал, я бы помо́г.<br>
     в) Я бы хочу́ ко́фе. &nbsp; г) На твоём ме́сте я бы не пошёл.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Я хоте́л бы ко́фе</b>. <em>Бы</em> hozirgi zamon bilan
    ishlatilmaydi — faqat oʻtgan zamon bilan.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>бы</b><span>shart mayli yuklamasi</span></li>
  <li><b>е́сли бы</b><span>agar … boʻlganda</span></li>
  <li><b>я хоте́л бы</b><span>xohlardim</span></li>
  <li><b>на твоём ме́сте</b><span>sening oʻrningda</span></li>
  <li><b>сове́т</b><span>maslahat</span></li>
  <li><b>оши́бка</b><span>xato</span></li>
  <li><b>о́пыт</b><span>tajriba</span></li>
  <li><b>верну́ться</b><span>qaytmoq</span></li>
  <li><b>ча́ще</b><span>tez-tezroq</span></li>
  <li><b>бо́льше · ме́ньше</b><span>koʻproq · kamroq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Butun qoida: <b>oʻtgan zamon + бы</b>. Tuslanish ham, zamon ham
        yoʻq.</li>
    <li><b>Е́сли бы…, … бы</b> — <em>бы</em> <b>ikkala</b> qismda.</li>
    <li><b>Е́сли</b> (haqiqiy shart) ↔ <b>е́сли бы</b> (noreal shart).</li>
    <li><b>Я хоте́л бы</b> — muloyim soʻrovning standart shakli.</li>
    <li><b>На твоём ме́сте я бы…</b> — maslahat berishning muloyim
        yoʻli.</li>
    <li>Oʻzbekchada bir necha shakl bor, ruschada bittasi — <b>bu safar
        ruscha osonroq</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-61: Majhul nisbat: дом строится / дом построен",
        "category": "russian",
        "order": 61,
        "summary": (
            "Ish kim tomonidan qilinganini aytmaslik kerak boʻlganda majhul "
            "nisbat ishlatiladi. Rus tilida uning ikki shakli bor — va farq "
            "oʻsha tanish vid farqi."
        ),
        "stories": ["Как был постро́ен Петербу́рг"],
        "content": """
<h2>PR-61: Majhul nisbat: дом строится / дом построен</h2>

<p>Baʼzan gapda <b>kim qilgani muhim emas</b> — muhimi, nima
qilinganligi. «Uy qurildi» — kim qurgani aytilmagan. Bunday gaplarni
<b>majhul nisbat</b> (страда́тельный зало́г) deyiladi.</p>

<p>Rus tilida uning <b>ikkita</b> shakli bor, va ular orasidagi farq
sizga allaqachon tanish: <b>jarayon</b> yoki <b>natija</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>-ся</b> bilan majhul nisbat yasaysiz: <b>дом стро́ится</b></li>
    <li>Qisqa sifatdosh bilan yasaysiz: <b>дом постро́ен</b></li>
    <li>Bajaruvchini <b>Твори́тельный</b> bilan qoʻshasiz</li>
    <li>Uchala zamonda ishlatasiz</li>
  </ul>
</div>

<div class="pr-aspect">
  <div class="pr-aspect__side">
    <p class="pr-aspect__h">НСВ — jarayon</p>
    <p class="pr-aspect__v">дом стро́ится</p>
    <p>Uy qurilyapti. Ish davom etyapti, natija hali yoʻq.</p>
  </div>
  <div class="pr-aspect__side pr-aspect__side--sv">
    <p class="pr-aspect__h">СВ — natija</p>
    <p class="pr-aspect__v">дом постро́ен</p>
    <p>Uy qurilgan. Ish tugagan, natija bor.</p>
  </div>
</div>

<h3>1. Birinchi shakl: -ся</h3>

<p>НСВ feʼlga <b>-ся</b> qoʻshiladi. Bu PR-25 dagi qaytim qoʻshimchasining
yana bir vazifasi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Faol</th><th>Majhul</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-res">Рабо́чие стро́ят дом.</td>
      <td class="pr-end">Дом стро́ится.</td><td class="pr-uz">Uy qurilyapti.</td></tr>
  <tr><td class="pr-res">Здесь продаю́т хлеб.</td>
      <td class="pr-end">Хлеб продаётся здесь.</td><td class="pr-uz">Non shu yerda sotiladi.</td></tr>
  <tr><td class="pr-res">Кни́гу чита́ют мно́гие.</td>
      <td class="pr-end">Кни́га чита́ется легко́.</td><td class="pr-uz">Kitob oson oʻqiladi.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ehtiyot boʻling</span>
Bu shakl faqat <b>uchinchi shaxsda</b> ishlaydi — <em>стро́ится,
стро́ятся</em>. <em>«Я строюсь»</em> majhul nisbat emas.<br><br>
Va u faqat <b>НСВ</b> feʼllardan yasaladi. СВ uchun ikkinchi shakl
kerak.</div>

<h3>2. Ikkinchi shakl: qisqa sifatdosh</h3>

<p>СВ feʼldan <b>qisqa sifatdosh</b> yasaladi. U sifat kabi jins va son
boʻyicha moslashadi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Feʼl (СВ)</th><th>erkak</th><th>ayol</th><th>oʻrta</th><th>koʻplik</th></tr>
  <tr><td class="pr-res">постро́ить</td><td class="pr-end">постро́ен</td>
      <td class="pr-end">постро́ена</td><td class="pr-end">постро́ено</td>
      <td class="pr-end">постро́ены</td></tr>
  <tr><td class="pr-res">написа́ть</td><td class="pr-end">напи́сан</td>
      <td class="pr-end">напи́сана</td><td class="pr-end">напи́сано</td>
      <td class="pr-end">напи́саны</td></tr>
  <tr><td class="pr-res">откры́ть</td><td class="pr-end">откры́т</td>
      <td class="pr-end">откры́та</td><td class="pr-end">откры́то</td>
      <td class="pr-end">откры́ты</td></tr>
  <tr><td class="pr-res">закры́ть</td><td class="pr-end">закры́т</td>
      <td class="pr-end">закры́та</td><td class="pr-end">закры́то</td>
      <td class="pr-end">закры́ты</td></tr>
  <tr><td class="pr-res">найти́</td><td class="pr-end">на́йден</td>
      <td class="pr-end">на́йдена</td><td class="pr-end">на́йдено</td>
      <td class="pr-end">на́йдены</td></tr>
  <tr><td class="pr-res">сде́лать</td><td class="pr-end">сде́лан</td>
      <td class="pr-end">сде́лана</td><td class="pr-end">сде́лано</td>
      <td class="pr-end">сде́ланы</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__ru"><span class="pe-hl pe-hl--s">Магази́н</span>
     <span class="pe-hl pe-hl--v">закры́т</span>.
     <span class="pe-hl pe-hl--s">Дверь</span>
     <span class="pe-hl pe-hl--v">закры́та</span>.</p>
  <p class="pe-ex__uz">Doʻkon yopiq. Eshik yopiq.</p>
  <p class="pe-ex__why">Shakl <b>egaga</b> moslashadi:
     <em>магази́н</em> erkak, <em>дверь</em> ayol jinsida. Bu — sifat
     kabi.</p>
</div>

<h3>3. Zamon: был / бу́дет</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Zamon</th><th>Gap</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-uz">Hozir</td><td class="pr-res">Дом постро́ен.</td>
      <td class="pr-end">Uy qurilgan (hozir turibdi).</td></tr>
  <tr><td class="pr-uz">Kecha</td><td class="pr-res">Дом был постро́ен.</td>
      <td class="pr-end">Uy qurilgan edi.</td></tr>
  <tr><td class="pr-uz">Ertaga</td><td class="pr-res">Дом бу́дет постро́ен.</td>
      <td class="pr-end">Uy quriladi.</td></tr>
</table></div>

<p>Yaʼni <b>быть</b> qoʻshiladi va u odatdagidek ishlaydi: hozirgi zamonda
aytilmaydi (PR-11), oʻtgan va kelasi zamonda paydo boʻladi.</p>

<h3>4. Bajaruvchi — Твори́тельный</h3>

<div class="pe-ex">
  <p class="pe-ex__ru">Дом <span class="pe-hl pe-hl--v">постро́ен</span>
     <span class="pe-hl pe-hl--o">рабо́чими</span>.</p>
  <p class="pe-ex__uz">Uy ishchilar tomonidan qurilgan.</p>
  <p class="pe-ex__why">Kim qilgani aytilsa — u <b>Твори́тельный</b>'ga
     kiradi (PR-39). Lekin majhul nisbatning butun maqsadi koʻpincha
     bajaruvchini <b>aytmaslik</b>, shuning uchun bu qism
     tez-tez tushirib qoldiriladi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu dars siz uchun tanish, chunki oʻzbekchada ham majhul nisbat bor va u
<b>qoʻshimcha</b> bilan yasaladi — <b>-il-</b> yoki <b>-in-</b>:<br><br>
<em>qur-<b>il</b>-di</em> → <em>постро́ен</em><br>
<em>yoz-<b>il</b>-gan</em> → <em>напи́сан</em><br>
<em>och-<b>il</b>-di</em> → <em>откры́т</em><br><br>
Va oʻzbekchada ham <b>jarayon</b> va <b>natija</b> ajratiladi:<br>
<em>uy qur<b>ilyapti</b></em> → <em>дом стро́ится</em> (jarayon)<br>
<em>uy qur<b>ilgan</b></em> → <em>дом постро́ен</em> (natija)<br><br>
Bitta farq bor: bajaruvchini aytishda oʻzbekcha <b>«tomonidan»</b>
soʻzini ishlatadi (<em>ishchilar tomonidan</em>), ruscha esa
<b>Твори́тельный</b> kelishigini (<em>рабо́чими</em>). Yaʼni oʻzbekchada
qoʻshimcha soʻz, ruschada qoʻshimcha.</div>

<h3>5. Amalda qayerda uchraydi</h3>

<div class="pe-grid">
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">1</span>Eʼlonlar</p>
    <p><em>Откры́то</em> · <em>Закры́то</em><br>
       <em>Вход воспрещён</em> — kirish taqiqlangan.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">2</span>Tarix</p>
    <p><em>Го́род был осно́ван в 1703 году́.</em><br>
       Kim asos solgani ikkinchi darajali.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">3</span>Xabarlar</p>
    <p><em>Мост постро́ен.</em> · <em>Кни́га напи́сана.</em><br>
       Faktning oʻzi muhim.</p></div>
  <div class="pe-card"><p class="pe-card__h"><span class="pe-card__n">4</span>Kundalik</p>
    <p><em>Всё сде́лано.</em> — Hammasi bajarildi.<br>
       <em>Ключи́ на́йдены.</em> — Kalitlar topildi.</p></div>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Дверь закры́т.</s></p>
  <p class="pe-good">Дверь <b>закры́та</b> — <em>дверь</em> ayol jinsida</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Дом стро́ится рабо́чих.</s></p>
  <p class="pe-good">Дом стро́ится <b>рабо́чими</b> — bajaruvchi Твори́тельный'da</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Дом построи́лся вчера́.</s></p>
  <p class="pe-good">Дом <b>был постро́ен</b> — СВ uchun qisqa sifatdosh</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кни́га напи́сан Толсты́м.</s></p>
  <p class="pe-good">Кни́га <b>напи́сана</b> Толсты́м — ayol jinsi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu ikki gapning farqi nima?<br>
     <b>Дом стро́ится. · Дом постро́ен.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Jarayon</strong> (hali qurilyapti)
    va <strong>natija</strong> (qurib boʻlingan). Bu PR-51 dagi vid
    farqining majhul nisbatdagi koʻrinishi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Boʻsh joyga: <b>Дверь ___.</b> (закры́ть)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>закры́та</strong>. Qisqa
    sifatdosh egaga moslashadi, <em>дверь</em> esa ayol jinsida.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Boʻsh joyga: <b>Дом постро́ен ___.</b> (рабо́чие)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>рабо́чими</strong> —
    Твори́тельный koʻplik. Oʻzbekchada bu «ishchilar <b>tomonidan</b>»
    boʻlardi; ruschada alohida soʻz kerak emas, kelishik
    yetarli.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni oʻtgan zamonga oʻtkazing: <b>Дом постро́ен.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Дом был постро́ен.</strong>
    <em>Быть</em> odatdagidek ishlaydi: hozirgi zamonda aytilmaydi,
    oʻtgan va kelasi zamonda paydo boʻladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Qaysi gap notoʻgʻri?<br>
     а) Магази́н закры́т. &nbsp; б) Кни́га напи́сана Толсты́м.<br>
     в) Дверь закры́т. &nbsp; г) Ключи́ на́йдены.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>в)</strong>. Toʻgʻrisi —
    <b>Дверь закры́та</b>. Qisqa sifatdosh egaga moslashadi, va
    <em>дверь</em> ayol jinsida.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>стро́иться</b><span>qurilmoq (jarayon)</span></li>
  <li><b>постро́ен</b><span>qurilgan (natija)</span></li>
  <li><b>напи́сан</b><span>yozilgan</span></li>
  <li><b>откры́т · закры́т</b><span>ochiq · yopiq</span></li>
  <li><b>на́йден</b><span>topilgan</span></li>
  <li><b>осно́ван</b><span>asos solingan</span></li>
  <li><b>кре́пость</b><span>qalʼa</span></li>
  <li><b>боло́то</b><span>botqoq</span></li>
  <li><b>столи́ца</b><span>poytaxt</span></li>
  <li><b>век</b><span>asr</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Ikki shakl: <b>-ся</b> (jarayon, НСВ) va <b>qisqa sifatdosh</b>
        (natija, СВ).</li>
    <li><em>Дом стро́ится</em> — qurilyapti. <em>Дом постро́ен</em> —
        qurilgan.</li>
    <li>Qisqa sifatdosh <b>egaga moslashadi</b>: <em>закры́т,
        закры́та, закры́то, закры́ты</em>.</li>
    <li>Zamon <b>быть</b> bilan: <em>был постро́ен, бу́дет
        постро́ен</em>.</li>
    <li>Bajaruvchi <b>Твори́тельный</b>'da: <em>постро́ен
        рабо́чими</em>.</li>
    <li>Oʻzbekchada bu <b>-il- / -in-</b> qoʻshimchasi va
        <b>«tomonidan»</b> soʻzi — bir xil gʻoya, boshqa vosita.</li>
  </ul>
</div>
""",
    },
]
