# -*- coding: utf-8 -*-
"""Prime Russian — YAKUNIY BATCH: matn, tarix va xayrlashuv (98–100).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

BU KURSNING OXIRGI UCH DARSI. Uchtasi uch xil vazifa bajaradi:
98 — oʻquvchiga QUROL beradi (yozish skeleti),
99 — oʻquvchiga KALIT beradi (soʻz qayerdan kelgan),
100 — oʻquvchiga OYNA beradi (u qayerga yetib keldi).

PR-98 — matn qurish. Oʻzbekcha lever: oʻzbek maktabida insho aynan
uch qismdan (kirish — asosiy qism — xulosa) oʻrgatiladi, demak
oʻquvchi ME'MORCHILIKNI biladi, unga faqat ruscha gʻisht — «связки» —
kerak. Darsning gavhari: 15 ta bogʻlovchi soʻzni yodlagan odam
istalgan mavzuda insho yoza oladi. Tayyor skelet beriladi.
PR-99 — rus tilining qatlamlari. Kursdagi eng katta «voy!» darsi va
oʻzbek oʻquvchi uchun maxsus yozilgan:
  (a) ПОЛНОГЛАСИЕ kaliti — город/град, голова/глава, здоровье/
      здравствуйте. Kitobiy shakl MAVHUM maʼno oladi, ruscha shakl
      ANIQ maʼno: глава ≠ голова, страна ≠ сторона, краткий ≠ короткий.
      «Здравствуйте» PR-7 dan beri aytilib kelinadi — va u «здоровье».
  (b) TURKIY QATLAM — oʻquvchi bu soʻzlarni bolaligidan biladi:
      карандаш = qora tosh, изюм = uzum, богатырь = bahodir,
      сундук = sandiq, сарай = saroy, чемодан = jomadon, деньги = tanga.
      Bu — kursning 0.1-bandidagi «uchinchi sovgʻa» ning eng kuchli
      isboti va uni aynan oxirgi darslarda berish toʻgʻri: endi
      oʻquvchi buni tushunish uchun yetarli til biladi.
PR-100 — yakun. Maqtov emas, HISOBOT: qayerdasiz, nima qurdingiz,
nimani hali bilmaysiz, keyingi 100 kunda nima qilasiz. Oʻz-oʻzini
tekshirish matni bor — oʻquvchi PR-1 da oʻqiy olmagan matnni endi
oʻqiydi va oʻzgarishni oʻz koʻzi bilan koʻradi.

⚠️ Oʻqish matnlarida URGʻU BELGISI YOʻQ (2026-08-24) — darsliklar saqlaydi.

Mashqlar:        practice/management/commands/_practice_pr_98_100.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_98_100.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_98_100.py --author=prime
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
        "title": "PR-98: Matn qurish: kirish, asosiy qism, xulosa",
        "category": "russian",
        "order": 98,
        "summary": (
            "Insho arxitekturasini siz allaqachon bilasiz — u oʻzbekchada ham "
            "uch qismli. Sizga faqat 15 ta ruscha bogʻlovchi va tayyor skelet kerak."
        ),
        "stories": ["Как написать сочинение"],
        "content": """
<h2>PR-98: Matn qurish: kirish, asosiy qism, xulosa</h2>

<p>Ikki oʻquvchi bitta mavzuda insho yozdi. Ikkalasining
grammatikasi ham deyarli bir xil. Biri «5» oldi, ikkinchisi «3».</p>

<p>Farq qayerda edi?</p>

<p>Birinchisining matni <b>yoʻl</b> edi — kirish bor, har bir abzats
oldingisiga ulanadi, oxirida xulosa turibdi. Ikkinchisiniki
<b>uyum</b> edi — toʻgʻri gaplar, lekin tartibsiz.</p>

<p>Bu darsda gaplarni matnga aylantirishni oʻrganamiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Matnning <b>uch qismini</b> toʻgʻri toʻldirasiz</li>
    <li><b>15 ta bogʻlovchini</b> vazifasi boʻyicha olasiz</li>
    <li><b>Abzats qoidasini</b> bilasiz — bir abzats, bir fikr</li>
    <li>Tayyor <b>skeletni</b> qoʻlingizga olasiz</li>
    <li>Xulosani <b>kuchli</b> tugatasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qolip</span>
  <span class="pe-chip pe-chip--s">вступле́ние</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">основна́я часть</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">заключе́ние</span>
</div>

<h3>1. Arxitekturani siz allaqachon bilasiz</h3>

<div class="pe-call pe-uz"><span class="pe-call__t">Bu uchlik sizga maktabdan tanish</span>
Oʻzbek maktabida insho aynan shu uch qismdan oʻrgatiladi:<br><br>
<b>kirish</b> &nbsp;→&nbsp; <b>asosiy qism</b> &nbsp;→&nbsp; <b>xulosa</b><br><br>
Ruschada ham xuddi shunday:<br><br>
<b>вступле́ние</b> &nbsp;→&nbsp; <b>основна́я часть</b> &nbsp;→&nbsp;
<b>заключе́ние</b><br><br>
Yaʼni siz <b>meʼmorchilikni</b> bilasiz. Sizga yangi bino kerak
emas — sizga <b>ruscha gʻisht</b> kerak. Bu darsning butun mazmuni
shu gʻishtlarni berishdan iborat.<br><br>
Shuning uchun bu dars siz oʻylagandan osonroq boʻladi.</div>

<h3>2. Сочине́ние-рассужде́ние — eng koʻp soʻraladigan tur</h3>

<p>Maktabda ham, imtihonda ham eng koʻp soʻraladigan insho turi —
<b>fikr bildirish</b>. Uning ichki qolipi uchta:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Qism</th><th>Ichida nima</th><th>Necha gap</th></tr>
  <tr><td class="pr-stem">вступле́ние</td>
      <td class="pr-uz">mavzuni ochish + <b>те́зис</b> (asosiy fikringiz)</td>
      <td class="pr-end">2–3</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">основна́я часть</td>
      <td class="pr-uz"><b>аргуме́нты</b> — har bir dalil alohida abzatsda</td>
      <td class="pr-end">2 abzats</td></tr>
  <tr><td class="pr-stem">заключе́ние</td>
      <td class="pr-uz"><b>вы́вод</b> — tezisga qaytish, lekin boshqa soʻz bilan</td>
      <td class="pr-end">2–3</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Xulosa — takror emas</span>
Eng koʻp uchraydigan xato: xulosada kirishdagi jumlani
<b>soʻzma-soʻz</b> takrorlash.<br><br>
Xulosa tezisga <b>qaytadi</b>, lekin uni <b>boshqa soʻzlar</b> bilan
aytadi va unga dalillardan chiqqan bir narsa qoʻshadi.<br><br>
Kirish: <em>Я счита́ю, что чита́ть ну́жно ка́ждый день.</em><br>
Xulosa: <em>Таки́м о́бразом, ежедне́вное чте́ние — э́то не
привы́чка, а <b>инструме́нт</b>.</em></div>

<h3>3. Связки — 15 ta soʻz butun inshoni quradi</h3>

