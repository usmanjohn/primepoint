# -*- coding: utf-8 -*-
"""Prime Russian — Block G davomi (77–79): olmoshlar tizimi.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

Uchala dars bitta tizimning uch qavati, shuning uchun birga yozilgan:
  PR-77 — HAMMASI:  ка́ждый · все · весь · любо́й · друго́й · остальны́е
  PR-78 — NOANIQ:   кто́-то · кто́-нибудь · ко́е-кто
  PR-79 — INKOR:    никто́ · ничего́ · никогда́
Yaʼni кто soʻzi uch tomonga tarqaladi: кто́-то → никто́ → ка́ждый.
Oxirgi darsda ular bir joyga yigʻiladi.

Har uchala darsning oʻzbekcha tayanchi kuchli, lekin PR-79 niki eng
kuchlisi: OʻZBEKCHADA HAM IKKI INKOR BOR. «Hech kim hech narsa demadi»
= «Никто́ ничего́ не сказа́л» — soʻzma-soʻz. Ingliz tilida esa bu
qatʼiy xato. Shuning uchun bu dars oʻzbek oʻquvchisiga sovgʻa.

Mashqlar:        practice/management/commands/_practice_pr_77_79.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_77_79.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_77_79.py --author=prime
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
        "title": "PR-77: Каждый, все, весь, любой, другой, остальные",
        "category": "russian",
        "order": 77,
        "summary": (
            "«Har kuni» bilan «kun boʻyi» — oʻzbekchada ikki xil, ruschada ham: "
            "ка́ждый день ↔ весь день. Butun dars shu farqlar ustiga qurilgan."
        ),
        "stories": ["Ка́ждое у́тро, весь год"],
        "content": """
<h2>PR-77: Каждый, все, весь, любой, другой, остальные</h2>

<p>Ikki gap: <em>«Я рабо́тал <b>ка́ждый</b> день»</em> va
<em>«Я рабо́тал <b>весь</b> день»</em>. Birinchisi — <b>har kuni</b>,
bir oy davomida. Ikkinchisi — <b>kun boʻyi</b>, ertalabdan
kechgacha. Oʻzbekchada bu ikki narsa boshqa-boshqa aytiladi, ruschada
ham. Shu farqni bir marta oʻrnatib olsangiz, bu darsning yarmi
tayyor.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Ка́ждый</b> (har bir) va <b>весь</b> (butun) ni ajratasiz</li>
    <li>Bir harf farqni koʻrasiz: <b>всё</b> (hamma narsa) ↔ <b>все</b> (hamma odam)</li>
    <li><b>Весь</b> ni turlaysiz</li>
    <li><b>Любо́й</b> (istalgan) va <b>друго́й</b> (boshqa) ni oʻrganasiz</li>
    <li>Foydali juftlikni olasiz: <b>ещё оди́н</b> ↔ <b>друго́й</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Takror</span>
  <span class="pe-chip pe-chip--s">ка́ждый день</span>
  <span class="pe-op">≠</span>
  <span class="pe-chip pe-chip--v">весь день</span>
  <span class="pe-formula__label">Davomiylik</span>
</div>

<h3>1. Ка́ждый ↔ весь — darsning yuragi</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">КА́ЖДЫЙ — har bir, birma-bir</p>
    <p><em>Я хожу́ туда́ <b>ка́ждый</b> день.</em><br>
       U yerga <b>har kuni</b> boraman.</p>
    <p>Takrorlanish. Har doim <b>birlikda</b>.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ВЕСЬ — butun, boshdan-oxir</p>
    <p><em>Я был там <b>весь</b> день.</em><br>
       U yerda <b>kun boʻyi</b> boʻldim.</p>
    <p>Bitta uzluksiz boʻlak.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha — toza moslik</span>
Bu farq oʻzbekchada ham bor va siz uni allaqachon qilasiz:<br><br>
<em><b>har kuni</b></em> &nbsp;→&nbsp; <b>ка́ждый день</b><br>
<em><b>kun boʻyi</b></em>, <em><b>butun kun</b></em> &nbsp;→&nbsp;
<b>весь день</b><br>
<em><b>har yili</b></em> &nbsp;→&nbsp; <b>ка́ждый год</b><br>
<em><b>yil boʻyi</b></em> &nbsp;→&nbsp; <b>весь год</b><br><br>
Yaʼni tarjima qilishda savol bitta: <b>«necha marta?»mi yoki
«qancha vaqt?»mi?</b> Necha marta boʻlsa — <em>ка́ждый</em>.
Qancha vaqt boʻlsa — <em>весь</em>.</div>

<h3>2. Все ↔ всё — bitta harf</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">ВСЕ — hamma (odamlar)</p>
    <p><em><b>Все</b> гото́вы.</em> — Hamma tayyor.</p>
    <p><em><b>Все</b> зна́ют его́.</em> — Hamma uni biladi.</p>
    <p>Koʻplik. Feʼl ham koʻplikda.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ВСЁ — hamma narsa</p>
    <p><em><b>Всё</b> гото́во.</em> — Hammasi tayyor.</p>
    <p><em>Я <b>всё</b> по́нял.</em> — Hammasini tushundim.</p>
    <p>Oʻrta jins, birlik. Feʼl birlikda.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu farq ham bizda bor, faqat biz uni <b>boshqa soʻz</b> bilan
koʻrsatamiz:<br><br>
<em><b>hamma</b> tayyor</em> (odamlar) &nbsp;→&nbsp; <b>все</b> гото́вы<br>
<em><b>hammasi</b> tayyor</em>, <em><b>hamma narsa</b> tayyor</em>
&nbsp;→&nbsp; <b>всё</b> гото́во<br><br>
Ruschada esa farq atigi <b>bitta harfda</b>: <em>е</em> yoki
<em>ё</em>. Yozganda buni albatta koʻrsating, aks holda gap
maʼnosi oʻzgaradi.<br><br>
Tekshirish oson: feʼlga qarang. <em>Все гото́в<b>ы</b></em> —
koʻplik. <em>Всё гото́в<b>о</b></em> — birlik.</div>

