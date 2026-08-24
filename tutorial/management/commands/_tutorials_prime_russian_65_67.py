# -*- coding: utf-8 -*-
"""Prime Russian — Block F davomi (65–67): ergash gaplar.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md
Lesson list: tutorial/management/commands/toc_prime_russian.txt

PR-65 — если va когда. Darsning yuragi bitta tuzoq: rus tilida kelasi zamon
haqida gapirilsa, ergash gapda HAM kelasi zamon turadi. Oʻzbekchada esa
«borsam» zamonsiz — shuning uchun oʻquvchi «Если я в Ташкенте» deb yozadi.
PR-66 — sabab va natija. Asosiy gʻoya: потому́ что va поэ́тому bir voqeani
ikki tomondan aytadi (oyna). Ustiga из-за + Р.п. / благодаря́ + Д.п.
PR-67 — qarama-qarshilik. Eng katta lever: oʻzbekcha «esa» = ruscha А,
«lekin» = ruscha НО. Plus зато́ — oʻzbekchada bitta soʻz bilan tarjimasi yoʻq.

Mashqlar:        practice/management/commands/_practice_pr_65_67.py
Oʻqish matnlari: corner/management/commands/_stories_prime_russian_65_67.py
⛔ AUDIO YOʻQ — 2026-08-09 dagi qaror.

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_russian_65_67.py --author=prime
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
        "title": "PR-65: Если va когда — shart va vaqt ergash gaplari",
        "category": "russian",
        "order": 65,
        "summary": (
            "Когда́ — aniq boʻladigan narsa, е́сли — boʻlishi mumkin narsa. Va rus "
            "tilining eng katta tuzogʻi: kelasi zamonda ikkala qismda ham kelasi zamon."
        ),
        "stories": ["Когда́ отключи́ли свет"],
        "content": """
<h2>PR-65: Если va когда — shart va vaqt ergash gaplari</h2>

<p>Ikki gapga qarang: <em>«<b>Когда́</b> он придёт, мы начнём»</em> va
<em>«<b>Е́сли</b> он придёт, мы начнём»</em>. Bitta soʻz farq qiladi.
Lekin birinchisida siz uni <b>kutyapsiz</b> — u albatta keladi. Ikkinchisida
esa kelishiga <b>ishonchingiz yoʻq</b>. Rus tilida bu farq har doim
eshitiladi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Когда́</b> (vaqt) bilan <b>е́сли</b> (shart) ni ajratasiz</li>
    <li>Rus tilining eng katta tuzogʻini yengasiz: <b>kelasi zamon ikkala qismda ham</b></li>
    <li>Feʼl turi <em>когда́</em> ning maʼnosini qanday oʻzgartirishini koʻrasiz</li>
    <li><b>Как то́лько, пока́, по́сле того́ как</b> — vaqtning boshqa bogʻlovchilarini olasiz</li>
    <li>Vergulni toʻgʻri joyga qoʻyasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ergash gap oldinda</span>
  <span class="pe-chip pe-chip--s">Когда́ / Е́сли + gap</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">asosiy gap</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Ergash gap keyinda</span>
  <span class="pe-chip pe-chip--v">asosiy gap</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--s">когда́ / е́сли + gap</span>
</div>

<h3>1. Когда́ yoki е́сли? — ishonch darajasi</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">КОГДА́ — vaqt</p>
    <p><em>Когда́ он придёт, мы начнём.</em><br>
       U kel<b>ganda</b> boshlaymiz.</p>
    <p>U <b>keladi</b> — bu aniq. Faqat qachonligi nomaʼlum.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Е́СЛИ — shart</p>
    <p><em>Е́сли он придёт, мы начнём.</em><br>
       <b>Agar</b> u kelsa, boshlaymiz.</p>
    <p>U kelmasligi <b>ham</b> mumkin. Bu — shart.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada bu farq qoʻshimchada turadi:<br><br>
<em>kel<b>ganda</b></em> — vaqt &nbsp;→&nbsp; <b>когда́</b><br>
<em>kel<b>sa</b></em> (yoki <em>agar</em> bilan) — shart &nbsp;→&nbsp; <b>е́сли</b><br><br>
Yaʼni oʻzbek oʻquvchisi bu ikkisini <b>allaqachon</b> ajratadi. Faqat
ruschada farq feʼlda emas, <b>bogʻlovchida</b> koʻrsatiladi.</div>

<h3>2. Eng katta tuzoq: kelasi zamon ikkala qismda ham</h3>

<p>Bu darsning asosiy qismi shu. Oʻzbekchada <em>«bor<b>sam</b>»</em> —
zamoni yoʻq shakl. Ruschada esa <b>zamon aytilishi shart</b>: gap kelajak
haqida boʻlsa, <em>е́сли</em> yoki <em>когда́</em> dan keyin ham
<b>kelasi zamon</b> turadi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Oʻzbekcha</th><th>Ruscha</th><th>Diqqat</th></tr>
  <tr><td class="pr-uz">Ertaga yomgʻir yogʻ<b>sa</b>, uyda qolaman.</td>
      <td class="pr-res">Е́сли за́втра <b>бу́дет</b> дождь, я <b>оста́нусь</b> до́ма.</td>
      <td class="pr-end">бу́дет — kelasi zamon</td></tr>
  <tr><td class="pr-uz">Toshkentga bor<b>sam</b>, senga qoʻngʻiroq qilaman.</td>
      <td class="pr-res">Е́сли я <b>бу́ду</b> в Ташке́нте, я тебе́ <b>позвоню́</b>.</td>
      <td class="pr-end">бу́ду — kelasi zamon</td></tr>
  <tr><td class="pr-uz">Uyga bor<b>ganimda</b>, senga qoʻngʻiroq qilaman.</td>
      <td class="pr-res">Когда́ я <b>приду́</b> домо́й, я тебе́ <b>позвоню́</b>.</td>
      <td class="pr-end">приду́ — kelasi zamon</td></tr>
  <tr><td class="pr-uz">Vaqt boʻl<b>sa</b>, kelaman.</td>
      <td class="pr-res">Е́сли <b>бу́дет</b> вре́мя, я <b>приду́</b>.</td>
      <td class="pr-end">ikkala feʼl ham kelajakda</td></tr>
</table></div>

<div class="pe-call pe-warn"><span class="pe-call__t">Diqqat</span>
Bu yerda rus tili <b>ingliz tilidan ham</b>, oʻzbek tilidan ham farq
qiladi. Ruschada mantiq juda oddiy: <b>voqea kelajakda boʻlsa — feʼl
kelasi zamonda</b>. Istisno yoʻq.<br><br>
<s>Е́сли за́втра идёт дождь…</s> &nbsp;→&nbsp; <b>Е́сли за́втра
бу́дет дождь…</b></div>