<p>Mana bu jadval — darsning eng qimmatli qismi. Uni yodlasangiz,
istalgan mavzuda yoza olasiz:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Vazifasi</th><th>Ruscha</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-stem">boshlash</td><td class="pr-res">Мно́гие счита́ют, что…</td>
      <td class="pr-end">Koʻpchilik shunday deb hisoblaydi…</td></tr>
  <tr><td class="pr-stem">boshlash</td><td class="pr-res">В на́ше вре́мя…</td>
      <td class="pr-end">Hozirgi zamonda…</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">fikr</td><td class="pr-res">На мой взгляд…</td>
      <td class="pr-end">Menimcha…</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">fikr</td><td class="pr-res">Я счита́ю, что…</td>
      <td class="pr-end">Men hisoblaymanki…</td></tr>
  <tr><td class="pr-stem">dalil 1</td><td class="pr-res">Во-пе́рвых…</td>
      <td class="pr-end">Birinchidan…</td></tr>
  <tr><td class="pr-stem">dalil 2</td><td class="pr-res">Во-вторы́х…</td>
      <td class="pr-end">Ikkinchidan…</td></tr>
  <tr><td class="pr-stem">qoʻshish</td><td class="pr-res">Кро́ме того́…</td>
      <td class="pr-end">Bundan tashqari…</td></tr>
  <tr><td class="pr-stem">misol</td><td class="pr-res">Наприме́р…</td>
      <td class="pr-end">Masalan…</td></tr>
  <tr><td class="pr-stem">tasdiq</td><td class="pr-res">Действи́тельно…</td>
      <td class="pr-end">Haqiqatan ham…</td></tr>
  <tr><td class="pr-stem">qarshi fikr</td><td class="pr-res">Одна́ко…</td>
      <td class="pr-end">Lekin…</td></tr>
  <tr><td class="pr-stem">qarshi fikr</td><td class="pr-res">С друго́й стороны́…</td>
      <td class="pr-end">Boshqa tomondan…</td></tr>
  <tr><td class="pr-stem">yon berish</td><td class="pr-res">Тем не ме́нее…</td>
      <td class="pr-end">Shunga qaramay…</td></tr>
  <tr><td class="pr-stem">sabab</td><td class="pr-res">Поэ́тому…</td>
      <td class="pr-end">Shuning uchun…</td></tr>
  <tr><td class="pr-stem">xulosa</td><td class="pr-res">Таки́м о́бразом…</td>
      <td class="pr-end">Shunday qilib…</td></tr>
  <tr><td class="pr-stem">xulosa</td><td class="pr-res">Подводя́ ито́г…</td>
      <td class="pr-end">Xulosa qilib aytganda…</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Bogʻlovchidan keyin vergul</span>
<b>Во-пе́рвых</b>, <b>кро́ме того́</b>, <b>таки́м о́бразом</b>,
<b>наприме́р</b> — bularning hammasi <b>kirish soʻz</b> (PR-97),
demak vergul bilan ajratiladi:<br><br>
✓ <em><b>Во-пе́рвых,</b> э́то до́рого.</em><br>
✓ <em><b>Таки́м о́бразом,</b> вы́вод очеви́ден.</em><br><br>
Lekin <b>одна́ко</b> gap boshida vergul <b>olmaydi</b> — u oʻsha
yerda «lekin» degani:<br>
✓ <em><b>Одна́ко</b> есть и друга́я сторона́.</em></div>

<h3>4. Abzats qoidasi</h3>

<div class="pe-call pe-rule"><span class="pe-call__t">Bir abzats — bir fikr</span>
Yangi fikr boshlanganda <b>yangi abzats</b> boshlanadi. Buning
tekshiruvi ham oddiy:<br><br>
<b>Har bir abzatsni bitta jumlada aytib bera olasizmi?</b><br><br>
Aytib bera olmasangiz — abzatsda ikki fikr bor, uni
<b>boʻling</b>. Aytadigan narsa chiqmasa — abzats
<b>keraksiz</b>.<br><br>
Rus oʻqituvchisi ishni birinchi qarashda shu bilan baholaydi: matn
<b>abzatslarga</b> boʻlinganmi yoki bir boʻlak boʻlib
turibdimi.</div>

<h3>5. Tayyor skelet — oʻzingizga koʻchirib oling</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Mavzu: «Ну́жно ли чита́ть кни́ги?»</p>
  <p class="pe-ex__ru"><b>В на́ше вре́мя</b> мно́гие говоря́т, что кни́ги
     бо́льше не нужны́. <b>На мой взгляд</b>, э́то не так.</p>
  <p class="pe-ex__ru"><b>Во-пе́рвых</b>, чте́ние у́чит ду́мать
     ме́дленно. <b>Наприме́р</b>, по́сле дли́нной кни́ги ле́гче
     поня́ть тру́дный текст.</p>
  <p class="pe-ex__ru"><b>Во-вторы́х</b>, кни́га даёт слова́.
     <b>Кро́ме того́</b>, она́ у́чит стро́ить фра́зу.</p>
  <p class="pe-ex__ru"><b>Одна́ко</b> я не счита́ю, что чита́ть на́до
     мно́го. <b>Тем не ме́нее</b> два́дцать мину́т в день меня́ют
     о́чень мно́гое.</p>
  <p class="pe-ex__ru"><b>Таки́м о́бразом</b>, кни́га — э́то не ста́рая
     привы́чка, а рабо́чий инструме́нт.</p>
  <p class="pe-ex__uz">Beshta abzats, beshta bogʻlovchi. Mavzuni
     almashtiring — skelet oʻsha-oʻsha qoladi.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Bu skelet nima uchun ishlaydi</span>
Eʼtibor bering: yuqoridagi inshoda <b>bitta ham qiyin grammatika
yoʻq</b>. U PR-30 gacha oʻrganilgan bilim bilan yozilgan.<br><br>
Yaxshi insho <b>qiyin gaplar</b>dan emas, <b>toʻgʻri
tartib</b>dan tugʻiladi. Shuning uchun oddiy yozing, lekin
<b>bogʻlab</b> yozing.</div>

<h3>6. Xulosani kuchli tugatish</h3>

<p>Xulosani mustahkamlashning uch yoʻli bor:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Usul</th><th>Misol</th></tr>
  <tr><td class="pr-stem">maqol (PR-95)</td>
      <td class="pr-res">Неда́ром говоря́т: <em>век живи́ — век учи́сь</em>.</td></tr>
  <tr><td class="pr-stem">savol</td>
      <td class="pr-res">А что вы́брали бы вы?</td></tr>
  <tr><td class="pr-stem">qisqa qatʼiy gap</td>
      <td class="pr-res">Вы́бор всегда́ остаётся за на́ми.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Xulosada qilinmaydigan uchta ish</span>