<h3>3. Весь — turlanishi</h3>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>Erkak</th><th>Ayol</th><th>Oʻrta</th><th>Koʻplik</th></tr>
  <tr><td class="pr-case__name">И.п.</td><td class="pr-res">весь</td>
      <td class="pr-res">вся</td><td class="pr-res">всё</td><td class="pr-res">все</td></tr>
  <tr><td class="pr-case__name">Р.п.</td><td class="pr-uz">всего́</td>
      <td class="pr-uz">всей</td><td class="pr-uz">всего́</td><td class="pr-uz">всех</td></tr>
  <tr><td class="pr-case__name">Д.п.</td><td class="pr-uz">всему́</td>
      <td class="pr-uz">всей</td><td class="pr-uz">всему́</td><td class="pr-uz">всем</td></tr>
  <tr><td class="pr-case__name">В.п.</td><td class="pr-uz">весь</td>
      <td class="pr-uz">всю</td><td class="pr-uz">всё</td><td class="pr-uz">все / всех</td></tr>
  <tr><td class="pr-case__name">Т.п.</td><td class="pr-uz">всем</td>
      <td class="pr-uz">всей</td><td class="pr-uz">всем</td><td class="pr-uz">все́ми</td></tr>
  <tr><td class="pr-case__name">П.п.</td><td class="pr-uz">обо всём</td>
      <td class="pr-uz">обо всей</td><td class="pr-uz">обо всём</td><td class="pr-uz">обо всех</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__t">Kelishiklarda</p>
  <p class="pe-ex__ru">Он рабо́тал <b>всю</b> ночь. <span class="pr-uz">(В.п., ayol)</span></p>
  <p class="pe-ex__ru">Спаси́бо <b>всем</b>! <span class="pr-uz">(Д.п., koʻplik)</span></p>
  <p class="pe-ex__ru">Мы говори́ли <b>обо всём</b>. <span class="pr-uz">(П.п.)</span></p>
  <p class="pe-ex__uz">U tun boʻyi ishladi. · Hammaga rahmat! · Hamma narsa haqida gaplashdik.</p>
</div>

<h3>4. Любо́й — istalgan</h3>

<p><b>Любо́й</b> «xohlaganingizni oling, farqi yoʻq» degani. Bu
<em>ка́ждый</em> dan boshqa narsa: <em>ка́ждый</em> — hammasi
birma-bir, <em>любо́й</em> — bittasi, qaysi biri boʻlsa ham.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Любо́й</p>
  <p class="pe-ex__ru">Возьми́ <b>любу́ю</b> кни́гу.</p>
  <p class="pe-ex__uz">Istalgan kitobni ol. — Qaysi biri boʻlsa ham.</p>
  <p class="pe-ex__ru">Приходи́ в <b>любо́е</b> вре́мя.</p>
  <p class="pe-ex__uz">Istalgan vaqtda kel.</p>
  <p class="pe-ex__ru"><b>Ка́ждый</b> студе́нт получи́л кни́гу.</p>
  <p class="pe-ex__uz">Har bir talaba kitob oldi. — Hammasi, birma-bir.</p>
</div>

<h3>5. Друго́й va ещё оди́н</h3>

<p>Bu juftlik kundalik hayotda juda koʻp kerak boʻladi va ular
adashtiriladi.</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">ЕЩЁ ОДИ́Н — yana bitta</p>
    <p><em>Да́йте <b>ещё оди́н</b> чай.</em><br>
       Yana bitta choy bering.</p>
    <p><b>Xuddi shunaqasidan</b> yana bitta.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ДРУГО́Й — boshqa</p>
    <p><em>Да́йте <b>друго́й</b> чай.</em><br>
       Boshqa choy bering.</p>
    <p>Bunisi <b>yoqmadi</b> — boshqasini bering.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bir soʻz — ikki tomon</span>
Oʻzbekchada ham aynan shu ikki ibora bor va ular ham
adashtirilmaydi:<br><br>
<em><b>yana bitta</b> choy</em> &nbsp;→&nbsp; <b>ещё оди́н</b> чай<br>
<em><b>boshqa</b> choy</em> &nbsp;→&nbsp; <b>друго́й</b> чай<br><br>
Restoranda buni adashtirish qimmatga tushadi:
<em>«да́йте друго́й чай»</em> deb aytsangiz, ofitsiant
choyingizni <b>olib ketadi</b> va boshqasini keltiradi.</div>

<h3>6. Остальны́е — qolganlar</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Остальны́е</p>
  <p class="pe-ex__ru">Три студе́нта оста́лись, <b>остальны́е</b> ушли́.</p>
  <p class="pe-ex__uz">Uchta talaba qoldi, qolganlari ketdi.</p>
  <p class="pe-ex__ru"><b>Остально́е</b> я расскажу́ за́втра.</p>
  <p class="pe-ex__uz">Qolganini ertaga aytaman.</p>
  <p class="pe-ex__why"><b>Остальны́е</b> — odamlar yoki narsalar
     (koʻplik), <b>остально́е</b> — qolgan qism (oʻrta jins).</p>
</div>

<h3>7. Tayyor iboralar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Ibora</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">всё вре́мя</td><td class="pr-uz">doim, tinmay</td>
      <td class="pr-stem">ка́ждый раз</td><td class="pr-uz">har safar</td></tr>
  <tr><td class="pr-stem">пре́жде всего́</td><td class="pr-uz">avvalo</td>
      <td class="pr-stem">в любо́м слу́чае</td><td class="pr-uz">har holda</td></tr>
  <tr><td class="pr-stem">все вме́сте</td><td class="pr-uz">hammasi birga</td>
      <td class="pr-stem">в друго́й раз</td><td class="pr-uz">boshqa safar</td></tr>
  <tr><td class="pr-stem">всего́ хоро́шего</td><td class="pr-uz">omon boʻling</td>
      <td class="pr-stem">на весь день</td><td class="pr-uz">kun boʻyiga</td></tr>