<h3>3. Когда́ va feʼl turi — bir soʻz, ikki manzara</h3>

<p><em>Когда́</em> dan keyin qaysi <b>turdagi (вид)</b> feʼl turgani
gapning maʼnosini butunlay oʻzgartiradi.</p>

<div class="pr-aspect">
  <div class="pr-aspect__side">
    <p class="pr-aspect__h">НСВ — bir vaqtda yoki takror</p>
    <p class="pr-aspect__v">Когда́ я <b>чита́ю</b>…</p>
    <p><em>Когда́ я чита́ю, я не слу́шаю му́зыку.</em><br>
       Oʻqiyotganimda musiqa eshitmayman. — Har safar, bir vaqtning oʻzida.</p>
  </div>
  <div class="pr-aspect__side pr-aspect__side--sv">
    <p class="pr-aspect__h">СВ — avval bu, keyin u</p>
    <p class="pr-aspect__v">Когда́ я <b>прочита́л</b>…</p>
    <p><em>Когда́ я прочита́л письмо́, я всё по́нял.</em><br>
       Xatni oʻqib boʻlgach, hammasini tushundim. — Ketma-ketlik.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">Yonma-yon</p>
  <p class="pe-ex__ru">Когда́ Дилно́за <b>гото́вила</b> у́жин, Жасу́р накрыва́л на стол.</p>
  <p class="pe-ex__uz">Dilnoza kechki ovqat tayyorlayotganda, Jasur dasturxon yozardi.</p>
  <p class="pe-ex__why">НСВ — ikkala ish <b>bir vaqtda</b> ketyapti.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">Yonma-yon</p>
  <p class="pe-ex__ru">Когда́ Дилно́за <b>пригото́вила</b> у́жин, все се́ли за стол.</p>
  <p class="pe-ex__uz">Dilnoza kechki ovqatni tayyorlab boʻlgach, hamma dasturxonga oʻtirdi.</p>
  <p class="pe-ex__why">СВ — avval ovqat tayyor boʻldi, <b>keyin</b> oʻtirishdi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Bu farq oʻzbekchada ham bor, faqat u <b>feʼlning oʻzida</b> koʻrsatiladi:<br><br>
<em>oʻqi<b>yotganimda</b></em> — davom etyapti &nbsp;→&nbsp; <b>когда́ + НСВ</b><br>
<em>oʻqi<b>b boʻlgach</b></em>, <em>oʻqi<b>gandan keyin</b></em> — tugadi
&nbsp;→&nbsp; <b>когда́ + СВ</b><br><br>
Yaʼni siz bu maʼnolarni allaqachon ajratasiz. Ruschada esa
<em>когда́</em> soʻzi <b>oʻzgarmaydi</b> — butun ish feʼl turiga
tushadi. Shuning uchun <em>когда́</em> li gap yozayotganda birinchi
savol har doim bitta: <b>«bu ish tugadimi yoki davom etyaptimi?»</b></div>

<h3>4. Е́сли ↔ е́сли бы — real va noreal</h3>

<p>PR-60 da <em>бы</em> ni oʻrgangansiz. Ikkalasini bir joyga qoʻyamiz,
chunki oʻquvchilar aynan shu yerda adashadi.</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">Е́СЛИ — boʻlishi mumkin</p>
    <p><em>Е́сли у меня́ <b>бу́дет</b> вре́мя, я <b>приду́</b>.</em><br>
       Vaqtim boʻlsa, kelaman.</p>
    <p>Hali hech narsa hal boʻlmagan. <b>Бы yoʻq.</b></p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">Е́СЛИ БЫ — boʻlmadi / boʻlmaydi</p>
    <p><em>Е́сли бы у меня́ <b>бы́ло</b> вре́мя, я <b>бы пришёл</b>.</em><br>
       Vaqtim boʻlganda edi, kelardim.</p>
    <p>Vaqt yoʻq. <b>Ikkala qismda ham бы + oʻtgan zamon.</b></p>
  </div>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Qoida</span>
<b>Бы</b> real shart bilan hech qachon uchrashmaydi. Gapda
<em>бу́дет</em> bor boʻlsa — <em>бы</em> yoʻq. Gapda <em>бы</em> bor
boʻlsa — ikkala feʼl ham <b>oʻtgan zamon</b> shaklida.</div>

<h3>5. Vaqtning boshqa bogʻlovchilari</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Bogʻlovchi</th><th>Maʼnosi</th><th>Misol</th></tr>
  <tr><td class="pr-stem">как то́лько</td><td class="pr-uz">…ishi bilanoq</td>
      <td class="pr-res">Как то́лько он придёт, мы начнём.</td></tr>
  <tr><td class="pr-stem">пока́</td><td class="pr-uz">…ayotgan payt, …ekan</td>
      <td class="pr-res">Пока́ ты гото́вишь, я накро́ю на стол.</td></tr>
  <tr><td class="pr-stem">пока́ не</td><td class="pr-uz">…gunicha</td>
      <td class="pr-res">Жди здесь, пока́ я не верну́сь.</td></tr>
  <tr><td class="pr-stem">по́сле того́ как</td><td class="pr-uz">…gandan keyin</td>
      <td class="pr-res">По́сле того́ как он ушёл, ста́ло ти́хо.</td></tr>
  <tr><td class="pr-stem">пе́ред тем как</td><td class="pr-uz">…dan oldin</td>
      <td class="pr-res">Пе́ред тем как вы́йти, вы́ключи свет.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Пока́ не — inkor emas</span>
<em>Жди, пока́ я <b>не</b> верну́сь</em> — «qaytmagunimcha kut».
Bu yerdagi <b>не</b> inkor emas, u shunchaki shu qurilishning bir
qismi. Oʻzbekchada ham xuddi shunday: «qayt<b>ma</b>gunimcha» —
ichida <em>-ma-</em> bor, lekin gap inkor emas.</div>

<h3>6. Vergul va «то»</h3>

<p>Ergash gap bilan asosiy gap orasida <b>har doim vergul</b> boʻladi —
qaysi biri oldinda turishidan qatʼi nazar.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Vergul</p>
  <p class="pe-ex__ru">Е́сли за́втра бу́дет дождь<b>,</b> <b>то</b> мы оста́немся до́ма.</p>
  <p class="pe-ex__uz">Agar ertaga yomgʻir yogʻsa, u holda uyda qolamiz.</p>
  <p class="pe-ex__why"><b>То</b> — ixtiyoriy. U faqat ergash gap
     <b>oldinda</b> turganda qoʻyiladi va gapni ikkiga aniq ajratadi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