✗ <b>Yangi dalil qoʻshish</b> — dalillar asosiy qismda tugaydi.<br>
✗ <b>Kechirim soʻrash</b> — <s>Я, наве́рное, не о́чень хорошо́
объясни́л…</s><br>
✗ <b>Kirishni takrorlash</b> — bu xulosa emas, aylanma.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Во-пе́рвых э́то до́рого.</s></p>
  <p class="pe-good">Во-пе́рвых<b>,</b> э́то до́рого — kirish soʻzdan keyin
     vergul (PR-97).</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Одна́ко, есть и друга́я сторона́.</s></p>
  <p class="pe-good">Одна́ко есть и друга́я сторона́ — gap boshida
     <em>одна́ко</em> vergul olmaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Xulosa: <s>Итак, я счита́ю, что чита́ть ну́жно
     ка́ждый день.</s> (kirishdagi jumlaning oʻzi)</p>
  <p class="pe-good">Таки́м о́бразом, ежедне́вное чте́ние — э́то
     <b>рабо́чий инструме́нт</b>. — oʻsha fikr, boshqa soʻzlar bilan.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Beshta fikr — bitta abzats.</p>
  <p class="pe-good">Beshta fikr — <b>kamida</b> uchta abzats. Har bir
     abzatsni bitta jumlada aytib bera olishingiz kerak.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Bu bogʻlovchilarni vazifasi boʻyicha ajrating.<br>
     <b>Таки́м о́бразом · Во-пе́рвых · Одна́ко · На мой взгляд</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>На мой взгляд</strong> —
    fikr bildirish (kirishda) · <strong>Во-пе́рвых</strong> —
    birinchi dalil · <strong>Одна́ко</strong> — qarshi fikr ·
    <strong>Таки́м о́бразом</strong> — xulosa. Yaʼni ular
    inshoning toʻrt xil joyida turadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Vergulni toʻgʻri qoʻying.<br>
     <b>Во-пе́рвых э́то до́рого. Одна́ко есть и плюсы́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Во-пе́рвых, э́то
    до́рого. Одна́ко есть и плюсы́.</strong><br>
    <em>Во-пе́рвых</em> — kirish soʻz, vergul oladi.
    <em>Одна́ко</em> gap boshida «lekin» degani va vergul
    <b>olmaydi</b> (PR-97).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu xulosada nima notoʻgʻri?<br>
     <b>Таки́м о́бразом, чита́ть поле́зно. Кро́ме того́, кни́ги сейча́с
     о́чень дороги́е.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Xulosaga <strong>yangi
    dalil</strong> qoʻshilgan («kitoblar qimmat»). Dalillar asosiy
    qismda tugashi kerak. Xulosa faqat <b>yigʻadi</b>, yangi narsa
    ochmaydi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Abzatsni tekshiring: unda ikkita fikr bormi?<br>
     <b>Спорт поле́зен для здоро́вья. Он у́чит дисципли́не. А ещё в
     на́шем го́роде ма́ло стадио́нов.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Ha, <strong>ikkita</strong>.
    Birinchi ikki gap — sportning foydasi. Uchinchisi — butunlay
    boshqa mavzu (shahardagi sharoit). Uni <b>alohida
    abzatsga</b> chiqarish kerak.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Skelet boʻyicha kirish yozing.<br>
     <b>Mavzu: «Ну́жен ли шко́льнику телефо́н?»</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Masalan: <strong>В на́ше вре́мя
    телефо́н есть почти́ у ка́ждого шко́льника. Мно́гие счита́ют,
    что он то́лько меша́ет. На мой взгляд, де́ло не в телефо́не, а
    в том, как им по́льзоваться.</strong><br>
    Uch gap: mavzuni ochish → boshqalarning fikri → sizning
    <b>tezis</b>ingiz. Keyin <em>во-пе́рвых</em> bilan asosiy
    qism boshlanadi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>сочине́ние</b><span>insho</span></li>
  <li><b>вступле́ние</b><span>kirish</span></li>
  <li><b>основна́я часть</b><span>asosiy qism</span></li>
  <li><b>заключе́ние</b><span>xulosa</span></li>
  <li><b>те́зис</b><span>asosiy fikr</span></li>
  <li><b>аргуме́нт</b><span>dalil</span></li>
  <li><b>вы́вод</b><span>natija, xulosa</span></li>
  <li><b>абза́ц</b><span>abzats</span></li>
  <li><b>Таки́м о́бразом…</b><span>Shunday qilib…</span></li>
  <li><b>Подводя́ ито́г…</b><span>Xulosa qilib aytganda…</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Arxitektura sizga tanish: <b>kirish — asosiy qism —
        xulosa</b>. Sizga faqat ruscha bogʻlovchilar kerak edi.</li>
    <li><b>15 ta связка</b> istalgan inshoni quradi. Ularni
        vazifasi boʻyicha yodlang.</li>
    <li><b>Bir abzats — bir fikr.</b> Tekshiruv: abzatsni bitta
        jumlada ayta olasizmi?</li>
    <li>Kirish soʻzlardan keyin <b>vergul</b>; <b>одна́ко</b> gap
        boshida — <b>vergulsiz</b>.</li>
    <li>Xulosa tezisga <b>boshqa soʻzlar bilan</b> qaytadi —
        takrorlamaydi.</li>
    <li>Xulosada <b>yangi dalil yoʻq</b>, <b>kechirim yoʻq</b>.</li>
    <li>Yaxshi insho qiyin gaplardan emas, <b>toʻgʻri tartibdan</b>
        tugʻiladi.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-99: Rus tili qayerdan kelgan: soʻz boyligining kelib chiqishi",
        "category": "russian",
        "order": 99,
        "summary": (
            "«Здравствуйте» = «здоровье». «Карандаш» = qora tosh. Rus tilining "
            "toʻrt qatlami va ulardan bittasi sizga bolaligingizdan tanish."
        ),
        "stories": ["Откуда пришли русские слова"],
        "content": """
<h2>PR-99: Rus tili qayerdan kelgan: soʻz boyligining kelib chiqishi</h2>

<p>Siz <b>«Здра́вствуйте»</b> soʻzini PR-7 dan beri aytib kelyapsiz.
Uni yuz marta yozgansiz.</p>

<p>Uning maʼnosini bilasizmi?</p>

<p>U <b>«здоро́вье»</b> soʻzidan. <em>Здра́вствуйте</em> soʻzma-soʻz
«<b>sogʻ boʻling</b>» degani.</p>

<p>Faqat <em>здоро́вье</em> da <b>-оро-</b>, <em>здра́вствуйте</em> da
esa <b>-ра-</b> turibdi. Bu tasodif emas — bu <b>kalit</b>. Bu
darsda oʻsha kalitni olasiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Rus tilining <b>toʻrt qatlamini</b> koʻrasiz</li>
    <li><b>-оро- / -ра-</b> kalitini olasiz — u yuzlab soʻzni ochadi</li>
    <li>Ruschadagi <b>turkiy soʻzlarni</b> taniysiz — siz ularni bilasiz</li>
    <li>Yevropa qatlamini va uning ohangini bilasiz</li>
    <li>Notanish soʻzning <b>uslubini</b> kelib chiqishiga qarab aniqlaysiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Toʻrt qatlam</span>
  <span class="pe-chip pe-chip--s">slavyan</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">turkiy</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">yunon-lotin</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">yevropa</span>
</div>

<h3>1. Toʻrt qatlam</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Qatlam</th><th>Qachon</th><th>Misollar</th><th>Ohangi</th></tr>
  <tr><td class="pr-stem">slavyan (oʻz)</td><td class="pr-uz">eng qadimiy</td>
      <td class="pr-res">мать · брат · вода́ · дом · хлеб · рука́</td>
      <td class="pr-end">eng oddiy, eng issiq</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">turkiy</td><td class="pr-uz">X–XV asrlar</td>
      <td class="pr-res">каранда́ш · де́ньги · сунду́к · база́р</td>
      <td class="pr-end">kundalik, sezilmaydi</td></tr>
  <tr><td class="pr-stem">yunon-lotin</td><td class="pr-uz">cherkov va fan orqali</td>
      <td class="pr-res">шко́ла · тетра́дь · исто́рия · до́ктор</td>
      <td class="pr-end">neytral, oʻquv</td></tr>
  <tr><td class="pr-stem">yevropa</td><td class="pr-uz">XVIII asrdan</td>
      <td class="pr-res">матро́с · пальто́ · футбо́л · компью́тер</td>
      <td class="pr-end">yangi, texnik</td></tr>
</table></div>

<h3>2. Kalit: -ОРО- va -РА-</h3>

<p>Qadimda ikki til yonma-yon yashagan: xalq gapiradigan
<b>ruscha</b> va kitob yoziladigan <b>cherkov-slavyan</b> tili.
Koʻp soʻz <b>ikki shaklda</b> saqlanib qolgan.</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">-ОРО- · -ОЛО- · -ЕРЕ-</p>
    <p><b>Ruscha shakl</b></p>
    <p>го́род · голова́ · здоро́вье · бе́рег · молодо́й</p>
    <p>Maʼnosi <b>aniq</b> va moddiy.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">-РА- · -ЛА- · -РЕ-</p>
    <p><b>Kitobiy shakl</b></p>
    <p>град · глава́ · здра́вствуйте · брег · мла́дший</p>
    <p>Maʼnosi <b>mavhum</b> yoki koʻtarinki.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Kitobiy</th><th>Maʼnolar ajralgani</th></tr>
  <tr><td class="pr-res">голова́</td><td class="pr-end">глава́</td>
      <td class="pr-uz">bosh (tana) / bob, rahbar</td></tr>
  <tr><td class="pr-res">сторона́</td><td class="pr-end">страна́</td>
      <td class="pr-uz">tomon / mamlakat</td></tr>
  <tr><td class="pr-res">коро́ткий</td><td class="pr-end">кра́ткий</td>
      <td class="pr-uz">kalta (uzunlik) / qisqacha (mazmun)</td></tr>
  <tr><td class="pr-res">молодо́й</td><td class="pr-end">мла́дший</td>
      <td class="pr-uz">yosh / kichik (tartib boʻyicha)</td></tr>
  <tr><td class="pr-res">хо́лод</td><td class="pr-end">хладнокро́вный</td>
      <td class="pr-uz">sovuq / sovuqqon, xotirjam</td></tr>
  <tr><td class="pr-res">молоко́</td><td class="pr-end">Мле́чный Путь</td>
      <td class="pr-uz">sut / Somon yoʻli</td></tr>
  <tr><td class="pr-res">по́рох</td><td class="pr-end">прах</td>
      <td class="pr-uz">porox / kul, tuproq (koʻtarinki)</td></tr>
  <tr><td class="pr-res">здоро́вье</td><td class="pr-end">здра́вствуйте</td>
      <td class="pr-uz">sogʻliq / «sogʻ boʻling»</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoidaning oʻzi</span>
<b>-ОРО- / -ОЛО- / -ЕРЕ- koʻrsangiz — bu ruscha shakl, maʼnosi
aniq va moddiy.</b><br>
<b>-РА- / -ЛА- / -РЕ- koʻrsangiz — bu kitobiy shakl, maʼnosi
mavhum yoki koʻtarinki.</b><br><br>
Shuning uchun <em>глава́ кни́ги</em> boʻladi, lekin
<s>голова́ кни́ги</s> boʻlmaydi. Va <em>он уда́рился
<b>голово́й</b></em> boʻladi, <s>уда́рился главо́й</s> esa
kulgili chiqadi.<br><br>
Endi shahar nomlariga qarang: <b>Волгогра́д</b>,
<b>Калинингра́д</b>, <b>Белгра́д</b> — hammasida
<em>-град</em>, chunki nom <b>tantanali</b> boʻlishi kerak.
Kundalik nutqda esa <em>го́род</em>.</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Bitta kalit — oʻnlab soʻz</span>
Bu qoidani bilsangiz, notanish kitobiy soʻzni ham yechasiz:<br><br>
<em>вла́сть</em> ← <em>во́лость</em> (viloyat) — «hokimiyat»<br>
<em>заглавие</em> ← <em>голова</em> — «sarlavha»<br>
<em>прибре́жный</em> ← <em>бе́рег</em> — «qirgʻoqboʻyi»<br>
<em>здравоохране́ние</em> ← <em>здоро́вье</em> — «sogʻliqni saqlash»<br><br>
Yaʼni siz bu soʻzlarni yodlamaysiz — <b>tanib olasiz</b>.</div>

<h3>3. Turkiy qatlam — siz bu soʻzlarni bilasiz</h3>

<p>Endi darsning eng qiziq qismi. Quyidagi soʻzlar ruscha
eshitiladi, lekin ular rus tiliga <b>turkiy tillardan</b> kirgan —
va siz ularni <b>bolaligingizdan</b> bilasiz:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ruscha</th><th>Oʻzbekcha</th><th>Izoh</th></tr>
  <tr class="pr-case__on"><td class="pr-res">каранда́ш</td><td class="pr-end">qora tosh</td>
      <td class="pr-uz">turkiy <em>qora</em> + <em>tosh</em> — qadimgi qalam qora toshdan edi</td></tr>
  <tr class="pr-case__on"><td class="pr-res">изю́м</td><td class="pr-end">uzum</td>
      <td class="pr-uz">turkiy <em>uzum</em>; ruschada maʼnosi torayib «mayiz» boʻlgan</td></tr>
  <tr class="pr-case__on"><td class="pr-res">богаты́рь</td><td class="pr-end">bahodir</td>
      <td class="pr-uz">rus ertaklarining qahramoni turkiy nom bilan yuradi</td></tr>
  <tr><td class="pr-res">де́ньги</td><td class="pr-end">tanga</td>
      <td class="pr-uz">turkiy <em>tanga</em> — pul birligi</td></tr>
  <tr><td class="pr-res">сунду́к</td><td class="pr-end">sandiq</td><td class="pr-uz">deyarli oʻzgarmagan</td></tr>
  <tr><td class="pr-res">чемода́н</td><td class="pr-end">jomadon</td><td class="pr-uz">fors tilidan turkiy orqali</td></tr>
  <tr><td class="pr-res">сара́й</td><td class="pr-end">saroy</td>
      <td class="pr-uz">oʻzbekchada «saroy», ruschada maʼnosi pasayib «omborxona»</td></tr>
  <tr><td class="pr-res">амба́р</td><td class="pr-end">ombor</td><td class="pr-uz">bir xil narsa, bir xil soʻz</td></tr>
  <tr><td class="pr-res">казна́</td><td class="pr-end">xazina</td><td class="pr-uz">davlat xazinasi</td></tr>
  <tr><td class="pr-res">база́р</td><td class="pr-end">bozor</td><td class="pr-uz">fors tilidan turkiy orqali</td></tr>
  <tr><td class="pr-res">арбу́з</td><td class="pr-end">tarvuz</td><td class="pr-uz">turkiy <em>karpuz</em></td></tr>
  <tr><td class="pr-res">утю́г</td><td class="pr-end">—</td><td class="pr-uz">turkiy <em>ütük</em>; oʻzbekcha «dazmol»</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">PR-1 dagi vaʼda — mana isboti</span>
Kursning birinchi darsida sizga aytilgan edi: <b>siz allaqachon
yuzlab ruscha soʻzni bilasiz</b>. Oʻshanda bu shunchaki
dalda boʻlib tuyulgandir.<br><br>
Endi buni oʻz koʻzingiz bilan koʻrdingiz. <em>Каранда́ш</em> —
«qora tosh». <em>Богаты́рь</em> — «bahodir». <em>Изю́м</em> —
«uzum».<br><br>
Rus bolasi bu soʻzlarni <b>yodlaydi</b>. Siz esa ularni
<b>taniysiz</b>. Bu — ingliz yoki fransuz oʻquvchisida
<b>yoʻq</b> imkoniyat, va u faqat sizda bor.<br><br>
Ikkala til ham bir necha asr yonma-yon yashagan. Savdo, sayohat va
qoʻshnichilik soʻzlarni ikki tomonga ham olib oʻtgan.</div>

<h3>4. Yevropa qatlami</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Qayerdan</th><th>Qachon va nega</th><th>Misollar</th></tr>
  <tr><td class="pr-stem">golland, nemis</td><td class="pr-uz">Pyotr I — kema va harbiy ish</td>
      <td class="pr-res">матро́с · ко́мпас · флаг · шторм · штраф</td></tr>
  <tr><td class="pr-stem">fransuz</td><td class="pr-uz">XVIII–XIX asr — saroy va sanʼat</td>
      <td class="pr-res">пальто́ · костю́м · рестора́н · бале́т · бага́ж</td></tr>
  <tr><td class="pr-stem">italyan</td><td class="pr-uz">musiqa</td>
      <td class="pr-res">о́пера · со́ло · пиани́но</td></tr>
  <tr><td class="pr-stem">ingliz</td><td class="pr-uz">XX–XXI asr — sport va texnika</td>
      <td class="pr-res">футбо́л · компью́тер · интерне́т · ме́неджер</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Ikkita qiziq tarix</span>
<b>Вокза́л</b> — Londondagi <em>Vauxhall</em> bogʻining nomidan.
U yerda musiqa yangraydigan zal bor edi; soʻz Rossiyaga kelib
avval «koʻngilochar zal», keyin «temiryoʻl bekati» maʼnosini
olgan.<br><br>
<b>Зо́нтик</b> — golland tilidan (<em>zonnedek</em> — «quyosh
qopqogʻi»). Ruslar soʻz oxiridagi <em>-ик</em> ni kichraytiruvchi
suffiks (PR-88) deb oʻylashgan va undan <b>«katta»</b> shakl —
<em>зонт</em> — ni yasashgan. Aslida bunday soʻz hech qachon
boʻlmagan. Til xatoni <b>qoida</b>ga aylantirgan.</div>

<h3>5. Uslub kelib chiqishga bogʻliq</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Qatlam</th><th>Qayerda ishlatiladi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">slavyan (oʻz)</td><td class="pr-uz">hamma joyda, eng issiq</td>
      <td class="pr-res">дом, мать, хлеб</td></tr>
  <tr><td class="pr-stem">kitobiy (-ра-)</td><td class="pr-uz">rasmiy, tantanali, sheʼr</td>
      <td class="pr-res">глава́, страна́, здравоохране́ние</td></tr>
  <tr><td class="pr-stem">turkiy</td><td class="pr-uz">kundalik — endi butunlay «oʻz»</td>
      <td class="pr-res">каранда́ш, де́ньги, база́р</td></tr>
  <tr><td class="pr-stem">yevropa</td><td class="pr-uz">texnika, sanʼat, yangi soha</td>
      <td class="pr-res">компью́тер, бале́т, ме́неджер</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Kitobiy shaklni oʻrinsiz ishlatmang</span>
Kitobiy shakl <b>har doim</b> ham toʻgʻri kelmaydi:<br><br>
✓ <em>пе́рвая <b>глава́</b> кни́ги</em> — kitobning birinchi bobi<br>
✗ <s>он уда́рился <b>главо́й</b> о дверь</s> — kulgili<br><br>
✓ <em><b>кра́ткое</b> содержа́ние</em> — qisqacha mazmun<br>
✗ <s><b>кра́ткие</b> брю́ки</s> — shim <em>коро́ткие</em> boʻladi<br><br>
Qoida: <b>moddiy narsa — ruscha shakl, mavhum tushuncha —
kitobiy shakl.</b></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>«Глава́» va «голова́» — bir xil soʻz, faqat
     kitobiyroq.</s></p>
  <p class="pe-good">Bir oʻzakdan, lekin <b>maʼnolari ajralgan</b>:
     <em>глава́</em> = bob, rahbar; <em>голова́</em> = bosh.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>«Здра́вствуйте» — shunchaki salom soʻzi, ichida
     maʼno yoʻq.</s></p>
  <p class="pe-good">U <b>«здоро́вье»</b> dan — «sogʻ boʻling» degani.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>«Каранда́ш» — asl ruscha soʻz.</s></p>
  <p class="pe-good">Turkiy: <b>qora</b> + <b>tosh</b>. Xuddi
     <em>изю́м</em>, <em>сунду́к</em>, <em>богаты́рь</em> kabi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Он уда́рился главо́й о дверь.</s></p>
  <p class="pe-good">…уда́рился <b>голово́й</b> — moddiy bosh haqida
     ruscha shakl ishlatiladi.</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>«Здра́вствуйте»</b> qaysi soʻzdan kelib chiqqan va nima
     degani?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>«Здоро́вье»</strong> dan.
    Soʻzma-soʻz — «<b>sogʻ boʻling</b>». <em>Здоро́вье</em> da
    <em>-оро-</em> (ruscha shakl), <em>здра́вствуйте</em> da
    <em>-ра-</em> (kitobiy shakl).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Qaysi biri ruscha shakl, qaysi biri kitobiy? Maʼnolari qanday
     ajralgan?<br>
     <b>сторона́ / страна́</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Сторона́</strong> —
    ruscha (<em>-оро-</em>), maʼnosi aniq: «tomon».
    <strong>Страна́</strong> — kitobiy (<em>-ра-</em>), maʼnosi
    mavhum: «mamlakat». Bitta oʻzak, ikki taqdir.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ruscha soʻzlarning oʻzbekcha «qarindoshini» toping.<br>
     <b>каранда́ш · изю́м · богаты́рь · сунду́к</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>qora tosh · uzum ·
    bahodir · sandiq</strong>. Toʻrttasi ham turkiy qatlamdan.
    Rus bolasi ularni yodlaydi — siz taniysiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Toʻgʻri shaklni tanlang va nega ekanini ayting.<br>
     <b>а) кра́ткое / коро́ткое содержа́ние &nbsp;
     б) кра́ткие / коро́ткие брю́ки</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>а) кра́ткое
    содержа́ние</strong> — mazmun <b>mavhum</b>, demak kitobiy
    shakl.<br><strong>б) коро́ткие брю́ки</strong> — shim
    <b>moddiy</b>, demak ruscha shakl. Qoida shu.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Siz bu soʻzni koʻrmagansiz: <b>здравоохране́ние</b>. Yeching.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><em>здрав-</em> (← здоро́вье) +
    <em>о</em> + <em>охране́ние</em> (← охраня́ть, «qoʻriqlamoq»)
    = <strong>sogʻliqni saqlash</strong>.<br>
    Uchta dars bir joyda ishladi: PR-86 (ikki oʻzak + bogʻlovchi
    unli), PR-87 (<em>-ение</em> suffiksi, ср.р.) va shu dars
    (<em>-ра-</em> kitobiy shakl).</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>происхожде́ние</b><span>kelib chiqish</span></li>
  <li><b>заи́мствование</b><span>oʻzlashma soʻz</span></li>
  <li><b>исто́чник</b><span>manba</span></li>
  <li><b>сла́вянский</b><span>slavyan</span></li>
  <li><b>тю́ркский</b><span>turkiy</span></li>
  <li><b>кни́жный</b><span>kitobiy</span></li>
  <li><b>глава́</b><span>bob; rahbar</span></li>
  <li><b>страна́</b><span>mamlakat</span></li>
  <li><b>кра́ткий</b><span>qisqacha (mavhum)</span></li>
  <li><b>богаты́рь</b><span>bahodir, pahlavon</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Rus tili — <b>toʻrt qatlam</b>: slavyan, turkiy,
        yunon-lotin, yevropa.</li>
    <li><b>Kalit:</b> <b>-оро- / -оло- / -ере-</b> = ruscha shakl,
        maʼnosi <b>aniq</b>; <b>-ра- / -ла- / -ре-</b> = kitobiy
        shakl, maʼnosi <b>mavhum</b>.</li>
    <li><b>Здра́вствуйте = здоро́вье</b> — «sogʻ boʻling».</li>
    <li>Turkiy qatlam sizga <b>bepul</b> berilgan:
        каранда́ш (qora tosh), изю́м (uzum), богаты́рь (bahodir),
        сунду́к (sandiq), сара́й (saroy), казна́ (xazina).</li>
    <li>Yevropa qatlami XVIII asrdan: <b>Pyotr</b> — golland,
        <b>saroy</b> — fransuz, <b>bugun</b> — ingliz.</li>
    <li>Soʻzning <b>kelib chiqishi</b> uning <b>uslubini</b>
        aytadi. Moddiy narsa — ruscha shakl; mavhum tushuncha —
        kitobiy shakl.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-100: Yakuniy dars: 100 darsdan keyin siz qayerdasiz va endi nima qilasiz",
        "category": "russian",
        "order": 100,
        "summary": (
            "Bu darsda yangi grammatika yoʻq. Bu darsda siz oʻzingizni "
            "koʻrasiz: qayerga yetdingiz, nima qololmadingiz va endi nima qilasiz."
        ),
        "stories": ["Сто уроков спустя"],
        "content": """