</table></div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я рабо́тал ка́ждый день с утра́ до ве́чера.</s>
     <em>(bitta kun haqida)</em></p>
  <p class="pe-good">Я рабо́тал <b>весь</b> день — bitta uzluksiz kun</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Все гото́во.</s></p>
  <p class="pe-good"><b>Всё</b> гото́во — «hamma narsa», demak <em>ё</em> va birlik</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Ка́ждые студе́нты пришли́.</s></p>
  <p class="pe-good"><b>Все</b> студе́нты пришли́ — <em>ка́ждый</em> koʻplikda ishlatilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Да́йте друго́й чай.</s> <em>(yana bitta kerak edi)</em></p>
  <p class="pe-good">Да́йте <b>ещё оди́н</b> чай — «boshqa» emas, «yana bitta»</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>Ка́ждый</b> yoki <b>весь</b>? &nbsp; <b>Он чита́л ___ ве́чер
     и лёг спать по́здно.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>весь</strong> — «kechqurun
    boʻyi». Bu bitta uzluksiz oqshom, takror emas. <em>Ка́ждый
    ве́чер</em> «har kechqurun» boʻlardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>Все</b> yoki <b>всё</b>? &nbsp; <b>___ уже́ пришли́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Все</strong>. Feʼl
    <em>пришли́</em> — koʻplikda, demak gap <b>odamlar</b> haqida.
    <em>Всё пришло́</em> deyilsa, «hammasi keldi» degan boshqa
    maʼno chiqardi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Он рабо́тал ___ ночь.</b> (весь)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>всю</strong> —
    Вини́тельный, ayol jinsi (<em>ночь</em>). Vaqt davomiyligi
    В.п. bilan beriladi (PR-49).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Restoranda choy yoqmadi. Nima deysiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Извини́те, принеси́те,
    пожа́луйста, друго́й чай.</strong> «Boshqa» — <em>друго́й</em>.
    <em>Ещё оди́н</em> desangiz, xuddi shunaqasidan yana bitta
    keltiriladi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Har kuni bir xil edi. Yil boʻyi esa — yoʻq.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ка́ждый день был одина́ковым.
    А весь год — нет.</strong> Bitta gapda ikkala soʻz ham:
    <em>ка́ждый</em> takrorni, <em>весь</em> esa butun davrni
    bildiradi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>ка́ждый</b><span>har bir</span></li>
  <li><b>все</b><span>hamma (odamlar)</span></li>
  <li><b>всё</b><span>hamma narsa, hammasi</span></li>
  <li><b>весь / вся / всё</b><span>butun</span></li>
  <li><b>любо́й</b><span>istalgan</span></li>
  <li><b>друго́й</b><span>boshqa</span></li>
  <li><b>ещё оди́н</b><span>yana bitta</span></li>
  <li><b>остальны́е</b><span>qolganlar</span></li>
  <li><b>пре́жде всего́</b><span>avvalo</span></li>
  <li><b>одина́ковый</b><span>bir xil</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Ка́ждый день</b> = har kuni (takror).
        <b>Весь день</b> = kun boʻyi (davomiylik).</li>
    <li><b>Все</b> — hamma odam (koʻplik). <b>Всё</b> — hamma narsa
        (birlik). Feʼlga qarang.</li>
    <li><b>Ка́ждый</b> hech qachon koʻplikda ishlatilmaydi.</li>
    <li><b>Любо́й</b> — istalgani, farqi yoʻq.
        <b>Ка́ждый</b> — hammasi birma-bir.</li>
    <li><b>Ещё оди́н</b> = yana bitta (xuddi shunaqasi).
        <b>Друго́й</b> = boshqa.</li>
    <li><b>Остальны́е</b> — qolganlar, <b>остально́е</b> — qolgan
        qism.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-78: Кто-то / кто-нибудь / кое-кто — noaniq olmoshlar",
        "category": "russian",
        "order": 78,
        "summary": (
            "Uchta zarracha, uchta maʼno: -то (bor, lekin kimligi nomaʼlum), "
            "-нибудь (kim boʻlsa ham, farqi yoʻq), кое- (bilaman, aytmayman)."
        ),
        "stories": ["Кто́-то оста́вил зонт"],
        "content": """
<h2>PR-78: Кто-то / кто-нибудь / кое-кто — noaniq olmoshlar</h2>

<p>Uchta gap: <em>«<b>Кто́-то</b> звони́л»</em>, <em>«<b>Кто́-нибудь</b>
звони́л?»</em>, <em>«<b>Ко́е-кто</b> звони́л»</em>. Uchalasida ham
«kimdir» bor, lekin uchtasi uch xil narsa aytadi: birinchisida odam
<b>bor</b>, lekin kimligi nomaʼlum; ikkinchisida umuman <b>boʻlgan-boʻlmagani</b>
soʻralyapti; uchinchisida soʻzlovchi <b>biladi</b>, lekin aytmayapti.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Uchta zarrachani ajratasiz: <b>-то</b>, <b>-нибудь</b>, <b>ко́е-</b></li>
    <li>Qachon qaysi biri kelishini bitta jadvaldan koʻrasiz</li>
    <li>Butun oilani olasiz: <b>что́-то, где́-то, когда́-то, како́й-то…</b></li>
    <li>Turlanishni oʻrganasiz: <b>кого́-то</b>, lekin <b>ко́е с кем</b></li>
    <li>Defis qoidasini eslab qolasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-chip pe-chip--s">-то</span>
  <span class="pe-formula__label">bor, kimligi nomaʼlum</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">-нибудь</span>
  <span class="pe-formula__label">kim boʻlsa ham</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">ко́е-</span>
  <span class="pe-formula__label">bilaman, aytmayman</span>
</div>

<h3>1. Uchtasi yonma-yon</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Bir feʼl, uch maʼno</p>
  <p class="pe-ex__ru"><b>Кто́-то</b> звони́л, пока́ тебя́ не́ было.</p>
  <p class="pe-ex__uz">Sen yoʻgʻingda kimdir qoʻngʻiroq qildi. — Odam bor, kimligi nomaʼlum.</p>
  <p class="pe-ex__ru"><b>Кто́-нибудь</b> звони́л?</p>
  <p class="pe-ex__uz">Kimdir qoʻngʻiroq qildimi? — Umuman boʻldimi?</p>
  <p class="pe-ex__ru"><b>Ко́е-кто</b> звони́л, но я не скажу́ кто.</p>
  <p class="pe-ex__uz">Bir kishi qoʻngʻiroq qildi, lekin kimligini aytmayman.</p>
</div>

<h3>2. Qachon qaysi biri — asosiy jadval</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Holat</th><th>Zarracha</th><th>Misol</th></tr>
  <tr><td class="pr-uz">Oʻtgan zamon, xabar</td><td class="pr-end">-то</td>
      <td class="pr-res">Вчера́ <b>кто́-то</b> приходи́л.</td></tr>
  <tr><td class="pr-uz">Hozirgi zamon, xabar</td><td class="pr-end">-то</td>
      <td class="pr-res">Он <b>что́-то</b> пи́шет.</td></tr>
  <tr><td class="pr-uz"><b>Savol</b></td><td class="pr-end">-нибудь</td>
      <td class="pr-res"><b>Кто́-нибудь</b> зна́ет отве́т?</td></tr>
  <tr><td class="pr-uz"><b>Buyruq, iltimos</b></td><td class="pr-end">-нибудь</td>
      <td class="pr-res">Расскажи́ <b>что́-нибудь</b>.</td></tr>
  <tr><td class="pr-uz"><b>Kelasi zamon</b></td><td class="pr-end">-нибудь</td>
      <td class="pr-res">Я <b>кому́-нибудь</b> позвоню́.</td></tr>
  <tr><td class="pr-uz"><b>Shart (е́сли)</b></td><td class="pr-end">-нибудь</td>
      <td class="pr-res">Е́сли <b>кто́-нибудь</b> спро́сит, скажи́…</td></tr>
  <tr><td class="pr-uz">Bilaman, aytmayman</td><td class="pr-end">ко́е-</td>
      <td class="pr-res"><b>Ко́е-кто</b> мне рассказа́л.</td></tr>
</table></div>

<div class="pe-call pe-rule"><span class="pe-call__t">Bitta qisqa qoida</span>
Agar gapda voqea <b>allaqachon boʻlgan</b> — <b>-то</b>.<br>
Agar voqea <b>hali boʻlmagan</b> yoki <b>boʻldimi deb soʻralyapti</b> —
<b>-нибудь</b>.<br><br>
Shuning uchun savol, buyruq, kelasi zamon va shart — hammasi
<em>-нибудь</em> oladi.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada ham ikki xil soʻz bor, faqat ular biroz boshqacha
taqsimlangan:<br><br>
<em><b>kimdir</b> qoʻngʻiroq qildi</em> &nbsp;→&nbsp;
<b>кто́-то</b> (odam bor, kimligi nomaʼlum)<br>
<em><b>birorta</b> odam qoʻngʻiroq qildimi?</em> &nbsp;→&nbsp;
<b>кто́-нибудь</b><br>
<em><b>birortasiga</b> qoʻngʻiroq qilaman</em> &nbsp;→&nbsp;
<b>кому́-нибудь</b><br><br>
Yaʼni oʻzbekcha <b>«birorta / biror»</b> ni koʻrsangiz — deyarli
har doim <em>-нибудь</em>. <b>«…dir»</b> ni koʻrsangiz —
<em>-то</em>.</div>

<h3>3. Butun oila</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Savol soʻzi</th><th>-то</th><th>-нибудь</th><th>Maʼnosi</th></tr>
  <tr><td class="pr-stem">кто</td><td class="pr-res">кто́-то</td>
      <td class="pr-end">кто́-нибудь</td><td class="pr-uz">kimdir</td></tr>
  <tr><td class="pr-stem">что</td><td class="pr-res">что́-то</td>
      <td class="pr-end">что́-нибудь</td><td class="pr-uz">nimadir</td></tr>
  <tr><td class="pr-stem">где</td><td class="pr-res">где́-то</td>
      <td class="pr-end">где́-нибудь</td><td class="pr-uz">qayerdadir</td></tr>
  <tr><td class="pr-stem">куда́</td><td class="pr-res">куда́-то</td>
      <td class="pr-end">куда́-нибудь</td><td class="pr-uz">qayergadir</td></tr>
  <tr><td class="pr-stem">когда́</td><td class="pr-res">когда́-то</td>
      <td class="pr-end">когда́-нибудь</td><td class="pr-uz">bir paytlar / qachondir</td></tr>
  <tr><td class="pr-stem">как</td><td class="pr-res">ка́к-то</td>
      <td class="pr-end">ка́к-нибудь</td><td class="pr-uz">qandaydir</td></tr>
  <tr><td class="pr-stem">како́й</td><td class="pr-res">како́й-то</td>
      <td class="pr-end">како́й-нибудь</td><td class="pr-uz">qandaydir (qaysidir)</td></tr>
  <tr><td class="pr-stem">почему́</td><td class="pr-res">почему́-то</td>
      <td class="pr-end">—</td><td class="pr-uz">negadir</td></tr>
</table></div>

<div class="pe-ex">
  <p class="pe-ex__t">Oila ish ustida</p>
  <p class="pe-ex__ru">Я <b>где́-то</b> ви́дел э́то лицо́.</p>
  <p class="pe-ex__uz">Bu yuzni qayerdadir koʻrganman.</p>
  <p class="pe-ex__ru">Пое́дем ле́том <b>куда́-нибудь</b> к мо́рю.</p>
  <p class="pe-ex__uz">Yozda dengiz boʻyiga birortasiga boraylik.</p>
  <p class="pe-ex__ru">Он <b>почему́-то</b> не отвеча́ет.</p>
  <p class="pe-ex__uz">U negadir javob bermayapti.</p>
</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Когда́-то ↔ когда́-нибудь</span>
Bu juftlik <b>vaqtni</b> ikki tomonga ajratadi:<br><br>
<b>Когда́-то</b> — <b>oʻtmishda</b>, «bir paytlar»:
<em>Когда́-то здесь был сад.</em><br>
<b>Когда́-нибудь</b> — <b>kelajakda</b>, «qachondir»:
<em>Когда́-нибудь я туда́ пое́ду.</em></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Butun oila oʻzbekchada ham bor</span>
Bu jadvalni yodlash shart emas — oʻzbekchada aynan shu tizim
ishlaydi. Savol soʻziga <b>«…dir»</b> qoʻshiladi:<br><br>
<em>kim → kim<b>dir</b></em> &nbsp;→&nbsp; кто → кто́-то<br>
<em>nima → nima<b>dir</b></em> &nbsp;→&nbsp; что → что́-то<br>
<em>qayer → qayerda<b>dir</b></em> &nbsp;→&nbsp; где → где́-то<br>
<em>qachon → qachon<b>dir</b></em> &nbsp;→&nbsp; когда́ → когда́-то<br>
<em>nega → nega<b>dir</b></em> &nbsp;→&nbsp; почему́ → почему́-то<br><br>
Yaʼni ruscha <b>-то</b> — oʻzbekcha <b>«-dir»</b> ning aynan oʻzi,
va u ham savol soʻziga yopishadi. Faqat oʻzbekchada
<em>-нибудь</em> uchun alohida qoʻshimcha yoʻq: biz «birorta»,
«biror» degan alohida soʻz ishlatamiz.</div>

<h3>4. Turlanish: asosiy soʻz oʻzgaradi</h3>

<p>Zarracha (<em>-то, -нибудь</em>) <b>hech qachon oʻzgarmaydi</b>.
Turlanadigan narsa — undan oldingi soʻz.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Kelishik</th><th>Shakl</th><th>Misol</th></tr>
  <tr><td class="pr-uz">И.п.</td><td class="pr-res">кто́-то</td>
      <td class="pr-end">Кто́-то пришёл.</td></tr>
  <tr><td class="pr-uz">Р.п.</td><td class="pr-res">кого́-то</td>
      <td class="pr-end">Я кого́-то жду.</td></tr>
  <tr><td class="pr-uz">Д.п.</td><td class="pr-res">кому́-то</td>
      <td class="pr-end">Он кому́-то звони́т.</td></tr>
  <tr><td class="pr-uz">Т.п.</td><td class="pr-res">ке́м-то</td>
      <td class="pr-end">Она́ говори́т с ке́м-то.</td></tr>
  <tr><td class="pr-uz">П.п.</td><td class="pr-res">(о) ко́м-то</td>
      <td class="pr-end">Он ду́мает о ко́м-то.</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ко́е- da predlog ichkariga kiradi</span>
Bu gʻalati, lekin qoida shunday: <b>ко́е-</b> bilan predlog
zarracha va soʻzning <b>orasiga</b> tushadi va hammasi
<b>alohida</b> yoziladi:<br><br>
<em>ко́е-кто</em> &nbsp;→&nbsp; <b>ко́е с кем</b> (kimdir bilan)<br>
<em>ко́е-что</em> &nbsp;→&nbsp; <b>ко́е о чём</b> (nimadir haqida)<br><br>
Solishtiring: <em>-то</em> da esa predlog oldinda qoladi —
<b>с ке́м-то</b>, <b>о ко́м-то</b>.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Ко́е- oʻzbekchada</span>
<b>Ко́е-</b> ga bitta soʻzli tarjima yoʻq, lekin maʼnosi
tanish: bu <em>«bir kishi»</em>, <em>«bir narsa»</em> — soʻzlovchi
biladi, ammo atayin aytmayapti.<br><br>
<em><b>Bir kishi</b> menga aytdi…</em> &nbsp;→&nbsp;
<b>Ко́е-кто</b> мне сказа́л…<br>
<em>Senga <b>bir narsa</b> olib keldim.</em> &nbsp;→&nbsp;
Я тебе́ <b>ко́е-что</b> принёс.<br><br>
Farqni his qiling: <em>кто́-то</em> — men ham bilmayman.
<em>Ко́е-кто</em> — men bilaman, sen bilmaysan.</div>

<h3>5. Defis</h3>

<p><b>-то, -нибудь, ко́е-</b> — uchalasi ham <b>defis bilan</b>
yoziladi: <em>кто́-то</em>, <em>что́-нибудь</em>, <em>ко́е-кто</em>.
Yagona istisno — yuqoridagi predlogli holat.</p>

<h3>6. Nozik joy: takrorlanadigan ish</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Har safar boshqa odam</p>
  <p class="pe-ex__ru">Ка́ждый день <b>кто́-нибудь</b> опа́здывает.</p>
  <p class="pe-ex__uz">Har kuni kimdir kechikadi. — Har kuni <b>boshqa</b> odam.</p>
  <p class="pe-ex__ru">Вчера́ <b>кто́-то</b> опозда́л.</p>
  <p class="pe-ex__uz">Kecha kimdir kechikdi. — Bitta aniq odam, kimligi nomaʼlum.</p>
  <p class="pe-ex__why">Takrorlanadigan ishda odam har safar
     oʻzgargani uchun <b>-нибудь</b> keladi, garchi gap oʻtgan
     zamonda boʻlsa ham.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Кто́-то звони́л?</s> <em>(savol)</em></p>
  <p class="pe-good"><b>Кто́-нибудь</b> звони́л? — savolda <em>-нибудь</em></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Позвони́ кому́-то.</s></p>
  <p class="pe-good">Позвони́ <b>кому́-нибудь</b> — buyruqda <em>-нибудь</em></p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Вчера́ кто́-нибудь приходи́л.</s> <em>(xabar)</em></p>
  <p class="pe-good">Вчера́ <b>кто́-то</b> приходи́л — boʻlib oʻtgan voqea</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я говори́л с кто́-то.</s></p>
  <p class="pe-good">Я говори́л <b>с ке́м-то</b> — asosiy soʻz turlanadi</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>-то</b> yoki <b>-нибудь</b>? &nbsp; <b>У тебя́ есть
     что́-___ почита́ть?</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>что́-нибудь</strong>. Bu
    <b>savol</b>, va nima boʻlishi farqi yoʻq — «biror narsa».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>-то</b> yoki <b>-нибудь</b>? &nbsp; <b>Он ушёл куда́-___ и
     не сказа́л куда́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>куда́-то</strong>. Voqea
    <b>boʻlib oʻtgan</b> — u allaqachon ketdi. Joy aniq bor, faqat
    biz bilmaymiz.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapning farqi nima?<br>
     <b>Когда́-то я жил в Москве́. · Когда́-нибудь я пое́ду в
     Москву́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi — <b>oʻtmish</b>:
    «bir paytlar Moskvada yashaganman». Ikkinchisi —
    <b>kelajak</b>: «qachondir Moskvaga boraman».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Она́ до́лго говори́ла ___
     по телефо́ну.</b> (кто́-то)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>с ке́м-то</strong> —
    Твори́тельный. Predlog <em>-то</em> da <b>oldinda</b> qoladi.
    Agar <em>ко́е-</em> boʻlganda — <em>ко́е с кем</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Agar birortasi soʻrasa, men kutubxonadaman deb ayt.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Е́сли кто́-нибудь спро́сит,
    скажи́, что я в библиоте́ке.</strong> Shart gapida
    <b>-нибудь</b>, chunki hali hech kim soʻragani yoʻq.
    Oʻzbekcha «birortasi» ham shuni koʻrsatib turibdi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>кто́-то</b><span>kimdir (bor, kimligi nomaʼlum)</span></li>
  <li><b>кто́-нибудь</b><span>birortasi, kim boʻlsa ham</span></li>
  <li><b>ко́е-кто</b><span>bir kishi (bilaman, aytmayman)</span></li>
  <li><b>что́-то / что́-нибудь</b><span>nimadir / biror narsa</span></li>
  <li><b>где́-то</b><span>qayerdadir</span></li>
  <li><b>когда́-то</b><span>bir paytlar (oʻtmishda)</span></li>
  <li><b>когда́-нибудь</b><span>qachondir (kelajakda)</span></li>
  <li><b>како́й-то</b><span>qandaydir</span></li>
  <li><b>почему́-то</b><span>negadir</span></li>
  <li><b>опа́здывать</b><span>kechikmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>-то</b> — voqea boʻlgan, odam bor, kimligi nomaʼlum.</li>
    <li><b>-нибудь</b> — savol, buyruq, kelasi zamon, shart. «Kim
        boʻlsa ham».</li>
    <li><b>Ко́е-</b> — bilaman, lekin aytmayman.</li>
    <li>Oʻzbekcha <b>«…dir»</b> → <em>-то</em>, <b>«birorta»</b> →
        <em>-нибудь</em>.</li>
    <li><b>Когда́-то</b> — oʻtmish. <b>Когда́-нибудь</b> — kelajak.</li>
    <li>Turlanadigan narsa — <b>asosiy soʻz</b>: <em>с ке́м-то,
        о ко́м-то</em>. Lekin <em>ко́е-</em> da predlog ichkariga
        kiradi: <b>ко́е с кем</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-79: Никто, ничто, никогда — rus tilida ikki inkor qoidasi",
        "category": "russian",
        "order": 79,
        "summary": (
            "«Hech kim hech narsa demadi» = «Никто́ ничего́ не сказа́л» — soʻzma-soʻz. "
            "Rus tilida ikki inkor MAJBURIY, va oʻzbekchada ham xuddi shunday."
        ),
        "stories": ["Никто́ ничего́ не сказа́л"],
        "content": """