<b>То</b> — oʻzbekchadagi <em>«u holda»</em>, <em>«unda»</em> ning
aynan oʻzi:<br><br>
<em>Agar yomgʻir yogʻsa, <b>u holda</b> uyda qolamiz.</em><br>
→ Е́сли бу́дет дождь, <b>то</b> мы оста́немся до́ма.<br><br>
Oʻzbekchada ham, ruschada ham u <b>majburiy emas</b> — gapni aniqroq
boʻlaklarga ajratish uchun qoʻyiladi. Uzun gaplarda foydali.</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Раз — «madomiki»</span>
Ogʻzaki tilda <em>е́сли</em> ning bir qarindoshi bor: <b>раз</b>.
U «shundoq ekan, madomiki» degani — shart emas, allaqachon maʼlum
fakt:<br><br>
<em>Раз ты здесь, помоги́ мне.</em> — Kelibsanmi, yordam ber.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Е́сли за́втра идёт дождь, я оста́нусь до́ма.</s></p>
  <p class="pe-good">Е́сли за́втра <b>бу́дет</b> дождь — kelajak haqida, demak kelasi zamon</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Когда́ я приду́ домо́й, я звоню́ тебе́.</s></p>
  <p class="pe-good">…я <b>позвоню́</b> тебе́ — asosiy gap ham kelajakda</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Е́сли бы за́втра бу́дет вре́мя, я приду́.</s></p>
  <p class="pe-good">Е́сли за́втра <b>бу́дет</b> вре́мя, я приду́ — real shart, <b>бы</b> keraksiz</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Когда́ он пришёл мы уже́ у́жинали.</s></p>
  <p class="pe-good">Когда́ он пришёл<b>,</b> мы уже́ у́жинали — vergul majburiy</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>Е́сли</b> yoki <b>когда́</b>? &nbsp; <b>___ мне бу́дет 18 лет,
     я полу́чу па́спорт.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Когда́</strong>. 18 yosh
    albatta toʻladi — bu shart emas, <b>vaqt</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Е́сли ты ___ мне за́втра,
     я всё объясню́.</b> (позвони́ть)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>позвони́шь</strong> — kelasi
    zamon. Oʻzbekcha «qoʻngʻiroq qil<b>sang</b>» zamonsiz, ruschada esa
    zamon aytilishi shart.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Bu ikki gapning farqi nima?<br>
     <b>Когда́ я чита́л письмо́, вошла́ ма́ма. · Когда́ я прочита́л
     письмо́, вошла́ ма́ма.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Birinchisida (<b>НСВ</b>) men xatni
    <b>oʻqiyotgan paytimda</b> oyim kirdi — xat tugamagan. Ikkinchisida
    (<b>СВ</b>) xatni <b>oʻqib boʻldim</b>, keyin oyim kirdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Xatoni toping. &nbsp; <b>Жди меня́ здесь, пока́ я верну́сь.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>пока́ я <b>не</b>
    верну́сь</strong>. «Qaytgunimcha» maʼnosi uchun <em>пока́</em>
    dan keyin <b>не</b> kerak. <em>Не</em> siz gap «men qaytayotgan
    payt kut» degan boshqa maʼno beradi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Agar vaqtim boʻlganda edi, men ham kelardim.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Е́сли бы у меня́ бы́ло
    вре́мя, я бы то́же пришёл.</strong> «…boʻlganda edi» — noreal
    shart, demak <b>е́сли бы</b> va ikkala qismda ham oʻtgan
    zamon.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>е́сли</b><span>agar (real shart)</span></li>
  <li><b>е́сли бы</b><span>…boʻlganda edi (noreal shart)</span></li>
  <li><b>когда́</b><span>…ganda, qachonki</span></li>
  <li><b>то</b><span>u holda (ergash gap oldinda turganda)</span></li>
  <li><b>как то́лько</b><span>…ishi bilanoq</span></li>
  <li><b>пока́</b><span>…ekan, …ayotgan paytda</span></li>
  <li><b>пока́ не</b><span>…gunicha</span></li>
  <li><b>по́сле того́ как</b><span>…gandan keyin</span></li>
  <li><b>пе́ред тем как</b><span>…dan oldin</span></li>
  <li><b>раз</b><span>madomiki, shundoq ekan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Когда́</b> — albatta boʻladi (vaqt). <b>Е́сли</b> — boʻlmasligi
        ham mumkin (shart).</li>
    <li>Gap <b>kelajak</b> haqida boʻlsa — <b>ikkala qismda ham kelasi
        zamon</b>: <em>Е́сли бу́дет вре́мя, я приду́.</em></li>
    <li><b>Когда́ + НСВ</b> — bir vaqtda yoki takror.
        <b>Когда́ + СВ</b> — avval bu, keyin u.</li>
    <li><b>Е́сли бы</b> real shart bilan uchrashmaydi: <em>бы</em> bor
        boʻlsa, ikkala feʼl ham oʻtgan zamonda.</li>
    <li><b>Пока́ не</b> ichidagi <em>не</em> — inkor emas, qurilishning
        qismi.</li>
    <li>Ergash gap bilan asosiy gap orasida <b>har doim vergul</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-66: Потому что, поэтому, так как, из-за того что — sabab va natija",
        "category": "russian",
        "order": 66,
        "summary": (
            "Потому́ что sababni aytadi, поэ́тому natijani — bitta voqeaning ikki "
            "tomoni. Ustiga из-за + Р.п. (yomon sabab) va благодаря́ + Д.п. (yaxshi)."
        ),
        "stories": ["Почему́ Байка́л тако́й глубо́кий"],
        "content": """
<h2>PR-66: Потому что, поэтому, так как, из-за того что — sabab va natija</h2>

<p>Bitta voqeani ikki xil aytish mumkin: <em>«Kelmadim, <b>chunki</b> kasal
boʻldim»</em> va <em>«Kasal boʻldim, <b>shuning uchun</b> kelmadim»</em>.
Voqea bitta, gap ikkita. Rus tilida ham xuddi shunday — faqat bu ikki
soʻz bir-biriga juda oʻxshaydi va oʻquvchilar ularni doim adashtiradi:
<b>потому́ что</b> va <b>поэ́тому</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>Потому́ что</b> (sabab) bilan <b>поэ́тому</b> (natija) ni hech qachon adashtirmaysiz</li>
    <li>Vergulni <em>потому́</em> dan <b>oldin</b> qoʻyishni oʻrganasiz</li>
    <li><b>Так как</b> va <b>поско́льку</b> bilan gap boshlaysiz</li>
    <li><b>Из-за</b> + Р.п. va <b>благодаря́</b> + Д.п. ni ajratasiz</li>
    <li>Qaysi bogʻlovchi qaysi uslubga tegishli ekanini bilasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Sabab</span>
  <span class="pe-chip pe-chip--v">natija</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--s">потому́ что + sabab</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Natija</span>
  <span class="pe-chip pe-chip--s">sabab</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">поэ́тому + natija</span>
</div>

<h3>1. Oyna: bir voqea, ikki gap</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">ПОТОМУ́ ЧТО — chunki</p>
    <p><em>Я не пришёл, <b>потому́ что</b> заболе́л.</em><br>
       Kelmadim, <b>chunki</b> kasal boʻldim.</p>
    <p>Oldin <b>natija</b>, keyin <b>sabab</b>.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">ПОЭ́ТОМУ — shuning uchun</p>
    <p><em>Я заболе́л, <b>поэ́тому</b> не пришёл.</em><br>
       Kasal boʻldim, <b>shuning uchun</b> kelmadim.</p>
    <p>Oldin <b>sabab</b>, keyin <b>natija</b>.</p>
  </div>
</div>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Sabab bilan</th><th>Natija bilan</th></tr>
  <tr><td class="pr-res">Мы оста́лись до́ма, <b>потому́ что</b> шёл дождь.</td>
      <td class="pr-end">Шёл дождь, <b>поэ́тому</b> мы оста́лись до́ма.</td></tr>
  <tr><td class="pr-res">Афсо́на хорошо́ говори́т, <b>потому́ что</b> мно́го чита́ет.</td>
      <td class="pr-end">Афсо́на мно́го чита́ет, <b>поэ́тому</b> хорошо́ говори́т.</td></tr>
  <tr><td class="pr-res">Авто́бус не пришёл, <b>потому́ что</b> была́ ава́рия.</td>
      <td class="pr-end">Была́ ава́рия, <b>поэ́тому</b> авто́бус не пришёл.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Bitta savol yetarli</span>
Gapning <b>ikkinchi</b> qismiga qarang.<br><br>
U <b>«nega?»</b> degan savolga javob berayaptimi → <b>потому́ что</b>.<br>
U <b>«nima boʻldi?»</b> degan savolga javob berayaptimi → <b>поэ́тому</b>.</div>

<h3>2. Vergul qayerda?</h3>

<p><b>Vergul <em>потому́</em> dan oldin qoʻyiladi</b>, ikki soʻzning
orasiga emas:</p>

<div class="pe-ex">
  <p class="pe-ex__t">Odatdagi holat</p>
  <p class="pe-ex__ru">Он опозда́л<b>,</b> потому́ что проспа́л.</p>
  <p class="pe-ex__uz">U kechikdi, chunki uxlab qoldi.</p>
  <p class="pe-ex__why">Vergul butun bogʻlovchidan oldin — bu 99% holat.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">Natija tomondan</p>
  <p class="pe-ex__ru">У Бекзо́да не́ было интерне́та<b>,</b> поэ́тому он не сдал рабо́ту во́время.</p>
  <p class="pe-ex__uz">Bekzodda internet yoʻq edi, shuning uchun ishni vaqtida topshirmadi.</p>
  <p class="pe-ex__why"><b>Поэ́тому</b> dan oldin ham vergul turadi — u
     ikkita mustaqil gapni bogʻlaydi.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Nozik joy</span>
Vergulni <em>потому́</em> dan <b>keyin</b> ham qoʻyish mumkin — lekin
u holda maʼno oʻzgaradi va <em>потому́</em> taʼkidlanadi:<br><br>
<em>Он опозда́л не потому́<b>,</b> что проспа́л, а потому́<b>,</b> что
не́ было авто́буса.</em><br>
U uxlab qolgani uchun emas, avtobus boʻlmagani uchun kechikdi.<br><br>
Bu qurilish <em>не потому́…, а потому́…</em> bilan keladi. Boshqa
paytda vergulni har doim <b>oldiga</b> qoʻying.</div>

<h3>3. Так как va поско́льку — gap boshida</h3>

<p><em>Потому́ что</em> ning bitta cheklovi bor: u <b>gapni boshlay
olmaydi</b>. Sababni oldinga chiqarmoqchi boʻlsangiz — <b>так как</b>
yoki <b>поско́льку</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Sabab oldinda</p>
  <p class="pe-ex__ru"><b>Так как</b> бы́ло хо́лодно<b>,</b> мы оста́лись до́ма.</p>
  <p class="pe-ex__uz">Sovuq boʻlgani uchun uyda qoldik.</p>
  <p class="pe-ex__why"><s>Потому́ что бы́ло хо́лодно, мы оста́лись до́ма</s> — bunday yozilmaydi.</p>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha yordam beradi</span>
Oʻzbekchada sabab deyarli har doim <b>oldinda</b> turadi:
<em>Sovuq boʻl<b>gani uchun</b> uyda qoldik.</em> Yaʼni oʻzbekcha
tartib sizni toʻgʻridan-toʻgʻri <b>так как</b> ga olib keladi.<br><br>
Shuning uchun oddiy qoida: gapni oʻzbekcha oʻylab, sabab boshida
tursa — <b>так как</b> yozing; sababni oxiriga surmoqchi boʻlsangiz —
<b>потому́ что</b>.</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Bitta istisno</span>
<em>Потому́ что</em> gapni faqat bir holatda boshlaydi: <b>savolga
javob berganda</b>.<br><br>
— Почему́ ты не пришёл?<br>
— <b>Потому́ что</b> заболе́л.</div>

<h3>4. Из-за va благодаря́ — ot bilan keladigan sabab</h3>

<p>Yuqoridagilar <b>gap</b> bogʻlaydi. Ba'zan esa sabab bitta soʻz —
u holda bogʻlovchi emas, <b>predlog</b> kerak boʻladi.</p>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">ИЗ-ЗА + Роди́тельный</p>
    <p><em>из-за дожд<b>я́</b></em> — yomgʻir tufayli<br>
       <em>из-за боле́зн<b>и</b></em> — kasallik tufayli</p>
    <p>Natija <b>yomon</b>. Bu — ayb qoʻyish.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">БЛАГОДАРЯ́ + Да́тельный</p>
    <p><em>благодаря́ дру́г<b>у</b></em> — doʻst tufayli<br>
       <em>благодаря́ по́мощ<b>и</b></em> — yordam tufayli</p>
    <p>Natija <b>yaxshi</b>. Bu — minnatdorchilik.</p>
  </div>
</div>

<div class="pe-call pe-warn"><span class="pe-call__t">Ikki xato birdan</span>
<b>Благодаря́</b> — Да́тельный kelishigi, chunki soʻzning ichida
<em>«благодари́ть»</em> (rahmat aytmoq) turibdi, rahmat esa
<b>kimga?</b> aytiladi.<br><br>
<s>благодаря́ учи́теля</s> &nbsp;→&nbsp; <b>благодаря́ учи́телю</b><br>
<s>из-за дождю́</s> &nbsp;→&nbsp; <b>из-за дождя́</b><br><br>
Predloglar mavzusiga PR-83 da yana qaytamiz.</div>

<h3>5. Из-за того́ что — predlogning gap shakli</h3>

<p>Sabab bitta soʻz emas, butun gap boʻlsa, <em>из-за</em> ga
<b>того́ что</b> qoʻshiladi:</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Ot bilan</th><th>Gap bilan</th></tr>
  <tr><td class="pr-res">Из-за дождя́ мы не пошли́.</td>
      <td class="pr-end">Из-за того́ что шёл дождь, мы не пошли́.</td></tr>
  <tr><td class="pr-res">Из-за боле́зни он не сдал экза́мен.</td>
      <td class="pr-end">Из-за того́ что он заболе́л, он не сдал экза́мен.</td></tr>
  <tr><td class="pr-res">Благодаря́ учи́телю я по́нял те́му.</td>
      <td class="pr-end">Благодаря́ тому́ что учи́тель объясни́л, я по́нял те́му.</td></tr>
</table></div>

<h3>6. Uslub darajalari</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Bogʻlovchi</th><th>Uslub</th><th>Nima qiladi</th></tr>
  <tr><td class="pr-stem">потому́ что</td><td class="pr-uz">ogʻzaki + neytral</td>
      <td class="pr-res">sabab; gapni boshlamaydi</td></tr>
  <tr><td class="pr-stem">так как</td><td class="pr-uz">neytral</td>
      <td class="pr-res">sabab; gapni boshlaydi</td></tr>
  <tr><td class="pr-stem">поско́льку</td><td class="pr-uz">kitobiy</td>
      <td class="pr-res">sabab; koʻpincha gap boshida</td></tr>
  <tr><td class="pr-stem">из-за того́ что</td><td class="pr-uz">neytral</td>
      <td class="pr-res">salbiy sabab</td></tr>
  <tr><td class="pr-stem">поэ́тому</td><td class="pr-uz">hamma joyda</td>
      <td class="pr-res">natija</td></tr>
  <tr><td class="pr-stem">зна́чит</td><td class="pr-uz">ogʻzaki</td>
      <td class="pr-res">xulosa: «demak»</td></tr>
  <tr><td class="pr-stem">сле́довательно</td><td class="pr-uz">rasmiy / ilmiy</td>
      <td class="pr-res">xulosa: «binobarin»</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada sabab koʻpincha <b>qoʻshimcha</b> bilan beriladi:
<em>kasal boʻl<b>gani uchun</b></em>, <em>yomgʻir <b>tufayli</b></em>.
Ruschada esa har doim <b>alohida soʻz</b> qoʻyiladi va u gapni ikkiga
boʻladi.<br><br>
Foydali moslik:<br>
<em>chunki</em> &nbsp;→&nbsp; <b>потому́ что</b><br>
<em>…gani uchun</em> &nbsp;→&nbsp; <b>так как</b> yoki <b>из-за того́ что</b><br>
<em>shuning uchun</em> &nbsp;→&nbsp; <b>поэ́тому</b><br>
<em>tufayli</em> (yomon) &nbsp;→&nbsp; <b>из-за</b> + Р.п.<br>
<em>tufayli, sharofati bilan</em> (yaxshi) &nbsp;→&nbsp; <b>благодаря́</b> + Д.п.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Bitta soʻz, ikki qoʻshimcha</span>
<em>Потому́</em> va <em>поэ́тому</em> — ikkalasi ham bitta
<b>то</b> oʻzagidan. Farqni <b>bosh qismi</b> qiladi, va uni oʻzbekcha
orqali eslab qolish oson:<br><br>
<b>по-ЧЕМУ́?</b> — nega? &nbsp;→&nbsp; javobi <b>по-ТОМУ́ что</b> — chunki<br>
<b>по-ЭТОМУ</b> — «shu sababdan» &nbsp;→&nbsp; natija<br><br>
Yaʼni <em>потому́ что</em> savolga javob beradi, <em>поэ́тому</em> esa
xulosa chiqaradi.</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я заболе́л, потому́ что не пришёл.</s></p>
  <p class="pe-good">Я не пришёл, потому́ что <b>заболе́л</b> — sabab bogʻlovchidan keyin turadi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Поэ́тому что бы́ло хо́лодно, мы оста́лись до́ма.</s></p>
  <p class="pe-good"><b>Так как</b> бы́ло хо́лодно… — «поэ́тому что» degan bogʻlovchi yoʻq</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Из-за по́мощи дру́га я сдал экза́мен.</s></p>
  <p class="pe-good"><b>Благодаря́</b> по́мощи дру́га… — natija yaxshi</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Мы не пошли́ потому́ что бы́ло по́здно.</s></p>
  <p class="pe-good">Мы не пошли́<b>,</b> потому́ что бы́ло по́здно — vergul majburiy</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>Потому́ что</b> yoki <b>поэ́тому</b>? &nbsp;
     <b>Бы́ло по́здно, ___ мы вы́звали такси́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>поэ́тому</strong>. Birinchi qism
    — sabab (kech edi), ikkinchisi — <b>natija</b> (taksi chaqirdik).</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Xuddi shu fikrni teskarisidan ayting.<br>
     <b>Шёл дождь, поэ́тому матч отмени́ли.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Матч отмени́ли, потому́ что
    шёл дождь.</strong> Natija oldinga, sabab orqaga — oyna
    aylantirildi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Toʻgʻri shaklni qoʻying. &nbsp; <b>Благодаря́ ___ я нашёл рабо́ту.</b>
     (Ше́рбек)</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Ше́рбеку</strong> —
    <b>Да́тельный</b>. <em>Благодаря́</em> har doim «kimga?»
    kelishigini oladi, chunki uning ichida «rahmat aytmoq»
    turibdi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     <b>Из-за</b> yoki <b>благодаря́</b>? &nbsp;
     <b>___ снегопа́да аэропо́рт закры́ли.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Из-за снегопа́да</strong>.
    Aeroport yopilishi — yomon natija, demak <em>из-за</em> +
    <b>Роди́тельный</b>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring, sababni <b>oldinga</b> qoʻying.<br>
     <b>Kutubxona yopiq boʻlgani uchun uyda ishladik.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Так как библиоте́ка была́
    закры́та, мы рабо́тали до́ма.</strong> Sabab oldinda turgani uchun
    <em>потому́ что</em> ishlamaydi — <b>так как</b> yoki
    <b>поско́льку</b> kerak.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>потому́ что</b><span>chunki</span></li>
  <li><b>поэ́тому</b><span>shuning uchun</span></li>
  <li><b>так как</b><span>…gani uchun (gap boshida)</span></li>
  <li><b>поско́льку</b><span>madomiki (kitobiy)</span></li>
  <li><b>из-за</b> + Р.п.<span>tufayli (yomon natija)</span></li>
  <li><b>благодаря́</b> + Д.п.<span>tufayli, sharofati bilan (yaxshi)</span></li>
  <li><b>из-за того́ что</b><span>…gani sababli</span></li>
  <li><b>зна́чит</b><span>demak</span></li>
  <li><b>сле́довательно</b><span>binobarin (rasmiy)</span></li>
  <li><b>причи́на</b><span>sabab</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li><b>Потому́ что</b> = sabab, <b>поэ́тому</b> = natija. Bir voqea,
        ikki gap.</li>
    <li>Vergul <b>потому́ dan oldin</b>: <em>Он опозда́л, потому́
        что…</em></li>
    <li><b>Потому́ что</b> gapni boshlamaydi (savolga javobdan tashqari).
        Buning uchun <b>так как</b> yoki <b>поско́льку</b>.</li>
    <li><b>Из-за</b> + Роди́тельный — yomon sabab.
        <b>Благодаря́</b> + Да́тельный — yaxshi sabab.</li>
    <li>Sabab butun gap boʻlsa: <b>из-за того́ что</b> / <b>благодаря́
        тому́ что</b>.</li>
    <li><b>«Поэ́тому что»</b> degan bogʻlovchi rus tilida <b>yoʻq</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PR-67: Хотя, но, зато, однако, тем не менее — qarama-qarshilik",
        "category": "russian",
        "order": 67,
        "summary": (
            "Oʻzbekcha «esa» — ruscha А, «lekin» — ruscha НО. Ustiga зато́ (kamchilik "
            "oʻrnini bosadigan yaxshilik), хотя́, одна́ко va тем не ме́нее."
        ),
        "stories": ["Ма́ленький го́род, больша́я библиоте́ка"],
        "content": """