<h2>PR-100: Yakuniy dars: 100 darsdan keyin siz qayerdasiz va endi nima qilasiz</h2>

<p>PR-1 da sizga birinchi ruscha jumla koʻrsatilgan edi. Oʻshanda u
harflar toʻplami boʻlib tuyulgandi.</p>

<p>Endi shu matnni oʻqing. Toʻxtamang, lugʻat ochmang — shunchaki
oʻqing:</p>

<div class="pe-ex">
  <p class="pe-ex__t">Oʻzingizni tekshiring</p>
  <p class="pe-ex__ru">Челове́к, кото́рый на́чал учи́ть язы́к и не
     бро́сил его́ че́рез ме́сяц, уже́ сде́лал са́мое тру́дное.</p>
  <p class="pe-ex__ru">Прочита́в сто уро́ков, он ви́дит текст не как
     сте́ну, а как доро́гу.</p>
  <p class="pe-ex__ru">Ему́ всё ещё быва́ет тру́дно, одна́ко тепе́рь он
     зна́ет, куда́ смотре́ть: где ко́рень, где паде́ж, где вид
     глаго́ла.</p>
  <p class="pe-ex__ru">Э́то и есть свобо́да — не знать всего́, а
     понима́ть, как устро́ено то, чего́ ты ещё не зна́ешь.</p>
  <p class="pe-ex__uz">Tildan oʻrganishni boshlab, bir oydan keyin
     tashlab qoʻymagan odam eng qiyin ishni allaqachon qilgan.
     Yuzta darsni oʻqib chiqib, u matnni devor emas, yoʻl deb
     koʻradi. Unga hali ham qiyin boʻladi, lekin endi u qayerga
     qarashni biladi: oʻzak qayerda, kelishik qayerda, feʼl turi
     qayerda. Erkinlik — hammasini bilish emas, hali bilmagan
     narsangning qanday qurilganini tushunishdir.</p>