<h2>PR-79: Никто, ничто, никогда — rus tilida ikki inkor qoidasi</h2>

<p>Ingliz tilida oʻqiyotgan odam uchun bu dars — qiynoq. Ular
«hech kim kelmadi» degan gapda <b>bitta</b> inkor qoʻyishga
oʻrgangan. Rus tili esa <b>ikkitasini</b> talab qiladi:
<em>«Никто́ <b>не</b> пришёл»</em>. Va mana bu yerda siz yutasiz —
chunki <b>oʻzbekchada ham aynan shunday</b>: «Hech kim kel<b>ma</b>di».
Ikkita belgi, ikkala tilda ham.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li>Rus tilining bosh qoidasini oʻrnatasiz: <b>ни- + не</b></li>
    <li>Butun oilani olasiz: <b>никто́, ничего́, никогда́, нигде́, никако́й</b></li>
    <li>Predlog soʻzni ikkiga boʻlishini koʻrasiz: <b>ни с кем</b></li>
    <li><b>Ничто́</b> bilan <b>ничего́</b> ni ajratasiz</li>
    <li>Boshqa oilani tanib olasiz: <b>не́чего де́лать</b>, <b>не́кому помо́чь</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Qatʼiy qolip</span>
  <span class="pe-chip pe-chip--neg">ни- soʻzi</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--neg">не</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">feʼl</span>