<h2>PR-67: Хотя, но, зато, однако, тем не менее — qarama-qarshilik</h2>

<p><em>«Kvartira kichkina, <b>lekin</b> arzon.»</em> Oʻzbekchada bitta
soʻz — <em>lekin</em>. Ruschada esa bu oʻrinda kamida <b>beshta</b>
turli soʻz turishi mumkin, va ular bir-birining oʻrnini bosa olmaydi.
Eng koʻp xato esa eng oddiy joyda: <b>а</b> bilan <b>но</b> ni
adashtirishda.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsda siz</p>
  <ul>
    <li><b>А</b> bilan <b>но</b> ni ajratasiz — bu darsning eng muhim qismi</li>
    <li><b>Зато́</b> ni ishlata olasiz (oʻzbekchada bitta soʻzli tarjimasi yoʻq)</li>
    <li><b>Хотя́</b> bilan gap boshlaysiz</li>
    <li><b>Одна́ко</b> va <b>тем не ме́нее</b> ni yozma matnda ishlatasiz</li>
    <li>Har birining oldiga vergul qoʻyishni eslab qolasiz</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Solishtirish</span>
  <span class="pe-chip pe-chip--s">gap 1</span>
  <span class="pe-op">, а</span>
  <span class="pe-chip pe-chip--o">gap 2</span>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Kutilganga zid</span>
  <span class="pe-chip pe-chip--s">gap 1</span>
  <span class="pe-op">, но</span>
  <span class="pe-chip pe-chip--neg">gap 2</span>