</div>

<p>Agar bu matnni tarjimasiz tushungan boʻlsangiz — kurs oʻz ishini
bajardi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda yangi qoida yoʻq. Bu darsda siz</p>
  <ul>
    <li>Yuqoridagi matn ichida <b>nechta dars</b> yashiringanini koʻrasiz</li>
    <li>Oʻz darajangizni <b>halol</b> baholaysiz</li>
    <li>Nimani hali <b>bilmasligingizni</b> bilib olasiz</li>
    <li><b>Keyingi 100 kun</b> uchun aniq reja olasiz</li>
    <li>Tilni saqlab qoladigan <b>oltita</b> narsani bilasiz</li>
  </ul>
</div>

<h3>1. Oʻsha toʻrt jumlada nima bor edi</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Nima</th><th>Matndan</th><th>Qaysi dars</th></tr>
  <tr><td class="pr-stem">кото́рый ergash gapi</td>
      <td class="pr-res">Челове́к, <b>кото́рый</b> на́чал…</td><td class="pr-uz">PR-63</td></tr>
  <tr><td class="pr-stem">феʼl turi (вид)</td>
      <td class="pr-res">на́чал · <b>сде́лал</b> · не бро́сил</td><td class="pr-uz">PR-51</td></tr>
  <tr><td class="pr-stem">деепричастие</td>
      <td class="pr-res"><b>Прочита́в</b> сто уро́ков…</td><td class="pr-uz">PR-72</td></tr>
  <tr><td class="pr-stem">shaxssiz gap</td>
      <td class="pr-res"><b>Ему́</b> быва́ет тру́дно</td><td class="pr-uz">PR-81</td></tr>
  <tr><td class="pr-stem">одна́ко</td><td class="pr-res">…, <b>одна́ко</b> тепе́рь…</td>
      <td class="pr-uz">PR-67 · PR-97</td></tr>
  <tr><td class="pr-stem">то, чего́</td><td class="pr-res"><b>то, чего́</b> ты не зна́ешь</td>
      <td class="pr-uz">PR-69 · PR-79</td></tr>
  <tr><td class="pr-stem">qisqa majhul shakl</td>
      <td class="pr-res">как <b>устро́ено</b></td><td class="pr-uz">PR-71 · PR-73</td></tr>
  <tr><td class="pr-stem">tire va vergullar</td>
      <td class="pr-res">свобо́да <b>—</b> не знать…</td><td class="pr-uz">PR-97</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Sakkiz dars, toʻrt jumla</span>