</div>

<h3>1. Ikki inkor — majburiy</h3>

<div class="pe-ex">
  <p class="pe-ex__t">Ikkala belgi ham turadi</p>
  <p class="pe-ex__ru"><b>Никто́</b> <b>не</b> пришёл.</p>
  <p class="pe-ex__uz"><b>Hech kim</b> kel<b>ma</b>di.</p>
  <p class="pe-ex__ru">Я <b>ничего́</b> <b>не</b> зна́ю.</p>
  <p class="pe-ex__uz">Men <b>hech narsa</b> bil<b>may</b>man.</p>
  <p class="pe-ex__ru">Он <b>никогда́</b> <b>не</b> опа́здывает.</p>
  <p class="pe-ex__uz">U <b>hech qachon</b> kechik<b>may</b>di.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bu dars siz uchun sovgʻa</span>
Oʻzbekchada inkor <b>ikki joyda</b> koʻrsatiladi: <em>hech
kim</em> soʻzida va feʼldagi <em>-ma-</em> qoʻshimchasida.
Ruschada ham xuddi shunday: <em>никто́</em> soʻzida va
<em>не</em> yuklamasida.<br><br>
Yaʼni tarjima qilishda hech narsa oʻylash kerak emas — gapni
oʻzbekcha aytib, <b>ikkala belgini ham</b> ruschaga
koʻchiring:<br><br>
<em><b>Hech qachon</b> u yerga bor<b>ma</b>ganman.</em><br>
→ Я <b>никогда́</b> там <b>не</b> был.<br><br>
Ingliz tilida esa <s>«nobody didn't come»</s> qatʼiy xato. Shuning
uchun ingliz tilidan oʻrganayotgan odam bu darsda uzoq
qiynaladi.</div>