</div>

<h3>1. А va но — darsning yuragi</h3>

<div class="pe-vs">
  <div class="pe-vs__side">
    <p class="pe-vs__h">А — solishtirish</p>
    <p><em>Я люблю́ ко́фе, <b>а</b> Жасу́р лю́бит чай.</em><br>
       Men qahvani yaxshi koʻraman, Jasur <b>esa</b> choyni.</p>
    <p>Ikkala gap ham toʻgʻri. Ular shunchaki <b>boshqa-boshqa</b>.
       Hech qanday zidlik yoʻq.</p>
  </div>
  <div class="pe-vs__side">
    <p class="pe-vs__h">НО — kutilganga zid</p>
    <p><em>Я люблю́ ко́фе, <b>но</b> сего́дня пью чай.</em><br>
       Qahvani yaxshi koʻraman, <b>lekin</b> bugun choy ichyapman.</p>
    <p>Birinchi qismdan keyin siz boshqa narsani kutgan edingiz —
       ikkinchi qism uni <b>buzadi</b>.</p>
  </div>
</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha — bu darsning kaliti</span>
Bu yerda oʻzbek tili sizga tayyor javob beradi. Gapni oʻzbekchada
ayting va qaysi soʻz tabiiy chiqishiga qarang:<br><br>
<em>…, u <b>esa</b> …</em> &nbsp;→&nbsp; <b>а</b><br>
<em>…, <b>lekin</b> / <b>ammo</b> …</em> &nbsp;→&nbsp; <b>но</b><br><br>
<em>Men Toshkentda yashayman, akam <b>esa</b> Samarqandda.</em><br>
→ Я живу́ в Ташке́нте, <b>а</b> брат — в Самарка́нде.<br><br>
<em>Men Toshkentda yashayman, <b>lekin</b> shaharni yaxshi bilmayman.</em><br>
→ Я живу́ в Ташке́нте, <b>но</b> пло́хо зна́ю го́род.</div>