Siz bu qoidalarni <b>oʻylab</b> qoʻllamadingiz. Shunchaki
oʻqidingiz.<br><br>
Bu — tilni bilishning asl belgisi. Grammatika esdan chiqqanda
emas, <b>koʻrinmay qolganda</b> ishlay boshlaydi.</div>

<h3>2. Siz qayerdasiz — halol xarita</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Koʻnikma</th><th>Darajangiz</th><th>Nega shunday</th></tr>
  <tr class="pr-case__on"><td class="pr-stem">Oʻqish</td><td class="pr-res">B1–B2</td>
      <td class="pr-uz">Eng kuchli tomoningiz: 92 ta matn oʻqidingiz</td></tr>
  <tr><td class="pr-stem">Yozish</td><td class="pr-res">B1</td>
      <td class="pr-uz">Ariza, xat va insho skeletlari qoʻlingizda (PR-91, PR-98)</td></tr>
  <tr><td class="pr-stem">Tinglash</td><td class="pr-res">A2–B1</td>
      <td class="pr-uz">Kurs audio bermadi — bu sizning zaif tomoningiz</td></tr>
  <tr><td class="pr-stem">Gapirish</td><td class="pr-res">A2–B1</td>
      <td class="pr-uz">Suhbatdosh boʻlmadi; bilim bor, mashq yoʻq</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Nega bu jadval maqtovsiz</span>