<h3>2. Nechta boʻlsa ham mayli</h3>

<p>Rus tilida inkor soʻzlarni <b>istagancha</b> toʻplash mumkin —
gap notoʻgʻri boʻlmaydi, aksincha kuchayadi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Beshta inkor, bitta gap</p>
  <p class="pe-ex__ru"><b>Никто́</b> <b>никогда́</b> <b>никому́</b>
     <b>ничего́</b> <b>не</b> говори́л.</p>
  <p class="pe-ex__uz">Hech kim hech qachon hech kimga hech narsa aytmagan.</p>
  <p class="pe-ex__why">Oʻzbekchasi ham xuddi shunday uzun. Ikkala
     tilda ham bu gap <b>toʻgʻri</b> va tabiiy.</p>
</div>

<h3>3. Butun oila</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">никто́</td><td class="pr-uz">hech kim</td>
      <td class="pr-res">Никто́ не отве́тил.</td></tr>
  <tr><td class="pr-stem">ничего́</td><td class="pr-uz">hech narsa</td>
      <td class="pr-res">Я ничего́ не ви́жу.</td></tr>
  <tr><td class="pr-stem">никогда́</td><td class="pr-uz">hech qachon</td>
      <td class="pr-res">Он никогда́ не спо́рит.</td></tr>
  <tr><td class="pr-stem">нигде́</td><td class="pr-uz">hech qayerda</td>
      <td class="pr-res">Я нигде́ его́ не нашёл.</td></tr>
  <tr><td class="pr-stem">никуда́</td><td class="pr-uz">hech qayerga</td>
      <td class="pr-res">Мы никуда́ не пошли́.</td></tr>
  <tr><td class="pr-stem">никако́й</td><td class="pr-uz">hech qanday</td>
      <td class="pr-res">Никако́й пробле́мы нет.</td></tr>
  <tr><td class="pr-stem">ниче́й</td><td class="pr-uz">hech kimniki</td>
      <td class="pr-res">Э́та су́мка ниче́й.</td></tr>
  <tr><td class="pr-stem">ника́к</td><td class="pr-uz">hech qanday yoʻl bilan</td>
      <td class="pr-res">У меня́ ника́к не получа́ется.</td></tr>