<div class="pe-ex">
  <p class="pe-ex__t">Uchta yonma-yon</p>
  <p class="pe-ex__ru">Дилно́за — врач, <b>а</b> её сестра́ — учи́тель.</p>
  <p class="pe-ex__uz">Dilnoza shifokor, singlisi esa oʻqituvchi. — Solishtirish.</p>
  <p class="pe-ex__ru">Дилно́за — врач, <b>но</b> она́ бои́тся кро́ви.</p>
  <p class="pe-ex__uz">Dilnoza shifokor, lekin qondan qoʻrqadi. — Kutilmagan.</p>
  <p class="pe-ex__ru">Дилно́за — врач, <b>и</b> она́ лю́бит свою́ рабо́ту.</p>
  <p class="pe-ex__uz">Dilnoza shifokor va ishini yaxshi koʻradi. — Qoʻshimcha.</p>
</div>

<h3>2. Зато́ — kamchilikning oʻrnini bosadigan yaxshilik</h3>

<p>Bu rus tilining eng qulay soʻzlaridan biri, va oʻzbekchada uning
bitta soʻzli tarjimasi <b>yoʻq</b>. <em>Зато́</em> degani: «rost,
buning kamchiligi bor — <b>lekin buning evaziga</b> mana bu yaxshi
tomoni bor».</p>