Sizga «endi rus tilini bilasiz» deb aytish oson boʻlardi. Lekin bu
<b>notoʻgʻri</b> boʻlardi.<br><br>
Haqiqat shundaki, kurs <b>ikki oyoqni</b> mustahkam qildi (oʻqish
va yozish) va <b>ikkitasini</b> qura olmadi — chunki oʻqish
matnidan tinglash, darslikdan esa suhbat chiqmaydi.<br><br>
Buni bilish — <b>yutuq</b>, chunki endi siz aynan nimani mashq
qilish kerakligini bilasiz. Keyingi reja shu ikki oyoq uchun
tuzilgan.</div>

<h3>3. Siz nima qurdingiz</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Blok</th><th>Nima berdi</th></tr>
  <tr><td class="pr-stem">A · 1–5</td><td class="pr-uz">Kirill alifbosi va yetti soxta doʻst</td></tr>
  <tr><td class="pr-stem">B · 6–18</td><td class="pr-uz">Birinchi gaplar, jins, koʻplik, sifat</td></tr>
  <tr><td class="pr-stem">C · 19–28</td><td class="pr-uz">Feʼl: uch zamon, ikki tuslanish</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">D · 29–50</td>
      <td class="pr-uz">Oltita kelishik — kursning eng katta bloki</td></tr>
  <tr><td class="pr-stem">E · 51–62</td><td class="pr-uz">Feʼl turi, harakat feʼllari, prefikslar</td></tr>
  <tr><td class="pr-stem">F · 63–74</td><td class="pr-uz">Murakkab gap, sifatdosh, ravishdosh</td></tr>
  <tr><td class="pr-stem">G · 75–88</td><td class="pr-uz">Nozik grammatika va soʻz yasalishi</td></tr>
  <tr><td class="pr-stem">H · 89–100</td><td class="pr-uz">Til jonli holda: uslub, hujjat, ibora, matn</td></tr>
</table></div>

<p>Bundan tashqari: <b>100 ta mashq</b> (2000 ga yaqin savol) va
<b>92 ta oʻqish matni</b>. Bularning hammasi joyida turibdi va
istalgan vaqtda qaytib koʻrishingiz mumkin.</p>

<h3>4. Nimani hali bilmaysiz — halol roʻyxat</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Nima</th><th>Izoh</th></tr>
  <tr><td class="pr-stem">Tez ogʻzaki nutq</td>
      <td class="pr-uz">Rus tilida tez gapirilganda soʻzlar qoʻshilib ketadi</td></tr>
  <tr><td class="pr-stem">Ilmiy va yuridik til</td>
      <td class="pr-uz">Alohida leksika, alohida qurilishlar</td></tr>
  <tr><td class="pr-stem">Badiiy adabiyot tili</td>
      <td class="pr-uz">Klassiklar XIX asr rus tilida yozgan</td></tr>
  <tr><td class="pr-stem">Nozik uslubiy tuygʻu</td>
      <td class="pr-uz">Qaysi soʻz qayerda «gʻalati» eshitilishi</td></tr>
  <tr><td class="pr-stem">Katta lugʻat</td>
      <td class="pr-uz">B2 uchun 4000–5000 soʻz kerak; kurs asosini berdi</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bu roʻyxat sizni toʻxtatish uchun emas</span>
Har bir tilda shunday roʻyxat bor va u <b>hech qachon</b>
tugamaydi. Ona tilida ham shunday: oʻzbek tilida ham hamma
soʻzni bilmaysiz.<br><br>
Farq shundaki, ona tilingizda <b>bilmaganingizdan
qoʻrqmaysiz</b> — kontekstdan tushunasiz, soʻrab olasiz, davom
etasiz.<br><br>
Endi rus tilida ham xuddi shunday qila olasiz. <b>Kurs sizga
tilni emas, tilga qarash usulini berdi.</b></div>

<h3>5. Keyingi 100 kun — aniq reja</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Nima</th><th>Qancha</th><th>Nega aynan shu</th></tr>
  <tr class="pr-case__on"><td class="pr-stem">Ovoz chiqarib oʻqish</td>
      <td class="pr-res">kuniga 10 daqiqa</td>
      <td class="pr-uz">Oʻqishni gapirishga ulaydi — eng arzon koʻprik</td></tr>
  <tr class="pr-case__on"><td class="pr-stem">Tinglash</td><td class="pr-res">kuniga 15 daqiqa</td>
      <td class="pr-uz">Eng zaif oyogʻingiz. Subtitrsiz eshiting, keyin subtitr bilan</td></tr>
  <tr><td class="pr-stem">Kundalik</td><td class="pr-res">kuniga 3 gap</td>
      <td class="pr-uz">Uch gap — bu koʻp emas, shuning uchun tashlab qoʻymaysiz</td></tr>
  <tr><td class="pr-stem">Corner matnlari</td><td class="pr-res">haftasiga 1 ta</td>
      <td class="pr-uz">92 tasi joyida turibdi; qaytadan oʻqish yangisidan foydali</td></tr>
  <tr><td class="pr-stem">Suhbat</td><td class="pr-res">haftasiga 1 marta</td>
      <td class="pr-uz">Sherik toping. Bu shartlarning eng qiyini va eng muhimi</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Kundalik nega uch gap?</span>