</table></div>

<h3>4. Turlanish va predlog</h3>

<div class="pe-table-wrap"><table class="pr-case">
  <tr><th>Kelishik</th><th>никто́</th><th>ничто́</th><th>Predlog bilan</th></tr>
  <tr><td class="pr-case__name">И.п.</td><td class="pr-res">никто́</td>
      <td class="pr-res">ничто́</td><td class="pr-uz">—</td></tr>
  <tr><td class="pr-case__name">Р.п.</td><td class="pr-res">никого́</td>
      <td class="pr-res">ничего́</td><td class="pr-uz">ни у кого́</td></tr>
  <tr><td class="pr-case__name">Д.п.</td><td class="pr-res">никому́</td>
      <td class="pr-res">ничему́</td><td class="pr-uz">ни к кому́</td></tr>
  <tr><td class="pr-case__name">В.п.</td><td class="pr-res">никого́</td>
      <td class="pr-res">ничего́</td><td class="pr-uz">ни на что</td></tr>
  <tr><td class="pr-case__name">Т.п.</td><td class="pr-res">нике́м</td>
      <td class="pr-res">ниче́м</td><td class="pr-uz">ни с кем</td></tr>
  <tr><td class="pr-case__name">П.п.</td><td class="pr-res">—</td>
      <td class="pr-res">—</td><td class="pr-uz">ни о ком · ни о чём</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Predlog soʻzni ikkiga boʻladi</span>
Bu darsning eng koʻp xato qilinadigan joyi. Predlog
<b>ни</b> bilan asosiy soʻz <b>orasiga</b> tushadi va uchalasi
ham <b>alohida</b> yoziladi:<br><br>
<s>никем</s> + с &nbsp;→&nbsp; <b>ни с кем</b><br>
<s>ником</s> + о &nbsp;→&nbsp; <b>ни о ком</b><br>
<s>никого</s> + у &nbsp;→&nbsp; <b>ни у кого́</b><br><br>
<em>Я <b>ни с кем</b> не говори́л.</em> — Hech kim bilan
gaplashmadim.</div>

<h3>5. Ничто́ yoki ничего́?</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">НИЧТО́ — И.п., kam uchraydi</p>
    <p><em><b>Ничто́</b> не ве́чно.</em><br>Hech narsa abadiy emas.</p>
    <p>Kitobiy. Gapning <b>egasi</b> boʻlganda.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">НИЧЕГО́ — 95% holat</p>
    <p><em>Я <b>ничего́</b> не по́нял.</em><br>Hech narsa tushunmadim.</p>
    <p>Toʻldiruvchi boʻlganda. Kundalik nutqda shu.</p>
  </div>
</div>

<h3>6. Boshqa oila: не́чего, не́кого</h3>

<p>Diqqat: <b>ни-</b> (urgʻusiz) va <b>не́-</b> (urgʻuli) — ikki
boshqa narsa. Birinchisi <b>inkor</b> qiladi, ikkinchisi
<b>imkoniyat yoʻqligini</b> bildiradi va <b>infinitiv</b> bilan
keladi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ni- (inkor)</th><th>Ne- (imkoniyat yoʻq)</th></tr>
  <tr><td class="pr-res">Я ничего́ не де́лаю. <span class="pr-uz">— hech narsa qilmayapman</span></td>
      <td class="pr-end">Мне не́чего де́лать. <span class="pr-uz">— qiladigan ishim yoʻq</span></td></tr>
  <tr><td class="pr-res">Никто́ не помо́г. <span class="pr-uz">— hech kim yordam bermadi</span></td>
      <td class="pr-end">Не́кому помо́чь. <span class="pr-uz">— yordam beradigan odam yoʻq</span></td></tr>
  <tr><td class="pr-res">Я никуда́ не иду́. <span class="pr-uz">— hech qayerga bormayapman</span></td>
      <td class="pr-end">Мне не́куда идти́. <span class="pr-uz">— boradigan joyim yoʻq</span></td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Ikki oilani qanday ajratish</span>
Oʻzbekcha tarjimaga qarang — u darrov aytib beradi:<br><br>
<em>hech narsa qil<b>ma</b>yapman</em> (feʼl inkorda) &nbsp;→&nbsp;
<b>ни-</b> + <b>не</b><br>
<em>qiladigan ish<b>im yoʻq</b></em> (feʼl inkorda emas, «yoʻq»
bor) &nbsp;→&nbsp; <b>не́-</b> + infinitiv<br><br>
Ikkinchi qurilishda odam <b>Да́тельный</b> da turadi:
<em><b>мне</b> не́чего де́лать</em>, <em><b>ему́</b> не́куда
идти́</em>.<br><br>
Urgʻuni ham eslang: <em>ни</em> hech qachon urgʻu olmaydi,
<em>не́</em> esa <b>har doim</b> oladi.</div>

<div class="pe-ex">
  <p class="pe-ex__t">Ikki oila yonma-yon</p>
  <p class="pe-ex__ru">Он <b>никому́</b> <b>не</b> позвони́л.</p>
  <p class="pe-ex__uz">U hech kimga qoʻngʻiroq qilmadi. — Qila olardi, qilmadi.</p>
  <p class="pe-ex__ru">Ему́ <b>не́кому</b> позвони́ть.</p>
  <p class="pe-ex__uz">Unda qoʻngʻiroq qiladigan odam yoʻq. — Imkoniyat yoʻq.</p>
  <p class="pe-ex__why">Bir harf farq — <em>ни</em> yoki <em>не́</em> —
     va gap butunlay boshqa narsa aytadi.</p>