<div class="pe-formula">
  <span class="pe-formula__label">Doim shu tartibda</span>
  <span class="pe-chip pe-chip--neg">minus</span>
  <span class="pe-op">, зато́</span>
  <span class="pe-chip pe-chip--s">plus</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__t">Зато́</p>
  <p class="pe-ex__ru">Кварти́ра ма́ленькая, <b>зато́</b> дешёвая.</p>
  <p class="pe-ex__uz">Kvartira kichkina, buning evaziga arzon.</p>
  <p class="pe-ex__ru">Доро́га дли́нная, <b>зато́</b> краси́вая.</p>
  <p class="pe-ex__uz">Yoʻl uzoq, buning oʻrniga chiroyli.</p>
  <p class="pe-ex__ru">Я не сдал на «пять», <b>зато́</b> я всё по́нял.</p>
  <p class="pe-ex__uz">«Besh» ololmadim, lekin buning oʻrniga hammasini tushundim.</p>
</div>

<div class="pe-call pe-rule"><span class="pe-call__t">Tartib buzilmaydi</span>
<b>Зато́</b> dan keyin har doim <b>ijobiy</b> tomon keladi. Teskarisi
— <em>«Кварти́ра больша́я, зато́ дорога́я»</em> — grammatik jihatdan
mumkin, lekin bu <b>kinoya</b> boʻlib eshitiladi. Oddiy gapda plusni
oxiriga qoʻying.</div>

<div class="pe-call pe-uz"><span class="pe-call__t">Nega bu soʻz qiyin</span>
Oʻzbekchada <em>зато́</em> ga <b>bitta soʻz</b> toʻgʻri kelmaydi —
butun ibora kerak: <em>«buning evaziga»</em>, <em>«buning
oʻrniga»</em>, <em>«ammo shuning oʻrniga»</em>. Aynan shuning uchun
oʻzbek oʻquvchisi <em>зато́</em> ni <b>deyarli ishlatmaydi</b> va
hamma joyda <em>но</em> deb qoʻya qoladi.<br><br>
Lekin rus tilida bu soʻz juda tez-tez ishlatiladi va nutqni birdan
tabiiy qiladi. Qoida oddiy: <b>kamchilikni tan olib, keyin uning
oʻrnini bosadigan yaxshilikni aytsangiz — <em>но</em> emas,
<em>зато́</em>.</b></div>

<h3>3. Хотя́ — «garchi …sa ham»</h3>

<p><em>Хотя́</em> ikki joyda tura oladi: gap boshida ham, oʻrtasida
ham. Maʼnosi oʻzgarmaydi.</p>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Oʻrni</th><th>Misol</th><th>Oʻzbekcha</th></tr>
  <tr><td class="pr-uz">gap boshida</td>
      <td class="pr-res"><b>Хотя́</b> бы́ло по́здно, мы пошли́ гуля́ть.</td>
      <td class="pr-end">Kech boʻlsa ham, sayr qilgani chiqdik.</td></tr>
  <tr><td class="pr-uz">oʻrtada</td>
      <td class="pr-res">Мы пошли́ гуля́ть, <b>хотя́</b> бы́ло по́здно.</td>
      <td class="pr-end">Sayr qilgani chiqdik, garchi kech boʻlsa ham.</td></tr>
  <tr><td class="pr-uz">но bilan</td>
      <td class="pr-res"><b>Хотя́</b> бы́ло по́здно, <b>но</b> мы всё же пошли́.</td>
      <td class="pr-end">Kech boʻlsa ham, baribir chiqdik.</td></tr>
</table></div>

<div class="pe-call pe-uz"><span class="pe-call__t">Oʻzbekcha</span>
Oʻzbekchada bu qurilish <b>juftlashgan</b>: <em>garchi …-sa
<b>ham</b></em>. Ikki tomonda ikki belgi turadi.<br><br>
Ruschada esa <b>хотя́ ning oʻzi yetarli</b> — asosiy gapda hech narsa
kerak emas.<br><br>
Lekin diqqat: koʻpchilik tillardan farqli oʻlaroq, rus tilida
<em>хотя́ …, но …</em> yoki <em>хотя́ …, всё же …</em> deb ikkalasini
birga ishlatish ham <b>xato emas</b>. Bu adabiy meʼyorda bor va
oʻzbekcha juftlikka juda oʻxshaydi.</div>

<div class="pe-call pe-tip"><span class="pe-call__t">Хотя́ бы — boshqa soʻz</span>
<b>Хотя́ бы</b> = «hech boʻlmaganda», bogʻlovchi emas:<br><br>
<em>Позвони́ <b>хотя́ бы</b> ве́чером.</em> — Hech boʻlmaganda kechqurun
qoʻngʻiroq qil.<br>
<em>Дай мне <b>хотя́ бы</b> оди́н день.</em> — Menga hech boʻlmaganda
bir kun ber.</div>

<h3>4. Одна́ко va тем не ме́нее — yozma uslub</h3>

<div class="pe-table-wrap"><table class="pr-decl">
  <tr><th>Soʻz</th><th>Uslub</th><th>Misol</th></tr>
  <tr><td class="pr-stem">но</td><td class="pr-uz">neytral, hamma joyda</td>
      <td class="pr-res">Бы́ло тру́дно, но интере́сно.</td></tr>
  <tr><td class="pr-stem">а</td><td class="pr-uz">neytral, solishtirish</td>
      <td class="pr-res">Я чита́ю, а он пи́шет.</td></tr>
  <tr><td class="pr-stem">зато́</td><td class="pr-uz">ogʻzaki, iliq</td>
      <td class="pr-res">До́лго, зато́ надёжно.</td></tr>
  <tr><td class="pr-stem">хотя́</td><td class="pr-uz">neytral</td>
      <td class="pr-res">Хотя́ он уста́л, он продолжа́л.</td></tr>
  <tr><td class="pr-stem">одна́ко</td><td class="pr-uz">kitobiy, yozma</td>
      <td class="pr-res">Одна́ко реше́ние бы́ло при́нято.</td></tr>
  <tr><td class="pr-stem">тем не ме́нее</td><td class="pr-uz">rasmiy</td>
      <td class="pr-res">Он оши́бся; тем не ме́нее рабо́та хоро́шая.</td></tr>
  <tr><td class="pr-stem">всё-таки</td><td class="pr-uz">ogʻzaki, taʼkid</td>
      <td class="pr-res">Он всё-таки пришёл.</td></tr>