Chunki <b>uch gap yozmaslik uchun bahona topib boʻlmaydi</b>.<br><br>
Kuniga bir bet yozishga vaʼda bergan odam uchinchi kuni
tashlab qoʻyadi. Uch gap yozgan odam esa <b>yuz kun</b> yozadi va
oxirida uning qoʻlida <b>300 ta jumla</b> boʻladi.<br><br>
<em>Сего́дня бы́ло хо́лодно. Я купи́л хлеб. За́втра у меня́
экза́мен.</em> — mana shu yetadi.</div>

<h3>6. Tilni saqlab qoladigan oltita narsa</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th></th><th>Nima</th><th>Nega</th></tr>
  <tr><td class="pr-stem">1</td><td class="pr-res">Har kuni oz-ozdan</td>
      <td class="pr-uz">Haftada bir marta uch soat — bu ishlamaydi</td></tr>
  <tr><td class="pr-stem">2</td><td class="pr-res">Ovoz chiqarib oʻqing</td>
      <td class="pr-uz">Ogʻiz soʻzni «eslab qoladi», koʻz esa yoʻq</td></tr>
  <tr><td class="pr-stem">3</td><td class="pr-res">Xato qilishdan qoʻrqmang</td>
      <td class="pr-uz">Jim turgan odam xato qilmaydi va oʻrganmaydi ham</td></tr>
  <tr><td class="pr-stem">4</td><td class="pr-res">Soʻz emas, ibora yozing</td>
      <td class="pr-uz"><em>сдать экза́мен</em> — <s>сдать</s> emas (PR-93)</td></tr>
  <tr><td class="pr-stem">5</td><td class="pr-res">Bitta manbani tugating</td>
      <td class="pr-uz">Oʻnta kursni boshlagan odam nolinchi darajada qoladi</td></tr>
  <tr><td class="pr-stem">6</td><td class="pr-res">Til bilan biror ish qiling</td>
      <td class="pr-uz">Til maqsad emas — u vosita. Unda oʻqing, tuzating, tarjima qiling</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Oltinchisi eng muhimi</span>
«Rus tilini oʻrganaman» degan odam bir yildan keyin toʻxtaydi.<br><br>
«Rus tilida <b>kitob oʻqiyman</b>» yoki «rus tilida
<b>hujjat tayyorlayman</b>» degan odam toʻxtamaydi — chunki u
tilni oʻrganmayapti, u <b>ish qilyapti</b>, til esa oʻz-oʻzidan
oʻsib boradi.<br><br>
Endi buning imkoni bor: siz matnni oʻqiy olasiz, xat yoza
olasiz, arizani toʻgʻri toʻldirasiz. <b>Vositani ishga
soling.</b></div>

<h3>Oxirgi mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Darsning boshidagi matnga qayting. Undagi <b>деепричастие</b>
     ni toping va qaysi darsdan ekanini ayting.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Прочита́в</strong> сто
    уро́ков — bu <b>деепричастие</b>, PR-72. U «oʻqib chiqib,
    keyin» degan maʼnoni beradi: avval oʻqidi, keyin koʻra
    boshladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Nega matndagi <b>«одна́ко»</b> dan keyin vergul yoʻq?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Chunki u <b>«lekin»</b> maʼnosida
    kelyapti va gap boʻlagini boshlab turibdi (PR-97). Kirish soʻz
    sifatida gap <b>oʻrtasida</b> turganida ikki tomondan vergul
    olardi: <em>Он, одна́ко, не пришёл.</em></p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bugun kundaligingizga yozadigan uchta jumlani hozir yozing.</p>
  <details class="pe-reveal"><summary>Namuna</summary>
    <div class="pe-reveal__a"><p><strong>Сего́дня я зако́нчил
    со́тый уро́к. Бы́ло тру́дно, но интере́сно. За́втра начну́
    чита́ть кни́гу на ру́сском.</strong><br>
    Uch gap. Oʻtgan zamon, qarshilik bogʻlovchisi, kelasi zamon.
    Ertaga yana uchtasini yozing.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Roʻyxatdagi oltitadan <b>qaysi biri</b> siz uchun eng qiyin
     boʻladi? Uni bugun nomlang.</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Koʻpchilik uchun bu —
    <b>uchinchisi</b> (xato qilishdan qoʻrqmaslik) yoki
    <b>beshinchisi</b> (sherik topish).<br>
    Qaysi biri boʻlsa ham, uni <b>yozib qoʻying</b>. Nomlangan
    qiyinchilik yarim yengilgan qiyinchilikdir.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Oxirgi savol: <b>rus tilida nima qilmoqchisiz?</b> Kitob
     oʻqishmi, ish topishmi, imtihon topshirishmi, kimdir bilan
     gaplashishmi?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Bu savolning <b>toʻgʻri javobi
    yoʻq</b> — lekin javobsiz qoldirmang.<br><br>
    Tilni oʻrganganlar emas, til bilan <b>biror ish
    qilganlar</b> uni saqlab qoladi. Javobingizni bir jumlada
    yozing va koʻrinadigan joyga qoʻying.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>у́ровень</b><span>daraja</span></li>
  <li><b>свобо́дно</b><span>erkin (til haqida)</span></li>
  <li><b>привы́чка</b><span>odat</span></li>
  <li><b>продолжа́ть</b><span>davom ettirmoq</span></li>
  <li><b>ошиба́ться</b><span>xato qilmoq</span></li>
  <li><b>практикова́ться</b><span>mashq qilmoq</span></li>
  <li><b>собесе́дник</b><span>suhbatdosh</span></li>
  <li><b>вслух</b><span>ovoz chiqarib</span></li>
  <li><b>ежедне́вно</b><span>har kuni</span></li>
  <li><b>Ни пу́ха ни пера́!</b><span>Omad! — javobi: К чёрту!</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Yuz darsdan keyin</p>
  <ul>
    <li>Siz <b>oʻqiy olasiz</b>. Bu — kursning asosiy yutugʻi va u
        sizdan hech qayerga ketmaydi.</li>
    <li><b>Tinglash</b> va <b>gapirish</b> — zaif ikki oyoq. Reja
        aynan ular uchun tuzilgan.</li>
    <li>Kuniga <b>10 daqiqa ovoz chiqarib oʻqish</b>, <b>15 daqiqa
        tinglash</b>, <b>3 gap kundalik</b>.</li>
    <li>Soʻz emas, <b>ibora</b> yozing. Bitta manbani <b>tugating</b>.</li>
    <li>Til — maqsad emas, <b>vosita</b>. U bilan biror ish
        qiling.</li>
    <li>Siz eng qiyinini allaqachon qildingiz: <b>boshladingiz va
        tashlab qoʻymadingiz</b>.</li>
    <li><b>Ни пу́ха ни пера́!</b> — endi javobini ham bilasiz.</li>
  </ul>
</div>
""",
    },
]