</div>

<h3>7. Tayyor iboralar</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ibora</th><th>Maʼnosi</th><th>Qachon aytiladi</th></tr>
  <tr><td class="pr-stem">Ничего́!</td><td class="pr-uz">Hechqisi yoʻq!</td>
      <td class="pr-res">Kimdir uzr soʻraganda</td></tr>
  <tr><td class="pr-stem">Ничего́ стра́шного.</td><td class="pr-uz">Qoʻrqinchli joyi yoʻq.</td>
      <td class="pr-res">Xato boʻlganda tinchlantirish</td></tr>
  <tr><td class="pr-stem">Ничего́ осо́бенного.</td><td class="pr-uz">Alohida hech narsa.</td>
      <td class="pr-res">«Nima gap?» degan savolga</td></tr>
  <tr><td class="pr-stem">Ни за что!</td><td class="pr-uz">Aslo!</td>
      <td class="pr-res">Qatʼiy rad javob</td></tr>
  <tr><td class="pr-stem">Ничего́ подо́бного.</td><td class="pr-uz">Bunday narsa yoʻq.</td>
      <td class="pr-res">Eʼtiroz bildirganda</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Nega bu qoida bizga tabiiy</span>
Koʻp tillarda inkor <b>bir marta</b> aytiladi. Rus tili va oʻzbek
tili esa uni <b>ikki marta</b> aytadi — va bu tasodif emas: har
ikkala tilda ham inkor soʻzning oʻzi «hech» degan boʻshliqni
ochadi, feʼl esa uni yopadi.<br><br>
Shuning uchun qoidani <b>yodlash shart emas</b>. Gapni oʻzbekcha
ayting va ikkala belgini sanang:<br><br>
<em><b>Hech</b> qayerda uni topol<b>ma</b>dim.</em> — ikkita belgi<br>
→ Я <b>нигде́</b> его́ <b>не</b> нашёл. — ikkita belgi<br><br>
Agar ruschada bittasi tushib qolsa, gap darrov gʻalati
eshitiladi — xuddi oʻzbekchada <s>«hech kim keldi»</s> deyilgandek.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Никто́ пришёл.</s></p>
  <p class="pe-good">Никто́ <b>не</b> пришёл — <em>не</em> tashlab ketilmaydi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я ничего́ зна́ю.</s></p>
  <p class="pe-good">Я ничего́ <b>не</b> зна́ю — ikki inkor majburiy</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я говори́л никем.</s></p>
  <p class="pe-good">Я <b>ни с кем</b> не говори́л — predlog soʻzni ikkiga boʻladi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я не́чего не де́лаю.</s></p>
  <p class="pe-good">Я <b>ничего́</b> не де́лаю — inkor uchun <em>ни-</em>, urgʻusiz</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Xatoni tuzating. &nbsp; <b>Никто́ зна́ет отве́т.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Никто́ не зна́ет
    отве́т.</strong> <em>Ни-</em> soʻzi bor joyda feʼl oldida
    <b>не</b> ham turishi shart. Oʻzbekchada ham «hech kim
    bil<b>may</b>di».</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Toʻgʻri yozing. &nbsp; <b>Я … не говори́л об э́том.</b>
     (никто́ + с)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>ни с кем</strong> — uchta
    alohida soʻz. Predlog <em>ни</em> bilan <em>кем</em>
    orasiga tushadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapning farqi nima?<br>
     <b>Я ничего́ не де́лаю. · Мне не́чего де́лать.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisi: «hech narsa
    qilmayapman» — <b>xohlamayman yoki qilmayapman</b>.
    Ikkinchisi: «qiladigan ishim yoʻq» — <b>ish yoʻq</b>. Ikkinchi
    qurilishda odam Да́тельный da turadi va feʼl
    infinitivda.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Hech kim hech qachon hech narsa soʻramadi.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Никто́ никогда́ ничего́ не
    спроси́л.</strong> Uchta inkor soʻzi va bitta <em>не</em> —
    hammasi bir gapda, va bu <b>toʻgʻri</b>. Oʻzbekchasi ham
    xuddi shunday uzun.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Kimdir sizning oyogʻingizni bosib oldi va uzr soʻradi. Nima
     deysiz?</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ничего́!</strong> yoki
    <strong>Ничего́ стра́шного.</strong> — «Hechqisi yoʻq». Bu
    rus tilidagi eng koʻp eshitiladigan javoblardan
    biri.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>никто́</b><span>hech kim</span></li>
  <li><b>ничего́</b><span>hech narsa</span></li>
  <li><b>никогда́</b><span>hech qachon</span></li>
  <li><b>нигде́ / никуда́</b><span>hech qayerda / hech qayerga</span></li>
  <li><b>никако́й</b><span>hech qanday</span></li>
  <li><b>ни с кем</b><span>hech kim bilan</span></li>
  <li><b>не́чего де́лать</b><span>qiladigan ish yoʻq</span></li>
  <li><b>не́куда идти́</b><span>boradigan joy yoʻq</span></li>
  <li><b>Ничего́ стра́шного</b><span>hechqisi yoʻq</span></li>
  <li><b>Ни за что!</b><span>Aslo!</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Ни- soʻzi bor joyda feʼl oldida «не» turishi
        SHART.</b></li>
    <li>Bu oʻzbekcha bilan bir xil: «hech kim kel<b>ma</b>di» =
        «никто́ <b>не</b> пришёл».</li>
    <li>Inkor soʻzlar <b>istagancha</b> toʻplanishi mumkin —
        gap toʻgʻri boʻlaveradi.</li>
    <li>Predlog soʻzni <b>ikkiga boʻladi</b>: <em>ни с кем</em>,
        <em>ни о чём</em> — uchta alohida soʻz.</li>
    <li><b>Ничего́</b> — kundalik shakl. <b>Ничто́</b> — faqat ega
        boʻlganda, kitobiy.</li>
    <li><b>Не́чего / не́кому</b> (urgʻuli) — inkor emas,
        <b>imkoniyat yoʻqligi</b>, infinitiv bilan.</li>
  </ul>
</div>
""",
    },
]