</table></div>

<div class="pe-call pe-tip"><span class="pe-call__t">Одна́ко ning ikki oʻrni</span>
Gap boshida <em>одна́ко</em> — «shunga qaramay»:
<em><b>Одна́ко</b> никто́ не согласи́лся.</em><br><br>
Gap oʻrtasida esa u <b>но</b> ning kitobiy varianti:
<em>Он обеща́л прийти́, <b>одна́ко</b> не пришёл.</em><br><br>
Ogʻzaki nutqda <em>одна́ко</em> deyish gʻalati eshitiladi — u yerda
<b>но</b> deng.</div>

<h3>5. Vergul</h3>

<p>Qoida qisqa: <b>а, но, зато́, одна́ко, хотя́</b> — hammasining
<b>oldiga vergul</b> qoʻyiladi.</p>

<div class="pe-ex">
  <p class="pe-ex__t">Hammasi bir joyda</p>
  <p class="pe-ex__ru">Дом ста́рый<b>,</b> но кре́пкий. · Го́род ма́ленький<b>,</b>
     зато́ ти́хий. · Мы пошли́<b>,</b> хотя́ бы́ло по́здно.</p>
  <p class="pe-ex__uz">Uy eski, lekin mustahkam. · Shahar kichik, buning
     evaziga tinch. · Kech boʻlsa ham bordik.</p>
</div>

<h3>Koʻp uchraydigan xatolar</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Я люблю́ ко́фе, но Жасу́р лю́бит чай.</s></p>
  <p class="pe-good">Я люблю́ ко́фе, <b>а</b> Жасу́р лю́бит чай — bu solishtirish, zidlik emas</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Я хоте́л пойти́, а не смог.</s></p>
  <p class="pe-good">Я хоте́л пойти́, <b>но</b> не смог — kutilganga zid</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Кварти́ра ма́ленькая, зато́ ста́рая.</s></p>
  <p class="pe-good">Кварти́ра ма́ленькая, зато́ <b>дешёвая</b> — зато́ dan keyin ijobiy tomon</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Хотя́ бы́ло по́здно мы пошли́ гуля́ть.</s></p>
  <p class="pe-good">Хотя́ бы́ло по́здно<b>,</b> мы пошли́ гуля́ть — vergul majburiy</p>
</div>

<h3>Mashq</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     <b>А</b> yoki <b>но</b>? &nbsp; <b>Афсо́на живёт в Ташке́нте,
     ___ Ше́рбек — в Бухаре́.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>а</strong>. Ikkala gap ham
    toʻgʻri, ular shunchaki solishtirilyapti. Oʻzbekchada
    «Sherbek <b>esa</b> Buxoroda» — demak <em>а</em>.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     <b>А</b> yoki <b>но</b>? &nbsp; <b>Он до́лго учи́лся, ___ экза́мен
     не сдал.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>но</strong>. Uzoq oʻqigan
    odam imtihondan oʻtishi <b>kutiladi</b> — ikkinchi qism shu
    kutishni buzyapti.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Gapni <b>зато́</b> bilan tugating.<br>
     <b>Э́тот телефо́н не о́чень краси́вый, зато́ ___.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p>Masalan: <strong>…зато́ он
    дешёвый</strong> / <strong>…зато́ он до́лго рабо́тает</strong>.
    <em>Зато́</em> dan keyin <b>albatta ijobiy</b> tomon kelishi
    kerak.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Bu gapni <b>хотя́</b> ni gap boshiga chiqarib qayta yozing.<br>
     <b>Мы пошли́ на ры́нок, хотя́ шёл дождь.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Хотя́ шёл дождь, мы пошли́ на
    ры́нок.</strong> Vergul endi oʻrtada turadi. Maʼno umuman
    oʻzgarmadi.</p></div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Bu gapni ruschaga oʻgiring.<br>
     <b>Shahar kichkina, lekin buning evaziga u yerda tinch.</b></p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
    <div class="pe-reveal__a"><p><strong>Го́род ма́ленький, зато́
    там ти́хо.</strong> «Buning evaziga» — bu aynan <em>зато́</em>.
    Faqat <em>но</em> deyilsa, kompensatsiya maʼnosi
    yoʻqoladi.</p></div>
  </details>
</div>

<h3>Kalit soʻzlar</h3>

<ul class="pe-gloss">
  <li><b>а</b><span>…esa (solishtirish)</span></li>
  <li><b>но</b><span>lekin, ammo</span></li>
  <li><b>зато́</b><span>buning evaziga, buning oʻrniga</span></li>
  <li><b>хотя́</b><span>garchi …sa ham</span></li>
  <li><b>хотя́ бы</b><span>hech boʻlmaganda</span></li>
  <li><b>одна́ко</b><span>shunga qaramay (kitobiy)</span></li>
  <li><b>тем не ме́нее</b><span>shunga qaramasdan (rasmiy)</span></li>
  <li><b>всё-таки</b><span>baribir, shunday boʻlsa ham</span></li>
  <li><b>всё же</b><span>baribir</span></li>
  <li><b>надёжный</b><span>ishonchli, mustahkam</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Esda qoladigan narsa</p>
  <ul>
    <li>Oʻzbekcha <b>«esa»</b> → <b>а</b>. Oʻzbekcha <b>«lekin»</b> →
        <b>но</b>. Bu bitta sinov butun darsni hal qiladi.</li>
    <li><b>Зато́</b>: avval minus, keyin <b>albatta plus</b>.
        <em>Ма́ленькая, зато́ дешёвая.</em></li>
    <li><b>Хотя́</b> gap boshida ham, oʻrtasida ham tura oladi; asosiy
        gapda <em>но / всё же</em> boʻlishi ham mumkin.</li>
    <li><b>Хотя́ бы</b> — bogʻlovchi emas, «hech boʻlmaganda».</li>
    <li><b>Одна́ко</b> va <b>тем не ме́нее</b> — yozma va rasmiy matn
        uchun; ogʻzaki nutqda <b>но</b>.</li>
    <li>Hammasining <b>oldiga vergul</b>.</li>
  </ul>
</div>
""",
    },
]
